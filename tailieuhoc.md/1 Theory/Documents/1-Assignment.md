# CHƯƠNG 1: BÀI TẬP TỔNG QUAN CNTT TRONG TỔ CHỨC VÀ BỐI CẢNH ỨNG DỤNG

- **Môn học:** Cơ sở hạ tầng Công nghệ thông tin
- **Tài liệu tham khảo:** [Slide Chương 1](../1.md)

---

## PHẦN 1: BÀI TẬP TRẮC NGHIỆM

### Câu 1
Trong 3 vai trò của CNTT trong cơ quan/doanh nghiệp, vai trò nào nhấn mạnh “đảm bảo tổ chức chạy ổn định mỗi ngày” thông qua hệ thống lõi, hạ tầng kỹ thuật, bảo mật/tuân thủ và SLA?
- **A.** Strategic Enabler (đòn bẩy chiến lược)
- **B.** Operational Backbone (xương sống vận hành)
- **C.** Risk Governance (cơ chế quản trị rủi ro)
- **D.** Business Transformation (tái cấu trúc mô hình kinh doanh)

> **Đáp án gợi ý:** **B. Operational Backbone**

---

### Câu 2
Thành phần nào thuộc Nền tảng vận hành (Ops Platform) theo phân lớp hạ tầng CNTT?
- **A.** IAM/SSO/MFA, SIEM/SOC, WAF
- **B.** API Gateway, microservices, container/K8s
- **C.** Monitoring/Observability, ITSM, CMDB, backup/DR, FinOps
- **D.** ETL/ELT, MDM, data governance, data quality

> **Đáp án gợi ý:** **C. Monitoring/Observability, ITSM, CMDB, backup/DR, FinOps**

---

### Câu 3
Theo slide, “CNTT là hạ tầng của chuyển đổi số” vì mỗi mức chuyển đổi cần năng lực nền tảng tương ứng. Ghép nào đúng?
- **A.** Digitization $\rightarrow$ chỉ cần phần cứng; Digitalization $\rightarrow$ chỉ cần mạng; Transformation $\rightarrow$ chỉ cần email
- **B.** Digitization $\rightarrow$ workflow, tích hợp, dữ liệu chuẩn; Digitalization $\rightarrow$ tự động hóa + đo lường + giám sát; Transformation $\rightarrow$ API + data + cloud + bảo mật + DevSecOps
- **C.** Digitization $\rightarrow$ AI; Digitalization $\rightarrow$ blockchain; Transformation $\rightarrow$ IoT
- **D.** Digitization $\rightarrow$ bỏ quy trình; Digitalization $\rightarrow$ bỏ dữ liệu; Transformation $\rightarrow$ bỏ bảo mật

> **Đáp án gợi ý:** **B. Digitization $\rightarrow$ workflow, tích hợp, dữ liệu chuẩn; Digitalization $\rightarrow$ tự động hóa + đo lường + giám sát; Transformation $\rightarrow$ API + data + cloud + bảo mật + DevSecOps**

---

### Câu 4
“Mâu thuẫn kinh điển” cần quản trị giữa vận hành và chuyển đổi số là gì, và một mô hình giải quyết được nêu trong slide?
- **A.** “Chi phí vs Doanh thu”; mô hình Waterfall
- **B.** “Ổn định vs Nhanh”; mô hình Run–Grow–Transform
- **C.** “On-prem vs Cloud”; mô hình Kanban
- **D.** “Bảo mật vs Dữ liệu”; mô hình 5S

> **Đáp án gợi ý:** **B. “Ổn định vs Nhanh”; mô hình Run–Grow–Transform**

---

### Câu 5
Chỉ số nào thuộc nhóm Delivery & Agility (DORA metrics)?
- **A.** Availability / Uptime
- **B.** MTTR (Mean Time To Recover)
- **C.** Deployment frequency / Lead time for change / Change failure rate
- **D.** Backup success rate, RPO/RTO

> **Đáp án gợi ý:** **C. Deployment frequency / Lead time for change / Change failure rate**

---

## PHẦN 2: BÀI TẬP ỨNG DỤNG

### Đề bài
Chọn 1 bối cảnh (Nhà nước / Doanh nghiệp / Giáo dục / Y tế / Dịch vụ / Sản xuất) và xây dựng “bức tranh CNTT như hạ tầng cho vận hành & chuyển đổi số” cho một đơn vị cụ thể (ví dụ: một trường Đại học, một bệnh viện, một công ty bán lẻ…).

### Yêu cầu sản phẩm nộp (5 nội dung):
1. **Mô tả 3 vai trò CNTT trong đơn vị bạn chọn:**
   - Operational Backbone (xương sống vận hành)
   - Strategic Enabler (đòn bẩy chiến lược)
   - Risk mechanism (cơ chế quản trị rủi ro)  
   *(Kèm 1–2 ví dụ hệ thống cụ thể cho mỗi vai trò).*
2. **Vẽ sơ đồ 5 lớp hạ tầng CNTT và điền các thành phần cụ thể của đơn vị:**
   - (1) Tính toán – Kết nối (Compute & Connectivity)
   - (2) Nền tảng vận hành (Ops Platform)
   - (3) Danh tính & Bảo mật (Security + Identity)
   - (4) Nền tảng ứng dụng & Tích hợp (App & Integration)
   - (5) Nền tảng dữ liệu (Data Platform)
3. **Nêu 2 rủi ro nếu hạ tầng yếu:**
   - Phân tích hiện tượng đứt gãy dự án, dữ liệu không tin cậy, sự cố an ninh… và đề xuất biện pháp giảm thiểu rủi ro tương ứng.
4. **Đề xuất bộ KPI tối thiểu (6–8 chỉ số) bao gồm 3 nhóm:**
   - *Reliability (Vận hành tin cậy):* Uptime, MTTR, RPO, RTO…
   - *Delivery & Agility (Chuyển đổi linh hoạt):* DORA metrics, tỷ lệ số hóa end-to-end, thời gian tích hợp API…
   - *Data & Security (Dữ liệu & An ninh):* Data Quality, số lượng sự cố an ninh nghiêm trọng…
5. **Viết lộ trình Run – Grow – Transform trong 6–12 tháng:**
   - Chia thành 3 giai đoạn (pha), mỗi pha xác định 2–3 đầu việc ưu tiên cốt lõi kèm theo kết quả kỳ vọng rõ ràng.
