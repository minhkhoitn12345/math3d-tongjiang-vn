# Đưa bản Tongjiang Việt hoá lên GitHub và Vercel

Thư mục này là dự án riêng, không ghi đè repository `minhkhoitn12345/math3d` hoặc Vercel project `minhkhoitn12346/math3d`. Repository dự định: `minhkhoitn12345/math3d-tongjiang-vn`; Vercel project dự định: `minhkhoitn12346/math3d-tongjiang-vn`.

## Trước khi xuất bản

Chạy `python tools/audit.py`. Trang là HTML/CSS/JavaScript tĩnh, không có bước `npm install` hoặc build. `vercel.json` chọn gốc thư mục làm output; `.vercelignore` chỉ loại các công cụ phát triển, không loại 54 bài học và ảnh. Giữ các tệp `LICENSE` và `THIRD_PARTY_NOTICES.md` khi xuất bản vì source Tongjiang Lab dùng CC BY-NC 4.0.

## Khi terminal có quyền GitHub/Vercel và kết nối Internet

```powershell
cd D:\project3d\math3d-tongjiang-vn
gh auth login --web
gh repo create minhkhoitn12345/math3d-tongjiang-vn --public
git push -u origin main
npx --yes vercel@59.0.0 login
npx --yes vercel@59.0.0 deploy --prod --scope minhkhoitn12346
```

Remote `origin` đã được cấu hình sẵn trong Git local, vì vậy chỉ cần tạo repository trên GitHub rồi push. Nếu repository đã tồn tại, bỏ qua lệnh `gh repo create` và chỉ chạy `git push -u origin main` sau khi kiểm tra lịch sử remote. Lệnh Vercel tạo và liên kết project trong lần triển khai đầu. Chọn tên `math3d-tongjiang-vn` nếu CLI hỏi. Sao chép URL production mà CLI in ra; URL thực chỉ có sau khi deploy thành công. Trước khi chạy `vercel git connect`, kiểm tra project Vercel đã tự kết nối GitHub chưa; nếu chưa, chạy:

```powershell
npx --yes vercel@59.0.0 git connect --scope minhkhoitn12346
```

Sau khi GitHub được kết nối với Vercel, các lần `git push origin main` sẽ tạo deployment mới qua Vercel Git Integration. Workflow GitHub Actions trong repository chỉ kiểm tra cấu trúc, cú pháp và dữ liệu giao diện trước khi phát triển tiếp.

Nếu `gh` báo token trong keyring không hợp lệ, đăng nhập lại bằng `gh auth login --web`. Không dán token vào chat hay ghi token vào mã nguồn. Nếu Vercel báo không có quyền team, đăng nhập đúng tài khoản thuộc `minhkhoitn12346`.
