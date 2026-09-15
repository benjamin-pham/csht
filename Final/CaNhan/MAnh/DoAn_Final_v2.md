# 1. Tóm tắt điều hành (Executive Summary)

**ĐỒ ÁN MÔN HỌC: ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT**
**Dự án:** Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station

Dự án này đề xuất đầu tư Nền tảng tích hợp ứng dụng (Lớp 4), Nền tảng dữ liệu tập trung (Lớp 5) và 02 thành phần thiết yếu của Lớp 3 (Quản lý định danh IAM/SSO và Mã hóa dữ liệu cá nhân) cho chuỗi Ways Station, nhằm giải quyết các thách thức nghiêm trọng về đứt gãy tích hợp, phân mảnh dữ liệu và rủi ro rò rỉ dữ liệu cá nhân (PII - Personally Identifiable Information) trên 34 chi nhánh.

Thông qua việc đánh giá 3 kịch bản kiến trúc, dự án lựa chọn mô hình **Hybrid Cloud (Lai)** làm giải pháp tối ưu. Mô hình này kết hợp khả năng xử lý mạnh mẽ của điện toán đám mây cho phân tích dữ liệu và sự ổn định của hệ thống máy chủ tại các chi nhánh (Edge Cluster), đảm bảo duy trì hoạt động bán hàng ngay cả khi mất kết nối mạng, đồng thời tuân thủ nghiêm ngặt các quy định về bảo mật dữ liệu (Nghị định 13/2023/NĐ-CP).

Dự án được lên kế hoạch triển khai trong vòng 16 tuần (4 tháng) với 5 pha rõ ràng. Tổng mức đầu tư (CAPEX - Capital Expenditure) là **1.308.800.000 VNĐ**, và Tổng chi phí sở hữu (TCO - Total Cost of Ownership) trong 3 năm dự kiến là **5.209.160.000 VNĐ** — tương đương **khoảng 1,45% doanh thu chuỗi trong cùng kỳ**. Lợi ích quy đổi ước tính **~1.955.000.000 VNĐ/năm**, cho thời gian hoàn vốn trên dòng tiền ròng khoảng **1,7 năm**.

**Khuyến nghị:** Ban Giám đốc phê duyệt chủ trương đầu tư và ngân sách CAPEX 1.308.800.000 VNĐ (chưa gồm dự phòng 10%), khởi động Pha 1 ngay trong quý tới. Rủi ro lớn nhất của phương án "không đầu tư" không nằm ở chi phí mà ở nghĩa vụ tuân thủ Nghị định 13/2023/NĐ-CP, với mức phạt có thể lên đến 5% tổng doanh thu.

---

# 2. Hiện trạng AS-IS & vấn đề

## 2.0. Phương pháp khảo sát và nguồn số liệu

Nhóm thực hiện không có quyền truy cập trực tiếp vào hệ thống vận hành và số liệu tài chính nội bộ của Ways Station. Do đó, hiện trạng AS-IS được xây dựng bằng phương pháp **mô phỏng có căn cứ (evidence-based simulation)**, kết hợp ba nguồn:

1. **Tài liệu quy trình vận hành nội bộ của Ways Station** (nguồn sơ cấp): 08 bộ tài liệu đào tạo/quy trình chuẩn đang áp dụng tại chi nhánh — `GIỮ XE`, `THU NGÂN GYM`, `THU NGÂN NET + BIDA`, `THU NGÂN NET + HUB`, `PHỤC VỤ GYM`, `PHỤC VỤ BIDA`, `PHỤC VỤ CẦU LÔNG`, `PHỤC VỤ NET`. Chi tiết trích dẫn tại **Phụ lục A**.
2. **Chuẩn ngành và khung đo lường quốc tế** cho các ngưỡng mục tiêu (Google SRE, Atlassian ITSM, AWS DR, ISO/IEC 25012, NIST SP 800-175B).
3. **Nguyên lý kỹ thuật phổ quát** để suy luận các chỉ số không quan sát trực tiếp được (tỉ lệ backup thành công, độ trễ tổng hợp dữ liệu).

Các số liệu được đánh dấu **[MC]** là có minh chứng trực tiếp từ tài liệu nội bộ; **[SL]** là suy luận có căn cứ từ nguồn (2) và (3) và cần được xác nhận lại trong giai đoạn khảo sát chi tiết (Pha 1).

## 2.1. Khảo sát hiện trạng hạ tầng (AS-IS) có số liệu

**Sơ đồ kiến trúc hiện tại (AS-IS):**

```
   34 CHI NHÁNH (34 hộ kinh doanh cá thể - 34 "ốc đảo" dữ liệu)
 ┌──────────────┐  ┌──────────────┐          ┌──────────────┐
 │  Chi nhánh 1 │  │  Chi nhánh 2 │   ...    │ Chi nhánh 34 │
 │ POS Net      │  │ POS Net      │          │ POS Net      │
 │ POS Bida     │  │ PM MODUN Gym │          │ POS Bida     │
 │ PM MODUN Gym │  │ ACB portal   │          │ PM Cầu lông  │
 │ PM Kho       │  │ PM Kho       │          │ PM Kho       │
 │ Sổ giao ca   │  │ Sổ giao ca   │          │ Sổ giao ca   │
 └──────┬───────┘  └──────┬───────┘          └──────┬───────┘
        │ (không có API — 0% tích hợp tự động)      │
        ▼                 ▼                          ▼
   ╔═══════════════════════════════════════════════════════╗
   ║   3 KÊNH THỦ CÔNG:  Tổng đài 0889 555 559 (phím 2/3/8)║
   ║                     Zalo cá nhân nhân viên            ║
   ║                     Sổ giấy / biên bản giấy           ║
   ╚═══════════════════════════════════════════════════════╝
        │                                           │
        ▼                                           ▼
 ┌───────────────────┐                   ┌────────────────────────┐
 │ Phòng ban HQ      │                   │ Ảnh CCCD, cà vẹt xe,   │
 │ (NS/Điều phối/Kho)│                   │ Face ID lưu trên điện  │
 │ Excel thủ công    │                   │ thoại cá nhân (0% mã   │
 │ ~2.500 giờ/năm    │                   │ hóa) → RỦI RO NĐ13     │
 │ Trễ 24-48h        │                   └────────────────────────┘
 └───────────────────┘
```

**Điểm nghẽn hiện trạng (Baseline có định lượng):**

- **Điểm nghẽn 1 — Tích hợp & Vận hành (Lớp 4 - App & Integration Platform):** 34 chi nhánh sở hữu 8 hệ thống phần mềm rời rạc (POS - Point of Sale cho Net/Bida/Cầu lông, PM MODUN Gym, ACB portal, Nhân sự Ways `ns.ways.vn`, PM Kho...) hoạt động độc lập và phân mảnh **[MC]**. Tỉ lệ luồng tích hợp tự động là **0%**. 100% giao tiếp liên phòng ban đi qua 3 kênh thủ công: tổng đài duy nhất 0889 555 559 phân luồng theo phím số, Zalo, và sổ giao ca giấy **[MC]**.
- **Điểm nghẽn 2 — Dữ liệu & Quyết định (Lớp 5 - Data Platform):** Không có kho dữ liệu tập trung. Báo cáo được làm thủ công bằng Excel tiêu tốn **~2.500 giờ công/năm** **[SL]**. Độ trễ dữ liệu phục vụ quản trị lên tới **24 - 48 giờ** **[SL]**. Tỷ lệ sai lệch số liệu doanh thu khi đối soát là **3,8%** **[SL]**.
- **Điểm nghẽn 3 — Bảo mật & Định danh (02 thành phần Lớp 3 trong phạm vi đầu tư):** Khách hàng phải dùng tài khoản riêng cho từng mảng dịch vụ; nhân viên phải được hỗ trợ đăng nhập riêng cho từng phần mềm **[MC]**. Đáng lưu ý, 100% ảnh giấy tờ tùy thân của khách hàng (CCCD, cà vẹt xe) được chụp và gửi qua Zalo cá nhân của nhân viên cho quản lý, không có cơ chế mã hóa **[MC]**; dữ liệu sinh trắc học Face ID được thu thập tại quầy lễ tân phòng gym **[MC]**. Sao lưu cục bộ có tỉ lệ thành công chỉ **47%** với RPO (Recovery Point Objective) lên đến 24 giờ **[SL]**.

## 2.2. Nêu vấn đề và rủi ro nếu không đầu tư (WHY NOW?)

Từ các điểm nghẽn hiện trạng, hệ thống đang phải đối mặt với nhiều hạn chế kỹ thuật và rủi ro lớn nếu không được giải quyết ngay:

- **Rủi ro vận hành (Vấn đề 1 - Đứt gãy tích hợp):** Việc thiếu API (Application Programming Interface) Gateway khiến hệ thống chịu tải kém vào giờ cao điểm, gây gián đoạn bán hàng. Thời gian phát hiện sự cố chậm (4-8 giờ) do phụ thuộc vào việc nhân viên chi nhánh chủ động báo lỗi qua Zalo/tổng đài. Hàng ngàn giờ công bị lãng phí do đối soát thủ công và nhập liệu kép.
- **Rủi ro chiến lược (Vấn đề 2 - Mù dữ liệu thực thời):** Độ trễ dữ liệu 48 giờ khiến việc ra quyết định bị chậm trễ. Việc thiếu nguồn dữ liệu chuẩn hóa và tập trung để phân tích và dự báo nhu cầu dẫn đến lãng phí nguyên vật liệu F&B (Food and Beverage) và sai lệch trong việc sắp xếp ca trực của nhân viên. Không thể bán chéo dịch vụ giữa 5 mảng (Gym, Gaming, Billiards, Cầu lông, Hub) do khách hàng không có định danh duy nhất (SSO - Single Sign-On).
- **Rủi ro tuân thủ (Vấn đề 3 - Lỗ hổng bảo mật PII):** Việc lưu trữ dữ liệu cá nhân (PII) như ảnh CCCD, Face ID phân tán trên điện thoại cá nhân vi phạm nghiêm trọng **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân. Doanh nghiệp đối mặt với rủi ro bị phạt lên đến 5% tổng doanh thu và đánh mất uy tín thương hiệu. Đây là rủi ro **không thể trì hoãn**, vì mức độ phơi nhiễm tăng tuyến tính theo số lượt khách và số chi nhánh mới mở.

---

# 3. Mục tiêu & KPI (Key Performance Indicator) TO-BE

Bộ KPI kỹ thuật được thiết lập theo chuẩn quốc tế nhằm giải quyết triệt để 3 vấn đề nêu trên. Mỗi KPI sử dụng **tên độ đo đã được chuẩn hóa**, có **công thức tính**, **giá trị baseline hiện tại**, **mốc thời điểm đo** và **người chịu trách nhiệm số liệu (owner)**.

## 3.1. Ma trận Truy vết: Vấn đề → Mục tiêu → KPI → Baseline → Target → Mốc đo

| Mã | Vấn đề giải quyết | Mục tiêu kiến trúc | Tên độ đo chuẩn | Baseline hiện tại | Target | Mốc đo | Owner | Căn cứ nghiệm thu |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **1.1** | VĐ1: Đứt gãy tích hợp, gián đoạn kinh doanh | Nền tảng đạt độ sẵn sàng cao | **Availability / Uptime** [4] | Không đo lường được; SPOF = 100% chi nhánh | ≥ 99,99% (downtime ≤ 4,32 phút/tháng) | M5; +1/+3/+6 tháng | Infra Lead / SRE | Báo cáo uptime từ Cloud provider + Prometheus, 3 tháng liên tục |
| **1.2** | VĐ1: Sự cố kéo dài, phát hiện chậm | Hệ thống tự phục hồi (Self-healing) | **MTTR — Mean Time To Recovery** [2] | Phát hiện 4–8h; khắc phục 12–24h | ≤ 30 phút | M5; +3 tháng | Infra Lead / SRE | Log Kubernetes tự khởi tạo lại service + ticket ITSM (Jira) |
| **2.1** | VĐ2: Mù dữ liệu thực thời | Dữ liệu chuẩn thời gian thực cho kho dữ liệu | **Data Freshness — luồng CDC giao dịch** [5] | 24–48 giờ | ≤ 5 giây | M3; M5; +1 tháng | Data Lead | Đối soát timestamp giao dịch tại CN với bản ghi trên Data Lakehouse |
| **2.2** | VĐ2: Báo cáo thủ công, sai lệch số liệu | Luồng dữ liệu đầy đủ và tin cậy | **Pipeline Success Rate & Data Completeness** [5] | Sai lệch đối soát doanh thu 3,8%; 2.500 giờ công/năm | Completeness ≥ 99,5%; sai lệch đối soát < 0,5% | M4; M5; +3 tháng | Data Lead | Báo cáo đối soát doanh thu hàng tháng + log Airflow |
| **3.1** | VĐ3: Lỗ hổng rò rỉ dữ liệu PII | Ngăn chặn rò rỉ PII, tuân thủ NĐ13 | **Encryption Coverage** [6] | 0% (ảnh CCCD/Face ID qua Zalo cá nhân) | 100% at-rest và in-transit | M3; M5; +6 tháng | Security Lead | Audit DB + scan SSL/TLS + báo cáo pentest |
| **3.2** | VĐ3: Mất dữ liệu khi thảm họa | Không mất mát dữ liệu quan trọng | **RPO — Recovery Point Objective** [3] | 24 giờ; tỉ lệ backup thành công 47% | RPO ≤ 15 phút; backup success ≥ 99% | M2; M5; DR Drill 6 tháng/lần | Infra Lead / SRE | Biên bản DR Drill + test restore PITR |

**Tiêu chí thành công tổng thể:** dự án được nghiệm thu khi đạt **6/6 KPI tại mốc M5 (Go-live)** và duy trì tối thiểu **5/6 KPI tại mốc +3 tháng** sau Go-live.

## 3.2. Định lượng KPI theo công thức chuẩn (Standards)

1. **KPI 1.1 — Tính sẵn sàng (Availability / Uptime) ≥ 99,99%** *(Chuẩn Google SRE - Site Reliability Engineering [4])*
   - *Công thức:* $Uptime = \frac{\text{Total Time} - \text{Downtime}}{\text{Total Time}} \times 100\%$
   - *Ràng buộc:* Tổng thời gian chết (Downtime) trong 1 tháng (43.200 phút) không vượt quá 4,32 phút.

2. **KPI 1.2 — Thời gian khôi phục trung bình (MTTR) ≤ 30 phút** *(Chuẩn Atlassian ITSM - IT Service Management [2])*
   - *Công thức:* $MTTR = \frac{\text{Tổng thời gian gián đoạn (Downtime)}}{\text{Tổng số lượng sự cố}}$
   - *Ý nghĩa:* Hệ thống (Kubernetes) phải tự động khởi tạo lại service lỗi trong vài phút trước khi ảnh hưởng diện rộng.

3. **KPI 2.1 — Độ trễ dữ liệu, luồng CDC giao dịch (Data Freshness / Currentness) ≤ 5 giây** *(Chuẩn ISO/IEC 25012 — thuộc tính Currentness [5])*
   - *Công thức:* $\Delta t_{freshness} = t_{DataLakehouse} - t_{POS} \le 5s$
   - *Phạm vi độ đo:* chỉ áp dụng cho **luồng CDC (Change Data Capture) giao dịch thời gian thực** của nền tảng dữ liệu. Không áp dụng cho luồng batch huấn luyện mô hình AI — xem mục 3.4.

4. **KPI 2.2 — Chất lượng luồng dữ liệu (Pipeline Success Rate & Data Completeness)** *(Chuẩn ISO/IEC 25012 — thuộc tính Completeness [5])*
   - *Công thức:* $\text{Completeness} = \frac{\text{Số bản ghi nạp thành công vào Data Lakehouse}}{\text{Tổng số bản ghi gốc phát sinh tại POS}} \times 100\% \ge 99{,}5\%$
   - *Ràng buộc bổ sung:* tỷ lệ sai lệch khi đối soát doanh thu giữa POS chi nhánh và Data Lakehouse giảm từ **3,8% xuống dưới 0,5%**.
   - *Lý do chọn độ đo này:* đây là KPI đo đúng **năng lực của Lớp 5 (nền tảng dữ liệu)** — thứ mà dự án đầu tư. Độ chính xác của mô hình dự báo (MAPE) là chỉ số của *sản phẩm phần mềm chạy trên nền tảng*, được đặc tả tại mục 3.4.

5. **KPI 3.1 — Tỷ lệ mã hóa dữ liệu PII = 100%** *(Chuẩn NIST SP 800-175B [6])*
   - *Công thức:* $\text{Encryption Coverage} = \frac{\text{Số trường PII được mã hóa AES-256}}{\text{Tổng số trường PII trong hệ thống}} \times 100\%$
   - *Ràng buộc:* Toàn bộ dữ liệu nhạy cảm (ảnh CCCD, Face ID, số điện thoại) phải được mã hóa 100% cả khi lưu trữ (at-rest) và khi truyền tải (in-transit), chuyển từ hiện trạng 0% sang mục tiêu 100%.

6. **KPI 3.2 — Mục tiêu điểm khôi phục (RPO) ≤ 15 phút** *(Chuẩn AWS Disaster Recovery [3])*
   - *Công thức:* $RPO = t_{\text{sự cố}} - t_{\text{bản sao lưu gần nhất}} \le 15\ \text{phút}$
   - *Ý nghĩa:* Dung sai mất mát dữ liệu tối đa tính từ thời điểm thảm họa xảy ra là 15 phút.

## 3.3. Tiêu chí nghiệm thu bổ sung không thuộc bộ KPI nền tảng

Mô hình AI dự báo lưu lượng khách chạy trên nền tảng phải đạt **MAPE < 15%** trên tập kiểm thử tại thời điểm nghiệm thu Pilot 5 chi nhánh (Pha 4, cuối T13). Đây là **tiêu chí nghiệm thu hạng mục**, không phải KPI nền tảng: đồ án chỉ cam kết *điều kiện dữ liệu đầu vào* (KPI 2.1 và 2.2) để mô hình đạt được ngưỡng này.

## 3.4. Phân định phạm vi KPI với đề tài thực hành cùng nhóm

Nhóm thực hiện song song hai đề tài trên cùng doanh nghiệp Ways Station. Ranh giới đo lường được phân định như sau để tránh trùng lặp và mâu thuẫn số liệu:

| Tiêu chí | Đồ án môn học (tài liệu này) | Bài thực hành |
|:---|:---|:---|
| **Đối tượng đo** | Năng lực nền tảng: API Gateway, Kafka, Edge Cluster, Data Lakehouse, IAM | Sản phẩm phần mềm: Forecast Service, Data Pipeline batch, mô hình AI |
| **Uptime** | ≥ 99,99% (nền tảng) | ≥ 99,9% (ứng dụng — hao hụt tầng dịch vụ nằm trong ngân sách sẵn sàng của nền tảng) |
| **Độ trễ dữ liệu** | Data Freshness luồng CDC ≤ 5s | Batch Data Freshness luồng huấn luyện ≤ 24h |
| **Độ trễ dự báo** | API dự báo end-to-end P95 ≤ 500ms (TR-P07) | Model inference thuần ≤ 200ms (nằm trong 500ms) |
| **Độ chính xác mô hình** | Không phải KPI; chỉ là tiêu chí nghiệm thu Pilot (MAPE < 15%) | KPI lõi: MAPE < 15% tại Pilot → < 10% sau go-live 3 tháng |

Chất lượng của riêng mô hình AI (MAPE, MAE, Precision, inference latency) được đặc tả và nghiệm thu trong đề tài thực hành *"Ứng dụng AI Time-Series Forecasting dự báo lưu lượng khách hàng đa chi nhánh"*. Đồ án chỉ cam kết các điều kiện hạ tầng để mô hình đạt được các chỉ số đó.

---

# 4. Phạm vi & giả định / ràng buộc

## 4.1. Khảo sát tổng quan doanh nghiệp

- **Tên đơn vị thụ hưởng:** Chuỗi Ways Station — hệ sinh thái dịch vụ giải trí & thể thao tích hợp đa nền tảng.
- **Quy mô và phạm vi hoạt động:** 34 chi nhánh trên địa bàn TP. Hồ Chí Minh và vùng lân cận, phát triển từ quy mô khoảng 22 chi nhánh trong vòng 2 năm gần nhất. Mỗi chi nhánh vận hành đồng thời nhiều mảng dịch vụ: **Gym (24/7), Gaming/Net, Billiards, Cầu lông, Hub (không gian làm việc), Giữ xe** và dịch vụ F&B kèm theo **[MC]**.
- **Đặc điểm mô hình pháp lý — yếu tố quyết định kiến trúc:** mỗi chi nhánh được đăng ký dưới hình thức **hộ kinh doanh cá thể riêng biệt**. Mô hình này tối ưu về thuế và linh hoạt pháp lý, nhưng khiến hạ tầng CNTT bị chia cắt thành **34 "ốc đảo" dữ liệu độc lập**, không tồn tại một pháp nhân trung tâm sở hữu kho dữ liệu chung.
- **Cơ cấu tổ chức:** Trụ sở chính (HQ) gồm các phòng ban tập trung — **Phòng Nhân sự** (tuyển dụng, đào tạo, ký quỹ, đồng phục, chấm công, tính lương), **Phòng Điều phối** (lịch làm việc, ca phát sinh, nghỉ phép, vân tay chấm công in/out), **Bộ phận Kho hàng** (vật tư, hỗ trợ đăng nhập phần mềm) — điều hành 34 chi nhánh thông qua đội ngũ **Quản lý chi nhánh**, dưới là các vị trí vận hành (Thu ngân, Phục vụ, Giữ xe) **[MC]**.
- **Quy trình hoạt động hiện hành:** đã được chuẩn hóa thành 08 bộ tài liệu SOP bắt buộc học thuộc theo từng vị trí. Toàn bộ liên lạc giữa chi nhánh và HQ đi qua **một tổng đài duy nhất (0889 555 559), phân luồng bằng phím số theo phòng ban**; hồ sơ nhân sự qua cổng `ns.ways.vn`; sự vụ phát sinh qua Zalo và sổ giao ca giấy **[MC]**.
- **Tài liệu minh chứng:** xem **Phụ lục A — Danh mục minh chứng hiện trạng**.

## 4.2. Phạm vi đầu tư (Lớp năng lực)

Dự án **không đề xuất mua sắm thiết bị rời rạc**, mà đầu tư theo lớp năng lực hạ tầng:

| Lớp năng lực | Thành phần **trong** phạm vi | Thành phần **ngoài** phạm vi |
|:---|:---|:---|
| **Lớp 4 — Nền tảng ứng dụng & tích hợp** | API Gateway, Message Queue (Kafka), Container/K8s (Cloud + Edge K3s), CI/CD | Virtualization/hypervisor nâng cấp |
| **Lớp 5 — Nền tảng dữ liệu** | Data Lakehouse/DWH, ETL/ELT (Airflow), CDC Streaming, data quality | Data catalog, data governance nâng cao (giai đoạn sau) |
| **Lớp 3 — Bảo mật & danh tính (chỉ 02 thành phần)** | **IAM/SSO/MFA (Keycloak)**, **Mã hóa dữ liệu PII (at-rest/in-transit)** | PAM, EDR/XDR, SIEM/SOC, DLP — chưa đầu tư kỳ này |
| **Lớp 1 — Compute/Storage/Network** | Kế thừa hạ tầng mạng và phần cứng hiện có; chỉ bổ sung Edge Server và thiết bị mạng tại HQ | Không nâng cấp đường truyền lõi, không đầu tư SAN/NAS |
| **Lớp 2 — Nền tảng vận hành** | Monitoring/Observability, CMDB, backup/DR, patching phục vụ trực tiếp Lớp 4 & 5 | ITSM toàn doanh nghiệp, FinOps chuyên sâu |

> **Lưu ý về tính nhất quán:** 02 thành phần Lớp 3 được đưa vào phạm vi vì Vấn đề 3 (rò rỉ PII) không thể giải quyết chỉ bằng Lớp 4 và Lớp 5. Toàn bộ KPI 3.1, 3.2, các yêu cầu TR-S01→TR-S08 và hạng mục Keycloak trong BOM đều thuộc phạm vi đã khai báo tại bảng này.

## 4.3. Đối tượng thụ hưởng

| Nhóm đối tượng | Quy mô | Giá trị nhận được |
|:---|:---|:---|
| Ban Điều hành / Ban Giám đốc | ~5–8 người | Báo cáo doanh thu, tồn kho, lưu lượng khách theo thời gian thực thay cho báo cáo trễ 24–48 giờ |
| Quản lý chi nhánh | 34 người | Một tài khoản SSO duy nhất thay cho nhiều lần đăng nhập rời rạc; dashboard chi nhánh |
| Phòng Nhân sự / Điều phối / Kho (HQ) | ~15–20 người | Xóa bỏ đối soát và nhập liệu kép; giải phóng ~2.500 giờ công/năm |
| Nhân viên vận hành tại chi nhánh | ~250–300 người | Hệ thống tính giờ/thanh toán vẫn hoạt động khi mất mạng (offline mode) |
| Khách hàng | Toàn bộ hội viên | Một định danh duy nhất cho cả 5 mảng dịch vụ; dữ liệu CCCD/Face ID được mã hóa |

## 4.4. Thời gian và giả định / ràng buộc

- **Thời gian đầu tư:** 16 tuần triển khai (4 tháng), theo sau là 12 tháng vận hành có bảo hành. Chu kỳ đánh giá TCO: 3 năm.
- **Giả định:** (a) doanh nghiệp giữ nguyên mô hình 34 hộ kinh doanh cá thể trong chu kỳ dự án; (b) đường truyền Internet hiện có tại chi nhánh đủ ổn định cho CDC sau khi nâng băng thông; (c) 8 hệ thống phần mềm hiện hữu cho phép truy cập cơ sở dữ liệu hoặc có sẵn API ở mức tối thiểu.
- **Ràng buộc:** (a) điểm bán phải tiếp tục tính tiền được khi mất kết nối Internet; (b) dữ liệu PII phải lưu trữ trong lãnh thổ Việt Nam và do doanh nghiệp tự kiểm soát theo Nghị định 13/2023/NĐ-CP; (c) ngân sách CAPEX phù hợp doanh nghiệp vừa (SMB), ưu tiên mã nguồn mở; (d) không có đội ngũ IT thường trực tại chi nhánh.

---

# 5. Các phương án kiến trúc (On-prem / Hybrid / Cloud) + so sánh

Để thỏa mãn bộ KPI khắt khe trên đồng thời đảm bảo đặc thù nghiệp vụ, dự án phân tích 3 kịch bản kiến trúc.

## 5.1. Mô tả ba kịch bản

### Kịch bản A — On-Premise 100% (nâng cấp tập trung)
- **Kiến trúc theo lớp:** Lớp 1 — cụm máy chủ vật lý tại HQ + máy chủ nhỏ tại từng chi nhánh; Lớp 4 — API Gateway và Kafka tự vận hành trên cụm HQ; Lớp 5 — DWH trên PostgreSQL vật lý; Lớp 3 — Keycloak + PII DB tại HQ.
- **HA/DR:** Active-Standby tại một site duy nhất. Muốn Active-Active phải đầu tư site thứ hai (chi phí nhân đôi). Backup immutability khó đạt vì thiếu object storage có WORM.
- **Tích hợp:** SSO, log, monitoring đều tự vận hành; phụ thuộc hoàn toàn vào năng lực đội IT nội bộ.
- **Khả năng mở rộng:** tuyến tính theo phần cứng — mở chi nhánh thứ 35 cần mua thêm thiết bị và cấu hình thủ công.
- **Ưu:** kiểm soát dữ liệu tuyệt đối, tuân thủ NĐ13 dễ dàng, hoạt động offline tốt. **Nhược:** CAPEX rất cao (~2,8 tỷ), không auto-scaling, DR yếu.

### Kịch bản B — Cloud-Native 100% (thuần đám mây)
- **Kiến trúc theo lớp:** toàn bộ Lớp 4 và Lớp 5 chạy trên Managed K8s, Managed Kafka, Managed PostgreSQL, Object Storage; chi nhánh chỉ còn thiết bị đầu cuối kết nối Internet.
- **HA/DR:** Active-Active đa vùng sẵn có, backup immutable sẵn có — điểm mạnh nhất của kịch bản này.
- **Tích hợp:** SSO, log, monitoring đều là dịch vụ quản trị, triển khai nhanh.
- **Khả năng mở rộng:** auto-scaling theo tải, mở chi nhánh mới gần như tức thời.
- **Ưu:** CAPEX thấp nhất (~650tr), agility cao nhất. **Nhược:** **mất mạng là mất doanh thu ngay lập tức** — không chấp nhận được với mô hình tính tiền theo giờ; dữ liệu PII đặt trên hạ tầng bên thứ ba gây rủi ro tuân thủ NĐ13; OPEX cao nhất.

### Kịch bản C — Hybrid Cloud (Lai) — **Khuyến nghị**
- **Kiến trúc theo lớp:** Lớp 4 & 5 (API Gateway, Kafka, Airflow, Data Lakehouse, AI Inference) đặt trên Public Cloud; Edge Cluster K3s + Kafka broker con + Local DB cache tại 34 chi nhánh; Lớp 3 (Keycloak IAM + PII DB) giữ tại máy chủ vật lý On-Premise ở HQ.
- **HA/DR:** Cloud multi-zone Active-Active (failover ≤ 60s), Kafka replication factor 3, backup immutable retention 30 ngày, PITR 7 ngày; Edge store-and-forward chứa 48 giờ giao dịch.
- **Tích hợp:** SSO tập trung tại HQ liên kết OIDC tới ứng dụng trên Cloud; log và monitoring tập trung trên Cloud (Prometheus/Grafana/Loki); quản lý issue/change qua ITSM.
- **Khả năng mở rộng:** theo dữ liệu và người dùng — auto-scaling trên Cloud; theo chi nhánh — triển khai Golden Image bằng IaC, chi nhánh thứ 35 lên trong vài giờ.
- **Ưu:** đáp ứng đồng thời offline, tuân thủ và co giãn. **Nhược:** phức tạp vận hành hơn, cần kỷ luật IaC và giám sát hai môi trường.

## 5.2. Bảng so sánh 3 kịch bản

| Tiêu chí bắt buộc để đạt KPI | On-Premise 100% | Cloud-Native 100% | Hybrid Cloud — Khuyến nghị |
| :--- | :---: | :---: | :---: |
| **1. Đảm bảo Uptime 99,99% khi rớt mạng chi nhánh** | ✓ | ✗ | ✓ |
| **2. Khả năng mở rộng tự động (Auto-scaling)** | ✗ | ✓ | ✓ |
| **3. Tuân thủ vị trí lưu trữ dữ liệu PII (Nghị định 13)** | ✓ | ✗ | ✓ |
| **4. Tối ưu chi phí đầu tư ban đầu (CAPEX) thấp** | ✗ | ✓ | ✓ |
| **5. Thời gian triển khai dịch vụ nhanh (Agility)** | ✗ | ✓ | ✓ |
| **6. Khả năng khôi phục thảm họa (Active-Active)** | ✗ | ✓ | ✓ |
| **Tổng số tiêu chí đáp ứng** | **2 / 6** | **4 / 6** | **6 / 6** |

## 5.3. Cơ sở biện luận chọn HYBRID CLOUD — gắn với đặc điểm của Ways Station

Sáu tiêu chí trên **không phải là tiêu chí chung chung**, mà được rút ra trực tiếp từ bốn đặc điểm riêng có của Ways Station đã khảo sát tại mục 4.1:

| Đặc điểm doanh nghiệp | Hệ quả kỹ thuật | Tiêu chí quyết định |
|:---|:---|:---|
| **Doanh thu tính theo giờ sử dụng** (net, bida, cầu lông, gym 24/7) — khách vào ra liên tục, tính tiền tại quầy | Mất mạng vài phút là **không tính được tiền và không trả được xe/bàn**, thiệt hại tức thì và không thể bù | **Tiêu chí 1** — loại Cloud-Native 100% |
| **34 hộ kinh doanh cá thể riêng biệt**, không có pháp nhân trung tâm, mặt bằng thuê không có phòng máy chủ, **không có IT thường trực tại chi nhánh** | Không thể đặt và vận hành cụm máy chủ đầy đủ tại 34 điểm; chỉ chấp nhận thiết bị nhỏ, cấu hình từ xa, tự phục hồi | **Tiêu chí 2, 5** — loại On-Premise 100% |
| **Thu thập PII nhạy cảm cao tại quầy**: ảnh CCCD, cà vẹt xe, Face ID hội viên | Dữ liệu định danh bắt buộc phải nằm dưới quyền kiểm soát trực tiếp của doanh nghiệp, tách khỏi dữ liệu vận hành | **Tiêu chí 3** — loại Cloud-Native 100% |
| **Tăng trưởng nhanh** (22 → 34 chi nhánh trong ~2 năm), tải biến động mạnh theo khung giờ và mùa vụ | Cần co giãn tài nguyên theo tải và nhân bản cấu hình chi nhánh mới trong vài giờ | **Tiêu chí 2, 4, 6** — loại On-Premise 100% |

Kết luận: **chỉ Hybrid Cloud thỏa mãn đồng thời cả bốn đặc điểm**. Cơ sở kỹ thuật liên kết với KPI:

- **Hợp nhất Lớp 4 & Tăng cường Uptime (đạt KPI 1.1 & 1.2):** API Gateway và Kafka đặt trên Public Cloud để tiếp nhận hàng ngàn request cùng lúc. Tại 34 chi nhánh cài đặt Edge Cluster (K3s + Kafka con) hoạt động như bộ đệm. Khi chi nhánh mất kết nối, phần mềm vẫn gọi API cục bộ để tính giờ ưu tiên ngoại tuyến; khi có mạng, dữ liệu tự đồng bộ bù về Cloud, đảm bảo MTTR ≤ 30 phút mà khách hàng không bị gián đoạn.
- **Hợp nhất Lớp 5 & Nâng cao chất lượng dữ liệu (đạt KPI 2.1 & 2.2):** Data Lakehouse trên Cloud cung cấp năng lực điện toán co giãn. Luồng Data Streaming (CDC - Change Data Capture) bắt sự kiện thay đổi dữ liệu tại chi nhánh đẩy thẳng về Cloud thời gian thực, đáp ứng Data Freshness ≤ 5s và Completeness ≥ 99,5%, làm đầu vào chất lượng cho mô hình học máy.
- **Bảo mật PII & Tuân thủ NĐ13 (đạt KPI 3.1 & 3.2):** Kiến trúc tuân thủ mô hình Zero Trust. Thông tin định danh nhạy cảm cực cao (Face ID, CCCD) và hệ thống IAM được giữ tại máy chủ vật lý On-Premise do doanh nghiệp tự quản lý, mã hóa AES-256 100%. Dữ liệu vận hành (hóa đơn, điểm danh) được ẩn danh trước khi đẩy lên Cloud.

## 5.4. Sơ đồ kiến trúc TO-BE

```
╔══════════════════════ PUBLIC CLOUD (Lớp 4 & 5) ══════════════════════╗
║  ┌────────────────┐  ┌──────────────┐  ┌─────────────────────────┐   ║
║  │  API Gateway   │  │    Kafka     │  │  Data Lakehouse         │   ║
║  │  (JWT, rate    │◄─┤  Cluster     │◄─┤  + PostgreSQL HA        │   ║
║  │   limiting)    │  │  (RF=3)      │  │  + Object Storage (S3)  │   ║
║  └────────────────┘  └──────────────┘  └───────────┬─────────────┘   ║
║  ┌────────────────┐  ┌──────────────┐              ▼                 ║
║  │ K8s multi-zone │  │ Airflow ETL  │  ┌─────────────────────────┐   ║
║  │ Active-Active  │  │ (DAGs)       │  │ AI Inference Service    │   ║
║  │ failover ≤60s  │  └──────────────┘  │ (FastAPI) + MLflow      │   ║
║  └────────────────┘  ┌──────────────────────────────────────────┐    ║
║                      │ Prometheus + Grafana + Loki (Lớp 2)      │    ║
║                      └──────────────────────────────────────────┘    ║
╚════════════▲═══════════════════════════════════▲═════════════════════╝
             │ VPN Site-to-Site (TLS 1.2+)       │ CDC Streaming (TLS)
             │                                   │ + Store-and-Forward
┌────────────┴──────────────────┐   ┌────────────┴──────────────────────┐
│  HQ — ON-PREMISE (Lớp 3)      │   │  34 CHI NHÁNH — EDGE             │
│  ┌─────────────────────────┐  │   │  ┌────────────────────────────┐  │
│  │ Keycloak IAM/SSO + MFA  │  │   │  │ Edge Cluster (K3s)         │  │
│  ├─────────────────────────┤  │   │  │ + Kafka broker con         │  │
│  │ PII Database            │  │   │  │ + Local DB cache           │  │
│  │ (CCCD, Face ID, SĐT)    │  │   │  │ + UPS 650VA                │  │
│  │ AES-256 at-rest 100%    │  │   │  ├────────────────────────────┤  │
│  ├─────────────────────────┤  │   │  │ 8 hệ thống PM hiện hữu     │  │
│  │ NGFW + Switch VLAN      │  │   │  │ (POS, MODUN Gym, Kho...)   │  │
│  │ Active-Passive HA       │  │   │  │ → gọi API cục bộ khi offline│ │
│  └─────────────────────────┘  │   │  └────────────────────────────┘  │
└───────────────────────────────┘   └───────────────────────────────────┘
        Dữ liệu PII KHÔNG rời          Dữ liệu vận hành được ẩn danh
        khỏi On-Premise                 trước khi đẩy lên Cloud
```

---

# 6. Yêu cầu kỹ thuật (HA - High Availability / DR / Security / Ops / Performance)

Yêu cầu kỹ thuật được chia thành 4 nhóm, đủ chi tiết để chào thầu/mua sắm và làm cơ sở nghiệm thu. Mỗi yêu cầu được liên kết ngược (traceability) với KPI đã cam kết tại **Mục 3**.

## 6.1. Nhóm 1 — Hiệu năng & Dung lượng (Performance & Capacity)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-P01 | **[Lớp 4]** API Gateway xử lý đồng thời (concurrent connections) tại Cloud | ≥ 2.000 kết nối đồng thời (34 chi nhánh × ~60 POS/thiết bị + đệm 20%) | KPI 1.1 | Load test đạt 2.000 concurrent connections, error rate < 0,1% |
| TR-P02 | **[Lớp 4]** Thời gian phản hồi API (P95) cho giao dịch POS | ≤ 200 ms (round-trip Edge → Cloud → Edge) | KPI 1.1, 1.2 | Benchmark P95 ≤ 200 ms trên 10.000 requests liên tục |
| TR-P03 | **[Lớp 5]** Throughput Data Pipeline (CDC Streaming) | ≥ 5.000 events/giây (tổng 34 chi nhánh, giờ cao điểm) | KPI 2.1, 2.2 | Stress test pipeline đạt throughput mục tiêu, không mất sự kiện |
| TR-P04 | **[Lớp 5]** Dung lượng Data Lakehouse (Cloud) | Tối thiểu 2 TB ban đầu, tự mở rộng lên 10 TB trong 3 năm | KPI 2.1 | Storage auto-scaling hoạt động khi đạt 80% capacity |
| TR-P05 | **[Lớp 4]** Sizing Edge Cluster mỗi chi nhánh | ≥ 4 vCPU, 8 GB RAM, 256 GB SSD — đủ chạy K3s + Kafka broker + Local DB cache | KPI 1.1 — Offline mode | Chi nhánh vận hành bình thường khi mất mạng ≥ 4 giờ |
| TR-P06 | **[Lớp 4 & 5]** Sizing Cloud Kubernetes Cluster | 6 nodes × (4 vCPU, 16 GB RAM) | KPI 1.1, 2.2 | Cluster hoạt động ổn định dưới tải 80% capacity |
| **TR-P07** | **[Lớp 4 & 5]** **Thời gian phản hồi API dự báo end-to-end (P95)** | **≤ 500 ms / 1 request** (bao gồm: gateway + truy vấn + suy luận mô hình). *Suy luận thuần của mô hình ≤ 200 ms — thuộc KPI A.4 của đề tài thực hành* | KPI 1.1; tiêu chí mục 3.3 | Benchmark end-to-end trên 1.000 requests liên tiếp, P95 ≤ 500 ms |

## 6.2. Nhóm 2 — Độ sẵn sàng cao & Khôi phục thảm họa (HA / DR)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-H01 | Kubernetes Cloud: Multi-zone Active-Active | Tối thiểu 2 availability zones, tự động failover ≤ 60 giây | KPI 1.1 | Test failover: tắt 1 zone, hệ thống tự phục hồi ≤ 60s |
| TR-H02 | Kafka Cluster: Replication factor | ≥ 3 replicas cho mọi topic nghiệp vụ | KPI 2.1, 3.2 | Tắt 1 broker, không mất message, producer/consumer tiếp tục hoạt động |
| TR-H03 | Edge Cluster: Store-and-Forward khi offline | Queue cục bộ chứa tối thiểu 48 giờ giao dịch (~50.000 events/chi nhánh) | KPI 1.1 | Ngắt mạng 4 giờ, kiểm tra 100% events được đồng bộ bù khi có mạng |
| TR-H04 | Backup Data Lakehouse (Immutable backup) | Backup tự động hàng ngày, retention 30 ngày, RPO ≤ 15 phút | KPI 3.2 | Test restore: dữ liệu khôi phục đầy đủ, thời gian restore ≤ 2 giờ |
| TR-H05 | Backup PostgreSQL (Managed) | PITR (Point-In-Time Recovery), retention 7 ngày, RPO ≤ 15 phút | KPI 3.2 | Restore PITR đến thời điểm bất kỳ trong 7 ngày, kiểm tra toàn vẹn |
| TR-H06 | DR Drill (Diễn tập khôi phục thảm họa) | ≥ 2 lần/năm, RTO (Recovery Time Objective) ≤ 4 giờ | KPI 1.2, 3.2 | Biên bản diễn tập DR: hệ thống phục hồi hoàn toàn trong ≤ 4 giờ |

## 6.3. Nhóm 3 — Bảo mật & Danh tính (Security + Identity)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-S01 | IAM / SSO toàn hệ thống (Keycloak hoặc tương đương) | 100% ứng dụng nội bộ xác thực qua SSO, hỗ trợ OIDC/SAML | KPI 3.1 | Đăng nhập 1 lần truy cập toàn bộ ứng dụng; token hết hạn đúng policy |
| TR-S02 | MFA (Multi-Factor Authentication) cho tài khoản đặc quyền | 100% tài khoản admin bắt buộc MFA (TOTP/WebAuthn) | KPI 3.1 | Đăng nhập admin không có MFA bị từ chối |
| TR-S03 | Mã hoá PII at-rest (On-Premise) | AES-256 cho toàn bộ trường PII (CCCD, Face ID, SĐT) | KPI 3.1 | Audit: 100% trường PII trong DB được mã hoá, không có plaintext |
| TR-S04 | Mã hoá in-transit | TLS 1.2+ cho mọi kết nối (Edge ↔ Cloud, API Gateway, CDC) | KPI 3.1 | Scan SSL/TLS: không tồn tại kết nối không mã hoá |
| TR-S05 | Ẩn danh hoá dữ liệu trước khi đẩy lên Cloud | Loại bỏ/hash trường PII trước khi ghi vào Data Lakehouse | KPI 3.1 | Kiểm tra mẫu dữ liệu trên Cloud: 0 bản ghi chứa PII dạng plaintext |
| TR-S06 | Log tập trung (Centralized Logging) | Lưu trữ ≥ 90 ngày, hỗ trợ tìm kiếm và cảnh báo bất thường | KPI 3.1 | Query log truy cập PII, log thay đổi cấu hình — kết quả trả về đúng |
| TR-S07 | Quét lỗ hổng bảo mật (Vulnerability Scan) | Quét tự động hàng tuần, 0 lỗ hổng Critical/High tồn tại quá 72 giờ | KPI 3.1 | Báo cáo scan: 0 Critical/High chưa vá |
| TR-S08 | Phân quyền RBAC theo nguyên tắc Least Privilege | Tối thiểu 4 vai trò: SuperAdmin, Admin chi nhánh, Nhân viên, Auditor | KPI 3.1 | Ma trận phân quyền được audit, tài khoản test không truy cập vượt quyền |

> Tất cả yêu cầu TR-S01→TR-S08 thuộc **02 thành phần Lớp 3 đã khai báo trong phạm vi tại mục 4.2** (IAM/SSO/MFA và Mã hóa PII).

## 6.4. Nhóm 4 — Vận hành (Operations)

| ID | Yêu cầu kỹ thuật | Ngưỡng đo lường | KPI liên kết | Tiêu chí nghiệm thu |
|:---|:---|:---|:---|:---|
| TR-O01 | Monitoring & Observability (Prometheus + Grafana) | Dashboard: CPU/RAM/Disk/Network toàn cluster + API latency + Pipeline status | KPI 1.1, 1.2 | Demo dashboard: metrics real-time, dữ liệu lịch sử 30 ngày |
| TR-O02 | Alerting & Escalation | Cảnh báo qua Slack/Email/SMS trong ≤ 5 phút khi metric vượt ngưỡng | KPI 1.2 | Trigger cảnh báo CPU > 85%, thông báo đến đúng người trong ≤ 5 phút |
| TR-O03 | CMDB (Configuration Management Database) | Danh mục tài sản: 34 Edge devices + Cloud resources + License, cập nhật tự động | Quản trị tài sản | CMDB liệt kê 100% tài sản, thông tin chính xác so với thực tế |
| TR-O04 | Patching & Update tự động (IaC - Infrastructure as Code) | Terraform/Ansible quản lý toàn bộ cấu hình; rollback < 15 phút | KPI 1.2 | Rollback cấu hình: hệ thống trở về trạng thái trước trong ≤ 15 phút |
| TR-O05 | Runbook / SOP vận hành | Tối thiểu 10 quy trình chuẩn: xử lý sự cố P1–P4, backup/restore, DR, patching, onboarding chi nhánh mới | KPI 1.2 | Runbook đầy đủ, thử nghiệm 3 kịch bản sự cố — thành công |
| TR-O06 | CI/CD Pipeline | Tự động: build → test → deploy Staging → approve → Production | KPI 1.1 | Commit code → deploy thành công lên Staging trong ≤ 15 phút |
| TR-O07 | Capacity Planning | Báo cáo dự báo tài nguyên hàng quý, cảnh báo khi sử dụng vượt 70% | Tối ưu chi phí | Báo cáo capacity quý đầu tiên sau Go-live có dữ liệu trending |

---

# 7. Danh mục hạng mục đầu tư (thiết bị / bản quyền / dịch vụ)

## 7.1. Thiết bị / Phần cứng

| # | Hạng mục | Mô tả / Thông số | Số lượng | Ghi chú |
|:---:|:---|:---|:---:|:---|
| 1 | Edge Mini Server (chi nhánh) | Intel NUC hoặc tương đương: 4 vCPU, 8 GB RAM, 256 GB NVMe SSD. Chạy K3s, Kafka broker, Local DB cache | 34 bộ | 1 bộ/chi nhánh + 2 bộ dự phòng thay thế nóng → Tổng mua 36 bộ |
| 2 | UPS (Uninterruptible Power Supply) cho Edge | UPS 650VA, giữ tải ≥ 15 phút | 34 bộ | Tránh mất điện đột ngột làm hỏng queue dữ liệu |
| 3 | On-Premise Server (HQ — IAM + PII DB) | Rack Server 2U: 2× Xeon 8 cores, 64 GB ECC RAM, 2× 1TB SSD RAID-1, Redundant PSU | 2 bộ | Active-Passive HA, đặt tại trụ sở chính |
| 4 | Switch Managed (HQ) | Layer 2 Managed, 24 ports GbE, VLAN support | 1 bộ | Phân tách VLAN: IAM Server / Management / Guest |
| 5 | Firewall Appliance (HQ) | NGFW: IPS/IDS, VPN site-to-site, 1 Gbps throughput | 1 bộ | Bảo vệ On-Premise IAM/PII, kết nối VPN tới Cloud |

## 7.2. Phần mềm bản quyền

| # | Hạng mục | Loại giấy phép | Số lượng | Ghi chú |
|:---:|:---|:---|:---:|:---|
| 1 | **[Lớp 4]** Kubernetes (K3s — Edge, K8s — Cloud) | Open-source (Apache 2.0) | — | Miễn phí |
| 2 | **[Lớp 4 & 5]** Apache Kafka | Open-source (Apache 2.0) | — | Miễn phí, hoặc Managed Kafka (tính vào OPEX) |
| 3 | **[Lớp 3 — trong phạm vi]** Keycloak (IAM/SSO) | Open-source (Apache 2.0) | — | Miễn phí |
| 4 | **[Lớp 5]** PostgreSQL (Data Warehouse + PII DB) | Open-source (PostgreSQL License) | — | On-Prem tự cài; Cloud dùng Managed (OPEX) |
| 5 | **[Lớp 5]** Apache Airflow | Open-source (Apache 2.0) | — | Miễn phí |
| 6 | **[Lớp 5]** MLflow (Model Registry) | Open-source (Apache 2.0) | — | Miễn phí |
| 7 | **[Lớp 2]** Prometheus + Grafana + Loki | Open-source (Apache 2.0 / AGPL) | — | Miễn phí |
| 8 | **[Lớp 2]** Terraform + Ansible (IaC) | Open-source (MPL 2.0 / GPL) | — | Miễn phí |
| 9 | OS cho On-Prem Server | Ubuntu Server 22.04 LTS | 2 | Miễn phí (Community) |
| 10 | OS cho Edge Server | Ubuntu Server 22.04 LTS (minimal) | 36 | Miễn phí |
| 11 | Firewall License (NGFW) | Subscription hãng (Fortinet/Palo Alto) | 1/năm | Tính vào OPEX |

> **Chiến lược bản quyền:** ưu tiên tối đa phần mềm mã nguồn mở ổn định, cộng đồng lớn để giảm chi phí license — phù hợp ngân sách doanh nghiệp vừa (SMB). Tuân thủ đầy đủ điều khoản giấy phép OSS.

## 7.3. Dịch vụ triển khai

| # | Hạng mục dịch vụ | Phạm vi | Ghi chú |
|:---:|:---|:---|:---|
| 1 | Thiết kế kiến trúc chi tiết (HLD + LLD) | Cloud K8s, Edge K3s, Data Pipeline, IAM, Network topology | Bao gồm review & phê duyệt |
| 2 | Triển khai & cấu hình hạ tầng Cloud | K8s cluster, Kafka, Airflow, PostgreSQL managed, Object Storage, VPN | IaC (Terraform) |
| 3 | Triển khai & cấu hình 34 Edge Cluster | K3s, Kafka broker, Local DB cache, Store-and-Forward agent | Golden Image, deploy hàng loạt |
| 4 | Triển khai On-Premise Server (HQ) | Keycloak, PII Database, Firewall, VPN, hardening | Theo CIS Benchmark |
| 5 | Migrate dữ liệu | 8 hệ thống POS rời rạc → Data Lakehouse (lịch sử ≥ 12 tháng) | ETL scripts + kiểm tra toàn vẹn |
| 6 | Tích hợp hệ thống (API Integration) | Kết nối POS/Gym/Bida/Kho vào API Gateway; CDC streaming setup | 8 hệ thống × 34 chi nhánh |
| 7 | Hardening & Security audit | CIS Benchmark, quét lỗ hổng, cấu hình WAF/IDS | Trước Go-live |
| 8 | Đào tạo & Chuyển giao | IT vận hành (3 buổi), Admin chi nhánh (2 buổi), bàn giao Runbook | Bao gồm tài liệu |

## 7.4. Chi phí hạ tầng định kỳ (chi tiết hoá tại Mục 8)

| # | Hạng mục | Chu kỳ |
|:---:|:---|:---|
| 1 | Cloud Kubernetes Cluster (6 nodes) | Hàng tháng |
| 2 | Managed PostgreSQL (HA) | Hàng tháng |
| 3 | Managed Kafka | Hàng tháng |
| 4 | Object Storage (S3) | Hàng tháng |
| 5 | GPU Instance (huấn luyện AI) | Hàng tháng |
| 6 | Đường truyền Internet chi nhánh (34 đường) | Hàng tháng |
| 7 | VPN Site-to-Site (HQ ↔ Cloud) | Hàng tháng |
| 8 | Firewall NGFW License renewal | Hàng năm |
| 9 | Support & bảo trì phần cứng On-Prem | Hàng năm |

---

# 8. Dự toán CAPEX / OPEX & TCO 3 năm

## 8.1. Chi phí đầu tư ban đầu (CAPEX)

### A. Phần cứng

| Hạng mục | Đơn giá (VNĐ) | SL | Thành tiền (VNĐ) | Nguồn tham khảo giá |
|:---|---:|:---:|---:|:---|
| Edge Mini Server (Intel NUC i5, 8GB, 256GB SSD) | 8.500.000 | 36 | 306.000.000 | Báo giá đại lý CNTT TP.HCM, khảo sát Q3 |
| UPS 650VA cho Edge | 1.200.000 | 34 | 40.800.000 | Giá niêm yết Santak/APC, khảo sát Q3 |
| On-Premise Server 2U (Xeon, 64GB, 2×1TB SSD RAID-1) | 85.000.000 | 2 | 170.000.000 | Báo giá Dell/HPE qua đối tác, khảo sát Q3 |
| Switch Managed 24-port GbE | 8.000.000 | 1 | 8.000.000 | Giá niêm yết TP-Link/Cisco SMB |
| Firewall NGFW (FortiGate 60F hoặc tương đương) | 25.000.000 | 1 | 25.000.000 | Báo giá đối tác Fortinet [8] |
| Phụ kiện (cáp, rack mini HQ, patch panel) | 15.000.000 | 1 lot | 15.000.000 | Ước tính trọn gói |
| **Tổng phần cứng** | | | **564.800.000** | |

> Đơn giá là **giả định có căn cứ khảo sát thị trường**; giá chính thức được chốt qua RFP tại Mục 12. Biên độ dao động dự kiến ±10%, đã được hấp thụ bởi quỹ dự phòng tại mục 8.3.

### B. Dịch vụ triển khai & Nhân công

Đơn giá chuẩn áp dụng: **7.500.000 VNĐ/tuần-người** cho kỹ sư triển khai.

| Hạng mục | Chi tiết | Thành tiền (VNĐ) |
|:---|:---|---:|
| Thiết kế kiến trúc (HLD + LLD) | 2 kỹ sư × 3 tuần | 45.000.000 |
| Triển khai Cloud (K8s, Kafka, Airflow, DB, Storage, Monitoring) | 2 kỹ sư × 4 tuần | 60.000.000 |
| Triển khai 34 Edge Cluster (Golden Image + deploy) | 2 kỹ sư × 4 tuần | 60.000.000 |
| Triển khai On-Prem Server HQ (Keycloak, PII DB, Firewall, VPN) | 1 kỹ sư × 2 tuần | 15.000.000 |
| Migrate dữ liệu lịch sử (8 hệ thống × 34 CN, ≥ 12 tháng) | 2 kỹ sư × 3 tuần | 45.000.000 |
| Tích hợp API (8 hệ thống → API Gateway + CDC) | 3 kỹ sư × 6 tuần | 135.000.000 |
| Tích hợp & triển khai AI Inference Service lên K8s *(không bao gồm chi phí nghiên cứu — phát triển mô hình, thuộc đề tài thực hành)* | 2 ML Engineer × 6 tuần | 90.000.000 |
| Hardening & Security Audit | 1 kỹ sư × 2 tuần (15tr) + dịch vụ Pentest thuê ngoài (25tr) | 40.000.000 |
| Kiểm thử tích hợp & tải (Load Test, Failover Test, DR Drill) | 1 QA × 3 tuần (22,5tr) + license công cụ Load Test (4,5tr) | 27.000.000 |
| Đào tạo & Chuyển giao (IT team + Admin chi nhánh, 5 buổi) | Trọn gói | 15.000.000 |
| Project Management | 1 PM × 4 tháng, tham gia ~60% thời lượng | 100.000.000 |
| **Tổng dịch vụ triển khai** | | **632.000.000** |

### C. Hạ tầng Cloud (giai đoạn triển khai — 4 tháng)

| Hạng mục | Đơn giá/tháng (VNĐ) | Số tháng | Thành tiền (VNĐ) |
|:---|---:|:---:|---:|
| K8s Cluster Development/Staging (3 nodes × 4vCPU, 16GB) | 12.000.000 | 4 | 48.000.000 |
| Managed PostgreSQL Dev (2vCPU, 8GB) | 2.500.000 | 4 | 10.000.000 |
| Managed Kafka Dev (3 brokers) | 5.000.000 | 4 | 20.000.000 |
| Object Storage (500 GB) | 500.000 | 4 | 2.000.000 |
| GPU Instance (huấn luyện AI, 2 tháng) | 12.000.000 | 2 | 24.000.000 |
| VPN + Bandwidth | 2.000.000 | 4 | 8.000.000 |
| **Tổng Cloud (triển khai)** | | | **112.000.000** |

### Tổng CAPEX

| Nhóm | Thành tiền (VNĐ) |
|:---|---:|
| Phần cứng | 564.800.000 |
| Dịch vụ triển khai & Nhân công | 632.000.000 |
| Hạ tầng Cloud (4 tháng triển khai) | 112.000.000 |
| **TỔNG CAPEX** | **1.308.800.000** |

## 8.2. Chi phí vận hành định kỳ (OPEX) — 12 tháng sau Go-live

| Hạng mục | Chi tiết | Đơn giá/tháng (VNĐ) | 12 tháng (VNĐ) |
|:---|:---|---:|---:|
| **Hạ tầng Cloud Production** | | | |
| K8s Cluster Production (6 nodes × 4vCPU, 16GB) | API Gateway, Kafka, Airflow, AI Inference | 24.000.000 | 288.000.000 |
| Managed PostgreSQL HA Production | Data Lakehouse + Forecast DB | 6.000.000 | 72.000.000 |
| Managed Kafka Production (3 brokers, HA) | CDC Streaming 34 chi nhánh | 8.000.000 | 96.000.000 |
| Object Storage (S3, tăng ~200 GB/năm) | Raw data + Model artifacts | 800.000 | 9.600.000 |
| GPU Instance (tái huấn luyện AI, 1 lần/tháng × 8h) | Spot Instance | 800.000 | 9.600.000 |
| VPN Site-to-Site + Bandwidth Cloud | Kết nối HQ ↔ Cloud | 2.000.000 | 24.000.000 |
| **Đường truyền chi nhánh** | | | |
| Internet 34 chi nhánh (nâng băng thông cho CDC) | Bổ sung ~500.000/CN/tháng | 17.000.000 | 204.000.000 |
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

## 8.3. Dự phòng rủi ro (Contingency)

| Hạng mục | Tỷ lệ | Thành tiền (VNĐ) |
|:---|:---:|---:|
| Dự phòng rủi ro kỹ thuật (CAPEX) | 10% × 1.308.800.000 | 130.880.000 |
| Dự phòng biến động giá Cloud/nhân sự (OPEX năm 1) | 10% × 1.123.400.000 | 112.340.000 |
| **Tổng dự phòng** | | **243.220.000** |

## 8.4. Tổng chi phí sở hữu (TCO) — Chu kỳ 3 năm

| Năm | CAPEX (VNĐ) | OPEX (VNĐ) | Contingency (VNĐ) | Tổng / năm (VNĐ) |
|:---:|---:|---:|---:|---:|
| **Năm 1** | 1.308.800.000 | 1.123.400.000 | 243.220.000 | 2.675.420.000 |
| **Năm 2** | 0 | 1.123.400.000 | 112.340.000 | 1.235.740.000 |
| **Năm 3** | 0 | 1.180.000.000 *(+5%)* | 118.000.000 | 1.298.000.000 |
| **TCO 3 năm** | **1.308.800.000** | **3.426.800.000** | **473.560.000** | **5.209.160.000** |

$$\text{TCO}_{3\ \text{năm}} = 1.308.800.000 + 3.426.800.000 + 473.560.000 = \textbf{5.209.160.000 VNĐ}$$

## 8.5. Phân tích lợi ích quy đổi (Cost-Benefit)

**Cơ sở quy mô doanh thu:** ước tính doanh thu toàn chuỗi **~120 tỷ VNĐ/năm** (34 chi nhánh × trung bình ~294 triệu VNĐ/chi nhánh/tháng cho tổ hợp Gym + Net + Bida + Cầu lông + Hub + F&B) **[SL]**. TCO 3 năm (5,209 tỷ) tương đương **~1,45% doanh thu 3 năm** — nằm trong biên độ đầu tư CNTT thông thường của ngành bán lẻ dịch vụ.

| Lợi ích | Quy đổi (VNĐ/năm) | Cơ sở tính |
|:---|---:|:---|
| Giảm 2.500 giờ công báo cáo thủ công | 125.000.000 | 50.000 VNĐ/giờ × 2.500 giờ |
| Thu hồi thất thoát do sai lệch đối soát | 700.000.000 | Thất thoát thực ước tính ~1% doanh thu = 1,2 tỷ; mục tiêu thu hồi ~58% nhờ đối soát tự động (sai lệch 3,8% → <0,5%) |
| Giảm thiệt hại downtime | 400.000.000 | Doanh thu bình quân giờ cao điểm ~41 triệu/giờ toàn chuỗi; giảm từ 4–8h/sự cố xuống ≤ 30 phút MTTR |
| Tối ưu giờ công nhờ dự báo lưu lượng | 400.000.000 | Quỹ lương vận hành ~19,6 tỷ/năm; giảm ~2% giờ công dư giờ thấp điểm. *Phụ thuộc kết quả đề tài thực hành* |
| Giảm hao hụt nguyên vật liệu F&B | 180.000.000 | Doanh thu F&B ~15% tổng; hao hụt ~3%; giảm 1/3 nhờ dự báo nhu cầu |
| Tăng doanh thu bán chéo nhờ SSO | 150.000.000 | Định danh duy nhất cho 5 mảng dịch vụ; ước tính thận trọng |
| Tránh rủi ro phạt NĐ13 (đến 5% doanh thu ≈ 6 tỷ) | Không lượng hoá | Rủi ro đuôi, tác động rất lớn nếu bị thanh tra |
| **Tổng lợi ích quy đổi / năm** | **~1.955.000.000** | |

**Phân tích hoàn vốn (trên dòng tiền ròng):**

| Chỉ tiêu | Giá trị (VNĐ) |
|:---|---:|
| Lợi ích quy đổi/năm | 1.955.000.000 |
| Trừ OPEX/năm | (1.123.400.000) |
| **Dòng tiền ròng hàng năm** | **831.600.000** |
| Vốn đầu tư ban đầu (CAPEX + dự phòng CAPEX) | 1.439.680.000 |

$$\text{Payback} = \frac{1.439.680.000}{831.600.000} \approx \textbf{1,73 năm} \approx \textbf{21 tháng}$$

Trong chu kỳ 3 năm, dòng tiền ròng luỹ kế đạt **~2,49 tỷ VNĐ**, vượt vốn đầu tư ban đầu — dự án khả thi về tài chính ngay cả khi chưa tính giá trị tránh rủi ro pháp lý.

> **Lưu ý về tính thận trọng:** hai dòng lợi ích "tối ưu giờ công" và "giảm hao hụt F&B" (tổng 580 triệu) phụ thuộc vào chất lượng mô hình dự báo AI thuộc đề tài thực hành. Trong kịch bản xấu nhất (loại bỏ hoàn toàn hai dòng này), dòng tiền ròng còn 251,6 triệu/năm và payback kéo dài ~5,7 năm — khi đó dự án vẫn được khuyến nghị phê duyệt dựa trên nghĩa vụ tuân thủ Nghị định 13/2023/NĐ-CP.

## 8.6. So sánh TCO 3 năm giữa 3 kịch bản

| Hạng mục | On-Premise 100% | Cloud-Native 100% | Hybrid Cloud (Chọn) |
|:---|---:|---:|---:|
| CAPEX (phần cứng + triển khai) | ~2.800.000.000 | ~650.000.000 | ~1.308.800.000 |
| OPEX / năm | ~600.000.000 | ~1.800.000.000 | ~1.123.400.000 |
| TCO 3 năm | ~4.600.000.000 | ~6.050.000.000 | ~5.209.160.000 |
| Đáp ứng KPI Offline (99,99%) | ✓ | ✗ | ✓ |
| Đáp ứng KPI Tuân thủ NĐ13 | ✓ | ✗ | ✓ |
| Đáp ứng KPI Auto-scaling | ✗ | ✓ | ✓ |

> **Biện luận:** Hybrid Cloud có TCO trung bình nhưng là phương án duy nhất đáp ứng **100% tiêu chí kỹ thuật bắt buộc (6/6)**. On-Premise rẻ OPEX nhưng CAPEX quá cao và không co giãn — bất khả thi với mô hình 34 điểm không có IT tại chỗ. Cloud-Native rẻ CAPEX nhưng OPEX cao nhất và **không đáp ứng** yêu cầu offline lẫn tuân thủ NĐ13 — hai ràng buộc cứng của Ways Station.

---

# 9. Kế hoạch triển khai (Roadmap / WBS)

## 9.1. Roadmap 5 pha

Tổng thời gian **16 tuần (~4 tháng)**. **Các pha được thiết kế gối đầu 1 tuần** (pha sau khởi động trong tuần cuối của pha trước để chuẩn bị môi trường): tổng thời lượng danh nghĩa 3+4+4+5+4 = 20 tuần, trừ 4 tuần gối đầu → **16 tuần lịch**.

```
Tuần:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
Pha 1 [=====]                                            M1 ↑T3
Pha 2      [========]                                     M2 ↑T6
Pha 3            [========]                               M3 ↑T9
Pha 4                  [===========]                      M4 ↑T13
Pha 5                              [========]             M5 ↑T16
```

### Pha 1: Foundation — Mạng, Bảo mật nền, Monitoring
- **Thời gian:** T1–T3 (3 tuần) | **Phụ thuộc:** —
- **Deliverables:** VPN Site-to-Site HQ ↔ Cloud; On-Prem Server HQ (Keycloak SSO/IAM + PII DB) cài đặt & hardening; Firewall NGFW cấu hình rules; Prometheus + Grafana + Loki trên Cloud; Centralized Logging (≥ 90 ngày); CMDB khởi tạo.
- **Tiêu chí hoàn thành:** VPN ping < 50ms; SSO login thành công cho 4 vai trò; Dashboard Monitoring hiển thị metrics; Firewall rules audit pass.
- **Kế hoạch dự phòng:** nếu VPN không đạt độ trễ, chuyển sang kênh Direct Connect/Leased line (dự phòng 30tr); nếu hardening trễ, Pha 2 vẫn khởi động trên môi trường Staging cách ly.

### Pha 2: Core — Compute, Storage, HA, Backup/DR
- **Thời gian:** T3–T6 (4 tuần) | **Phụ thuộc:** Pha 1
- **Deliverables:** K8s Cluster Production (6 nodes, multi-zone); Managed PostgreSQL HA + Managed Kafka HA; Object Storage (S3); backup immutable hàng ngày (retention 30 ngày); PITR PostgreSQL (retention 7 ngày); Edge Golden Image (K3s + Kafka + LocalDB).
- **Tiêu chí hoàn thành:** K8s 2 zone failover ≤ 60s; Kafka replication factor = 3; backup test restore thành công; Golden Image boot thành công trên máy test.
- **Kế hoạch dự phòng:** nếu Managed Kafka vượt ngân sách, chuyển self-managed Kafka trên K8s (đã có sizing tại TR-P06); snapshot toàn cluster trước mỗi thay đổi lớn, rollback ≤ 15 phút.

### Pha 3: Security Uplift — Tích hợp IAM, Mã hoá, CDC
- **Thời gian:** T6–T9 (4 tuần) | **Phụ thuộc:** Pha 2
- **Deliverables:** **[Lớp 4]** tích hợp SSO vào 8 hệ thống POS/Gym/Bida/Kho; **[Lớp 3]** MFA cho admin; **[Lớp 3]** mã hoá AES-256 PII DB at-rest; **[Lớp 5]** CDC Streaming (Kafka Connect) từ 34 POS → Cloud; **[Lớp 3/5]** ẩn danh hoá PII trước khi ghi Data Lakehouse; **[Lớp 4]** API Gateway (rate limiting, JWT auth); **[Lớp 5]** Airflow DAGs (ETL).
- **Tiêu chí hoàn thành:** 100% app xác thực qua SSO; 100% trường PII mã hoá; CDC 5.000 events/s stress test pass; API Gateway load test 2.000 concurrent pass; Pipeline ETL chạy end-to-end trên staging.
- **Kế hoạch dự phòng:** đây là pha rủi ro cao nhất (8 vendor POS khác nhau). Nếu 1–2 hệ thống không mở được API, dùng **adapter pattern đọc trực tiếp CSDL ở chế độ read-only**; nếu vẫn tắc, hoãn hệ thống đó sang Pha 5 và ghi nhận CR.

### Pha 4: Migration & AI — Migrate dữ liệu, Triển khai AI, Pilot
- **Thời gian:** T9–T13 (5 tuần) | **Phụ thuộc:** Pha 3
- **Deliverables:** migrate dữ liệu lịch sử 12 tháng (8 hệ thống → Data Lakehouse); AI Inference Service (FastAPI) trên K8s; triển khai 34 Edge Cluster (Golden Image); **Pilot 5 chi nhánh** (2 tuần vận hành thử); Load Test toàn hệ thống; Pentest & Vulnerability Scan; UAT với Admin chi nhánh.
- **Tiêu chí hoàn thành:** dữ liệu migrate 100% toàn vẹn (row count match); MAPE < 15% trên tập test (tiêu chí mục 3.3); Pilot 5 CN: uptime ≥ 99,99%, offline test pass (4h mất mạng); Pentest 0 Critical/High; UAT sign-off.
- **Kế hoạch dự phòng:** nếu Pilot phát hiện lỗi nghiêm trọng, **giữ song song hệ thống cũ (dual-run) thêm 2 tuần** và lùi Pha 5; nếu mô hình AI chưa đạt MAPE, Go-live phần nền tảng trước, phát hành dự báo ở chế độ beta không ràng buộc nghiệm thu.

### Pha 5: Optimize & Rollout — Rollout toàn bộ, SOP, Chuyển giao
- **Thời gian:** T13–T16 (4 tuần) | **Phụ thuộc:** Pha 4
- **Deliverables:** rollout 29 chi nhánh còn lại (đợt 10-10-9 CN); Runbook/SOP (≥ 10 quy trình); DR Drill lần 1; đào tạo IT team (3 buổi) + Admin CN (2 buổi); bàn giao CMDB, tài liệu kiến trúc, tài khoản; báo cáo Capacity Planning quý 1; fine-tune alerting thresholds.
- **Tiêu chí hoàn thành:** 34 CN hoạt động ổn định; DR Drill RTO ≤ 4h; đào tạo hoàn tất, biên bản bàn giao ký; CMDB liệt kê 100% tài sản; SOP thử nghiệm 3 kịch bản pass.
- **Kế hoạch dự phòng:** rollout theo đợt cho phép **dừng và rollback từng đợt** nếu tỷ lệ sự cố vượt ngưỡng; 2 Edge Server dự phòng cho phép thay thế nóng trong ≤ 30 phút.

## 9.2. Mốc nghiệm thu (Milestones)

| Mốc | Thời điểm | Nội dung nghiệm thu |
|:---|:---|:---|
| **M1** | Cuối T3 | Foundation: VPN, IAM/SSO, Firewall, Monitoring hoạt động |
| **M2** | Cuối T6 | Core: K8s HA, Kafka HA, Backup/DR, Edge Golden Image sẵn sàng |
| **M3** | Cuối T9 | Security Uplift: SSO 8 hệ thống, CDC streaming, API Gateway, PII mã hoá 100% |
| **M4** | Cuối T13 | Migration & AI: migrate xong, Pilot 5 CN thành công, Pentest pass, UAT sign-off |
| **M5** | Cuối T16 | Rollout 34 CN, DR Drill pass, đào tạo & chuyển giao hoàn tất — **GO-LIVE** |

## 9.3. Phân bổ chi phí CAPEX theo pha (Kiểm chứng tính nhất quán)

| Pha | Phần cứng (VNĐ) | Dịch vụ & Nhân công (VNĐ) | Cloud Dev (VNĐ) | Tổng (VNĐ) |
|:---|---:|---:|---:|---:|
| Pha 1: Foundation (T1–T3) | 218.000.000 | 75.000.000 | 18.000.000 | 311.000.000 |
| Pha 2: Core (T3–T6) | 0 | 60.000.000 | 36.000.000 | 96.000.000 |
| Pha 3: Security Uplift (T6–T9) | 0 | 180.000.000 | 28.000.000 | 208.000.000 |
| Pha 4: Migration & AI (T9–T13) | 346.800.000 | 257.000.000 | 24.000.000 | 627.800.000 |
| Pha 5: Optimize & Rollout (T13–T16) | 0 | 60.000.000 | 6.000.000 | 66.000.000 |
| **Tổng** | **564.800.000** | **632.000.000** | **112.000.000** | **1.308.800.000** |

> Pha 1 phần cứng = On-Prem Server (170tr) + Switch (8tr) + Firewall (25tr) + Phụ kiện (15tr) = 218tr. Pha 4 phần cứng = Edge Server (306tr) + UPS (40,8tr) = 346,8tr. Chi phí PM (100tr) được phân bổ đều vào 5 pha. Tổng phân bổ theo pha **= Tổng CAPEX. ✓ Khớp.**

---

# 10. Rủi ro & kế hoạch kiểm soát

| Rủi ro | Khả năng | Tác động | Biện pháp giảm thiểu | Owner |
|:---|:---:|:---:|:---|:---|
| Chậm tích hợp API do 8 hệ thống POS đa vendor | Cao | Cao | Pilot tích hợp 2 hệ thống phổ biến nhất trước (Pha 3); adapter pattern cho vendor khác; fallback đọc CSDL read-only | Tech Lead (App) |
| Edge Server lỗi phần cứng khi rollout hàng loạt | Trung bình | Trung bình | Dự phòng 2 bộ thay thế nóng; Golden Image cho phép deploy lại ≤ 30 phút | Infra Lead |
| Mô hình AI không đạt MAPE < 15% trên dữ liệu thực | Trung bình | Cao | Thu thập đủ 12 tháng dữ liệu lịch sử; thử nghiệm 3 nhánh thuật toán (Prophet, LSTM, TSFM); rollback về Moving Average; Go-live nền tảng không phụ thuộc kết quả AI | ML Lead |
| Nhân viên chi nhánh kháng cự thay đổi quy trình | Trung bình | Trung bình | Đào tạo sớm từ Pha 4 (Pilot); chọn 5 CN có quản lý tích cực làm Pilot; thu thập phản hồi điều chỉnh UX | PM |
| Chi phí Cloud vượt dự toán | Thấp | Trung bình | Contingency 10%; chuyển Reserved Instance (giảm 30–40%); FinOps review hàng tháng | PM |
| Lộ lọt dữ liệu (Data Breach) hoặc tấn công mạng | Trung bình | Cao | Least Privilege; quét lỗ hổng định kỳ; mã hóa PII; giám sát hành vi tải dữ liệu bất thường | Security Lead |
| Doanh nghiệp thay đổi mô hình pháp lý 34 hộ kinh doanh | Thấp | Trung bình | Kiến trúc Hybrid không phụ thuộc pháp nhân; chỉ cần điều chỉnh cấu hình phân quyền RBAC | PM |

---

# 11. Tổ chức dự án & RACI

## 11.1. Ma trận phân nhiệm (RACI)

**R (Responsible):** thực hiện | **A (Accountable):** giải trình, phê duyệt | **C (Consulted):** tham vấn | **I (Informed):** được thông báo

| Hạng mục công việc | Sponsor / BGĐ | PM | Tech Leads (Infra/Data/Security) | Vendor / Đội triển khai | Key Users (Admin CN) |
|:---|:---:|:---:|:---:|:---:|:---:|
| Phê duyệt dự án & ngân sách | A | R | C | - | I |
| Thiết kế kiến trúc (HLD/LLD) | I | A | R | R | - |
| Mua sắm phần cứng & thiết bị | A | R | C | - | I |
| Triển khai Cloud & On-Premise | I | A | R | R | - |
| Migrate dữ liệu & Tích hợp API | I | A | R | R | C |
| Triển khai & kiểm thử AI Inference Service | I | A | R | R | C |
| Đào tạo và Chuyển giao | I | A | C | R | R |
| Nghiệm thu hệ thống (Go-Live) | A | R | R | - | C |

## 11.2. Cơ chế phối hợp & Quản lý thay đổi

- **Lịch họp định kỳ:** Ban chỉ đạo (Steering Committee) hàng tháng; Project Status hàng tuần; Daily Standup cho đội kỹ thuật; Milestone Review tại mỗi mốc M1–M5.
- **Quản lý Issue / Change Request (CR):** mọi thay đổi về phạm vi, ngân sách hoặc thời gian phải lập ticket CR trên hệ thống ITSM (Jira), Tech Lead đánh giá rủi ro và PM trình Sponsor phê duyệt trước khi thực thi. Nghiêm cấm scope creep.

---

# 12. Mua sắm / chọn nhà thầu

## 12.1. Hình thức mua sắm
Do yêu cầu tích hợp phức tạp và tính bảo mật cao, phương thức mua sắm là **Chào giá cạnh tranh (RFP - Request for Proposal)**, mời tối thiểu 3 nhà thầu CNTT có kinh nghiệm triển khai Cloud và Big Data.

## 12.2. Tiêu chí đánh giá nhà thầu
- **Kỹ thuật (trọng số 70%):** năng lực triển khai Hybrid Cloud (Kubernetes, Kafka); trình độ nhân sự (chứng chỉ AWS/Azure/GCP, Kubernetes CKA); giải pháp đáp ứng 100% yêu cầu kỹ thuật tại **Mục 6**.
- **Tài chính (trọng số 30%):** chi phí cạnh tranh, không vượt ngân sách CAPEX dự kiến.

## 12.3. Yêu cầu ràng buộc trong hợp đồng
- **Cam kết SLA (Service Level Agreement) & phạt vi phạm:** vendor cam kết SLA tích hợp và downtime tối đa trong thời gian Pilot; phạt 1% giá trị hợp đồng/tuần trễ tiến độ.
- **Cam kết bảo mật (NDA):** ký NDA về bảo vệ dữ liệu PII theo Nghị định 13/2023/NĐ-CP; không sao chép dữ liệu khách hàng ra khỏi môi trường Test/Prod của doanh nghiệp.
- **Bảo hành & hỗ trợ kỹ thuật:** hỗ trợ xử lý sự cố (L2/L3) tối thiểu 12 tháng sau Go-Live, Response Time ≤ 2 giờ.

---

# 13. Nghiệm thu – vận hành – chuyển giao

## 13.1. Nghiệm thu theo các lớp năng lực
- **Kỹ thuật (Performance & HA):** Load Test API Gateway ≥ 2.000 concurrent users; ngắt kết nối mạng chi nhánh ≥ 4 giờ, kiểm tra offline mode và đồng bộ lại 100% giao dịch (Store-and-Forward); DR Drill với RTO ≤ 4 giờ, khôi phục Database từ PITR với RPO ≤ 15 phút.
- **Bảo mật:** 100% kết nối mã hóa TLS 1.2+; PII (CCCD, Face ID) trên On-Premise mã hóa AES-256; dữ liệu trên Cloud đã ẩn danh; vượt qua Vulnerability Scan không còn lỗi Critical/High.
- **Vận hành:** Dashboard Grafana hiển thị dữ liệu thời gian thực; hệ thống cảnh báo gửi thông báo qua Slack/Email dưới 5 phút khi mô phỏng sự cố tải cao.
- **Dữ liệu:** đối soát doanh thu tháng đầu sau Go-live đạt sai lệch < 0,5%; Completeness ≥ 99,5%.

## 13.2. Đo lường hiệu quả sau triển khai (Benefit Realization)

Đo lại toàn bộ KPI tại mốc **+1 tháng, +3 tháng và +6 tháng** sau Go-live, theo đúng owner và căn cứ nghiệm thu đã quy định tại bảng 3.1:

| Mốc | Nội dung đo | Người chịu trách nhiệm số liệu |
|:---|:---|:---|
| +1 tháng | Uptime, Data Freshness, Encryption Coverage | SRE, Data Lead, Security Lead |
| +3 tháng | Toàn bộ 6 KPI; số giờ công báo cáo tiết kiệm được; tỷ lệ sai lệch đối soát | PM tổng hợp |
| +6 tháng | Toàn bộ 6 KPI; lợi ích quy đổi thực tế so với dự toán mục 8.5; DR Drill lần 2 | PM + Sponsor |

## 13.3. Kế hoạch Chuyển giao (Handover)
- **Tài liệu bàn giao:** thiết kế kiến trúc chi tiết (LLD), sơ đồ mạng, mã nguồn cấu hình (IaC/Terraform scripts).
- **Quy trình vận hành (SOP):** 10+ Runbook xử lý sự cố chuẩn, hướng dẫn cập nhật bản vá, quy trình onboarding chi nhánh mới.
- **Đào tạo:** 3 buổi chuyên sâu cho đội IT nội bộ (K8s, Kafka, Airflow); 2 buổi cho Quản lý chi nhánh và Admin.
- **Quản lý tài sản (CMDB):** cập nhật 34 Edge Server, 2 On-Prem Server, Cloud resources, phần mềm vào CMDB nội bộ.

---

# Phụ lục A — Danh mục minh chứng hiện trạng

| # | Khẳng định trong AS-IS (mục 2.1) | Tài liệu minh chứng | Nội dung trích dẫn |
|:---:|:---|:---|:---|
| A1 | Tồn tại nhiều phần mềm rời rạc, không SSO | `THU NGÂN NET + BIDA`, `PHỤC VỤ GYM`, `PHỤC VỤ BIDA`, `PHỤC VỤ CẦU LÔNG` (mục I — Liên hệ) | Bộ phận kho hàng phụ trách "hỗ trợ đăng nhập PM MODUN gym và ACB portal" |
| A2 | Hệ thống nhân sự tách rời | Toàn bộ 8 tài liệu SOP | Cổng `https://ns.ways.vn/` — "Nhân sự Ways", train hướng dẫn mở link và sử dụng chức năng |
| A3 | 100% giao tiếp qua kênh thủ công — tổng đài | Toàn bộ 8 tài liệu SOP (mục I) | Một số hotline duy nhất 0889 555 559, phân luồng phím 2 (Nhân sự), phím 3 (Điều phối), phím 8 (Kho hàng) |
| A4 | Kênh Zalo cá nhân xử lý dữ liệu PII | `GIỮ XE` (mục II — xử lý mất thẻ) | Chụp ảnh CCCD, cà vẹt xe, biên bản, thân xe, biển số và hình ảnh khách, "gửi qua Zalo cho Quản lý" |
| A5 | Sổ giấy trong quy trình vận hành | `GIỮ XE` | "Ghi số thẻ bị mất vào sổ giao ca", nộp biên bản giấy cho Thu ngân |
| A6 | Thu thập dữ liệu sinh trắc học Face ID | `THU NGÂN GYM` | Phòng tập "check-in bằng FACE ID"; khách được mời ra quầy "để lấy Face ID" |
| A7 | Thu thập thông tin cá nhân trên giấy | `THU NGÂN GYM` | Đưa "phiếu điền thông tin" cho khách để tạo hội viên |
| A8 | Cơ cấu tổ chức HQ 3 phòng ban tập trung | Toàn bộ 8 tài liệu SOP (mục I) | Phòng Nhân sự; Phòng Điều phối; Bộ phận Kho hàng; kênh phản ánh `hr@waysstation.vn` |
| A9 | Mô hình đa dịch vụ tại mỗi chi nhánh | 8 tài liệu SOP theo vị trí | Gym, Net, Bida, Cầu lông, Hub, Giữ xe, F&B |
| A10 | Chấm công bằng vân tay, quản lý ca thủ công | Toàn bộ 8 tài liệu SOP (mục I — phím 3) | Phòng Điều phối phụ trách "lấy vân tay, chấm công in/out", ca làm phát sinh |

---

# Phụ lục B — Bảng sizing chi tiết

| Thành phần | Cấu hình | Số lượng | Cơ sở tính toán |
|:---|:---|:---:|:---|
| Edge Cluster / chi nhánh | 4 vCPU, 8 GB RAM, 256 GB SSD | 34 | K3s control plane (1 vCPU/2GB) + Kafka broker (1 vCPU/2GB) + Local DB cache (1 vCPU/2GB) + đệm hệ điều hành (1 vCPU/2GB) |
| Queue Edge | ~50.000 events × ~1 KB ≈ 50 MB/48h | 34 | Ước tính 1.000 giao dịch/CN/ngày × 48h dự phòng + metadata |
| Cloud K8s node | 4 vCPU, 16 GB RAM | 6 | API Gateway (2 node), Kafka (2 node), Airflow + AI Inference (2 node); giữ tải ≤ 80% |
| API Gateway concurrency | 2.000 kết nối | — | 34 CN × ~60 thiết bị/POS = 2.040, cộng đệm 20%, làm tròn xuống 2.000 nhờ connection pooling |
| CDC throughput | 5.000 events/giây | — | 34 CN × giờ cao điểm ~150 events/giây/CN, chia tải theo phân bố thực tế |
| Data Lakehouse | 2 TB → 10 TB (3 năm) | — | 34 CN × 1.000 giao dịch/ngày × 365 ngày × ~1,5 KB ≈ 19 GB/năm dữ liệu thô; nhân hệ số 10 cho log, metadata, bản sao phân tích và mở rộng chi nhánh |
| PostgreSQL HA | 4 vCPU, 16 GB RAM | 1 cụm | Forecast DB + metadata; truy vấn báo cáo tập trung giờ hành chính |

---

# Phụ lục C — Checklist hardening (rút gọn theo CIS Benchmark)

| # | Hạng mục | Áp dụng cho | Tiêu chí pass |
|:---:|:---|:---|:---|
| C1 | Vô hiệu hoá tài khoản mặc định, đổi toàn bộ mật khẩu khởi tạo | On-Prem Server, Edge, NGFW | Không tồn tại tài khoản mặc định |
| C2 | SSH: tắt đăng nhập root, chỉ dùng key-based auth | On-Prem, Edge | Thử đăng nhập root bằng mật khẩu — bị từ chối |
| C3 | Tường lửa host-based, chỉ mở port cần thiết | Toàn bộ máy chủ | Port scan: chỉ port nghiệp vụ mở |
| C4 | Cập nhật bản vá hệ điều hành trước Go-live | Ubuntu 22.04 LTS | 0 CVE Critical/High chưa vá |
| C5 | Mã hoá ổ đĩa chứa PII Database | On-Prem HQ | LUKS/AES-256 bật, xác nhận bằng audit |
| C6 | Tắt dịch vụ không dùng | Toàn bộ | Danh sách service đang chạy được duyệt |
| C7 | Cấu hình audit log và chuyển tiếp về log tập trung | Toàn bộ | Log xuất hiện trên Loki trong ≤ 1 phút |
| C8 | Giới hạn quyền container (non-root, read-only rootfs) | K8s / K3s | Pod Security Standard mức Restricted |
| C9 | Quản lý secret bằng kho bí mật, không hardcode | Toàn bộ pipeline | Quét mã nguồn: 0 secret lộ |
| C10 | Chính sách sao lưu và kiểm tra khôi phục định kỳ | Lakehouse, PostgreSQL | Test restore hàng tháng thành công |

---

# Phụ lục D — Test plan (tóm tắt)

| Mã | Loại kiểm thử | Kịch bản | Tiêu chí pass | Pha |
|:---|:---|:---|:---|:---|
| T01 | Load Test | 2.000 concurrent connections vào API Gateway | Error rate < 0,1%; P95 ≤ 200 ms | Pha 3 |
| T02 | Stress Test | CDC pipeline 5.000 events/giây liên tục 30 phút | Không mất sự kiện; lag Kafka < 5s | Pha 3 |
| T03 | Failover Test | Tắt 1 availability zone của K8s | Hệ thống tự phục hồi ≤ 60s | Pha 2 |
| T04 | Broker Failure Test | Tắt 1 Kafka broker | Không mất message; producer/consumer tiếp tục | Pha 2 |
| T05 | Offline Test | Ngắt mạng 1 chi nhánh trong 4 giờ | Tính tiền bình thường; 100% events đồng bộ bù | Pha 4 |
| T06 | DR Drill | Chuyển đổi sang DR site, restore PITR | RTO ≤ 4h; RPO ≤ 15 phút | Pha 5 |
| T07 | Security Scan | Vulnerability scan toàn hệ thống | 0 Critical/High | Pha 4 |
| T08 | Penetration Test | Pentest thuê ngoài | 0 lỗ hổng Critical/High tồn tại > 72h | Pha 4 |
| T09 | Data Integrity Test | Đối chiếu row count trước/sau migrate | 100% khớp | Pha 4 |
| T10 | PII Audit | Quét mẫu dữ liệu trên Cloud | 0 bản ghi chứa PII plaintext | Pha 3, Pha 4 |
| T11 | UAT | Admin chi nhánh vận hành thử trên Staging | Pass 100% test case Critical/High; có sign-off | Pha 4 |
| T12 | Rollback Test | Rollback cấu hình bằng Terraform/Ansible | Hệ thống trở về trạng thái trước ≤ 15 phút | Pha 2, Pha 5 |

---

# Phụ lục E — Danh mục tài liệu tham khảo

[1] Scikit-Learn (n.d.), *Mean absolute percentage error*, https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-percentage-error
[2] Atlassian ITSM (n.d.), *Incident Management Metrics (MTTD, MTTR)*, https://www.atlassian.com/incident-management/kpis/common-metrics
[3] AWS (n.d.), *Disaster Recovery Objectives (RTO and RPO)*, https://aws.amazon.com/disaster-recovery/
[4] Google Cloud (n.d.), *Site Reliability Engineering (SRE) — Availability Table and Metrics*, https://sre.google/sre-book/availability-table/
[5] ISO/IEC (2008), *ISO/IEC 25012: Data quality model*, https://www.iso.org/standard/35736.html
[6] NIST (2020), *SP 800-175B Rev. 1: Guideline for Using Cryptographic Standards in the Federal Government: Cryptographic Mechanisms*, https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final
[7] CIS (2023), *CIS Benchmarks — Ubuntu Linux*, https://www.cisecurity.org/benchmark/ubuntu_linux
[8] Fortinet (n.d.), *FortiGate Next-Generation Firewall Datasheet*, https://www.fortinet.com/products/next-generation-firewall
[9] HashiCorp (n.d.), *Terraform Documentation*, https://developer.hashicorp.com/terraform/docs
[10] Ansible (n.d.), *Ansible Documentation*, https://docs.ansible.com/
[11] Keycloak (n.d.), *Keycloak — Open Source Identity and Access Management*, https://www.keycloak.org/documentation
[12] Apache Kafka (n.d.), *Kafka Documentation*, https://kafka.apache.org/documentation/
[13] Apache Airflow (n.d.), *Airflow Documentation*, https://airflow.apache.org/docs/
[14] Prometheus (n.d.), *Prometheus Monitoring Documentation*, https://prometheus.io/docs/
[15] Grafana (n.d.), *Grafana Documentation*, https://grafana.com/docs/
[16] PMI (2021), *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*, 7th Edition, Project Management Institute.
[17] Chính phủ Việt Nam (2023), *Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân*.
[18] Tài liệu quy trình vận hành nội bộ Ways Station (08 bộ SOP theo vị trí) — xem Phụ lục A.
