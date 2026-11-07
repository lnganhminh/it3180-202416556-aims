# Lab 02 — Nhánh tính năng và tích hợp

## Đồng bộ master trước khi gửi PR có tác dụng gì?
Một tính năng có thể chạy đúng trên nền mã cũ nhưng gặp lỗi sau khi ghép với
thay đổi mới. Fetch rồi merge master vào nhánh làm việc cho phép phát hiện
xung đột và kiểm tra tổ hợp mã trước khi tích hợp.

## Có nên rebase mọi nhánh không?
Không. Rebase tạo lại commit với SHA khác. Nếu người khác đang dùng lịch sử
cũ, họ phải xử lý phân kỳ. Với master, release hoặc nhánh đã chia sẻ, nên
thêm commit sửa hay revert; chỉ sửa lịch sử nhánh riêng chưa công bố.

## Feature và topic
Hai tiền tố mô tả mục đích công việc. Feature thay đổi chức năng, chẳng hạn
in giỏ hoặc tìm DVD; topic có thể bổ sung tài liệu và mẫu PR. Git quản lý
cả hai như những nhánh thông thường.

## Chọn cách merge
Merge commit giữ cấu trúc phân nhánh, phù hợp khi cần theo dõi quá trình làm.
Squash gom một yêu cầu thành một commit, thuận tiện để revert cả yêu cầu.
Rebase and merge tạo lịch sử thẳng nhưng thay SHA và có thể phải hoàn tác
nhiều commit. Khi revert merge, cần xác định đúng parent chính với `-m`.

## Cách hiển thị giỏ
Giỏ rỗng có thông báo riêng. Giỏ có dữ liệu hiển thị số lượng, các dòng DVD
đánh số từ 1 và tổng tiền. Tìm kiếm trả danh sách mới để giữ nguyên dữ liệu đầu vào.
