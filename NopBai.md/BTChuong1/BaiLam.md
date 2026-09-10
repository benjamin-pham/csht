# Bài Làm - Bài Tập Chương 1

## Câu 1: Khái niệm và vai trò của các thành phần của 5 lớp năng lực trong hạ tầng CNTT (Công nghệ Thông tin)

Theo khung kiến trúc hạ tầng Công nghệ Thông tin, một hệ thống doanh nghiệp vững chắc cần được xây dựng đồng bộ dựa trên 5 lớp năng lực cốt lõi. Mỗi lớp đều có các thành phần từ phần cứng, phần mềm, mạng đến quản trị và bảo mật nhằm đảm bảo hệ thống vận hành liên tục và hỗ trợ quá trình chuyển đổi số.

### 1. Lớp Hạ tầng Tính toán & Kết nối (Compute & Connectivity)
- **Khái niệm & Vai trò**: Là nền tảng cơ bản nhất, bao gồm các thành phần vật lý và mạng lưới truyền dẫn, cung cấp tài nguyên xử lý tính toán, lưu trữ và kết nối mạng. Lớp này đảm bảo hệ thống có đủ sức mạnh để vận hành ứng dụng và khả năng giao tiếp xuyên suốt.
- **Thành phần tiêu biểu**:
  - *Phần cứng*: Máy chủ (Server), Máy tính cá nhân (PC - Personal Computer), Thiết bị lưu trữ (Storage), Thiết bị đầu cuối (Endpoint).
  - *Phần mềm/Mạng*: Hệ điều hành nền tảng (OS - Operating System), Hypervisor, LAN (Local Area Network)/WAN (Wide Area Network), VPC (Virtual Private Cloud)/VNET (Virtual Network) (trên đám mây), Switch, Router, Firewall, VPN (Virtual Private Network).

### 2. Lớp Nền tảng Vận hành (Ops Platform)
- **Khái niệm & Vai trò**: Cung cấp các công cụ và quy trình để duy trì, giám sát, và quản lý hạ tầng một cách ổn định. Lớp này đảm bảo tính liên tục của doanh nghiệp thông qua việc phát hiện lỗi sớm và tự động hóa quy trình quản trị hệ thống.
- **Thành phần tiêu biểu**:
  - *Công cụ giám sát*: Hệ thống theo dõi trạng thái và hiệu suất (Monitoring/Observability).
  - *Công cụ quản trị & tự động hóa*: ITSM (Information Technology Service Management), CMDB (Configuration Management Database), Patching/Orchestration, Cơ sở hạ tầng dưới dạng mã (IaC - Infrastructure as Code).
  - *Sao lưu & Phục hồi*: Công cụ sao lưu dữ liệu (Backup) và phục hồi sau thảm họa (DR - Disaster Recovery tooling) để đảm bảo an toàn thông tin.

### 3. Lớp Danh tính & Bảo mật (Security + Identity)
- **Khái niệm & Vai trò**: Là lớp bao trùm và xuyên suốt từ tầng vật lý đến tầng dữ liệu. Hoạt động như một hệ thống bảo vệ toàn diện, bảo đảm an toàn thông tin theo mô hình CIA (Confidentiality, Integrity, Availability - Tính bảo mật, Tính toàn vẹn, Tính sẵn sàng) và kiểm soát quyền truy cập một cách nghiêm ngặt.
- **Thành phần tiêu biểu**:
  - *Xác thực & Danh tính*: IAM (Identity and Access Management), SSO (Single Sign-On), MFA (Multi-Factor Authentication), PAM (Privileged Access Management).
  - *Bảo mật hệ thống & mạng*: EDR (Endpoint Detection and Response)/XDR (Extended Detection and Response), SIEM (Security Information and Event Management)/SOAR (Security Orchestration, Automation, and Response), ZTNA (Zero Trust Network Access)/VPN (Virtual Private Network), Firewall/WAF (Web Application Firewall).
  - *Bảo mật dữ liệu*: Chống rò rỉ dữ liệu (DLP - Data Loss Prevention), Hệ thống quản lý khóa mã hóa (KMS - Key Management Service).

### 4. Lớp Nền tảng Ứng dụng & Tích hợp (App & Integration Platform)
- **Khái niệm & Vai trò**: Cung cấp môi trường thực thi, kết nối và tích hợp các ứng dụng cũng như dịch vụ nội bộ và đối tác. Lớp này giúp quá trình chuyển đổi số diễn ra nhanh chóng, hỗ trợ kiến trúc linh hoạt (như microservices) và quy trình giao hàng liên tục (DevSecOps - Development, Security, and Operations).
- **Thành phần tiêu biểu**:
  - *Môi trường chạy*: Container, Kubernetes, Microservices.
  - *Tích hợp & Giao tiếp*: Middleware/ESB (Enterprise Service Bus), API (Application Programming Interface) Gateway, Message queue/Event bus.
  - *Quản trị ứng dụng*: Chuỗi quy trình CI/CD (Continuous Integration/Continuous Deployment), Service mesh.

### 5. Lớp Nền tảng Dữ liệu (Data Platform)
- **Khái niệm & Vai trò**: Là trung tâm xử lý của hệ thống hiện đại. Lớp này đóng vai trò cốt lõi trong việc thu thập, lưu trữ, xử lý, làm sạch và quản trị dữ liệu. Dữ liệu chuẩn xác và đáng tin cậy là nền tảng thiết yếu để triển khai Trí tuệ nhân tạo (AI - Artificial Intelligence), Học máy (Machine Learning) và Phân tích nghiệp vụ (BI - Business Intelligence).
- **Thành phần tiêu biểu**:
  - *Lưu trữ & Xử lý*: Hệ quản trị cơ sở dữ liệu (DBMS - Database Management System), Data Warehouse, Data Lake/Lakehouse.
  - *Luân chuyển & Làm sạch*: ETL (Extract, Transform, Load)/ELT (Extract, Load, Transform), Xử lý luồng (Streaming).
  - *Quản trị dữ liệu*: Data Catalog, Công cụ đánh giá chất lượng dữ liệu, Data governance, Mã hóa và ẩn danh dữ liệu.

---

## Câu 2: Khái niệm, vai trò và cách thức đo lường các bộ chỉ số KPI (Key Performance Indicators)

### Khái niệm
KPI (Key Performance Indicators) trong lĩnh vực Công nghệ Thông tin là tập hợp các chỉ số định lượng trọng yếu được sử dụng để đánh giá mức độ hiệu quả, độ ổn định, khả năng chuyển đổi số, và mức độ đóng góp của hệ thống Công nghệ Thông tin vào mục tiêu kinh doanh chung của tổ chức.

### Vai trò
- Chứng minh hệ thống được vận hành hiệu quả, tối ưu hiệu suất và sử dụng ngân sách hợp lý.
- Cân bằng giữa việc duy trì sự ổn định của hệ thống hiện tại và tốc độ linh hoạt trong việc đổi mới chuyển đổi số.
- Đo lường mức độ trưởng thành của tiến trình chuyển đổi số nhằm đảm bảo sự phát triển bền vững trong dài hạn.
- Giám sát các rủi ro bảo mật và mức độ tuân thủ quy định, cung cấp dữ liệu minh bạch hỗ trợ cho các quyết định đầu tư chiến lược.

### Cách thức đo lường các bộ chỉ số (IT Metrics)
Dựa trên hệ sinh thái quản trị và vận hành, KPI Công nghệ Thông tin được phân loại và đo lường qua 4 nhóm chính:

**1. Nhóm Vận hành (Độ tin cậy của CNTT - IT Reliability)**
- **Uptime / Availability**: Tỷ lệ phần trăm thời gian hệ thống hoạt động liên tục không bị gián đoạn (theo cam kết SLA - Service Level Agreement).
- **MTTR (Mean Time To Recover)**: Thời gian trung bình để xử lý và khôi phục hoạt động khi xảy ra sự cố nghiêm trọng (P1 - Priority 1 / P2 - Priority 2).
- **RPO/RTO & Backup Success Rate**: Tỷ lệ hoàn thành sao lưu thành công và khả năng phục hồi dữ liệu (RPO - Recovery Point Objective / RTO - Recovery Time Objective) đáp ứng đúng mức cam kết khi đối mặt với thảm họa.

**2. Nhóm Chuyển đổi (Tốc độ & Tính linh hoạt - Delivery & Agility)**
- **DORA (DevOps Research and Assessment) Metrics**: 
  - *Tần suất triển khai (Deployment frequency)*.
  - *Thời gian chờ thay đổi (Lead time for change)*: Thời gian tính từ thời điểm tiếp nhận yêu cầu đến khi thay đổi được triển khai thành công vào môi trường thực tế.
  - *Tỷ lệ thất bại khi thay đổi (Change failure rate)*: Tỷ lệ các thay đổi gây ra sự cố cho hệ thống.
- **Thời gian tích hợp (API - Application Programming Interface time)**: Thời gian cần thiết để kết nối và tích hợp các hệ thống mới hoặc hệ thống của đối tác.
- **Tỷ lệ số hóa**: Tỷ lệ phần trăm các quy trình nghiệp vụ được số hóa toàn trình (end-to-end).

**3. Nhóm Dữ liệu & An ninh (Dữ liệu và Bảo mật - Data & Security)**
- **Chất lượng dữ liệu (Data Quality)**: Đo lường tính đầy đủ, độ chính xác, tính nhất quán và khả năng cập nhật kịp thời của hệ thống dữ liệu.
- **Chỉ số sự cố an ninh**: Số lượng các sự kiện an ninh mạng nghiêm trọng, thời gian phát hiện và thời gian ứng cứu (từ thời điểm bị xâm nhập đến khi cô lập thành công sự cố).
- **Tỷ lệ tuân thủ**: Tỷ lệ các hệ thống đáp ứng đúng cấu hình chuẩn bảo mật (baseline) như cài đặt phần mềm bảo vệ điểm cuối (EDR - Endpoint Detection and Response), kích hoạt xác thực đa yếu tố (MFA - Multi-Factor Authentication) và cập nhật bản vá lỗi đúng hạn.

**4. Nhóm Quản trị, Kinh doanh & Dịch vụ Số**
- **Hiệu quả đầu tư**: Tỷ lệ các dự án được hoàn thành đúng tiến độ và nằm trong phạm vi ngân sách phê duyệt.
- **Tác động kinh doanh**: Sự gia tăng doanh thu từ nền tảng số, tỷ lệ chuyển đổi khách hàng (conversion), sự giảm trừ chi phí phục vụ (cost-to-serve), và việc rút ngắn thời gian chu kỳ kinh doanh (cycle time).
- **Trải nghiệm người dùng**: Chỉ số đo lường sự hài lòng của khách hàng (NPS - Net Promoter Score / CSAT - Customer Satisfaction Score) và tỷ lệ người dùng chấp nhận sử dụng hệ thống (adoption).
