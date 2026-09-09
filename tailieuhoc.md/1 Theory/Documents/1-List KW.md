# CHƯƠNG 1: DANH MỤC TỪ KHÓA & THUẬT NGỮ (KEYWORDS)
## Tổng Quan CNTT Trong Tổ Chức và Bối Cảnh Ứng Dụng

- **Môn học:** Cơ sở hạ tầng Công nghệ thông tin
- **Tài liệu liên quan:** [Slide Chương 1](../1.md) | [Bài tập Chương 1](./1-Assignment.md)

---

## 1) Ứng dụng nghiệp vụ (Business Applications)
- **ERP (Enterprise Resource Planning):** Hệ thống quản trị nguồn lực tổng thể doanh nghiệp — tích hợp toàn diện tài chính, kế toán, mua hàng, quản lý kho, sản xuất, nhân sự… trong một nền tảng cơ sở dữ liệu duy nhất.
- **CRM (Customer Relationship Management):** Hệ thống quản trị quan hệ khách hàng — quản lý toàn diện hồ sơ khách hàng, quy trình bán hàng (sales pipeline), dịch vụ chăm sóc khách hàng, chiến dịch marketing và lịch sử tương tác.
- **DMS (Document Management System):** Hệ thống quản lý tài liệu/hồ sơ điện tử — lưu trữ, phân loại, tìm kiếm toàn văn, quản lý phiên bản, phân quyền bảo mật và tự động hóa luồng phê duyệt văn bản.

---

## 2) Quản trị doanh nghiệp & tuân thủ (Enterprise Governance)
- **EA (Enterprise Architecture):** Kiến trúc doanh nghiệp — khung định hướng chuẩn hóa cấu trúc hệ thống CNTT, luồng dữ liệu, quy chuẩn tích hợp và lộ trình công nghệ dài hạn của tổ chức.
- **Portfolio (IT Portfolio Management):** Danh mục đầu tư/dự án CNTT — quản trị việc ưu tiên các dự án, cân đối ngân sách, kiểm soát tiến độ và đo lường giá trị mang lại của các chương trình CNTT và chuyển đổi số.
- **Compliance:** Tuân thủ — đáp ứng các quy định pháp lý, tiêu chuẩn ngành và yêu cầu kiểm toán (audit) về an toàn dữ liệu, chuẩn hóa quy trình và bảo mật thông tin.
- **Security Governance:** Quản trị an ninh mạng — thiết lập khung chính sách, phân định vai trò trách nhiệm, kiểm soát rủi ro và giám sát thực thi an toàn thông tin toàn diện.

---

## 3) Nhận dạng & quản lý truy cập (Identity & Access)
- **IAM (Identity & Access Management):** Quản lý định danh và quyền truy cập — xác định rõ danh tính (Identity) và kiểm soát người dùng được phép thao tác những gì, trên hệ thống nào.
- **SSO (Single Sign-On):** Cơ chế đăng nhập một lần — người dùng chỉ cần đăng nhập một lần bằng một tài khoản duy nhất để truy cập vào nhiều hệ thống và ứng dụng khác nhau (thường kết hợp MFA).
- **MFA (Multi-Factor Authentication):** Xác thực đa yếu tố — phương thức bảo mật bắt buộc người dùng cung cấp từ 2 yếu tố xác thực trở lên (Mật khẩu đã biết + Mã OTP/Token gửi về thiết bị + Sinh trắc học vân tay/khuôn mặt).
- **PAM (Privileged Access Management):** Quản lý tài khoản đặc quyền (admin, root) — kiểm soát nghiêm ngặt tài khoản quản trị nhạy cảm: cấp quyền tạm thời (*Just-In-Time*), quay video phiên làm việc, tự động đổi mật khẩu và lưu trữ mật mã trong két an toàn (vault).

---

## 4) An ninh mạng & phòng thủ (Security)
- **Ransomware (Mã độc tống tiền):** Loại mã độc nguy hiểm mã hóa hoặc khóa toàn bộ dữ liệu/hệ thống của nạn nhân để làm tê liệt hoạt động, sau đó đòi tiền chuộc để giải mã (kèm đe dọa phát tán dữ liệu bí mật).
- **Zero Trust (Mô hình không tin cậy mặc định):** Triết lý bảo mật coi mọi kết nối và truy cập đều không đáng tin cậy cho đến khi được xác thực liên tục; áp dụng nguyên tắc đặc quyền tối thiểu (least privilege), kiểm tra định danh – thiết bị – ngữ cảnh, phân đoạn mạng (micro-segmentation) và ghi log toàn diện nhằm giảm rủi ro xâm nhập/leo thang đặc quyền.
- **DLP (Data Loss Prevention):** Giải pháp chống thất thoát dữ liệu — phát hiện, cảnh báo và ngăn chặn hành vi gửi nhầm hoặc chia sẻ trái phép dữ liệu nhạy cảm ra ngoài qua email, cloud storage, USB…
- **WAF (Web Application Firewall):** Tường lửa ứng dụng web — bảo vệ các trang web và API khỏi các cuộc tấn công phổ biến như SQL Injection, Cross-Site Scripting (XSS), bot độc hại…
- **EDR (Endpoint Detection and Response):** Giải pháp an ninh trên máy trạm/endpoint — giám sát hành vi bất thường, phát hiện mối đe dọa, cô lập máy tính bị nhiễm và hỗ trợ điều tra nguyên nhân gốc.
- **XDR (Extended Detection and Response):** Nền tảng an ninh mở rộng — tương quan và phân tích dữ liệu telemetry từ nhiều nguồn (Endpoint, Email, Network, Cloud, Identity) để phát hiện và phản ứng sự cố toàn diện.
- **SIEM (Security Information and Event Management):** Hệ thống thu thập, chuẩn hóa, phân tích tập trung nhật ký (log) bảo mật từ toàn bộ hạ tầng và tạo cảnh báo tương quan.
- **SOC (Security Operations Center):** Trung tâm vận hành an ninh — bộ phận chuyên trách trực 24/7 theo dõi, phát hiện, phân tích và ứng cứu kịp thời các sự cố an toàn thông tin.

---

## 5) Mạng & kết nối (Network & Connectivity)
- **SD-WAN (Software-Defined WAN):** Mạng diện rộng điều khiển bằng phần mềm — tối ưu hóa việc định tuyến và kết nối giữa nhiều chi nhánh (tự động chọn đường truyền Internet/MPLS tốt nhất theo thời gian thực, ưu tiên ứng dụng nghiệp vụ, quản trị tập trung trên cloud).
- **VPN (Virtual Private Network):** Mạng riêng ảo — tạo “đường hầm” mã hóa an toàn qua Internet để nhân viên truy cập dữ liệu nội bộ công ty từ xa.

---

## 6) Vận hành CNTT & quản lý dịch vụ (IT Operations & Service Management)
- **ITSM (IT Service Management):** Quản lý dịch vụ CNTT theo các quy trình chuẩn (như ITIL): quản lý sự cố (Incident), yêu cầu dịch vụ (Service Request), thay đổi (Change), vấn đề (Problem) và cam kết SLA.
- **CMDB (Configuration Management Database):** Cơ sở dữ liệu quản lý cấu hình — lưu trữ danh mục tài sản CNTT cùng bản đồ mối quan hệ phụ thuộc lẫn nhau (Server – App – Database – Network…) phục vụ quản lý thay đổi và khắc phục sự cố.
- **SRE (Site Reliability Engineering):** Kỹ thuật đảm bảo độ tin cậy hệ thống — phương pháp áp dụng tư duy kỹ thuật phần mềm vào vận hành hạ tầng thông qua tự động hóa, thiết lập SLO/Error Budget và giám sát quan sát.
- **Log / Audit:**
  - *Log:* Nhật ký kỹ thuật ghi lại chuỗi sự kiện của hệ thống/ứng dụng (đăng nhập, lỗi, truy cập…).
  - *Audit:* Dấu vết kiểm toán phục vụ tuân thủ pháp lý và điều tra (ai đã thao tác, vào lúc nào, thay đổi dữ liệu gì).
- **Backup / DR (Disaster Recovery):**
  - *Backup:* Sao lưu dữ liệu để khôi phục khi bị xóa nhầm, hỏng đĩa hoặc nhiễm virus.
  - *DR (Disaster Recovery):* Kế hoạch và hạ tầng dự phòng để khôi phục toàn bộ hoạt động hệ thống sau thảm họa lớn (cháy nổ data center, thiên tai, sập mạng lưới) theo mục tiêu RTO/RPO định trước.
- **SLA / SLO:**
  - *SLA (Service Level Agreement):* Cam kết chất lượng dịch vụ có tính ràng buộc giữa bên cung cấp và bên sử dụng (ví dụ uptime 99.9%/tháng, thời gian xử lý sự cố trong 2 giờ).
  - *SLO (Service Level Objective):* Mục tiêu kỹ thuật nội bộ của đội ngũ vận hành nhằm đảm bảo luôn đạt được chỉ số SLA đã cam kết.

---

## 7) Chỉ số độ tin cậy & quản trị sự cố (Reliability & Incident Metrics)
- **Availability / Uptime:** Mức độ sẵn sàng — tỷ lệ phần trăm thời gian hệ thống hoạt động bình thường, phục vụ người dùng không bị gián đoạn (ví dụ 99.9%/tháng).
- **MTTR (Mean Time To Restore / Recover):** Thời gian trung bình để khôi phục dịch vụ — tính từ thời điểm sự cố phát sinh cho đến khi hệ thống hoạt động bình thường trở lại.
- **Incident Rate:** Tần suất phát sinh sự cố trong một khoảng thời gian, thường được phân loại theo mức độ nghiêm trọng (P1, P2, P3…).
- **P1 / P2 (Severity Levels):**
  - *P1 (Priority 1):* Sự cố ở mức nghiêm trọng nhất (dịch vụ cốt lõi bị tê liệt hoàn toàn, ảnh hưởng diện rộng toàn tổ chức hoặc khách hàng lớn).
  - *P2 (Priority 2):* Sự cố nghiêm trọng cao nhưng phạm vi ảnh hưởng hẹp hơn hoặc đã có giải pháp khắc phục tạm thời.
- **RPO / RTO:**
  - *RPO (Recovery Point Objective):* Mục tiêu điểm khôi phục dữ liệu — lượng dữ liệu tối đa chấp nhận bị mất mát tính theo đơn vị thời gian (ví dụ RPO = 15 phút nghĩa là dữ liệu mất tối đa không quá 15 phút phát sinh gần nhất).
  - *RTO (Recovery Time Objective):* Mục tiêu thời gian khôi phục dịch vụ — khoảng thời gian tối đa cho phép để đưa hệ thống hoạt động trở lại sau sự cố (ví dụ RTO = 2 giờ).

---

## 8) Tích hợp & kiến trúc ứng dụng (Integration & Application Architecture)
- **Middleware / ESB:**
  - *Middleware:* Lớp phần mềm trung gian giúp các ứng dụng và hệ thống khác nhau có thể kết nối, giao tiếp và trao đổi dữ liệu dễ dàng.
  - *ESB (Enterprise Service Bus):* Trục tích hợp dịch vụ doanh nghiệp — đóng vai trò trung tâm điều phối, định tuyến và chuyển đổi khuôn dạng dữ liệu cho nhiều hệ thống phân tán.
- **API Gateway:** Cổng quản lý API tập trung — thực hiện các nhiệm vụ kiểm soát: xác thực, giới hạn tần suất gọi (rate limiting), cân bằng tải, định tuyến yêu cầu, ghi log và quản lý phiên bản API.
- **Microservices:** Kiến trúc vi dịch vụ — chia nhỏ ứng dụng lớn thành tập hợp các dịch vụ nhỏ độc lập, mỗi dịch vụ tự quản lý CSDL riêng và giao tiếp qua API/message, cho phép triển khai và mở rộng độc lập.
- **Container / K8s (Kubernetes):**
  - *Container (Docker):* Công nghệ đóng gói ứng dụng cùng môi trường và toàn bộ thư viện phụ thuộc để chạy nhất quán trên mọi máy chủ.
  - *Kubernetes (K8s):* Nền tảng điều phối cụm container mã nguồn mở — tự động hóa triển khai, tự phục hồi lỗi (self-healing), tự co giãn quy mô (auto-scaling) và cập nhật không gián đoạn (rolling update).
- **Message Queue / Event Bus:**
  - *Message Queue (RabbitMQ, SQS):* Hàng đợi thông điệp giúp các thành phần hệ thống xử lý tác vụ bất đồng bộ, giảm tải phụ thuộc trực tiếp.
  - *Event Bus (Apache Kafka, EventBridge):* Luồng sự kiện theo cơ chế publish/subscribe dành cho kiến trúc hướng sự kiện (event-driven architecture).

---

## 9) Quản trị dữ liệu & nền tảng khách hàng (Data Management)
- **MDM (Master Data Management):** Quản trị dữ liệu chủ — quy trình và công nghệ đảm bảo các thực thể dữ liệu cốt lõi (khách hàng, sản phẩm, nhà cung cấp) chỉ có “một phiên bản sự thật duy nhất” (single source of truth), chuẩn hóa và đồng bộ giữa tất cả các phần mềm trong doanh nghiệp.
- **MarTech / CRM / CDP:**
  - *MarTech:* Bộ công cụ công nghệ tiếp thị tự động hóa chiến dịch, tracking và đo lường.
  - *CRM:* Quản lý thông tin và các điểm chạm bán hàng với khách hàng.
  - *CDP (Customer Data Platform):* Nền tảng dữ liệu khách hàng — hợp nhất dữ liệu định danh khách hàng từ đa kênh về một nơi duy nhất để phân khúc và kích hoạt tiếp thị tức thời.
- **Analytics:** Hoạt động phân tích dữ liệu số để đo lường hiệu quả, thấu hiểu hành vi và ra quyết định kinh doanh dựa trên dữ liệu.

---

## 10) Trải nghiệm số & tăng trưởng (Digital Experience & Growth)
- **Omni-channel (Đa kênh hợp nhất):** Mô hình tổ chức tất cả các kênh tiếp xúc (Website, App di động, Cửa hàng vật lý, Tổng đài hotline, Mạng xã hội…) liên thông liền mạch, chia sẻ dữ liệu và trạng thái nhất quán theo thời gian thực; khách hàng chuyển đổi giữa các kênh không bao giờ phải làm lại từ đầu.
- **Self-service (Tự phục vụ):** Cung cấp công cụ để khách hàng/người dùng tự giải quyết các nhu cầu phổ biến qua cổng Portal, App, Chatbot thông minh, FAQ (tra cứu hóa đơn, đặt lịch hẹn, đổi mật khẩu) mà không cần nhân viên hỗ trợ.
- **Personalization (Cá nhân hóa):** Khả năng may đo nội dung, giao diện, gợi ý sản phẩm hoặc lộ trình dịch vụ riêng biệt cho từng người dùng dựa trên hồ sơ dữ liệu và hành vi lịch sử.
- **Adoption:** Tỷ lệ tiếp nhận và làm quen hệ thống số (số người dùng tích cực hàng tháng, tần suất dùng các tính năng mới).
- **NPS / CSAT:**
  - *NPS (Net Promoter Score):* Chỉ số đo lường mức độ sẵn sàng giới thiệu sản phẩm/dịch vụ của khách hàng cho người khác (độ trung thành).
  - *CSAT (Customer Satisfaction Score):* Chỉ số đo lường sự hài lòng tức thời của người dùng ngay sau một phiên tương tác dịch vụ cụ thể.
- **Engagement:** Mức độ tương tác và gắn kết của người dùng (thời gian trên trang, số phiên truy cập, tần suất quay lại).
- **Churn Rate:** Tỷ lệ khách hàng rời bỏ dịch vụ hoặc ngừng sử dụng sản phẩm trong một chu kỳ nhất định.
- **Conversion Rate:** Tỷ lệ chuyển đổi hành động mục tiêu (ví dụ: từ người xem trở thành người đăng ký hoặc mua hàng).
- **Cost-to-serve:** Chi phí trung bình mà tổ chức phải bỏ ra để phục vụ một khách hàng, một đơn hàng hoặc một yêu cầu dịch vụ.
- **Cycle Time:** Tổng thời gian hoàn tất một chu trình công việc đầu cuối (end-to-end), từ lúc phát sinh nhu cầu đến khi bàn giao kết quả.

---

## 11) Tự động hóa quy trình (Process Automation)
- **RPA (Robotic Process Automation):** Tự động hóa quy trình bằng robot phần mềm — sử dụng các “bot” mô phỏng chính xác thao tác nhấp chuột, gõ phím của con người để tự động thực thi các tác vụ lặp đi lặp lại theo quy tắc (nhập liệu, trích xuất hóa đơn, đối soát công nợ, xuất báo cáo).

---

## 12) Phân phối phần mềm & DevSecOps (Software Delivery)
- **DevSecOps:** Mô hình phát triển phần mềm tích hợp chặt chẽ an ninh mạng ngay từ giai đoạn đầu và xuyên suốt toàn bộ vòng đời (Dev + Sec + Ops) dựa trên nguyên tắc *“Security-by-Design”*; tự động hóa kiểm tra mã độc, quét lỗ hổng thư viện và kiểm thử bảo mật trong pipeline CI/CD để phát hành vừa nhanh vừa an toàn.
- **CI/CD (Continuous Integration / Continuous Delivery & Deployment):**
  - *CI (Tích hợp liên tục):* Tự động hóa việc hợp nhất mã nguồn, build và chạy unit test mỗi khi lập trình viên đẩy code lên repo.
  - *CD (Phân phối/Triển khai liên tục):* Tự động đóng gói và triển khai phiên bản phần mềm lên môi trường Staging/Production một cách tin cậy, nhất quán.
- **DORA Metrics:** Bộ 4 chỉ số vàng đo lường hiệu suất chuyển giao phần mềm và vận hành hệ thống:
  1. *Deployment Frequency (Tần suất phát hành):* Tần suất đưa mã nguồn thành công lên Production.
  2. *Lead Time for Changes (Thời gian hoàn thành thay đổi):* Thời gian từ lúc commit code đến khi code chạy trên Production.
  3. *Change Failure Rate (Tỷ lệ lỗi khi thay đổi):* Phần trăm các đợt phát hành gây lỗi cần rollback hoặc vá nóng.
  4. *Time to Restore Service (Thời gian phục hồi dịch vụ):* Thời gian cần thiết để khôi phục hệ thống khi có sự cố phát sinh từ đợt phát hành.

---

## 13) Quản trị chi phí Cloud (Cloud Cost Management)
- **FinOps (Cloud Financial Operations):** Khung văn hóa và thực hành quản trị tài chính đám mây kết hợp chặt chẽ giữa IT, Tài chính và Bộ phận kinh doanh — liên tục theo dõi, dự báo, tối ưu hóa kích thước tài nguyên (rightsizing) và phân bổ minh bạch chi phí cloud để tối đa hóa giá trị đầu tư.

---

## 14) Bối cảnh hội tụ OT/IT (Industrial Context)
- **IT (Information Technology):** Công nghệ thông tin dành cho môi trường văn phòng, quản trị doanh nghiệp, dữ liệu kinh doanh và dịch vụ số.
- **OT (Operational Technology):** Công nghệ vận hành tại hiện trường và phân xưởng công nghiệp — bao gồm các hệ thống phần cứng và phần mềm trực tiếp điều khiển, cảm biến và giám sát các thiết bị vật lý, dây chuyền sản xuất và máy móc công nghiệp (SCADA, PLC, DCS, Industrial IoT).
