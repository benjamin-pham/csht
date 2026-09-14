# Buổi 7: Tài nguyên mạng, Dịch vụ mạng và Quản trị hệ thống

## 1. Nội dung bài giảng

### Chương 5: Tài nguyên mạng và các dịch vụ mạng cơ bản
*   **Các khái niệm cơ bản:**
    *   **Mạng nội bộ (LAN):** Kết nối các thiết bị trong phạm vi nhỏ (phòng, lớp học, tòa nhà) giúp trao đổi dữ liệu, dùng chung thiết bị, quản lý tập trung. Ưu điểm: Tốc độ cao, chi phí hợp lý, an toàn (nếu không kết nối internet bên ngoài).
    *   **Internet:** Hệ thống liên kết mạng toàn cầu cung cấp nhiều dịch vụ (web, email, lưu trữ). Đòi hỏi các biện pháp kiểm soát và định danh như địa chỉ IP.
    *   **Địa chỉ IP:** Đóng vai trò như địa chỉ nhà để nhận dạng thiết bị. Có các loại: IP nội bộ, IP công cộng, IP tĩnh (máy chủ, camera) và IP động (người dùng).
*   **Mô hình kết nối:**
    *   **Ngang hàng (Peer-to-Peer):** Các máy tính chia sẻ trực tiếp, dễ triển khai nhưng khó quản lý quy mô lớn.
    *   **Máy khách - Máy chủ (Client-Server):** Phù hợp doanh nghiệp, trường học. Phụ thuộc bên thứ 3 (máy chủ) nhưng hỗ trợ quản lý tập trung tốt.
*   **Các thiết bị mạng cơ bản:**
    *   **Thiết bị đầu cuối:** Máy tính, điện thoại, máy in, camera.
    *   **Switch:** Kết nối nhiều thiết bị trong mạng nội bộ, tăng hiệu quả truyền dữ liệu.
    *   **Router:** Kết nối mạng nội bộ với internet hoặc liên kết các mạng, định tuyến đường truyền.
    *   **Firewall (Tường lửa):** Thiết bị/phần mềm kiểm soát lưu lượng, chặn truy cập trái phép, bảo vệ hệ thống mạng.
*   **Các dịch vụ mạng nền tảng:**
    *   **DNS:** Chuyển đổi tên miền thành địa chỉ IP.
    *   **DHCP:** Cấp phát IP tự động, tránh trùng lặp.
    *   **VPN:** Tạo kết nối an toàn từ xa qua internet, bảo mật dữ liệu, thích hợp cho làm việc từ xa hoặc truy cập tài nguyên nội bộ công ty.
*   **Giám sát kết nối mạng:** Theo dõi trạng thái thiết bị, băng thông, độ trễ, và gói tin bị mất nhằm phát hiện sớm sự cố và đảm bảo an toàn.

### Chương 6: Quản trị hệ thống và vận hành hạ tầng
*   **Quản lý người dùng:** 
    *   Cấp quyền đúng người, đúng thời điểm, đúng phạm vi. Mỗi người dùng phải có tài khoản riêng để kiểm soát trách nhiệm, tránh dùng chung.
    *   Tài khoản không dùng hoặc nhân viên nghỉ việc phải bị vô hiệu hóa ngay. Không giao tài khoản cá nhân của mình cho bất kỳ ai (kể cả admin/nhân viên IT).
*   **Phân quyền truy cập:** 
    *   Nguyên tắc: Cấp quyền tối thiểu (Least Privilege). 
    *   Hình thức phổ biến hiện nay: Phân quyền theo vai trò (Role-based).
*   **Quản lý cấu hình:** Thiết lập tiêu chuẩn vận hành đồng nhất, lưu lại lịch sử các thay đổi để dễ dàng khôi phục khi có sự cố hệ thống.
*   **Nhật ký hệ thống (Log):** Ghi lại hoạt động đăng nhập, cảnh báo lỗi,... theo dõi bất thường, phục vụ kiểm toán và phân tích khai thác dữ liệu hành vi.
*   **Sao lưu & Khôi phục (Backup & Recovery):** Phòng ngừa thiên tai, mã độc, xóa nhầm. Yêu cầu dự kiến máy chủ ở nhiều nơi và có cơ chế khôi phục rõ ràng (Ví dụ: sự cố Amazon).
*   **Cam kết dịch vụ (SLA):** Các tiêu chuẩn đảm bảo như thời gian uptime (ví dụ 99%, 99.9%), thời gian phản hồi và khôi phục khi có sự cố.
*   **Quy trình xử lý sự cố (6 bước):** Phát hiện/Tiếp nhận -> Phân loại mức độ ảnh hưởng (B1-B4) -> Phân công -> Khắc phục tạm thời -> Khôi phục dịch vụ -> Tổng kết nguyên nhân và phòng ngừa.
*   **Quản lý tài sản công nghệ thông tin:** Quản lý toàn bộ vòng đời tài sản để tối ưu hóa mức đầu tư, kiểm soát chi phí.
*   **Dự toán chi phí & Chuẩn hóa:** Ước tính chi phí đầu tư ban đầu, chi phí vận hành định kỳ theo từng giai đoạn và chuẩn hóa tài liệu vận hành.

---

## 📝 Bài tập & Đồ án

### Bài tập về nhà
- **Nội dung:** Bài tập lập kế hoạch giai đoạn 2.
- **Yêu cầu thực hiện:** 
  - Đại diện nhóm tạo thư mục bài tập (bên trong chia thành 2 thư mục con: đồ án môn học và bài thực hành để cô dễ chấm).
  - Nộp link bài tập trong **tối nay** (trước). Sau đó phân công các thành viên tiến hành làm các bước.

### Đồ án môn học (Bước 5 đến Bước 8)
- **Nhiệm vụ:** Lập danh mục yêu cầu kỹ thuật, danh mục đầu tư, kế hoạch triển khai và dự toán chi phí.
- **Lưu ý cực kỳ quan trọng:** Phải có sự **thống nhất xuyên suốt** từ trên xuống dưới (Mục tiêu dự án -> KPI -> Kiến trúc -> Yêu cầu kỹ thuật -> Hạng mục đầu tư). 
- Dự toán chi phí phải được phân rã theo từng giai đoạn (mua sắm, triển khai, vận hành, bảo trì), tổng chi phí các giai đoạn phải bằng với tổng kinh phí đề xuất ban đầu.

### Bài thực hành (Bước 9)
- **Nhiệm vụ:** Tập trung vào các yêu cầu nghiệp vụ, chức năng/phi chức năng và kiến trúc phần mềm (Web, Application, Data).
- Lập kế hoạch triển khai dựa trên vòng đời phát triển phần mềm (khảo sát, thiết kế, phát triển, kiểm thử, vận hành).
- **Dự toán chi phí phần mềm:** Tập trung vào các phần như chi phí bản quyền (license), nhân công phát triển, thuê/mua hạ tầng, bảo mật, và đào tạo chuyển giao. Tính thống nhất cũng phải được đặt lên hàng đầu.

---

## 📌 Yêu cầu & Nhắc nhở

1. **Tiến độ chung:** Lớp chỉ còn 1 buổi (buổi 8) để hoàn thiện toàn bộ các nội dung còn lại trước khi tiến hành thi vấn đáp. Các nhóm phải tuân thủ đúng tiến độ.
2. **Quy cách nộp báo cáo:** File kết quả nộp cho cô chấm (File final) phải được đặt bên ngoài cùng của thư mục chính, không được giấu sâu bên trong để cô dễ dàng truy cập.
3. **Tuyệt đối không copy-paste bài tập vào Form báo cáo chung:** 
   - Không được gom tất cả các bài tập từng bước và bê nguyên vào báo cáo tổng hợp.
   - Báo cáo tổng hợp/Thuyết minh đề tài phải được viết lại, chuẩn hóa theo mục lục chuẩn của Form mẫu cung cấp.
   - Các thuật ngữ, đơn vị đo, ký hiệu phải được sử dụng đồng nhất, nhất quán trong toàn bộ báo cáo.
4. **Kiểm tra chéo:** Phải có một người rà soát tổng hợp cuối cùng để đảm bảo các thành viên làm không bị lệch chuẩn (trên nói một đằng, dưới làm một nẻo).
5. **Góp ý riêng cho một số nhóm:** 
   - **Nhóm làm AI (Deepfake - Nhóm 10):** Khi áp dụng công nghệ mới vào quy trình (như dùng model AI detect Deepfake), cần có 2 hệ thống KPI tách biệt: KPI vận hành phần mềm và KPI đánh giá độ chính xác của model (ví dụ: Precision, Tỷ lệ detect đúng).
   - **Mẹo làm đề tài ngân sách:** Xác định tên đề tài -> Nhân lực tương ứng -> Sản phẩm/KPI tương ứng -> Chi phí phù hợp để tránh bị vướng mắc khi bảo vệ, thanh tra, kiểm toán kinh phí.
