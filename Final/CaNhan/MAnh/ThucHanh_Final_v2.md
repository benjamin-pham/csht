# 1. Thông tin chung & tên đề tài

- **Tên đề tài:** Ứng dụng mô hình học sâu và mô hình nền tảng chuỗi thời gian (Deep Learning & Time-Series Foundation Models) để dự báo lưu lượng khách hàng đa chi nhánh.
- **Thông tin chung:** Đơn vị chủ trì: Nhóm 5. Phạm vi triển khai: nền tảng hạ tầng tính toán Cloud và luồng dữ liệu của chuỗi Ways Station.

> **Ghi chú về cách đặt tên đề tài:** tên đề tài nêu **nhánh kỹ thuật** thay vì khóa chặt vào một thuật toán cụ thể. Nhóm dự kiến thực nghiệm tối thiểu 4 phương pháp thuộc nhánh này (TSFM, LSTM/BiLSTM, Prophet, ARIMA) và lựa chọn mô hình cho kết quả tốt nhất, ổn định nhất trên dữ liệu thực tế. Cam kết nghiệm thu gắn với **ngưỡng chỉ số đạt được**, không gắn với việc bắt buộc dùng một thuật toán cụ thể.

---

# 2. Bối cảnh – hiện trạng – vấn đề

## 2.1. Quy trình và nhóm người dùng trong phạm vi

Bài toán trọng tâm: **dự báo lưu lượng khách hàng theo từng khung giờ cho từng chi nhánh**. Đây là thông tin đầu vào mà nhiều quy trình nghiệp vụ hiện hành của Ways Station đang thiếu:

| Quy trình hiện hành | Nhóm người dùng | Điểm nghẽn khi không có dự báo |
|:---|:---|:---|
| Xếp ca và điều phối nhân sự | Phòng Điều phối, Quản lý chi nhánh | Xếp ca theo cảm tính → thiếu người giờ cao điểm, dư người giờ thấp điểm |
| Luân chuyển hàng hoá và vật tư | Bộ phận Kho hàng | Không dự báo được nhu cầu → đứt gãy cung ứng hoặc tồn đọng quá hạn |
| Lập kế hoạch khuyến mãi, kích cầu | Bộ phận Marketing | Chạy khuyến mãi vào khung giờ đã kín chỗ → lãng phí ngân sách |
| Bảo đảm chất lượng dịch vụ | Quản lý chi nhánh | Không lường trước được đột biến → khách chờ lâu, trải nghiệm giảm |

Một kết quả dự báo duy nhất phục vụ đồng thời **bốn quy trình, ba phòng ban** — đây là cơ sở cho tính cấp thiết của đề tài.

## 2.2. Chuẩn bị đầu vào

- **Bối cảnh:** chuỗi Ways Station vận hành 34 chi nhánh đa dịch vụ, lưu lượng khách biến động mạnh theo khung giờ trong ngày và theo ngày trong tuần.
- **Vấn đề hiện tại:** phân tích và dự báo số lượng khách tại mỗi chi nhánh hiện được thực hiện thủ công. Cơ sở dữ liệu giao dịch rời rạc, chưa được làm sạch, thiếu luồng xử lý tự động. Hạ tầng hiện hữu không đủ năng lực tính toán để huấn luyện mô hình học máy.
- **Đối tượng sử dụng:** hệ thống dữ liệu tập trung (Data Warehouse), máy chủ dịch vụ API (Application Programming Interface).
- **Hệ thống liên quan:** hệ thống POS (Point of Sale) tại chi nhánh, phần mềm ERP (Enterprise Resource Planning) và các nền tảng báo cáo nội bộ.
- **Ràng buộc:** giới hạn cấu hình hạ tầng hiện có; yêu cầu cao về tính sẵn sàng và bảo mật của luồng dữ liệu (Data Pipeline); dữ liệu giao dịch phải được ẩn danh theo Nghị định 13/2023/NĐ-CP.

## 2.3. Hiện trạng vận hành & điểm nghẽn hệ thống

- **Dữ liệu phân tán và độ trễ cao:** toàn bộ dữ liệu giao dịch POS tại 34 chi nhánh hiện được xử lý thủ công và lưu trữ phân tán, dẫn đến độ trễ tổng hợp dữ liệu từ 48 đến 72 giờ.
- **Hoạch định tài nguyên bị động theo kinh nghiệm:** do thiếu công cụ dự báo định lượng theo chuỗi thời gian, việc điều phối nguồn lực phụ thuộc hoàn toàn vào cảm tính:
  - *Khung giờ cao điểm:* thiếu nhân lực phục vụ và gián đoạn nguồn cung vật tư, kéo dài thời gian chờ và làm suy giảm chất lượng dịch vụ.
  - *Khung giờ thấp điểm:* dư thừa nhân lực phân bổ cố định, gây lãng phí chi phí vận hành (OPEX - Operational Expenditure).
- **Hạn chế hạ tầng tính toán cục bộ:** máy chủ tại chi nhánh không đủ năng lực để làm sạch, trích xuất đặc trưng và huấn luyện mô hình học máy trên tập dữ liệu lịch sử lớn.

## 2.4. Động lực đầu tư & giá trị hệ thống mang lại

Hệ thống dự báo lưu lượng khách theo chuỗi thời gian kết hợp đường ống dữ liệu tự động đóng vai trò **Hệ thống hỗ trợ ra quyết định (DSS - Decision Support System)**, mang lại các giá trị cốt lõi:

1. **Hỗ trợ tối ưu hóa điều phối nhân lực:** cung cấp dữ liệu dự báo theo từng khung giờ, làm cơ sở định lượng giúp Phòng Điều phối thiết lập ca làm việc linh hoạt, hạn chế giờ công dư thừa và bảo đảm đủ nhân lực giờ cao điểm.
2. **Hỗ trợ kế hoạch điều phối cung ứng:** dự báo nhu cầu sát thực tế, hỗ trợ Bộ phận Kho hàng lập kế hoạch luân chuyển kịp thời, hạn chế đứt gãy cung ứng hoặc tồn đọng quá hạn.
3. **Cung cấp dữ liệu định hướng kế hoạch tiếp thị:** nhận diện chính xác các khung giờ thấp điểm định kỳ để gợi ý thời điểm kích cầu, tránh khuyến mãi lãng phí vào khung giờ đã đạt ngưỡng phục vụ tối đa.

## 2.5. Ưu thế kiến trúc kỹ thuật & cam kết vận hành

- **Tối ưu chi phí nhờ nền tảng Cloud:** chuyển từ mua sắm máy chủ vật lý (CAPEX - Capital Expenditure) sang thuê dịch vụ điện toán đám mây linh hoạt (OPEX).
- **Khả năng tự động co giãn (Auto-scaling):** hạ tầng Cloud tự mở rộng khi lưu lượng gọi API tăng vọt và thu hẹp khi tải giảm.
- **Cam kết mức độ dịch vụ (SLA - Service Level Agreement):** tính sẵn sàng của dịch vụ API đạt Uptime ≥ 99,9% (gián đoạn tối đa 43,2 phút/tháng), thời gian phản hồi ở mức mili-giây, dữ liệu được bảo vệ theo chuẩn mực bảo mật thông tin.

---

# 3. Mục tiêu & KPI (Key Performance Indicator)

## 3.1. Mục tiêu tổng quát

Xây dựng nền tảng tự động thu thập dữ liệu giao dịch, huấn luyện mô hình học máy phân tích chuỗi thời gian, và cung cấp kết quả dự báo thông qua các API chuyên dụng phục vụ nội bộ.

## 3.2. Mục tiêu cụ thể và KPI kỹ thuật

Hệ thống phần mềm không áp dụng KPI phân rã theo tầng hạ tầng của đồ án, mà phân tách thành **2 nhóm chỉ số độc lập**. Mỗi KPI có tên độ đo chuẩn, công thức, baseline đối chứng, mốc đo và người chịu trách nhiệm số liệu.

### Nhóm A — KPI Mô hình Trí tuệ nhân tạo (AI Model KPIs)

| Mã | Tên độ đo | Baseline đối chứng | Target | Mốc đo | Owner |
|:---|:---|:---|:---|:---|:---|
| **A.1** | MAPE — Mean Absolute Percentage Error [1][8] | Moving Average 7 ngày ~25–30%; ARIMA(1,1,1) ~18–22% | **< 15% tại nghiệm thu Pilot (T13)** → **< 10% sau go-live 3 tháng**; cải thiện ≥ 10% so với baseline tốt nhất | G3; +1/+3/+6 tháng | ML Engineer |
| **A.2** | MAE — Mean Absolute Error [2] | Không đo lường được (xếp ca cảm tính) | ≤ 3 khách/chi nhánh/khung giờ | G3; +3 tháng | ML Engineer |
| **A.3** | Peak Traffic Detection Precision [3] | Không đo lường được | ≥ 85% với khung giờ vượt ngưỡng 1,5 × lưu lượng trung bình | G3; +3 tháng | ML Engineer |
| **A.4** | Model Inference Latency | Không áp dụng | ≤ 200 ms/chu kỳ suy luận của 1 chi nhánh | G3; G4 | ML Engineer |
| **A.5** | Độ ổn định đa ngữ cảnh (Δ MAPE) | Không đo lường được | Δ ≤ 10% giữa các ngữ cảnh Gym / Gaming / Hub, trên tối thiểu 4 bộ dữ liệu kiểm thử | G3; +6 tháng | ML Engineer |

**Diễn giải và công thức:**

1. **A.1 — MAPE**
   $$\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%$$
   Đo mức chênh lệch phần trăm giữa lưu lượng khách thực tế ($y_i$) và dự báo ($\hat{y}_i$). Ngưỡng được thiết kế theo **lộ trình siết dần**: < 15% tại thời điểm nghiệm thu Pilot (dữ liệu vừa migrate, chưa đủ chu kỳ mùa vụ) → < 10% sau go-live 3 tháng (khi Data Completeness ổn định ≥ 99,5% và mô hình đã qua tối thiểu 2 chu kỳ tái huấn luyện). Baseline đối chứng tham khảo Hyndman & Athanasopoulos [8]. Trích dẫn độ đo: Scikit-Learn [1].

2. **A.2 — MAE**
   $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
   Phản ánh độ lệch số lượng khách cụ thể trong mỗi khung giờ, đảm bảo sai số không ảnh hưởng lớn đến việc tham khảo xếp ca. Trích dẫn: Scikit-Learn [2].

3. **A.3 — Precision**
   $$\text{Precision} = \frac{TP}{TP + FP}$$
   Trong tập kiểm thử gồm các trường hợp được mô hình nhận diện là giờ cao điểm, ít nhất 85% thực sự là giờ cao điểm ($TP$), hạn chế tối đa báo động giả ($FP$). Trích dẫn: Powers (2011) [3].

4. **A.4 — Inference Latency:** thời gian suy luận thuần của mô hình cho 1 chu kỳ dự báo của 1 chi nhánh, không bao gồm thời gian gateway và truy vấn cơ sở dữ liệu.

5. **A.5 — Độ ổn định đa ngữ cảnh:** $\Delta = \max(\text{MAPE}_j) - \min(\text{MAPE}_j)$ với $j$ là các ngữ cảnh dữ liệu (chi nhánh Gym, Gaming, Hub) và các mốc thời gian khác nhau. Cam kết mô hình không chỉ chính xác trên một ngữ cảnh mà **ổn định trên nhiều ngữ cảnh và nhiều khoảng thời gian**.

### Nhóm B — KPI Phần mềm & Vận hành hệ thống

| Mã | Tên độ đo | Baseline | Target | Mốc đo | Owner |
|:---|:---|:---|:---|:---|:---|
| **B.1** | API Response Time P95 [6] | Chưa có API | ≤ 500 ms/request (end-to-end, đã bao gồm A.4) | G4; +1 tháng | Backend Dev |
| **B.2** | Batch Job Duration | Tổng hợp thủ công 48–72h | ≤ 30 phút cho toàn bộ 34 chi nhánh | G4; +1 tháng | Data Engineer |
| **B.3** | Software Availability / Uptime [4] | Chưa có hệ thống | ≥ 99,9% (downtime ≤ 43,2 phút/tháng) | G5; +1/+3/+6 tháng | DevOps/SRE |
| **B.4** | Data Completeness [5] | Dữ liệu rời rạc, chưa làm sạch | ≥ 99,5% bản ghi POS nạp thành công | G1; G5; +3 tháng | Data Engineer |
| **B.5** | **Batch Data Freshness — luồng huấn luyện/dự báo** [5] | 48–72 giờ | ≤ 24 giờ (hoàn tất đồng bộ 01:00 AM) | G5; +1 tháng | Data Engineer |
| **B.6** | API Error Rate [7] | Không áp dụng | < 0,1% (HTTP 5xx) | G4; +1 tháng | QA / SRE |
| **B.7** | MTTD — Mean Time To Detect | 4–8 giờ (nhân viên báo lỗi qua Zalo) | ≤ 15 phút | G5; +3 tháng | DevOps/SRE |

**Diễn giải và công thức:**

1. **B.1 — API Response Time:** $P95 \le 500\ \text{ms}$ — bảo đảm 95% số request có thời gian xử lý và trả kết quả dưới 500 ms. Trích dẫn: AWS Builders' Library [6].
2. **B.2 — Batch Job Duration:** thời gian chạy trọn vẹn luồng ETL + batch inference cho 34 chi nhánh.
3. **B.3 — Uptime:** $\text{Uptime} = \frac{\text{Total Time} - \text{Downtime}}{\text{Total Time}} \times 100\%$. Trích dẫn: Google SRE [4].
4. **B.4 — Completeness:** $\frac{\text{Số bản ghi nạp thành công}}{\text{Tổng số bản ghi gốc tại POS}} \times 100\%$. Trích dẫn: ISO/IEC 25012 [5].
5. **B.5 — Batch Data Freshness:** $\Delta t = t_{\text{Data Warehouse}} - t_{\text{POS}} \le 24\ \text{h}$. Trích dẫn: ISO/IEC 25012 [5].
6. **B.6 — Error Rate:** $\frac{\text{Số phản hồi HTTP 5xx}}{\text{Tổng số request}} \times 100\%$. Trích dẫn: Google SRE SLO [7].
7. **B.7 — MTTD:** tổng thời gian từ lúc sự cố xảy ra đến lúc được phát hiện, cộng dồn toàn bộ sự cố trong kỳ, chia cho số sự cố.

## 3.3. Phân định phạm vi KPI với đồ án môn học cùng nhóm

Nhóm thực hiện song song hai đề tài trên cùng doanh nghiệp Ways Station. Ranh giới đo lường:

| Tiêu chí | Bài thực hành (tài liệu này) | Đồ án môn học |
|:---|:---|:---|
| **Đối tượng đo** | Sản phẩm phần mềm: Forecast Service, Data Pipeline batch, mô hình AI | Năng lực nền tảng: API Gateway, Kafka, Edge Cluster, Data Lakehouse, IAM |
| **Uptime** | ≥ 99,9% (ứng dụng) | ≥ 99,99% (nền tảng). Hao hụt ở tầng dịch vụ nằm trong ngân sách sẵn sàng của nền tảng |
| **Độ trễ dữ liệu** | Batch Data Freshness luồng huấn luyện ≤ 24h — kiến trúc Batch Processing xử lý dữ liệu lịch sử theo lô hàng đêm, không yêu cầu real-time | Data Freshness luồng CDC ≤ 5s — streaming thời gian thực cho nền tảng dữ liệu tập trung |
| **Độ trễ dự báo** | Model inference thuần ≤ 200 ms (KPI A.4) | API dự báo end-to-end P95 ≤ 500 ms (TR-P07), đã bao gồm 200 ms suy luận |
| **Độ chính xác mô hình** | KPI lõi: MAPE < 15% tại Pilot → < 10% sau 3 tháng | Không phải KPI nền tảng; chỉ là tiêu chí nghiệm thu Pilot (MAPE < 15%) |

Hai bộ KPI đo **hai đối tượng khác nhau**; các ngưỡng chênh lệch đều nằm trong quan hệ bao hàm hoặc khác điều kiện đo, không mâu thuẫn.

## 3.4. Ánh xạ KPI theo giai đoạn triển khai và tiêu chí bàn giao

| Giai đoạn | Hoạt động kỹ thuật | Deliverables | KPI nghiệm thu | Nhân sự phụ trách |
| :--- | :--- | :--- | :--- | :--- |
| **G1: Khảo sát & Phân tích dữ liệu** | Thu thập dữ liệu lịch sử POS, chuẩn hóa schema, làm sạch dữ liệu khuyết thiếu | Tài liệu đặc tả dữ liệu; Dataset đã làm sạch | **B.4** Completeness ≥ 99,5%; Schema hợp lệ 100% | Kỹ sư Dữ liệu |
| **G2: Thiết kế kiến trúc phần mềm** | Thiết kế Data Pipeline, Web Service RESTful API và mô hình AI | Tài liệu thiết kế kiến trúc; API Contract | 100% API đạt chuẩn RESTful; kiến trúc sẵn sàng mở rộng | Kiến trúc sư Phần mềm |
| **G3: Phát triển mô hình & Pipeline** | Xây dựng ETL tự động; thực nghiệm ≥ 4 phương pháp, tinh chỉnh mô hình tốt nhất | Mã nguồn Data Pipeline; Artifact mô hình AI | **A.1** MAPE < 15% (Pilot); **A.3** Precision ≥ 85%; **A.4** ≤ 200 ms; **A.5** Δ ≤ 10% | Kỹ sư AI |
| **G4: Kiểm thử & Đóng gói** | Integration Test, Load Test, đóng gói Container | Docker Image; bộ kịch bản Test; báo cáo UAT | **B.1** P95 ≤ 500 ms; **B.6** Error Rate < 0,1%; **B.2** Batch ≤ 30 phút | Kỹ sư Kiểm thử (QA) |
| **G5: Triển khai & Vận hành** | Triển khai Cloud, thiết lập giám sát Prometheus/Grafana | Hệ thống API Production; Dashboard giám sát | **B.3** Uptime ≥ 99,9%; **B.5** Freshness ≤ 24h; **B.7** MTTD ≤ 15 phút | Kỹ sư DevOps/SRE |
| **Sau go-live** | Vận hành, tái huấn luyện, đo hiệu quả | Báo cáo Benefit Realization | **A.1** MAPE < 10% (mốc +3 tháng) | ML Engineer + PM |

---

# 4. Đối tượng áp dụng, phạm vi, giả định/ràng buộc

## 4.1. Đối tượng và phạm vi

- Tập trung vào **1 quy trình kỹ thuật lõi**: xây dựng luồng tích hợp dữ liệu từ máy POS tại chi nhánh lên Cloud, huấn luyện mô hình dự báo chuỗi thời gian, và xuất kết quả qua RESTful API.
- **Người dùng đích:** Quản lý chi nhánh (34), Quản lý trung tâm / Phòng Điều phối, Bộ phận Kho hàng, Bộ phận Marketing, đội IT vận hành.

## 4.2. Phần ngoài phạm vi

- Không can thiệp, sửa đổi kiến trúc phần mềm quản lý kho, phần mềm nhân sự, hoặc hệ thống ERP hiện hành. Các phần mềm này giao tiếp thông qua API được cung cấp.
- **Không bao gồm đầu tư hạ tầng Lớp 4 & Lớp 5** (API Gateway, Kafka, Edge Cluster, Data Lakehouse, IAM tập trung) — nội dung này thuộc đề tài đồ án cùng nhóm *Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station*. Bài thực hành giả định một môi trường Cloud độc lập và **không phụ thuộc vào việc đồ án có được phê duyệt hay không**. Trường hợp cả hai được triển khai đồng thời, hệ thống dự báo sẽ tái sử dụng Data Lakehouse của nền tảng thay vì dựng Data Warehouse riêng (xem ghi chú chi phí tại mục 9.4).

## 4.3. Giới hạn đề tài & vai trò của AI

- **Giới hạn trách nhiệm AI:** nền tảng AI chỉ đóng vai trò **hỗ trợ ra quyết định**. Các bộ phận nghiệp vụ sử dụng kết quả dự báo để tham khảo; **quyết định điều phối cuối cùng hoàn toàn do quản lý con người**.
- **Giới hạn kỹ thuật:** khả năng dự đoán suy giảm đáng kể khi gặp sự kiện đột biến không có mẫu trong tập dữ liệu lịch sử (bão lũ, sự kiện bất thường). Mô hình yêu cầu tái huấn luyện định kỳ hàng tháng để duy trì độ chính xác.
- **Phương án kỹ thuật dự phòng:** nhóm cam kết **ngưỡng chỉ số**, không cam kết thuật toán cụ thể. Quy trình lựa chọn mô hình: thực nghiệm song song tối thiểu 4 phương pháp (TSFM, LSTM/BiLSTM, Prophet, ARIMA) trên cùng tập dữ liệu và cùng bộ độ đo, chọn phương pháp cho kết quả tốt nhất và ổn định nhất (A.5). Nếu không phương pháp nào đạt MAPE < 15% tại Pilot, hệ thống phát hành ở **chế độ beta không ràng buộc nghiệm thu**, giữ Moving Average 7 ngày làm fallback, và lập Change Request gia hạn giai đoạn G3.

---

# 5. Yêu cầu nghiệp vụ & yêu cầu hệ thống (FR/NFR)

## 5.1. Yêu cầu nghiệp vụ (Business Requirements / Use Case level)

| ID | Tên nghiệp vụ (User Story) | Tác nhân | Luồng chính | Ngoại lệ | Đầu ra |
|:---|:---|:---|:---|:---|:---|
| BR-01 | Xem dự báo lưu lượng khách | Quản lý chi nhánh | 1. Đăng nhập <br>2. Chọn chi nhánh & khoảng thời gian <br>3. Hệ thống gọi API trả về dữ liệu dự báo | API lỗi hoặc chưa có dự báo mới → báo lỗi & hiển thị dữ liệu lịch sử tuần trước | Bảng/biểu đồ dự báo khách theo giờ (JSON) |
| BR-02 | Nhận cảnh báo giờ cao điểm | Bộ phận Điều phối | 1. Hệ thống phân tích kết quả dự báo <br>2. Nếu lượng khách > 1,5 × trung bình → tự động gửi cảnh báo | Gửi email/webhook thất bại → đẩy thông báo trực tiếp trên App/Dashboard nội bộ | Thông báo cảnh báo (webhook/email) |
| BR-03 | Tự động hoá Pipeline dữ liệu | Hệ thống (Cronjob) | 1. Kết nối POS DB (01:00 AM) <br>2. Trích xuất batch <br>3. Làm sạch, chuẩn hóa <br>4. Nạp vào Data Warehouse | Rớt kết nối tới POS → retry 3 lần, thất bại thì alert Kỹ sư dữ liệu | Dataset chuẩn hóa tại Data Warehouse |
| BR-04 | Giám sát trạng thái hệ thống | Kỹ sư vận hành | 1. Truy cập Grafana <br>2. Xem dashboard metrics (Pipeline, API, Model, Resource) | Mất kết nối Prometheus → cảnh báo khẩn qua PagerDuty/Slack | Dashboard giám sát real-time |
| BR-05 | Lập kế hoạch nhập hàng theo dự báo | Bộ phận Kho hàng | 1. Xem dự báo tổng hợp theo ngày/chi nhánh <br>2. Xuất báo cáo nhu cầu dự kiến | Thiếu dữ liệu chi nhánh → hiển thị cảnh báo độ tin cậy thấp | Báo cáo nhu cầu dự kiến 7 ngày |

## 5.2. Yêu cầu chức năng (Functional Requirements)

**Module 1: Data Pipeline (Thu thập & Xử lý dữ liệu)**

| ID | Yêu cầu | Mô tả |
|:---|:---|:---|
| FR-01 | Trích xuất dữ liệu POS tự động | Kết nối database POS tại 34 chi nhánh qua kênh mã hóa TLS, trích xuất giao dịch theo lịch batch hàng đêm (01:00 AM) |
| FR-02 | Làm sạch và chuẩn hóa dữ liệu | Xử lý giá trị khuyết, loại bỏ bản ghi trùng lặp, chuẩn hóa schema thống nhất giữa các chi nhánh |
| FR-03 | Nạp dữ liệu vào Data Warehouse | Ghi vào bảng staging, sau đó chuyển vào production tables theo quy trình ELT |
| FR-04 | Ghi log trạng thái pipeline | Số bản ghi vào/ra, tỷ lệ thành công, thời gian thực thi mỗi lần chạy batch |

**Module 2: AI Forecasting Engine (Mô hình dự báo)**

| ID | Yêu cầu | Mô tả |
|:---|:---|:---|
| FR-05 | Huấn luyện mô hình chuỗi thời gian | Dùng dữ liệu lịch sử tối thiểu 12 tháng; hỗ trợ tái huấn luyện định kỳ hàng tháng |
| FR-06 | Dự báo lưu lượng khách | Xuất dự báo theo từng khung giờ (1 giờ/slot), cho từng chi nhánh, trong 7 ngày tới |
| FR-07 | Nhận diện khung giờ cao điểm | Tự động gán nhãn peak cho khung giờ vượt ngưỡng 1,5 × lưu lượng trung bình của chi nhánh đó |
| FR-08 | Quản lý phiên bản mô hình | Lưu artifact theo phiên bản (Model Registry), hỗ trợ rollback khi mô hình mới cho kết quả kém hơn |
| FR-13 | So sánh đa mô hình (Model Benchmark) | Cho phép huấn luyện và đánh giá song song ≥ 4 phương pháp trên cùng bộ độ đo, lưu kết quả so sánh vào Model Registry |

**Module 3: API Service & Dashboard (Phân phối kết quả)**

| ID | Yêu cầu | Mô tả |
|:---|:---|:---|
| FR-09 | RESTful API dự báo | Endpoint `GET /api/v1/forecast/{branch_id}` trả kết quả dự báo 7 ngày dạng JSON; hỗ trợ filter theo ngày và khung giờ |
| FR-10 | RESTful API cảnh báo giờ cao điểm | Endpoint `GET /api/v1/alerts/{branch_id}` trả danh sách khung giờ đột biến kèm confidence score |
| FR-11 | Dashboard giám sát hệ thống | Hiển thị metrics pipeline, metrics API (latency P95, error rate) và metrics mô hình (MAPE, MAE) |
| FR-12 | Xác thực và phân quyền API | API Key/JWT cho mọi endpoint; phân quyền theo vai trò (RBAC) |

## 5.3. Yêu cầu phi chức năng (Non-Functional Requirements)

| Nhóm NFR | Yêu cầu | Ngưỡng đo lường (tiêu chí test) | KPI liên kết |
|:---|:---|:---|:---|
| **Hiệu năng** | Thời gian phản hồi API dự báo (P95) | ≤ 500 ms/request | **B.1** |
| **Hiệu năng** | Thời gian suy luận mô hình AI | ≤ 200 ms/chi nhánh | **A.4** |
| **Hiệu năng** | Thời gian xử lý Batch Job (34 chi nhánh) | ≤ 30 phút | **B.2** |
| **Sẵn sàng** | Uptime dịch vụ API | ≥ 99,9% (downtime ≤ 43,2 phút/tháng) | **B.3** |
| **Sẵn sàng** | Thời gian phát hiện sự cố (MTTD) | ≤ 15 phút | **B.7** |
| **Dữ liệu** | Tính đầy đủ bản ghi pipeline | ≥ 99,5% | **B.4** |
| **Dữ liệu** | Độ trễ đồng bộ dữ liệu batch | ≤ 24 giờ | **B.5** |
| **Chất lượng mô hình** | Sai số dự báo | MAPE < 15% (Pilot) → < 10% (+3 tháng); MAE ≤ 3 | **A.1, A.2** |
| **Chất lượng mô hình** | Ổn định đa ngữ cảnh | Δ MAPE ≤ 10% trên ≥ 4 bộ dữ liệu | **A.5** |
| **Bảo mật** | Mã hóa kết nối trích xuất dữ liệu | Bắt buộc TLS 1.2+ | Ràng buộc mục 2.2 |
| **Bảo mật** | Xác thực API | Bắt buộc API Key / JWT | FR-12 |
| **Mở rộng** | Hỗ trợ scale số lượng chi nhánh | Thêm lên 50 CN không cần đổi kiến trúc | Giả định mục 4 |
| **Tuân thủ** | Bảo mật thông tin cá nhân (PII) | Dữ liệu giao dịch được ẩn danh 100% | Ràng buộc NĐ13 |

---

# 6. Giải pháp đề xuất & kiến trúc (TO-BE, tích hợp, dữ liệu)

## 6.1. Quy trình nghiệp vụ TO-BE

1. **Thu thập (24/7):** khách hàng giao dịch tại hệ thống POS của chi nhánh.
2. **Đồng bộ & xử lý (01:00 AM mỗi ngày):** pipeline tự động rút dữ liệu từ POS về kho dữ liệu Cloud trung tâm, làm sạch, loại bỏ lỗi.
3. **Dự báo (02:00 AM):** AI Engine chạy Batch Inference cho 34 chi nhánh dựa trên dữ liệu mới nhất, lưu kết quả.
4. **Cảnh báo (tự động):** Alert Service quét kết quả dự báo; nếu phát hiện khung giờ vượt tải (> 150% lưu lượng trung bình), tự động push Webhook/Email.
5. **Ra quyết định (08:00 AM — điểm kiểm soát):** Quản lý chi nhánh gọi API dự báo, tham khảo kết quả để duyệt lịch phân ca và chuẩn bị kho bãi. **Con người chốt quyết định cuối cùng.**

**Sơ đồ quy trình TO-BE:**

```
 [Khách giao dịch tại POS]  ──── 24/7
            │
            ▼
 ┌──────────────────────────┐
 │ 01:00 Extract (TLS)      │  Airflow DAG: extract_pos
 │ POS DB 34 CN → S3 Raw    │
 └──────────┬───────────────┘
            ▼
 ┌──────────────────────────┐   Lỗi kết nối → retry ×3
 │ 01:15 Transform          │   → Alert Data Engineer
 │ Làm sạch, khử trùng lặp, │
 │ ẩn danh PII → PostgreSQL │
 └──────────┬───────────────┘
            ▼
      ┌─────┴──────┐
      ▼            ▼
┌───────────┐  ┌──────────────────┐
│ Train     │  │ 02:00 Predict    │
│ (hàng     │  │ Batch Inference  │
│  tháng)   │  │ 34 CN × 7 ngày   │
│ → MLflow  │  │ → Forecast_Result│
└───────────┘  └────────┬─────────┘
                        ▼
              ┌──────────────────┐   Gửi thất bại →
              │ Alert Service    │   noti trên Dashboard
              │ nếu > 1.5 × TB   │
              └────────┬─────────┘
                        ▼
   ◆ ĐIỂM KIỂM SOÁT 08:00 — Quản lý chi nhánh xem dự báo
     qua API/Dashboard → DUYỆT lịch phân ca & kế hoạch kho
     (quyết định cuối cùng thuộc về con người)
```

## 6.2. Kiến trúc hệ thống tổng thể (3 tầng)

```
┌─────────────── TẦNG TRÌNH BÀY (Presentation) ────────────────┐
│  Web Dashboard (DSS)  │  Grafana (IT)  │  Webhook / Email    │
└───────────────────────┬──────────────────────────────────────┘
                        │ HTTPS + JWT
┌───────────────────────▼──────────────────────────────────────┐
│                TẦNG ỨNG DỤNG (Application)                   │
│  API Gateway (JWT auth, Rate Limiting)                       │
│  ├── Forecast Service (FastAPI)                              │
│  ├── Alert Service (FastAPI)                                 │
│  └── Pipeline Orchestrator (Apache Airflow)                  │
└───────────────────────┬──────────────────────────────────────┘
                        │ Internal VPC
┌───────────────────────▼──────────────────────────────────────┐
│                   TẦNG DỮ LIỆU (Data)                        │
│  PostgreSQL (Data Warehouse)  │  MLflow (Model Registry)     │
│  Object Storage S3 (Raw Data) │  Prometheus + Loki           │
└──────────────────────────────────────────────────────────────┘
```

1. **Tầng Trình bày:** Web Dashboard cho Quản lý chi nhánh và Quản lý trung tâm; Grafana cho bộ phận IT; Webhook/Email Alert phân phối cảnh báo tự động.
2. **Tầng Ứng dụng:** API Gateway (xác thực JWT, Rate Limiting); Forecast Service (FastAPI); Alert Service (FastAPI); Pipeline Orchestrator (Apache Airflow).
3. **Tầng Dữ liệu:** Data Warehouse (PostgreSQL); Model Registry (MLflow); Prometheus + Loki; Object Storage (S3) cho dữ liệu thô và model artifacts.

## 6.3. Luồng xử lý Data Pipeline

1. **Extract:** 01:00 AM, Airflow trích xuất batch từ POS DB của 34 chi nhánh qua TLS; dữ liệu thô lưu tại Raw Zone trên S3.
2. **Transform:** làm sạch, chuẩn hóa, loại bỏ bản ghi trùng lặp hoặc không hợp lệ, ẩn danh trường PII; dữ liệu sạch nạp vào Clean Zone tại PostgreSQL.
3. **Train & Predict:** 
   - *Train:* DAG tái huấn luyện chạy theo chu kỳ hàng tháng; mô hình được phiên bản hóa tại MLflow Registry cùng bộ chỉ số A.1–A.5 để so sánh với phiên bản trước.
   - *Predict:* hàng đêm, DAG dự báo dùng mô hình mới nhất chạy batch inference; kết quả ghi về Data Warehouse (bảng `Forecast_Result`), sẵn sàng cho Forecast Service truy xuất.

## 6.4. Tích hợp hệ thống

| Hệ thống Nguồn / Đích | Giao thức | Tần suất | Dữ liệu trao đổi | Bảo mật |
|:---|:---|:---|:---|:---|
| POS DB → S3 | JDBC/ODBC qua TLS | Batch 1 lần/đêm | Giao dịch ẩn danh (lượng khách, thời gian, mã chi nhánh) | Mã hóa in-transit |
| S3 → Data Warehouse | Internal VPC | Theo luồng Extract | Dataset đã chuẩn hóa | Mã hóa at-rest (AES-256) |
| Forecast API → ERP | RESTful (HTTPS) | On-demand | JSON chứa mảng lượng khách dự báo theo slot giờ | JWT + RBAC |
| Prometheus → Grafana | Internal scrape | 15 giây/lần | Metrics hệ thống (Uptime, API Latency) | Nội bộ VPC |

---

# 7. Kế hoạch triển khai & tiến độ (WBS - Work Breakdown Structure)

| Pha | Tuần | Hoạt động chính | Deliverables | Tiêu chí hoàn thành | Owner |
|:---|:---:|:---|:---|:---|:---|
| **1. Khảo sát & Phân tích (SRS/BRD)** | T1–T3 | Thu thập dữ liệu POS lịch sử ≥ 12 tháng; phân tích chất lượng; làm sạch missing/duplicate | Data Dictionary; Dataset sạch | **B.4** ≥ 99,5%; Schema hợp lệ 100% | Kỹ sư Dữ liệu |
| **2. Thiết kế (HLD/LLD)** | T4–T5 | Thiết kế Data Pipeline; API Contract (OpenAPI); ERD; hạ tầng Cloud | HLD/LLD; API Contract; ERD; Terraform scripts | Kiến trúc được Sponsor và Key User duyệt 100% | Kiến trúc sư / Backend Lead |
| **3. Phát triển (Dev)** | T6–T10 | Code Airflow DAGs (ETL); thực nghiệm ≥ 4 mô hình, chọn mô hình tốt nhất; code API Services (FastAPI); tích hợp MLflow | Source code Pipeline & API; Artifact AI Model; báo cáo benchmark đa mô hình | **A.1** MAPE < 15%; **A.3** ≥ 85%; **A.4** ≤ 200 ms; **A.5** Δ ≤ 10% | Kỹ sư AI |
| **4. Kiểm thử (SIT/UAT)** | T11–T13 | Test tích hợp; **Load Test 500 CCU**; test bảo mật; đóng gói Docker; hỗ trợ UAT | Kịch bản test; báo cáo SIT; biên bản UAT (Sign-off) | **B.1** P95 ≤ 500 ms; **B.6** < 0,1%; **B.2** ≤ 30 phút; Pass UAT | Kỹ sư Kiểm thử (QA) |
| **5. Triển khai (Rollout/Ops)** | T14–T15 | Triển khai Kubernetes; cấu hình Grafana/Prometheus; Pilot 5 chi nhánh → rollout 34 chi nhánh | Hệ thống Live; Dashboard giám sát; Runbook | **B.3** ≥ 99,9%; **B.5** ≤ 24h; **B.7** ≤ 15 phút | Kỹ sư DevOps/SRE |
| **6. Vận hành & Bảo trì (Hypercare)** | T16–T19 | Hypercare 1 tháng; daily standup rà soát lỗi API và độ trễ dữ liệu; tái huấn luyện lần 1 | Báo cáo Hypercare; mô hình phiên bản 2 | Không có sự cố P0/P1 trong 14 ngày liên tục | SRE + ML Engineer |

*Tổng thời lượng phát triển: 15 tuần (~4 tháng), cộng 4 tuần Hypercare sau Go-live.*

---

# 8. Tổ chức nhân sự & cơ chế phối hợp (RACI)

## 8.1. Cơ cấu nhân sự

| Vai trò | Số lượng | Trách nhiệm chính |
|:---|:---:|:---|
| **Project Manager (PM)** | 1 | Quản lý rào cản, ngân sách, tiến độ; báo cáo Sponsor (Ban Giám đốc) |
| **Kỹ sư Dữ liệu (Data Engineer)** | 2 | Phát triển luồng ETL/ELT, duy trì Data Warehouse |
| **Kỹ sư AI (ML Engineer)** | 2 | Thực nghiệm, tinh chỉnh thuật toán và vận hành mô hình học máy |
| **Kỹ sư Backend (Backend Dev)** | 1 | Viết API, phân quyền, tối ưu response time |
| **Kỹ sư DevOps / SRE** | 1 | Hạ tầng Cloud, CI/CD, monitoring, bảo đảm SLA |
| **Kỹ sư Kiểm thử (QA)** | 1 | Test chất lượng, hiệu năng, điều phối UAT |
| **Key User (Quản lý chi nhánh)** | 2 | Cung cấp logic xếp ca thực tế, kiểm thử UAT và ký sign-off |

## 8.2. Ma trận phối hợp (RACI)

| Đầu việc chính | PM | Data Eng | ML Eng | Backend | SRE | QA | Key User |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Thu thập & làm sạch dữ liệu (Pha 1) | A | **R** | C | — | — | — | I |
| Chốt yêu cầu & thiết kế hệ thống (Pha 2) | A | C | C | **R** | **R** | — | I |
| Phát triển mô hình & API (Pha 3) | A | C | **R** | **R** | — | — | — |
| Duyệt UAT & ký Sign-off (Pha 4) | A | I | I | I | I | C | **R** |
| Triển khai Go-live (Pha 5) | A | — | — | C | **R** | — | I |
| Hypercare & tái huấn luyện (Pha 6) | A | C | **R** | — | **R** | — | I |
| Bàn giao tài liệu vận hành | **R** | C | C | C | **R** | — | A |

*(**R**: Thực hiện, **A**: Chịu trách nhiệm duyệt, **C**: Tham vấn, **I**: Nhận thông tin)*

## 8.3. Cơ chế làm việc & quản trị rủi ro

- **Họp tiến độ:** standup hàng tuần, Sprint review 2 tuần/lần; Milestone Review với Sponsor tại mốc kết thúc mỗi pha.
- **Quản lý thay đổi (Change Request):** nghiêm cấm scope creep. Mọi tính năng phát sinh ngoài mục 4 phải lập phiếu CR để PM tính toán chi phí/thời gian và trình duyệt.
- **Quản lý Issue/Risk:** tracking trên Jira. Rủi ro liên quan tới dữ liệu (bẩn, sai lệch) phải báo cho Data Engineer xử lý trong SLA ≤ 24h.

---

# 9. Dự toán chi phí & phương án tài chính

## 9.1. Chi phí đầu tư dự án (CAPEX) — giai đoạn 15 tuần

| Nhóm chi phí | Chi tiết hạng mục (giả định đơn giá) | Thành tiền (VNĐ) |
|:---|:---|---:|
| **Nhân công (Dev/Outsource)** | Lương khoán đội dự án (PM, Data, ML, BE, SRE, QA) trong 1–4 tháng tùy vị trí (trung bình 22tr/người/tháng, tổng ~27 người-tháng) | 594.000.000 |
| **Bản quyền (License)** | Sử dụng Open-source (Airflow, MLflow, FastAPI) | 0 |
| **Hạ tầng (giai đoạn phát triển)** | Thuê VM, GPU training, PostgreSQL, S3 môi trường Dev/Staging trong 4 tháng | 64.000.000 |
| **Đào tạo & Chuyển giao** | 2 buổi hướng dẫn đọc Dashboard cho Key Users | 5.000.000 |
| **Tổng CAPEX** | (chưa gồm dự phòng rủi ro 10%) | **663.000.000** |

## 9.2. Chi phí vận hành & bảo trì (OPEX) — 1 năm sau Go-live

| Nhóm chi phí | Chi tiết hạng mục | Thành tiền (VNĐ) |
|:---|:---|---:|
| **Hạ tầng (Cloud Server)** | K8s Cluster (96tr), PostgreSQL HA (54tr), S3 Storage (7,2tr), băng thông & DNS (6tr) | 163.200.000 |
| **Hạ tầng (GPU AI)** | GPU Spot Instances chạy job tái huấn luyện (1 lần/tháng) | 9.600.000 |
| **Nhân sự Ops / Hypercare** | Part-time SRE/Data Eng duy trì SLA, giám sát hệ thống | 132.000.000 |
| **Bảo mật & Tuân thủ** | Thuê bên thứ 3 Pentest đánh giá bảo mật API (2 lần/năm) | 20.000.000 |
| **Tổng OPEX / Năm 1** | (chưa gồm dự phòng rủi ro 10%) | **325.800.000** |

## 9.3. Tổng chi phí sở hữu (TCO) & phương án tài chính

- **Dự phòng rủi ro (Contingency 10%):** 98.880.000 VNĐ
- **TCO Năm 1 = CAPEX + OPEX + Contingency = 1.087.680.000 VNĐ**
- **TCO 3 năm (tham chiếu):** 663.000.000 + (325.800.000 × 3 × hệ số trượt giá 1,05 trung bình) + dự phòng ≈ **1.790.000.000 VNĐ**
- **Phương án tài chính:** chuyển hóa 100% chi phí hạ tầng máy chủ thành OPEX hàng tháng (thuê Cloud) thay vì mua thiết bị vật lý. Tiết kiệm phí license qua hệ sinh thái mã nguồn mở.

## 9.4. Ghi chú về chồng lấn chi phí với đồ án môn học

Hai đề tài được dự toán **độc lập**, mỗi bài giả định triển khai riêng lẻ. Nếu doanh nghiệp phê duyệt cả hai và triển khai đồng thời, chi phí **không được cộng dồn** ở các hạng mục sau:

| Hạng mục | Thực hành (độc lập) | Đồ án (nền tảng) | Khi triển khai chung |
|:---|---:|---:|:---|
| Hạ tầng Cloud (K8s, PostgreSQL, S3, băng thông) | 163.200.000/năm | Đã bao gồm trong OPEX nền tảng | Hấp thụ vào OPEX nền tảng → **thực hành giảm 163,2tr/năm** |
| GPU tái huấn luyện AI | 9.600.000/năm | 9.600.000/năm | Dùng chung → tính **1 lần** |
| Nhân sự Ops part-time | 132.000.000/năm | Đã có DevOps/SRE full-time + Data Eng | Hấp thụ một phần → giảm ~50% |
| Phát triển mô hình AI | 663.000.000 (CAPEX) | 90.000.000 — chỉ **tích hợp & triển khai** Inference Service, không bao gồm nghiên cứu mô hình | Không trùng lặp |

**TCO năm 1 của bài thực hành trong kịch bản triển khai chung: ~925.000.000 VNĐ** (thay vì 1.087.680.000 VNĐ).

## 9.5. Kiểm chứng tính nhất quán chi phí (phân bổ theo giai đoạn)

| Kế hoạch WBS | Phí nhân công (VNĐ) | Phí hạ tầng/khác (VNĐ) | Tổng cộng (VNĐ) |
|:---|---:|---:|---:|
| Pha 1: Khảo sát & Phân tích | 134.000.000 | 10.500.000 | 144.500.000 |
| Pha 2: Thiết kế (HLD/LLD) | 75.000.000 | 7.000.000 | 82.000.000 |
| Pha 3: Phát triển (Dev) | 265.000.000 | 30.500.000 | 295.500.000 |
| Pha 4: Kiểm thử (SIT/UAT) | 95.000.000 | 10.500.000 | 105.500.000 |
| Pha 5: Triển khai (Go-live) | 25.000.000 | 10.500.000 | 35.500.000 |
| **Kiểm chứng tổng (khớp)** | **594.000.000** | **69.000.000** | **663.000.000** |

> Pha 6 (Hypercare) được tính vào OPEX năm 1, không thuộc CAPEX.

---

# 10. Rủi ro, chất lượng, kiểm thử, quản lý thay đổi

## 10.1. Quản trị rủi ro (Risk Register)

| Mã | Rủi ro | Xác suất | Ảnh hưởng | Mức độ | Biện pháp giảm thiểu | Owner |
|:---|:---|:---:|:---:|:---:|:---|:---|
| R01 | **Dữ liệu POS bẩn / thiếu hụt:** máy POS mất kết nối hoặc nhân viên nhập sai | Cao | Cao | **Cao** | Cơ chế làm sạch tự động (Fill NA/Drop Outliers) trong Data Pipeline; cảnh báo Data Quality cho Key User xử lý thủ công | Kỹ sư Dữ liệu |
| R02 | **Mô hình không đạt ngưỡng MAPE cam kết** trên dữ liệu thực | Trung bình | Cao | **Cao** | Thực nghiệm song song ≥ 4 phương pháp (TSFM, LSTM/BiLSTM, Prophet, ARIMA) và chọn phương pháp tốt nhất; nếu không đạt, phát hành chế độ beta không ràng buộc nghiệm thu, giữ Moving Average làm fallback, lập CR gia hạn G3 | Kỹ sư AI |
| R03 | **Data Drift:** hành vi khách hàng thay đổi đột ngột (thời tiết, sự kiện) làm giảm độ chính xác | Trung bình | Cao | **Cao** | Ngưỡng cảnh báo MAPE > 15% tự động kích hoạt tiến trình tái huấn luyện; giám sát A.5 theo tháng | Kỹ sư AI |
| R04 | **Scope Creep:** Quản lý chi nhánh yêu cầu bổ sung tính năng quản lý nhân sự | Trung bình | Trung bình | **Vừa** | Kiểm soát qua quy trình Change Request; Sponsor duyệt mọi chi phí phát sinh | PM |
| R05 | **Nghẽn tải lúc 08:00 AM:** 34 chi nhánh cùng gọi API lấy dự báo | Thấp | Cao | **Vừa** | Auto-scaling trên Kubernetes; Rate Limiting tại API Gateway; cache kết quả dự báo | SRE / DevOps |
| R06 | **Key User không tham gia UAT đúng tiến độ** | Trung bình | Trung bình | **Vừa** | Chốt lịch UAT từ Pha 2; chọn 2 Key User có cam kết; chuẩn bị kịch bản test sẵn để rút ngắn thời gian | PM |

## 10.2. Kế hoạch kiểm thử và đảm bảo chất lượng (QA/QC)

| Loại kiểm thử | Kịch bản | Tiêu chí Pass |
|:---|:---|:---|
| **Data Testing** | Kiểm tra tính toàn vẹn Data Pipeline | 100% schema hợp lệ; ≥ 99,5% bản ghi luân chuyển thành công |
| **Model Testing** | Backtesting trên dữ liệu lịch sử | MAPE < 15% (Pilot); MAE ≤ 3; Precision ≥ 85%; Δ MAPE ≤ 10% trên ≥ 4 bộ dữ liệu |
| **Load / Stress Testing** | Dùng JMeter giả lập **500 CCU** truy cập đồng thời vào API | P95 Latency ≤ 500 ms; HTTP 5xx < 0,1% |
| **Security Testing** | Pentest API, kiểm tra xác thực JWT/API Key, quét TLS | 0 lỗ hổng Critical/High; không tồn tại kết nối không mã hóa |
| **UAT** | Key User vận hành thử trên môi trường Staging | Pass 100% test case Critical/High; ký biên bản Sign-off trước Go-live |

> **Lưu ý thống nhất:** ngưỡng tải chuẩn cho toàn bộ kế hoạch kiểm thử là **500 CCU** (áp dụng đồng nhất tại Pha 4 mục 7 và tại mục này).

## 10.3. Quản lý thay đổi (Change Management)

- **Truyền thông:** thông báo toàn hệ thống Ways Station trước Go-live 2 tuần về hệ thống DSS mới.
- **Đào tạo:** 2 buổi workshop online cho Quản lý chi nhánh về cách đọc Dashboard và sử dụng số liệu dự báo để xếp ca.
- **Tài liệu:** User Manual dạng video ngắn và file PDF, tích hợp sẵn trong mục Help của phần mềm.

---

# 11. Vận hành – bảo trì – chuyển giao

## 11.1. Mô hình vận hành và hỗ trợ (Hypercare)

- **Giai đoạn Hypercare (1 tháng sau Go-live):** đội dự án duy trì hỗ trợ mức cao nhất, daily standup lúc 09:00 AM rà soát lỗi API và độ trễ dữ liệu.
- **Quy trình hỗ trợ ITSM (Tier 1-2-3):**
  - Tier 1: Helpdesk nội bộ tiếp nhận ticket.
  - Tier 2: vấn đề dữ liệu/API đẩy cho đội IT nội bộ của Ways Station.
  - Tier 3: vấn đề lõi AI/hạ tầng đẩy về đội dự án (SRE/ML Eng). SLA xử lý lỗi nghiêm trọng ≤ 4 giờ.

## 11.2. Giám sát hệ thống và an toàn dữ liệu

- **Monitoring & Alerting:** Grafana giám sát 3 metrics chính (Pipeline Freshness, API Latency, Model MAPE); cảnh báo khẩn qua PagerDuty/Slack nếu Uptime < 99,9% hoặc MTTD vượt 15 phút.
- **Backup & Disaster Recovery:**
  - **Nguyên tắc sao lưu 3-2-1:** sao lưu Data Warehouse (PostgreSQL) tự động hàng ngày, có bản lưu cục bộ và bản đồng bộ lên Cloud Storage cách ly.
  - DR Drill 6 tháng/lần, đảm bảo RPO < 24h và RTO < 4h.

## 11.3. Lộ trình nâng cấp 6–12 tháng

| Mốc | Nội dung |
|:---|:---|
| +3 tháng | Siết ngưỡng MAPE xuống < 10%; bổ sung biến ngoại sinh (thời tiết, ngày lễ) vào mô hình |
| +6 tháng | Mở rộng dự báo từ lưu lượng khách sang dự báo doanh thu và nhu cầu vật tư F&B |
| +12 tháng | Chuyển từ batch inference sang near-real-time nếu nền tảng CDC của đồ án đã go-live |

## 11.4. Bàn giao và chuyển giao công nghệ

- Mã nguồn Data Pipeline, AI Model và API Services (trên GitLab).
- Tài khoản quản trị Cloud (AWS/GCP), MLflow, Airflow.
- Tài liệu Kiến trúc (HLD/LLD), Sổ tay vận hành (Runbook) cho các kịch bản xử lý sự cố thường gặp.
- Báo cáo benchmark đa mô hình (kết quả thực nghiệm ≥ 4 phương pháp) làm cơ sở cho các lần tái huấn luyện sau.

---

# 12. Nghiệm thu & đánh giá hiệu quả

## 12.1. Tiêu chí nghiệm thu hệ thống

1. Báo cáo UAT có chữ ký xác nhận của đại diện Quản lý chi nhánh (Pass 100% test case mức Critical/High).
2. Hệ thống hoạt động ổn định trên Production tối thiểu 14 ngày liên tục, không có sự cố gián đoạn mức nghiêm trọng (P0/P1).
3. Biên bản đo lường SLA đạt chuẩn: **B.3** Uptime ≥ 99,9%; **B.1** API P95 ≤ 500 ms; **B.6** Error Rate < 0,1%.
4. Mô hình đạt **A.1** MAPE < 15%, **A.2** MAE ≤ 3, **A.3** Precision ≥ 85%, **A.5** Δ ≤ 10% tại thời điểm nghiệm thu.

## 12.2. Đo lường hiệu quả nghiệp vụ (Benefit Realization)

Đo lại toàn bộ KPI tại mốc **+1 tháng, +3 tháng, +6 tháng** sau Go-live, theo đúng owner quy định tại mục 3.2:

| Mốc | Nội dung đo | Người chịu trách nhiệm |
|:---|:---|:---|
| +1 tháng | B.1, B.2, B.3, B.5, B.6 — hệ thống vận hành ổn định | SRE, Backend Dev, Data Engineer |
| +3 tháng | **A.1 phải đạt < 10%**; A.2, A.3; B.4, B.7; chỉ số tối ưu nhân sự: giảm bao nhiêu % chi phí giờ công tại khung giờ thấp điểm | ML Engineer + PM |
| +6 tháng | A.5 (độ ổn định qua các mùa vụ); chỉ số chất lượng dịch vụ: tỷ lệ khách phải chờ trong giờ cao điểm có giảm không (khảo sát tại cửa hàng); đánh giá tần suất cần tái huấn luyện | PM + Sponsor |

---

# Phụ lục A — Thiết kế dữ liệu (ERD High-level)

| Thực thể | Thuộc tính chính | Mô tả |
|:---|:---|:---|
| **Branch** | `branch_id` (PK), `branch_name`, `branch_type`, `region` | Danh mục chi nhánh (Master Data) |
| **Transaction_Hourly** | `id` (PK), `branch_id` (FK), `date`, `hour_slot`, `customer_count` | Dữ liệu lượng khách thực tế tổng hợp theo giờ |
| **Forecast_Result** | `id` (PK), `branch_id` (FK), `forecast_date`, `hour_slot`, `predicted_count`, `is_peak`, `model_id` (FK) | Kết quả xuất ra từ mô hình dự báo AI |
| **Model_Metadata** | `model_id` (PK), `version`, `algorithm`, `mape_score`, `mae_score`, `precision_score`, `delta_stability`, `status` | Thông tin lịch sử độ chính xác và ổn định của từng phiên bản mô hình |

**Quan hệ:** `Branch` 1—n `Transaction_Hourly`; `Branch` 1—n `Forecast_Result`; `Model_Metadata` 1—n `Forecast_Result`.

**Quy tắc chuẩn hóa / mã hóa danh mục:**
- Khóa định danh chi nhánh: `WS-{TYPE}-{NNN}` (ví dụ `WS-GYM-001`).
- Khóa thời gian (hour slot): số nguyên 0–23 theo chu kỳ 24h.
- Trường `algorithm` ghi nhận phương pháp thực tế được chọn sau benchmark (phục vụ phương án kỹ thuật dự phòng mục 4.3).

---

# Phụ lục B — Ma trận phân quyền (RBAC)

| Vai trò (Role) | Xem dự báo chi nhánh mình | Xem dự báo toàn hệ thống | Xem Dashboard giám sát | Cấu hình ngưỡng cảnh báo | Quản lý mô hình AI | Quản lý Pipeline |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Quản lý chi nhánh | ✓ | — | — | — | — | — |
| Quản lý trung tâm / Điều phối | ✓ | ✓ | ✓ | ✓ | — | — |
| Bộ phận Kho hàng | ✓ | ✓ | — | — | — | — |
| Kỹ sư AI (ML Engineer) | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Kỹ sư Dữ liệu (DE) | — | — | ✓ | — | — | ✓ |
| Kỹ sư DevOps/SRE | — | — | ✓ | ✓ | — | ✓ |

---

# Phụ lục C — Mockup giao diện Dashboard dự báo

```
┌────────────────────────────────────────────────────────────────┐
│  WAYS STATION — DỰ BÁO LƯU LƯỢNG KHÁCH          [ Đăng xuất ]  │
├────────────────────────────────────────────────────────────────┤
│  Chi nhánh: [ WS-GYM-001  ▾ ]   Khoảng: [ 7 ngày tới  ▾ ]      │
├────────────────────────────────────────────────────────────────┤
│  Khách/giờ                                                     │
│   60│                        ▓▓                                │
│   45│                    ▓▓  ▓▓  ▓▓         ← ngưỡng peak 1.5× │
│   30│  ──────────────▓▓──▓▓──▓▓──▓▓──▓▓───────────────────     │
│   15│      ▒▒  ▒▒  ▒▒▓▓  ▓▓  ▓▓  ▓▓  ▓▓  ▒▒  ▒▒               │
│    0└──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──         │
│       06  08  10  12  14  16  18  20  22  00  02  04           │
│       ▓▓ Giờ cao điểm (peak)    ▒▒ Giờ thường                  │
├────────────────────────────────────────────────────────────────┤
│  ⚠ CẢNH BÁO: 18:00–21:00 ngày 20/09 — dự báo 58 khách          │
│    (vượt 1.8× trung bình). Độ tin cậy: 87%                     │
│    → Đề xuất tham khảo: bố trí thêm nhân sự ca chiều           │
│    [ Quyết định phân ca do Quản lý chi nhánh duyệt ]           │
├────────────────────────────────────────────────────────────────┤
│  Độ chính xác mô hình hiện tại: MAPE 9.2% | MAE 2.4 khách      │
│  Dữ liệu cập nhật lúc: 02:00 AM hôm nay                        │
└────────────────────────────────────────────────────────────────┘
```

---

# Phụ lục D — Danh mục thuật ngữ (Glossary)

| Thuật ngữ | Viết tắt | Giải nghĩa |
|:---|:---|:---|
| Application Programming Interface | API | Giao diện lập trình ứng dụng, cho phép các phần mềm giao tiếp với nhau |
| Capital Expenditure | CAPEX | Chi phí đầu tư ban đầu |
| Change Data Capture | CDC | Kỹ thuật bắt sự kiện thay đổi dữ liệu để đồng bộ thời gian thực |
| Concurrent Users | CCU | Số người dùng truy cập đồng thời |
| Decision Support System | DSS | Hệ thống hỗ trợ ra quyết định |
| Directed Acyclic Graph | DAG | Đồ thị có hướng không chu trình — đơn vị luồng công việc trong Airflow |
| Disaster Recovery | DR | Khôi phục sau thảm họa |
| Entity Relationship Diagram | ERD | Sơ đồ quan hệ thực thể |
| Extract, Transform, Load | ETL | Quy trình trích xuất – chuyển đổi – nạp dữ liệu |
| High-Level / Low-Level Design | HLD/LLD | Thiết kế mức cao / mức chi tiết |
| JSON Web Token | JWT | Chuẩn token dùng để xác thực API |
| Mean Absolute Error | MAE | Sai số tuyệt đối trung bình |
| Mean Absolute Percentage Error | MAPE | Sai số phần trăm tuyệt đối trung bình |
| Mean Time To Detect | MTTD | Thời gian trung bình phát hiện sự cố |
| Operational Expenditure | OPEX | Chi phí vận hành định kỳ |
| Personally Identifiable Information | PII | Thông tin định danh cá nhân |
| Point of Sale | POS | Hệ thống bán hàng tại điểm giao dịch |
| Recovery Point / Time Objective | RPO / RTO | Mục tiêu điểm khôi phục / thời gian khôi phục |
| Role-Based Access Control | RBAC | Phân quyền theo vai trò |
| Service Level Agreement | SLA | Cam kết mức độ dịch vụ |
| Site Reliability Engineering | SRE | Kỹ thuật độ tin cậy hệ thống |
| System Integration / User Acceptance Testing | SIT / UAT | Kiểm thử tích hợp hệ thống / kiểm thử chấp nhận người dùng |
| Time-Series Foundation Model | TSFM | Mô hình nền tảng cho dữ liệu chuỗi thời gian |
| Total Cost of Ownership | TCO | Tổng chi phí sở hữu |
| Transport Layer Security | TLS | Giao thức mã hóa đường truyền |
| Work Breakdown Structure | WBS | Cấu trúc phân rã công việc |

---

# Phụ lục E — Danh mục tài liệu tham khảo

[1] Scikit-Learn (n.d.), *Mean absolute percentage error*, https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-percentage-error
[2] Scikit-Learn (n.d.), *Mean absolute error*, https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-error
[3] Powers, D. M. W. (2011), *Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation*, Journal of Machine Learning Technologies, 2(1), pp. 37–63. *(Cơ sở cho độ đo Precision — KPI A.3)*
[4] Google Cloud (n.d.), *Site Reliability Engineering — Availability Table and Metrics*, https://sre.google/sre-book/availability-table/
[5] ISO/IEC (2008), *ISO/IEC 25012: Data quality model*, https://www.iso.org/standard/35736.html
[6] AWS (2021), *Amazon Builders' Library: Latency and Percentiles*, https://aws.amazon.com/builders-library/latency-and-percentiles/
[7] Google Cloud (n.d.), *Site Reliability Engineering — Error Rates*, https://sre.google/sre-book/service-level-objectives/#error-rate-metrics
[8] Hyndman, R. J. & Athanasopoulos, G. (2021), *Forecasting: Principles and Practice*, 3rd edition, OTexts: Melbourne, Australia, https://otexts.com/fpp3/ *(Cơ sở toán học cho các độ đo lỗi dự báo chuỗi thời gian MAPE, MAE và baseline ARIMA/Moving Average)*
[9] Google Cloud (n.d.), *Kubernetes Engine Documentation*, https://cloud.google.com/kubernetes-engine/docs
[10] Apache Software Foundation (n.d.), *Apache Airflow Documentation*, https://airflow.apache.org/docs/
[11] MLflow (n.d.), *MLflow Documentation — Model Registry*, https://mlflow.org/docs/latest/model-registry.html
[12] PMI (2021), *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*, 7th Edition, Project Management Institute.
[13] Chính phủ Việt Nam (2023), *Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân*.
