# CHƯƠNG 2: DANH MỤC TỪ KHÓA & THUẬT NGỮ (KEYWORDS)
## Kiến Trúc Hạ Tầng CNTT Doanh Nghiệp và Tư Duy Hệ Thống

- **Môn học:** Cơ sở hạ tầng Công nghệ thông tin
- **Tài liệu liên quan:** [Slide Chương 2](../2.md)

---

## 1. Phần cứng, Lưu trữ & Tính toán (Compute & Storage)
- **PC — Personal Computer:** Máy tính cá nhân dành cho người dùng cuối làm việc văn phòng.
- **CPU — Central Processing Unit:** Bộ xử lý trung tâm thực thi các tập lệnh chương trình và điều phối toàn bộ hoạt động tính toán của hệ thống.
- **RAM — Random Access Memory:** Bộ nhớ truy cập ngẫu nhiên, lưu trữ tạm thời các chỉ lệnh và dữ liệu của các tiến trình đang hoạt động để CPU truy xuất nhanh.
- **IO (I/O) — Input/Output:** Các hoạt động nhập/xuất và truyền tải dữ liệu qua lại giữa CPU – Bộ nhớ – Ổ đĩa – Card mạng.
- **IOPS — Input/Output Operations Per Second:** Số lượng thao tác vào/ra dữ liệu thực hiện được trong mỗi giây — chỉ số thước đo cốt lõi đánh giá hiệu năng của hệ thống lưu trữ (đặc biệt là SSD/SAN).
- **DAS — Direct Attached Storage:** Hệ thống lưu trữ gắn trực tiếp vào một máy chủ/máy trạm qua cáp vật lý.
- **NAS — Network Attached Storage:** Thiết bị lưu trữ gắn vào mạng LAN, cung cấp dịch vụ chia sẻ file tập trung cho nhiều người dùng qua mạng.
- **SAN — Storage Area Network:** Mạng lưu trữ chuyên dụng tốc độ cao kết nối các máy chủ với hệ thống khối lưu trữ (Block storage) trong Data Center.
- **SPOF — Single Point of Failure:** Điểm lỗi đơn lẻ — vị trí hoặc linh kiện mà nếu gặp sự cố hỏng hóc sẽ làm toàn bộ hệ thống bị tê liệt hoàn toàn.
- **TPM — Trusted Platform Module:** Chip bảo mật phần cứng chuyên dụng tích hợp trên bo mạch chủ, hỗ trợ lưu trữ khóa mã hóa an toàn và xác thực tính toàn vẹn của thiết bị (Secure Boot).
- **HSM — Hardware Security Module:** Thiết bị phần cứng bảo mật chuyên nghiệp cấp doanh nghiệp dùng để sinh, quản lý và bảo vệ an toàn tuyệt đối cho các khóa mật mã (dùng trong ngân hàng, PKI, chữ ký số).

---

## 2. Mạng & Kết nối (Network & Connectivity)
- **LAN — Local Area Network:** Mạng cục bộ kết nối các thiết bị trong phạm vi địa lý nhỏ hẹp (phòng làm việc, tầng lầu, tòa nhà văn phòng).
- **WAN — Wide Area Network:** Mạng diện rộng kết nối các mạng LAN ở khoảng cách địa lý xa (liên tỉnh, liên quốc gia).
- **SD-WAN — Software-Defined Wide Area Network:** Mạng WAN điều khiển bằng phần mềm giúp tối ưu hóa định tuyến, nâng cao hiệu năng và đơn giản hóa việc kết nối các chi nhánh về trung tâm.
- **VPN — Virtual Private Network:** Mạng riêng ảo tạo đường hầm mã hóa an toàn truyền qua môi trường mạng công cộng Internet.
- **DNS — Domain Name System:** Hệ thống phân giải tên miền (ví dụ: `uit.edu.vn`) sang địa chỉ IP máy chủ.

---

## 3. Phần mềm, Hệ điều hành & Ảo hóa (Software & Virtualization)
- **OS — Operating System:** Hệ điều hành quản lý tài nguyên phần cứng máy tính và cung cấp môi trường thực thi, dịch vụ nền tảng cho các ứng dụng.
- **app — application:** Cách viết tắt thông dụng của từ “ứng dụng” phần mềm.
- **VMware — VMware:** Nền tảng và bộ giải pháp ảo hóa công nghiệp hàng đầu (vSphere, ESXi) cho phép khởi tạo và quản lý nhiều máy ảo trên cùng một hạ tầng máy chủ vật lý.
- **K8s — Kubernetes:** Nền tảng điều phối cụm container (Container Orchestration); tên gọi bắt nguồn từ chữ “K”, theo sau là 8 chữ cái và kết thúc bằng chữ “s”.
- **API — Application Programming Interface:** Giao diện lập trình ứng dụng — tập hợp các quy chuẩn và giao thức cho phép các hệ thống phần mềm trao đổi dữ liệu và tích hợp chức năng với nhau.

---

## 4. Ứng dụng nghiệp vụ & Dữ liệu doanh nghiệp (Enterprise Apps & Data)
- **ERP — Enterprise Resource Planning:** Hệ thống hoạch định nguồn lực doanh nghiệp tích hợp tài chính, kế toán, kho bãi, mua hàng, nhân sự trên một nền tảng CSDL.
- **CRM — Customer Relationship Management:** Hệ thống quản lý quan hệ khách hàng (bán hàng, chăm sóc, marketing).
- **LMS — Learning Management System:** Hệ thống quản lý học tập và đào tạo trực tuyến (khóa học, bài giảng, điểm số, bài kiểm tra).
- **HIS — Hospital Information System:** Hệ thống thông tin bệnh viện phục vụ quản lý toàn diện quy trình khám chữa bệnh, hồ sơ bệnh án điện tử và viện phí.
- **DB — Database:** Cơ sở dữ liệu — tập hợp dữ liệu có cấu trúc được tổ chức khoa học để phục vụ việc lưu trữ, truy vấn và phân tích.
- **DBMS — Database Management System:** Hệ quản trị cơ sở dữ liệu — phần mềm chuyên dụng để định nghĩa, khởi tạo, lưu trữ, truy vấn và quản lý bảo mật dữ liệu (Oracle, MySQL, SQL Server, PostgreSQL).

---

## 5. Mô hình dịch vụ điện toán đám mây (Cloud Computing Models)
- **IaaS — Infrastructure as a Service:** Dịch vụ hạ tầng — nhà cung cấp cloud cung cấp máy ảo, tài nguyên tính toán, mạng và lưu trữ; doanh nghiệp tự quản trị hệ điều hành và ứng dụng.
- **PaaS — Platform as a Service:** Dịch vụ nền tảng — nhà cung cấp cloud lo toàn bộ hạ tầng, OS, runtime, cơ sở dữ liệu managed; doanh nghiệp chỉ tập trung phát triển và triển khai mã nguồn ứng dụng.
- **SaaS — Software as a Service:** Dịch vụ phần mềm hoàn chỉnh — người dùng sử dụng trực tiếp ứng dụng qua mạng (như Google Workspace, Microsoft 365, Salesforce) mà không phải lo bất kỳ khâu hạ tầng nào.

---

## 6. Quản trị hạ tầng, Độ tin cậy & Kinh tế CNTT (Operations, Reliability & Economics)
- **CMDB — Configuration Management Database:** Cơ sở dữ liệu quản lý cấu hình và tài sản CNTT cùng các mối quan hệ phụ thuộc kỹ thuật giữa chúng.
- **DR — Disaster Recovery:** Khôi phục sau thảm họa — tập hợp các giải pháp công nghệ và quy trình đưa toàn bộ hệ thống CNTT trở lại hoạt động bình thường sau sự cố phá hủy lớn.
- **SLA — Service Level Agreement:** Bản cam kết mức độ dịch vụ giữa bên cung cấp và bên sử dụng (thời gian uptime, thời gian khắc phục, mức bồi thường vi phạm).
- **SLO — Service Level Objective:** Mục tiêu nội bộ cụ thể, định lượng của đội ngũ kỹ thuật để đảm bảo luôn đạt cam kết SLA.
- **IR — Incident Response:** Quy trình ứng phó và xử lý sự cố (đặc biệt là các sự cố an toàn thông tin và gián đoạn dịch vụ nghiêm trọng).
- **BCP — Business Continuity Plan:** Kế hoạch duy trì hoạt động kinh doanh liên tục — chiến lược đảm bảo các nghiệp vụ trọng yếu của doanh nghiệp vẫn duy trì vận hành khi hạ tầng CNTT bị gián đoạn.
- **CapEx — Capital Expenditure:** Chi phí đầu tư tài sản cố định ban đầu (mua máy chủ, mua thiết bị mạng, xây phòng data center).
- **OpEx — Operating Expenditure:** Chi phí vận hành định kỳ hằng tháng/quý (tiền điện, thuê mạng, thuê dịch vụ cloud, bảo trì, lương nhân sự vận hành).
- **TCO — Total Cost of Ownership:** Tổng chi phí sở hữu — toàn bộ chi phí tài chính trực tiếp và gián tiếp để mua sắm, vận hành, bảo trì và loại bỏ hệ thống trong suốt vòng đời (3–5 năm).
- **FinOps — Financial Operations:** Khung văn hóa và thực hành kết hợp giữa Tài chính – CNTT – Kinh doanh nhằm tối ưu hóa chi phí điện toán đám mây và tối đa hóa giá trị thu về.

---

## 7. An toàn thông tin & Phòng thủ (Security)
- **vuln — vulnerability:** Cách viết tắt thông dụng của thuật ngữ “lỗ hổng bảo mật”.
- **IDS — Intrusion Detection System:** Hệ thống phát hiện xâm nhập — giám sát lưu lượng mạng và phát ra cảnh báo khi phát hiện dấu hiệu tấn công.
- **IPS — Intrusion Prevention System:** Hệ thống ngăn chặn xâm nhập — chủ động phát hiện và chặn đứng ngay lập tức các gói tin lưu lượng độc hại theo thời gian thực.
- **WAF — Web Application Firewall:** Tường lửa chuyên dụng bảo vệ các ứng dụng web trên giao thức HTTP/HTTPS khỏi các tấn công phổ biến (SQL Injection, XSS, CSRF).
- **IAM — Identity and Access Management:** Hệ thống quản lý danh tính người dùng và phân quyền truy cập.
- **SSO — Single Sign-On:** Cơ chế đăng nhập một lần cho nhiều hệ thống phân tán.
- **MFA — Multi-Factor Authentication:** Xác thực đa yếu tố tăng cường độ bảo mật khi đăng nhập.
- **PAM — Privileged Access Management:** Quản lý và giám sát các tài khoản có quyền truy cập đặc quyền cấp cao (Admin, Root).
- **DLP — Data Loss Prevention:** Hệ thống phòng chống thất thoát và rò rỉ dữ liệu nhạy cảm của tổ chức ra môi trường bên ngoài.
