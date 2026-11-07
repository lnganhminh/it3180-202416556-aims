# Đối chiếu nội dung và phiên bản

## Các mốc trong kho

| Lab | Nhánh | Tag | PR tích hợp |
|---|---|---|---|
| 01 | release/lab01 | v0.1.0 | [#1](https://github.com/lnganhminh/it3180-202416556-aims-new/pull/1) |
| 02 | release/lab02 | v0.2.0 | [#2](https://github.com/lnganhminh/it3180-202416556-aims-new/pull/2) |
| 03 | release/lab03 | v0.3.0 | [#3](https://github.com/lnganhminh/it3180-202416556-aims-new/pull/3) |
| 04 | release/lab04 | v1.0.0, v1.0.1 | [#4](https://github.com/lnganhminh/it3180-202416556-aims-new/pull/4), [#5](https://github.com/lnganhminh/it3180-202416556-aims-new/pull/5) |
| 05 | release/lab05 | v1.1.0 | [#6](https://github.com/lnganhminh/it3180-202416556-aims-new/pull/6), [#7](https://github.com/lnganhminh/it3180-202416556-aims-new/pull/7) |

## Kết quả kiểm tra mã

- Demo ở các mốc Lab 01–05 cho tổng 63.89 USD.
- Lab 03: 6 kiểm thử; bản 1.0.0: 7 kiểm thử; bản vá 1.0.1: 8 kiểm thử.
- Bản 1.1.0: 14 kiểm thử, gồm giới hạn giỏ, giảm giá, xóa DVD, tìm kiếm và sắp xếp.
- Bản vá tìm kiếm đã được kiểm tra thất bại trước sửa và thành công sau sửa.
- Commit sửa lỗi trên dòng 1.0.x: `4d0d7a0d62881e3189bf36beb4eb94b725d68ee7`;
  chuyển vào master bằng `cherry-pick -x` qua PR #6.
- CI được cấu hình trong `.github/workflows/ci.yml`; trạng thái chạy nằm ở tab Actions.

## Phạm vi lịch sử

Kho được khởi tạo từ các tệp thực hành có sẵn trên máy, sau đó chỉnh sửa và
tích hợp qua các PR nêu trên. Lịch sử mới ghi nhận lần nhập và chỉnh sửa này;
không tái tạo các thao tác đã diễn ra trước khi khởi tạo kho.

Các chủ đề restore/amend, ba kiểu merge, conflict và reset/revert được giải
thích trong đáp án; không xem phần giải thích là bằng chứng đã thực hiện đầy
đủ các thao tác đó trong lịch sử mới. Các PR hiện có dùng merge commit và
chưa có review độc lập. Chưa thiết lập branch protection trong kho này.
Xác thực Git dùng HTTPS/Git Credential Manager, chưa thực hiện bước SSH của đề.
