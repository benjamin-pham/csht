# Bài Thực Hành: Ứng Dụng Mô Hình AI Dự Báo Lưu Lượng Khách Hàng Dành Cho Chuỗi Ways Station

## Bước 0 — Chuẩn bị đầu vào
- **Bối cảnh:** Chuỗi Ways Station có nhu cầu vận hành đa chi nhánh, đòi hỏi khả năng phản ứng nhanh với sự biến động của khách hàng trong ngày.
- **Vấn đề hiện tại:** Việc phân tích và dự báo số lượng khách hàng tại mỗi chi nhánh hiện được thực hiện thủ công. Cơ sở dữ liệu giao dịch rời rạc, chưa được làm sạch, thiếu luồng xử lý tự động. Hạ tầng hiện hữu không đáp ứng đủ năng lực tính toán để huấn luyện các mô hình học máy.
- **Đối tượng sử dụng:** Hệ thống dữ liệu tập trung (Data Warehouse), máy chủ dịch vụ API.
- **Hệ thống liên quan:** Hệ thống POS tại chi nhánh, phần mềm ERP và các nền tảng báo cáo nội bộ.
- **Ràng buộc:** Giới hạn cấu hình hạ tầng hiện có, yêu cầu cao về tính sẵn sàng và tính bảo mật của luồng dữ liệu (Data Pipeline).

## Bước 1 — Viết Tên đề tài + Thông tin chung
- **Tên đề tài:** Ứng dụng mô hình AI Time-Series Forecasting dự báo lưu lượng khách hàng đa chi nhánh.
- **Thông tin chung:** Đơn vị chủ trì: Nhóm 5. Phạm vi triển khai: Nền tảng hạ tầng tính toán Cloud và luồng dữ liệu của chuỗi Ways Station.

## Bước 2 — Bối cảnh & Lý do chọn đề tài (Business Case)

### 2.1. Hiện trạng vận hành & Điểm nghẽn hệ thống
- **Dữ liệu phân tán và độ trễ cao:** Toàn bộ dữ liệu giao dịch POS tại 34 chi nhánh của Ways Station hiện được xử lý thủ công và lưu trữ phân tán, dẫn đến độ trễ tổng hợp dữ liệu từ 48 đến 72 giờ.
- **Hoạch định tài nguyên bị động theo kinh nghiệm:** Do thiếu công cụ dự báo định lượng theo chuỗi thời gian, việc điều phối nguồn lực tại các chi nhánh phụ thuộc hoàn toàn vào cảm tính:
  - *Khung giờ cao điểm:* Thiếu hụt nhân lực phục vụ và gián đoạn nguồn cung vật tư, kéo dài thời gian chờ đợi của khách hàng và làm suy giảm chất lượng dịch vụ.
  - *Khung giờ thấp điểm:* Dư thừa nhân lực phân bổ cố định, gây lãng phí nghiêm trọng chi phí vận hành (OPEX).
- **Hạn chế hạ tầng tính toán cục bộ:** Máy chủ tại chi nhánh không đủ năng lực tính toán để làm sạch, trích xuất đặc trưng và huấn luyện các mô hình học máy trên tập dữ liệu lịch sử lớn.

### 2.2. Động lực đầu tư & Giá trị hệ thống mang lại
Xây dựng hệ thống dự báo lưu lượng khách hàng theo chuỗi thời gian (AI Time-Series Forecasting) kết hợp đường ống dữ liệu tự động (Automated Data Pipeline) đóng vai trò là **Hệ thống hỗ trợ ra quyết định (Decision Support System - DSS)**, mang lại các giá trị cốt lõi:
1. **Hỗ trợ tối ưu hóa điều phối nhân lực:** Cung cấp dữ liệu dự báo lưu lượng khách theo từng khung giờ trong ngày, làm cơ sở định lượng giúp bộ phận điều phối thiết lập ca làm việc linh hoạt, hạn chế giờ công dư thừa vào giờ vắng và bảo đảm đủ nhân lực trong giờ cao điểm.
2. **Hỗ trợ kế hoạch điều phối cung ứng:** Đưa ra dự báo nhu cầu phục vụ sát thực tế, hỗ trợ bộ phận kho vận lập kế hoạch luân chuyển hàng hóa kịp thời, hạn chế tình trạng đứt gãy cung ứng hoặc tồn đọng hàng hóa quá hạn.
3. **Cung cấp dữ liệu định hướng kế hoạch tiếp thị:** Nhận diện chính xác các khung giờ thấp điểm định kỳ để gợi ý thời điểm kích cầu dịch vụ, tránh việc triển khai khuyến mãi lãng phí vào các khung giờ đã đạt ngưỡng phục vụ tối đa.

### 2.3. Ưu thế kiến trúc kỹ thuật & Cam kết vận hành
- **Tối ưu chi phí nhờ nền tảng Cloud:** Chuyển đổi mô hình đầu tư từ mua sắm máy chủ vật lý tốn kém (CAPEX) sang thuê dịch vụ điện toán đám mây linh hoạt (OPEX).
- **Khả năng tự động co giãn (Auto-scaling):** Hạ tầng Cloud tự động mở rộng tài nguyên khi lưu lượng gọi API tăng vọt và thu hẹp khi tải giảm, bảo đảm hệ thống vận hành liên tục mà không bị nghẽn tải.
- **Cam kết mức độ dịch vụ kỹ thuật (SLA):** Đảm bảo tính sẵn sàng của dịch vụ API đạt Uptime $\ge 99.9\%$ (thời gian gián đoạn dịch vụ tối đa dưới 43.2 phút/tháng), thời gian phản hồi ở mức mili-giây và dữ liệu được bảo vệ an toàn theo các chuẩn mực bảo mật thông tin.

## Bước 3 — Mục tiêu, KPI và tiêu chí thành công

### 3.1. Mục tiêu tổng quát
Xây dựng nền tảng tích hợp tự động thu thập dữ liệu giao dịch, huấn luyện mô hình học máy (Machine Learning) để phân tích chuỗi thời gian, và triển khai dự báo thông qua các API chuyên dụng phục vụ nội bộ.

### 3.2. Mục tiêu cụ thể và KPI Kỹ thuật (Phân tách 2 nhóm độc lập theo định hướng kỹ thuật)
Toàn bộ hệ thống phần mềm không áp dụng các KPI phân rã theo tầng hạ tầng/mạng của đồ án, mà được phân tách rõ ràng thành **2 nhóm chỉ số KPI độc lập**:

#### Nhóm A: KPI Mô hình Trí tuệ nhân tạo (AI Model KPIs)
Đo lường năng lực và độ chính xác của mô hình học máy chuỗi thời gian (Time-Series Forecasting) so với baseline thủ công:

1. **Sai số tỷ lệ phần trăm tuyệt đối trung bình (MAPE - Mean Absolute Percentage Error):**
   - *KPI:* $\text{MAPE} < 10\%$ trên tập dữ liệu kiểm thử (Test set).
   - *Công thức:*
     $$\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%$$
   - *Diễn giải & Phương pháp tính:* Đo lường mức độ chênh lệch phần trăm giữa lưu lượng khách thực tế ($y_i$) và lưu lượng dự báo ($\hat{y}_i$). Giá trị $< 10\%$ khẳng định mô hình đạt độ chính xác dự báo tương đương $> 90\%$.
   - *Baseline đối chứng:* Phương pháp dự báo truyền thống Moving Average 7 ngày cho MAPE ước tính ~25-30%; mô hình ARIMA(1,1,1) cho MAPE ước tính ~18-22% (theo khảo sát vận hành và tham khảo nghiên cứu của Hyndman & Athanasopoulos [[8]](#ref8)). Mô hình AI cam kết **cải thiện sai số tối thiểu 10%** so với phương pháp Baseline tốt nhất và duy trì **độ chênh lệch hiệu suất $\Delta \le 10\%$** giữa các ngữ cảnh dữ liệu khác nhau (chi nhánh Gym vs Gaming vs Hub) trên tối thiểu 4 bộ dữ liệu kiểm thử.
   - *Trích dẫn:* Scikit-Learn, *Mean absolute percentage error* [1].

2. **Sai số tuyệt đối trung bình (MAE - Mean Absolute Error):**
   - *KPI:* $\text{MAE} \le 3$ khách/chi nhánh/khung giờ.
   - *Công thức:*
     $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
   - *Diễn giải & Phương pháp tính:* Phản ánh độ lệch số lượng khách cụ thể trong mỗi khung giờ, đảm bảo sai số không gây ảnh hưởng lớn đến việc tham khảo xếp ca.
   - *Trích dẫn:* Scikit-Learn, *Mean absolute error* [2].

3. **Độ chính xác nhận diện khung giờ cao điểm (Peak Traffic Detection Precision):**
   - *KPI:* $\text{Precision} \ge 85\%$ đối với các khung giờ có lưu lượng đột biến vượt ngưỡng $1.5 \times \text{lưu lượng trung bình}$.
   - *Công thức:*
     $$\text{Precision} = \frac{TP}{TP + FP}$$
   - *Diễn giải & Phương pháp tính:* Trong tập kiểm thử gồm các trường hợp được mô hình nhận diện là giờ cao điểm, ít nhất $85\%$ số trường hợp đó thực sự là giờ cao điểm trong thực tế ($TP$), hạn chế tối đa các trường hợp báo động giả ($FP$).
   - *Trích dẫn:* Powers, D. M. W. (2011), *Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation* [3].

4. **Thời gian suy luận của mô hình (Inference Latency):**
   - *KPI:* $\le 200\text{ms}$ cho mỗi chu kỳ suy luận dự báo của 1 chi nhánh.

---

#### Nhóm B: KPI Phần mềm & Vận hành hệ thống (Software & Operational KPIs)
Đo lường tính sẵn sàng, độ tin cậy và chất lượng kỹ thuật của ứng dụng phần mềm dự báo trong môi trường vận hành:

1. **Thời gian đáp ứng của dịch vụ API (API Response Time):**
   - *KPI:* Thời gian phản hồi API thời gian thực $\le 500\text{ms}$ ở phân vị thứ 95 ($P95$); thời gian xử lý toàn bộ dữ liệu dự báo theo lô định kỳ ban đêm (Batch Job) $\le 30$ phút.
   - *Công thức:* $P95 \le 500\text{ms}$ (Đảm bảo 95% tổng số lượng request có thời gian xử lý và trả kết quả dưới 500ms).
   - *Trích dẫn:* AWS (2021), *Latency and Percentiles* [6].

2. **Tính sẵn sàng của dịch vụ phần mềm (Software Availability / Uptime):**
   - *KPI:* $\text{Uptime} \ge 99.9\%$ (tổng thời gian gián đoạn dịch vụ API tối đa không quá 43.2 phút/tháng).
   - *Công thức:* $\text{Uptime} = \frac{\text{Tổng thời gian vận hành (Total Time)} - \text{Thời gian gián đoạn (Downtime)}}{\text{Tổng thời gian vận hành (Total Time)}} \times 100\%$
   - *Trích dẫn:* Google Cloud, *Site Reliability Engineering - Availability Metrics* [4].

3. **Chất lượng và độ toàn vẹn của luồng dữ liệu (Data Pipeline Quality):**
   - *KPI Tính đầy đủ (Completeness):* $\ge 99.5\%$ bản ghi giao dịch POS được trích xuất, làm sạch và nạp thành công vào Data Warehouse.
   - *Công thức tính đầy đủ:* $\text{Completeness} = \frac{\text{Số lượng bản ghi nạp thành công}}{\text{Tổng số bản ghi gốc tại POS}} \times 100\%$
   - *KPI Tính kịp thời (Data Freshness):* Độ trễ luồng dữ liệu $\le 24$ giờ (hoàn tất đồng bộ dữ liệu lúc 01:00 AM mỗi ngày).
   - *Công thức tính kịp thời:* $\Delta t_{freshness} = t_{\text{Data Warehouse}} - t_{\text{POS}} \le 24\text{h}$
   - *Lưu ý phân biệt với Đồ án:* Đồ án hạ tầng cam kết Data Freshness $\le 5s$ (real-time streaming qua CDC) cho toàn bộ nền tảng dữ liệu tập trung. Tại bài Thực hành, luồng huấn luyện mô hình AI sử dụng kiến trúc Batch Processing xử lý dữ liệu lịch sử theo lô hàng đêm (không yêu cầu real-time) nên mục tiêu $\le 24\text{h}$ là phù hợp với đặc thù bài toán dự báo chuỗi thời gian.
   - *Trích dẫn:* ISO/IEC 25012: Data quality model [5].

4. **Tỷ lệ lỗi dịch vụ (API Error Rate):**
   - *KPI:* Tỷ lệ lỗi máy chủ (HTTP 5xx) $< 0.1\%$ trên tổng số lượt gọi API.
   - *Công thức:* $\text{Error Rate} = \frac{\text{Số lượng phản hồi lỗi (HTTP 5xx)}}{\text{Tổng số lượng request đến API}} \times 100\%$
   - *Trích dẫn:* Google Cloud, *Site Reliability Engineering - Error Rates* [7].

---

### 3.3. Ánh xạ KPI theo từng giai đoạn triển khai và tiêu chí bàn giao
Nhằm đảm bảo tính xuyên suốt từ thiết kế đến nghiệm thu và dự toán chi phí, KPI kỹ thuật được phân bổ cụ thể làm tiêu chí nghiệm thu bàn giao qua 5 giai đoạn phát triển phần mềm:

| Giai đoạn triển khai | Hoạt động kỹ thuật & Yêu cầu | Sản phẩm bàn giao (Deliverables) | KPI nghiệm thu giai đoạn | Nhân sự phụ trách |
| :--- | :--- | :--- | :--- | :--- |
| **G1: Khảo sát & Phân tích dữ liệu** | Thu thập dữ liệu lịch sử POS, chuẩn hóa schema, làm sạch dữ liệu khuyết thiếu. | Tài liệu đặc tả dữ liệu, Dataset đã làm sạch. | Tính đầy đủ dữ liệu $\ge 99.5\%$, Schema hợp lệ $100\%$. | Kỹ sư Dữ liệu (Data Engineer) |
| **G2: Thiết kế kiến trúc phần mềm** | Thiết kế Data Pipeline, cấu trúc Web Service RESTful API và mô hình AI. | Tài liệu thiết kế kiến trúc, API Contract. | $100\%$ API đạt chuẩn RESTful, kiến trúc sẵn sàng mở rộng. | Kiến trúc sư Phần mềm (Software Architect) |
| **G3: Phát triển mô hình & Pipeline** | Xây dựng đường ống ETL tự động; huấn luyện và tinh chỉnh mô hình TSFM. | Mã nguồn Data Pipeline, Artifact mô hình AI đã huấn luyện. | $\text{MAPE} < 10\%$, $\text{Precision} \ge 85\%$, Inference Latency $\le 200\text{ms}$. | Kỹ sư AI (Machine Learning Engineer) |
| **G4: Kiểm thử & Đóng gói phần mềm** | Kiểm thử tích hợp (Integration Test), tải (Load Test), đóng gói Container. | Docker Image, Bộ kịch bản Test, Báo cáo UAT. | API Response Time $< 500\text{ms}$ (P95), Error Rate $< 0.1\%$. | Kỹ sư Kiểm thử (QA Engineer) |
| **G5: Triển khai & Vận hành** | Triển khai trên môi trường Cloud, thiết lập giám sát Prometheus/Grafana. | Hệ thống API Production, Dashboard giám sát. | SLA Uptime $\ge 99.9\%$, Freshness $< 24\text{h}$, MTTD $\le 15\text{p}$. | Kỹ sư DevOps / SRE |

## Bước 4 — Đối tượng, phạm vi và giả định/ràng buộc

### 4.1. Đối tượng và Phạm vi
- Tập trung chuyên sâu vào **1 quy trình kỹ thuật lõi**: Xây dựng luồng tích hợp dữ liệu từ máy POS tại chi nhánh lên Cloud, huấn luyện mô hình dự báo chuỗi thời gian, và xuất dữ liệu thông qua RESTful API.

### 4.2. Phần ngoài phạm vi
- Không can thiệp, sửa đổi kiến trúc phần mềm quản lý kho, phần mềm nhân sự, hoặc hệ thống ERP hiện hành của doanh nghiệp. Các phần mềm này sẽ tự giao tiếp thông qua API được cung cấp.

### 4.3. Giới hạn đề tài & Vai trò của AI
- **Giới hạn trách nhiệm AI:** Nền tảng AI được phát triển chỉ đóng vai trò **Hỗ trợ ra quyết định**. Các bộ phận nghiệp vụ sử dụng kết quả dự báo để tham khảo; việc ra quyết định điều phối cuối cùng hoàn toàn phụ thuộc vào quản lý con người.
- **Giới hạn kỹ thuật:** Khả năng dự đoán của mô hình học máy sẽ bị suy giảm đáng kể khi đối mặt với các sự kiện đột biến không có mẫu trong tập dữ liệu lịch sử (ví dụ: bão lũ). Mô hình yêu cầu quá trình tái huấn luyện định kỳ mỗi tháng để duy trì độ chính xác.

## Danh mục tài liệu tham khảo
[1] Scikit-Learn (n.d.), *Mean absolute percentage error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-percentage-error  
[2] Scikit-Learn (n.d.), *Mean absolute error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-error  
[3] Powers, D. M. W. (2011), *Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation*, Journal of Machine Learning Technologies, 2(1), pp. 37–63.  
[4] Google Cloud (n.d.), *Site Reliability Engineering - Availability Table and Metrics*, truy cập tại: https://sre.google/sre-book/availability-table/  
[5] ISO/IEC (2008), *ISO/IEC 25012: Data quality model*, truy cập tại: https://www.iso.org/standard/35736.html  
[6] AWS (2021), *Amazon Builders' Library: Latency and Percentiles*, truy cập tại: https://aws.amazon.com/builders-library/latency-and-percentiles/  
[7] Google Cloud (n.d.), *Site Reliability Engineering - Error Rates*, truy cập tại: https://sre.google/sre-book/service-level-objectives/#error-rate-metrics
[8] Hyndman, R. J. & Athanasopoulos, G. (2021), *Forecasting: Principles and Practice*, 3rd edition, OTexts, truy cập tại: https://otexts.com/fpp3/
