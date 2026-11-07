# Lab 04 — Chốt phiên bản phát hành

## Vì sao không ghép toàn bộ release về master?
Trong flow của học phần, release duy trì một dòng phiên bản cụ thể. Ghép cả
nhánh có thể kéo version và tài liệu của dòng cũ về master. Nên chuyển đúng
commit sửa lỗi cần thiết, rồi cập nhật metadata riêng cho mỗi dòng.

## Khác biệt với GitFlow
Bài này dùng master làm nơi tích hợp và release/labXX làm các dòng nộp bài.
GitFlow truyền thống có thêm develop cho phát triển, còn main/master chứa
các bản ổn định. Vì ít nhánh dài hạn hơn, flow của bài thuận tiện cho dự án nhỏ.

## Ý nghĩa của 1.0.0
Đây là mốc công bố phạm vi sử dụng ổn định đầu tiên. SemVer không bắt buộc
Lab 04 phải mang số 1.0.0; 0.4.0 vẫn hợp lý nếu giao diện còn đang thử nghiệm.
Sau mốc ổn định, bản vá dùng patch và tính năng tương thích dùng minor.

## Vì sao chuẩn bị phiên bản trước khi rẽ release?
Đưa version, test và tài liệu qua PR vào master trước giúp nhánh release xuất
phát từ một trạng thái đã kiểm tra. Tag giữ nguyên mốc gốc dù nhánh release
về sau nhận thêm hotfix.

## Các lệnh đối chiếu
`git log A..B` liệt kê commit thuộc B nhưng không thuộc A. `git diff A B`
so sánh nội dung. `git describe --tags` mô tả vị trí so với tag tổ tiên.
Dùng `git archive` khi cần xuất mã tại một mốc để chạy lại.
