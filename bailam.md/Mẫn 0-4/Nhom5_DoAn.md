# ĐỒ ÁN MÔN HỌC: ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT
**Dự án:** Triển khai Nền tảng Tích hợp (App & Integration) và Nền tảng Dữ liệu (Data Platform) cho chuỗi Ways Station
**Thực hiện:** Nhóm 5

---

## Bước 0 — Xác định phạm vi đề xuất (đầu tư cái gì?)
Dự án tập trung tái cấu trúc hạ tầng IT cho chuỗi Ways Station (34+ chi nhánh), giải quyết triệt để tình trạng phân mảnh của các "ốc đảo phần mềm" (Gym, Net, Bida). Phạm vi đầu tư được giới hạn nghiêm ngặt ở **Lớp (4) App & Integration Platform** và **Lớp (5) Data Platform**, tận dụng lại Compute/Network nền tảng:
- **Phần mềm (SW):** 
  - *Lớp 4:* Triển khai API Gateway (Kong/Tyk), Message Queue (Kafka), Container orchestration (Kubernetes/K3s) thay thế các tích hợp điểm-điểm thủ công.
  - *Lớp 5:* Thiết lập Data Lakehouse, các công cụ Data Streaming (Debezium CDC), và Data Catalog để chuẩn hóa luồng dữ liệu thời gian thực.
- **Mạng (Network):** Xây dựng API traffic control nội bộ, Ingress/Egress định tuyến giữa chi nhánh và Cloud, thiết lập đường truyền Data Ingest mã hóa.
- **Quản trị & Bảo mật (Ops/Security):** Xây dựng CI/CD Pipeline (GitLab CI/ArgoCD), chuẩn hóa Data Governance, áp dụng IAM (Keycloak - OIDC/SAML) và mã hóa dữ liệu (Encryption at-rest/in-transit) chống rò rỉ theo NĐ13.

## Bước 1 — Khảo sát hiện trạng hạ tầng (AS-IS) có số liệu
*Khảo sát cho thấy hệ thống đang bế tắc ở 3 điểm nghẽn chính:*
- **Vấn đề 1 (Tích hợp & Vận hành):** 100% ứng dụng tại 34 chi nhánh (POS, Kho, CRM) chạy độc lập cục bộ, không có API trung tâm. Hệ thống thường xuyên bị quá tải/crash vào giờ cao điểm. Việc khớp nối số liệu phải dùng "trục tích hợp chạy bằng cơm" tiêu tốn hàng ngàn giờ công mỗi tháng.
- **Vấn đề 2 (Dữ liệu & Dự báo):** Không có kho dữ liệu tập trung, độ trễ báo cáo (Data Latency) lên tới 48 giờ. Quản lý chi nhánh không có công cụ Data Analytics để dự báo nhu cầu nhập nguyên vật liệu F&B, hoàn toàn phải nhập hàng theo cảm tính chủ quan.
- **Vấn đề 3 (Bảo mật & Tuân thủ):** Ứng dụng công nghệ nhận diện khuôn mặt (Face ID) nhưng dữ liệu PII này lại được lưu trữ phân tán, không mã hóa và luân chuyển qua Zalo. Backup thủ công khiến RPO (điểm phục hồi dữ liệu) lên tới 24h.

## Bước 2 — Nêu vấn đề & rủi ro nếu không đầu tư (Why now?)
*Từ 3 vấn đề ở Bước 1, nếu không nâng cấp Lớp 4 & Lớp 5, Ways Station đang phải gánh chịu khoản "Nợ kỹ thuật" và tổn thất tài chính định lượng ước tính **~6.3 Tỷ VNĐ/năm**, cụ thể:*
- **Từ Vấn đề 1 (Đứt gãy tích hợp):** Việc thiếu API Gateway và hệ thống hay bị tải chậm/crash giờ cao điểm gây thiệt hại doanh thu (Downtime Cost) khoảng **2.4 Tỷ VNĐ/năm**. Bên cạnh đó, việc dùng "trục tích hợp chạy bằng cơm" tiêu tốn hàng nghìn giờ nhập liệu kép, gây lãng phí sức lao động (Manual Labor Waste) lên tới **2.7 Tỷ VNĐ/năm**.
- **Từ Vấn đề 2 (Mù dữ liệu thời gian thực):** Việc trễ dữ liệu 48h khiến hệ thống không thể tạo ra **"Dữ liệu Vàng"** để huấn luyện AI dự báo lưu lượng khách (LSTM/Transformer). Hệ lụy trực tiếp:
  1. *Phòng Nhân sự:* Xếp ca sai lệch, lãng phí quỹ lương giờ thấp điểm.
  2. *Phòng Kho bãi:* Thiếu Data Analytics dự báo nhập hàng dẫn đến dư thừa, làm lãng phí nguyên vật liệu hư hỏng **~1.2 Tỷ VNĐ/năm**.
  3. *Phòng Marketing:* Đánh mất khả năng tung chiến dịch kích cầu (Flash Sale) vào đúng thời điểm.
- **Từ Vấn đề 3 (Bảo mật lỏng lẻo):** Dữ liệu phân mảnh và không mã hóa tạo ra lỗ hổng bảo mật chết người đối với **Dữ liệu Sinh trắc học (Face ID)**. Rủi ro rò rỉ dữ liệu PII này trực tiếp đối diện mức phạt lên tới **5% tổng doanh thu** theo Nghị định 13/2023/NĐ-CP, đồng thời phá hủy uy tín thương hiệu của toàn chuỗi.

## Bước 3 — Xác lập mục tiêu & KPI hạ tầng (TO-BE)
*KPI của hệ thống không chỉ là các chỉ số kỹ thuật khô khan, mà là "tấm khiên" bảo vệ dòng tiền của Ways Station. Cấu trúc KPI dưới đây được tham chiếu từ các chuẩn quốc tế (Google SRE, AWS, ISO) để giải quyết trực tiếp 3 rủi ro cốt lõi ở Bước 2.*

### 3.1. Sự liên kết: Vấn đề $\rightarrow$ Mục tiêu (KPI) $\rightarrow$ Kiến trúc
- **Từ Vấn đề 1 (Đứt gãy Tích hợp $\rightarrow$ Thiệt hại 5.1 tỷ):** 
  - *Mục tiêu:* Đảm bảo tính sẵn sàng cao và xử lý sự cố siêu tốc.
  - *KPI:* Uptime $\ge 99.99\%$; MTTR $\le 30$ phút. 
  - *Giải pháp (Bước 4):* Triển khai Lớp Edge (K3s, Kafka) tại chi nhánh kết hợp API Gateway.
- **Từ Vấn đề 2 (Mù Dữ liệu $\rightarrow$ Thiệt hại 1.2 tỷ):** 
  - *Mục tiêu:* Cung cấp "Dữ liệu Vàng" thời gian thực cho 3 phòng ban (Nhân sự xếp ca, Kho bãi nhập hàng, Marketing kích cầu).
  - *KPI:* Data Freshness $\le 5$ giây; Sai số dự báo AI (MAPE) $< 15\%$.
  - *Giải pháp (Bước 4):* Xây dựng Data Lakehouse trên Public Cloud chạy mô hình học sâu chuỗi thời gian (LSTM/Transformer).
- **Từ Vấn đề 3 (Bảo mật $\rightarrow$ Rủi ro phạt 5% doanh thu):** 
  - *Mục tiêu:* Ngăn chặn rò rỉ Face ID và khôi phục dữ liệu tức thời khi có thảm họa.
  - *KPI:* Mã hóa $100\%$ PII; RPO $\le 15$ phút.
  - *Giải pháp (Bước 4):* Giữ hệ thống Quản lý định danh (IAM) ở máy chủ On-premise theo kiến trúc Zero Trust.

### 3.2. Định lượng KPI bằng Toán học & Tiêu chuẩn Quốc tế

**A. Độ tin cậy hạ tầng (IT Reliability - Theo chuẩn Google SRE & Atlassian)**
1. **Tính sẵn sàng (Availability / Uptime) $\ge 99.99\%$:**
   - *Công thức:* $Uptime = \frac{Total Time - Downtime}{Total Time} \times 100\%$
   - *Ràng buộc:* Tổng thời gian chết (Downtime) trong 1 tháng (43,200 phút) không được vượt quá **4.32 phút**.
   - *Nguồn tham khảo chuẩn:* [[7]](#ref7)
2. **Thời gian phục hồi trung bình (MTTR - Mean Time To Recovery) $\le 30$ phút:**
   - *Công thức:* $MTTR = \frac{\text{Tổng thời gian gián đoạn (Downtime)}}{\text{Tổng số lượng sự cố}}$
   - *Ý nghĩa:* Hệ thống K3s/Kubernetes phải tự động khôi phục (self-heal) service bị lỗi trước khi gián đoạn diện rộng.
   - *Nguồn tham khảo chuẩn:* [[4]](#ref4)

**B. Khả năng khôi phục sau thảm họa (Disaster Recovery - Theo chuẩn AWS & IBM)**
3. **Mục tiêu điểm khôi phục (RPO - Recovery Point Objective) $\le 15$ phút:**
   - *Ý nghĩa:* Dung sai mất mát dữ liệu lớn nhất khi hệ thống sập. Data Streaming qua Kafka giúp đồng bộ Real-time, giảm RPO từ 24h (như ở Bước 1) xuống dưới 15 phút.
   - *Nguồn tham khảo chuẩn:* [[5]](#ref5)
4. **Thời gian khôi phục dịch vụ (RTO - Recovery Time Objective) $\le 2$ giờ.**
   - *Nguồn tham khảo chuẩn:* [[6]](#ref6)

**C. Chất lượng Dữ liệu & AI (Data Quality & AI - Theo chuẩn ISO & Scikit-Learn)**
5. **Độ trễ dữ liệu (Data Freshness) $\le 5$ giây:**
   - *Công thức:* $\Delta t_{freshness} = t_{DataLake} - t_{POS} \le 5s$. Xóa bỏ tình trạng trễ báo cáo Excel thủ công 48h.
   - *Nguồn tham khảo chuẩn:* [[9]](#ref9)
6. **Sai số tuyệt đối trung bình phần trăm của mô hình AI (MAPE) $< 15\%$:**
   - *Công thức:* $MAPE = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%$ *(Với $y_i$ là số khách thực tế, $\hat{y}_i$ là số khách dự báo)*.
   - *Ý nghĩa:* Tỷ lệ dự báo chính xác $> 85\%$ là cơ sở toán học để ứng dụng "Dữ liệu Vàng", giúp phòng Kho bãi thu hồi 1.2 tỷ thiệt hại nguyên liệu F&B.
   - *Nguồn tham khảo chuẩn:* [[1]](#ref1)

**D. Bảo mật & Tuân thủ (Security & Compliance - Theo NĐ13/2023/NĐ-CP)**
7. **Tỷ lệ mã hóa dữ liệu nhạy cảm (PII Encryption Rate) $= 100\%$:**
   - Toàn bộ ảnh CCCD và sinh trắc Face ID bắt buộc mã hóa chuẩn AES-256 (lưu trữ) và TLS 1.3 (đường truyền).
   - *Nguồn tham khảo chuẩn:* [[8]](#ref8)

## Bước 4 — Xây dựng phương án kiến trúc TO-BE (2–3 lựa chọn)
*Để đạt được bộ KPI khắt khe ở Bước 3, kiến trúc hệ thống cần sự linh hoạt tối đa. Chúng tôi tiến hành đánh giá 3 kịch bản kiến trúc thông qua 2 góc nhìn: Tổng quan đáp ứng tính năng (Checkbox) và Phân tích chuyên sâu (Chấm điểm).*

### 4.1. Ma trận tổng quan đáp ứng tiêu chí cốt lõi
| Tiêu chí Đánh giá cốt lõi | Kịch bản 1: 100% On-premise | Kịch bản 2: Hybrid Cloud (Khuyến nghị) | Kịch bản 3: 100% Cloud-Native |
| :--- | :---: | :---: | :---: |
| **1. Tối ưu vốn đầu tư ban đầu (Low CapEx)** | [ ] | [x] | [x] |
| **2. Tối ưu chi phí vận hành dài hạn (Low OpEx)** | [ ] | [x] | [ ] |
| **3. Khả năng mở rộng tự động (Auto-scaling)** | [ ] | [x] | [x] |
| **4. Triển khai dịch vụ nhanh (Time-to-Market)** | [ ] | [x] | [x] |
| **5. Kiểm soát bảo mật vật lý (Data Security)** | [x] | [x] | [ ] |
| **6. Tuân thủ vị trí lưu trữ tại VN (NĐ13)** | [x] | [x] | [ ] |
| **7. Giảm tải gánh nặng bảo trì hạ tầng IT** | [ ] | [x] | [x] |
| **8. Dự phòng thảm họa đa trung tâm (Active-Active)** | [ ] | [x] | [x] |
| **Tổng số tiêu chí đáp ứng** | **2 / 8** | **8 / 8** | **5 / 8** |

### 4.2. Ma trận phân tích đánh giá chuyên sâu (Thang điểm 1-5)
| Tiêu chí Đánh giá (Trọng số cốt lõi) | Kịch bản 1: 100% On-premise | Kịch bản 2: Hybrid Cloud (Khuyến nghị) | Kịch bản 3: 100% Cloud-Native |
| :--- | :---: | :---: | :---: |
| **1. Tối ưu vốn đầu tư (CapEx) ban đầu** | 1 (Rất cao, tốn kém Server/SAN) | **3** (Trung bình, kế thừa hiện tại) | 5 (Rất thấp, gần như bằng 0) |
| **2. Tối ưu chi phí vận hành (OpEx)** | 4 (Cố định, nhưng lãng phí tài nguyên) | **3** (Pay-as-you-go, có thể tối ưu FinOps) | 1 (Rủi ro Bill Shock cực cao) |
| **3. Khả năng mở rộng (Scalability)** | 1 (Kém, tốn hàng tháng để mua sắm) | **4** (Tốt, Auto-scale vô hạn trên Cloud) | 5 (Serverless tự co giãn micro-giây) |
| **4. Agility & Time-to-Market (TTM)** | 2 (Chậm, phụ thuộc quy trình tĩnh) | **4** (Nhanh, dùng IaC và CI/CD) | 5 (Rất nhanh nhờ PaaS/SaaS) |
| **5. Bảo mật Dữ liệu (Data Security)** | 5 (Kiểm soát vật lý tuyệt đối) | **4** (Rất tốt, PII On-prem, Data Cloud mã hóa) | 2 (Rủi ro lộ lọt cấu hình) |
| **6. Tuân thủ Pháp lý (Nghị định 13)** | 5 (100% tuân thủ, máy chủ tại VN) | **5** (Tuân thủ, phần nhạy cảm giữ tại VN) | 2 (Phụ thuộc vị trí Region của Cloud) |
| **7. Quản trị Vận hành (Maintenance)** | 2 (Cực nhọc bảo trì vật lý) | **3** (Đòi hỏi team DevOps giỏi) | 4 (Hạ tầng do Provider lo) |
| **8. Khả năng phục hồi (DR/BCP)** | 1 (Active-Passive tốn kém gấp đôi) | **4** (Active-Active giữa Cloud & On-prem) | 5 (Multi-Region Cloud) |
| **Tổng điểm Đánh giá** | **21 / 40** | **30 / 40** | **29 / 40** |

**Cơ sở biện luận chọn Kịch bản 2 (Hybrid Cloud - Đáp ứng 8/8 tiêu chí, Đạt 30/40 điểm):**
Kiến trúc Hybrid Cloud là giải pháp **duy nhất** cân bằng hoàn hảo giữa Rủi ro (Risk) và Lợi ích (Reward) để xử lý triệt để 3 vấn đề cốt lõi của dự án:
- **Tối ưu Vận hành & Sức mạnh AI:** Đẩy Lớp Tích hợp (API Gateway, Event Bus) và Data Lakehouse lên Public Cloud giúp tận dụng khả năng co giãn tự động (Auto-scaling) để hứng lượng truy cập khổng lồ giờ cao điểm và cung cấp sức mạnh điện toán vô hạn để huấn luyện AI dự báo. Ở dưới chi nhánh, Lớp Edge (K3s, Kafka) vẫn duy trì hoạt động tính tiền offline khi mất mạng diện rộng, đảm bảo SLA Uptime 99.99%.
- **Tuân thủ Bảo mật & Kiến trúc Zero Trust:** Dữ liệu nhạy cảm cực cao (sinh trắc học Face ID, hồ sơ hội viên) và hệ thống Quản lý định danh (IAM) được giữ lại tại máy chủ On-premise. Nhờ đó, doanh nghiệp kiểm soát vật lý tuyệt đối dữ liệu PII, tuân thủ nghiêm ngặt Nghị định 13/2023/NĐ-CP, hoàn toàn loại bỏ "tử huyệt" mất kiểm soát dữ liệu của kịch bản 100% Cloud.

## Bước 5 — Danh mục tài liệu tham khảo
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
