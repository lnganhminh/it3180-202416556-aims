# Lab 05 — Bản vá và bảo trì nhiều phiên bản

## Sửa master trước hay release trước?
Upstream first bảo đảm dòng phát triển mới có bản sửa trước, sau đó backport
về các bản cũ. Release first bắt đầu đúng phiên bản gặp sự cố nên dễ giới hạn
phạm vi bản vá, nhưng phải theo dõi việc chuyển sửa đổi sang các dòng còn lại.

## Làm sao biết một dòng đã nhận bản sửa?
Chạy test hồi quy trên từng dòng để xác nhận hành vi. Kiểm tra tổ tiên bằng
`git tag --contains FIX_SHA` chỉ tìm đúng commit gốc. Cherry-pick sinh SHA
khác, nên tag không chứa SHA gốc chưa chứng minh rằng thiếu bản vá.
`git cherry -v release/lab05 release/lab04` giúp tìm patch tương đương;
dấu trừ cho biết thay đổi tương ứng đã có ở nhánh đích.

## Tại sao tách sửa lỗi và tăng version?
Phần mã và test có thể chuyển giữa các dòng, còn số phiên bản phải giữ đúng
với từng dòng. Mang cả commit tăng 1.0.1 sang dòng 1.1.x có thể hạ sai version.

## Vì sao chờ kiểm tra xong mới đặt tag?
Tag phát hành xác định một bản cụ thể. Nếu cần thêm hotfix, phải hoàn thành
và kiểm tra trước khi chốt. Khi tag đã công bố, phát hành số mới thay vì di chuyển tag.

## Tìm kiếm và sắp xếp
Chuẩn hóa từ khóa một lần bằng casefold trước khi duyệt. Cách này hỗ trợ
so sánh không phân biệt hoa thường, kể cả một số ký tự Unicode. Tìm thể loại
so sánh toàn bộ tên thể loại, còn tìm tiêu đề chấp nhận chuỗi con. Sắp xếp chỉ
đổi thứ tự, không được làm mất DVD hoặc thay tổng tiền.
