# Báo Cáo Thực Hành: Đề Xuất Phát Triển Hệ Thống AI Dự Báo Lưu Lượng Khách Hàng Dành Cho Chuỗi Ways Station

## 1. Thông tin chung & tên đề tài
- **Tên đề tài:** Xây dựng hệ thống Trí tuệ nhân tạo dự báo lưu lượng khách hàng theo khung giờ nhằm tối ưu hóa vận hành đa phòng ban tại chuỗi Ways Station.
- **Đối tượng:** Dữ liệu giao dịch (POS), dữ liệu thời tiết, ngày lễ và lịch sử lưu lượng khách hàng.
- **Phạm vi:** Ứng dụng tại toàn bộ các chi nhánh thuộc chuỗi Ways Station.
- **Bối cảnh:** Ways Station đang đối mặt với bài toán tối ưu chi phí vận hành do sự biến động khó lường của lượng khách hàng trong ngày.

### 1.1. Giải thích các thuật ngữ tiếng Anh viết tắt
Để giúp hội đồng dễ dàng theo dõi, nhóm xin giải thích các thuật ngữ chuyên ngành được sử dụng trong báo cáo:
- **AI (Artificial Intelligence):** Trí tuệ nhân tạo.
- **POS (Point of Sale):** Hệ thống máy tính tiền và quản lý bán hàng tại quầy.
- **OPEX (Operating Expense):** Chi phí vận hành định kỳ (ví dụ: tiền lương nhân viên, tiền điện nước, chi phí thuê Cloud hàng tháng).
- **CAPEX (Capital Expenditure):** Chi phí đầu tư tài sản ban đầu (ví dụ: tiền mua đứt máy chủ Server, xây dựng quán).
- **SLA (Service Level Agreement):** Cam kết mức độ/chất lượng dịch vụ (ví dụ: cam kết hệ thống luôn hoạt động 99.9% thời gian).
- **API (Application Programming Interface):** Cổng giao tiếp lập trình ứng dụng, đóng vai trò như một "chiếc cầu nối" giúp các phần mềm khác nhau có thể truyền dữ liệu cho nhau.
- **ERP (Enterprise Resource Planning):** Hệ thống phần mềm quản trị tổng thể doanh nghiệp (chứa dữ liệu cốt lõi của kho, kế toán, nhân sự).
- **KPI (Key Performance Indicator):** Chỉ số đo lường hiệu quả hoạt động (được định lượng bằng con số/công thức rõ ràng).
- **SLO (Service Level Objective):** Mục tiêu chất lượng dịch vụ nội bộ của đội ngũ IT (tiêu chuẩn kỹ thuật khắt khe hơn để bảo đảm đạt cam kết SLA bên ngoài).
- **P1 / P2 Incident:** Phân loại mức độ nghiêm trọng của sự cố CNTT (P1: sự cố tối khẩn cấp làm ngừng trệ hệ thống lõi; P2: sự cố mức độ cao gây gián đoạn cục bộ).
- **Cycle Time:** Thời gian chu kỳ hoàn tất một quy trình nghiệp vụ từ điểm bắt đầu đến kết thúc (end-to-end).
- **RBAC (Role-Based Access Control):** Cơ chế kiểm soát truy cập phân quyền dựa trên vai trò của người dùng trong tổ chức.
- **Backup Success Rate:** Tỷ lệ các phiên sao lưu dữ liệu được thực hiện thành công và toàn vẹn.

## 2. Bối cảnh – Hiện trạng – Vấn đề (Business Case)
- **Vấn đề cốt lõi (Nỗi đau):** Hiện tại, việc dự báo lượng khách phụ thuộc hoàn toàn vào kinh nghiệm thủ công. Hậu quả:
  - Khung giờ cao điểm: Không đủ nhân viên và nguyên vật liệu, dẫn đến giảm chất lượng dịch vụ, khách hàng phàn nàn.
  - Khung giờ thấp điểm: Dư thừa nhân viên gây lãng phí chi phí OPEX.
- **Giá trị vàng:** Xây dựng hệ thống dự báo số lượng khách hàng theo từng khung giờ (Time-Series Forecasting). Dữ liệu sinh ra từ AI sẽ tham gia trực tiếp vào quá trình **hỗ trợ cho vận hành** (việc ra quyết định cuối cùng vẫn là do con người), mang lại lợi ích tối ưu cho 3 phòng ban:
  1. **Phòng Nhân sự:** Phân bổ ca làm việc linh hoạt, vừa đủ người, tăng chất lượng phục vụ và giảm quỹ lương dư thừa.
  2. **Phòng Kho bãi/Chuỗi cung ứng:** Tự động lên kế hoạch nhập xuất nguyên vật liệu sát với nhu cầu thực tế, tránh tình trạng đứt gãy cung ứng hoặc tồn kho hỏng hóc.
  3. **Phòng Marketing:** Đưa ra các chiến dịch "Flash Sale" hoặc "Happy Hour" tự động kích cầu vào các khung giờ vắng khách được dự báo trước.

### 2.1. Phân tích chi tiết Business Case & Giá trị thực tiễn (Dành cho bảo vệ đồ án)
*Bản chất của bài toán này là: Thay vì đoán mò xem ngày mai đông hay vắng khách, chúng ta dùng AI để tính toán trước. Khi đã biết trước tương lai, công ty sẽ tiết kiệm được rất nhiều tiền và không bị lãng phí.*

**a. Giải quyết bài toán Nhân Sự (Tiết kiệm quỹ lương):**
- **Vấn đề:** Nếu xếp ca làm việc mà không biết trước lúc nào đông khách. Giờ vắng khách thì nhân viên đứng chơi (tốn tiền trả lương vô ích). Giờ đông khách thì làm không kịp (khách đợi lâu sẽ bực mình và bỏ đi).
- **Giải pháp:** AI sẽ tính toán và đề xuất số lượng nhân viên cần thiết cho từng khung giờ. Ban quản lý nhìn vào đề xuất này để cắt giảm nhân viên ở giờ vắng, điều thêm part-time vào giờ đông.

**b. Giải quyết bài toán Kho Bãi (Không để vốn bị "chôn" trong kho):**
- **Vấn đề:** Nếu nhập quá nhiều hàng (sữa, trái cây), hàng không bán hết sẽ bị hỏng và phải vứt đi. Tiền mua hàng bị kẹt trong kho. Nếu nhập quá ít thì lúc đông khách lại hết đồ bán.
- **Giải pháp:** Khi AI dự báo được lượng khách tuần tới, hệ thống tính ra cần chính xác bao nhiêu nguyên liệu. Quản lý kho chỉ nhập đúng số lượng đó, không bị thừa mứa lãng phí.

**c. Giải quyết bài toán Marketing (Kéo khách vào giờ ế):**
- **Vấn đề:** Việc tung khuyến mãi giảm giá vào lúc cửa hàng đã đông đúc sẵn là một sự lãng phí tiền bạc, vì lúc đó không giảm giá khách vẫn mua.
- **Giải pháp:** Hệ thống AI chỉ ra những "Khung giờ ế khách". Hệ thống gợi ý bật khuyến mãi 30% chỉ áp dụng đúng vào giờ ế này để lôi kéo khách hàng. Ngược lại vào giờ cao điểm, hệ thống nhắc nhở tắt khuyến mãi để thu lợi nhuận cao nhất.

**d. Góc Độ Kỹ Thuật (Kiến trúc & Hạ tầng):**
- **Sử dụng Cloud thay vì tự mua máy chủ (On-Premise):** Giống như đi "thuê nhà" thay vì "xây nhà", giúp tiết kiệm tiền đầu tư ban đầu (CAPEX). Khi lượng truy cập tăng vọt, Cloud tự động "nới rộng phòng" (Auto-scaling) ngay lập tức để hệ thống không sập.
- **SLA (Service Level Agreement):** Là "bản cam kết" chất lượng. Nhóm cam kết SLA Uptime 99.9%, hệ thống phải luôn sống và sẵn sàng phục vụ, trong 1 tháng chỉ được phép trục trặc vài phút.

*(Lưu ý: Dữ liệu AI sinh ra không tự ý quyết định thay con người, mà đóng vai trò như một "Cố vấn đắc lực" hỗ trợ ban quản lý ra quyết định).*

## 3. Mục tiêu & KPI

### 3.1. Mục tiêu tổng quát
Dự án thực hiện đồng thời 2 vai trò cốt lõi của CNTT trong doanh nghiệp (theo định hướng bài giảng):
1. **Xương sống vận hành (Operational Backbone):** Thiết lập nền tảng hạ tầng Cloud và luồng dữ liệu giao dịch POS tập trung, đảm bảo tính liên tục, ổn định và an toàn thông tin 24/7 cho toàn bộ 34+ chi nhánh của Ways Station.
2. **Nền tảng chuyển đổi số (Digital Platform):** Ứng dụng mô hình AI chuỗi thời gian (TSFM) để chuyển đổi quy trình ra quyết định từ trạng thái "phản ứng bị động theo kinh nghiệm thủ công" sang "chủ động dựa trên dữ liệu dự báo". Qua đó, tối ưu hóa đồng thời chi phí quỹ lương nhân sự, giảm thiểu tỷ lệ hao hụt hàng tồn kho và gia tăng doanh thu trong các khung giờ thấp điểm.

### 3.2. Mục tiêu cụ thể & Tiêu chí đo lường SMART (Bộ 7 Chỉ Số Trọng Yếu)
Bám sát yêu cầu của bài giảng về việc xác lập bộ chỉ số tối ưu (6–8 chỉ số trọng yếu) bao quát từ Hạ tầng (Reliability), Dữ liệu (Data Quality) đến Nghiệp vụ (Business Impact), nhóm tinh gọn thành 7 mục tiêu cụ thể và tiêu chí nghiệm thu SMART như sau:

1. **Mục tiêu AI & Mô hình: Cung cấp dự báo chính xác và kịp thời làm căn cứ điều hành**
   - *Chỉ số đo lường (KPI):* **MAPE < 10%** trên tập kiểm thử (độ chính xác dự báo tương đương > 90%); **Tầm nhìn (Forecasting Horizon): 7–14 ngày** (đáp ứng trọn vẹn chu trình lập lịch tuần); **Độ trễ suy luận (Inference Latency):** Real-time API < 500ms, Batch đêm < 30 phút.
   - *Hiện trạng (Baseline):* Sai số dự báo thủ công ~30%, tầm nhìn bị động chỉ biết trước trong ngày.
   - *Thời điểm đo lường:* Giai đoạn kiểm thử UAT và định kỳ hàng tháng sau Go-live.
   - *Bộ phận chịu trách nhiệm (Owner):* Đội ngũ phát triển AI (Data / AI Team).

2. **Mục tiêu Chất lượng Dữ liệu: Bảo đảm nguồn dữ liệu POS đạt chuẩn 4 tiêu chí (Đầy đủ – Kịp thời – Nhất quán – Chuẩn xác)**
   - *Chỉ số đo lường (KPI):* **Tính đầy đủ (Completeness) ≥ 99.5%** không thất thoát hóa đơn/giao dịch; **Tính kịp thời (Data Freshness): Trễ < 24 giờ** (hoàn tất đồng bộ dữ liệu lúc 01:00 AM mỗi ngày); **Tính nhất quán:** 100% dữ liệu đồng bộ chuẩn hóa theo Schema định sẵn của Data Warehouse.
   - *Hiện trạng (Baseline):* Dữ liệu POS hay bị sót (~90%) và trễ 2–3 ngày do lỗi mạng cục bộ tại chi nhánh.
   - *Thời điểm đo lường:* Kiểm tra đối soát tự động hàng ngày qua luồng ETL.
   - *Bộ phận chịu trách nhiệm (Owner):* Kỹ sư dữ liệu (Data Engineer).

3. **Mục tiêu Tính sẵn sàng Hạ tầng (SLA & SLO): Đảm bảo hệ thống vận hành liên tục, không làm gián đoạn bán hàng**
   - *Chỉ số đo lường (KPI):* **SLA Uptime cam kết ≥ 99.9%** (thời gian gián đoạn tối đa < 44 phút/tháng); **SLO nội bộ đội Ops ≥ 99.95%**; Ngưỡng tự động mở rộng tải (**Auto-scaling threshold**) kích hoạt khi CPU/RAM vượt 75%.
   - *Hiện trạng (Baseline):* Uptime chỉ đạt ~98.5% (máy chủ cục bộ tại chi nhánh thường xuyên chập chờn).
   - *Thời điểm đo lường:* Báo cáo nghiệm thu SLA định kỳ hàng tháng.
   - *Bộ phận chịu trách nhiệm (Owner):* Đội ngũ Vận hành Cloud / DevOps (Cloud Ops).

4. **Mục tiêu Vận hành & Quản trị sự cố (IT Ops): Phát hiện và khắc phục sự cố hệ thống siêu tốc**
   - *Chỉ số đo lường (KPI):* **MTTD ≤ 15 phút** (thời gian trung bình phát hiện qua Prometheus/Grafana); **MTTR ≤ 30 phút** (khôi phục dịch vụ nhờ Kubernetes tự phục hồi Pod); **Sự cố nghiêm trọng cấp P1 (sập hệ thống lõi) = 0 vụ/quý**; 100% ticket sự cố P2 được xử lý đúng SLA.
   - *Hiện trạng (Baseline):* MTTD ~120 phút, MTTR ~240 phút (phụ thuộc vào phản ánh thủ công và kỹ sư sửa lỗi bằng tay).
   - *Thời điểm đo lường:* Tổng kết sau 1, 3 và 6 tháng vận hành.
   - *Bộ phận chịu trách nhiệm (Owner):* IT Helpdesk & Đội ngũ DevOps.

5. **Mục tiêu An toàn Dữ liệu & Khôi phục sau thảm họa (DR & Security): Bảo toàn dữ liệu và dự phòng chuyển đổi tức thì**
   - *Chỉ số đo lường (KPI):* **RPO ≤ 1 giờ** (sao lưu dữ liệu tự động mỗi giờ); **RTO ≤ 2 giờ** (hạ tầng Cloud dự phòng sẵn sàng kích hoạt trong 2 tiếng); **Tỷ lệ sao lưu thành công (Backup Success Rate) ≥ 99.9%**; 100% quyền truy cập quản trị tuân thủ **RBAC** và lưu vết đầy đủ qua **Audit Log**.
   - *Hiện trạng (Baseline):* RPO = 24 giờ, RTO = 12 giờ (sao lưu thủ công, nguy cơ mất trắng dữ liệu kinh doanh trong ngày khi hỏng ổ cứng).
   - *Thời điểm đo lường:* Diễn tập kịch bản phục hồi thảm họa định kỳ 6 tháng/lần.
   - *Bộ phận chịu trách nhiệm (Owner):* Kỹ sư Quản trị hạ tầng (Infrastructure Lead).

6. **Mục tiêu Tối ưu hóa Nhân sự (HR Impact): Rút ngắn chu kỳ lập lịch và xóa bỏ lãng phí quỹ lương**
   - *Chỉ số đo lường (KPI):* **Tỷ lệ ca trực phát sinh lệch giảm ít nhất 30%** so với baseline; **Rút ngắn Cycle Time (thời gian hoàn tất lập lịch ca tuần) từ 3 ngày xuống dưới 2 giờ** (nhờ hệ thống tự động gợi ý số lượng nhân viên cần thiết).
   - *Hiện trạng (Baseline):* ~25% số ca trực bị phân bổ thừa hoặc thiếu nhân viên so với nhu cầu thực tế; quản lý mất nhiều ngày để xếp ca thủ công.
   - *Thời điểm đo lường:* Đo lại sau 1 tháng và 3 tháng Go-live.
   - *Bộ phận chịu trách nhiệm (Owner):* Trưởng phòng Nhân sự.

7. **Mục tiêu Tối ưu Kho bãi & Tăng trưởng Marketing: Giảm Cost-to-serve kho và kích cầu giờ thấp điểm**
   - *Chỉ số đo lường (KPI):* 
     - **Kho bãi:** Tỷ lệ hao hụt / hủy nguyên vật liệu tươi **giảm xuống < 3%** (baseline hiện trạng ~8–10% doanh số kho, giúp hạ thấp đáng kể chi phí phục vụ - Cost-to-serve).
     - **Marketing:** Doanh thu kích cầu khung giờ thấp điểm **tăng 15% đến 20%** (nhờ áp dụng khuyến mãi Flash Sale đúng khung giờ vắng khách do AI chỉ điểm).
   - *Thời điểm đo lường:* Quyết toán định kỳ sau 3 tháng và 6 tháng Go-live.
   - *Bộ phận chịu trách nhiệm (Owner):* Quản lý Kho & Trưởng phòng Marketing.

#### Checklist kiểm soát chất lượng KPI:
- [x] **Đúng số lượng chuẩn môn học:** Gói gọn trong đúng 7 chỉ số trọng yếu (khớp chuẩn 6–8 KPI theo bài giảng Chương 1).
- [x] **Bao quát đầy đủ 2 vai trò CNTT:** Operational Backbone (Hạ tầng, Dữ liệu, Vận hành tin cậy) và Digital Platform (AI, Nghiệp vụ).
- [x] **Có Baseline hiện tại & Target tương lai rõ ràng** cho từng chỉ số kỹ thuật và nghiệp vụ.
- [x] **Có thời điểm đo lường định kỳ** (UAT, sau go-live 1 tháng, 3 tháng, 6 tháng).
- [x] **Có "Owner" phân định trách nhiệm cụ thể** cho từng nhóm chỉ số (Data Team, DevOps, Phòng ban nghiệp vụ).
- [x] **Đảm bảo tính xuyên suốt (Traceability):** Ánh xạ trực tiếp 1-1 từ Bài toán Business Case (Mục 2) đến Tiêu chí nghiệm thu.

### 3.3. Chi tiết các công thức chuẩn được áp dụng
*(Toàn bộ các công thức dưới đây được chuẩn hóa theo tài liệu kỹ thuật quốc tế và giáo trình môn học)*

#### A. Các Độ Đo Đánh Giá Mô Hình Dự Báo (Time-Series Forecasting Metrics)
Trong các bài toán dự báo chuỗi thời gian, các độ đo giúp xác định mức độ sai lệch giữa giá trị dự báo ($\hat{y}_i$) do mô hình tạo ra và giá trị thực tế quan sát được ($y_i$) trên tổng số $n$ mẫu quan sát.

- **MAPE (Mean Absolute Percentage Error)**
  - *Định nghĩa:* Sai số tuyệt đối trung bình phần trăm. Cho biết dự báo lệch bao nhiêu % so với thực tế.
  - *Công thức:* $$ \text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\% $$
  - *Nguồn tham khảo chuẩn:* [[1]](#ref1)

- **MAE (Mean Absolute Error)**
  - *Định nghĩa:* Sai số tuyệt đối trung bình. Phản ánh quy mô sai lệch tuyệt đối theo đơn vị người/đơn hàng.
  - *Công thức:* $$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$
  - *Nguồn tham khảo chuẩn:* [[2]](#ref2)

- **RMSE (Root Mean Square Error)**
  - *Định nghĩa:* Căn bậc hai sai số toàn phương trung bình. Phạt nặng hơn các lỗi dự báo có độ sai lệch lớn.
  - *Công thức:* $$ \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} $$
  - *Nguồn tham khảo chuẩn:* [[3]](#ref3)

#### B. Các Chỉ Số Tính Sẵn Sàng & Quản Trị Vận Hành Hạ Tầng (Availability & IT Ops)
Đây là các chỉ số đánh giá độ tin cậy của nền tảng hạ tầng và năng lực ứng cứu sự cố của đội ngũ vận hành.

- **Availability / Uptime (Tính sẵn sàng dịch vụ theo SLA)**
  - *Định nghĩa:* Tỷ lệ phần trăm thời gian hệ thống hoạt động bình thường, không gián đoạn trong một chu kỳ đo lường (tháng).
  - *Công thức:* $$ \text{Availability (\%)} = \frac{T_{\text{tổng thời gian thỏa thuận}} - T_{\text{thời gian gián đoạn (Downtime)}}}{T_{\text{tổng thời gian thỏa thuận}}} \times 100\% $$
  - *Áp dụng cụ thể:* Với cam kết Uptime $\ge 99.9\%$ trong 1 tháng (30 ngày = 43,200 phút), tổng thời gian gián đoạn tối đa cho phép là: $$ \text{Downtime tối đa} \le 43,200 \times (1 - 0.999) = 43.2 \text{ phút/tháng} $$
  - *Nguồn tham khảo chuẩn:* [[7]](#ref7)

- **MTTD (Mean Time To Detect)**
  - *Định nghĩa:* Thời gian trung bình để hệ thống giám sát hoặc con người phát hiện ra sự cố kể từ lúc sự cố bắt đầu phát sinh.
  - *Công thức:* $$ \text{MTTD} = \frac{\sum_{j=1}^{m} (t_{\text{phát hiện, } j} - t_{\text{bắt đầu sự cố, } j})}{m} $$ *(với $m$ là tổng số sự cố ghi nhận)*.
  - *Nguồn tham khảo chuẩn:* [[4]](#ref4)

- **MTTR (Mean Time To Repair/Recovery)**
  - *Định nghĩa:* Thời gian trung bình để khắc phục, sửa chữa và khôi phục dịch vụ trở lại trạng thái hoạt động bình thường kể từ khi phát hiện sự cố.
  - *Công thức:* $$ \text{MTTR} = \frac{\text{Tổng thời gian hệ thống bị gián đoạn (Total Downtime)}}{\text{Tổng số lượng sự cố (m)}} $$
  - *Nguồn tham khảo chuẩn:* [[4]](#ref4)

#### C. Các Chỉ Số An Toàn Dữ Liệu & Khôi Phục Sau Thảm Họa (DR & Backup)
Bộ chỉ số đo lường năng lực bảo vệ dữ liệu nghiệp vụ và mức độ sẵn sàng của hạ tầng dự phòng khi xảy ra thảm họa (cháy nổ, mã độc ransomware, lỗi phần cứng trung tâm).

- **Backup Success Rate (Tỷ lệ sao lưu thành công)**
  - *Định nghĩa:* Tỷ lệ phần trăm các tác vụ sao lưu tự động hoàn thành trọn vẹn, không phát sinh lỗi và vượt qua kiểm tra tính toàn vẹn (Checksum verification).
  - *Công thức:* $$ \text{Backup Success Rate (\%)} = \frac{\text{Số lượng phiên backup thành công hợp lệ}}{\text{Tổng số lượng phiên backup đã lập lịch}} \times 100\% $$
  - *Nguồn tham khảo chuẩn:* [[8]](#ref8)

- **RPO (Recovery Point Objective)**
  - *Định nghĩa:* Mức độ mất mát dữ liệu tối đa chấp nhận được (tính bằng thời gian) khi có sự cố nghiêm trọng xảy ra.
  - *Mục tiêu cam kết:* $\text{RPO} \le 1 \text{ giờ}$ (chu kỳ kích hoạt cơ chế backup log/snapshot tự động mỗi giờ một lần).
  - *Nguồn tham khảo chuẩn:* [[5]](#ref5)

- **RTO (Recovery Time Objective)**
  - *Định nghĩa:* Thời gian tối đa cho phép để khôi phục toàn bộ dịch vụ hoạt động trở lại sau sự cố gián đoạn.
  - *Mục tiêu cam kết:* $\text{RTO} \le 2 \text{ giờ}$ (kịch bản chuyển đổi dự phòng sang môi trường Cloud được cấu hình tự động sẵn sàng tiếp quản dịch vụ).
  - *Nguồn tham khảo chuẩn:* [[6]](#ref6)

#### D. Các Chỉ Số Đo Lường Chất Lượng Dữ Liệu (Data Quality Metrics)
Bộ chỉ số bảo đảm nguồn dữ liệu thu thập từ máy tính tiền POS đáp ứng tiêu chuẩn "Dữ liệu sạch" trước khi nạp vào mô hình AI huấn luyện và suy luận.

- **Data Completeness (Tính đầy đủ của dữ liệu)**
  - *Định nghĩa:* Tỷ lệ phần trăm bản ghi giao dịch thu nhận thành công tại Data Warehouse so với tổng số lượng giao dịch thực tế phát sinh tại điểm bán POS.
  - *Công thức:* $$ \text{Completeness (\%)} = \frac{\text{Số bản ghi giao dịch hợp lệ ghi nhận tại DWH}}{\text{Tổng số bản ghi giao dịch thực tế phát sinh tại máy POS chi nhánh}} \times 100\% $$
  - *Mục tiêu cam kết:* $\text{Completeness} \ge 99.5\%$ (cho phép dung sai tối đa 0.5% do độ trễ truyền gói tin mạng cục bộ).
  - *Nguồn tham khảo chuẩn:* [[9]](#ref9)

- **Data Freshness (Tính kịp thời của dữ liệu)**
  - *Định nghĩa:* Khoảng cách thời gian kể từ thời điểm giao dịch thực tế phát sinh tại quầy ($t_{\text{pos}}$) cho đến khi dữ liệu được làm sạch và sẵn sàng phục vụ mô hình AI ($t_{\text{dwh}}$).
  - *Công thức:* $$ \Delta t_{\text{freshness}} = t_{\text{dwh}} - t_{\text{pos}} \le 24 \text{ giờ} $$
  - *Nguồn tham khảo chuẩn:* [[9]](#ref9)

#### E. Các Chỉ Số Đo Lường Hiệu Quả Quy Trình Nghiệp Vụ (Business Process Metrics)
Định lượng hóa giá trị mang lại cho ban điều hành và các phòng ban sau khi áp dụng hệ thống dự báo.

- **Cycle Time (Thời gian chu kỳ lập lịch ca trực tuần của Phòng Nhân sự)**
  - *Định nghĩa:* Tổng thời gian cần thiết để hoàn tất chu trình lập và phê duyệt lịch làm việc theo tuần cho toàn bộ nhân viên các chi nhánh.
  - *Công thức:* $$ \text{Cycle Time} = T_{\text{hoàn tất phê duyệt lịch ca}} - T_{\text{bắt đầu trích xuất dữ liệu dự báo}} $$
  - *Mục tiêu cam kết:* Rút ngắn từ $\text{Baseline} = 72 \text{ giờ}$ (3 ngày thủ công) xuống $\text{TO-BE} \le 2 \text{ giờ}$.
  - *Nguồn tham khảo chuẩn:* [[10]](#ref10)

- **Tỷ lệ giảm ca trực phát sinh lệch (Shift Variance Reduction Rate)**
  - *Định nghĩa:* Tỷ lệ phần trăm cắt giảm các ca làm việc bị thiếu hụt hoặc dư thừa nhân sự so với nhu cầu thực tế.
  - *Công thức:* $$ \Delta \text{Lệch} = \frac{\text{Tỷ lệ ca lệch (Baseline)} - \text{Tỷ lệ ca lệch (TO-BE)}}{\text{Tỷ lệ ca lệch (Baseline)}} \times 100\% $$
  - *Nguồn tham khảo chuẩn:* [[10]](#ref10)

## 4. Đối tượng áp dụng, phạm vi (In/Out-of-scope), giả định/ràng buộc
- **In-scope:** 
  - Thu thập dữ liệu từ hệ thống máy POS tại toàn bộ các chi nhánh.
  - Xây dựng Data Pipeline làm sạch và chuẩn hóa dữ liệu tập trung.
  - Triển khai mô hình AI dự báo chuỗi thời gian (TSFM) trên hạ tầng Cloud.
  - Phát triển API cung cấp kết quả dự báo cho 3 phòng ban (Nhân sự, Marketing, Kho).
- **Out-of-scope:** Không can thiệp thay đổi kiến trúc phần mềm quản lý kho hoặc ERP hiện tại của doanh nghiệp, chỉ thực hiện kết nối tích hợp qua API Gateway.
- **Giả định/Ràng buộc:** Dữ liệu đầu vào từ các máy POS tại các chi nhánh phải được đồng bộ tập trung ít nhất 1 lần/ngày vào Data Warehouse.

## 5. Danh mục tài liệu tham khảo
<a id="ref1"></a>[1] Scikit-Learn (n.d.), *Mean absolute percentage error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-percentage-error
<a id="ref2"></a>[2] Scikit-Learn (n.d.), *Mean absolute error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-error
<a id="ref3"></a>[3] Scikit-Learn (n.d.), *Mean squared error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-squared-error
<a id="ref4"></a>[4] Atlassian ITSM (n.d.), *Incident Management Metrics (MTTD, MTTR)*, truy cập tại: https://www.atlassian.com/incident-management/kpis/common-metrics
<a id="ref5"></a>[5] IBM (n.d.), *What is RPO and RTO?*, truy cập tại: https://www.ibm.com/topics/rpo-rto
<a id="ref6"></a>[6] AWS (n.d.), *Disaster Recovery Objectives (RTO and RPO)*, truy cập tại: https://aws.amazon.com/disaster-recovery/
<a id="ref7"></a>[7] Google Cloud (n.d.), *Site Reliability Engineering (SRE) - Availability Table and Metrics*, truy cập tại: https://sre.google/sre-book/availability-table/
<a id="ref8"></a>[8] National Institute of Standards and Technology - NIST (2010), *Contingency Planning Guide for Federal Information Systems (NIST SP 800-34 Rev. 1)*, truy cập tại: https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final
<a id="ref9"></a>[9] ISO/IEC (2008), *ISO/IEC 25012: Data quality model (Software and Systems Engineering - Software product Quality Requirements and Evaluation)*, truy cập tại: https://www.iso.org/standard/35736.html
<a id="ref10"></a>[10] APQC (n.d.), *Process Performance Metric - Cycle Time and Efficiency Standards*, American Productivity & Quality Center, truy cập tại: https://www.apqc.org/benchmarking-portal
