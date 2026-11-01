"""Vietnamese text for all remaining visible sections of the six featured lessons."""

QUIZZES = {
    "projectile-step": [
        ("Rơi tự do", "Hai bi A (phóng ngang) và B (thả rơi) từ cùng độ cao sẽ chạm đất khi nào?", ["A trước", "B trước", "Cùng lúc", "Phụ thuộc lực gõ"], 2, "Phương đứng của bi phóng ngang là rơi tự do, giống bi B."),
        ("Suy ra thời gian", "Không có đồng hồ, làm sao suy ra các khoảng thời gian bằng nhau?", ["Dùng đồng hồ bấm giây", "Từ độ rơi y theo tỉ lệ 1:4:9:16", "Từ độ dời ngang trước", "Từ độ cao vạch thả"], 1, "Vì y = ½gt², tỉ lệ y là 1:4:9:16 tương ứng tỉ lệ t là 1:2:3:4."),
        ("Phương ngang", "Các độ dời ngang bằng nhau trong những khoảng thời gian bằng nhau cho thấy điều gì?", ["Chuyển động nhanh dần", "Chuyển động đều", "Chuyển động chậm dần", "Chưa đủ dữ liệu"], 1, "Vận tốc ngang không đổi nên x = v₀t."),
        ("Sai số bán kính", "Không hiệu chỉnh bán kính bi khi đọc độ rơi y sẽ làm v₀ tính được thế nào?", ["Không đổi", "Nhỏ đi ở mọi nấc", "Lớn hơn, đặc biệt ở nấc có y nhỏ", "Lúc lớn lúc nhỏ"], 2, "Giấy ghi mép dưới của bi; y đọc nhỏ hơn độ rơi của tâm, khiến v₀ = x√(g/2y) bị tính lớn."),
    ],
    "centripetal-step": [
        ("Tỉ số lực", "Hai bi có cùng m và r. Bi phải quay nhanh gấp đôi: nếu thước trái 8 vạch, thước phải mấy vạch?", ["16", "32", "64", "8"], 1, "F ∝ ω² nên tốc độ góc gấp đôi làm lực gấp bốn: 8 × 4 = 32 vạch."),
        ("Dây đai III", "Tốc độ góc bi phải gấp ba. Từ 8 vạch bên trái, bên phải có mấy vạch?", ["24", "48", "72", "9"], 2, "3² = 9 nên 8 × 9 = 72 vạch."),
        ("Bán kính", "Chỉ tăng bán kính từ 4 cm lên 8 cm; lực hướng tâm thay đổi bao nhiêu lần?", ["Không đổi", "Gấp 2", "Gấp 4", "Gấp 8"], 1, "Khi m và ω không đổi, F = mω²r tỉ lệ thuận với r."),
        ("Tính lực", "Vật 0,10 kg ở bán kính 0,10 m quay với ω = 4 rad/s chịu lực hướng tâm bao nhiêu?", ["0,04 N", "0,16 N", "1,6 N", "16 N"], 1, "F = mω²r = 0,10 × 4² × 0,10 = 0,16 N."),
        ("Dây tuột", "Dây đai tháo ra làm thước bên phải không hiện vạch vì sao?", ["Bi quá nặng", "Bi không quay nên không có lực hướng tâm", "Thước hỏng", "Tay quay ngược"], 1, "Không có chuyển động tròn thì lực ép lên bộ phận đo lực bằng không."),
    ],
    "accel-force-step": [
        ("Thứ tự", "Khi ghi băng giấy, thao tác nào đúng?", ["Thả xe rồi bật máy", "Bật máy rồi thả xe", "Bật máy sau khi xe dừng", "Không cần bật máy"], 1, "Bật máy trước để ghi được cả giai đoạn bắt đầu chuyển động."),
        ("Độ dốc", "Độ dốc của đồ thị v–t cho đại lượng nào?", ["Quãng đường", "Gia tốc", "Khối lượng", "Lực ma sát"], 1, "Gia tốc là mức thay đổi vận tốc theo thời gian."),
        ("Giữ biến", "Muốn xem a phụ thuộc F, cần giữ cố định đại lượng nào?", ["Khối lượng xe", "Lực kéo", "Thời gian", "Tốc độ ban đầu"], 0, "Chỉ thay F và giữ m không đổi để đọc đúng quan hệ a ∝ F."),
        ("Ma sát", "Ván chưa được bù ma sát làm đồ thị a–F ra sao?", ["Vẫn qua gốc", "Có thể lệch khỏi gốc", "Luôn là đường ngang", "Không có điểm đo"], 1, "Một phần lực kéo phải thắng ma sát nên đường a–F có thể lệch khỏi gốc."),
    ],
    "energy-step": [
        ("Thao tác", "Khi thả vật để ghi băng giấy, làm gì trước?", ["Thả vật", "Bật máy ghi chấm", "Đổi vật", "Vẽ đồ thị"], 1, "Bật máy trước rồi mới thả vật để không mất các điểm đầu."),
        ("Vận tốc tại B", "Với A, B, C cách đều theo thời gian T, tính v_B bằng công thức nào?", ["(h_C − h_B)/T", "(h_C − h_A)/(2T)", "h_B/T", "gT²/2"], 1, "Vận tốc tại B gần bằng vận tốc trung bình từ A đến C."),
        ("Bảo toàn", "Nếu chỉ trọng lực sinh công, quan hệ nào đúng?", ["½v² = gh", "v = gh", "½v = gh²", "v² = gh"], 0, "Từ ½mv² = mgh, khối lượng triệt tiêu và còn ½v² = gh."),
        ("Lực cản", "Có lực cản thì thế năng giảm và động năng tăng quan hệ ra sao?", ["Bằng nhau chính xác", "Thế năng giảm thường lớn hơn", "Động năng tăng luôn lớn hơn", "Cả hai đều bằng không"], 1, "Một phần thế năng chuyển thành nhiệt và dạng khác do lực cản."),
    ],
    "brownian-step": [
        ("Vật chuyển động", "Trong chuyển động Brown, ta quan sát trực tiếp vật nào?", ["Phân tử nước", "Hạt nhỏ lơ lửng", "Từng nguyên tử", "Phân tử mực"], 1, "Kính hiển vi cho thấy hạt lơ lửng; chuyển động của nó phản ánh va chạm phân tử."),
        ("Tránh nhầm", "Hạt tiêu chuyển động mạnh khi đun nước có chắc là chuyển động Brown?", ["Có, luôn luôn", "Không, có thể do đối lưu", "Chỉ khi nước sôi", "Không cần quan sát"], 1, "Dòng đối lưu làm hạt trôi theo dòng; đó không phải dấu hiệu riêng của va chạm ngẫu nhiên."),
        ("Chất lỏng", "Bụi nhỏ chuyển động Brown trong dầu cho thấy điều gì?", ["Phân tử dầu chuyển động hỗn loạn", "Dầu đứng yên hoàn toàn", "Bụi là phân tử dầu", "Dầu không có phân tử"], 0, "Chuyển động của hạt bụi là dấu vết gián tiếp của phân tử chất lỏng."),
        ("Đường gấp khúc", "Nối các vị trí ghi mỗi 30 giây tạo ra đường gì?", ["Đường đi liên tục thật", "Đường nối các mẫu vị trí", "Đường thẳng bắt buộc", "Đồ thị vận tốc"], 1, "Hạt còn di chuyển giữa hai lần ghi; đường nối không phải toàn bộ quỹ đạo thật."),
        ("Hạt nhỏ", "Giữ nhiệt độ, hạt nhỏ hơn thường chuyển động Brown ra sao?", ["Rõ hơn", "Yếu hơn", "Không đổi", "Biến mất"], 0, "Hạt nhỏ dễ thay đổi chuyển động trước tác động va chạm không cân bằng."),
        ("Thống kê", "Hai hạt khác nhau ở cùng điều kiện có đường đi giống hệt nhau không?", ["Luôn giống", "Không, từng đường đi ngẫu nhiên", "Chỉ giống khi đun nóng", "Không thể quan sát"], 1, "Quy luật thể hiện ở thống kê nhiều lần, không phải ở từng đường đi."),
    ],
    "river-step": [
        ("Thung lũng chữ V", "Ở miền núi, vì sao thung lũng sông thường có mặt cắt chữ V?", ["Chủ yếu xói sâu", "Chủ yếu bồi tụ", "Không có nước", "Do thủy triều"], 0, "Độ dốc lớn và dòng nhanh khiến xói sâu chiếm ưu thế."),
        ("Khúc uốn", "Ở khúc uốn, bờ lõm và bờ lồi thay đổi thế nào?", ["Cả hai cùng bồi", "Bờ lõm xói, bờ lồi bồi", "Bờ lõm bồi, bờ lồi xói", "Không thay đổi"], 1, "Dòng chảy mạnh phía bờ lõm, yếu phía bờ lồi."),
        ("Quạt bồi tích", "Quạt bồi tích thường hình thành ở đâu?", ["Cửa núi ra đồng bằng", "Giữa đại dương", "Đỉnh núi", "Giữa hồ sâu"], 0, "Ra khỏi núi, độ dốc và vận tốc giảm, vật liệu lắng thành hình quạt."),
        ("Châu thổ", "Điều kiện trực tiếp tạo đồng bằng châu thổ là gì?", ["Nước chảy nhanh hơn ở cửa sông", "Phù sa lắng khi dòng chảy chậm lại", "Đáy biển dốc đứng", "Không có phù sa"], 1, "Ở cửa sông, dòng chảy giảm tốc và phù sa lắng ra phía biển."),
        ("Nơi ở", "Khi lập khu dân cư trên đồng bằng sông, điều gì cần xem trước?", ["Màu nước", "Nguy cơ ngập lũ", "Số cá", "Độ cong của mây"], 1, "Vị trí an toàn cần xét cao độ và phạm vi ngập lũ."),
    ],
}

UNITS = {
    "projectile-step": [
        ("Máng và viên bi", "Máng có đầu nằm ngang, ba vạch thả và viên bi."),
        ("So sánh rơi", "Búa, thanh đàn hồi, hai viên bi A/B và hai giá đỡ."),
        ("Ghi dấu", "Tấm nền, giấy trắng, giấy than và tấm chắn điều chỉnh độ cao."),
        ("Giấy ô", "Bảng ô vuông và ảnh chụp ở các thời điểm bằng nhau."),
    ],
    "centripetal-step": [
        ("Máy và tay quay", "Thân máy, chân đỡ, trục quay và tay quay."),
        ("Ròng rọc và dây", "Ba tầng ròng rọc và dây đai quyết định tỉ số tốc độ góc."),
        ("Rãnh dài", "Bi trong rãnh dài, tay đòn và thước đo lực bên trái."),
        ("Rãnh ngắn", "Bi trong rãnh ngắn, tay đòn và thước đo lực bên phải."),
    ],
    "accel-force-step": [
        ("Ván và ròng rọc", "Tấm ván dài, miếng kê, dây kéo và ròng rọc."),
        ("Xe và quả cân", "Xe, quả cân đặt trên xe và quả cân treo kéo xe."),
        ("Máy ghi chấm", "Máy ghi chấm, băng giấy và thước đo."),
        ("Cân và đồ thị", "Cân khối lượng và bảng tọa độ để vẽ số liệu."),
    ],
    "energy-step": [
        ("Giá và máy", "Giá đỡ, máy ghi chấm, nguồn điện và dây nối."),
        ("Vật và cân", "Vật nặng, kẹp giữ và cân khối lượng."),
        ("Băng giấy", "Băng giấy có các chấm thời gian và thước đo độ cao."),
        ("Bảng tọa độ", "Bảng vẽ quan hệ giữa ½v² và h."),
    ],
    "brownian-step": [
        ("Kính hiển vi", "Kính, tiêu bản và mẫu mực loãng; hình ảnh hiện trên màn hình."),
        ("Giấy tọa độ", "Ghi một vị trí hạt mỗi 30 giây và nối các điểm lấy mẫu."),
        ("Khung phóng đại", "Hạt nhỏ và phân tử được phóng đại để nhìn va chạm."),
        ("Bể khuếch tán", "Một giọt mực lan dần trong nước tĩnh."),
    ],
    "river-step": [
        ("Sông miền núi", "Độ dốc lớn làm nước chảy nhanh và xói sâu lòng sông."),
        ("Quạt bồi tích", "Ra cửa núi, nước chậm lại và vật liệu thô lắng thành hình quạt."),
        ("Khúc uốn", "Bờ lõm bị xói, bờ lồi được bồi, hình thành bãi ven sông."),
        ("Châu thổ", "Ở cửa sông, phù sa lắng và phần đất nhô dần ra biển."),
    ],
}

PLATES = {
    "projectile-step": {
        "labChute":"Máng nghiêng M", "labBall":"Viên bi", "labPanel":"Tấm ghi dấu", "labBoard":"Tấm chắn N", "labGrid":"Bảng giấy ô", "labStrobe":"Ảnh nhiều thời điểm", "slowmo":"Chạy chậm ×0,25", "inkCount":"Số dấu", "rowsOnPlate":"lượt đã ghi", "dropA":"Bi A (phóng ngang)", "dropB":"Bi B (rơi tự do)", "ballR":"Bán kính bi r = 10 mm", "boardY":"Độ cao tấm chắn", "boardHeight":"Độ cao tấm chắn", "scaleTitle":"Độ cao chắn / mm", "schemaNote":"Minh họa", "labPlumb":"Dây dọi (gốc)", "labHammer":"Búa nhỏ",
    },
    "centripetal-step": {
        "left":"Thước trái: 8 vạch", "right":"Thước phải: 8 vạch", "table":"Vạch đỏ trắng · thang 80 vạch", "name":"Máy đo lực hướng tâm", "crank":"Tay quay 1", "gearLbl":"Ròng rọc 2·3", "slotLbl":"Rãnh dài 4", "shortLbl":"Rãnh ngắn 5", "leftTag":"Trái", "rightTag":"Phải",
    },
    "accel-force-step": {
        "plateFlat":"Ván ngang · chưa bù lực cản", "plateOk":"Nâng 1,15° · đã bù lực cản", "plateOver":"Nâng 2,29° · quá mức", "labBoard":"Tấm ván dài", "labCart":"Xe thí nghiệm", "labTicker":"Máy ghi chấm", "labCoord":"Bảng tọa độ", "chartSlope":"Độ dốc", "slowmo":"Chạy chậm ×0,2", "labBal":"Khối lượng xe vừa cân", "labSupply":"Nguồn điện", "tickerTag":"Máy ghi chấm · AC 50 Hz",
    },
    "energy-step": {
        "labStand":"Giá đỡ", "labTicker":"Máy ghi chấm", "labTape":"Băng giấy", "labLoad":"Vật nặng", "labBal":"Cân", "labCoord":"Bảng tọa độ", "labSupply":"Nguồn điện", "releasePt":"Điểm thả", "chartEmpty":"Ghi một lượt để vẽ", "tautOn":"Băng giấy thẳng", "tautOff":"Băng giấy lệch", "blankOn":"Đầu băng chưa ghi", "slowmo":"Chạy chậm ×0,15",
    },
    "brownian-step": {
        "scope":"Kính hiển vi", "slip":"Một giọt mực pha loãng", "monitor":"Màn hình · mẫu huyền phù", "monitorOff":"Màn hình · chạm để xem", "traceHead":"Ghi vị trí mỗi 30 giây", "microNote":"Đã phóng đại · không đúng tỉ lệ", "microImpact":"Va chạm phân tử chất lỏng", "microF":"Hợp lực F", "microPath":"Đường đi thật trong 30 giây", "microGrain":"Hạt nhỏ", "tankHead":"Nước tĩnh · một giọt mực", "tankRef":"Đối chiếu 100°C (minh họa)", "tankNow":"Hiện tại", "tankPeak":"Giá trị đỉnh", "benchTag":"Điều kiện: nhiệt độ · cỡ hạt · số lần ghi",
    },
    "river-step": {},
}

DETAILS = {
    "projectile-step": {"top":"x = v₀t · y = ½gt² · suy ra v₀ từ điểm rơi", "chain":["Tách chuyển động","Phương đứng","Suy ra thời gian","Phương ngang"], "goal":"Tách chuyển động ném ngang thành hai phương, đo v₀ từ các điểm rơi và giải thích hai nguồn sai số.", "note":"Mô hình dụng cụ và số liệu được dựng để giảng dạy theo bài gốc; đây là thí nghiệm mô phỏng."},
    "centripetal-step": {"top":"F = mω²r · giữ cố định biến", "chain":["Cho máy quay","Đọc số vạch","Đổi một biến","So sánh tỉ số","Rút công thức"], "goal":"Dùng hai thước trên máy quay để tìm F phụ thuộc m, r và ω thế nào.", "note":"Hình máy, dây đai và số vạch là mô hình giảng dạy; kết quả là tỉ số, không phải lực đo trực tiếp bằng N."},
    "accel-force-step": {"top":"a = F/m · giữ cố định biến", "chain":[], "goal":"Dùng băng giấy và các quả cân để tìm quan hệ giữa a, F và m, rồi nhận ra sai số.", "note":"Dụng cụ và số đo là mô phỏng để học phương pháp thực nghiệm; không thay cho thí nghiệm trên thiết bị thật."},
    "energy-step": {"top":"½v² ≈ gh · vận tốc từ băng giấy", "chain":["Điều kiện","Ghi chấm","Tính v","So năng lượng","Kết luận"], "goal":"Đo vận tốc và độ cao bằng băng giấy để kiểm chứng ½v² ≈ gh và phân tích lực cản.", "note":"Mô hình có chế độ lý tưởng và chế độ có lực cản; số đo là dữ liệu mô phỏng."},
    "brownian-step": {"top":"⟨r²⟩ = 4Dt · mô hình 2D mở rộng", "chain":[], "goal":"Quan sát hạt nhỏ, lấy mẫu nhiều lần và phân biệt đường đi ngẫu nhiên với xu hướng thống kê.", "note":"Hạt và phân tử được vẽ phóng đại; phép đo D và ⟨r²⟩ là phần mở rộng trong mô phỏng."},
    "river-step": {"top":"Độ dốc → tốc độ dòng chảy → xói mòn và bồi tụ", "chain":[], "goal":"Dùng sa bàn để xem sông xói sâu, mở rộng thung lũng và bồi tụ ở cửa núi, cửa sông.", "note":"Hình học, độ dốc, lưu lượng và số đo đều là mô phỏng dùng để học quy luật."},
}

LAYERS = {
    "accel-force-step": {"measure":"Tháo băng giấy để đo x₁…x₄ và Δx (Δx = aT²)"},
    "river-step": {
        "contour":"Đường đồng mức (mỗi 100 m, minh họa)",
        "valley":"Mặt cắt thung lũng (ngang: 1 ô = 1 km; đứng phóng đại ×10)",
        "cut":"Mặt cắt trước: độ rộng, độ sâu và các giai đoạn",
        "floodplain":"Mùa lũ: bãi ven sông bị ngập",
        "villages":"Khu dân cư ở nơi ít nguy cơ ngập lũ",
        "label":"Địa danh và tỉ lệ",
    },
}

TOAST = {"brownian-step": {"ref":"Đã về điều kiện mẫu: 20°C · hạt 0,5 μm · 10 lần ghi (300 s)"}}
