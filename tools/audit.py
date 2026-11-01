"""Check links, bundled JavaScript syntax and localization invariants."""
from __future__ import annotations

import json
import codecs
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
selected = json.loads((ROOT / "lessons-vi.json").read_text(encoding="utf-8"))
errors = []

if len(catalog) != 54:
    errors.append(f"Dự kiến 54 bài, thấy {len(catalog)}")
if len({row["slug"] for row in catalog}) != len(catalog):
    errors.append("Trùng slug bài học")

for row in catalog:
    slug = row["slug"]
    course = ROOT / row["file"]
    cover = ROOT / row["cover"]
    if not course.is_file() or not cover.is_file():
        errors.append(f"Thiếu HTML hoặc ảnh: {slug}")
        continue
    html = course.read_text(encoding="utf-8")
    if '.meta.home||"./index.html"' in html:
        errors.append(f"Liên kết Mục lục còn sai: {slug}")
    if '.meta.home||"../index.html"' not in html:
        errors.append(f"Không thấy liên kết Mục lục: {slug}")
    if slug in selected:
        if '<html lang="vi">' not in html or selected[slug]["title"] not in html:
            errors.append(f"Thiếu tiêu đề tiếng Việt: {slug}")
        if selected[slug]["title"] not in (ROOT / "nguon.html").read_text(encoding="utf-8"):
            errors.append(f"Thiếu trong thư viện: {slug}")
        ui_at = html.find("ui:{", html.find(f'meta:{{slug:"{slug}"'))
        ui = re.search(r'ui:\{crumb:("(?:\\.|[^"\\])*"),subAll:("(?:\\.|[^"\\])*")\}', html[ui_at:ui_at + 500]) if ui_at >= 0 else None
        if not ui or any(re.search(r'[\u4e00-\u9fff]', codecs.decode(value[1:-1], "unicode_escape")) for value in ui.groups()):
            errors.append(f"Nhãn khu vực bài học còn tiếng Trung: {slug}")
        start = html.find("steps:[", html.find(f'meta:{{slug:"{slug}"'))
        lesson_source = html[start:start + 60000]
        markers = list(re.finditer(r'\{tag:"(?:\\.|[^"\\])*",q:("(?:\\.|[^"\\])*")', lesson_source))
        if len(markers) != len(row["steps"]):
            errors.append(f"Số bước không khớp: {slug}")
        for index, marker in enumerate(markers):
            boundary = markers[index + 1].start() if index + 1 < len(markers) else len(lesson_source)
            segment = lesson_source[marker.end():boundary]
            fields = [marker.group(1)]
            for pattern in [r'act:\{.{0,650}?text:("(?:\\.|[^"\\])*")', r'expect:\{text:("(?:\\.|[^"\\])*")', r'concl:("(?:\\.|[^"\\])*")']:
                field = re.search(pattern, segment)
                if field:
                    fields.append(field.group(1))
            if len(fields) != 4 or any(re.search(r'[\u4e00-\u9fff]', codecs.decode(value[1:-1], "unicode_escape")) for value in fields):
                errors.append(f"Câu hỏi, thao tác, quan sát hoặc kết luận chưa Việt hoá: {slug} bước {index + 1}")
        panel_at = html.find("panel:{", html.find(f'meta:{{slug:"{slug}"'))
        if panel_at < 0:
            errors.append(f"Thiếu bảng điều khiển: {slug}")
        else:
            depth = 0
            quoted = escaped = False
            panel_end = None
            for pos in range(panel_at + 6, len(html)):
                char = html[pos]
                if quoted:
                    if escaped:
                        escaped = False
                    elif char == "\\":
                        escaped = True
                    elif char == '"':
                        quoted = False
                elif char == '"':
                    quoted = True
                elif char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    if depth == 0:
                        panel_end = pos + 1
                        break
            if panel_end is None:
                errors.append(f"Bảng điều khiển chưa đóng: {slug}")
            else:
                panel = html[panel_at:panel_end]
                for literal in re.findall(r'"(?:\\.|[^"\\])*"', panel):
                    if re.search(r'[\u4e00-\u9fff]', codecs.decode(literal[1:-1], "unicode_escape")):
                        errors.append(f"Nhãn tham số còn tiếng Trung: {slug}")
                        break
    script = re.search(r'<script type="module">(.*?)</script>', html, re.S)
    if script is None:
        errors.append(f"Thiếu mô phỏng: {slug}")
        continue
    check = subprocess.run(["node", "--check", "--input-type=module"], input=script.group(1), text=True, capture_output=True, encoding="utf-8")
    if check.returncode:
        errors.append(f"JavaScript lỗi ở {slug}: {check.stderr[-250:]}")

for target in ["index.html", "nguon.html", "style.css", "app.js", "LICENSE", "THIRD_PARTY_NOTICES.md"]:
    if not (ROOT / target).is_file():
        errors.append(f"Thiếu {target}")

check = subprocess.run(["node", "--check", str(ROOT / "app.js")], text=True, capture_output=True, encoding="utf-8")
if check.returncode:
    errors.append(check.stderr[-250:])

visible = subprocess.run(["node", str(ROOT / "tools" / "audit-visible.cjs")], text=True, capture_output=True, encoding="utf-8")
if visible.returncode:
    errors.append(visible.stderr[-1000:] or "Kiểm tra nội dung hiển thị không đạt")

if errors:
    print("Lỗi kiểm tra:")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)
print(f"Đạt: {len(catalog)} bài, {len(selected)} lộ trình tiếng Việt, đầy đủ ảnh và JavaScript hợp lệ.")
print(visible.stdout.strip())
