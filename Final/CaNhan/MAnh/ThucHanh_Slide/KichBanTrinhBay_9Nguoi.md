# KỊCH BẢN TRÌNH BÀY BÀI THỰC HÀNH (9 NGƯỜI)
**Dự án:** Ứng dụng Deep Learning & TSFM để dự báo lưu lượng khách hàng.
**Thời gian:** 45 phút (Mỗi người trình bày trong 5 phút, tập trung không ngắt quãng).
**Văn phong:** Kỹ thuật, trực diện, không dài dòng. Bám sát thiết kế kiến trúc và thông số.

---

## Người 1: Tổng quan & Hiện trạng (Phút 00:00 - 05:00)

**Slide 1:**
Kính chào hội đồng, em là [Tên], đại diện nhóm trình bày đề tài Thực hành: "Ứng dụng mô hình học sâu và mô hình nền tảng chuỗi thời gian để dự báo lưu lượng khách hàng". Đề tài triển khai trên hạ tầng Cloud nội bộ, phục vụ trực tiếp 34 chi nhánh Ways Station. Cam kết của dự án dựa trên các ngưỡng chỉ số sai số chính xác, không khóa chặt vào một thuật toán duy nhất.

**Slide 2:**
Bài toán trọng tâm của chúng em là cung cấp dự báo khách hàng theo khung giờ. Hiện tại, dữ liệu POS tại Ways Station đang rất phân tán và trễ từ 48-72h. Việc thiếu dự báo định lượng gây ra 4 điểm nghẽn lớn: Xếp ca cảm tính gây lãng phí hoặc thiếu hụt; Kho không chủ động được hàng; Khuyến mãi nhầm vào giờ cao điểm; và Trải nghiệm khách hàng giảm sút.

**Slide 3:**
Động lực đầu tư của hệ thống này là đóng vai trò như một Decision Support System - Hỗ trợ ra quyết định. Nó cung cấp số liệu đáng tin cậy để phòng Điều phối tối ưu lịch ca linh hoạt, Kho luân chuyển kịp thời. Nền tảng được xây trên Cloud với khả năng auto-scaling, đổi CAPEX thành OPEX, giúp tối ưu chi phí vận hành lâu dài cho doanh nghiệp.

---

## Người 2: Bộ KPI Kỹ thuật AI & Hệ thống (Phút 05:00 - 10:00)

**Slide 4:**
Kính chào hội đồng, em là [Tên]. Tiếp nối phần tổng quan, dự án được đo lường bằng hai nhóm KPI cứng.
Nhóm A là KPI cho Mô hình AI. Chúng em cam kết A.1: Chỉ số MAPE dưới 15% tại Pilot và siết xuống dưới 10% sau 3 tháng. A.2: Sai số tuyệt đối (MAE) tối đa 3 khách/chi nhánh/giờ. A.3: Độ chính xác phát hiện giờ cao điểm đạt 85%. A.4: Độ trễ suy luận AI thuần phải dưới 200ms và A.5: Độ ổn định giữa các mô hình kinh doanh (Gym, Net, Bida) không được chênh lệch sai số quá 10%.

**Slide 5:**
Nhóm B là KPI cho phần mềm và vận hành. Tốc độ phản hồi API (B.1) cam kết P95 dưới 500ms. Luồng ETL Batch (B.2) cho 34 chi nhánh hoàn tất dưới 30 phút. Uptime dịch vụ (B.3) phải đạt chuẩn 99,9% - tức downtime tối đa 43 phút/tháng. Độ toàn vẹn dữ liệu nạp vào phải vượt 99,5% và tuổi dữ liệu (Data Freshness) đảm bảo độ trễ không quá 24h.

---

## Người 3: Phân định ranh giới & Phạm vi (Phút 10:00 - 15:00)

**Slide 6:**
Em là [Tên]. Để tránh hiểu lầm khi triển khai song song Bài thực hành này và Đồ án Nền tảng, em xin phân định ranh giới đo lường. Đồ án đánh giá hạ tầng (Uptime 99.99%, Data Freshness luồng CDC < 5s), trong khi bài Thực hành đo lường Ứng dụng AI (Uptime 99.9%, Batch Data Freshness < 24h). Mức 99.9% của ứng dụng hoàn toàn lọt trong ngân sách rủi ro của nền tảng 99.99%. Hai hệ thống đo đối tượng khác nhau và bổ trợ hoàn hảo cho nhau.

**Slide 7:**
Về giới hạn, AI Engine ở đây chỉ làm nhiệm vụ Hỗ trợ ra quyết định, quyền quyết định phân ca hay luân chuyển vật tư hoàn toàn do con người. Ngoài ra, nếu trong quá trình thực nghiệm, các mô hình Deep Learning không đạt được MAPE dưới 15% như cam kết Pilot, nhóm đã chuẩn bị phương án fallback: Hệ thống sẽ xuất xưởng bản Beta với thuật toán Moving Average 7 ngày để đảm bảo có số liệu tham khảo cho vận hành, đồng thời xin CR gia hạn giai đoạn tuning mô hình.

---

## Người 4: Yêu cầu Nghiệp vụ & Chức năng (Phút 15:00 - 20:00)

**Slide 8:**
Em là [Tên]. Từ góc độ nghiệp vụ, hệ thống giải quyết 4 Use Case chính: Quản lý chi nhánh gọi API lấy dự báo 7 ngày; Hệ thống tự động push cảnh báo khi có khung giờ tải cao bất thường (>1.5 lần trung bình); Cronjob tự động chạy luồng pipeline lúc 1h sáng; và Đội IT có công cụ Grafana để giám sát các luồng dữ liệu này.

**Slide 9:**
Về yêu cầu chức năng kỹ thuật, hệ thống chia làm 3 Module. Module Data Pipeline chịu trách nhiệm Extract dữ liệu POS, làm sạch và ẩn danh các trường PII để tuân thủ Nghị định 13, sau đó đẩy vào kho tập trung. Module AI Engine huấn luyện lịch sử 12 tháng, đánh giá và lưu trữ bằng MLflow. Module API Service sử dụng FastAPI cung cấp các endpoint có bảo vệ bằng JWT và giới hạn Rate Limiting để phân phối dự báo.

---

## Người 5: Kiến trúc & Giải pháp (Phút 20:00 - 25:00)

**Slide 10:**
Chào hội đồng, em là [Tên]. Em xin trình bày về luồng nghiệp vụ TO-BE. Trình tự thời gian hàng ngày diễn ra như sau: Khách hàng giao dịch tại POS 24/7. Đúng 01:00 sáng, luồng Airflow sẽ rút toàn bộ dữ liệu giao dịch về Cloud. Lúc 02:00, Batch Inference chạy cho 34 chi nhánh và tự động gửi cảnh báo cao điểm. Đến 08:00 sáng, Quản lý chi nhánh truy cập Dashboard để chốt lịch điều phối nhân sự.

**Slide 11:**
Về kiến trúc kỹ thuật, chúng em xây dựng hệ thống 3 tầng rõ rệt. Tầng Trình bày (Presentation) gồm Web Dashboard và hệ thống Alerting Webhook. Tầng Ứng dụng đứng sau API Gateway, xử lý request thông qua Forecast Service và Alert Service viết bằng FastAPI, cùng Airflow điều phối batch. Cuối cùng, Tầng Dữ liệu (Data) dùng PostgreSQL làm kho Warehouse, S3 lưu trữ raw, MLflow quản lý mô hình và Prometheus thu thập metric hệ thống.

---

## Người 6: Luồng Xử lý Dữ liệu & Tích hợp (Phút 25:00 - 30:00)

**Slide 12:**
Em là [Tên]. Em xin đi sâu vào kỹ thuật luồng Data Pipeline. Giai đoạn Extract sử dụng Airflow rút dữ liệu trực tiếp từ 34 Database POS qua kênh mã hóa TLS, lưu vào S3 Raw Zone. Giai đoạn Transform sẽ thực hiện Data Cleansing, ẩn danh PII và đẩy vào PostgreSQL. Về AI, luồng Train chạy tái huấn luyện hàng tháng; trong khi luồng Predict chạy suy luận Batch hàng đêm và nạp kết quả trở lại bảng Forecast_Result.

**Slide 13:**
Về phương thức tích hợp đa hệ thống: Kết nối POS lên Cloud dùng JDBC/ODBC bắt buộc TLS mã hóa in-transit. Dữ liệu trên Cloud như S3 hay DWH được mã hóa lưu trữ at-rest bằng AES-256. Các nền tảng ERP hiện hữu của Ways Station khi cần kết quả dự báo chỉ việc gọi qua giao thức HTTPS RESTful với token JWT và phân quyền theo Role.

---

## Người 7: Kế hoạch triển khai & RACI (Phút 30:00 - 35:00)

**Slide 14:**
Kính chào hội đồng, em là [Tên]. Kế hoạch dự án kéo dài 15 tuần phát triển và 4 tuần Hypercare. Tuần 1-3 tập trung làm sạch Dataset. Tuần 4-5 chốt thiết kế kiến trúc. Tuần 6-10 là giai đoạn code API và Benchmark đa mô hình. Tuần 11-13 thực hiện kiểm thử Load Test. Tuần 14-19 là Go-live và duy trì Hypercare.

**Slide 15:**
Nhân sự dự án gồm 7 vai trò cốt lõi. Trong ma trận phối hợp RACI, Data Engineer chịu trách nhiệm làm sạch dữ liệu. ML Engineer tập trung vào việc Tuning đảm bảo MAPE < 15%. DevOps và QA đảm bảo khâu đóng gói tự động CI/CD và kiểm thử. Key User từ phòng Điều phối sẽ tham gia giai đoạn kiểm thử mức độ chấp nhận UAT và ký Sign-off.

---

## Người 8: Tài chính & TCO (Phút 35:00 - 40:00)

**Slide 16:**
Em là [Tên]. Tổng CAPEX đầu tư phát triển trong 15 tuần là 663 triệu đồng, tập trung vào chi phí chuyên gia thuật toán và kỹ sư. Về OPEX năm đầu duy trì hệ thống Cloud, thuê GPU tái huấn luyện và nhân sự giám sát bán thời gian là 325,8 triệu đồng. TCO tham chiếu vòng đời 3 năm là khoảng 1,79 tỷ đồng, đã gồm 10% dự phòng.

**Slide 17:**
Điểm quan trọng về tối ưu dòng tiền: Bằng việc kiến trúc trên Cloud, chúng ta cắt hoàn toàn việc mua Server vật lý. Nếu công ty phê duyệt chạy song song đề tài Thực hành này với Đồ án hạ tầng, toàn bộ chi phí Cloud như K8s, Kho dữ liệu, Băng thông (163,2 triệu/năm) sẽ được hấp thụ hoàn toàn vào Đồ án hạ tầng dùng chung, kéo TCO năm 1 của bài toán AI này giảm xuống chỉ còn khoảng 925 triệu đồng.

---

## Người 9: Quản trị Rủi ro, Kiểm thử & Vận hành (Phút 40:00 - 45:00)

**Slide 18:**
Chào hội đồng, em là [Tên], chốt lại phần kỹ thuật, dự án đối mặt với 3 rủi ro cốt lõi. Thứ nhất là dữ liệu bẩn, được xử lý tự động ngay tại tầng Pipeline. Thứ hai là Model không đạt ngưỡng, khắc phục bằng việc thực nghiệm benchmark đồng thời 4 mô hình (LSTM, Prophet, TSFM, ARIMA) để chọn thuật toán tốt nhất. Thứ ba là Data Drift do hành vi đổi, giải quyết bằng chu trình Auto-retraining.

**Slide 19:**
Trong công tác QA/QC, bài test quan trọng nhất là Load Test bằng JMeter giả lập 500 CCU truy cập đồng thời vào các API, ép hệ thống duy trì ngưỡng P95 dưới 500ms. Tiêu chí nghiệm thu Go-live bắt buộc hệ thống chạy Pilot liên tục 14 ngày không lỗi P0/P1, Uptime đạt 99.9% và sai số MAPE dưới 15%.

**Slide 20:**
Trong tháng đầu vận hành Hypercare, đội SRE sẽ giám sát trên Grafana và xử lý sự cố Tier 3 trong tối đa 4 tiếng. Lộ trình nâng cấp sau 12 tháng tiếp theo của hệ thống là tiến lên xử lý near-real-time và mở rộng khả năng dự báo sang luồng vật tư F&B nội bộ.
Bài trình bày của nhóm xin kết thúc tại đây. Cảm ơn hội đồng đã lắng nghe.

