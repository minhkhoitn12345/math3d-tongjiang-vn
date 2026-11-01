"""Apply reviewable Vietnamese edits to the copied Tongjiang HTML bundles.

Run from the project root with ``python tools/localize.py``. This only changes
our copy under courses/; the original source directory is never modified.
"""
from __future__ import annotations

import codecs
import html
import json
import re
from pathlib import Path

from guided_vi import GUIDED, OUTCOMES
from panel_vi import PANEL_VI
from full_ui_vi import QUIZZES, UNITS, PLATES, DETAILS, LAYERS, TOAST

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "courses"
CATALOG = {row["slug"]: row for row in json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))}

LESSONS = {
    "projectile-step": {
        "title": "Khám phá chuyển động ném ngang",
        "question": "Từ máng phóng và tấm chắn, làm sao tách chuyển động ngang và rơi tự do để tìm vận tốc ban đầu?",
        "steps": ["Làm quen dụng cụ", "Xét chuyển động thẳng đứng", "Chỉnh đầu máng nằm ngang", "Ghi bốn vị trí", "Xác định khoảng thời gian", "Chuyển động ngang đều", "Thay vị trí thả", "Hai nguồn sai số", "Tự kiểm tra"],
        "summary": "Tách một chuyển động thành hai phương độc lập: x = v₀t, y = ½gt².",
    },
    "centripetal-step": {
        "title": "Lực hướng tâm: khối lượng, bán kính, tốc độ góc",
        "question": "Dùng hai thước đo trên máy quay để suy ra lực hướng tâm phụ thuộc vào m, r và ω như thế nào?",
        "steps": ["Làm quen máy quay", "Kiểm tra thiết bị", "Thay khối lượng", "Thay bán kính", "Thay tốc độ góc", "Ghép thành công thức", "Sai số và thao tác sai", "Tự kiểm tra: ω bình phương"],
        "summary": "Giữ cố định hai đại lượng, thay đại lượng còn lại để tìm F = mω²r.",
    },
    "accel-force-step": {
        "title": "Gia tốc, lực và khối lượng",
        "question": "Từ băng giấy và các quả cân, làm sao tìm được quan hệ giữa gia tốc, lực và khối lượng?",
        "steps": ["Làm quen dụng cụ", "Bù lực cản", "Ghi băng giấy", "Tính gia tốc", "Quan hệ a và F", "Quan hệ a và m", "Phân tích sai số", "Tự kiểm tra"],
        "summary": "Điều khiển từng biến, đo gia tốc trên băng giấy và kiểm chứng a = F/m.",
    },
    "energy-step": {
        "title": "Kiểm chứng định luật bảo toàn cơ năng",
        "question": "Khi vật rơi, thế năng giảm có chuyển hết thành động năng tăng không? Băng giấy giúp kiểm chứng ra sao?",
        "steps": ["Làm quen dụng cụ", "Bật máy rồi thả vật", "Chọn các điểm đo", "Đo h và tính v", "Ghi số liệu, vẽ đồ thị", "Thay vật nặng", "Phân tích sai số", "Tự kiểm tra"],
        "summary": "So sánh gh với ½v², rồi giải thích phần chênh lệch do lực cản.",
    },
    "brownian-step": {
        "title": "Chuyển động Brown và khuếch tán",
        "question": "Không nhìn thấy phân tử, ta có thể tìm dấu vết chuyển động hỗn loạn của chúng bằng cách nào?",
        "steps": ["Quan sát hạt chuyển động", "Ghi một điểm mỗi 30 giây", "So sánh quãng đi và độ dời", "Thay kích thước hạt", "Thay nhiệt độ", "Giải thích va chạm", "Một lần khác với thống kê", "Quan sát khuếch tán", "Tự kiểm tra"],
        "summary": "Theo dõi nhiều lần thử để phân biệt đường đi ngẫu nhiên với quy luật thống kê.",
    },
    "river-step": {
        "title": "Dòng sông tạo nên địa hình",
        "question": "Vì sao bờ sông ở một khúc uốn có thể dịch chuyển theo thời gian?",
        "steps": ["Quan sát sa bàn", "Thung lũng chữ V", "Mặt cắt thung lũng", "Quạt bồi tích", "Bờ lõm và bờ lồi", "Bãi bồi ven sông", "Đồng bằng châu thổ", "Tự kiểm tra: mùa lũ"],
        "summary": "Quan sát độ dốc, vận tốc dòng chảy, xói mòn và bồi tụ trên sa bàn 3D.",
    },
}

# Shared controls and status labels in every bundled lesson. Exact-string
# replacement leaves the bundled Three.js code and formulas untouched.
COMMON = {
    "目录": "Mục lục", "回到课程目录（学习进度会自动保存）": "Về danh sách bài học (tiến độ được lưu tự động)",
    "检测": "Kiểm tra", "玩法": "Cách dùng", "全屏": "Toàn màn hình", "设备名": "Tên dụng cụ",
    "运行中": "Đang chạy", "已停车": "Đã dừng", "报警": "Cảnh báo", "事故": "Sự cố",
    "得分": "Điểm", "主线问题": "Câu hỏi chính", "因果链": "Chuỗi nguyên nhân", "步骤": "Bước",
    "本步": "Bước này", "问句 → 动手 → 结论 + 要点 + 考点": "Câu hỏi → Thử nghiệm → Kết luận",
    "收起": "Thu gọn", "方程式 · 条件": "Công thức · Điều kiện", "动手试一试": "Thử ngay",
    "应该看到": "Quan sát dự kiến", "关键结论": "Kết luận chính", "要点": "Điểm cần nhớ",
    "考点提示": "Gợi ý ôn tập", "流程": "Tiến trình", "整体": "Toàn cảnh",
    "揭示结论": "Xem kết luận", "结论已揭示": "Đã xem kết luận", "复位本步": "Đặt lại bước này",
    "做过了": "Đã làm", "还没做": "Chưa làm", "依据": "Căn cứ",
    "‹ 上一步": "‹ Bước trước", "下一步 ›": "Bước tiếp ›",
    "中控台": "Bảng điều khiển", "拖一个滑块，看全局的代价": "Kéo thanh trượt để quan sát tác động",
    "← 回控制台": "← Về bảng điều khiển", "量程": "Phạm vi", "教材": "Tài liệu",
    "参考": "Tham khảo", "参考工况": "Thiết lập mẫu", "开车": "Bắt đầu", "停车": "Dừng",
    "课件设定": "Thiết lập bài học", "达标": "Đạt mục tiêu", "未达标": "Chưa đạt",
    "实验记录": "Nhật ký thí nghiệm", "记录一组": "Ghi một lượt", "还没有记录": "Chưa có dữ liệu",
    "这一组已经记过了": "Đã ghi lượt này", "现在读数不稳，等一下再记": "Số đo chưa ổn định, hãy đợi rồi ghi",
    "随堂检测": "Kiểm tra nhanh", "下一题": "Câu tiếp", "完成": "Hoàn thành",
    "答对了": "Đúng rồi", "再想想": "Hãy thử lại", "解析": "Giải thích",
    "检测结果": "Kết quả", "再做一次": "Làm lại", "关闭": "Đóng",
    "回看主线": "Xem lại bài", "全对！": "Đúng tất cả!", "玩法与快捷键": "Cách dùng và phím tắt",
    "知道了": "Đã hiểu", "已回到参考工况": "Đã về thiết lập mẫu",
    "已停车": "Đã dừng", "原理与现象": "Nguyên lý và hiện tượng", "物理": "Vật lý", "高中地理": "Địa lý",
    "考核": "Tự kiểm tra", "认识器材": "Làm quen dụng cụ", "认识演示器": "Làm quen máy quay",
    "结论": "Kết luận", "控制变量": "Giữ cố định các biến", "误差": "Sai số",
    "实验台": "Bàn thí nghiệm", "实验": "Thí nghiệm", "观察台": "Bàn quan sát", "河流地貌": "Địa hình sông",
    "跳到第 n 步": "Đi tới bước số n",
}

EXTRA = {
    "projectile-step": {
        "整体 · 参考案例的装置": "Toàn cảnh · bộ dụng cụ mẫu",
        "只靠一只斜槽和一块挡板，能不能把平抛拆成两个分运动、量出初速度？": "Từ máng phóng và tấm chắn, làm sao tách chuyển động ngang và rơi tự do để tìm vận tốc ban đầu?",
        "平抛拆成水平与竖直两个分运动，先做竖直（参考案例 步骤1）": "Tách ném ngang thành chuyển động ngang và thẳng đứng; quan sát phương đứng trước.",
        "两球同时落地 ⟹ 竖直分运动是自由落体；等时点的 y 比 1 : 4 : 9 : 16": "Hai viên bi chạm đất cùng lúc: phương đứng là rơi tự do; độ rơi ở các thời điểm đều cách nhau theo tỉ lệ 1 : 4 : 9 : 16.",
        "由 y = ½gt² 反推「相等的时间间隔」T = 0.0639 s——桌上没有计时器": "Từ y = ½gt², suy ra khoảng thời gian bằng nhau T = 0,0639 s dù không có đồng hồ.",
        "相等时间内 x 比 1 : 2 : 3 : 4、Δx 恒定 ⟹ 水平分运动是匀速直线运动": "Trong những khoảng thời gian bằng nhau, x theo tỉ lệ 1 : 2 : 3 : 4; Δx không đổi nên chuyển động ngang là đều.",
        "v₀ = x√(g/2y)，四点落在同一条 y = kx² 上；k 只由 v₀ 决定": "v₀ = x√(g/2y); bốn điểm nằm trên cùng parabol y = kx² và k phụ thuộc v₀.",
        "斜槽与钢球": "Máng nghiêng và viên bi", "竖直分运动比对": "So sánh chuyển động thẳng đứng", "描迹背板与挡板": "Tấm ghi dấu và chắn", "方格纸与频闪照片": "Giấy ô và ảnh nhấp nháy",
    },
    "centripetal-step": {
        "整体 · 一台演示器": "Toàn cảnh · máy quay mẫu",
        "挡板压力 → 横臂杠杆 → 套筒下降 → 标尺露出红白格（一格一格地数）": "Áp lực lên tấm chắn truyền qua tay đòn; ống trượt hạ xuống và thước lộ các vạch đỏ trắng.",
        "这台手摇的演示器只给你两个标尺上的格数——能不能用它把 F 与 m、r、ω 的定量关系量出来？": "Từ số vạch trên hai thước của máy quay, bạn có thể tìm quan hệ định lượng giữa F, m, r và ω không?",
        "手柄 → 塔轮 → 皮带 → 转盘：两球同速转，或按皮带档倍速转": "Tay quay → ròng rọc → dây đai → đĩa quay: hai viên bi quay cùng tốc độ hoặc theo tỉ số dây đai.",
        "一次只动 m、r、ω 中的一个，其余两个锁死（控制变量）": "Mỗi lần chỉ thay một trong m, r, ω và giữ cố định hai đại lượng còn lại.",
        "两标尺格数相除 = 两球向心力之比（教材说「粗略」）": "Tỉ số vạch trên hai thước xấp xỉ tỉ số lực hướng tâm tác dụng lên hai viên bi.",
        "三条过原点的直线 → Fn = mω²r = m v²/r": "Ba quan hệ đi qua gốc tọa độ dẫn tới F = mω²r = mv²/r.",
        "变成格数": "Đổi thành số vạch", "只改一个": "Chỉ đổi một biến", "读比值": "Đọc tỉ số", "得结论": "Rút ra kết luận",
    },
    "accel-force-step": {
        "整体 · 参考案例 1 的装置": "Toàn cảnh · bộ dụng cụ mẫu 1",
        "不直接测力、也不直接测加速度——一张纸带加几个槽码，能不能把 a 与 F、m 的关系量出来？": "Từ băng giấy và các quả cân, làm sao đo được quan hệ giữa gia tốc a, lực F và khối lượng m?",
        "垫高木板，重力沿板分量抵消摩擦：点距变等距（Δx = 0.00 mm）": "Nâng tấm ván để thành phần trọng lực cân bằng ma sát; khoảng cách giữa các chấm trở nên đều.",
        "先通电、后放车，纸带记下 4 段间距 x₁…x₄": "Bật máy trước, thả xe sau; băng giấy ghi bốn quãng x₁…x₄.",
        "间距 → 速度 vₙ → v–t 图斜率 = a": "Từ khoảng cách giữa chấm suy ra vận tốc; độ dốc đồ thị v–t chính là a.",
        "只改槽码个数（a–F）／只改车上砝码块（a–1/m）": "Chỉ thay số quả cân kéo xe để xét a–F; chỉ thay khối lượng trên xe để xét a–1/m.",
        "两条过原点的直线：a ∝ F、a ∝ 1/m；斜率是 1/m 与 F": "Hai quan hệ tuyến tính qua gốc: a ∝ F và a ∝ 1/m; từ đó a = F/m.",
        "平衡": "Cân bằng", "打点": "Ghi chấm", "求 a": "Tính a",
    },
    "energy-step": {
        "整体 · 参考案例 1 的装置": "Toàn cảnh · bộ dụng cụ mẫu 1",
        "重物下落时，减少的重力势能是不是正好变成了增加的动能？一条纸带能不能把这件事量出来？": "Khi vật rơi, thế năng giảm có chuyển hết thành động năng tăng không? Dùng băng giấy để đo.",
        "只有重力做功（纸带竖直、限位孔对齐），机械能才守恒": "Khi chỉ có trọng lực sinh công, cơ năng mới bảo toàn; hãy giữ băng giấy thẳng và giảm lực cản.",
        "先接通电源、后释放重物，纸带记下 O、A、B、C 一串点": "Bật máy trước rồi thả vật; băng giấy ghi các vị trí O, A, B, C.",
        "中间时刻的速度 = 这段的平均速度：v_B = (h_C − h_A)/(2T)": "Vận tốc tại B xấp xỉ vận tốc trung bình từ A đến C: v_B = (h_C − h_A)/(2T).",
        "½v² 与 gh 直接比 —— 消掉质量，两条腿都从纸带量出来": "So sánh trực tiếp ½v² với gh; cả hai đều đo được từ băng giấy và không cần khối lượng.",
        "½v²–h 过原点、斜率 ≈ g；差值来自阻力：ΔEp 略大于 ΔEk": "Đồ thị ½v²–h gần qua gốc, độ dốc gần g; lực cản làm thế năng giảm nhiều hơn động năng tăng.",
        "条件": "Điều kiện", "测 v": "Đo v", "比能": "So sánh năng lượng",
    },
    "brownian-step": {
        "整体 · 显微镜 + 坐标纸 + 放大视窗 + 扩散槽": "Toàn cảnh · kính hiển vi, giấy ô, khung phóng đại và bể khuếch tán",
        "看不见的分子，凭什么说它在乱动？": "Không nhìn thấy phân tử, làm sao biết chúng chuyển động hỗn loạn?",
        "显微镜下，悬浮的小炭粒在自己的位置附近无规则游走": "Dưới kính hiển vi, hạt nhỏ lơ lửng di chuyển không theo hướng cố định.",
        "每 30 s 记一个点，连成的折线不是它的真实路径": "Cứ 30 giây ghi một vị trí; đường nối các điểm chỉ là bản ghi mẫu, không phải đường đi thật.",
        "液体分子四面撞它、撞击不平衡，微粒才改变运动状态": "Phân tử chất lỏng va chạm từ mọi phía; va chạm không cân bằng khiến hạt đổi hướng.",
        "微粒越小、温度越高，运动越明显（撞击数变少、η 变小）": "Hạt càng nhỏ và nhiệt độ càng cao thì chuyển động Brown càng dễ quan sát.",
        "同一个根源（分子热运动），让浓度从高向低展开": "Chuyển động nhiệt cũng khiến chất khuếch tán từ nơi nồng độ cao sang thấp.",
        "看见": "Quan sát", "描迹": "Ghi dấu", "撞击": "Va chạm", "强弱": "Mức độ", "扩散": "Khuếch tán",
    },
    "river-step": {
        "整体 · 一块从山地到海的沙盘": "Toàn cảnh · sa bàn từ núi ra biển",
        "长江镇江段的岸线为什么持续向北推移？": "Vì sao bờ sông ở một khúc uốn có thể dịch chuyển theo thời gian?",
        "山区落差大 → 流速快 → 向下侵蚀为主": "Ở núi, độ dốc lớn làm nước chảy nhanh và xói sâu lòng sông.",
        "落差减小 → 向两岸侵蚀加强 → 河谷拓宽": "Khi độ dốc giảm, xói mòn sang hai bờ tăng và thung lũng mở rộng.",
        "凹岸侵蚀、凸岸堆积 → 河道更弯": "Bờ lõm bị xói, bờ lồi được bồi tụ, làm khúc sông uốn cong hơn.",
        "流速减慢 → 搬运能力减弱 → 三种冲积平原": "Nước chảy chậm mang ít phù sa hơn, tạo các dạng đồng bằng bồi tích.",
        "落差": "Độ dốc", "展宽": "Mở rộng", "弯道": "Khúc uốn", "堆积": "Bồi tụ",
    },
}

STRING = re.compile(r'"(?:\\.|[^"\\])*"')


def decode_js_string(literal: str) -> str | None:
    raw = literal[1:-1]
    try:
        return codecs.decode(raw, "unicode_escape")
    except (UnicodeError, ValueError):
        return None


def replace_literals(source: str, mapping: dict[str, str]) -> tuple[str, int]:
    count = 0

    def sub(match: re.Match[str]) -> str:
        nonlocal count
        decoded = decode_js_string(match.group())
        if decoded not in mapping:
            return match.group()
        count += 1
        return json.dumps(mapping[decoded], ensure_ascii=True)

    return STRING.sub(sub, source), count


def main() -> None:
    total = 0
    for path in sorted(COURSES.glob("*-step.html")):
        slug = path.stem
        source = path.read_text(encoding="utf-8")
        source = re.sub(r'/\* VI_UI_START \*/.*?/\* VI_UI_END \*/', '', source, flags=re.S)
        # The upstream fallback points to a missing courses/index.html.
        source = source.replace('.meta.home||"./index.html"', '.meta.home||"../index.html"')
        mapping = dict(COMMON)
        selected = LESSONS.get(slug)
        if selected:
            row = CATALOG[slug]
            mapping[row["title"]] = selected["title"]
            mapping[row["question"]] = selected["question"]
            mapping.update(zip(row["steps"], selected["steps"]))
            mapping.update(EXTRA[slug])
            mapping.update(PANEL_VI[slug])
            start = source.find("steps:[", source.find(f'meta:{{slug:"{slug}"'))
            step_source = source[start:start + 60000]
            markers = list(re.finditer(r'\{tag:"(?:\\.|[^"\\])*",q:("(?:\\.|[^"\\])*")', step_source))
            if len(markers) != len(GUIDED[slug]):
                raise ValueError(f"Số bước thay đổi ở {slug}: {len(markers)}")
            if len(OUTCOMES[slug]) != len(markers):
                raise ValueError(f"Số bản dịch kết luận không khớp ở {slug}")
            for index, marker in enumerate(markers):
                question, action = GUIDED[slug][index]
                old_question = decode_js_string(marker.group(1))
                if old_question:
                    mapping[old_question] = question
                boundary = markers[index + 1].start() if index + 1 < len(markers) else len(step_source)
                action_match = re.search(r'act:\{.{0,650}?text:("(?:\\.|[^"\\])*")', step_source[marker.end():boundary])
                if action_match:
                    old_action = decode_js_string(action_match.group(1))
                    if old_action:
                        mapping[old_action] = action
                step_segment = step_source[marker.end():boundary]
                observation, takeaway = OUTCOMES[slug][index]
                for pattern, translated in [
                    (r'expect:\{text:("(?:\\.|[^"\\])*")', observation),
                    (r'concl:("(?:\\.|[^"\\])*")', takeaway),
                ]:
                    field = re.search(pattern, step_segment)
                    if not field:
                        raise ValueError(f"Thiếu phần quan sát/kết luận ở {slug}, bước {index + 1}")
                    original_field = decode_js_string(field.group(1))
                    if original_field:
                        mapping[original_field] = translated
            locate = re.search(r'locate:("(?:\\.|[^"\\])*")', source[source.find(f'meta:{{slug:"{slug}"'):])
            if locate:
                original = decode_js_string(locate.group(1))
                if original:
                    mapping[original] = "Bài học thực hành 3D · chương trình phổ thông"
            source = source.replace('<html lang="zh-CN">', '<html lang="vi">', 1)
            source = re.sub(r"<title>.*?</title>", f'<title>{selected["title"]} · Phòng thí nghiệm 3D</title>', source, count=1)
        source, changes = replace_literals(source, mapping)
        if slug == "energy-step":
            source = source.replace(
                r'`\u52A8\u80FD\u6BD4\u52BF\u80FD\u5C11 ${(-t.delta*100).toFixed(2)} %`',
                '`Động năng nhỏ hơn thế năng ${(-t.delta*100).toFixed(2)}%`',
            )
        if selected:
            config = re.search(r'var (\w+)=\{meta:\{slug:"' + re.escape(slug) + r'"', source)
            if not config:
                raise ValueError(f"Không tìm thấy cấu hình bài {slug}")
            shared = re.search(r'var ([\w$]+)=\{home:"M\\u1ee5c l\\u1ee5c"', source)
            if not shared:
                raise ValueError(f"Không tìm thấy nhãn dùng chung của {slug}")
            data = {
                "guided": GUIDED[slug], "outcomes": OUTCOMES[slug],
                "quiz": QUIZZES[slug], "units": UNITS[slug], "plates": PLATES[slug],
                "details": DETAILS[slug], "layers": LAYERS.get(slug, {}), "toast": TOAST.get(slug, {}),
            }
            if len(data["quiz"]) != len(re.findall(r'\{tag:"(?:\\.|[^"\\])*",unit:', source[source.find('quiz:{', config.end()):source.find('help:{', config.end())])):
                raise ValueError(f"Số câu kiểm tra khác dự kiến ở {slug}")
            payload = json.dumps(data, ensure_ascii=True, separators=(",", ":"))
            snippet = f'''/* VI_UI_START */(function(){{const C={config.group(1)},U={shared.group(1)},T={payload},han=/[\\u3400-\\u9fff]/;
                C.top.total=T.details.top;
                C.mainline.chain.forEach((item,i)=>{{if(T.details.chain[i])item.k=T.details.chain[i]}});
                C.units.forEach((item,i)=>{{const v=T.units[i];if(v){{item.name=v[0];item.short=v[0];item.brief=v[1]}}}});
                C.steps.forEach((step,i)=>{{const [question,action]=T.guided[i],[observation,takeaway]=T.outcomes[i];
                    step.points=[observation,takeaway];step.ref="Nguồn: Tongjiang Lab; số liệu là mô phỏng giảng dạy.";
                    step.exam="Tự kiểm tra: "+question;step.tags=(step.tags||[]).filter(v=>typeof v==="string"&&!han.test(v));
                    if(typeof step.eqCal==="string"&&han.test(step.eqCal))step.eqCal="";
                    if(typeof step.eq==="string"&&han.test(step.eq))step.eq="";
                }});
                if(C.plates)Object.assign(C.plates,T.plates);
                C.quiz.list.forEach((item,i)=>{{const v=T.quiz[i];if(v)Object.assign(item,{{tag:v[0],q:v[1],opts:v[2],ans:v[3],why:v[4]}})}});
                C.help.items[0]=["Kéo / cuộn chuột","Xoay và phóng to mô hình"];
                C.help.items[1]=["← →","Chuyển bước học"];
                C.help.goal=T.details.goal;C.foot.note=T.details.note;
                C.foot.keys="Phím tắt: ← → chuyển bước · Q kiểm tra · F toàn màn hình";
                Object.assign(C.layers||{{}},T.layers);Object.assign(C.toast||{{}},T.toast);
                U.no="Bước";U.ofEnd=i=>`/ ${{i}} bước`;
                U.autoing="Có thể xem mô phỏng tự động của bước này trước khi tự thử.";
                U.last=i=>`Đây là bước ${{i}}. Bạn có thể quay lại bất kỳ bước nào để ôn lại.`;
                U.hint=i=>`← → đổi bước · chọn một trong ${{i}} bước · Esc về bảng điều khiển`;
                U.rec.count=(i,n)=>`${{i}} / ${{n}} lượt`;
                U.rec.folded=i=>`${{i}} lượt trước đã thu gọn`;
                U.rec.oldHead=i=>`${{i}} (dữ liệu cũ, không tính vào đường khớp)`;
                U.rec.oldFolded=i=>`${{i}} lượt dữ liệu cũ đã thu gọn`;
                U.quiz.sub=i=>`${{i}} câu trắc nghiệm; trả lời sai sẽ gợi ý bước cần xem lại`;
                U.quiz.unitOf="Câu này kiểm tra bước";
                U.quiz.good="Bạn đã hiểu nhiều ý chính. Hãy xem giải thích của câu sai.";
                U.quiz.retry="Hãy xem lại các bước rồi thử thêm lần nữa.";
                Object.assign(U.accident,{{head:"Xem lại sự cố",restart:"Đặt lại thiết bị",close:"Xem mô hình",countdown:"Cảnh báo",countdownSub:"Hãy điều chỉnh trong 3 giây",countdownFix:"Thông số đã về vùng an toàn",chainHead:"Chuỗi nguyên nhân"}});
                Object.assign(U.toast,{{esc:"Đã dừng khẩn cấp",repaired:"Đã đặt lại thông số và khởi động",stepReset:"Đã đặt lại bước này và ẩn kết luận",win:"Đạt mục tiêu"}});
            }})();/* VI_UI_END */'''
            calls = list(re.finditer(r'\b\w+\(\{C:' + re.escape(config.group(1)) + r'\b', source))
            if not calls:
                raise ValueError(f"Không tìm thấy điểm khởi chạy bài {slug}")
            call = calls[-1]
            source = source[:call.start()] + snippet + source[call.start():]
        path.write_text(source, encoding="utf-8", newline="\n")
        total += changes
        print(f"{slug}: {changes} nhãn Việt hoá")
    (ROOT / "lessons-vi.json").write_text(json.dumps(LESSONS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    categories = {"physics": "Vật lý", "chem": "Hoá học", "bio": "Sinh học", "geo": "Địa lý"}
    aliases = {"phys": "Vật lý", "physics": "Vật lý", "chem": "Hoá học", "bio": "Sinh học", "geo": "Địa lý"}
    cards = []
    for row in CATALOG.values():
        slug = row["slug"]
        title = LESSONS.get(slug, {}).get("title", row["title"])
        label = "Đã biên tập tiếng Việt" if slug in LESSONS else "Nguồn gốc · đang biên tập"
        category = aliases.get(row["subject"], categories.get(row["subject"], "Khoa học"))
        cards.append(f'<a class="resource-card" href="./courses/{html.escape(slug)}.html"><img src="./covers/{html.escape(slug)}.webp" alt="" loading="lazy"><span><small>{html.escape(category)} · {html.escape(label)}</small><strong>{html.escape(title)}</strong><em>{len(row["steps"])} bước học ↗</em></span></a>')
    library = '''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kho tài nguyên 3D · Không gian Toán 3D</title><link rel="stylesheet" href="style.css"><style>.library{max-width:1320px;margin:auto;padding:70px 44px}.library h1{font:800 clamp(35px,5vw,60px) Manrope,Arial,sans-serif;margin:15px 0}.library>p{color:#a9c1bd;line-height:1.7;max-width:700px}.resource-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:35px}.resource-card{display:flex;gap:12px;background:#102d34;border:1px solid #2a4e50;padding:10px;border-radius:12px;min-width:0}.resource-card:hover{border-color:#80e6c9}.resource-card img{width:94px;height:82px;object-fit:cover;border-radius:7px}.resource-card span{display:flex;flex-direction:column;gap:6px;min-width:0}.resource-card small{color:#83dbbd;font-size:10px}.resource-card strong{font-size:13px;line-height:1.35}.resource-card em{font-size:11px;color:#95b0ac;font-style:normal}@media(max-width:900px){.resource-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:620px){.library{padding:35px 20px}.resource-grid{grid-template-columns:1fr}}</style></head><body><header class="topbar"><a class="brand" href="./index.html"><span class="brand-mark">∑</span><span>KHÔNG GIAN<br><strong>TOÁN 3D</strong></span></a><nav><a href="./index.html">← Về trang chủ</a></nav></header><main class="library"><span class="section-kicker">TÀI NGUYÊN NGUỒN</span><h1>54 phòng thí nghiệm 3D</h1><p>Sáu bài có nhãn và lộ trình tiếng Việt. Các bài còn lại được giữ nguyên tài nguyên 3D để tiếp tục rà soát và Việt hoá nội dung chuyên môn. Tên tiếng Trung của chúng được giữ để bạn nhận biết phần chưa biên tập.</p><div class="resource-grid">''' + "".join(cards) + '''</div></main><footer><span>KHÔNG GIAN TOÁN 3D</span><span>Nguồn: Tongjiang Lab · CC BY-NC 4.0</span></footer></body></html>'''
    (ROOT / "nguon.html").write_text(library, encoding="utf-8")
    print(f"Tổng: {total} nhãn; 6 bài được biên tập câu hỏi và lộ trình.")


if __name__ == "__main__":
    main()
