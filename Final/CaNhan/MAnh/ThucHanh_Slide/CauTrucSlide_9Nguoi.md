# NỘI DUNG SLIDE THUYẾT TRÌNH BÀI THỰC HÀNH (DỰ BÁO LƯU LƯỢNG)
**Dự án:** Ứng dụng mô hình học sâu và mô hình nền tảng chuỗi thời gian để dự báo lưu lượng khách hàng đa chi nhánh.
**Quy mô:** 9 người trình bày
**Thời lượng tối đa:** 45 phút (Mỗi người ~5 phút)
**Văn phong:** Kỹ thuật, trực diện, không dài dòng.

---

## Người 1: Tổng quan dự án & Bối cảnh, Hiện trạng

**Slide 1: Tiêu đề & Thông tin chung**
*   **Đề tài:** Ứng dụng Deep Learning & Time-Series Foundation Models dự báo lưu lượng khách hàng.
*   **Phạm vi:** Nền tảng hạ tầng tính toán Cloud và luồng dữ liệu 34 chi nhánh Ways Station.
*   **Cam kết:** Nghiệm thu theo ngưỡng chỉ số (MAPE, MAE), không khóa cứng thuật toán.

**Slide 2: Bài toán trọng tâm & Vấn đề hiện tại**
*   **Bài toán:** Dự báo khách hàng theo khung giờ cho từng chi nhánh.
*   **4 Quy trình bị ảnh hưởng do thiếu dự báo:** Xếp ca nhân sự, Luân chuyển kho, Khuyến mãi, Chất lượng dịch vụ.
*   **Hiện trạng:** Dữ liệu phân tán, trễ 48-72h. Hạ tầng cục bộ không đủ năng lực xử lý ML.

**Slide 3: Động lực đầu tư & Giá trị mang lại**
*   **Định vị:** Xây dựng Hệ thống hỗ trợ ra quyết định (DSS).
*   **Giá trị:**
    *   Tối ưu điều phối nhân sự (đủ người giờ cao điểm, giảm dư thừa).
    *   Chủ động cung ứng kho bãi, không đứt gãy.
    *   Tự động mở rộng (Auto-scaling) trên Cloud, tối ưu OPEX.

---

## Người 2: Bộ KPI Kỹ thuật (Mô hình AI & Phần mềm)

**Slide 4: KPI Mô hình Trí tuệ nhân tạo (Nhóm A)**
*   **A.1 - MAPE (Sai số phần trăm tuyệt đối trung bình):** < 15% tại Pilot, < 10% sau 3 tháng.
*   **A.2 - MAE:** Lệch tối đa ≤ 3 khách/chi nhánh/khung giờ.
*   **A.3 - Precision (Độ chính xác cao điểm):** ≥ 85% cho khung giờ > 1.5x trung bình.
*   **A.4 - Latency:** Suy luận ≤ 200 ms/chu kỳ.
*   **A.5 - Ổn định:** Δ MAPE ≤ 10% giữa các ngữ cảnh (Gym, Gaming, Hub).

**Slide 5: KPI Phần mềm & Vận hành (Nhóm B)**
*   **B.1 - API P95:** ≤ 500 ms/request.
*   **B.2 - Batch Job Duration:** ≤ 30 phút cho 34 chi nhánh.
*   **B.3 - Uptime:** ≥ 99.9% (Downtime ≤ 43,2 phút/tháng).
*   **B.4 & B.5 - Dữ liệu:** Completeness ≥ 99.5%, Freshness luồng batch ≤ 24h.
*   **B.6 & B.7 - Lỗi:** Error Rate < 0.1%, Thời gian phát hiện sự cố (MTTD) ≤ 15 phút.

---

## Người 3: Phân định phạm vi & Ràng buộc hệ thống

**Slide 6: Ranh giới đo lường (Thực hành vs. Đồ án nền tảng)**
*   *(Bảng so sánh 4 tiêu chí lõi)*
*   **Đối tượng:** Ứng dụng dự báo (Thực hành) vs. Nền tảng hạ tầng (Đồ án).
*   **Uptime:** 99.9% (Ứng dụng) nằm trong ngưỡng an toàn của 99.99% (Nền tảng).
*   **Độ trễ:** Batch Freshness ≤ 24h (xử lý lô hàng đêm) so với luồng CDC ≤ 5s của nền tảng.
*   Hai hệ thống đo độc lập, bổ trợ nhau không mâu thuẫn.

**Slide 7: Giới hạn hệ thống & Phương án dự phòng (Fallback)**
*   **Trách nhiệm AI:** Chỉ đóng vai trò tham khảo (DSS). Quyết định cuối cùng do con người.
*   **Ngoài phạm vi:** Không sửa đổi ERP, POS gốc.
*   **Fallback thuật toán:** Nếu các mô hình Deep Learning không đạt MAPE < 15%, phát hành chế độ beta, giữ Moving Average 7 ngày làm fallback và gia hạn tuning.

---

## Người 4: Yêu cầu Nghiệp vụ & Chức năng (FR/NFR)

**Slide 8: Yêu cầu Nghiệp vụ (User Stories)**
*   **BR-01:** Quản lý chi nhánh xem dự báo (gọi API trả JSON).
*   **BR-02:** Cảnh báo giờ cao điểm (tự động webhook/email khi vượt 1.5x tải).
*   **BR-03:** Cronjob tự động hóa Data Pipeline hàng đêm.
*   **BR-04:** SRE giám sát metric trên Grafana.

**Slide 9: Yêu cầu Chức năng (FR) theo 3 Module**
*   **FR Pipeline:** Tự động trích xuất POS lúc 01:00 AM, làm sạch, nạp DWH.
*   **FR AI Engine:** Hỗ trợ dự báo 7 ngày, tái huấn luyện hàng tháng, Model Registry (MLflow).
*   **FR API:** Cung cấp RESTful API có JWT/RBAC để phân phối kết quả.

---

## Người 5: Kiến trúc & Giải pháp Đề xuất (TO-BE)

**Slide 10: Quy trình nghiệp vụ TO-BE (Timeline hàng ngày)**
*   **24/7:** POS thu thập giao dịch.
*   **01:00 AM:** Extract data về Cloud.
*   **02:00 AM:** Chạy Batch Inference bằng AI cho 34 chi nhánh. Tự động đẩy cảnh báo.
*   **08:00 AM (Điểm kiểm soát):** Quản lý xem API dự báo, duyệt lịch phân ca & kho bãi.

**Slide 11: Sơ đồ kiến trúc 3 tầng (Trình bày - Ứng dụng - Dữ liệu)**
*   *(Chèn sơ đồ kiến trúc hệ thống)*
*   **Tầng Trình bày:** Web Dashboard, Grafana, Webhook.
*   **Tầng Ứng dụng:** API Gateway, Forecast Service, Airflow.
*   **Tầng Dữ liệu:** PostgreSQL (DWH), S3 (Raw), MLflow (Registry), Prometheus.

---

## Người 6: Luồng dữ liệu (Data Pipeline) & Tích hợp

**Slide 12: Chi tiết luồng Data Pipeline & Huấn luyện**
*   **Extract:** Airflow rút batch qua TLS từ POS → Raw S3.
*   **Transform:** Khử trùng lặp, ẩn danh PII (NĐ13) → PostgreSQL Clean Zone.
*   **Train:** Tái huấn luyện hàng tháng lưu artifact tại MLflow.
*   **Predict:** Suy luận hàng đêm, nạp về `Forecast_Result`.

**Slide 13: Ma trận Tích hợp các hệ thống**
*   **POS → S3:** JDBC/ODBC qua TLS (Mã hóa đường truyền).
*   **S3 → DWH:** Internal VPC (Mã hóa lưu trữ AES-256).
*   **API → ERP:** HTTPS RESTful + JWT.
*   **Prometheus:** Pull metrics nội bộ 15s/lần.

---

## Người 7: Kế hoạch Triển khai (WBS) & Tổ chức Nhân sự

**Slide 14: Lộ trình triển khai (15 tuần + 4 tuần Hypercare)**
*   **T1-T3:** Khảo sát & Làm sạch dataset (Target: 99.5% Completeness).
*   **T4-T5:** HLD/LLD & API Contract.
*   **T6-T10:** Dev Pipeline & AI Model (Benchmark đa mô hình).
*   **T11-T13:** SIT/UAT & Load Test.
*   **T14-T19:** Go-live & Hypercare 1 tháng, tái huấn luyện lần 1.

**Slide 15: Cơ cấu nhân sự & RACI**
*   **Đội ngũ (7 vị trí):** PM, Data Eng, ML Eng, Backend, DevOps/SRE, QA, Key User.
*   **RACI tiêu biểu:**
    *   ML Eng: Chịu trách nhiệm (R) phát triển mô hình, Tuning.
    *   Key User: Tham gia UAT và Duyệt Sign-off.

---

## Người 8: Dự toán Chi phí & Phương án Tài chính

**Slide 16: Tổng chi phí sở hữu (TCO) Dự án độc lập**
*   **CAPEX (Phát triển 15 tuần):** 663 triệu VNĐ (Chiếm chủ yếu bởi nhân công).
*   **OPEX (Vận hành Năm 1):** 325,8 triệu VNĐ (Cloud K8s, GPU, Part-time Ops, Pentest).
*   **TCO 3 năm (Tham chiếu):** ~1.79 tỷ VNĐ (Bao gồm dự phòng 10%).

**Slide 17: Giải pháp tài chính & Chống chồng lấn Đồ án**
*   **Thuê Cloud:** Chuyển CAPEX phần cứng thành OPEX để tối ưu dòng tiền.
*   **Tối ưu Hấp thụ (Nếu chạy song song với Đồ án Nền tảng):**
    *   Chi phí K8s, DWH, Băng thông (163.2tr) → Khấu trừ hoàn toàn vào Đồ án.
    *   Nhân sự Ops → Dùng chung hệ sinh thái.
    *   **TCO Năm 1 thực tế:** Giảm từ 1.08 tỷ xuống còn ~925 triệu VNĐ.

---

## Người 9: Quản trị Rủi ro, Kiểm thử & Vận hành

**Slide 18: Rủi ro cốt lõi (Risk Register)**
*   **R01 (Dữ liệu bẩn):** Xử lý bằng pipeline tự động (Fill NA).
*   **R02 (Model sai lệch):** Benchmark song song 4 mô hình, giữ phương pháp ổn định nhất (MAPE < 15%).
*   **R03 (Data Drift):** Tái huấn luyện tự động định kỳ, monitor ∆ MAPE liên tục.

**Slide 19: Chiến lược Kiểm thử & Nghiệm thu**
*   **Load Test:** JMeter 500 CCU, đảm bảo API P95 ≤ 500ms.
*   **Nghiệm thu lõi:** Pass 100% test case UAT, Uptime 99.9%, MAPE < 15% (Pilot).

**Slide 20: Vận hành & Chuyển giao**
*   **Hypercare:** Daily standup 09:00 AM, SRE xử lý Tier 3 trong ≤ 4 giờ.
*   **Giám sát:** Grafana alerting tự động qua Slack/PagerDuty.
*   **Lộ trình (6-12T):** Chuyển dịch near-real-time và mở rộng dự báo doanh thu.

