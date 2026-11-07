# Lab 01 — Cấu hình kho và tổ chức mã

## Global và local khác nhau ở đâu?
Thiết lập global áp dụng cho các kho của người dùng trên máy, thường nằm ở
`~/.gitconfig`. Cấu hình local nằm trong `.git/config` và ghi đè thiết lập
global tương ứng. Đặt tên và email ở local giúp các dự án dùng danh tính phù hợp.

## Tại sao dùng git mv khi refactor?
Lệnh này chuyển tệp và chuẩn bị thay đổi trong staging cùng lúc. Ví dụ, sau
`git mv cart.py aims/cart.py`, cần sửa import của chương trình chạy chính.
Git nhận diện đổi tên bằng cách so sánh nội dung snapshot; không có một đối
tượng riêng lưu thao tác rename. `git log --follow -- aims/cart.py` giúp tra
lại lịch sử của tệp trước khi chuyển thư mục.

## Khi nào release/lab01 là baseline?
Khi chọn một commit trên nhánh làm mốc nộp và kiểm soát các thay đổi tiếp theo.
Nhánh có thể tiến lên, nên tag annotated và SHA giúp chỉ rõ phiên bản ban đầu.

## Vì sao làm cá nhân vẫn cần PR?
PR gom thay đổi thành một mục đích cụ thể và lưu kết quả kiểm tra trước khi
tích hợp. Chế độ cá nhân dùng 0 approval; các thay đổi vẫn đi qua PR.

## Ba vùng làm việc
`restore` bỏ sửa đổi chưa stage; `restore --staged` lấy thay đổi ra khỏi staging
nhưng giữ nội dung trong working tree. Amend chỉ phù hợp với commit chưa chia sẻ.
Kho này dùng HTTPS và Git Credential Manager; chưa thực hiện bước SSH của đề.
