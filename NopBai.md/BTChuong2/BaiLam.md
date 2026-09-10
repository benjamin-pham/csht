# Bài Làm - Bài Tập Chương 2

## Kiến Trúc Hạ Tầng CNTT Doanh Nghiệp Thông Qua Khung Tham Chiếu

### 1. Khái niệm Mô hình hạ tầng tham chiếu (Reference Model)
Mô hình hạ tầng tham chiếu là một khung mô tả chuẩn dùng để phân loại, tổ chức và chuẩn hoá cách nhìn về các thành phần trong hạ tầng CNTT (bao gồm tính toán, lưu trữ, mạng, bảo mật, vận hành và dữ liệu). Khung tham chiếu không phải là một sản phẩm cụ thể mà là sơ đồ chỉ ra các lớp, miền năng lực và cách chúng liên kết với nhau.

### 2. Vai trò của Khung tham chiếu
- **Chuẩn hóa kiến trúc:** Tạo ra ngôn ngữ kiến trúc chung để các bộ phận (IT, Security, Data, Business) có thể dễ dàng giao tiếp và phối hợp.
- **Cơ sở thiết kế & Đánh giá:** Trở thành nền tảng tham chiếu để thiết kế, so sánh và đánh giá các phương án triển khai hạ tầng khác nhau (như On-premise, Cloud, Hybrid).
- **Nền tảng quản trị (Governance):** Hỗ trợ thiết lập các tiêu chuẩn, chính sách, kiểm soát rủi ro, cam kết chất lượng dịch vụ (SLA) và đảm bảo tính tuân thủ cho toàn bộ hệ thống.

### 3. Đặc điểm kỹ thuật của các mô hình triển khai hạ tầng
Dựa vào khung tham chiếu, các doanh nghiệp thường lựa chọn một trong ba mô hình triển khai chính:

- **Mô hình On-premise (Tại chỗ):**
  - *Đặc điểm:* Hạ tầng được đặt tại Data Center của tổ chức. Tổ chức tự chịu trách nhiệm toàn diện từ mua sắm, cấu hình, vận hành đến vá lỗi và nâng cấp.
  - *Ưu nhược điểm:* Khả năng kiểm soát và bảo mật vật lý cao, độ trễ thấp; tuy nhiên chi phí đầu tư ban đầu (CapEx) lớn và tốc độ mở rộng chậm.

- **Mô hình Cloud (Đám mây):**
  - *Đặc điểm:* Thuê tài nguyên hạ tầng từ nhà cung cấp (CSP) dưới dạng dịch vụ (IaaS, PaaS, SaaS) theo nhu cầu sử dụng (pay-as-you-go).
  - *Ưu nhược điểm:* Khả năng mở rộng (scale) nhanh chóng, linh hoạt, chuyển từ chi phí CapEx sang OpEx; nhưng cần chú ý quản trị chi phí (FinOps) và tuân thủ mô hình trách nhiệm chia sẻ (Shared Responsibility Model).

- **Mô hình Hybrid (Lai):**
  - *Đặc điểm:* Sự kết hợp và tích hợp sâu giữa On-premise và Cloud thông qua các kết nối chuyên dụng, đồng bộ danh tính, và luồng dữ liệu liên thông.
  - *Ưu nhược điểm:* Tối ưu hóa được từng loại workload (giữ dữ liệu cốt lõi tại chỗ, mở rộng trên cloud khi cần thiết); tuy nhiên độ phức tạp trong kiến trúc, vận hành và bảo mật là rất cao.

### 4. Khung tham chiếu 5 lớp năng lực cốt lõi
Một khung tham chiếu phổ biến thường được xây dựng dưới dạng ma trận 5 lớp năng lực kết hợp với 5 thành phần (Phần cứng, Phần mềm, Mạng, Quản trị, Bảo mật):
1. **Lớp Hạ tầng Tính toán & Kết nối (Compute & Connectivity):** Nền tảng vật lý và logic cung cấp khả năng xử lý, lưu trữ và kết nối mạng cơ bản.
2. **Lớp Nền tảng Vận hành (Ops Platform):** Cung cấp các công cụ và quy trình (Monitoring, ITSM, IaC, CI/CD) để tự động hoá, giám sát, và vận hành hạ tầng hiệu quả.
3. **Lớp Danh tính & Bảo mật (Security + Identity):** Lớp bảo vệ bao trùm, đảm bảo an toàn thông tin xuyên suốt (IAM, SSO, EDR, SIEM, Firewall, mã hóa).
4. **Lớp Nền tảng Ứng dụng & Tích hợp (App & Integration Platform):** Môi trường thực thi và kết nối ứng dụng, hỗ trợ kiến trúc linh hoạt như Microservices, Container (Kubernetes), API Gateway.
5. **Lớp Nền tảng Dữ liệu (Data Platform):** Xử lý lưu trữ, phân tích và quản trị vòng đời dữ liệu để phục vụ cho các quyết định kinh doanh và AI/ML.

### 5. Nguyên tắc thiết kế và vận hành theo khung tham chiếu
Khi xây dựng kiến trúc dựa trên khung tham chiếu, cần tuân thủ 5 nguyên tắc cốt lõi:
- **Tính sẵn sàng (Availability):** Đảm bảo hệ thống hoạt động liên tục (uptime) nhờ dự phòng (redundancy) và loại bỏ điểm lỗi đơn (SPOF).
- **Hiệu năng (Performance):** Đảm bảo khả năng xử lý và thời gian phản hồi nhanh, không bị nghẽn cổ chai (bottleneck) giữa Compute, Storage và Network.
- **Khả năng mở rộng (Scalability):** Cho phép tăng giảm tài nguyên (Scale-up hoặc Scale-out) đáp ứng linh hoạt sự thay đổi của tải công việc.
- **Chi phí (Cost / TCO):** Tối ưu hóa Tổng chi phí sở hữu (TCO), cân bằng giữa mức độ đầu tư, hiệu năng và độ ổn định.
- **Rủi ro (Risk):** Giảm thiểu rủi ro bảo mật và vận hành theo mô hình Phòng ngừa - Phát hiện - Ứng phó, thông qua các cơ chế sao lưu, khôi phục sau thảm họa (DR) và kiểm soát truy cập.

