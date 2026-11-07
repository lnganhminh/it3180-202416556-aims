# IT3180 · Thực hành Git & GitHub

### AIMS-mini — Quản lý giỏ DVD

[![CI](https://github.com/lnganhminh/it3180-202416556-aims-new/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/lnganhminh/it3180-202416556-aims-new/actions/workflows/ci.yml)


Lường Nguyễn Anh Minh MSSV:202416556

## 1. Giới thiệu chương trình

AIMS-mini là ứng dụng Python chạy trên dòng lệnh, lưu danh sách DVD trong bộ nhớ.
Chương trình minh họa các thao tác giỏ hàng, đồng thời là dự án thực hành quản lý
cấu hình, tích hợp thay đổi và phát hành phiên bản bằng Git/GitHub.

- **Giỏ hàng:** thêm, xóa DVD, xem danh sách và tính tổng tiền.
- **Giảm giá:** tính số tiền thanh toán theo tỷ lệ phần trăm hợp lệ.
- **Tra cứu:** tìm theo một phần tiêu đề hoặc theo thể loại.
- **Sắp xếp:** đổi thứ tự DVD theo tên hoặc giá.

## 2. Tra cứu bài nộp

Chọn nhánh để xem nội dung từng Lab, hoặc mở tag để xem đúng mốc phiên bản.

| Bài thực hành | Nội dung học phần | Mã nguồn | Mốc phiên bản | Câu trả lời |
|---|---|---|---|---|
| **Lab 01** | Thiết lập Git; restore/amend; tổ chức lại mã nguồn | [Nhánh Lab 01](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/release/lab01) | [v0.1.0](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/v0.1.0) | [Đọc đáp án](docs/answers-lab01.md) |
| **Lab 02** | Nhánh feature/topic; đồng bộ; các phương án merge | [Nhánh Lab 02](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/release/lab02) | [v0.2.0](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/v0.2.0) | [Đọc đáp án](docs/answers-lab02.md) |
| **Lab 03** | Kiểm thử lỗi; conflict; reset và revert | [Nhánh Lab 03](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/release/lab03) | [v0.3.0](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/v0.3.0) | [Đọc đáp án](docs/answers-lab03.md) |
| **Lab 04** | Chốt bản phát hành; duy trì dòng 1.0.x | [Nhánh Lab 04](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/release/lab04) | [v1.0.0](https://github.com/lnganhminh/it3180-202416556-aims-new/releases/tag/v1.0.0) → [v1.0.1](https://github.com/lnganhminh/it3180-202416556-aims-new/releases/tag/v1.0.1) | [Đọc đáp án](docs/answers-lab04.md) |
| **Lab 05** | Mở rộng chức năng; sửa lỗi và chuyển bản vá | [Nhánh Lab 05](https://github.com/lnganhminh/it3180-202416556-aims-new/tree/release/lab05) | [v1.1.0](https://github.com/lnganhminh/it3180-202416556-aims-new/releases/tag/v1.1.0) | [Đọc đáp án](docs/answers-lab05.md) |

`master` chứa mã và tài liệu mới nhất. Sáu tag đều là annotated tag;
`release/lab04` đã nhận bản vá 1.0.1, còn tag 1.0.0 giữ mốc phát hành ban đầu.

## 3. Cài đặt và chạy

Sử dụng **Python 3.10 trở lên**. Dự án chỉ cần thư viện chuẩn của Python.

```console
git clone https://github.com/lnganhminh/it3180-202416556-aims-new.git
cd it3180-202416556-aims-new
python main.py
python -m unittest discover -s tests -v
```

Ví dụ ba DVD có tổng **63,89 USD**, hiển thị `Total cost: 63.89 $`.
Bản mã hiện tại có **14 kiểm thử** chạy thành công trên máy; huy hiệu CI phía
trên hiển thị trạng thái kiểm tra tự động trên GitHub.

## 4. Tài liệu đi kèm

| Tài liệu | Mục đích |
|---|---|
| [Đối chiếu nội dung và mốc kiểm tra](docs/submission-checklist.md) | Tra cứu nhánh, tag, PR và phạm vi lịch sử |
| [Hướng dẫn chạy lại](docs/reproduce.md) | Kiểm tra chương trình và đối chiếu các phiên bản |
| [Ca sử dụng AIMS-mini](docs/use-case.md) | Mô tả các thao tác và luồng xử lý chính |
| [Nhật ký thay đổi](CHANGELOG.md) | Xem những thay đổi của bản hiện tại |
| [Pull Requests](https://github.com/lnganhminh/it3180-202416556-aims-new/pulls?q=is%3Apr) | Xem các lần đề xuất và tích hợp thay đổi |
| [Releases](https://github.com/lnganhminh/it3180-202416556-aims-new/releases) | Tra cứu các bản phát hành đã công bố |

Phạm vi thực hiện và nguồn của lịch sử được ghi trong
[bảng đối chiếu](docs/submission-checklist.md#phạm-vi-lịch-sử).
