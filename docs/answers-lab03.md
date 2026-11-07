# Lab 03 — Kiểm tra lỗi và hoàn tác

## Merge base dùng để làm gì?
Git cần một tổ tiên chung để biết mỗi nhánh đã đổi gì. Merge base là tổ tiên
chung tốt nhất dùng trong phép hợp nhất ba chiều. Có thể xem bằng
`git merge-base A B`; lịch sử phức tạp có thể có nhiều merge base.

## Vì sao ưu tiên revert trên master và release?
Các nhánh này có thể đã được người khác tải về. Revert tạo commit đảo ngược
thay đổi nên vẫn giữ được đường đi của lịch sử. Reset di chuyển con trỏ nhánh
và có thể làm mất liên hệ với các commit đã chia sẻ.

## Phân biệt ba kiểu reset
Soft giữ thay đổi trong staging. Mixed giữ nội dung ở working tree nhưng
bỏ stage. Hard đưa cả working tree và staging về commit đích; cần đặc biệt
cẩn thận với phần sửa chưa lưu. Reflog hỗ trợ tìm lại vị trí con trỏ local,
nhưng có thời hạn và không được đẩy lên remote.

## Trường hợp biên cần kiểm tra
Giỏ có tối đa 20 DVD, lần thêm thứ 21 phải trả False. Xóa một DVD không tồn
tại không làm thay đổi giỏ. Nếu có hai DVD bằng nhau, một lần xóa chỉ bỏ một
phần tử. Với giảm giá, 0% giữ nguyên tổng, 100% cho kết quả 0 và tỷ lệ ngoài
khoảng 0–100 phải bị từ chối.

## Khi gặp conflict
Đọc cả hai thay đổi và mục đích của chúng trước khi chọn kết quả. Xóa các dấu
conflict, chạy lại chương trình và test rồi mới commit phần giải quyết.
