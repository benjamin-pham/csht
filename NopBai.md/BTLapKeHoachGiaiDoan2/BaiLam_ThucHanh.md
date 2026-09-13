# Bài Thực Hành — Giai Đoạn 2 (Bước 5 – 9)
## Ứng Dụng Mô Hình AI Dự Báo Lưu Lượng Khách Hàng Dành Cho Chuỗi Ways Station

> **Tham chiếu Giai đoạn 1:** [BaiLam_ThucHanh.md (Bước 0–4)](../BTLapKeHoachGiaiDoan1/BaiLam_ThucHanh.md)

---

## Bước 5 — Yêu cầu nghiệp vụ và yêu cầu hệ thống

### 5.1. Yêu cầu nghiệp vụ (Business Requirements / Use Case level)

Yêu cầu nghiệp vụ được trình bày theo use case/user story, bám sát phạm vi luồng tích hợp dữ liệu POS → Cloud → Mô hình AI → RESTful API.

| ID | Tên nghiệp vụ (User Story) | Tác nhân | Luồng chính (Main Flow) | Ngoại lệ (Exception Flow) | Đầu ra / Kết quả |
|:---|:---|:---|:---|:---|:---|
| BR-01 | Xem dự báo lưu lượng khách | Quản lý chi nhánh | 1. Đăng nhập hệ thống <br>2. Chọn chi nhánh & khoảng thời gian <br>3. Hệ thống query API trả về dữ liệu dự báo | API lỗi hoặc chưa có dự báo mới $\rightarrow$ Báo lỗi & hiển thị dữ liệu lịch sử của tuần trước. | Bảng/Biểu đồ dự báo khách theo giờ (JSON). |
| BR-02 | Nhận cảnh báo giờ cao điểm | Bộ phận điều phối | 1. Hệ thống phân tích kết quả dự báo <br>2. Nếu lượng khách $> 1.5 \times$ trung bình $\rightarrow$ Tự động gửi cảnh báo. | Gửi email/webhook thất bại $\rightarrow$ Đẩy noti trực tiếp trên App/Dashboard nội bộ. | Thông báo cảnh báo (webhook/email). |
| BR-03 | Tự động Pipeline dữ liệu | Hệ thống (Cronjob) | 1. Kết nối POS DB (01:00 AM) <br>2. Trích xuất batch <br>3. Làm sạch, chuẩn hóa <br>4. Nạp vào Data Warehouse | Rớt kết nối mạng tới POS $\rightarrow$ Retry 3 lần, nếu thất bại Alert cho Kỹ sư dữ liệu. | Dataset chuẩn hóa lưu tại Data Warehouse. |
| BR-04 | Giám sát trạng thái hệ thống | Kỹ sư vận hành | 1. Truy cập Grafana <br>2. Xem dashboard metrics (Pipeline, API, Model, Resource) | Mất kết nối tới Prometheus $\rightarrow$ Bật cảnh báo khẩn qua PagerDuty/Slack. | Dashboard giám sát real-time (Uptime, MAPE). |

### 5.2. Yêu cầu chức năng (Functional Requirements)

Nhóm theo 3 module chính tương ứng với 3 tầng kỹ thuật của hệ thống:

**Module 1: Data Pipeline (Thu thập & Xử lý dữ liệu)**
| ID | Yêu cầu chức năng | Mô tả |
|:---|:---|:---|
| FR-01 | Trích xuất dữ liệu POS tự động | Kết nối database POS tại 34 chi nhánh qua kênh mã hóa TLS, trích xuất giao dịch theo lịch batch hàng đêm (01:00 AM). |
| FR-02 | Làm sạch và chuẩn hóa dữ liệu | Xử lý giá trị khuyết (missing values), loại bỏ bản ghi trùng lặp, chuẩn hóa schema thống nhất giữa các chi nhánh. |
| FR-03 | Nạp dữ liệu vào Data Warehouse | Ghi dữ liệu đã làm sạch vào bảng staging, sau đó chuyển vào bảng chính (production tables) theo quy trình ELT. |
| FR-04 | Ghi log trạng thái pipeline | Ghi nhận số bản ghi đầu vào/đầu ra, tỷ lệ thành công, thời gian thực thi mỗi lần chạy batch. |

**Module 2: AI Forecasting Engine (Mô hình dự báo)**
| ID | Yêu cầu chức năng | Mô tả |
|:---|:---|:---|
| FR-05 | Huấn luyện mô hình chuỗi thời gian | Sử dụng dữ liệu lịch sử tối thiểu 12 tháng để huấn luyện mô hình Time-Series Forecasting (TSFM). Hỗ trợ tái huấn luyện định kỳ hàng tháng. |
| FR-06 | Dự báo lưu lượng khách | Xuất kết quả dự báo lưu lượng khách theo từng khung giờ (1 giờ/slot), cho từng chi nhánh, trong 7 ngày tới. |
| FR-07 | Nhận diện khung giờ cao điểm | Tự động gán nhãn "peak" cho các khung giờ có dự báo vượt ngưỡng $1.5 \times$ lưu lượng trung bình của chi nhánh đó. |
| FR-08 | Quản lý phiên bản mô hình | Lưu trữ artifact mô hình theo phiên bản (Model Registry), hỗ trợ rollback về phiên bản trước khi mô hình mới cho kết quả kém hơn. |

**Module 3: API Service & Dashboard (Phân phối kết quả)**
| ID | Yêu cầu chức năng | Mô tả |
|:---|:---|:---|
| FR-09 | RESTful API dự báo real-time | Endpoint `GET /api/v1/forecast/{branch_id}` trả kết quả dự báo 7 ngày dưới dạng JSON. Hỗ trợ filter theo ngày và khung giờ. |
| FR-10 | RESTful API cảnh báo giờ cao điểm | Endpoint `GET /api/v1/alerts/{branch_id}` trả danh sách khung giờ đột biến kèm mức độ tin cậy (confidence score). |
| FR-11 | Dashboard giám sát hệ thống | Hiển thị metrics pipeline (thời gian chạy, tỷ lệ thành công), metrics API (latency P95, error rate) và metrics mô hình (MAPE, MAE). |
| FR-12 | Xác thực và phân quyền API | Áp dụng xác thực API Key/JWT cho mọi endpoint. Phân quyền theo vai trò (RBAC). |

### 5.3. Yêu cầu phi chức năng (Non-Functional Requirements)

Các yêu cầu phi chức năng được thiết lập khớp trực tiếp với bộ KPI đã cam kết tại Bước 3:

| Nhóm NFR | Yêu cầu | Ngưỡng đo lường (Tiêu chí Test) | KPI liên kết (Bước 3) |
|:---|:---|:---|:---|
| **Hiệu năng** | Thời gian phản hồi API dự báo (P95) | ≤ 500 ms / request | KPI B.1 — API Response Time |
| **Hiệu năng** | Thời gian suy luận mô hình AI | ≤ 200 ms / chi nhánh | KPI A.4 — Inference Latency |
| **Hiệu năng** | Thời gian xử lý Batch Job (34 chi nhánh) | ≤ 30 phút | KPI B.1 — Batch Processing |
| **Sẵn sàng** | Uptime dịch vụ API | ≥ 99.9% (downtime ≤ 43.2 phút/tháng) | KPI B.2 — Availability |
| **Sẵn sàng** | Thời gian phát hiện sự cố (MTTD) | ≤ 15 phút | KPI B (Bảng 3.3 — G5) |
| **Dữ liệu** | Tính đầy đủ bản ghi pipeline | ≥ 99.5% | KPI B.3 — Completeness |
| **Dữ liệu** | Độ trễ đồng bộ dữ liệu (Data Freshness) | ≤ 24 giờ | KPI B.3 — Freshness |
| **Bảo mật** | Mã hóa kết nối trích xuất dữ liệu | Bắt buộc giao thức TLS 1.2+ | Ràng buộc Bước 0 |
| **Bảo mật** | Xác thực API | Bắt buộc API Key / JWT | FR-12 |
| **Mở rộng** | Hỗ trợ scale số lượng chi nhánh | Thêm lên 50 CN không cần đổi kiến trúc | Giả định Bước 4 |
| **Tuân thủ** | Bảo mật thông tin cá nhân (PII) | Dữ liệu giao dịch được ẩn danh 100% | Ràng buộc NĐ13 |

### 5.4. Ma trận phân quyền (RBAC)

| Vai trò (Role) | Xem dự báo chi nhánh mình | Xem dự báo toàn hệ thống | Xem Dashboard giám sát | Cấu hình ngưỡng cảnh báo | Quản lý mô hình AI | Quản lý Pipeline |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Quản lý chi nhánh | ✓ | — | — | — | — | — |
| Quản lý trung tâm | ✓ | ✓ | ✓ | ✓ | — | — |
| Kỹ sư AI (ML Engineer) | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Kỹ sư Dữ liệu (DE) | — | — | ✓ | — | — | ✓ |
| Kỹ sư DevOps/SRE | — | — | ✓ | ✓ | — | ✓ |

---

## Bước 6 — Thiết kế giải pháp (TO-BE) và kiến trúc tổng thể

### 6.1. Quy trình nghiệp vụ TO-BE
Quy trình vận hành có sự tham gia của AI đóng vai trò hệ thống hỗ trợ ra quyết định (DSS). Luồng công việc:
1. **Thu thập (24/7):** Khách hàng giao dịch tại hệ thống POS của chi nhánh.
2. **Đồng bộ & Xử lý (01:00 AM mỗi ngày):** Pipeline tự động rút dữ liệu từ POS về kho dữ liệu Cloud trung tâm, tiến hành làm sạch, loại bỏ lỗi.
3. **Dự báo (02:00 AM):** AI Engine chạy Batch Inference cho 34 chi nhánh dựa trên dữ liệu mới nhất, lưu trữ kết quả.
4. **Cảnh báo (Tự động):** Alert Service quét kết quả dự báo. Nếu phát hiện khung giờ vượt tải ($>150\%$ lưu lượng trung bình), tự động push Webhook/Email cho bộ phận quản lý.
5. **Ra quyết định (08:00 AM - Điểm kiểm soát):** Quản lý chi nhánh truy cập phần mềm nội bộ (gọi API dự báo), tham khảo kết quả để duyệt lịch phân ca nhân viên và chuẩn bị kho bãi. **Con người chốt quyết định cuối cùng**.

### 6.2. Kiến trúc hệ thống tổng thể (3 tầng)

Kiến trúc được thiết kế trên nền tảng Cloud, chia thành 3 lớp rõ ràng:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TẦNG TRÌNH BÀY (Presentation Layer)                 │
│                                                                         │
│   ┌──────────────┐   ┌──────────────┐   ┌────────────────────────┐     │
│   │  Web Dashboard│   │ Grafana      │   │ Webhook / Email Alert │     │
│   │  (Dành cho QL)│   │ (Giám sát IT)│   │ (Cảnh báo tự động)   │     │
│   └──────┬───────┘   └──────┬───────┘   └────────────┬───────────┘     │
│          │                  │                        │                   │
├──────────┴──────────────────┴────────────────────────┴───────────────────┤
│                    TẦNG ỨNG DỤNG (Application Layer)                    │
│                                                                         │
│   ┌────────────────────────────────────────────────────────────────┐    │
│   │              API Gateway (Xác thực JWT + Rate Limiting)        │    │
│   └──────────────────────────┬─────────────────────────────────────┘    │
│                              │                                          │
│   ┌──────────────┐   ┌──────┴───────┐   ┌──────────────────────┐       │
│   │ Forecast     │   │ Alert        │   │ Pipeline             │       │
│   │ Service      │   │ Service      │   │ Orchestrator         │       │
│   │ (FastAPI)    │   │ (FastAPI)    │   │ (Apache Airflow)     │       │
│   └──────┬───────┘   └──────┬───────┘   └──────────┬───────────┘       │
│          │                  │                       │                    │
├──────────┴──────────────────┴───────────────────────┴────────────────────┤
│                    TẦNG DỮ LIỆU (Data Layer)                            │
│                                                                         │
│   ┌──────────────┐   ┌──────────────┐   ┌──────────────────────┐       │
│   │ Data         │   │ Model        │   │ Prometheus +         │       │
│   │ Warehouse    │   │ Registry     │   │ Loki (Metrics/Logs)  │       │
│   │ (PostgreSQL) │   │ (MLflow)     │   │                      │       │
│   └──────────────┘   └──────────────┘   └──────────────────────┘       │
│                                                                         │
│   ┌────────────────────────────────────────────────────────────────┐    │
│   │          Object Storage (S3) — Raw Data + Model Artifacts      │    │
│   └────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.3. Luồng xử lý Data Pipeline

```
POS DB (34 chi nhánh)
    │
    │ [01:00 AM] Trích xuất batch qua kết nối TLS
    ▼
Airflow DAG: Extract  ──► Object Storage (S3) — Raw Zone
    │
    ▼
Airflow DAG: Transform (Làm sạch, chuẩn hóa, loại trùng)
    │
    ▼
Data Warehouse (PostgreSQL) — Clean Zone
    │
    ├──► Airflow DAG: Train (Tái huấn luyện mô hình hàng tháng) ──► MLflow Registry
    │
    └──► Airflow DAG: Predict (Chạy dự báo batch hàng đêm) ──► Bảng Kết Quả Dự Báo
```

### 6.4. Tích hợp hệ thống

| Hệ thống Nguồn / Đích | Giao thức | Tần suất | Dữ liệu trao đổi (Mapping) | Bảo mật |
|:---|:---|:---|:---|:---|
| POS DB $\rightarrow$ S3 | JDBC/ODBC qua TLS | Batch 1 lần/đêm | Giao dịch ẩn danh (lượng khách, thời gian, mã chi nhánh) | Mã hóa in-transit |
| S3 $\rightarrow$ Data Warehouse | Internal VPC | Theo luồng Extract | Dataset đã chuẩn hóa | Mã hóa at-rest (AES-256) |
| Forecast API $\rightarrow$ ERP | RESTful (HTTPS) | On-demand | JSON chứa array lượng khách dự báo theo slot giờ | JWT + RBAC |
| Prometheus $\rightarrow$ Grafana | Internal scrape | 15 giây/lần | Metrics hệ thống IT (Uptime, API Latency) | Nội bộ mạng ảo VPC |

### 6.5. Thiết kế dữ liệu (ERD High-level)

| Thực thể | Thuộc tính chính | Mô tả |
|:---|:---|:---|
| **Branch** | `branch_id` (PK), `branch_name`, `branch_type`, `region` | Danh mục chi nhánh (Master Data) |
| **Transaction_Hourly** | `id` (PK), `branch_id` (FK), `date`, `hour_slot`, `customer_count` | Dữ liệu lượng khách thực tế tổng hợp theo giờ |
| **Forecast_Result** | `id` (PK), `branch_id` (FK), `forecast_date`, `hour_slot`, `predicted_count`, `is_peak` | Kết quả xuất ra từ mô hình dự báo AI |
| **Model_Metadata** | `model_id` (PK), `version`, `mape_score`, `mae_score`, `status` | Thông tin lịch sử độ chính xác mô hình |

**Quy tắc chuẩn hóa / Mã hóa danh mục:**
- Khóa định danh chi nhánh: `WS-{TYPE}-{NNN}` (VD: `WS-GYM-001`).
- Khóa thời gian (Hour slot): Số nguyên 0–23 định dạng chu kỳ 24h.

---

## Bước 7 — Kế hoạch triển khai (WBS) và tiến độ

Chia theo 5 pha chuẩn mực. Kế hoạch triển khai khớp trực tiếp với bảng ánh xạ KPI theo giai đoạn đã định nghĩa tại Bước 3.3 (Bảng G1–G5):

| Pha / Giai đoạn | Tuần | Hoạt động chính | Sản phẩm đầu ra (Deliverables) | Tiêu chí hoàn thành (Nghiệm thu) | Người chịu trách nhiệm (Owner) |
|:---|:---:|:---|:---|:---|:---|
| **1. Khảo sát & Phân tích (SRS/BRD)** | T1–T3 | Thu thập dữ liệu POS lịch sử $\ge$ 12 tháng; Phân tích chất lượng dữ liệu; Làm sạch missing/duplicate. | Tài liệu đặc tả dữ liệu (Data Dictionary); Dataset sạch. | Completeness $\ge$ 99.5%; Schema hợp lệ 100%. | Kỹ sư Dữ liệu (Data Engineer) |
| **2. Thiết kế (HLD/LLD)** | T4–T5 | Thiết kế Data Pipeline; Thiết kế API Contract (OpenAPI); Thiết kế ERD; Thiết kế hạ tầng Cloud. | HLD/LLD; API Contract; ERD; Terraform scripts. | Kiến trúc được Sponsor và Key User duyệt 100%. | Kiến trúc sư / Backend Lead |
| **3. Phát triển (Dev)** | T6–T10 | Code Airflow DAGs (ETL); Huấn luyện mô hình TSFM; Code API Services (FastAPI); Tích hợp MLflow. | Source code Pipeline & API; Artifact AI Model. | $\text{MAPE} < 10\%$; $\text{Precision} \ge 85\%$. | Kỹ sư AI (ML Engineer) |
| **4. Kiểm thử (SIT/UAT)** | T11–T13 | Test tích hợp; Test tải (100 CCU); Test bảo mật; Đóng gói Docker; Hỗ trợ UAT. | Kịch bản test; Báo cáo SIT; Biên bản UAT (Sign-off). | API P95 $\le$ 500ms; Error Rate $<$ 0.1%; Pass UAT. | Kỹ sư Kiểm thử (QA) |
| **5. Triển khai & Vận hành (Rollout/Ops)** | T14–T15 | Triển khai Kubernetes; Cấu hình Grafana/Prometheus; Pilot 5 chi nhánh $\rightarrow$ Rollout 34 chi nhánh. | Hệ thống Live; Dashboard giám sát; Tài liệu vận hành (Runbook). | Uptime $\ge$ 99.9%; Freshness $\le$ 24h. | Kỹ sư DevOps/SRE |

*Tổng thời lượng: 15 tuần (~4 tháng).*

---

## Bước 8 — Nhân sự, tổ chức dự án và cơ chế phối hợp

### 8.1. Cơ cấu nhân sự
| Vai trò | Số lượng | Trách nhiệm chính |
|:---|:---:|:---|
| **Project Manager (PM)** | 1 | Quản lý rào cản, ngân sách, tiến độ; Báo cáo Sponsor (Ban Giám đốc). |
| **Kỹ sư Dữ liệu (Data Engineer)** | 2 | Phát triển luồng ETL/ELT, duy trì Data Warehouse. |
| **Kỹ sư AI (ML Engineer)** | 2 | Phát triển, tinh chỉnh thuật toán và vận hành mô hình học máy. |
| **Kỹ sư Backend (Backend Dev)** | 1 | Viết API, phân quyền, tối ưu response time. |
| **Kỹ sư DevOps / SRE** | 1 | Xây hạ tầng Cloud, CI/CD, hệ thống monitoring, lo SLA. |
| **Kỹ sư Kiểm thử (QA)** | 1 | Test chất lượng, hiệu năng, điều phối UAT với User. |
| **Key User (QL Chi nhánh)** | 2 | Cung cấp logic xếp ca thực tế, kiểm thử UAT và ký sign-off. |

### 8.2. Ma trận phối hợp (RACI)
| Đầu việc chính | PM | Data Eng | ML Eng | Backend | SRE | QA | Key User |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Thu thập & làm sạch dữ liệu (Pha 1) | A | **R** | C | — | — | — | I |
| Chốt yêu cầu & Thiết kế hệ thống (Pha 2) | A | C | C | **R** | **R** | — | I |
| Phát triển Mô hình & API (Pha 3) | A | C | **R** | **R** | — | — | — |
| Duyệt UAT & Ký Sign-off (Pha 4) | A | I | I | I | I | C | **R** |
| Triển khai Go-live hạ tầng (Pha 5) | A | — | — | C | **R** | — | I |
| Bàn giao tài liệu vận hành | **R** | C | C | C | **R** | — | A |

*(**R**: Thực hiện, **A**: Chịu trách nhiệm duyệt, **C**: Tham vấn, **I**: Nhận thông tin)*

### 8.3. Cơ chế làm việc & Quản trị rủi ro
*   **Họp tiến độ:** Standup hàng tuần, báo cáo Sprint review 2 tuần/lần. Tại mốc kết thúc Pha, họp đánh giá (Milestone Review) với Sponsor.
*   **Quản lý thay đổi (Change Request - CR):** Nghiêm cấm scope creep (mở rộng phạm vi không kiểm soát). Mọi tính năng phát sinh ngoài Bước 4 phải lập phiếu CR để PM tính toán đội chi phí/thời gian duyệt.
*   **Quản lý Issue/Risk:** Tracking trên Jira. Bất kỳ rủi ro nào liên quan tới dữ liệu (bẩn, sai lệch) phải được báo cho Data Engineer giải quyết trong SLA $\le$ 24h.

---

## Bước 9 — Dự toán chi phí và phương án tài chính

### 9.1. Bảng phân tách dự toán (CAPEX / OPEX)
Chi phí tách bạch giữa phí đầu tư xây dựng ban đầu (CAPEX) và phí duy trì nền tảng, Cloud định kỳ hàng năm (OPEX). Có chèn quỹ dự phòng (Contingency) 10%.

#### A. Chi phí đầu tư dự án (CAPEX) — Giai đoạn 15 tuần
| Nhóm chi phí | Chi tiết hạng mục (Giả định đơn giá) | Thành tiền (VNĐ) |
|:---|:---|---:|
| **Nhân công (Dev/Outsource)** | Lương khoán đội dự án (PM, Data, ML, BE, SRE, QA) trong 1-4 tháng tùy vị trí (Trung bình 22tr/người/tháng). | 594.000.000 |
| **Bản quyền (License)** | Sử dụng Open-source (Airflow, MLflow, FastAPI). | 0 |
| **Hạ tầng (GĐ Phát triển)** | Phí thuê VM, GPU training, PostgreSQL, S3 môi trường Dev/Staging trong 4 tháng. | 64.000.000 |
| **Đào tạo & Chuyển giao** | Tổ chức 2 buổi hướng dẫn đọc Dashboard cho Key Users. | 5.000.000 |
| **Tổng CAPEX** | (Chưa bao gồm dự phòng rủi ro 10%) | **663.000.000** |

#### B. Chi phí vận hành Cloud & Bảo trì (OPEX) — 1 năm sau Go-live
| Nhóm chi phí | Chi tiết hạng mục | Thành tiền (VNĐ) |
|:---|:---|---:|
| **Hạ tầng (Cloud Server)** | Thuê K8s Cluster (96tr), PostgreSQL HA (54tr), S3 Storage (7.2tr), Băng thông & DNS (6tr). | 163.200.000 |
| **Hạ tầng (GPU AI)** | Thuê GPU Spot Instances chạy job tái huấn luyện (1 lần/tháng). | 9.600.000 |
| **Nhân sự Ops / Hypercare** | Chi phí part-time SRE/Data Eng duy trì SLA, giám sát hệ thống. | 132.000.000 |
| **Bảo mật & Tuân thủ** | Thuê bên thứ 3 Pentest đánh giá bảo mật API định kỳ (2 lần/năm). | 20.000.000 |
| **Tổng OPEX / Năm 1** | (Chưa bao gồm dự phòng rủi ro 10%) | **325.800.000** |

### 9.2. Tổng chi phí sở hữu (TCO) & Phương án tài chính
*   **Tổng dự phòng rủi ro (Contingency 10%):** 98.880.000 VNĐ
*   **Tổng TCO (Năm 1) = CAPEX + OPEX + Contingency = 1.087.680.000 VNĐ**
*   **Phương án tài chính:** Chủ trương chuyển hóa 100% chi phí hạ tầng máy chủ thành chi phí hoạt động OPEX hàng tháng (thuê Cloud) thay vì mua thiết bị vật lý. Tiết kiệm phí license qua hệ sinh thái mã nguồn mở.

### 9.3. Kiểm chứng tính nhất quán chi phí (Phân bổ theo giai đoạn)
Bảng kiểm chứng chứng minh tổng ngân sách CAPEX xin cấp (663 triệu) được phân bổ logic, khớp với WBS (Bước 7):

| Kế hoạch WBS | Phí nhân công (VNĐ) | Phí hạ tầng/khác (VNĐ) | Tổng cộng (VNĐ) |
|:---|---:|---:|---:|
| Pha 1: Khảo sát & Phân tích | 134.000.000 | 10.500.000 | 144.500.000 |
| Pha 2: Thiết kế (HLD/LLD) | 75.000.000 | 7.000.000 | 82.000.000 |
| Pha 3: Phát triển (Dev) | 265.000.000 | 30.500.000 | 295.500.000 |
| Pha 4: Kiểm thử (SIT/UAT) | 95.000.000 | 10.500.000 | 105.500.000 |
| Pha 5: Triển khai (Go-live) | 25.000.000 | 10.500.000 | 35.500.000 |
| **Kiểm chứng tổng (Khớp)**| **594.000.000** | **69.000.000** | **663.000.000** |

---

## Danh mục tài liệu tham khảo bổ sung (Giai đoạn 2)
[9] Google Cloud (n.d.), *Kubernetes Engine Documentation*, truy cập tại: https://cloud.google.com/kubernetes-engine/docs  
[10] Apache Software Foundation (n.d.), *Apache Airflow Documentation*, truy cập tại: https://airflow.apache.org/docs/  
[11] MLflow (n.d.), *MLflow Documentation — Model Registry*, truy cập tại: https://mlflow.org/docs/latest/model-registry.html  
[12] PMI (2021), *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*, 7th Edition, Project Management Institute.
