---
marp: true
theme: default
paginate: true
---

# Ứng dụng AI Time-Series Forecasting
**Dự báo lưu lượng khách hàng đa chi nhánh**
- **Nhóm thực hiện:** Nhóm 5
- **Phạm vi:** Nền tảng Cloud & hệ thống Ways Station

---

# Bối cảnh & Điểm nghẽn hiện tại

- **Quy mô:** Chuỗi Ways Station vận hành 34 chi nhánh.
- **Điểm nghẽn kỹ thuật:** 
  - Xử lý dữ liệu POS thủ công, độ trễ 48-72 giờ.
  - Máy chủ chi nhánh yếu, không đủ huấn luyện AI.
- **Hệ quả vận hành:** Xếp ca theo cảm tính $\rightarrow$ Lãng phí nhân sự vào giờ thấp điểm, thiếu hụt phục vụ giờ cao điểm.

---

# Mục tiêu & Giải pháp đề xuất

- **Mục tiêu:** Xây dựng hệ thống Hỗ trợ ra quyết định (DSS) dựa trên dữ liệu.
- **Giải pháp lõi:**
  1. **Data Pipeline:** Tự động thu thập, chuẩn hóa từ POS lên Cloud.
  2. **AI Model:** Huấn luyện mô hình dự báo chuỗi thời gian (TSFM).
  3. **RESTful API:** Cấp quyền truy xuất dự báo real-time cho phần mềm nội bộ.

---

# KPI Kỹ thuật: Mô hình AI

- **MAPE < 10%:** Sai số phần trăm tuyệt đối trung bình (Cải thiện >10% so với phương pháp thủ công).
- **MAE $\le$ 3:** Sai số tuyệt đối tối đa 3 khách/giờ/chi nhánh.
- **Precision $\ge$ 85%:** Độ chính xác nhận diện đúng khung giờ cao điểm (Lưu lượng >1.5 lần mức trung bình).
- **Inference Latency $\le$ 200ms:** Thời gian đáp ứng của mỗi chu kỳ dự báo.

---

# KPI Kỹ thuật: Hệ thống & Vận hành

- **Tính sẵn sàng (Uptime) $\ge$ 99.9%**: Gián đoạn tối đa $\le$ 43.2 phút/tháng.
- **API Response Time (P95) $\le$ 500ms**: Tốc độ phản hồi của API.
- **Data Freshness $\le$ 24h**: Batch processing dữ liệu hoàn tất lúc 1h sáng.
- **Data Completeness $\ge$ 99.5%**: Tỷ lệ làm sạch và nạp thành công vào Data Warehouse.

---

# Kiến trúc hệ thống tổng thể (3 Lớp)

1. **Tầng Trình bày (Presentation):** 
   - Web Dashboard (DSS), Grafana (Giám sát), Alert (Webhook/Email).
2. **Tầng Ứng dụng (Application):** 
   - API Gateway, FastAPI (Forecast/Alert Service), Apache Airflow.
3. **Tầng Dữ liệu (Data):** 
   - PostgreSQL (Data Warehouse), MLflow (Model Registry), AWS S3 (Raw Data).

---

# Luồng dữ liệu tự động (Data Pipeline)

- **01:00 AM (Extract):** Tự động rút dữ liệu từ POS 34 chi nhánh (TLS) $\rightarrow$ Đẩy lên S3.
- **01:15 AM (Transform):** Làm sạch, chuẩn hóa $\rightarrow$ Nạp vào PostgreSQL.
- **02:00 AM (Predict):** AI Engine chạy Batch Inference $\rightarrow$ Lưu kết quả dự báo.
- **08:00 AM (Decision):** Sẵn sàng dữ liệu cho Quản lý chi nhánh duyệt ca làm việc.

---

# Các tính năng & Use case cốt lõi

- **ETL Tự động:** Đồng bộ và làm sạch dữ liệu hàng đêm.
- **API Dự báo:** Trả về kết quả lưu lượng dự báo trong 7 ngày tới (RESTful).
- **Cảnh báo Cao điểm:** Tự động gửi Alert khi lưu lượng dự báo đột biến.
- **Monitoring Dashboard:** Giám sát real-time (MAPE, Latency, Uptime).

---

# Lộ trình triển khai (15 Tuần)

- **Tháng 1 (T1-T3):** Khảo sát hệ thống, thu thập & làm sạch dữ liệu lịch sử.
- **Tháng 2 (T4-T5):** Thiết kế Kiến trúc (HLD/LLD), API Contract.
- **Tháng 3 (T6-T10):** Lập trình Pipeline (Airflow), Huấn luyện AI, Viết API.
- **Tháng 4 (T11-T13):** Kiểm thử SIT/UAT & Stress Test.
- **Tháng 4.5 (T14-T15):** Triển khai Go-live 34 chi nhánh & Bàn giao.

---

# Tổ chức nhân sự (RACI)

- **Project Manager (1):** Quản lý tiến độ, ngân sách, rủi ro.
- **Data Engineer (2):** Xây dựng kho dữ liệu & ETL.
- **ML Engineer (2):** Huấn luyện & tối ưu AI Model.
- **Backend / SRE / QA (3):** Code API, hạ tầng Cloud, CI/CD và Kiểm thử.
- **Key User (2):** Cung cấp nghiệp vụ xếp ca, tham gia nghiệm thu UAT.

---

# Dự toán chi phí (TCO)

- **Chi phí đầu tư (CAPEX):** ~663 Triệu VNĐ.
  - Phân bổ chính vào lương nhân sự (Dev/Outsource) trong 15 tuần.
- **Chi phí vận hành (OPEX / Năm 1):** ~325.8 Triệu VNĐ.
  - Phân bổ chính vào thuê hạ tầng Cloud & bảo trì.
- **Tối ưu tài chính:** Sử dụng Open-source (Airflow, MLflow), chuyển đổi CAPEX phần cứng sang OPEX Cloud linh hoạt.

---

# Quản trị rủi ro & Vận hành

- **Rủi ro Dữ liệu:** Tự động Drop/Fill missing values. Alert cho Data Engineer nếu tỷ lệ rớt >0.5%.
- **Rủi ro AI Drift:** Auto-trigger Retrain mô hình khi MAPE vượt ngưỡng >15%.
- **Sao lưu (Backup):** Áp dụng nguyên tắc 3-2-1 cho PostgreSQL.
- **Giám sát:** Metrics tập trung trên Grafana (SLA $\le$ 15p phát hiện sự cố).

---

# Đánh giá hiệu quả (Benefit Realization)

- **Tối ưu OPEX:** Giảm giờ công dư thừa vào các khung giờ thấp điểm.
- **Nâng cao chất lượng:** Đảm bảo đủ nhân lực phục vụ giờ cao điểm (Cải thiện trải nghiệm).
- **Văn hóa dữ liệu:** Chuyển đổi doanh nghiệp từ quyết định cảm tính sang Data-driven (Dựa trên dữ liệu).

---

# Q&A
**Cảm ơn Hội đồng đã lắng nghe!**

