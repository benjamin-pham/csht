# 1. Thông tin chung & tên đề tài

- **Tên đề tài:** Ứng dụng mô hình AI Time-Series Forecasting dự báo lưu lượng khách hàng đa chi nhánh.
- **Thông tin chung:** Đơn vị chủ trì: Nhóm 5. Phạm vi triển khai: Nền tảng hạ tầng tính toán Cloud và luồng dữ liệu của chuỗi Ways Station.

# 2. Bối cảnh – hiện trạng – vấn đề

**Chuẩn bị đầu vào:**
- **Bối cảnh:** Chuỗi Ways Station có nhu cầu vận hành đa chi nhánh, đòi hỏi khả năng phản ứng nhanh với sự biến động của khách hàng trong ngày.
- **Vấn đề hiện tại:** Việc phân tích và dự báo số lượng khách hàng tại mỗi chi nhánh hiện được thực hiện thủ công. Cơ sở dữ liệu giao dịch rời rạc, chưa được làm sạch, thiếu luồng xử lý tự động. Hạ tầng hiện hữu không đáp ứng đủ năng lực tính toán để huấn luyện các mô hình học máy.
- **Đối tượng sử dụng:** Hệ thống dữ liệu tập trung (Data Warehouse), máy chủ dịch vụ API.
- **Hệ thống liên quan:** Hệ thống POS tại chi nhánh, phần mềm ERP và các nền tảng báo cáo nội bộ.
- **Ràng buộc:** Giới hạn cấu hình hạ tầng hiện có, yêu cầu cao về tính sẵn sàng và tính bảo mật của luồng dữ liệu (Data Pipeline).

## 2.1. Hiện trạng vận hành & Điểm nghẽn hệ thống
- **Dữ liệu phân tán và độ trễ cao:** Toàn bộ dữ liệu giao dịch POS tại 34 chi nhánh của Ways Station hiện được xử lý thủ công và lưu trữ phân tán, dẫn đến độ trễ tổng hợp dữ liệu từ 48 đến 72 giờ.
- **Hoạch định tài nguyên bị động theo kinh nghiệm:** Do thiếu công cụ dự báo định lượng theo chuỗi thời gian, việc điều phối nguồn lực tại các chi nhánh phụ thuộc hoàn toàn vào cảm tính:
  - *Khung giờ cao điểm:* Thiếu hụt nhân lực phục vụ và gián đoạn nguồn cung vật tư, kéo dài thời gian chờ đợi của khách hàng và làm suy giảm chất lượng dịch vụ.
  - *Khung giờ thấp điểm:* Dư thừa nhân lực phân bổ cố định, gây lãng phí nghiêm trọng chi phí vận hành (OPEX).
- **Hạn chế hạ tầng tính toán cục bộ:** Máy chủ tại chi nhánh không đủ năng lực tính toán để làm sạch, trích xuất đặc trưng và huấn luyện các mô hình học máy trên tập dữ liệu lịch sử lớn.

## 2.2. Động lực đầu tư & Giá trị hệ thống mang lại
Xây dựng hệ thống dự báo lưu lượng khách hàng theo chuỗi thời gian (AI Time-Series Forecasting) kết hợp đường ống dữ liệu tự động (Automated Data Pipeline) đóng vai trò là **Hệ thống hỗ trợ ra quyết định (Decision Support System - DSS)**, mang lại các giá trị cốt lõi:
1. **Hỗ trợ tối ưu hóa điều phối nhân lực:** Cung cấp dữ liệu dự báo lưu lượng khách theo từng khung giờ trong ngày, làm cơ sở định lượng giúp bộ phận điều phối thiết lập ca làm việc linh hoạt, hạn chế giờ công dư thừa vào giờ vắng và bảo đảm đủ nhân lực trong giờ cao điểm.
2. **Hỗ trợ kế hoạch điều phối cung ứng:** Đưa ra dự báo nhu cầu phục vụ sát thực tế, hỗ trợ bộ phận kho vận lập kế hoạch luân chuyển hàng hóa kịp thời, hạn chế tình trạng đứt gãy cung ứng hoặc tồn đọng hàng hóa quá hạn.
3. **Cung cấp dữ liệu định hướng kế hoạch tiếp thị:** Nhận diện chính xác các khung giờ thấp điểm định kỳ để gợi ý thời điểm kích cầu dịch vụ, tránh việc triển khai khuyến mãi lãng phí vào các khung giờ đã đạt ngưỡng phục vụ tối đa.

## 2.3. Ưu thế kiến trúc kỹ thuật & Cam kết vận hành
- **Tối ưu chi phí nhờ nền tảng Cloud:** Chuyển đổi mô hình đầu tư từ mua sắm máy chủ vật lý tốn kém (CAPEX) sang thuê dịch vụ điện toán đám mây linh hoạt (OPEX).
- **Khả năng tự động co giãn (Auto-scaling):** Hạ tầng Cloud tự động mở rộng tài nguyên khi lưu lượng gọi API tăng vọt và thu hẹp khi tải giảm, bảo đảm hệ thống vận hành liên tục mà không bị nghẽn tải.
- **Cam kết mức độ dịch vụ kỹ thuật (SLA):** Đảm bảo tính sẵn sàng của dịch vụ API đạt Uptime $\ge 99.9\%$ (thời gian gián đoạn dịch vụ tối đa dưới 43.2 phút/tháng), thời gian phản hồi ở mức mili-giây và dữ liệu được bảo vệ an toàn theo các chuẩn mực bảo mật thông tin.

# 3. Mục tiêu & KPI

## 3.1. Mục tiêu tổng quát
Xây dựng nền tảng tích hợp tự động thu thập dữ liệu giao dịch, huấn luyện mô hình học máy (Machine Learning) để phân tích chuỗi thời gian, và triển khai dự báo thông qua các API chuyên dụng phục vụ nội bộ.

## 3.2. Mục tiêu cụ thể và KPI Kỹ thuật (Phân tách 2 nhóm độc lập theo định hướng kỹ thuật)
Toàn bộ hệ thống phần mềm không áp dụng các KPI phân rã theo tầng hạ tầng/mạng của đồ án, mà được phân tách rõ ràng thành **2 nhóm chỉ số KPI độc lập**:

### Nhóm A: KPI Mô hình Trí tuệ nhân tạo (AI Model KPIs)
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

### Nhóm B: KPI Phần mềm & Vận hành hệ thống (Software & Operational KPIs)
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

## 3.3. Ánh xạ KPI theo từng giai đoạn triển khai và tiêu chí bàn giao
Nhằm đảm bảo tính xuyên suốt từ thiết kế đến nghiệm thu và dự toán chi phí, KPI kỹ thuật được phân bổ cụ thể làm tiêu chí nghiệm thu bàn giao qua 5 giai đoạn phát triển phần mềm:

| Giai đoạn triển khai | Hoạt động kỹ thuật & Yêu cầu | Sản phẩm bàn giao (Deliverables) | KPI nghiệm thu giai đoạn | Nhân sự phụ trách |
| :--- | :--- | :--- | :--- | :--- |
| **G1: Khảo sát & Phân tích dữ liệu** | Thu thập dữ liệu lịch sử POS, chuẩn hóa schema, làm sạch dữ liệu khuyết thiếu. | Tài liệu đặc tả dữ liệu, Dataset đã làm sạch. | Tính đầy đủ dữ liệu $\ge 99.5\%$, Schema hợp lệ $100\%$. | Kỹ sư Dữ liệu (Data Engineer) |
| **G2: Thiết kế kiến trúc phần mềm** | Thiết kế Data Pipeline, cấu trúc Web Service RESTful API và mô hình AI. | Tài liệu thiết kế kiến trúc, API Contract. | $100\%$ API đạt chuẩn RESTful, kiến trúc sẵn sàng mở rộng. | Kiến trúc sư Phần mềm (Software Architect) |
| **G3: Phát triển mô hình & Pipeline** | Xây dựng đường ống ETL tự động; huấn luyện và tinh chỉnh mô hình TSFM. | Mã nguồn Data Pipeline, Artifact mô hình AI đã huấn luyện. | $\text{MAPE} < 10\%$, $\text{Precision} \ge 85\%$, Inference Latency $\le 200\text{ms}$. | Kỹ sư AI (Machine Learning Engineer) |
| **G4: Kiểm thử & Đóng gói phần mềm** | Kiểm thử tích hợp (Integration Test), tải (Load Test), đóng gói Container. | Docker Image, Bộ kịch bản Test, Báo cáo UAT. | API Response Time $< 500\text{ms}$ (P95), Error Rate $< 0.1\%$. | Kỹ sư Kiểm thử (QA Engineer) |
| **G5: Triển khai & Vận hành** | Triển khai trên môi trường Cloud, thiết lập giám sát Prometheus/Grafana. | Hệ thống API Production, Dashboard giám sát. | SLA Uptime $\ge 99.9\%$, Freshness $< 24\text{h}$, MTTD $\le 15\text{p}$. | Kỹ sư DevOps / SRE |

# 4. Đối tượng áp dụng, phạm vi, giả định/ràng buộc

## 4.1. Đối tượng và Phạm vi
- Tập trung chuyên sâu vào **1 quy trình kỹ thuật lõi**: Xây dựng luồng tích hợp dữ liệu từ máy POS tại chi nhánh lên Cloud, huấn luyện mô hình dự báo chuỗi thời gian, và xuất dữ liệu thông qua RESTful API.

## 4.2. Phần ngoài phạm vi
- Không can thiệp, sửa đổi kiến trúc phần mềm quản lý kho, phần mềm nhân sự, hoặc hệ thống ERP hiện hành của doanh nghiệp. Các phần mềm này sẽ tự giao tiếp thông qua API được cung cấp.

## 4.3. Giới hạn đề tài & Vai trò của AI
- **Giới hạn trách nhiệm AI:** Nền tảng AI được phát triển chỉ đóng vai trò **Hỗ trợ ra quyết định**. Các bộ phận nghiệp vụ sử dụng kết quả dự báo để tham khảo; việc ra quyết định điều phối cuối cùng hoàn toàn phụ thuộc vào quản lý con người.
- **Giới hạn kỹ thuật:** Khả năng dự đoán của mô hình học máy sẽ bị suy giảm đáng kể khi đối mặt với các sự kiện đột biến không có mẫu trong tập dữ liệu lịch sử (ví dụ: bão lũ). Mô hình yêu cầu quá trình tái huấn luyện định kỳ mỗi tháng để duy trì độ chính xác.

# 5. Yêu cầu nghiệp vụ & yêu cầu hệ thống (FR/NFR)

## 5.1. Yêu cầu nghiệp vụ (Business Requirements / Use Case level)

Yêu cầu nghiệp vụ được trình bày theo use case/user story, bám sát phạm vi luồng tích hợp dữ liệu POS → Cloud → Mô hình AI → RESTful API.

| ID | Tên nghiệp vụ (User Story) | Tác nhân | Luồng chính (Main Flow) | Ngoại lệ (Exception Flow) | Đầu ra / Kết quả |
|:---|:---|:---|:---|:---|:---|
| BR-01 | Xem dự báo lưu lượng khách | Quản lý chi nhánh | 1. Đăng nhập hệ thống <br>2. Chọn chi nhánh & khoảng thời gian <br>3. Hệ thống query API trả về dữ liệu dự báo | API lỗi hoặc chưa có dự báo mới $\rightarrow$ Báo lỗi & hiển thị dữ liệu lịch sử của tuần trước. | Bảng/Biểu đồ dự báo khách theo giờ (JSON). |
| BR-02 | Nhận cảnh báo giờ cao điểm | Bộ phận điều phối | 1. Hệ thống phân tích kết quả dự báo <br>2. Nếu lượng khách $> 1.5 \times$ trung bình $\rightarrow$ Tự động gửi cảnh báo. | Gửi email/webhook thất bại $\rightarrow$ Đẩy noti trực tiếp trên App/Dashboard nội bộ. | Thông báo cảnh báo (webhook/email). |
| BR-03 | Tự động Pipeline dữ liệu | Hệ thống (Cronjob) | 1. Kết nối POS DB (01:00 AM) <br>2. Trích xuất batch <br>3. Làm sạch, chuẩn hóa <br>4. Nạp vào Data Warehouse | Rớt kết nối mạng tới POS $\rightarrow$ Retry 3 lần, nếu thất bại Alert cho Kỹ sư dữ liệu. | Dataset chuẩn hóa lưu tại Data Warehouse. |
| BR-04 | Giám sát trạng thái hệ thống | Kỹ sư vận hành | 1. Truy cập Grafana <br>2. Xem dashboard metrics (Pipeline, API, Model, Resource) | Mất kết nối tới Prometheus $\rightarrow$ Bật cảnh báo khẩn qua PagerDuty/Slack. | Dashboard giám sát real-time (Uptime, MAPE). |

## 5.2. Yêu cầu chức năng (Functional Requirements)

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

## 5.3. Yêu cầu phi chức năng (Non-Functional Requirements)

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

# 6. Giải pháp đề xuất & kiến trúc (TO-BE, tích hợp, dữ liệu)

## 6.1. Quy trình nghiệp vụ TO-BE
Quy trình vận hành có sự tham gia của AI đóng vai trò hệ thống hỗ trợ ra quyết định (DSS). Luồng công việc:
1. **Thu thập (24/7):** Khách hàng giao dịch tại hệ thống POS của chi nhánh.
2. **Đồng bộ & Xử lý (01:00 AM mỗi ngày):** Pipeline tự động rút dữ liệu từ POS về kho dữ liệu Cloud trung tâm, tiến hành làm sạch, loại bỏ lỗi.
3. **Dự báo (02:00 AM):** AI Engine chạy Batch Inference cho 34 chi nhánh dựa trên dữ liệu mới nhất, lưu trữ kết quả.
4. **Cảnh báo (Tự động):** Alert Service quét kết quả dự báo. Nếu phát hiện khung giờ vượt tải ($>150\%$ lưu lượng trung bình), tự động push Webhook/Email cho bộ phận quản lý.
5. **Ra quyết định (08:00 AM - Điểm kiểm soát):** Quản lý chi nhánh truy cập phần mềm nội bộ (gọi API dự báo), tham khảo kết quả để duyệt lịch phân ca nhân viên và chuẩn bị kho bãi. **Con người chốt quyết định cuối cùng**.

## 6.2. Kiến trúc hệ thống tổng thể (3 tầng)

Kiến trúc được thiết kế trên nền tảng Cloud, chia thành 3 lớp rõ ràng:

1. **Tầng Trình bày (Presentation Layer):**
   - **Web Dashboard:** Giao diện hiển thị dành cho Quản lý chi nhánh và Quản lý trung tâm để xem kết quả dự báo.
   - **Grafana:** Bảng điều khiển dành cho bộ phận IT (Kỹ sư dữ liệu, SRE, DevOps) để giám sát các chỉ số hoạt động của hệ thống (Metrics/Logs).
   - **Webhook / Email Alert:** Kênh phân phối thông báo tự động (cảnh báo giờ cao điểm, cảnh báo lỗi hệ thống) đến người dùng cuối.

2. **Tầng Ứng dụng (Application Layer):**
   - **API Gateway:** Cửa ngõ tiếp nhận toàn bộ các yêu cầu từ Tầng Trình bày. Đảm nhiệm chức năng xác thực người dùng (Xác thực JWT) và kiểm soát lưu lượng (Rate Limiting).
   - **Forecast Service (FastAPI):** Dịch vụ API xử lý và trả về kết quả dự báo lưu lượng khách hàng.
   - **Alert Service (FastAPI):** Dịch vụ API phụ trách xử lý logic và kích hoạt các cảnh báo dựa trên ngưỡng thiết lập.
   - **Pipeline Orchestrator (Apache Airflow):** Hệ thống điều phối luồng dữ liệu (Data Pipeline), tự động hóa các tác vụ ETL và huấn luyện mô hình.

3. **Tầng Dữ liệu (Data Layer):**
   - **Data Warehouse (PostgreSQL):** Kho dữ liệu có cấu trúc, lưu trữ dữ liệu sau khi đã được làm sạch và dữ liệu dự báo.
   - **Model Registry (MLflow):** Nơi lưu trữ, phiên bản hóa và quản lý các mô hình học máy (AI Models).
   - **Prometheus + Loki:** Các công cụ thu thập và lưu trữ thông số hoạt động (Metrics) và nhật ký hệ thống (Logs) phục vụ cho Grafana.
   - **Object Storage (S3):** Nơi lưu trữ khối (Object Storage) dành cho dữ liệu thô (Raw Data) trích xuất từ các POS và các tạo tác mô hình (Model Artifacts).

## 6.3. Luồng xử lý Data Pipeline

Luồng dữ liệu trong hệ thống được vận hành một cách tự động thông qua các DAG (Directed Acyclic Graph) trên Apache Airflow theo các bước sau:

1. **Trích xuất dữ liệu (Extract):**
   - Hàng ngày vào lúc 01:00 AM, Airflow thực thi tác vụ trích xuất dữ liệu theo lô (batch) từ hệ thống Cơ sở dữ liệu POS của 34 chi nhánh.
   - Việc kết nối và truyền tải dữ liệu được bảo mật qua giao thức TLS.
   - Dữ liệu thô thu thập được sẽ được lưu trữ tại phân vùng Raw Zone trên Object Storage (S3).

2. **Chuyển đổi dữ liệu (Transform):**
   - Ngay sau quá trình Extract, Airflow thực thi các tiến trình làm sạch dữ liệu.
   - Dữ liệu thô được chuẩn hóa, loại bỏ các bản ghi trùng lặp hoặc không hợp lệ.
   - Kết quả dữ liệu sạch (Clean Data) được nạp vào phân vùng Clean Zone tại Data Warehouse (PostgreSQL).

3. **Huấn luyện và Dự báo (Train & Predict):**
   - Từ dữ liệu sạch tại Data Warehouse, hệ thống phân nhánh thành hai tiến trình chính:
     - **Tái huấn luyện (Train):** Airflow thực thi DAG tái huấn luyện mô hình theo chu kỳ (ví dụ: hàng tháng). Mô hình huấn luyện xong được cập nhật và lưu trữ phiên bản tại MLflow Registry.
     - **Dự báo (Predict):** Hàng đêm, Airflow thực thi DAG dự báo bằng cách sử dụng mô hình AI mới nhất để chạy dự báo hàng loạt (batch). Kết quả dự báo được ghi nhận trở lại Data Warehouse (bảng Kết Quả Dự Báo), sẵn sàng cho Forecast Service truy xuất.

## 6.4. Tích hợp hệ thống

| Hệ thống Nguồn / Đích | Giao thức | Tần suất | Dữ liệu trao đổi (Mapping) | Bảo mật |
|:---|:---|:---|:---|:---|
| POS DB $\rightarrow$ S3 | JDBC/ODBC qua TLS | Batch 1 lần/đêm | Giao dịch ẩn danh (lượng khách, thời gian, mã chi nhánh) | Mã hóa in-transit |
| S3 $\rightarrow$ Data Warehouse | Internal VPC | Theo luồng Extract | Dataset đã chuẩn hóa | Mã hóa at-rest (AES-256) |
| Forecast API $\rightarrow$ ERP | RESTful (HTTPS) | On-demand | JSON chứa array lượng khách dự báo theo slot giờ | JWT + RBAC |
| Prometheus $\rightarrow$ Grafana | Internal scrape | 15 giây/lần | Metrics hệ thống IT (Uptime, API Latency) | Nội bộ mạng ảo VPC |

# 7. Kế hoạch triển khai & tiến độ (WBS)

Chia theo 5 pha chuẩn mực. Kế hoạch triển khai khớp trực tiếp với bảng ánh xạ KPI theo giai đoạn đã định nghĩa tại Bước 3.3 (Bảng G1–G5):

| Pha / Giai đoạn | Tuần | Hoạt động chính | Sản phẩm đầu ra (Deliverables) | Tiêu chí hoàn thành (Nghiệm thu) | Người chịu trách nhiệm (Owner) |
|:---|:---:|:---|:---|:---|:---|
| **1. Khảo sát & Phân tích (SRS/BRD)** | T1–T3 | Thu thập dữ liệu POS lịch sử $\ge$ 12 tháng; Phân tích chất lượng dữ liệu; Làm sạch missing/duplicate. | Tài liệu đặc tả dữ liệu (Data Dictionary); Dataset sạch. | Completeness $\ge$ 99.5%; Schema hợp lệ 100%. | Kỹ sư Dữ liệu (Data Engineer) |
| **2. Thiết kế (HLD/LLD)** | T4–T5 | Thiết kế Data Pipeline; Thiết kế API Contract (OpenAPI); Thiết kế ERD; Thiết kế hạ tầng Cloud. | HLD/LLD; API Contract; ERD; Terraform scripts. | Kiến trúc được Sponsor và Key User duyệt 100%. | Kiến trúc sư / Backend Lead |
| **3. Phát triển (Dev)** | T6–T10 | Code Airflow DAGs (ETL); Huấn luyện mô hình TSFM; Code API Services (FastAPI); Tích hợp MLflow. | Source code Pipeline & API; Artifact AI Model. | $\text{MAPE} < 10\%$; $\text{Precision} \ge 85\%$. | Kỹ sư AI (ML Engineer) |
| **4. Kiểm thử (SIT/UAT)** | T11–T13 | Test tích hợp; Test tải (100 CCU); Test bảo mật; Đóng gói Docker; Hỗ trợ UAT. | Kịch bản test; Báo cáo SIT; Biên bản UAT (Sign-off). | API P95 $\le$ 500ms; Error Rate $<$ 0.1%; Pass UAT. | Kỹ sư Kiểm thử (QA) |
| **5. Triển khai & Vận hành (Rollout/Ops)** | T14–T15 | Triển khai Kubernetes; Cấu hình Grafana/Prometheus; Pilot 5 chi nhánh $\rightarrow$ Rollout 34 chi nhánh. | Hệ thống Live; Dashboard giám sát; Tài liệu vận hành (Runbook). | Uptime $\ge$ 99.9%; Freshness $\le$ 24h. | Kỹ sư DevOps/SRE |

*Tổng thời lượng: 15 tuần (~4 tháng).*

# 8. Tổ chức nhân sự & cơ chế phối hợp (RACI)

## 8.1. Cơ cấu nhân sự
| Vai trò | Số lượng | Trách nhiệm chính |
|:---|:---:|:---|
| **Project Manager (PM)** | 1 | Quản lý rào cản, ngân sách, tiến độ; Báo cáo Sponsor (Ban Giám đốc). |
| **Kỹ sư Dữ liệu (Data Engineer)** | 2 | Phát triển luồng ETL/ELT, duy trì Data Warehouse. |
| **Kỹ sư AI (ML Engineer)** | 2 | Phát triển, tinh chỉnh thuật toán và vận hành mô hình học máy. |
| **Kỹ sư Backend (Backend Dev)** | 1 | Viết API, phân quyền, tối ưu response time. |
| **Kỹ sư DevOps / SRE** | 1 | Xây hạ tầng Cloud, CI/CD, hệ thống monitoring, lo SLA. |
| **Kỹ sư Kiểm thử (QA)** | 1 | Test chất lượng, hiệu năng, điều phối UAT với User. |
| **Key User (QL Chi nhánh)** | 2 | Cung cấp logic xếp ca thực tế, kiểm thử UAT và ký sign-off. |

## 8.2. Ma trận phối hợp (RACI)
| Đầu việc chính | PM | Data Eng | ML Eng | Backend | SRE | QA | Key User |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Thu thập & làm sạch dữ liệu (Pha 1) | A | **R** | C | — | — | — | I |
| Chốt yêu cầu & Thiết kế hệ thống (Pha 2) | A | C | C | **R** | **R** | — | I |
| Phát triển Mô hình & API (Pha 3) | A | C | **R** | **R** | — | — | — |
| Duyệt UAT & Ký Sign-off (Pha 4) | A | I | I | I | I | C | **R** |
| Triển khai Go-live hạ tầng (Pha 5) | A | — | — | C | **R** | — | I |
| Bàn giao tài liệu vận hành | **R** | C | C | C | **R** | — | A |

*(**R**: Thực hiện, **A**: Chịu trách nhiệm duyệt, **C**: Tham vấn, **I**: Nhận thông tin)*

## 8.3. Cơ chế làm việc & Quản trị rủi ro
*   **Họp tiến độ:** Standup hàng tuần, báo cáo Sprint review 2 tuần/lần. Tại mốc kết thúc Pha, họp đánh giá (Milestone Review) với Sponsor.
*   **Quản lý thay đổi (Change Request - CR):** Nghiêm cấm scope creep (mở rộng phạm vi không kiểm soát). Mọi tính năng phát sinh ngoài Bước 4 phải lập phiếu CR để PM tính toán đội chi phí/thời gian duyệt.
*   **Quản lý Issue/Risk:** Tracking trên Jira. Bất kỳ rủi ro nào liên quan tới dữ liệu (bẩn, sai lệch) phải được báo cho Data Engineer giải quyết trong SLA $\le$ 24h.

# 9. Dự toán chi phí & phương án tài chính

## 9.1. Bảng phân tách dự toán (CAPEX / OPEX)
Chi phí tách bạch giữa phí đầu tư xây dựng ban đầu (CAPEX) và phí duy trì nền tảng, Cloud định kỳ hàng năm (OPEX). Có chèn quỹ dự phòng (Contingency) 10%.

### A. Chi phí đầu tư dự án (CAPEX) — Giai đoạn 15 tuần
| Nhóm chi phí | Chi tiết hạng mục (Giả định đơn giá) | Thành tiền (VNĐ) |
|:---|:---|---:|
| **Nhân công (Dev/Outsource)** | Lương khoán đội dự án (PM, Data, ML, BE, SRE, QA) trong 1-4 tháng tùy vị trí (Trung bình 22tr/người/tháng). | 594.000.000 |
| **Bản quyền (License)** | Sử dụng Open-source (Airflow, MLflow, FastAPI). | 0 |
| **Hạ tầng (GĐ Phát triển)** | Phí thuê VM, GPU training, PostgreSQL, S3 môi trường Dev/Staging trong 4 tháng. | 64.000.000 |
| **Đào tạo & Chuyển giao** | Tổ chức 2 buổi hướng dẫn đọc Dashboard cho Key Users. | 5.000.000 |
| **Tổng CAPEX** | (Chưa bao gồm dự phòng rủi ro 10%) | **663.000.000** |

### B. Chi phí vận hành Cloud & Bảo trì (OPEX) — 1 năm sau Go-live
| Nhóm chi phí | Chi tiết hạng mục | Thành tiền (VNĐ) |
|:---|:---|---:|
| **Hạ tầng (Cloud Server)** | Thuê K8s Cluster (96tr), PostgreSQL HA (54tr), S3 Storage (7.2tr), Băng thông & DNS (6tr). | 163.200.000 |
| **Hạ tầng (GPU AI)** | Thuê GPU Spot Instances chạy job tái huấn luyện (1 lần/tháng). | 9.600.000 |
| **Nhân sự Ops / Hypercare** | Chi phí part-time SRE/Data Eng duy trì SLA, giám sát hệ thống. | 132.000.000 |
| **Bảo mật & Tuân thủ** | Thuê bên thứ 3 Pentest đánh giá bảo mật API định kỳ (2 lần/năm). | 20.000.000 |
| **Tổng OPEX / Năm 1** | (Chưa bao gồm dự phòng rủi ro 10%) | **325.800.000** |

## 9.2. Tổng chi phí sở hữu (TCO) & Phương án tài chính
*   **Tổng dự phòng rủi ro (Contingency 10%):** 98.880.000 VNĐ
*   **Tổng TCO (Năm 1) = CAPEX + OPEX + Contingency = 1.087.680.000 VNĐ**
*   **Phương án tài chính:** Chủ trương chuyển hóa 100% chi phí hạ tầng máy chủ thành chi phí hoạt động OPEX hàng tháng (thuê Cloud) thay vì mua thiết bị vật lý. Tiết kiệm phí license qua hệ sinh thái mã nguồn mở.

## 9.3. Kiểm chứng tính nhất quán chi phí (Phân bổ theo giai đoạn)
Bảng kiểm chứng chứng minh tổng ngân sách CAPEX xin cấp (663 triệu) được phân bổ logic, khớp với WBS (Bước 7):

| Kế hoạch WBS | Phí nhân công (VNĐ) | Phí hạ tầng/khác (VNĐ) | Tổng cộng (VNĐ) |
|:---|---:|---:|---:|
| Pha 1: Khảo sát & Phân tích | 134.000.000 | 10.500.000 | 144.500.000 |
| Pha 2: Thiết kế (HLD/LLD) | 75.000.000 | 7.000.000 | 82.000.000 |
| Pha 3: Phát triển (Dev) | 265.000.000 | 30.500.000 | 295.500.000 |
| Pha 4: Kiểm thử (SIT/UAT) | 95.000.000 | 10.500.000 | 105.500.000 |
| Pha 5: Triển khai (Go-live) | 25.000.000 | 10.500.000 | 35.500.000 |
| **Kiểm chứng tổng (Khớp)**| **594.000.000** | **69.000.000** | **663.000.000** |

# 10. Rủi ro, chất lượng, kiểm thử, quản lý thay đổi

## 10.1. Quản trị rủi ro (Risk Management)
Bảng Risk Register nhận diện các rủi ro có thể xảy ra trong quá trình triển khai dự án, cùng biện pháp giảm thiểu:

| Mã | Rủi ro | Xác suất | Ảnh hưởng | Mức độ | Biện pháp giảm thiểu | Người phụ trách (Owner) |
|:---|:---|:---:|:---:|:---:|:---|:---|
| R01 | **Dữ liệu POS bẩn / thiếu hụt:** Hệ thống máy POS tại các chi nhánh bị mất kết nối hoặc nhân viên nhập sai dữ liệu. | Cao | Cao | **Cao** | Xây dựng cơ chế làm sạch tự động (Fill NA/Drop Outliers) trong Data Pipeline. Có cảnh báo Data Quality cho Key User xử lý thủ công. | Kỹ sư Dữ liệu |
| R02 | **Mô hình dự báo sai lệch (Data Drift):** Hành vi khách hàng thay đổi đột ngột (ví dụ do thời tiết, sự kiện) làm giảm độ chính xác của AI. | Trung bình | Cao | **Cao** | Thiết lập ngưỡng cảnh báo MAPE > 15% tự động kích hoạt tiến trình tái huấn luyện mô hình. | Kỹ sư AI |
| R03 | **Scope Creep (Phình yêu cầu):** Quản lý chi nhánh yêu cầu bổ sung tính năng quản lý nhân sự thay vì chỉ xem dự báo. | Trung bình | Trung bình | **Vừa** | Kiểm soát chặt chẽ qua quy trình Change Request (CR). Yêu cầu Sponsor duyệt mọi chi phí phát sinh. | PM |
| R04 | **Nghẽn tải hệ thống lúc 08:00 AM:** 34 chi nhánh cùng truy cập API lấy dự báo gây rớt dịch vụ. | Thấp | Cao | **Vừa** | Thiết lập cơ chế Auto-scaling trên Kubernetes; Áp dụng Rate Limiting tại API Gateway. | SRE / DevOps |

## 10.2. Kế hoạch kiểm thử và Đảm bảo chất lượng (QA/QC)
*   **Kiểm thử Dữ liệu (Data Testing):** Kiểm tra tính toàn vẹn của Data Pipeline. Tiêu chí Pass: $100\%$ schema hợp lệ, $\ge 99.5\%$ bản ghi được luân chuyển thành công.
*   **Kiểm thử Mô hình (Model Testing):** Chạy Backtesting trên dữ liệu lịch sử. Tiêu chí Pass: MAPE $< 10\%$, MAE $\le 3$ và Precision $\ge 85\%$.
*   **Kiểm thử Hiệu năng (Load/Stress Testing):** Dùng JMeter giả lập 500 CCU truy cập đồng thời vào API. Tiêu chí Pass: P95 Latency $< 500$ms, không rớt request (HTTP 5xx $< 0.1\%$).
*   **Kiểm thử UAT (User Acceptance Testing):** Key User vận hành thử trên môi trường Staging. Ký biên bản Sign-off trước khi Go-live.

## 10.3. Quản lý thay đổi (Change Management)
*   **Truyền thông:** Gửi thông báo toàn hệ thống Ways Station trước Go-live 2 tuần về hệ thống DSS mới.
*   **Đào tạo:** Tổ chức 2 buổi workshop online (qua Zoom/Teams) cho Quản lý chi nhánh cách đọc Dashboard và sử dụng số liệu dự báo để xếp ca.
*   **Tài liệu:** Cung cấp User Manual dạng video ngắn và file PDF, tích hợp sẵn trong mục Help của phần mềm.

# 11. Vận hành – bảo trì – chuyển giao

## 11.1. Mô hình vận hành và Hỗ trợ (Hypercare)
*   **Giai đoạn Hypercare (1 tháng sau Go-live):** Đội dự án duy trì hỗ trợ mức cao nhất, họp chớp nhoáng hàng ngày (Daily Standup) lúc 09:00 AM để rà soát lỗi API và độ trễ dữ liệu.
*   **Quy trình hỗ trợ ITSM (Tier 1-2-3):** 
    - Tier 1: Helpdesk nội bộ tiếp nhận ticket.
    - Tier 2: Vấn đề dữ liệu/API đẩy cho đội IT nội bộ của Ways Station.
    - Tier 3: Vấn đề lõi AI/Hạ tầng sâu đẩy về đội dự án (SRE/ML Eng). Cam kết SLA xử lý lỗi nghiêm trọng $\le 4$ giờ.

## 11.2. Giám sát hệ thống (Monitoring) và An toàn dữ liệu
*   **Monitoring & Alerting:** Sử dụng Grafana giám sát 3 metrics chính (Pipeline Freshness, API Latency, Model MAPE). Gửi cảnh báo khẩn cấp qua PagerDuty/Slack nếu Uptime $< 99.9\%$.
*   **Backup & Disaster Recovery (DR):** 
    - Áp dụng **nguyên tắc sao lưu 3-2-1**: Sao lưu Data Warehouse (PostgreSQL) tự động hàng ngày (có bản lưu cục bộ và bản đồng bộ lên Cloud Storage cách ly).
    - DR Drill (Diễn tập phục hồi thảm họa) thực hiện 6 tháng/lần, đảm bảo RPO $< 24$h và RTO $< 4$h.

## 11.3. Bàn giao và Chuyển giao công nghệ
Gói bàn giao cho đội ngũ IT của Ways Station bao gồm:
*   Mã nguồn (Source Code) Data Pipeline, AI Model và API Services (trên GitLab).
*   Tài khoản quản trị Cloud (AWS/GCP), MLflow, Airflow.
*   Tài liệu Kiến trúc (HLD/LLD), Sổ tay vận hành (Runbook) cho các kịch bản xử lý sự cố thường gặp.

# 12. Nghiệm thu & đánh giá hiệu quả

## 12.1. Tiêu chí nghiệm thu hệ thống
Nghiệm thu dựa trên việc hoàn thành các mốc Deliverables và đạt chuẩn KPI Kỹ thuật (Bước 3):
1. Báo cáo UAT có chữ ký xác nhận của đại diện Quản lý chi nhánh (Pass 100% Test Case mức Critical/High).
2. Hệ thống hoạt động ổn định trên Production tối thiểu 14 ngày liên tục mà không có sự cố gián đoạn mức độ nghiêm trọng (P0/P1).
3. Biên bản đo lường SLA đạt chuẩn (Uptime $\ge 99.9\%$, API P95 $\le 500$ms).

## 12.2. Đo lường hiệu quả nghiệp vụ (Benefit Realization)
Việc đánh giá hệ thống không chỉ dừng ở mặt kỹ thuật (tháng đầu tiên) mà cần đo lường giá trị thực mang lại cho doanh nghiệp định kỳ tại tháng 1 - tháng 3 - tháng 6 sau Go-live:
*   **Chỉ số Tối ưu Nhân sự:** Giảm được bao nhiêu phần trăm chi phí giờ công (OPEX) tại các khung giờ thấp điểm so với trước khi dùng hệ thống?
*   **Chỉ số Chất lượng Dịch vụ:** Tỷ lệ khách hàng phải chờ đợi trong giờ cao điểm có giảm không? (Khảo sát qua hệ thống đánh giá tại cửa hàng).
*   **Độ ổn định của Model:** Model có duy trì được MAPE $< 10\%$ qua các tháng hay không, từ đó đánh giá tần suất cần thiết phải tái huấn luyện mô hình.

# Phụ lục: sơ đồ quy trình, mockup, ERD, ma trận phân quyền, danh mục thuật ngữ

## Phụ lục 1: Thiết kế dữ liệu (ERD High-level)

| Thực thể | Thuộc tính chính | Mô tả |
|:---|:---|:---|
| **Branch** | `branch_id` (PK), `branch_name`, `branch_type`, `region` | Danh mục chi nhánh (Master Data) |
| **Transaction_Hourly** | `id` (PK), `branch_id` (FK), `date`, `hour_slot`, `customer_count` | Dữ liệu lượng khách thực tế tổng hợp theo giờ |
| **Forecast_Result** | `id` (PK), `branch_id` (FK), `forecast_date`, `hour_slot`, `predicted_count`, `is_peak` | Kết quả xuất ra từ mô hình dự báo AI |
| **Model_Metadata** | `model_id` (PK), `version`, `mape_score`, `mae_score`, `status` | Thông tin lịch sử độ chính xác mô hình |

**Quy tắc chuẩn hóa / Mã hóa danh mục:**
- Khóa định danh chi nhánh: `WS-{TYPE}-{NNN}` (VD: `WS-GYM-001`).
- Khóa thời gian (Hour slot): Số nguyên 0–23 định dạng chu kỳ 24h.

## Phụ lục 2: Ma trận phân quyền (RBAC)

| Vai trò (Role) | Xem dự báo chi nhánh mình | Xem dự báo toàn hệ thống | Xem Dashboard giám sát | Cấu hình ngưỡng cảnh báo | Quản lý mô hình AI | Quản lý Pipeline |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Quản lý chi nhánh | ✓ | — | — | — | — | — |
| Quản lý trung tâm | ✓ | ✓ | ✓ | ✓ | — | — |
| Kỹ sư AI (ML Engineer) | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Kỹ sư Dữ liệu (DE) | — | — | ✓ | — | — | ✓ |
| Kỹ sư DevOps/SRE | — | — | ✓ | ✓ | — | ✓ |

## Danh mục tài liệu tham khảo
[1] Scikit-Learn (n.d.), *Mean absolute percentage error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-percentage-error  
[2] Scikit-Learn (n.d.), *Mean absolute error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-error  
[3] Powers, D. M. W. (2011), *Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation*, Journal of Machine Learning Technologies, 2(1), pp. 37–63.  
[4] Google Cloud (n.d.), *Site Reliability Engineering - Availability Table and Metrics*, truy cập tại: https://sre.google/sre-book/availability-table/  
[5] ISO/IEC (2008), *ISO/IEC 25012: Data quality model*, truy cập tại: https://www.iso.org/standard/35736.html  
[6] AWS (2021), *Amazon Builders' Library: Latency and Percentiles*, truy cập tại: https://aws.amazon.com/builders-library/latency-and-percentiles/  
[7] Google Cloud (n.d.), *Site Reliability Engineering - Error Rates*, truy cập tại: https://sre.google/sre-book/service-level-objectives/#error-rate-metrics
[8] Hyndman, R. J. & Athanasopoulos, G. (2021), *Forecasting: Principles and Practice*, 3rd edition, OTexts, truy cập tại: https://otexts.com/fpp3/
[9] Google Cloud (n.d.), *Kubernetes Engine Documentation*, truy cập tại: https://cloud.google.com/kubernetes-engine/docs  
[10] Apache Software Foundation (n.d.), *Apache Airflow Documentation*, truy cập tại: https://airflow.apache.org/docs/  
[11] MLflow (n.d.), *MLflow Documentation — Model Registry*, truy cập tại: https://mlflow.org/docs/latest/model-registry.html  
[12] PMI (2021), *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*, 7th Edition, Project Management Institute.  
[13] Hyndman, R.J., & Athanasopoulos, G. (2021), *Forecasting: Principles and Practice*, 3rd Edition, OTexts: Melbourne, Australia. (Tài liệu tham khảo cơ sở toán học cho các độ đo lỗi dự báo chuỗi thời gian như MAPE, MAE).  
[14] Powers, D. M. W. (2011), *Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation*, Journal of Machine Learning Technologies, 2(1), 37-63. (Tài liệu tham khảo cho các độ đo đánh giá mô hình học máy như Precision).
