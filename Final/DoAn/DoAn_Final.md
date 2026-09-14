# 1. Tóm tắt điều hành (Executive Summary)

**ĐỒ ÁN MÔN HỌC: ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT**
**Dự án:** Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station

Dự án này đề xuất đầu tư Nền tảng tích hợp ứng dụng (Lớp 4) và Nền tảng dữ liệu tập trung (Lớp 5) cho chuỗi Ways Station nhằm giải quyết các thách thức nghiêm trọng về đứt gãy tích hợp, phân mảnh dữ liệu và rủi ro rò rỉ dữ liệu cá nhân (PII - Personally Identifiable Information) trên 34+ chi nhánh.

Thông qua việc đánh giá 3 kịch bản kiến trúc, dự án lựa chọn mô hình **Hybrid Cloud (Lai)** làm giải pháp tối ưu. Mô hình này kết hợp khả năng xử lý mạnh mẽ của điện toán đám mây cho phân tích dữ liệu và sự ổn định của hệ thống máy chủ tại các chi nhánh (Edge Cluster), đảm bảo duy trì hoạt động bán hàng ngay cả khi mất kết nối mạng, đồng thời tuân thủ nghiêm ngặt các quy định về bảo mật dữ liệu (Nghị định 13/2023/NĐ-CP).

Dự án được lên kế hoạch triển khai trong vòng 16 tuần (4 tháng) với 5 pha rõ ràng. Tổng mức đầu tư (CAPEX - Capital Expenditure) là **1.308.800.000 VNĐ**, và Tổng chi phí sở hữu (TCO - Total Cost of Ownership) trong 3 năm dự kiến là **5.209.160.000 VNĐ**. Lợi ích mang lại không chỉ giải quyết các vấn đề vận hành, tiết kiệm ~2.500 giờ công/năm, giảm sai lệch doanh thu mà còn nâng cấp khả năng ra quyết định theo thời gian thực với sự hỗ trợ của mô hình AI (Artificial Intelligence), cho thời gian thu hồi vốn ước tính khoảng 2.75 năm.

# 2. Hiện trạng AS-IS & vấn đề

## 2.1. Khảo sát hiện trạng hạ tầng (AS-IS) có số liệu

**Điểm nghẽn hiện trạng (Baseline có định lượng):**
- **Điểm nghẽn 1 (Tích hợp & Vận hành Lớp 4 - App & Integration Platform):** 34 chi nhánh sở hữu 8 hệ thống phần mềm rời rạc (POS - Point of Sale, Bida, Gym, Kho...) hoạt động độc lập và phân mảnh. Tỉ lệ luồng tích hợp tự động là **0%**. 100% giao tiếp đi qua 3 kênh thủ công (Tổng đài, Zalo, Sổ giấy).
- **Điểm nghẽn 2 (Dữ liệu & Quyết định Lớp 5 - Data Platform):** Không có kho dữ liệu tập trung. Báo cáo được làm thủ công bằng Excel tiêu tốn **~2.500 giờ công/năm**. Độ trễ dữ liệu phục vụ quản trị lên tới **24 - 48 giờ**. Tỷ lệ sai lệch số liệu doanh thu khi đối soát là **3,8%**.
- **Điểm nghẽn 3 (Bảo mật & Định danh Lớp 3/4):** Khách hàng phải dùng tài khoản riêng cho từng mảng. Đáng lưu ý, 100% ảnh giấy tờ tùy thân của khách hàng và dữ liệu Face ID được gửi qua Zalo cá nhân của nhân viên, không có cơ chế mã hóa. Sao lưu cục bộ có tỉ lệ thành công chỉ **47%** với RPO (Recovery Point Objective) lên đến 24 giờ.

## 2.2. Nêu vấn đề và rủi ro nếu không đầu tư (WHY NOW?)

Từ các điểm nghẽn hiện trạng, hệ thống đang phải đối mặt với nhiều hạn chế kỹ thuật và rủi ro lớn nếu không được giải quyết ngay:

- **Rủi ro vận hành (Vấn đề 1 - Đứt gãy tích hợp):** Việc thiếu API (Application Programming Interface) Gateway khiến hệ thống chịu tải kém vào giờ cao điểm, gây gián đoạn bán hàng. Thời gian phát hiện sự cố chậm (4-8 giờ). Hàng ngàn giờ công bị lãng phí do đối soát thủ công và nhập liệu kép.
- **Rủi ro chiến lược (Vấn đề 2 - Mù dữ liệu thực thời):** Độ trễ dữ liệu 48 giờ khiến việc ra quyết định bị chậm trễ. Việc thiếu nguồn dữ liệu chuẩn hóa và tập trung để phân tích và dự báo nhu cầu dẫn đến lãng phí nguyên vật liệu F&B (Food and Beverage) và sai lệch trong việc sắp xếp ca trực của nhân viên. Không thể bán chéo dịch vụ do khách hàng không có định danh duy nhất (SSO - Single Sign-On).
- **Rủi ro tuân thủ (Vấn đề 3 - Lỗ hổng bảo mật PII):** Việc lưu trữ dữ liệu cá nhân (PII) như ảnh CCCD, Face ID phân tán trên điện thoại cá nhân vi phạm nghiêm trọng **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân. Doanh nghiệp đối mặt với rủi ro bị phạt lên đến 5% tổng doanh thu và đánh mất uy tín thương hiệu.

# 3. Mục tiêu & KPI (Key Performance Indicator) TO-BE

Bộ KPI kỹ thuật được thiết lập theo chuẩn quốc tế nhằm giải quyết triệt để 3 vấn đề nêu trên. Tính liên kết chặt chẽ được thể hiện thông qua Ma trận Truy vết (Traceability Matrix).

### 3.1. Ma trận Truy vết: Vấn đề $\rightarrow$ Mục tiêu $\rightarrow$ KPI
| Vấn đề giải quyết | Mục tiêu kiến trúc | KPI Kỹ thuật đo lường (Target) |
| :--- | :--- | :--- |
| **Vấn đề 1:** Đứt gãy tích hợp, gián đoạn kinh doanh | Đảm bảo hệ thống đạt độ sẵn sàng cao, có khả năng tự phục hồi nhanh (Self-healing). | KPI 1.1: **Uptime $\ge$ 99.99%** <br> KPI 1.2: **MTTR (Mean Time To Recovery) $\le$ 30 phút** |
| **Vấn đề 2:** Mù dữ liệu, báo cáo thủ công | Cung cấp dữ liệu chuẩn thời gian thực cho kho dữ liệu và hỗ trợ thuật toán AI dự báo chính xác. | KPI 2.1: **Độ trễ dữ liệu $\le$ 5 giây** <br> KPI 2.2: **Sai số dự báo (MAPE - Mean Absolute Percentage Error) $<$ 15%** |
| **Vấn đề 3:** Lỗ hổng rò rỉ dữ liệu PII | Ngăn chặn rò rỉ PII và đảm bảo không mất mát dữ liệu quan trọng khi có thảm họa. | KPI 3.1: **Tỷ lệ mã hóa PII = 100%** <br> KPI 3.2: **RPO $\le$ 15 phút** |

### 3.2. Định lượng KPI theo công thức chuẩn (Standards)

1. **KPI 1.1 - Tính sẵn sàng (Availability / Uptime) $\ge 99.99\%$ (Chuẩn Google SRE (Site Reliability Engineering)):**
   - *Công thức:* $Uptime = \frac{\text{Total Time} - \text{Downtime}}{\text{Total Time}} \times 100\%$
   - *Ràng buộc:* Tổng thời gian chết (Downtime) trong 1 tháng (43.200 phút) không vượt quá 4,32 phút.

2. **KPI 1.2 - Thời gian khôi phục trung bình (MTTR) $\le 30$ phút (Chuẩn Atlassian ITSM (IT Service Management)):**
   - *Công thức:* $MTTR = \frac{\text{Tổng thời gian gián đoạn (Downtime)}}{\text{Tổng số lượng sự cố}}$
   - *Ý nghĩa:* Hệ thống (VD: Kubernetes) phải tự động khởi tạo lại service lỗi trong vài phút trước khi ảnh hưởng diện rộng.

3. **KPI 2.1 - Độ trễ dữ liệu (Data Freshness) $\le 5$ giây (Chuẩn ISO (International Organization for Standardization)/IEC (International Electrotechnical Commission) 25012):**
   - *Công thức:* $\Delta t_{freshness} = t_{DataLake} - t_{POS} \le 5s$. (Rút ngắn độ trễ từ 48 giờ xuống vài giây).

4. **KPI 2.2 - Sai số dự báo mô hình AI (MAPE) $< 15\%$ (Chuẩn Scikit-Learn):**
   - *Công thức:* $MAPE = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%$ *(Với $y_i$ là số khách thực tế, $\hat{y}_i$ là dự báo).*
   - *Cam kết Baseline:* Mô hình AI phải cải thiện sai số dự báo **tối thiểu 10%** so với phương pháp dự báo truyền thống (Moving Average 7 ngày, Baseline MAPE ước tính ~25-30% theo khảo sát vận hành hiện tại). Độ chênh lệch hiệu suất giữa các ngữ cảnh dữ liệu khác nhau (chi nhánh Gym vs Gaming vs Hub) không vượt quá $\Delta \le 10\%$.

5. **KPI 3.1 - Tỷ lệ mã hóa dữ liệu PII = 100% (Chuẩn NIST (National Institute of Standards and Technology) SP 800-175B):**
   - *Công thức:* $\text{Encryption Coverage} = \frac{\text{Số trường PII được mã hóa AES-256 (Advanced Encryption Standard)}}{\text{Tổng số trường PII trong hệ thống}} \times 100\%$
   - *Ràng buộc:* Toàn bộ dữ liệu nhạy cảm (ảnh CCCD, Face ID, số điện thoại) phải được mã hóa 100% cả khi lưu trữ (at-rest) và khi truyền tải (in-transit), chuyển từ hiện trạng 0% sang mục tiêu 100%.
   - *Trích dẫn:* NIST (2020), *SP 800-175B: Guideline for Using Cryptographic Standards in the Federal Government*.

6. **KPI 3.2 - Mục tiêu điểm khôi phục (RPO) $\le 15$ phút (Chuẩn AWS (Amazon Web Services) DR (Disaster Recovery)):**
   - *Ý nghĩa:* Dung sai mất mát dữ liệu tối đa tính từ thời điểm thảm họa xảy ra là 15 phút.

# 4. Phạm vi & giả định / ràng buộc

- **Đơn vị thụ hưởng:** Chuỗi Ways Station (34+ chi nhánh đa dịch vụ: Gym, Gaming, Billiards, Cầu lông, Hub).
- **Lớp năng lực đầu tư:** Lớp (4) Nền tảng ứng dụng & tích hợp (App & Integration Platform) và Lớp (5) Nền tảng dữ liệu (Data Platform). Kế thừa hạ tầng mạng và phần cứng hiện có.

# 5. Các phương án kiến trúc (On-prem / Hybrid / Cloud) + so sánh

Để thỏa mãn bộ KPI khắt khe trên đồng thời đảm bảo đặc thù nghiệp vụ (các điểm bán phải tiếp tục tính tiền offline kể cả khi đứt cáp internet), dự án phân tích 3 kịch bản kiến trúc:

### 5.1. Bảng so sánh 3 kịch bản kiến trúc

| Tiêu chí bắt buộc để đạt KPI | On-Premise 100% (Tập trung) | Cloud-Native 100% (Thuần đám mây) | Hybrid Cloud (Lai) - Khuyến nghị |
| :--- | :---: | :---: | :---: |
| **1. Đảm bảo Uptime 99.99% khi rớt mạng chi nhánh** | [x] | [ ] | [x] |
| **2. Khả năng mở rộng tự động (Auto-scaling)** | [ ] | [x] | [x] |
| **3. Tuân thủ vị trí lưu trữ dữ liệu PII (Nghị định 13)** | [x] | [ ] | [x] |
| **4. Tối ưu chi phí đầu tư ban đầu (CAPEX) thấp** | [ ] | [x] | [x] |
| **5. Thời gian triển khai dịch vụ nhanh (Agility)** | [ ] | [x] | [x] |
| **6. Khả năng khôi phục thảm họa (Active-Active)** | [ ] | [x] | [x] |
| **Tổng số tiêu chí đáp ứng** | **2 / 6** | **4 / 6** | **6 / 6** |

### 5.2. Sự liên kết và Cơ sở biện luận chọn HYBRID CLOUD
**Phương án lựa chọn: Kịch bản Hybrid Cloud (Lai)**
Kiến trúc Hybrid Cloud là giải pháp duy nhất cân bằng hoàn hảo giữa Rủi ro (Risk) và Lợi ích (Reward) để xử lý triệt để bài toán mâu thuẫn (như thể hiện ở bảng trên): Vừa cần sức mạnh co giãn của Cloud (đáp ứng Tiêu chí 2, 4, 5, 6) để xử lý dữ liệu và tích hợp API, vừa cần độ ổn định độc lập tại chi nhánh để đối phó với rủi ro rớt mạng (đáp ứng Tiêu chí 1) và tuân thủ vị trí lưu trữ (đáp ứng Tiêu chí 3). Cơ sở biện luận được thiết kế liên kết chặt chẽ với các KPI như sau:

- **Hợp nhất Lớp 4 & Tăng cường Uptime (Đạt KPI 1.1 & 1.2):** Cổng API Gateway và hệ thống điều phối thông điệp (Kafka) được đặt trên Public Cloud để tiếp nhận hàng ngàn request cùng lúc. Tại 34 chi nhánh sẽ cài đặt Edge Cluster (K3s/Kafka con) hoạt động như bộ đệm. Khi chi nhánh mất kết nối mạng, phần mềm vẫn gọi API cục bộ để tính giờ ưu tiên ngoại tuyến; khi có mạng, dữ liệu tự đồng bộ bù về Cloud, đảm bảo MTTR $\le 30$ phút mà khách hàng không bị gián đoạn.
- **Hợp nhất Lớp 5 & Nâng cao chất lượng dữ liệu (Đạt KPI 2.1 & 2.2):** Xây dựng kho dữ liệu (Data Lakehouse) trên Cloud cung cấp sức mạnh điện toán vô hạn. Áp dụng luồng Data Streaming (CDC - Change Data Capture) để bắt sự kiện thay đổi dữ liệu tại chi nhánh đẩy thẳng về Cloud trong thời gian thực, đáp ứng Data Freshness $\le 5s$, làm đầu vào chất lượng cho mô hình học máy (Machine Learning) tối ưu hóa dự báo.
- **Bảo mật PII & Tuân thủ NĐ13 (Đạt KPI 3.1 & 3.2):** Kiến trúc tuân thủ mô hình Zero Trust. Các thông tin định danh nhạy cảm cực cao (Face ID, thẻ CCCD) và hệ thống Quản lý định danh (IAM - Identity and Access Management) được giữ lại tại máy chủ vật lý On-Premise do doanh nghiệp tự quản lý và mã hóa AES-256 100%. Dữ liệu vận hành (hóa đơn, điểm danh) được ẩn danh trước khi đẩy lên Cloud, hoàn toàn loại bỏ rủi ro mất kiểm soát dữ liệu và tuân thủ tuyệt đối Nghị định 13/2023/NĐ-CP.

# 6. Yêu cầu kỹ thuật (HA - High Availability / DR / Security / Ops / Performance)

Yêu cầu kỹ thuật được chia thành 4 nhóm, đủ chi tiết để chào thầu/mua sắm và làm cơ sở nghiệm thu. Mỗi yêu cầu được liên kết ngược (traceability) với KPI đã cam kết tại Bước 3. Các yêu cầu này tập trung hiện thực hóa **Lớp (4) Nền tảng ứng dụng & tích hợp** và **Lớp (5) Nền tảng dữ liệu**.

### 6.1. Nhóm 1 — Hiệu năng & Dung lượng (Performance & Capacity)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-P01 | **[Lớp 4]** API Gateway xử lý đồng thời (concurrent connections) tại Cloud | ≥ 2.000 kết nối đồng thời (tính cho 34 chi nhánh × ~60 POS/thiết bị + đệm 20%) | KPI 1.1 — Uptime | Load test đạt 2.000 concurrent connections, error rate < 0.1% |
| TR-P02 | **[Lớp 4]** Thời gian phản hồi API (P95) cho giao dịch POS | ≤ 200 ms (round-trip từ Edge → Cloud → Edge) | KPI 1.1, 1.2 | Benchmark P95 ≤ 200 ms trên 10.000 requests liên tục |
| TR-P03 | **[Lớp 5]** Throughput Data Pipeline (CDC Streaming) | ≥ 5.000 events/giây (tổng 34 chi nhánh, giờ cao điểm) | KPI 2.1 — Data Freshness ≤ 5s | Stress test pipeline đạt throughput mục tiêu, không mất sự kiện |
| TR-P04 | **[Lớp 5]** Dung lượng Data Lakehouse (Cloud) | Tối thiểu 2 TB ban đầu, hỗ trợ mở rộng tự động lên 10 TB trong 3 năm | KPI 2.1 | Storage auto-scaling hoạt động khi đạt 80% capacity |
| TR-P05 | **[Lớp 4]** Sizing Edge Cluster mỗi chi nhánh | ≥ 4 vCPU, 8 GB RAM, 256 GB SSD — đủ chạy K3s + Kafka broker + Local DB (Database) cache | KPI 1.1 — Offline mode | Chi nhánh vận hành bình thường khi mất mạng ≥ 4 giờ |
| TR-P06 | **[Lớp 4 & 5]** Sizing Cloud Kubernetes Cluster | 6 nodes × (4 vCPU, 16 GB RAM) — chạy API Gateway, Kafka Cluster, Data Pipeline, AI Inference | KPI 1.1, 2.2 | Cluster hoạt động ổn định dưới tải 80% capacity |
| TR-P07 | **[Lớp 5]** Suy luận mô hình AI (Inference latency) | ≤ 500 ms / 1 request dự báo | KPI 2.2 — MAPE | Benchmark inference trên 1.000 requests liên tiếp |

### 6.2. Nhóm 2 — Độ sẵn sàng cao & Khôi phục thảm họa (HA / DR)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-H01 | Kubernetes Cloud: Multi-zone Active-Active | Tối thiểu 2 availability zones, tự động failover trong ≤ 60 giây | KPI 1.1 — 99.99% | Test failover: tắt 1 zone, hệ thống tự phục hồi ≤ 60s |
| TR-H02 | Kafka Cluster: Replication factor | ≥ 3 replicas cho mọi topic nghiệp vụ | KPI 2.1, 3.2 | Tắt 1 broker, không mất message, producer/consumer tiếp tục hoạt động |
| TR-H03 | Edge Cluster: Store-and-Forward khi offline | Queue cục bộ chứa tối thiểu 48 giờ giao dịch (~50.000 events/chi nhánh) | KPI 1.1 | Ngắt mạng 4 giờ, kiểm tra 100% events được đồng bộ bù khi có mạng |
| TR-H04 | Backup Data Lakehouse (Immutable backup) | Backup tự động hàng ngày, retention 30 ngày, RPO ≤ 15 phút | KPI 3.2 — RPO | Test restore từ backup: dữ liệu khôi phục đầy đủ, thời gian restore ≤ 2 giờ |
| TR-H05 | Backup PostgreSQL (Managed) | Point-in-time recovery (PITR - Point-In-Time Recovery), retention 7 ngày, RPO ≤ 15 phút | KPI 3.2 | Restore PITR đến thời điểm bất kỳ trong 7 ngày, kiểm tra tính toàn vẹn dữ liệu |
| TR-H06 | DR Drill (Diễn tập khôi phục thảm họa) | Thực hiện ≥ 2 lần/năm, RTO (Recovery Time Objective) ≤ 4 giờ (toàn hệ thống) | KPI 1.2 | Biên bản diễn tập DR: hệ thống phục hồi hoàn toàn trong ≤ 4 giờ |

### 6.3. Nhóm 3 — Bảo mật & Danh tính (Security + Identity)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-S01 | IAM / SSO cho toàn hệ thống (Keycloak hoặc tương đương) | 100% ứng dụng nội bộ xác thực qua SSO, hỗ trợ OIDC (OpenID Connect)/SAML (Security Assertion Markup Language) | KPI 3.1 | Đăng nhập 1 lần truy cập toàn bộ ứng dụng; token hết hạn đúng policy |
| TR-S02 | MFA (Multi-Factor Authentication) cho tài khoản đặc quyền (Admin, DevOps) | 100% tài khoản admin bắt buộc MFA (TOTP - Time-based One-Time Password / WebAuthn) | KPI 3.1 | Kiểm tra: đăng nhập admin không có MFA bị từ chối |
| TR-S03 | Mã hoá PII at-rest (On-Premise) | AES-256 cho toàn bộ trường PII (CCCD, Face ID, SĐT) | KPI 3.1 — 100% | Audit: 100% trường PII trong DB được mã hoá, không có plaintext |
| TR-S04 | Mã hoá in-transit | TLS (Transport Layer Security) 1.2+ cho mọi kết nối (Edge ↔ Cloud, API Gateway, CDC) | KPI 3.1 | Scan SSL/TLS: không tồn tại kết nối không mã hoá |
| TR-S05 | Ẩn danh hoá dữ liệu trước khi đẩy lên Cloud | Loại bỏ/hash trường PII trước khi ghi vào Data Lakehouse | KPI 3.1 — NĐ13 | Kiểm tra mẫu dữ liệu trên Cloud: 0 bản ghi chứa PII dạng plaintext |
| TR-S06 | Log tập trung (Centralized Logging) | Lưu trữ ≥ 90 ngày, hỗ trợ tìm kiếm và cảnh báo bất thường | KPI 3.1 | Query log truy cập PII, log thay đổi cấu hình — kết quả trả về đúng |
| TR-S07 | Quét lỗ hổng bảo mật (Vulnerability Scan) | Quét tự động hàng tuần, 0 lỗ hổng Critical/High tồn tại quá 72 giờ | KPI 3.1 | Báo cáo scan: 0 Critical/High chưa vá |
| TR-S08 | Phân quyền RBAC (Role-Based Access Control) theo nguyên tắc Least Privilege | Tối thiểu 4 vai trò: SuperAdmin, Admin chi nhánh, Nhân viên, Auditor | KPI 3.1 | Ma trận phân quyền được audit, tài khoản test không truy cập vượt quyền |

### 6.4. Nhóm 4 — Vận hành (Operations)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-O01 | Hệ thống Monitoring & Observability (Prometheus + Grafana) | Dashboard theo dõi: CPU/RAM/Disk/Network toàn cluster + API latency + Pipeline status | KPI 1.1, 1.2 | Demo dashboard: tất cả metrics hiển thị real-time, dữ liệu lịch sử 30 ngày |
| TR-O02 | Alerting & Escalation | Cảnh báo qua Slack/Email/SMS trong ≤ 5 phút khi metric vượt ngưỡng | KPI 1.2 — MTTR | Test: trigger cảnh báo CPU > 85%, thông báo đến đúng người trong ≤ 5 phút |
| TR-O03 | CMDB (Configuration Management Database) | Danh mục tài sản: 34 Edge devices + Cloud resources + License, cập nhật tự động | Quản trị tài sản | CMDB (Configuration Management Database) liệt kê 100% tài sản, thông chính xác so với thực tế |
| TR-O04 | Patching & Update tự động (IaC - Infrastructure as Code) | Terraform/Ansible quản lý toàn bộ cấu hình; rollback < 15 phút | KPI 1.2 | Thực hiện rollback cấu hình: hệ thống trở về trạng thái trước trong ≤ 15 phút |
| TR-O05 | Runbook / SOP (Standard Operating Procedure) vận hành | Tối thiểu 10 quy trình chuẩn: xử lý sự cố P1–P4, backup/restore, DR, patching, onboarding chi nhánh mới | KPI 1.2 | Tài liệu Runbook đầy đủ, thử nghiệm 3 kịch bản sự cố theo Runbook — thành công |
| TR-O06 | CI/CD (Continuous Integration/Continuous Deployment) Pipeline | Tự động: build → test → deploy lên Staging → approve → Production | KPI 1.1 | Demo CI/CD: commit code → deploy thành công lên Staging trong ≤ 15 phút |
| TR-O07 | Capacity Planning | Báo cáo dự báo tài nguyên hàng quý, cảnh báo khi sử dụng vượt 70% | Tối ưu chi phí | Báo cáo capacity quý đầu tiên sau Go-live có dữ liệu trending |

# 7. Danh mục hạng mục đầu tư (thiết bị / bản quyền / dịch vụ)

Danh mục được tách rõ 4 nhóm: Thiết bị/Phần cứng, Phần mềm bản quyền, Dịch vụ triển khai, và Chi phí hạ tầng định kỳ.

### 7.1. Thiết bị / Phần cứng

| # | Hạng mục | Mô tả / Thông số giả định | Số lượng | Ghi chú |
|:---:|:---|:---|:---:|:---|
| 1 | Edge Mini Server (chi nhánh) | Intel NUC hoặc tương đương: 4 vCPU, 8 GB RAM, 256 GB NVMe SSD. Chạy K3s, Kafka broker, Local DB cache. | 34 bộ | 1 bộ/chi nhánh. Dự phòng 2 bộ thêm cho thay thế nóng → Tổng mua: 36 bộ |
| 2 | UPS (Uninterruptible Power Supply) cho Edge Server | UPS 650VA, thời gian giữ tải ≥ 15 phút | 34 bộ | Đảm bảo Edge không mất điện đột ngột → dữ liệu queue không hỏng |
| 3 | On-Premise Server (HQ - Headquarters — IAM + PII DB) | Rack Server 2U: 2× Xeon 8 cores, 64 GB ECC RAM, 2× 1TB SSD RAID-1, Redundant PSU | 2 bộ | Active-Passive cho HA. Đặt tại trụ sở chính (HQ) |
| 4 | Switch Managed (HQ) | Switch Layer 2 Managed, 24 ports GbE, VLAN support | 1 bộ | Phân tách VLAN: IAM Server / Management / Guest |
| 5 | Firewall Appliance (HQ) | Next-Gen Firewall: IPS/IDS (Intrusion Detection System), VPN (Virtual Private Network) site-to-site, 1 Gbps throughput | 1 bộ | Bảo vệ On-Premise IAM/PII, kết nối VPN tới Cloud |

### 7.2. Phần mềm bản quyền

| # | Hạng mục | Loại giấy phép | Số lượng | Ghi chú |
|:---:|:---|:---|:---:|:---|
| 1 | **[Lớp 4]** Kubernetes (K3s — Edge, K8s — Cloud) | Open-source (Apache 2.0) | — | Miễn phí |
| 2 | **[Lớp 4 & 5]** Apache Kafka | Open-source (Apache 2.0) | — | Miễn phí. Hoặc dùng Managed Kafka trên Cloud (tính vào OPEX (Operational Expenditure)) |
| 3 | **[Lớp 3]** Keycloak (IAM/SSO) | Open-source (Apache 2.0) | — | Miễn phí |
| 4 | **[Lớp 5]** PostgreSQL (Data Warehouse + PII DB) | Open-source (PostgreSQL License) | — | On-Prem: tự cài. Cloud: dùng Managed PostgreSQL (OPEX) |
| 5 | **[Lớp 5]** Apache Airflow (Data Pipeline orchestration) | Open-source (Apache 2.0) | — | Miễn phí |
| 6 | **[Lớp 5]** MLflow (Model Registry) | Open-source (Apache 2.0) | — | Miễn phí |
| 7 | **[Lớp Vận hành]** Prometheus + Grafana + Loki (Monitoring stack) | Open-source (Apache 2.0 / AGPL) | — | Miễn phí |
| 8 | **[Lớp Vận hành]** Terraform + Ansible (IaC) | Open-source (MPL 2.0 / GPL) | — | Miễn phí |
| 9 | OS (Operating System) cho On-Prem Server | Ubuntu Server 22.04 LTS | 2 licenses | Miễn phí (Community) |
| 10 | OS cho Edge Server | Ubuntu Server 22.04 LTS (minimal) | 36 licenses | Miễn phí |
| 11 | Firewall License (NGFW - Next-Generation Firewall) | Subscription hãng (Fortinet/Palo Alto) | 1 license/năm | Tính vào OPEX |

> **Chiến lược bản quyền:** Ưu tiên tối đa phần mềm mã nguồn mở ổn định, cộng đồng lớn để giảm chi phí license — phù hợp với ngân sách doanh nghiệp vừa (SMB). Tuân thủ đầy đủ điều khoản giấy phép OSS (Open Source Software).

### 7.3. Dịch vụ triển khai

| # | Hạng mục dịch vụ | Phạm vi | Ghi chú |
|:---:|:---|:---|:---|
| 1 | Thiết kế kiến trúc chi tiết (HLD - High-Level Design + LLD - Low-Level Design) | Kiến trúc Cloud K8s, Edge K3s, Data Pipeline, IAM, Network topology | Bao gồm review & phê duyệt |
| 2 | Triển khai & Cấu hình hạ tầng Cloud | Dựng K8s cluster, Kafka, Airflow, PostgreSQL managed, Object Storage, VPN | IaC (Terraform) |
| 3 | Triển khai & Cấu hình 34 Edge Cluster | Cài đặt K3s, Kafka broker, Local DB cache, Store-and-Forward agent | Đóng Golden Image, deploy hàng loạt |
| 4 | Triển khai On-Premise Server (HQ) | Cài đặt Keycloak, PII Database, Firewall, VPN, hardening | Theo CIS (Center for Internet Security) Benchmark |
| 5 | Migrate dữ liệu | Di chuyển dữ liệu từ 8 hệ thống POS rời rạc → Data Lakehouse (lịch sử ≥ 12 tháng) | ETL (Extract, Transform, Load) scripts + kiểm tra toàn vẹn |
| 6 | Tích hợp hệ thống (API Integration) | Kết nối POS/Gym/Bida/Kho... vào API Gateway; CDC streaming setup | 8 hệ thống × 34 chi nhánh |
| 7 | Hardening & Security audit | Áp dụng CIS Benchmark, quét lỗ hổng, cấu hình WAF (Web Application Firewall)/IDS | Trước Go-live |
| 8 | Đào tạo & Chuyển giao | Đào tạo đội ngũ IT vận hành (3 buổi), đào tạo Admin chi nhánh (2 buổi), bàn giao Runbook | Bao gồm tài liệu |

### 7.4. Chi phí hạ tầng định kỳ (sẽ chi tiết hoá tại Bước 8)

| # | Hạng mục | Chu kỳ | Ghi chú |
|:---:|:---|:---|:---|
| 1 | Cloud Kubernetes Cluster (6 nodes) | Hàng tháng | Managed K8s |
| 2 | Managed PostgreSQL (HA) | Hàng tháng | Production DB |
| 3 | Managed Kafka (hoặc self-managed trên K8s) | Hàng tháng | Message streaming |
| 4 | Object Storage (S3 - Simple Storage Service) | Hàng tháng | Raw data + Model artifacts |
| 5 | GPU (Graphics Processing Unit) Instance (huấn luyện AI, 1 lần/tháng) | Hàng tháng | Spot/Preemptible |
| 6 | Đường truyền Internet chi nhánh (34 đường) | Hàng tháng | Bandwidth đảm bảo CDC streaming |
| 7 | VPN Site-to-Site (HQ ↔ Cloud) | Hàng tháng | Kết nối bảo mật |
| 8 | Firewall NGFW License renewal | Hàng năm | Subscription |
| 9 | Support & Bảo trì phần cứng On-Prem | Hàng năm | Bảo hành mở rộng |

# 8. Dự toán CAPEX / OPEX & TCO 3–5 năm

### 8.1. Chi phí đầu tư ban đầu (CAPEX)

#### A. Phần cứng

| Hạng mục | Đơn giá (VNĐ) | Số lượng | Thành tiền (VNĐ) |
|:---|---:|:---:|---:|
| Edge Mini Server (Intel NUC i5, 8GB, 256GB SSD) | 8.500.000 | 36 | 306.000.000 |
| UPS 650VA cho Edge | 1.200.000 | 34 | 40.800.000 |
| On-Premise Server 2U (Xeon, 64GB, 2×1TB SSD RAID-1, Redundant PSU) | 85.000.000 | 2 | 170.000.000 |
| Switch Managed 24-port GbE | 8.000.000 | 1 | 8.000.000 |
| Firewall NGFW (Fortinet FortiGate 60F hoặc tương đương) | 25.000.000 | 1 | 25.000.000 |
| Phụ kiện (Cáp, Rack mini HQ, patch panel) | 15.000.000 | 1 lot | 15.000.000 |
| **Tổng phần cứng** | | | **564.800.000** |

#### B. Dịch vụ triển khai & Nhân công

| Hạng mục | Chi tiết | Thành tiền (VNĐ) |
|:---|:---|---:|
| Thiết kế kiến trúc (HLD + LLD) | 2 kỹ sư × 3 tuần | 45.000.000 |
| Triển khai Cloud (K8s, Kafka, Airflow, DB, Storage, Monitoring) | 2 kỹ sư × 4 tuần | 60.000.000 |
| Triển khai 34 Edge Cluster (đóng Golden Image + deploy) | 2 kỹ sư × 4 tuần | 60.000.000 |
| Triển khai On-Prem Server HQ (Keycloak, PII DB, Firewall, VPN) | 1 kỹ sư × 2 tuần | 15.000.000 |
| Migrate dữ liệu lịch sử (8 hệ thống × 34 CN, ≥ 12 tháng) | 2 kỹ sư × 3 tuần | 45.000.000 |
| Tích hợp API (8 hệ thống POS/Gym/Bida/Kho → API Gateway + CDC) | 3 kỹ sư × 6 tuần | 135.000.000 |
| Phát triển mô hình AI dự báo (Train + Inference Service) | 2 ML (Machine Learning) Engineer × 6 tuần | 90.000.000 |
| Hardening & Security Audit | 1 kỹ sư × 2 tuần + Dịch vụ Pentest | 40.000.000 |
| Kiểm thử tích hợp & tải (Load Test, Failover Test, DR Drill) | 1 QA (Quality Assurance) × 3 tuần | 27.000.000 |
| Đào tạo & Chuyển giao (IT team + Admin chi nhánh, 5 buổi) | Trọn gói | 15.000.000 |
| Project Management (PM - Project Manager, 16 tuần) | 1 PM × 4 tháng | 100.000.000 |
| **Tổng dịch vụ triển khai** | | **632.000.000** |

#### C. Hạ tầng Cloud (giai đoạn triển khai — 4 tháng)

| Hạng mục | Đơn giá/tháng (VNĐ) | Số tháng | Thành tiền (VNĐ) |
|:---|---:|:---:|---:|
| K8s Cluster Development/Staging (3 nodes × 4vCPU, 16GB) | 12.000.000 | 4 | 48.000.000 |
| Managed PostgreSQL Dev (2vCPU, 8GB) | 2.500.000 | 4 | 10.000.000 |
| Managed Kafka Dev (3 brokers) | 5.000.000 | 4 | 20.000.000 |
| Object Storage (500 GB) | 500.000 | 4 | 2.000.000 |
| GPU Instance (huấn luyện AI, 2 tháng) | 12.000.000 | 2 | 24.000.000 |
| VPN + Bandwidth | 2.000.000 | 4 | 8.000.000 |
| **Tổng Cloud (triển khai)** | | | **112.000.000** |

#### Tổng CAPEX

| Nhóm | Thành tiền (VNĐ) |
|:---|---:|
| Phần cứng | 564.800.000 |
| Dịch vụ triển khai & Nhân công | 632.000.000 |
| Hạ tầng Cloud (4 tháng triển khai) | 112.000.000 |
| **TỔNG CAPEX** | **1.308.800.000** |

### 8.2. Chi phí vận hành định kỳ (OPEX) — Tính cho 12 tháng sau Go-live

| Hạng mục | Chi tiết | Đơn giá/tháng (VNĐ) | 12 tháng (VNĐ) |
|:---|:---|---:|---:|
| **Hạ tầng Cloud Production** | | | |
| K8s Cluster Production (6 nodes × 4vCPU, 16GB) | API Gateway, Kafka, Airflow, AI Inference | 24.000.000 | 288.000.000 |
| Managed PostgreSQL HA Production | Data Lakehouse + Forecast DB | 6.000.000 | 72.000.000 |
| Managed Kafka Production (3 brokers, HA) | CDC Streaming 34 chi nhánh | 8.000.000 | 96.000.000 |
| Object Storage (S3, tăng trưởng ~200 GB/năm) | Raw data + Model artifacts | 800.000 | 9.600.000 |
| GPU Instance (tái huấn luyện AI, 1 lần/tháng × 8h) | Spot Instance | 800.000 | 9.600.000 |
| VPN Site-to-Site + Bandwidth Cloud | Kết nối HQ ↔ Cloud | 2.000.000 | 24.000.000 |
| **Đường truyền chi nhánh** | | | |
| Internet 34 chi nhánh (nâng cấp băng thông cho CDC) | Bổ sung ~500.000/CN/tháng | 17.000.000 | 204.000.000 |
| **Nhân sự vận hành** | | | |
| DevOps/SRE (1 người full-time) | Giám sát, xử lý sự cố, patching, capacity | 22.000.000 | 264.000.000 |
| Data Engineer (part-time 30%) | Bảo trì pipeline, data quality, retrain AI | 6.600.000 | 79.200.000 |
| **Bảo mật & Tuân thủ** | | | |
| Firewall NGFW License renewal | Subscription hàng năm | — | 15.000.000 |
| Pentest (2 lần/năm) | Dịch vụ bên ngoài | — | 30.000.000 |
| SSL Certificate (Let's Encrypt) | Miễn phí | 0 | 0 |
| **Bảo trì phần cứng** | | | |
| Bảo trì On-Prem Server (HQ) | Hợp đồng bảo hành mở rộng | — | 15.000.000 |
| Thay thế Edge Server hỏng (dự phòng 5%) | ~2 bộ/năm | — | 17.000.000 |
| | | **Tổng OPEX / năm** | **1.123.400.000** |

### 8.3. Dự phòng rủi ro (Contingency)

| Hạng mục | Tỷ lệ | Thành tiền (VNĐ) |
|:---|:---:|---:|
| Dự phòng rủi ro kỹ thuật (CAPEX) | 10% × 1.308.800.000 | 130.880.000 |
| Dự phòng biến động giá Cloud/nhân sự (OPEX năm 1) | 10% × 1.123.400.000 | 112.340.000 |
| **Tổng dự phòng** | | **243.220.000** |

### 8.4. Tổng chi phí sở hữu (TCO) — Chu kỳ 3 năm

| Năm | CAPEX (VNĐ) | OPEX (VNĐ) | Contingency (VNĐ) | Tổng / năm (VNĐ) |
|:---:|---:|---:|---:|---:|
| **Năm 1** | 1.308.800.000 | 1.123.400.000 | 243.220.000 | 2.675.420.000 |
| **Năm 2** | 0 | 1.123.400.000 | 112.340.000 | 1.235.740.000 |
| **Năm 3** | 0 | 1.180.000.000 *(+5% tăng trưởng)* | 118.000.000 | 1.298.000.000 |
| **TCO 3 năm** | **1.308.800.000** | **3.426.800.000** | **473.560.000** | **5.209.160.000** |

$$\text{TCO}_{3 \text{ năm}} = \text{CAPEX} + \text{OPEX}_{3 \text{ năm}} + \text{Contingency} = 1.308.800.000 + 3.426.800.000 + 473.560.000 = \textbf{5.209.160.000 VNĐ}$$

### 8.5. Phân tích lợi ích quy đổi (Cost-Benefit)

| Lợi ích kỹ thuật | Quy đổi tài chính (ước tính / năm) | Cơ sở |
|:---|---:|:---|
| Giảm 2.500 giờ công báo cáo thủ công/năm | 125.000.000 | 50.000 VNĐ/giờ × 2.500 giờ |
| Giảm sai lệch doanh thu 3,8% → < 0,5% | 200.000.000 | Ước tính doanh thu chuỗi ~5,3 tỷ/năm; giảm thất thoát ~3,3% |
| Giảm downtime từ 4-8 giờ/sự cố → ≤ 30 phút MTTR | 150.000.000 | Giảm thiệt hại mất doanh thu giờ cao điểm |
| Tránh rủi ro phạt NĐ13 (lên đến 5% doanh thu) | — | Không lượng hoá, nhưng rủi ro rất lớn nếu bị kiểm tra |
| **Tổng lợi ích quy đổi / năm** | **~475.000.000** | |

> **Payback Period ước tính:** $\frac{\text{CAPEX}}{\text{Lợi ích/năm}} = \frac{1.308.800.000}{475.000.000} \approx$ **2,75 năm** — nằm trong chu kỳ TCO 3 năm.

### 8.6. So sánh TCO 3 năm giữa 3 kịch bản

| Hạng mục | On-Premise 100% | Cloud-Native 100% | Hybrid Cloud (Chọn) |
|:---|---:|---:|---:|
| CAPEX (phần cứng + triển khai) | ~2.800.000.000 | ~650.000.000 | ~1.308.800.000 |
| OPEX / năm | ~600.000.000 | ~1.800.000.000 | ~1.123.400.000 |
| TCO 3 năm | ~4.600.000.000 | ~6.050.000.000 | ~5.209.160.000 |
| Đáp ứng KPI Offline (99.99%) | ✓ | ✗ | ✓ |
| Đáp ứng KPI Tuân thủ NĐ13 | ✓ | ✗ | ✓ |
| Đáp ứng KPI Auto-scaling | ✗ | ✓ | ✓ |

> **Biện luận:** Hybrid Cloud có TCO trung bình nhưng là phương án duy nhất đáp ứng **100% tiêu chí kỹ thuật bắt buộc** (6/6 tiêu chí). On-Premise rẻ OPEX nhưng CAPEX quá cao và không co giãn. Cloud-Native rẻ CAPEX nhưng OPEX cao nhất và **không đáp ứng** yêu cầu offline + tuân thủ NĐ13.

# 9. Kế hoạch triển khai (Roadmap / WBS)

### 9.1. Roadmap 5 pha

Kế hoạch triển khai chia 5 pha, tổng thời gian **16 tuần (~4 tháng)**, giảm thiểu rủi ro thông qua triển khai có kiểm soát và Pilot trước khi rollout toàn bộ.

#### Pha 1: Foundation — Mạng, Bảo mật nền, Monitoring
- **Thời gian:** T1–T3 (3 tuần)
- **Phụ thuộc:** —
- **Deliverables (Sản phẩm bàn giao):**
  - VPN Site-to-Site HQ ↔ Cloud hoạt động
  - On-Prem Server HQ: Keycloak (SSO/IAM) + PII DB cài đặt & hardening
  - Firewall NGFW cấu hình rules
  - Prometheus + Grafana + Loki cài đặt trên Cloud
  - Centralized Logging (≥ 90 ngày)
  - CMDB khởi tạo
- **Tiêu chí hoàn thành:** VPN ping < 50ms; SSO login thành công cho 4 vai trò; Dashboard Monitoring hiển thị metrics; Firewall rules audit pass

#### Pha 2: Core — Compute, Storage, HA, Backup/DR
- **Thời gian:** T3–T6 (4 tuần)
- **Phụ thuộc:** Pha 1
- **Deliverables (Sản phẩm bàn giao):**
  - K8s Cluster Production (6 nodes, multi-zone)
  - Managed PostgreSQL HA + Managed Kafka HA
  - Object Storage (S3)
  - Backup immutable hàng ngày (retention 30 ngày)
  - PITR cho PostgreSQL (retention 7 ngày)
  - Edge Golden Image đóng gói (K3s + Kafka + LocalDB)
- **Tiêu chí hoàn thành:** K8s cluster: 2 zone failover ≤ 60s; Kafka replication factor = 3; Backup test restore thành công; Edge Golden Image boot thành công trên 1 máy test

#### Pha 3: Security Uplift — Tích hợp IAM, Mã hoá, CDC
- **Thời gian:** T6–T9 (4 tuần)
- **Phụ thuộc:** Pha 2
- **Deliverables (Sản phẩm bàn giao):**
  - **[Lớp 4]** Tích hợp SSO (Keycloak) vào 8 hệ thống POS/Gym/Bida/Kho
  - **[Lớp 3]** MFA cho tài khoản admin
  - **[Lớp 3]** Mã hoá AES-256 cho PII DB at-rest
  - **[Lớp 5]** CDC Streaming (Kafka Connect) từ 34 POS → Cloud
  - **[Lớp 3/5]** Ẩn danh hoá PII trước khi ghi Data Lakehouse
  - **[Lớp 4]** API Gateway cấu hình (rate limiting, JWT auth)
  - **[Lớp 5]** Data Pipeline Airflow DAGs (ETL)
- **Tiêu chí hoàn thành:** 100% app xác thực qua SSO; 100% trường PII mã hoá; CDC streaming 5.000 events/s stress test pass; API Gateway load test 2.000 concurrent pass; Pipeline ETL chạy end-to-end trên staging

#### Pha 4: Migration & AI — Migrate dữ liệu, Triển khai AI, Pilot
- **Thời gian:** T9–T13 (5 tuần)
- **Phụ thuộc:** Pha 3
- **Deliverables (Sản phẩm bàn giao):**
  - **[Lớp 5]** Migrate dữ liệu lịch sử 12 tháng (8 hệ thống → Data Lakehouse)
  - **[Lớp 5]** Huấn luyện mô hình AI dự báo lưu lượng
  - **[Lớp 5]** AI Inference Service (FastAPI) trên K8s
  - Triển khai 34 Edge Cluster (deploy Golden Image)
  - **Pilot 5 chi nhánh** (2 tuần vận hành thử)
  - Load Test toàn hệ thống
  - Pentest & Vulnerability Scan
  - UAT (User Acceptance Testing) với Admin chi nhánh
- **Tiêu chí hoàn thành:** Dữ liệu migrate: 100% toàn vẹn (row count match); AI MAPE < 15% trên tập test; Pilot 5 CN: uptime ≥ 99.99%, offline test pass (4h mất mạng); Pentest: 0 Critical/High; UAT sign-off

#### Pha 5: Optimize & Rollout — Rollout toàn bộ, SOP, Chuyển giao
- **Thời gian:** T13–T16 (4 tuần)
- **Phụ thuộc:** Pha 4
- **Deliverables (Sản phẩm bàn giao):**
  - Rollout 29 chi nhánh còn lại (đợt 10-10-9 CN)
  - Runbook/SOP vận hành (≥ 10 quy trình)
  - DR Drill lần 1
  - Đào tạo IT team (3 buổi) + Admin CN (2 buổi)
  - Bàn giao CMDB, tài liệu kiến trúc, tài khoản
  - Capacity Planning báo cáo quý 1
  - Fine-tune alerting thresholds
- **Tiêu chí hoàn thành:** Toàn bộ 34 CN hoạt động ổn định; DR Drill: RTO ≤ 4h; Đào tạo hoàn tất, biên bản bàn giao ký; CMDB liệt kê 100% tài sản; SOP thử nghiệm 3 kịch bản — pass

### 9.2. Mốc nghiệm thu (Milestones)

| Mốc | Thời điểm | Nội dung nghiệm thu |
|:---|:---|:---|
| **M1** | Cuối T3 | Foundation: VPN, IAM/SSO, Firewall, Monitoring hoạt động |
| **M2** | Cuối T6 | Core: K8s cluster HA, Kafka HA, Backup/DR, Edge Golden Image sẵn sàng |
| **M3** | Cuối T9 | Security Uplift: SSO tích hợp 8 hệ thống, CDC streaming, API Gateway, PII mã hoá 100% |
| **M4** | Cuối T13 | Migration & AI: Dữ liệu migrate xong, AI model đạt KPI, Pilot 5 CN thành công, Pentest pass, UAT sign-off |
| **M5** | Cuối T16 | Rollout toàn bộ 34 CN, DR Drill pass, Đào tạo & Chuyển giao hoàn tất — **GO-LIVE chính thức** |

### 9.3. Phân bổ chi phí CAPEX theo pha (Kiểm chứng tính nhất quán)

| Pha | Phần cứng (VNĐ) | Dịch vụ & Nhân công (VNĐ) | Cloud Dev (VNĐ) | Tổng (VNĐ) |
|:---|---:|---:|---:|---:|
| Pha 1: Foundation (T1–T3) | 218.000.000 | 75.000.000 | 18.000.000 | 311.000.000 |
| Pha 2: Core (T3–T6) | 0 | 60.000.000 | 36.000.000 | 96.000.000 |
| Pha 3: Security Uplift (T6–T9) | 0 | 180.000.000 | 28.000.000 | 208.000.000 |
| Pha 4: Migration & AI (T9–T13) | 346.800.000 | 257.000.000 | 24.000.000 | 627.800.000 |
| Pha 5: Optimize & Rollout (T13–T16) | 0 | 60.000.000 | 6.000.000 | 66.000.000 |
| **Tổng** | **564.800.000** | **632.000.000** | **112.000.000** | **1.308.800.000** |

> Tổng phân bổ theo pha (1.308.800.000 VNĐ) = Tổng CAPEX (1.308.800.000 VNĐ). ✓ **Khớp.**

# 10. Rủi ro & kế hoạch kiểm soát

| Rủi ro | Khả năng | Tác động | Biện pháp giảm thiểu |
|:---|:---:|:---:|:---|
| Chậm tích hợp API do 8 hệ thống POS đa dạng vendor | Cao | Cao | Pilot tích hợp 2 hệ thống phổ biến nhất trước (Pha 3); chuẩn bị adapter pattern cho các vendor khác |
| Edge Server lỗi phần cứng khi rollout hàng loạt | Trung bình | Trung bình | Dự phòng 2 bộ thay thế nóng; Golden Image cho phép deploy lại trong ≤ 30 phút |
| Mô hình AI không đạt MAPE < 15% trên dữ liệu thực | Trung bình | Cao | Thu thập đủ 12 tháng dữ liệu lịch sử; thử nghiệm 3 thuật toán (Prophet, LSTM, TSFM); rollback về Moving Average nếu chưa đạt |
| Nhân viên chi nhánh kháng cự thay đổi quy trình | Trung bình | Trung bình | Đào tạo sớm từ Pha 4 (Pilot); chọn 5 CN có quản lý tích cực làm Pilot; thu thập phản hồi và điều chỉnh UX |
| Chi phí Cloud vượt dự toán | Thấp | Trung bình | Contingency 10%; chuyển Reserved Instance (giảm 30–40%) nếu vượt; FinOps review hàng tháng |
| Lộ lọt dữ liệu (Data Breach) hoặc tấn công mạng | Trung bình | Cao | Áp dụng phân quyền Least Privilege; định kỳ quét lỗ hổng; mã hóa dữ liệu PII và giám sát hành vi tải dữ liệu bất thường. |

# 11. Tổ chức dự án & RACI

### 11.1. Ma trận phân nhiệm (RACI)
- **R (Responsible):** Người chịu trách nhiệm thực hiện.
- **A (Accountable):** Người chịu trách nhiệm giải trình (phê duyệt).
- **C (Consulted):** Người được tham vấn.
- **I (Informed):** Người được thông báo.

| Hạng mục công việc | Sponsor / Ban Giám đốc | Project Manager (PM) | Tech Leads (Infra/Data) | Vendor / Đội triển khai | Key Users (Admin CN) |
|:---|:---:|:---:|:---:|:---:|:---:|
| Phê duyệt dự án & ngân sách | A | R | C | - | I |
| Thiết kế kiến trúc (HLD/LLD) | I | A | R | R | - |
| Mua sắm phần cứng & thiết bị | A | R | C | - | I |
| Triển khai Cloud & On-Premise | I | A | R | R | - |
| Migrate dữ liệu & Tích hợp API| I | A | R | R | C |
| Xây dựng và kiểm thử mô hình AI | I | A | R | R | C |
| Đào tạo và Chuyển giao | I | A | C | R | R |
| Nghiệm thu hệ thống (Go-Live) | A | R | R | - | C |

### 11.2. Cơ chế phối hợp & Quản lý thay đổi
- **Lịch họp định kỳ:** Họp Ban chỉ đạo (Steering Committee) hàng tháng; Họp trạng thái dự án (Project Status) hàng tuần; Daily Standup cho đội kỹ thuật.
- **Quản lý Issue / Change Request (CR):** Mọi thay đổi về phạm vi, ngân sách hoặc thời gian phải lập ticket CR trên hệ thống ITSM (Jira), được Tech Lead đánh giá rủi ro và PM trình Sponsor phê duyệt trước khi thực thi.

# 12. Mua sắm / chọn nhà thầu

### 12.1. Hình thức mua sắm
- Do đặc thù yêu cầu tích hợp phức tạp và tính bảo mật cao, phương thức mua sắm là **Chào giá cạnh tranh (RFP - Request for Proposal)** mời tối thiểu 3 nhà thầu CNTT có kinh nghiệm triển khai Cloud và Big Data.

### 12.2. Tiêu chí đánh giá nhà thầu
- **Kỹ thuật (Trọng số 70%):** 
  - Năng lực và kinh nghiệm triển khai Hybrid Cloud (Kubernetes, Kafka).
  - Trình độ đội ngũ nhân sự (có chứng chỉ AWS/Azure/GCP, Kubernetes CKA).
  - Giải pháp đề xuất đáp ứng 100% yêu cầu kỹ thuật tại Bước 6.
- **Tài chính (Trọng số 30%):** Chi phí cạnh tranh, đảm bảo không vượt quá ngân sách CAPEX dự kiến.

### 12.3. Yêu cầu ràng buộc trong hợp đồng
- **Cam kết SLA (Service Level Agreement) & Phạt vi phạm:** Vendor phải cam kết SLA tích hợp và downtime tối đa trong thời gian Pilot. Phạt vi phạm hợp đồng nếu trễ tiến độ (ví dụ 1% giá trị hợp đồng/tuần trễ).
- **Cam kết bảo mật (NDA - Non-Disclosure Agreement):** Ký NDA chặt chẽ về việc bảo vệ dữ liệu PII theo Nghị định 13/2023/NĐ-CP. Không sao chép dữ liệu khách hàng ra khỏi môi trường Test/Prod của doanh nghiệp.
- **Bảo hành & Hỗ trợ kỹ thuật:** Hỗ trợ xử lý sự cố (L2/L3) trong tối thiểu 12 tháng sau Go-Live với cam kết thời gian phản hồi (Response Time) $\le$ 2 giờ.

# 13. Nghiệm thu – vận hành – chuyển giao

### 13.1. Nghiệm thu theo các lớp năng lực
- **Nghiệm thu Kỹ thuật (Performance & HA):** 
  - Chạy Load Test API Gateway đạt $\ge$ 2.000 concurrent users.
  - Ngắt kết nối mạng chi nhánh $\ge$ 4 giờ, kiểm tra khả năng tự hoạt động (offline mode) và đồng bộ lại 100% giao dịch khi có mạng (Store-and-Forward).
  - Diễn tập DR (DR Drill): Chuyển đổi hệ thống sang DR site với RTO $\le$ 4 giờ, khôi phục Database từ PITR với RPO $\le$ 15 phút.
- **Nghiệm thu Bảo mật:**
  - 100% kết nối được mã hóa TLS 1.2+.
  - Dữ liệu PII (CCCD, Face ID) trên On-Premise được mã hóa AES-256. Dữ liệu trên Cloud đã được ẩn danh.
  - Hệ thống vượt qua vòng rà quét lỗ hổng (Vulnerability Scan) không còn lỗi Critical/High.
- **Nghiệm thu Vận hành:**
  - Bảng điều khiển (Dashboard) Grafana hiển thị dữ liệu thời gian thực.
  - Hệ thống cảnh báo tự động gửi thông báo qua Slack/Email đúng thời gian (dưới 5 phút) khi mô phỏng sự cố tải cao.

### 13.2. Kế hoạch Chuyển giao (Handover)
- **Tài liệu bàn giao:** Tài liệu thiết kế kiến trúc chi tiết (LLD), Sơ đồ mạng, Tài liệu cấu hình mã nguồn (IaC/Terraform scripts).
- **Quy trình vận hành (SOP):** Bàn giao 10+ Runbook xử lý sự cố chuẩn, hướng dẫn cập nhật bản vá, quy trình onboarding chi nhánh mới.
- **Đào tạo:** 
  - 3 buổi đào tạo chuyên sâu cho đội ngũ IT nội bộ (vận hành K8s, Kafka, Airflow).
  - 2 buổi đào tạo sử dụng hệ thống mới cho Quản lý chi nhánh và Admin.
- **Quản lý tài sản (CMDB):** Cập nhật danh sách 34 Edge Server, 2 On-Prem Server, Cloud resources, phần mềm bản quyền vào hệ thống CMDB nội bộ.

# Phụ lục: Danh mục tài liệu tham khảo

[1] Scikit-Learn (n.d.), *Mean absolute percentage error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-percentage-error
[2] Atlassian ITSM (n.d.), *Incident Management Metrics (MTTD, MTTR)*, truy cập tại: https://www.atlassian.com/incident-management/kpis/common-metrics
[3] AWS (n.d.), *Disaster Recovery Objectives (RTO and RPO)*, truy cập tại: https://aws.amazon.com/disaster-recovery/
[4] Google Cloud (n.d.), *Site Reliability Engineering (SRE) - Availability Table and Metrics*, truy cập tại: https://sre.google/sre-book/availability-table/
[5] ISO/IEC (2008), *ISO/IEC 25012: Data quality model*, truy cập tại: https://www.iso.org/standard/35736.html
[6] NIST (2020), *SP 800-175B Rev. 1: Guideline for Using Cryptographic Standards in the Federal Government: Cryptographic Mechanisms*, truy cập tại: https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final
[7] CIS (2023), *CIS Benchmarks — Ubuntu Linux*, truy cập tại: https://www.cisecurity.org/benchmark/ubuntu_linux  
[8] Fortinet (n.d.), *FortiGate Next-Generation Firewall Datasheet*, truy cập tại: https://www.fortinet.com/products/next-generation-firewall  
[9] HashiCorp (n.d.), *Terraform Documentation*, truy cập tại: https://developer.hashicorp.com/terraform/docs  
[10] Ansible (n.d.), *Ansible Documentation*, truy cập tại: https://docs.ansible.com/  
[11] Keycloak (n.d.), *Keycloak — Open Source Identity and Access Management*, truy cập tại: https://www.keycloak.org/documentation  
[12] Apache Kafka (n.d.), *Kafka Documentation*, truy cập tại: https://kafka.apache.org/documentation/  
[13] Apache Airflow (n.d.), *Airflow Documentation*, truy cập tại: https://airflow.apache.org/docs/  
[14] Prometheus (n.d.), *Prometheus Monitoring Documentation*, truy cập tại: https://prometheus.io/docs/  
[15] Grafana (n.d.), *Grafana Documentation*, truy cập tại: https://grafana.com/docs/  
[16] PMI (2021), *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*, 7th Edition, Project Management Institute.
