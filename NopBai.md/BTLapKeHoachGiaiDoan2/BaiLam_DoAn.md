# Đồ Án Môn Học — Giai Đoạn 2 (Bước 5 – 8)
## Đề Xuất Đầu Tư Nền Tảng Tích Hợp Ứng Dụng & Nền Tảng Dữ Liệu Tập Trung Cho Chuỗi Ways Station

> **Tham chiếu Giai đoạn 1:** [BaiLam_DoAn.md (Bước 1–4)](../BTLapKeHoachGiaiDoan1/BaiLam_DoAn.md)

---

## Bước 5 — Chuẩn hoá yêu cầu kỹ thuật (Technical Requirements)

Yêu cầu kỹ thuật được chia thành 4 nhóm theo hướng dẫn Guide-Project, đủ chi tiết để chào thầu/mua sắm và làm cơ sở nghiệm thu. Mỗi yêu cầu được liên kết ngược (traceability) với KPI đã cam kết tại Bước 3.

### 5.1. Nhóm 1 — Hiệu năng & Dung lượng (Performance & Capacity)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-P01 | API Gateway xử lý đồng thời (concurrent connections) tại Cloud | ≥ 2.000 kết nối đồng thời (tính cho 34 chi nhánh × ~60 POS/thiết bị + đệm 20%) | KPI 1.1 — Uptime | Load test đạt 2.000 concurrent connections, error rate < 0.1% |
| TR-P02 | Thời gian phản hồi API (P95) cho giao dịch POS | ≤ 200 ms (round-trip từ Edge → Cloud → Edge) | KPI 1.1, 1.2 | Benchmark P95 ≤ 200 ms trên 10.000 requests liên tục |
| TR-P03 | Throughput Data Pipeline (CDC Streaming) | ≥ 5.000 events/giây (tổng 34 chi nhánh, giờ cao điểm) | KPI 2.1 — Data Freshness ≤ 5s | Stress test pipeline đạt throughput mục tiêu, không mất sự kiện |
| TR-P04 | Dung lượng Data Lakehouse (Cloud) | Tối thiểu 2 TB ban đầu, hỗ trợ mở rộng tự động lên 10 TB trong 3 năm | KPI 2.1 | Storage auto-scaling hoạt động khi đạt 80% capacity |
| TR-P05 | Sizing Edge Cluster mỗi chi nhánh | ≥ 4 vCPU, 8 GB RAM, 256 GB SSD — đủ chạy K3s + Kafka broker + Local DB cache | KPI 1.1 — Offline mode | Chi nhánh vận hành bình thường khi mất mạng ≥ 4 giờ |
| TR-P06 | Sizing Cloud Kubernetes Cluster | 6 nodes × (4 vCPU, 16 GB RAM) — chạy API Gateway, Kafka Cluster, Data Pipeline, AI Inference | KPI 1.1, 2.2 | Cluster hoạt động ổn định dưới tải 80% capacity |
| TR-P07 | Suy luận mô hình AI (Inference latency) | ≤ 500 ms / 1 request dự báo | KPI 2.2 — MAPE | Benchmark inference trên 1.000 requests liên tiếp |

### 5.2. Nhóm 2 — Độ sẵn sàng cao & Khôi phục thảm họa (HA / DR)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-H01 | Kubernetes Cloud: Multi-zone Active-Active | Tối thiểu 2 availability zones, tự động failover trong ≤ 60 giây | KPI 1.1 — 99.99% | Test failover: tắt 1 zone, hệ thống tự phục hồi ≤ 60s |
| TR-H02 | Kafka Cluster: Replication factor | ≥ 3 replicas cho mọi topic nghiệp vụ | KPI 2.1, 3.2 | Tắt 1 broker, không mất message, producer/consumer tiếp tục hoạt động |
| TR-H03 | Edge Cluster: Store-and-Forward khi offline | Queue cục bộ chứa tối thiểu 48 giờ giao dịch (~50.000 events/chi nhánh) | KPI 1.1 | Ngắt mạng 4 giờ, kiểm tra 100% events được đồng bộ bù khi có mạng |
| TR-H04 | Backup Data Lakehouse (Immutable backup) | Backup tự động hàng ngày, retention 30 ngày, RPO ≤ 15 phút | KPI 3.2 — RPO | Test restore từ backup: dữ liệu khôi phục đầy đủ, thời gian restore ≤ 2 giờ |
| TR-H05 | Backup PostgreSQL (Managed) | Point-in-time recovery (PITR), retention 7 ngày, RPO ≤ 15 phút | KPI 3.2 | Restore PITR đến thời điểm bất kỳ trong 7 ngày, kiểm tra tính toàn vẹn dữ liệu |
| TR-H06 | DR Drill (Diễn tập khôi phục thảm họa) | Thực hiện ≥ 2 lần/năm, RTO ≤ 4 giờ (toàn hệ thống) | KPI 1.2 | Biên bản diễn tập DR: hệ thống phục hồi hoàn toàn trong ≤ 4 giờ |

### 5.3. Nhóm 3 — Bảo mật & Danh tính (Security + Identity)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-S01 | IAM / SSO cho toàn hệ thống (Keycloak hoặc tương đương) | 100% ứng dụng nội bộ xác thực qua SSO, hỗ trợ OIDC/SAML | KPI 3.1 | Đăng nhập 1 lần truy cập toàn bộ ứng dụng; token hết hạn đúng policy |
| TR-S02 | MFA cho tài khoản đặc quyền (Admin, DevOps) | 100% tài khoản admin bắt buộc MFA (TOTP/WebAuthn) | KPI 3.1 | Kiểm tra: đăng nhập admin không có MFA bị từ chối |
| TR-S03 | Mã hoá PII at-rest (On-Premise) | AES-256 cho toàn bộ trường PII (CCCD, Face ID, SĐT) | KPI 3.1 — 100% | Audit: 100% trường PII trong DB được mã hoá, không có plaintext |
| TR-S04 | Mã hoá in-transit | TLS 1.2+ cho mọi kết nối (Edge ↔ Cloud, API Gateway, CDC) | KPI 3.1 | Scan SSL/TLS: không tồn tại kết nối không mã hoá |
| TR-S05 | Ẩn danh hoá dữ liệu trước khi đẩy lên Cloud | Loại bỏ/hash trường PII trước khi ghi vào Data Lakehouse | KPI 3.1 — NĐ13 | Kiểm tra mẫu dữ liệu trên Cloud: 0 bản ghi chứa PII dạng plaintext |
| TR-S06 | Log tập trung (Centralized Logging) | Lưu trữ ≥ 90 ngày, hỗ trợ tìm kiếm và cảnh báo bất thường | KPI 3.1 | Query log truy cập PII, log thay đổi cấu hình — kết quả trả về đúng |
| TR-S07 | Quét lỗ hổng bảo mật (Vulnerability Scan) | Quét tự động hàng tuần, 0 lỗ hổng Critical/High tồn tại quá 72 giờ | KPI 3.1 | Báo cáo scan: 0 Critical/High chưa vá |
| TR-S08 | Phân quyền RBAC theo nguyên tắc Least Privilege | Tối thiểu 4 vai trò: SuperAdmin, Admin chi nhánh, Nhân viên, Auditor | KPI 3.1 | Ma trận phân quyền được audit, tài khoản test không truy cập vượt quyền |

### 5.4. Nhóm 4 — Vận hành (Operations)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-O01 | Hệ thống Monitoring & Observability (Prometheus + Grafana) | Dashboard theo dõi: CPU/RAM/Disk/Network toàn cluster + API latency + Pipeline status | KPI 1.1, 1.2 | Demo dashboard: tất cả metrics hiển thị real-time, dữ liệu lịch sử 30 ngày |
| TR-O02 | Alerting & Escalation | Cảnh báo qua Slack/Email/SMS trong ≤ 5 phút khi metric vượt ngưỡng | KPI 1.2 — MTTR | Test: trigger cảnh báo CPU > 85%, thông báo đến đúng người trong ≤ 5 phút |
| TR-O03 | CMDB (Configuration Management Database) | Danh mục tài sản: 34 Edge devices + Cloud resources + License, cập nhật tự động | Quản trị tài sản | CMDB liệt kê 100% tài sản, thông tin chính xác so với thực tế |
| TR-O04 | Patching & Update tự động (IaC) | Terraform/Ansible quản lý toàn bộ cấu hình; rollback < 15 phút | KPI 1.2 | Thực hiện rollback cấu hình: hệ thống trở về trạng thái trước trong ≤ 15 phút |
| TR-O05 | Runbook / SOP vận hành | Tối thiểu 10 quy trình chuẩn: xử lý sự cố P1–P4, backup/restore, DR, patching, onboarding chi nhánh mới | KPI 1.2 | Tài liệu Runbook đầy đủ, thử nghiệm 3 kịch bản sự cố theo Runbook — thành công |
| TR-O06 | CI/CD Pipeline | Tự động: build → test → deploy lên Staging → approve → Production | KPI 1.1 | Demo CI/CD: commit code → deploy thành công lên Staging trong ≤ 15 phút |
| TR-O07 | Capacity Planning | Báo cáo dự báo tài nguyên hàng quý, cảnh báo khi sử dụng vượt 70% | Tối ưu chi phí | Báo cáo capacity quý đầu tiên sau Go-live có dữ liệu trending |

---

## Bước 6 — Lập danh mục hạng mục đầu tư (BOM / BoQ ở mức đề xuất)

Danh mục được tách rõ 4 nhóm: Thiết bị/Phần cứng, Phần mềm bản quyền, Dịch vụ triển khai, và Chi phí hạ tầng định kỳ.

### 6.1. Thiết bị / Phần cứng

| # | Hạng mục | Mô tả / Thông số giả định | Số lượng | Ghi chú |
|:---:|:---|:---|:---:|:---|
| 1 | Edge Mini Server (chi nhánh) | Intel NUC hoặc tương đương: 4 vCPU, 8 GB RAM, 256 GB NVMe SSD. Chạy K3s, Kafka broker, Local DB cache. | 34 bộ | 1 bộ/chi nhánh. Dự phòng 2 bộ thêm cho thay thế nóng → Tổng mua: 36 bộ |
| 2 | UPS cho Edge Server | UPS 650VA, thời gian giữ tải ≥ 15 phút | 34 bộ | Đảm bảo Edge không mất điện đột ngột → dữ liệu queue không hỏng |
| 3 | On-Premise Server (HQ — IAM + PII DB) | Rack Server 2U: 2× Xeon 8 cores, 64 GB ECC RAM, 2× 1TB SSD RAID-1, Redundant PSU | 2 bộ | Active-Passive cho HA. Đặt tại trụ sở chính (HQ) |
| 4 | Switch Managed (HQ) | Switch Layer 2 Managed, 24 ports GbE, VLAN support | 1 bộ | Phân tách VLAN: IAM Server / Management / Guest |
| 5 | Firewall Appliance (HQ) | Next-Gen Firewall: IPS/IDS, VPN site-to-site, 1 Gbps throughput | 1 bộ | Bảo vệ On-Premise IAM/PII, kết nối VPN tới Cloud |

### 6.2. Phần mềm bản quyền

| # | Hạng mục | Loại giấy phép | Số lượng | Ghi chú |
|:---:|:---|:---|:---:|:---|
| 1 | Kubernetes (K3s — Edge, K8s — Cloud) | Open-source (Apache 2.0) | — | Miễn phí |
| 2 | Apache Kafka | Open-source (Apache 2.0) | — | Miễn phí. Hoặc dùng Managed Kafka trên Cloud (tính vào OPEX) |
| 3 | Keycloak (IAM/SSO) | Open-source (Apache 2.0) | — | Miễn phí |
| 4 | PostgreSQL (Data Warehouse + PII DB) | Open-source (PostgreSQL License) | — | On-Prem: tự cài. Cloud: dùng Managed PostgreSQL (OPEX) |
| 5 | Apache Airflow (Data Pipeline orchestration) | Open-source (Apache 2.0) | — | Miễn phí |
| 6 | MLflow (Model Registry) | Open-source (Apache 2.0) | — | Miễn phí |
| 7 | Prometheus + Grafana + Loki (Monitoring stack) | Open-source (Apache 2.0 / AGPL) | — | Miễn phí |
| 8 | Terraform + Ansible (IaC) | Open-source (MPL 2.0 / GPL) | — | Miễn phí |
| 9 | OS cho On-Prem Server | Ubuntu Server 22.04 LTS | 2 licenses | Miễn phí (Community) |
| 10 | OS cho Edge Server | Ubuntu Server 22.04 LTS (minimal) | 36 licenses | Miễn phí |
| 11 | Firewall License (NGFW) | Subscription hãng (Fortinet/Palo Alto) | 1 license/năm | Tính vào OPEX |

> **Chiến lược bản quyền:** Ưu tiên tối đa phần mềm mã nguồn mở ổn định, cộng đồng lớn để giảm chi phí license — phù hợp với ngân sách doanh nghiệp vừa (SMB). Tuân thủ đầy đủ điều khoản giấy phép OSS (Chương 4, Slide 14).

### 6.3. Dịch vụ triển khai

| # | Hạng mục dịch vụ | Phạm vi | Ghi chú |
|:---:|:---|:---|:---|
| 1 | Thiết kế kiến trúc chi tiết (HLD + LLD) | Kiến trúc Cloud K8s, Edge K3s, Data Pipeline, IAM, Network topology | Bao gồm review & phê duyệt |
| 2 | Triển khai & Cấu hình hạ tầng Cloud | Dựng K8s cluster, Kafka, Airflow, PostgreSQL managed, Object Storage, VPN | IaC (Terraform) |
| 3 | Triển khai & Cấu hình 34 Edge Cluster | Cài đặt K3s, Kafka broker, Local DB cache, Store-and-Forward agent | Đóng Golden Image, deploy hàng loạt |
| 4 | Triển khai On-Premise Server (HQ) | Cài đặt Keycloak, PII Database, Firewall, VPN, hardening | Theo CIS Benchmark |
| 5 | Migrate dữ liệu | Di chuyển dữ liệu từ 8 hệ thống POS rời rạc → Data Lakehouse (lịch sử ≥ 12 tháng) | ETL scripts + kiểm tra toàn vẹn |
| 6 | Tích hợp hệ thống (API Integration) | Kết nối POS/Gym/Bida/Kho... vào API Gateway; CDC streaming setup | 8 hệ thống × 34 chi nhánh |
| 7 | Hardening & Security audit | Áp dụng CIS Benchmark, quét lỗ hổng, cấu hình WAF/IDS | Trước Go-live |
| 8 | Đào tạo & Chuyển giao | Đào tạo đội ngũ IT vận hành (3 buổi), đào tạo Admin chi nhánh (2 buổi), bàn giao Runbook | Bao gồm tài liệu |

### 6.4. Chi phí hạ tầng định kỳ (sẽ chi tiết hoá tại Bước 7)

| # | Hạng mục | Chu kỳ | Ghi chú |
|:---:|:---|:---|:---|
| 1 | Cloud Kubernetes Cluster (6 nodes) | Hàng tháng | Managed K8s |
| 2 | Managed PostgreSQL (HA) | Hàng tháng | Production DB |
| 3 | Managed Kafka (hoặc self-managed trên K8s) | Hàng tháng | Message streaming |
| 4 | Object Storage (S3) | Hàng tháng | Raw data + Model artifacts |
| 5 | GPU Instance (huấn luyện AI, 1 lần/tháng) | Hàng tháng | Spot/Preemptible |
| 6 | Đường truyền Internet chi nhánh (34 đường) | Hàng tháng | Bandwidth đảm bảo CDC streaming |
| 7 | VPN Site-to-Site (HQ ↔ Cloud) | Hàng tháng | Kết nối bảo mật |
| 8 | Firewall NGFW License renewal | Hàng năm | Subscription |
| 9 | Support & Bảo trì phần cứng On-Prem | Hàng năm | Bảo hành mở rộng |

---

## Bước 7 — Dự toán chi phí & Phân tích tài chính (CAPEX / OPEX + TCO)

### 7.1. Chi phí đầu tư ban đầu (CAPEX)

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
| Phát triển mô hình AI dự báo (Train + Inference Service) | 2 ML Engineer × 6 tuần | 90.000.000 |
| Hardening & Security Audit | 1 kỹ sư × 2 tuần + Dịch vụ Pentest | 40.000.000 |
| Kiểm thử tích hợp & tải (Load Test, Failover Test, DR Drill) | 1 QA × 3 tuần | 27.000.000 |
| Đào tạo & Chuyển giao (IT team + Admin chi nhánh, 5 buổi) | Trọn gói | 15.000.000 |
| Project Management (PM, 16 tuần) | 1 PM × 4 tháng | 100.000.000 |
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

### 7.2. Chi phí vận hành định kỳ (OPEX) — Tính cho 12 tháng sau Go-live

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

### 7.3. Dự phòng rủi ro (Contingency)

| Hạng mục | Tỷ lệ | Thành tiền (VNĐ) |
|:---|:---:|---:|
| Dự phòng rủi ro kỹ thuật (CAPEX) | 10% × 1.308.800.000 | 130.880.000 |
| Dự phòng biến động giá Cloud/nhân sự (OPEX năm 1) | 10% × 1.123.400.000 | 112.340.000 |
| **Tổng dự phòng** | | **243.220.000** |

### 7.4. Tổng chi phí sở hữu (TCO) — Chu kỳ 3 năm

| Năm | CAPEX (VNĐ) | OPEX (VNĐ) | Contingency (VNĐ) | Tổng / năm (VNĐ) |
|:---:|---:|---:|---:|---:|
| **Năm 1** | 1.308.800.000 | 1.123.400.000 | 243.220.000 | 2.675.420.000 |
| **Năm 2** | 0 | 1.123.400.000 | 112.340.000 | 1.235.740.000 |
| **Năm 3** | 0 | 1.180.000.000 *(+5% tăng trưởng)* | 118.000.000 | 1.298.000.000 |
| **TCO 3 năm** | **1.308.800.000** | **3.426.800.000** | **473.560.000** | **5.209.160.000** |

$$\text{TCO}_{3 \text{ năm}} = \text{CAPEX} + \text{OPEX}_{3 \text{ năm}} + \text{Contingency} = 1.308.800.000 + 3.426.800.000 + 473.560.000 = \textbf{5.209.160.000 VNĐ}$$

### 7.5. Phân tích lợi ích quy đổi (Cost-Benefit)

| Lợi ích kỹ thuật | Quy đổi tài chính (ước tính / năm) | Cơ sở |
|:---|---:|:---|
| Giảm 2.500 giờ công báo cáo thủ công/năm | 125.000.000 | 50.000 VNĐ/giờ × 2.500 giờ |
| Giảm sai lệch doanh thu 3,8% → < 0,5% | 200.000.000 | Ước tính doanh thu chuỗi ~5,3 tỷ/năm; giảm thất thoát ~3,3% |
| Giảm downtime từ 4-8 giờ/sự cố → ≤ 30 phút MTTR | 150.000.000 | Giảm thiệt hại mất doanh thu giờ cao điểm |
| Tránh rủi ro phạt NĐ13 (lên đến 5% doanh thu) | — | Không lượng hoá, nhưng rủi ro rất lớn nếu bị kiểm tra |
| **Tổng lợi ích quy đổi / năm** | **~475.000.000** | |

> **Payback Period ước tính:** $\frac{\text{CAPEX}}{\text{Lợi ích/năm}} = \frac{1.308.800.000}{475.000.000} \approx$ **2,75 năm** — nằm trong chu kỳ TCO 3 năm.

### 7.6. So sánh TCO 3 năm giữa 3 kịch bản

| Hạng mục | On-Premise 100% | Cloud-Native 100% | Hybrid Cloud (Chọn) |
|:---|---:|---:|---:|
| CAPEX (phần cứng + triển khai) | ~2.800.000.000 | ~650.000.000 | ~1.308.800.000 |
| OPEX / năm | ~600.000.000 | ~1.800.000.000 | ~1.123.400.000 |
| TCO 3 năm | ~4.600.000.000 | ~6.050.000.000 | ~5.209.160.000 |
| Đáp ứng KPI Offline (99.99%) | ✓ | ✗ | ✓ |
| Đáp ứng KPI Tuân thủ NĐ13 | ✓ | ✗ | ✓ |
| Đáp ứng KPI Auto-scaling | ✗ | ✓ | ✓ |

> **Biện luận:** Hybrid Cloud có TCO trung bình nhưng là phương án duy nhất đáp ứng **100% tiêu chí kỹ thuật bắt buộc** (6/6 tiêu chí — Bước 4). On-Premise rẻ OPEX nhưng CAPEX quá cao và không co giãn. Cloud-Native rẻ CAPEX nhưng OPEX cao nhất và **không đáp ứng** yêu cầu offline + tuân thủ NĐ13.

---

## Bước 8 — Kế hoạch triển khai theo giai đoạn (Roadmap)

### 8.1. Roadmap 5 pha

Kế hoạch triển khai chia 5 pha, tổng thời gian **16 tuần (~4 tháng)**, giảm thiểu rủi ro thông qua triển khai có kiểm soát và Pilot trước khi rollout toàn bộ.

| Pha | Tên pha | Tuần | Thời lượng | Deliverables (Sản phẩm bàn giao) | Tiêu chí hoàn thành | Phụ thuộc |
|:---:|:---|:---:|:---:|:---|:---|:---:|
| **1** | **Foundation** — Mạng, Bảo mật nền, Monitoring | T1–T3 | 3 tuần | • VPN Site-to-Site HQ ↔ Cloud hoạt động • On-Prem Server HQ: Keycloak (SSO/IAM) + PII DB cài đặt & hardening • Firewall NGFW cấu hình rules • Prometheus + Grafana + Loki cài đặt trên Cloud • Centralized Logging (≥ 90 ngày) • CMDB khởi tạo | VPN ping < 50ms; SSO login thành công cho 4 vai trò; Dashboard Monitoring hiển thị metrics; Firewall rules audit pass | — |
| **2** | **Core** — Compute, Storage, HA, Backup/DR | T3–T6 | 4 tuần | • K8s Cluster Production (6 nodes, multi-zone) • Managed PostgreSQL HA + Managed Kafka HA • Object Storage (S3) • Backup immutable hàng ngày (retention 30 ngày) • PITR cho PostgreSQL (retention 7 ngày) • Edge Golden Image đóng gói (K3s + Kafka + LocalDB) | K8s cluster: 2 zone failover ≤ 60s; Kafka replication factor = 3; Backup test restore thành công; Edge Golden Image boot thành công trên 1 máy test | Pha 1 |
| **3** | **Security Uplift** — Tích hợp IAM, Mã hoá, CDC | T6–T9 | 4 tuần | • Tích hợp SSO (Keycloak) vào 8 hệ thống POS/Gym/Bida/Kho • MFA cho tài khoản admin • Mã hoá AES-256 cho PII DB at-rest • CDC Streaming (Kafka Connect) từ 34 POS → Cloud • Ẩn danh hoá PII trước khi ghi Data Lakehouse • API Gateway cấu hình (rate limiting, JWT auth) • Data Pipeline Airflow DAGs (ETL) | 100% app xác thực qua SSO; 100% trường PII mã hoá; CDC streaming 5.000 events/s stress test pass; API Gateway load test 2.000 concurrent pass; Pipeline ETL chạy end-to-end trên staging | Pha 2 |
| **4** | **Migration & AI** — Migrate dữ liệu, Triển khai AI, Pilot | T9–T13 | 5 tuần | • Migrate dữ liệu lịch sử 12 tháng (8 hệ thống → Data Lakehouse) • Huấn luyện mô hình AI dự báo lưu lượng • AI Inference Service (FastAPI) trên K8s • Triển khai 34 Edge Cluster (deploy Golden Image) • **Pilot 5 chi nhánh** (2 tuần vận hành thử) • Load Test toàn hệ thống • Pentest & Vulnerability Scan • UAT với Admin chi nhánh | Dữ liệu migrate: 100% toàn vẹn (row count match); AI MAPE < 15% trên tập test; Pilot 5 CN: uptime ≥ 99.99%, offline test pass (4h mất mạng); Pentest: 0 Critical/High; UAT sign-off | Pha 3 |
| **5** | **Optimize & Rollout** — Rollout toàn bộ, SOP, Chuyển giao | T13–T16 | 4 tuần | • Rollout 29 chi nhánh còn lại (đợt 10-10-9 CN) • Runbook/SOP vận hành (≥ 10 quy trình) • DR Drill lần 1 • Đào tạo IT team (3 buổi) + Admin CN (2 buổi) • Bàn giao CMDB, tài liệu kiến trúc, tài khoản • Capacity Planning báo cáo quý 1 • Fine-tune alerting thresholds | Toàn bộ 34 CN hoạt động ổn định; DR Drill: RTO ≤ 4h; Đào tạo hoàn tất, biên bản bàn giao ký; CMDB liệt kê 100% tài sản; SOP thử nghiệm 3 kịch bản — pass | Pha 4 |

### 8.2. Mốc nghiệm thu (Milestones)

| Mốc | Thời điểm | Nội dung nghiệm thu |
|:---|:---|:---|
| **M1** | Cuối T3 | Foundation: VPN, IAM/SSO, Firewall, Monitoring hoạt động |
| **M2** | Cuối T6 | Core: K8s cluster HA, Kafka HA, Backup/DR, Edge Golden Image sẵn sàng |
| **M3** | Cuối T9 | Security Uplift: SSO tích hợp 8 hệ thống, CDC streaming, API Gateway, PII mã hoá 100% |
| **M4** | Cuối T13 | Migration & AI: Dữ liệu migrate xong, AI model đạt KPI, Pilot 5 CN thành công, Pentest pass, UAT sign-off |
| **M5** | Cuối T16 | Rollout toàn bộ 34 CN, DR Drill pass, Đào tạo & Chuyển giao hoàn tất — **GO-LIVE chính thức** |

### 8.3. Phân bổ chi phí CAPEX theo pha (Kiểm chứng tính nhất quán)

| Pha | Phần cứng (VNĐ) | Dịch vụ & Nhân công (VNĐ) | Cloud Dev (VNĐ) | Tổng (VNĐ) |
|:---|---:|---:|---:|---:|
| Pha 1: Foundation (T1–T3) | 218.000.000 | 75.000.000 | 18.000.000 | 311.000.000 |
| Pha 2: Core (T3–T6) | 0 | 60.000.000 | 36.000.000 | 96.000.000 |
| Pha 3: Security Uplift (T6–T9) | 0 | 180.000.000 | 28.000.000 | 208.000.000 |
| Pha 4: Migration & AI (T9–T13) | 346.800.000 | 257.000.000 | 24.000.000 | 627.800.000 |
| Pha 5: Optimize & Rollout (T13–T16) | 0 | 60.000.000 | 6.000.000 | 66.000.000 |
| **Tổng** | **564.800.000** | **632.000.000** | **112.000.000** | **1.308.800.000** |

> Tổng phân bổ theo pha (1.308.800.000 VNĐ) = Tổng CAPEX (1.308.800.000 VNĐ). ✓ **Khớp.**

### 8.4. Quản trị rủi ro triển khai (Risk Highlights)

| Rủi ro | Khả năng | Tác động | Biện pháp giảm thiểu |
|:---|:---:|:---:|:---|
| Chậm tích hợp API do 8 hệ thống POS đa dạng vendor | Cao | Cao | Pilot tích hợp 2 hệ thống phổ biến nhất trước (Pha 3); chuẩn bị adapter pattern cho các vendor khác |
| Edge Server lỗi phần cứng khi rollout hàng loạt | Trung bình | Trung bình | Dự phòng 2 bộ thay thế nóng; Golden Image cho phép deploy lại trong ≤ 30 phút |
| Mô hình AI không đạt MAPE < 15% trên dữ liệu thực | Trung bình | Cao | Thu thập đủ 12 tháng dữ liệu lịch sử; thử nghiệm 3 thuật toán (Prophet, LSTM, TSFM); rollback về Moving Average nếu chưa đạt |
| Nhân viên chi nhánh kháng cự thay đổi quy trình | Trung bình | Trung bình | Đào tạo sớm từ Pha 4 (Pilot); chọn 5 CN có quản lý tích cực làm Pilot; thu thập phản hồi và điều chỉnh UX |
| Chi phí Cloud vượt dự toán | Thấp | Trung bình | Contingency 10%; chuyển Reserved Instance (giảm 30–40%) nếu vượt; FinOps review hàng tháng |

---

## Danh mục tài liệu tham khảo bổ sung (Giai đoạn 2)

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
