BT Lập kế hoạch giai đoạn 1

## BƯỚC 1: KHẢO SÁT HIỆN TRẠNG HẠ TẦNG (AS-IS) CÓ SỐ LIỆU

### 1. Thu thập hiện trạng theo 5 lớp hạ tầng

### a. Tính toán & Kết nối

- **Máy chủ cục bộ:** Mỗi chi nhánh sử dụng 1 PC/Server Tower tự lắp ráp
  (cấu hình phân mảnh: Intel Core i5/i7 đời cũ, 16–32GB RAM), tuổi đời
  từ 2–4 năm. Tỷ lệ hỏng hóc phần cứng do bụi bẩn và vận hành 24/7 đạt
  tới 15%/năm.

- **Kết nối & Mạng:** Sử dụng cáp quang FTTH/Leased Line đơn kênh với IP
  động từ nhiều nhà mạng khác nhau. Switch tại chi nhánh là loại
  Unmanaged Switch, hoàn toàn không phân tách VLAN giữa mạng nội bộ (máy
  tính tiền, quầy thu ngân) và Wi-Fi công cộng cho khách hàng.

- **Rủi ro hạ tầng:** Mô hình mạng VPN thủ công dạng hình sao giả lập.
  Tỷ lệ dự phòng phần cứng/mạng tại chi nhánh bằng 0%; tồn tại điểm sự
  cố duy nhất (Single Point of Failure - SPOF).

### b. Vận hành (Ops)

- **Giám sát:** Không có hệ thống theo dõi tập trung (Prometheus,
  Grafana, Zabbix) hay log shipper. Việc phát hiện sự cố hoàn toàn bị
  động qua tin nhắn Zalo từ nhân viên.

- **Thời gian xử lý sự cố:**

  - MTTD (Thời gian trung bình phát hiện sự cố): Kéo dài từ 4 đến 8 giờ.

  - MTTR (Thời gian trung bình khắc phục sự cố): Kéo dài từ 12 đến 24
    giờ (do IT phải di chuyển vật lý đến chi nhánh xử lý).

- **Sao lưu & Phục hồi:** Không có Backup tự động. Nhân viên thu ngân
  sao lưu thủ công dữ liệu SQL Server ra USB/Google Drive cá nhân. RPO =
  24 giờ; RTO = 48 giờ.

### c. Bảo mật & Danh tính (Security & Identity)

- **Định danh:** Tồn tại nhiều hệ thống định danh song song, hoàn toàn
  bị phân mảnh (Face ID phòng Gym, tài khoản nạp tiền Gaming, máy tính
  tiền Bida).

- **Bảo mật dữ liệu:** Dữ liệu cá nhân nhạy cảm (ảnh CCCD, giấy tờ tùy
  thân, dữ liệu sinh trắc học Face ID) bị gửi qua ứng dụng nhắn tin cá
  nhân (Zalo). Dữ liệu lưu dưới dạng văn bản rõ (Plain-text) trên máy
  POS, không có mã hóa Data-at-Rest/Data-in-Transit.

- **Tuân thủ pháp lý:** Vi phạm nghiêm trọng các quy định bảo vệ dữ liệu
  cá nhân (Nghị định 13/2023/NĐ-CP).

### d. Ứng dụng & Tích hợp (App & Integration Platform)

- **Kiến trúc phần mềm:** Các hệ thống nghiệp vụ (MODUN Gym, CSM Net,
  Ocha POS) đều là các hệ thống đóng (Silo), không có API Gateway hay
  Middleware. Việc kết nối buộc phải truy xuất trực tiếp vào Database,
  gây ra nghẽn cổ chai.

- **Tốc độ mở rộng:** Thời gian triển khai chuẩn hóa phần mềm cho 1 chi
  nhánh mới mất 5 đến 7 ngày.

### e. Nền tảng dữ liệu (Data Platform)

- **Lưu trữ & Luồng dữ liệu:** Dữ liệu phân tán trên 34+ ổ cứng vật lý
  và hàng trăm file Excel/Google Drive rời rạc.

- **Xử lý số liệu:** Thu ngân đếm bàn/máy và gõ báo cáo Excel thủ công
  cuối ca.

- **Độ trễ dữ liệu:** Dữ liệu từ chi nhánh mất 24 đến 48 giờ mới lên tới
  Ban điều hành.

### 2. Tổng hợp các chỉ số định lượng hiện trạng (Baseline)

|  |  |
|----|----|
| **Chỉ số / Metric** | **Số liệu hiện trạng (AS-IS)** |
| SLA / Uptime hệ thống lõi | Không xác định (Downtime cao, SPOF = 100%) |
| Số sự cố vận hành / tháng | 2–3 sự cố/chi nhánh/tháng (đặc biệt rơi vào giờ cao điểm) |
| MTTD (Thời gian phát hiện sự cố) | 4 – 8 giờ |
| MTTR (Thời gian khôi phục sự cố) | 12 – 24 giờ |
| Backup Coverage / Tỷ lệ sao lưu tự động | 0% (Sao lưu thủ công bằng USB/Drive cá nhân) |
| RPO (Recovery Point Objective) | 24 giờ |
| RTO (Recovery Time Objective) | 48 giờ |
| Tỷ lệ thiết bị End-of-Support / Cũ | 100% thiết bị tại 34 chi nhánh từ 2–4 năm tuổi |
| Tỷ lệ mã hóa dữ liệu cá nhân nhạy cảm | 0% (Plain-text, gửi Zalo) |
| Độ trễ dữ liệu báo cáo (Data Latency) | 24 – 48 giờ |
| Lãng phí giờ công nhập liệu | 68 giờ công/ngày trên toàn chuỗi (2 giờ/chi nhánh/ngày) |

## BƯỚC 2: NÊU VẤN ĐỀ & RỦI RO NẾU KHÔNG ĐẦU TƯ (WHY NOW?)

## Việc duy trì hệ thống phân mảnh hiện tại khiến Ways Station chịu khoản "Nợ kỹ thuật" (Technical Debt) khổng lồ với tổng thiệt hại ước tính lên tới \> 6.3 tỷ VNĐ/năm.

### 1. Tác động vận hành

- **Gián đoạn kinh doanh giờ cao điểm:** Ngắt kết nối POS/Database khiến
  chi nhánh không thể tính tiền, in hóa đơn hay kiểm soát bàn/máy. Thiệt
  hại trực tiếp ước tính khoảng 2.4 tỷ VNĐ/năm.

- **Lãng phí nguồn lực:** 68 giờ công nhập báo cáo Excel/ngày tương
  đương 2,040 giờ/tháng (bằng 10 nhân sự full-time). Thiệt hại trực tiếp
  từ chi phí nhân công và sai sót kế toán ước tính 2.7 tỷ VNĐ/năm.

- **Đứt gãy chuỗi cung ứng F&B:** Độ trễ dữ liệu 24–48h khiến việc dự
  báo tồn kho thất bại, gây hủy hàng hết hạn hoặc thiếu hàng phục vụ.
  Thiệt hại khoảng 1.2 tỷ VNĐ/năm.

### 2. Tác động tuân thủ & an ninh (Nghị định 13/2023/NĐ-CP)

- **Rủi ro pháp lý:** Thu thập Face ID và CCCD nhưng truyền tải qua
  Zalo, lưu trữ Plain-text không mã hóa, không có cơ chế tick "Đồng ý"
  chính thức từ khách hàng.

- **Hậu quả chế tài:** Mức phạt hành chính lên đến 5% tổng doanh thu năm
  hoặc bị đình chỉ hoạt động xử lý dữ liệu. Tùy thuộc vào mức độ vi phạm
  có thể dẫn tới khủng hoảng thương hiệu.

### 3. Tác động chiến lược

- **Không thể mở rộng chuỗi:** Chi phí tích hợp và thời gian mở chi
  nhánh mới tăng tuyến tính.

- **Mù dữ liệu (Data Blindness):** Thiếu góc nhìn 360 độ về khách hàng,
  không thể triển khai cross-selling (vd: khách chơi Net sang tập Gym).

### 4. Bảng Ma trận Rủi ro & Biện pháp khắc phục

| **Hạng mục Rủi ro** | **Khả năng** | **Tác động** | **Chi phí thiệt hại ước tính** | **Biện pháp Kỹ thuật Khắc phục** |
|----|----|----|----|----|
| Vi phạm Bảo vệ Dữ liệu Cá nhân (NĐ 13/2023/NĐ-CP) | Rất Cao | Cực kỳ Nghiêm trọng | Phạt đến 5% Doanh thu năm (\>10 tỷ VNĐ) | Triển khai IAM/SSO tập trung, mã hóa AES-256 Data-at-Rest/TLS 1.3, DLP, Zero Trust Network. |
| Gián đoạn vận hành POS / Hệ thống tại chi nhánh | Rất Cao | Cao | ~2.4 tỷ VNĐ/năm | Triển khai Edge Computing (K3s) tại chi nhánh, Microservices trên K8s Cloud, Auto-scaling. |
| Lãng phí chi phí vận hành do nhập liệu thủ công | Chắc chắn | Cao | ~2.7 tỷ VNĐ/năm | Xây dựng pipeline tự động hóa tích hợp dữ liệu từ POS vào Data Warehouse. |
| Thất thoát & Đứt gãy chuỗi cung ứng F&B | Cao | Trung bình | ~1.2 tỷ VNĐ/năm | Xây dựng Real-time BI Dashboard quản trị tồn kho và luồng cung ứng 360 độ. |

## BƯỚC 3: XÁC LẬP MỤC TIÊU & KPI HẠ TẦNG (TO-BE)

| **Nhóm Chỉ số** | **Baseline hiện tại (AS-IS)** | **KPI Target (TO-BE)** | **Thời điểm & Căn cứ Đo lường** |
|----|----|----|----|
| Tính Sẵn sàng (Availability) | Không xác định (SPOF = 100%) | Uptime ≥ 99.99% cho Core API Gateway & Identity Service | Báo cáo Cloud Provider định kỳ hàng tháng sau Go-live. |
| Thời gian Khôi phục (MTTR) | 12 – 24 giờ | MTTR \< 15 phút (Tự động khôi phục container qua K8s) | Log K8s ghi nhận thời gian Pod restart. |
| Thời gian Phát hiện (MTTD) | 4 – 8 giờ | MTTD \< 5 phút (Cảnh báo tự động về Slack/Teams) | Dashboard Prometheus/Grafana alert logs. |
| Khôi phục Dữ liệu (RPO / RTO) | RPO = 24h; RTO = 48h | RPO ≤ 15 phút; RTO ≤ 4 giờ | Báo cáo kiểm tra Diễn tập Phục hồi Thảm họa (DR Drill) mỗi 6 tháng. |
| Độ trễ Dữ liệu (Data Latency) | 24 – 48 giờ | Data Latency \< 5 phút (Hiển thị Real-time BI Dashboard) | Khảo sát Timestamp đối soát giữa POS và Data Lakehouse. |
| Bảo mật & Tuân thủ NĐ13 | 0% mã hóa, lưu Plain-text | 100% dữ liệu mã hóa (AES-256 / TLS 1.3); Log tập trung lưu ≥ 1 năm | Báo cáo Penetration Testing & Kiểm toán Bảo mật. |
| Tốc độ Mở rộng Chi nhánh | 5 – 7 ngày / chi nhánh | \< 4 giờ / chi nhánh mới (Tự động hóa qua IaC) | Thời gian cấu hình thực tế khi mở chi nhánh thứ 35+. |
| Tỷ lệ lỗi do Triển khai phần mềm | \> 30% | \< 5% (Áp dụng CI/CD tự động và Canary Release) | Số lượng ticket lỗi trên Jira sau mỗi đợt Release. |

## BƯỚC 4: XÂY DỰNG PHƯƠNG ÁN KIẾN TRÚC TO-BE (2–3 LỰA CHỌN)

### 1. Mô tả Chi tiết 3 Kịch bản Kiến trúc

### Kịch bản 1: On-premise Data Center (Nâng cấp Trung tâm Dữ liệu Tại chỗ)

- **Mô tả:** Thuê tủ Rack tại Data Center Tier 3 (VNPT/FPT). Đầu tư mua
  mới cụm Server Blade, SAN Storage, Switch Core, Firewall phần cứng.
  Dùng VMware vSphere để ảo hóa. Kéo đường truyền Leased Line riêng từ
  34 chi nhánh về DC.

- **Ưu điểm:** Kiểm soát 100% tài sản và dữ liệu; chi phí OPEX dài hạn
  ổn định sau khấu hao.

- **Nhược điểm:** CAPEX ban đầu cực kỳ lớn; thời gian mở rộng rất chậm
  (8–12 tuần chờ phần cứng); yêu cầu đội ngũ IT Sysadmin đông đảo vận
  hành 24/7.

### Kịch bản 2: Hybrid Cloud Platform (Điện toán đám mây lai) - \[PHƯƠNG ÁN KHUYẾN NGHỊ\]

- **Mô tả:**

  - *Tại 34+ Chi nhánh (Edge Layer):* Cài đặt Kubernetes siêu nhẹ (K3s)
    trên PC hiện có. Duy trì các dịch vụ POS/Local Cache SQLite theo cơ
    chế **Offline-first**. Chi nhánh vẫn bán hàng, in bill bình thường
    kể cả khi mất Internet; dữ liệu tự đồng bộ lại khi có mạng.

  - *Tại Cloud Layer (AWS/Public Cloud):* Đặt các hệ thống tính toán
    nặng và hội tụ dữ liệu.

    - Security: Cloudflare WAF + Identity Provider (Keycloak/Auth0).

    - App Integration: API Gateway (Kong/Apisix) + Event Bus (Apache
      Kafka / CDC Debezium).

    - Data Platform: Data Lakehouse (Amazon S3 + Snowflake / Redshift).

  - *Kết nối & DR:* SD-WAN với IPsec VPN điểm-điểm mã hóa kết nối Edge
    tới Cloud VPC. Cụm K8s Multi-AZ đảm bảo High Availability (HA) và
    Nhân bản dữ liệu tự động.

- **Ưu điểm:** Tối ưu hóa dòng tiền (chuyển CAPEX thành OPEX linh hoạt);
  khả năng Auto-scaling vượt trội vào giờ cao điểm; đảm bảo chi nhánh
  hoạt động liên tục ngay cả khi rớt mạng.

- **Nhược điểm:** Kiến trúc hệ thống phức tạp; yêu cầu đội ngũ IT chuyển
  đổi sang năng lực Cloud-Native / DevOps.

### Kịch bản 3: Cloud-First / Pure SaaS (Thuần Đám mây)

- **Mô tả:** Bê toàn bộ ứng dụng và Database lên Cloud. Thay thế thiết
  bị POS tại chi nhánh bằng Tablet/Trình duyệt Web kết nối trực tiếp lên
  phần mềm SaaS trên Cloud.

- **Ưu điểm:** Triển khai siêu nhanh; không tốn chi phí quản lý phần
  cứng Edge.

- **Nhược điểm:** Phụ thuộc 100% vào Internet. Khi nhà mạng gặp sự cố
  đứt cáp, toàn bộ 34 chi nhánh bị đóng băng hoàn toàn không thể phục vụ
  khách hàng.

### 2. So sánh & Đánh giá Chi tiết 3 Phương án

| **Tiêu chí So sánh** | **Kịch bản 1: On-premise DC** | **Kịch bản 2: Hybrid Cloud (ĐỀ XUẤT)** | **Kịch bản 3: Cloud-First** |
|----|----|----|----|
| Chi phí đầu tư ban đầu (CAPEX) | Rất Cao (Hàng chục tỷ mua sắm phần cứng) | Thấp (Tận dụng PC Edge hiện có, chỉ nâng cấp Router) | Rất Thấp (Chỉ mua thiết bị đầu cuối) |
| Chi phí vận hành hàng tháng (OPEX) | Trung bình (Thuê rack, điện, bảo trì) | Linh hoạt (Trả tiền theo lưu lượng thực tế) | Rất Cao (Phí bản quyền SaaS & Data Transfer) |
| Tốc độ Mở rộng & Tự động Scaling | Chậm (Phụ thuộc mua sắm phần cứng 8-12 tuần) | Tức thì (Auto-scaling trên Cloud trong vài phút) | Tức thì (Thuần Cloud) |
| Độ chịu lỗi khi Đứt mạng Internet | Khá (Chạy cục bộ) | Tuyệt vời (Kiến trúc Offline-First tại Edge K3s) | Cực kỳ Rủi ro (Tê liệt hoàn toàn 100%) |
| Bảo mật & Tuân thủ NĐ13 | Rất Tốt (Kiểm soát 100%) | Rất Tốt (Mã hóa VPN IPsec, IAM/SSO tập trung) | Rủi ro nếu nhà cung cấp SaaS cấu hình sai |
| Khả năng Tích hợp hệ thống mở | Khó khăn (Mở port Firewall thủ công) | Rất Dễ dàng (Qua API Gateway & Event Bus) | Dễ dàng (Tùy thuộc vào SaaS Provider) |
| ĐÁNH GIÁ KHUYẾN NGHỊ | LOẠI BỎ | LỰA CHỌN PHƯƠNG ÁN NÀY | LOẠI BỎ |
