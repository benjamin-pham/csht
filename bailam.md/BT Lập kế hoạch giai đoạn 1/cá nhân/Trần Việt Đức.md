**BÁO CÁO CƠ SỞ HẠ TẦNG CÔNG NGHỆ THÔNG TIN***\
Giai đoạn 1: Đề xuất & Lập kế hoạch đầu tư hạ tầng*

―――――――――――――――――――――――――――――――――――――――――――――

**PHẦN 1: ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT (ĐỒ ÁN MÔN HỌC)**

**Bước 1: Khảo sát hiện trạng hạ tầng (AS-IS) có số liệu**

**1. Giới thiệu tổng quan về WAYS STATION**

- **•** Lĩnh vực hoạt động: Chuỗi không gian làm việc thông minh & tiện
  ích tích hợp công nghệ (Co-working space, Smart kiosk, Meeting room
  on-demand).

- **•** Quy mô hiện tại: 3 chi nhánh trung tâm, mỗi chi nhánh phục vụ
  trung bình 150–200 khách hàng/ngày và 30 nhân viên vận hành.

- **•** Quy trình hoạt động phụ thuộc CNTT: Đặt chỗ & thanh toán qua
  App/Web, Kiểm soát ra vào (Access Control/Smart Lock), Hệ thống Wi-Fi
  truy cập high-speed, Surveillance Camera (CCTV), Quản lý POS/Billing.

**2. Thu thập dữ liệu hiện trạng theo 5 lớp hạ tầng**

- **• Lớp 1 (Tính toán & Kết nối):** Compute/Storage: Mỗi chi nhánh dùng
  01 Mini Server / NAS phổ thông (4 Cores, 16GB RAM, 2TB Storage) chạy
  cục bộ. CPU/RAM utilization đạt mức 85–95% vào giờ cao điểm (9:00 -
  11:30 & 14:00 - 17:00). Tuổi đời thiết bị 4 năm (đã hết hạn bảo hành).

- **•** Network & Connectivity: 2 đường truyền FTTH dân dụng/doanh
  nghiệp nhỏ (150 Mbps/đường) không có cam kết băng thông quốc tế. Wi-Fi
  AP chuẩn Wi-Fi 5 cũ, quá tải khi \>80 khách dùng cùng lúc. Tồn tại
  điểm lỗi đơn lẻ (SPOF) tại Core Switch.

- **• Lớp 2 (Nền tảng vận hành):** Monitoring: Chưa có hệ thống giám sát
  tập trung (NO Monitoring/Observability). MTTD ~ 45 phút, MTTR ~ 3-5
  giờ.

- **•** Backup & DR: Sao lưu thủ công ra ổ cứng ngoài 1 tuần/lần, tỉ lệ
  thành công ~60%. RPO hiện tại: 7 ngày \| RTO hiện tại: 24 - 48 giờ.

- **• Lớp 3 (Bảo mật & Danh tính):** Identity & Security: Dùng tài khoản
  local trên từng thiết bị, chưa có IAM/SSO/MFA tập trung. Chưa có
  EDR/XDR. 100% máy trạm/server chưa quản lý vá lỗi tập trung, tồn tại
  lỗ hổng Critical.

- **• Lớp 4 (Ứng dụng & Tích hợp):** App & Integration: Mức độ ảo hóa 0%
  (Bare-metal). App đặt chỗ và POS chạy trên các nền tảng SaaS độc lập
  kết nối qua API công cộng không có API Gateway.

- **• Lớp 5 (Dữ liệu):** Data: Dữ liệu phân tán ở SaaS POS, Smart Lock
  Controller local, NAS local. Chưa có chính sách phân loại dữ liệu hay
  mã hóa data-at-rest.

**3. Bảng chỉ số đo lường hiện trạng (Baseline KPIs)**

| **Chỉ số / Metric** | **Giá trị hiện tại (AS-IS Baseline)** |
|:--:|----|
| SLA / Uptime hệ thống | 97.5% (~ 18 giờ downtime/tháng) |
| Số sự cố nghiêm trọng | 4 – 6 sự cố / 3 tháng (sập mạng Wi-Fi, lỗi đồng bộ cửa ra vào) |
| MTTD / MTTR | MTTD: 45 phút \| MTTR: 4 giờ |
| RPO / RTO | RPO: 7 ngày \| RTO: 24 - 48 giờ |
| Tỉ lệ thiết bị End-of-Support | 70% thiết bị mạng và server đã hết hạn hỗ trợ |
| Dự báo tăng trưởng dữ liệu/user | Dự kiến tăng 200% trong 12–18 tháng tới (mở thêm 5 chi nhánh) |

**4. Các "Pain Points" định lượng của WAYS STATION**

- **1.** Trải nghiệm khách hàng kém: Tỉ lệ rớt kết nối Wi-Fi đỉnh điểm
  lên tới 15% tổng số lượt truy cập trong giờ cao điểm.

- **2.** Mất doanh thu tức thì: Cửa thông minh ngưng trệ và POS sập gây
  thiệt hại ước tính 15 - 20 triệu VNĐ/giờ rớt mạng vào ca cao điểm.

- **3.** Nguy cơ mất an toàn thông tin: Dữ liệu nhận dạng khách hàng và
  lịch sử giao dịch không được mã hóa chuẩn hóa, nguy cơ rò rỉ cao.

**Bước 2: Nêu vấn đề & Rủi ro nếu không đầu tư (Why now?)**

Nếu WAYS STATION giữ nguyên hạ tầng AS-IS và tiến hành mở rộng chi nhánh
trong 12 tháng tới, doanh nghiệp sẽ đối mặt với các tác động nghiêm
trọng:

| **Nhóm tác động** | **Mô tả rủi ro khi không đầu tư** | **Mức độ** | **Chi phí thiệt hại ước tính** |
|:---:|---|---|---|
| 1. Tác động Vận hành | Mạng sập trong ca cao điểm làm nghẽn Smart Lock. Hỏng NAS local dẫn đến mất hoàn toàn dữ liệu hình ảnh & log ra vào. | Khả năng: Cao<br>Ảnh hưởng: Rất Cao | Mất 50 - 100 triệu VNĐ/sự cố lớn (Đền bù khách hàng, tổn hại uy tín). |
| 2. Tác động Tuân thủ & An ninh | Lỗ hổng security bị khai thác, rò rỉ dữ liệu khách hàng. Vi phạm Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân. | Khả năng: TB<br>Ảnh hưởng: Rất Cao | Phạt hành chính + Thiệt hại thương hiệu: 200 - 500 triệu VNĐ. |
| 3. Tác động Chiến lược | Hạ tầng không đủ khả năng mở rộng (Scalability bottleneck), không thể mở thêm 5 chi nhánh mới đúng tiến độ. | Khả năng: Rất Cao<br>Ảnh hưởng: Cao | Mất cơ hội kinh doanh: Tụt giảm 20 - 30% thị phần tiềm năng. |

**Bước 3: Xác lập mục tiêu & KPI hạ tầng (TO-BE)**

| **Tiêu chí** | **Baseline hiện tại (AS-IS)** | **Target mục tiêu (TO-BE Target)** |
|:--:|----|----|
| Độ sẵn sàng (Uptime) | 97.5% | ≥ 99.9% (Cho Core System & Connectivity) |
| Khôi phục sự cố (RPO / RTO) | RPO: 7 ngày \| RTO: 24 - 48h | RPO ≤ 1 giờ \| RTO ≤ 2 giờ |
| Hiệu năng Wi-Fi | 30 - 40 users/AP, trễ \> 120ms | ≥ 100 concurrent users/AP, Latency \< 20ms |
| Bảo mật (Security) | 0% EDR, không MFA | 100% Endpoint có EDR, 100% Admin có MFA |
| Vận hành (Ops Efficiency) | MTTD: 45 phút \| MTTR: 4 giờ | MTTD giảm 60% (\< 15p) \| MTTR giảm 50% (\< 2h) |

**Bước 4: Xây dựng phương án kiến trúc TO-BE (2–3 lựa chọn)**

**Kịch bản 1: Nâng cấp On-Premise hoàn toàn (Traditional Upgrade)**

- **•** Mô tả: Mua cụm Server/Storage HCI tập trung tại HQ + Nâng cấp
  Wi-Fi 6 Enterprise tại các chi nhánh.

- **•** Ưu/Nhược điểm: Tự chủ 100% dữ liệu nhưng chi phí đầu tư ban đầu
  (CAPEX) rất cao, khó mở rộng chi nhánh mới nhanh chóng.

**Kịch bản 2: Mô hình Lai - Hybrid Cloud (ĐỀ XUẤT CHỌN)**

- **•** Mô tả: Đẩy các hệ thống cốt lõi (App WAYS STATION, DB, POS,
  Central IAM) lên AWS/Azure; mỗi chi nhánh dùng SD-WAN Router + Wi-Fi 6
  AP Cloud-managed.

- **•** Kiến trúc 5 lớp: AWS EC2/ECS Auto-scaling, RDS Multi-AZ, SD-WAN
  Failover 2 nhà mạng, EDR CrowdStrike, Entra ID SSO/MFA, Datadog
  Monitoring.

- **•** Ưu điểm: Tối ưu chi phí ban đầu, mở chi nhánh mới chỉ cần cắm
  thiết bị Edge là chạy, độ sẵn sàng 99.95%.

**Kịch bản 3: Cloud-First / Serverless (Thuần Cloud)**

- **•** Mô tả: Loại bỏ hoàn toàn Server local, chuyển sang SaaS và AWS
  Lambda/Firebase.

- **•** Ưu/Nhược điểm: Khởi tạo cực nhanh nhưng OPEX lâu dài tăng cao và
  phụ thuộc hoàn toàn vào đường truyền Internet.

**PHẦN 2: BÀI TẬP LẬP KẾ HOẠCH GIAI ĐOẠN 1 (BÀI TẬP THỰC HÀNH)**

**Bước 0 & 1: Chuẩn bị đầu vào, Tên đề tài & Thông tin chung**

- **•** Đơn vị chủ quản: Công ty Cổ phần Công nghệ & Không gian làm việc
  WAYS STATION.

- **•** Tên đề tài: "Nâng cấp và chuyển đổi hạ tầng CNTT sang mô hình
  Hybrid Cloud nhằm tối ưu vận hành và mở rộng chuỗi không gian làm việc
  thông minh WAYS STATION"

- **•** Phân loại dự án: Dự án Đổi mới Hạ tầng CNTT & Chuyển đổi số (IT
  Infrastructure Modernization).

- **•** Thời gian thực hiện dự kiến: 6 tháng (Tháng 10/2026 – Tháng
  03/2027).

- **•** Tổng chi phí dự kiến: ~ 850.000.000 VNĐ (Bao gồm CAPEX mua sắm
  thiết bị Edge + OPEX Cloud/Bản quyền năm đầu).

**Bước 2: Bối cảnh & Lý do chọn đề tài (Business Case)**

WAYS STATION đang chuẩn bị mở rộng từ 3 lên 8 chi nhánh trong 12–18
tháng tới. Do mô hình vận hành phụ thuộc 100% vào CNTT (từ App đặt chỗ,
Smart Lock đến POS và Wi-Fi), hệ thống hạ tầng cũ đang trở thành "cổ
chai" kìm hãm sự phát triển:

- **1.** Hạ tầng cũ quá tải: Wi-Fi 5 và NAS local nghẽn nặng giờ cao
  điểm, CPU/RAM luôn \>85%.

- **2.** Rủi ro gián đoạn doanh thu: Sập mạng gây thiệt hại trực tiếp
  15 - 20 triệu VNĐ/giờ.

- **3.** Đề xuất giải pháp: Chuyển đổi sang Hybrid Cloud kết hợp SD-WAN
  tại chi nhánh để đảm bảo kết nối 24/7 và sẵn sàng mở rộng.

**Bước 3: Mục tiêu, KPI và Tiêu chí thành công**

- **•** Mục tiêu tổng quát: Xây dựng nền tảng hạ tầng CNTT hiện đại, tin
  cậy, đáp ứng phục vụ đồng thời \>1.000 users/chi nhánh và hỗ trợ mở
  rộng chi nhánh mới trong vài giờ.

- **•** Chỉ số Uptime: SLA ≥ 99.9%, RPO ≤ 1 giờ, RTO ≤ 2 giờ.

- **•** Chỉ số Hiệu năng & Bảo mật: Chịu tải ≥ 100 users/AP, Latency \<
  20ms, 100% Endpoint cài EDR, 100% Admin bật MFA.

- **•** Tiêu chí thành công: Vượt qua bài kiểm tra Load Test (150% tải),
  Failover Test (ngắt thử 1 đường FTTH) và Go-live tháng đầu tiên không
  xảy ra unplanned downtime.

**Bước 4: Đối tượng, Phạm vi và Giả định / Ràng buộc**

**1. Phạm vi dự án (In-Scope & Out-of-Scope)**

| **Trong phạm vi (In-Scope)** | **Ngoài phạm vi (Out-of-Scope)** |
|:---:|---|
| - Quy hoạch mạng SD-WAN & Wi-Fi 6 cho 3 chi nhánh cũ + 2 chi nhánh mới.<br>- Triển khai hạ tầng Cloud (AWS/Azure) cho Core App, DB & API Gateway.<br>- Triển khai Central IAM/SSO, MFA, EDR và Grafana Monitoring.<br>- Chuyển đổi dữ liệu từ NAS cũ lên Cloud Storage. | - Viết lại/Lập trình lại nguồn mã (Source code) của App WAYS STATION.<br>- Mua sắm/Sửa chữa phần cứng cửa Smart Lock hay nội thất bàn ghế. |

**2. Giả định & Ràng buộc (Assumptions & Constraints)**

- **•** Giả định: Nhà mạng (ISP) cung cấp đủ 2 đường FTTH độc lập
  (Viettel/VNPT) tại mỗi chi nhánh. Ngân sách OPEX Cloud (~30-40
  tr/tháng) được phê duyệt duy trì.

- **•** Ràng buộc thời gian: Công tác thi công, cắt chuyển mạng tại chi
  nhánh chỉ được làm vào ca đêm (22:00 - 06:00 sáng).

- **•** Ràng buộc tuân thủ: Tuân thủ Nghị định 13/2023/NĐ-CP về bảo vệ
  dữ liệu cá nhân khách hàng.
