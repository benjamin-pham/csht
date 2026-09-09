# Buổi 7

## Các khái niệm cơ bản về mạng
- **Mạng nội bộ (LAN)**: Kết nối các thiết bị trong phạm vi nhỏ (phòng làm việc, lớp học, tòa nhà) để trao đổi dữ liệu, dùng chung thiết bị, quản lý tập trung. Đặc điểm: Tốc độ cao, chi phí hợp lý, an toàn.
- **Internet**: Hệ thống kết nối thiết bị trên toàn thế giới, cung cấp nhiều dịch vụ (web, email, lưu trữ đám mây). Được hình thành từ nhiều mạng liên kết với nhau.
- **Địa chỉ IP**: Giống như địa chỉ nhà, dùng để nhận biết thiết bị khi tham gia mạng và giúp các nhà cung cấp mạng quản lý, truy vết. Các loại IP: IP nội bộ, IP công cộng, IP tĩnh (cho máy chủ, camera - ít thay đổi), IP động (tự động cấp phát).

## Mô hình kết nối mạng
- **Thiết bị đầu cuối**: Máy tính, điện thoại, máy in, camera, v.v.
- **Mô hình ngang hàng (P2P)**: Máy chủ chia sẻ trực tiếp với nhau. Phù hợp mạng nhỏ, dễ triển khai nhưng khó quản lý ở quy mô lớn.
- **Mô hình Client-Server (Máy khách - Máy chủ)**: Máy khách gửi yêu cầu, máy chủ cung cấp dữ liệu. Phù hợp doanh nghiệp, trường học. Nhược điểm là phụ thuộc vào bên thứ ba quản lý máy chủ (vấn đề bảo mật, quyền riêng tư do dữ liệu bị bên thứ ba nắm giữ).

## Các thiết bị mạng cơ bản
- **Switch**: Thiết bị kết nối nhiều thiết bị trong mạng LAN, mở rộng số lượng kết nối, tăng hiệu quả truyền dữ liệu.
- **Router (Bộ định tuyến)**: Kết nối mạng nội bộ với internet hoặc giữa các mạng với nhau. Giúp định tuyến đường truyền và chọn đường đi tối ưu cho gói tin.
- **Firewall (Tường lửa)**: Có thể là phần mềm hoặc thiết bị phần cứng, giúp kiểm soát lưu lượng ra vào, chặn truy cập trái phép, tăng cường an toàn mạng.

## Các dịch vụ mạng nền tảng
- **DNS**: Chuyển đổi tên miền thành địa chỉ IP (đóng vai trò như một danh bạ).
- **DHCP**: Cấp IP tự động cho các thiết bị, giảm thiểu cấu hình thủ công và tránh trùng lặp IP.
- **VPN**: Tạo kết nối an toàn giữa người dùng và mạng nội bộ từ xa qua internet. Giúp mã hóa lưu lượng, hạn chế rủi ro khi dùng wifi công cộng.

## Giám sát kết nối mạng
- **Mục đích**: Theo dõi trạng thái thiết bị, băng thông, độ trễ, tỉ lệ mất kết nối nhằm phát hiện sự cố sớm và nâng cao độ ổn định của mạng.

## Quản trị hệ thống và vận hành hạ tầng (Chương 6)

### Nguyên tắc quản lý người dùng
- **Quản lý vòng đời tài khoản**: Quá trình tạo, cập nhật, tạm ngưng và thu hồi tài khoản. Khi nhân sự nghỉ việc phải vô hiệu hóa tài khoản ngay lập tức.
- **Cấp quyền chính xác**: Phải cấp đúng quyền, đúng người, đúng thời điểm và đúng phạm vi để kiểm soát truy vết, đảm bảo hệ thống bảo mật và đáng tin cậy. Tránh việc cấp quyền sai (VD: cấp quyền nhập điểm cho sinh viên).
- **Mỗi người dùng có tài khoản riêng**: Hành động của tài khoản đại diện cho hành động của cá nhân đó. Tuyệt đối không giao thông tin tài khoản, mật khẩu cho người khác (kể cả quản trị viên) để tránh bị lừa đảo.
- **Phân quyền**: Chỉ cấp quyền tối thiểu cần thiết cho công việc. Tránh việc một người nắm toàn bộ quy trình quan trọng. Thường áp dụng phân quyền theo vai trò (Role-based).
- **Không dùng chung tài khoản quản trị**.

### Quản lý cấu hình
- Là tập hợp các tham số, thiết lập, tiêu chuẩn vận hành của hệ thống (cấu hình máy chủ, mạng, ứng dụng, bảo mật).
- **Mục tiêu**: Tránh sai lệch giữa các môi trường, hỗ trợ triển khai đồng nhất, giảm lỗi do thay đổi tùy tiện và dễ dàng khôi phục khi có sự cố. Cần lưu lại lịch sử các phiên bản cấu hình.

### Quản lý nhật ký (Logs)
- Ghi lại các sự kiện trên hệ thống: đăng nhập/xuất, thay đổi cấu hình, truy cập ứng dụng, lỗi, bảo mật.
- **Mục tiêu**: Theo dõi hoạt động, phát hiện bất thường, điều tra sự cố, phục vụ kiểm toán và tuân thủ quy định. Log còn được dùng trong phân tích hành vi người dùng.

### Sao lưu và khôi phục (Backup & Restore)
- **Sao lưu**: Tạo bản sao dữ liệu phòng trường hợp mất mát (do xóa nhầm, lỗi phần cứng, mã độc, thiên tai).
- **Khôi phục**: Cơ chế phục hồi dữ liệu/dịch vụ sau sự cố. Đối với các hệ thống lớn, cần lưu trữ máy chủ ở nhiều vị trí địa lý khác nhau để dự phòng rủi ro thiên tai.

### SLA (Service Level Agreement) và Giám sát hệ thống
- **SLA**: Độ đo cam kết chất lượng dịch vụ giữa đơn vị cung cấp và người sử dụng. Ví dụ: Cam kết thời gian Uptime (như 99.9%), thời gian khôi phục sự cố nhanh chóng.
- **Giám sát**: Theo dõi liên tục tình trạng hạ tầng/dịch vụ để phát hiện sớm bất thường, cảnh báo trước khi dịch vụ bị gián đoạn.

### Quy trình xử lý sự cố và Quản trị tài sản
- **Quy trình xử lý sự cố cơ bản**: Phát hiện & tiếp nhận -> Phân loại mức độ ảnh hưởng -> Phân công & xử lý -> Khắc phục tạm thời -> Khôi phục dịch vụ -> Tổng kết nguyên nhân & phòng ngừa. Phải ưu tiên khôi phục dịch vụ trước.
- **Quản trị tài sản**: Quản lý các tài sản CNTT trong suốt vòng đời của chúng, kiểm soát chi phí đầu tư.

---

## 📝 Bài tập & Đồ án

**Đồ án môn học:**
- **Nhiệm vụ**: Thực hiện tiếp từ bước 5 đến bước 8.
- **Yêu cầu kỹ thuật**: Phải được xây dựng thống nhất với các mục tiêu, phạm vi và KPI (như các lớp năng lực, kiến trúc hệ thống) đã xác định ở các bước trước. Đảm bảo yêu cầu kỹ thuật khớp với tiêu chí nghiệm thu.
- **Lập danh mục đầu tư**: Lên danh sách chi tiết các thiết bị phần cứng, phần mềm bản quyền và dịch vụ cần đầu tư.
- **Dự toán chi phí**: Phân tích chi phí theo từng giai đoạn (mua sắm ban đầu, triển khai, bảo trì, vận hành định kỳ). **Lưu ý**: Tổng chi phí các giai đoạn phải bằng tổng kinh phí đề xuất ban đầu.
- **Tổng hợp báo cáo**: Khi viết báo cáo, không được chỉ copy/paste các bước làm bài tập gộp lại một cách rời rạc. Phải **chuẩn hóa báo cáo** theo một form/mục lục thống nhất, chuẩn hóa các ký hiệu độ đo, công thức tính toán để đảm bảo tính chuyên nghiệp.

**Bài tập thực hành:**
- **Nhiệm vụ**: Làm tiếp đến bước 9 (Lập kế hoạch giai đoạn 2).
- **Nội dung**:
  - Xác định các yêu cầu nghiệp vụ, yêu cầu chức năng và phi chức năng.
  - Xây dựng kiến trúc phần mềm tổng thể (Application, Web Server, Database...).
  - Xây dựng **kế hoạch triển khai phần mềm** theo quy trình: Khảo sát phân tích -> Thiết kế -> Phát triển -> Kiểm thử -> Triển khai -> Vận hành bảo trì.
  - **Dự toán chi phí phần mềm**: Tính toán chi phí license bản quyền, nhân công phát triển, thuê hạ tầng/server, giải pháp bảo mật và chi phí đào tạo chuyển giao.
- **Quy cách nộp bài**: Tạo folder lưu trữ rõ ràng, tách biệt giữa bài Thực hành và Đồ án môn học. Gom vào một file nén (.zip/.rar) đặt ở ngoài cùng để giảng viên dễ dàng chấm bài.

---

## ⚠️ Yêu cầu & Nhắc nhở

- **Deadline**: Đại diện (thư ký/trưởng nhóm) nộp đường link nộp bài tập trong tối hôm nay. Sau đó nhóm tự phân công công việc tiếp theo vì thời gian đến lúc thi vấn đáp không còn nhiều.
- **Tính xuyên suốt**: Khi làm bài, cần đảm bảo tính logic xuyên suốt từ mục tiêu ban đầu đến giải pháp, yêu cầu kỹ thuật và dự toán. Bắt buộc phải có thành viên rà soát, kiểm định lại toàn bộ nội dung tổng hợp để tránh tình trạng râu ông nọ cắm cằm bà kia.
- **Hỏi đáp với Giảng viên**: Khi có thắc mắc trong quá trình làm bài, sinh viên cần đặt câu hỏi rõ ràng, gắn chặt với ngữ cảnh bài toán của nhóm (VD: Thắc mắc về việc áp dụng Deepfake để chống giả mạo khuôn mặt trong app ngân hàng) để được hướng dẫn chính xác.
