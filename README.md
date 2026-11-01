# Không gian Toán 3D · bản phát triển từ Tongjiang Lab

Đây là **thư mục dự án mới**, độc lập với `../math3d` và bản nguồn `../tongjiang-lab-main`. Toàn bộ 54 mô phỏng Three.js cùng ảnh bìa được giữ lại. Trang chủ mới tập trung sáu bài dễ liên hệ với toán học: chuyển động ném ngang, lực hướng tâm, định luật II Newton, cơ năng, chuyển động Brown và địa hình sông.

## Mở dự án

```powershell
cd D:\project3d\math3d-tongjiang-vn
python -m http.server 5174 --bind 127.0.0.1
```

Mở <http://127.0.0.1:5174/>. Không cần `npm install` hoặc kết nối Internet. Các trang bài học vẫn là những tệp HTML tự chứa của bản gốc. Nút **Mục lục** trên 54 bài đã được sửa để về trang chủ mới.

## Mức độ Việt hoá hiện tại

- Trang chủ, danh mục 54 bài, sáu tiêu đề, câu hỏi chính và tên các bước học bằng tiếng Việt.
- Các nút, trạng thái, bảng điều khiển, ghi số liệu và kiểm tra thường gặp được thay nhãn trên toàn bộ 54 bài.
- Cả 50 bước của sáu bài chọn lọc đã có **câu hỏi, thao tác, quan sát dự kiến và kết luận tiếng Việt**. Những đoạn này được biên tập ngắn gọn theo nội dung gốc.
- **Bảng điều khiển tham số của sáu bài** đã Việt hoá: tên thanh trượt, công tắc, các nấc, số đo, đồ thị, trạng thái và thông báo khi đổi tham số. Script kiểm tra sẽ báo lỗi nếu còn chuỗi tiếng Trung trong cấu hình bảng điều khiển này.
- Sáu bài tuyển chọn được bổ sung bản tiếng Việt cho phần câu hỏi kiểm tra, nhãn trên mô hình 3D, dụng cụ, gợi ý, chú thích và phím tắt. Kiểm tra tự động đánh giá cấu hình giao diện sau khi áp dụng bản dịch, gồm cả chuỗi tạo động.
- **48 bài ngoài sáu bài tuyển chọn vẫn chủ yếu là bản nguồn tiếng Trung.** Các đoạn tiếng Trung còn nằm trong tệp mã của sáu bài là dữ liệu gốc đã được bản dịch thay trước khi bài học hiển thị, ghi chú nội bộ và thông báo phát triển. Không nên giới thiệu cả kho 54 bài là đã Việt hoá hoàn chỉnh.

Để tiếp tục biên tập, thêm bản dịch vào `COMMON`, `EXTRA` hoặc `LESSONS` trong `tools/localize.py`, rồi chạy `python tools/localize.py`. Tệp `lessons-vi.json` và `nguon.html` được tạo lại từ script. Các bản gốc không bị sửa.

## Kiểm tra

```powershell
python tools/audit.py
```

Script kiểm tra 54 HTML và 54 ảnh, liên kết mục lục, tiêu đề tiếng Việt của sáu bài và cú pháp JavaScript nhúng. Đây là kiểm tra tĩnh; tương tác WebGL, màn hình di động và các phép đo vật lý trong bài cần được thử trong trình duyệt thật.

## Nguồn và giấy phép

Dựa trên [Tongjiang Lab](https://lab.tongjiang.app), tác giả 铜匠十点睡觉. Bản nguồn được cấp phép [CC BY-NC 4.0](LICENSE), yêu cầu ghi công và chỉ sử dụng phi thương mại. Các thư viện đóng gói giữ giấy phép riêng trong [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Các thay đổi của dự án này gồm trang chủ, điều hướng, bản dịch từng phần và sửa liên kết mục lục.
