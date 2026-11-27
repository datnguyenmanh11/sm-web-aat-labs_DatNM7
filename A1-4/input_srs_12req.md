| ID | Yêu cầu | Tiêu chí chấp nhận | Ưu tiên |
|---|---|---|---|
| REQ-SF-01 | Khách thêm sản phẩm vào giỏ từ trang chi tiết sản phẩm với số lượng chọn được. | Given đang ở trang chi tiết sản phẩm còn hàng, When chọn số lượng N và bấm "Thêm vào giỏ", Then giỏ có thêm N đơn vị sản phẩm đó và biểu tượng giỏ hiển thị số lượng mới. | Cao |
| REQ-SF-02 | Sản phẩm hết hàng không được thêm vào giỏ. | Given sản phẩm hiển thị "Hết hàng", Then nút thêm vào giỏ bị vô hiệu hoặc hệ thống báo lỗi, giỏ không thay đổi. | Cao |
| REQ-SF-03 | Số lượng mỗi sản phẩm trong giỏ từ 1 đến 10. | When nhập số lượng < 1 hoặc > 10, Then hệ thống không chấp nhận và hiển thị thông báo. | Cao |
| REQ-SF-04 | Khách thay đổi số lượng hoặc xóa dòng sản phẩm trong giỏ; tổng tiền cập nhật ngay. | When đổi số lượng hoặc xóa dòng, Then thành tiền dòng và tổng giỏ được tính lại đúng. | Cao |
| REQ-SF-05 | Giỏ hàng hiển thị nhanh. | — | Trung bình |
| REQ-SF-06 | Mua sỉ: khách mua từ 20 sản phẩm cùng loại trong một đơn được giảm 5% cho dòng đó. | When số lượng dòng ≥ 20, Then giảm 5% thành tiền dòng. | Trung bình |
| REQ-SF-07 | Giỏ hàng của khách đã đăng nhập được giữ lại khi đăng xuất và đăng nhập lại. | Given giỏ có sản phẩm, When đăng xuất rồi đăng nhập lại, Then giỏ còn nguyên. | Thấp |
| REQ-SF-10 | Checkout gồm 4 bước theo thứ tự: Giỏ hàng → Đăng nhập → Địa chỉ thanh toán → Phương thức thanh toán. | Không thể sang bước sau khi bước trước chưa hợp lệ. | Cao |
| REQ-SF-11 | Khách chưa đăng nhập phải đăng nhập hoặc đăng ký trước khi nhập địa chỉ. | Given chưa đăng nhập, When ở bước 2, Then hiển thị form đăng nhập/đăng ký. | Cao |
| REQ-SF-12 | Địa chỉ thanh toán bắt buộc: địa chỉ, thành phố, tỉnh/bang, quốc gia, mã bưu chính. | Thiếu một trường bắt buộc → không sang bước 4, hiển thị lỗi tại trường. | Cao |
| REQ-SF-15 | Phí vận chuyển: 25.000đ nội thành, 35.000đ tỉnh khác; **miễn phí vận chuyển cho đơn từ 300.000đ**. | Hiển thị phí ở bước xác nhận. *(Chưa triển khai trên UAT – kiểm thử ở mức thiết kế/review.)* | Trung bình |
| REQ-SF-16 | Giao diện thanh toán thân thiện với người dùng. | — | Trung bình |
