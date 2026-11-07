# Chạy lại và đối chiếu kết quả

## Chương trình hiện tại

```console
python main.py
python -m unittest discover -s tests -v
```

Demo cho tổng 63.89 USD. Bản 1.1.0 có 14 kiểm thử. Bộ kiểm thử dùng unittest
có sẵn trong Python, không yêu cầu cài gói bổ sung.

## Chạy một mốc phát hành

Khi working tree sạch, có thể chuyển sang tag rồi chạy lại mã:

```console
git status --short
git switch --detach v1.0.1
python main.py
python -m unittest discover -s tests -v
git switch master
```

Không tạo thay đổi cần lưu trên detached HEAD; nếu cần chỉnh mã hãy tạo nhánh mới.
Lab 01–02 chưa có bộ unittest và giữ lỗi giới hạn giỏ để phục vụ nội dung Lab 03.

## Đối chiếu bản vá

```console
git log --oneline v1.0.0..v1.0.1
git diff --stat v1.0.0 v1.0.1
git cat-file -t v1.0.1
git log --all --grep="cherry picked from"
```

Lệnh cat-file trả về `tag` với annotated tag. Tại v1.0.0, tìm `lion` không
khớp `The Lion King`; ở v1.0.1 và v1.1.0, tìm kiếm không phân biệt hoa thường.
Test `test_search_patch.py` kiểm tra các từ khóa `lion`, `LION` và `LiOn`.
