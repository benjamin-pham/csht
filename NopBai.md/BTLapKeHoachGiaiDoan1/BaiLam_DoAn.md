# ĐỒ ÁN MÔN HỌC: ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT
**Dự án:** Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station

---

## BƯỚC 1: KHẢO SÁT HIỆN TRẠNG HẠ TẦNG (AS-IS) CÓ SỐ LIỆU

**1. Phạm vi đầu tư:**
- **Đơn vị thụ hưởng:** Chuỗi Ways Station (34+ chi nhánh đa dịch vụ: Gym, Gaming, Billiards, Cầu lông, Hub).
- **Lớp năng lực đầu tư:** Lớp (4) Nền tảng ứng dụng & tích hợp (App & Integration Platform) và Lớp (5) Nền tảng dữ liệu (Data Platform). Kế thừa hạ tầng mạng và phần cứng hiện có.

**2. Điểm nghẽn hiện trạng (Baseline có định lượng):**
- **Điểm nghẽn 1 (Tích hợp & Vận hành Lớp 4):** 34 chi nhánh sở hữu 8 hệ thống phần mềm rời rạc (POS, Bida, Gym, Kho...) hoạt động độc lập và phân mảnh. Tỉ lệ luồng tích hợp tự động là **0%**. 100% giao tiếp đi qua 3 kênh thủ công (Tổng đài, Zalo, Sổ giấy).
- **Điểm nghẽn 2 (Dữ liệu & Quyết định Lớp 5):** Không có kho dữ liệu tập trung. Báo cáo được làm thủ công bằng Excel tiêu tốn **~2.500 giờ công/năm**. Độ trễ dữ liệu phục vụ quản trị lên tới **24 - 48 giờ**. Tỷ lệ sai lệch số liệu doanh thu khi đối soát là **3,8%**.
- **Điểm nghẽn 3 (Bảo mật & Định danh Lớp 3/4):** Khách hàng phải dùng tài khoản riêng cho từng mảng. Đáng lưu ý, 100% ảnh giấy tờ tùy thân của khách hàng và dữ liệu Face ID được gửi qua Zalo cá nhân của nhân viên, không có cơ chế mã hóa. Sao lưu cục bộ có tỉ lệ thành công chỉ **47%** với RPO lên đến 24 giờ.

## BƯỚC 2: NÊU VẤN ĐỀ VÀ RỦI RO NẾU KHÔNG ĐẦU TƯ (WHY NOW?)

Từ các điểm nghẽn hiện trạng, hệ thống đang phải đối mặt với nhiều hạn chế kỹ thuật và rủi ro lớn nếu không được giải quyết ngay:

- **Rủi ro vận hành (Vấn đề 1 - Đứt gãy tích hợp):** Việc thiếu API Gateway khiến hệ thống chịu tải kém vào giờ cao điểm, gây gián đoạn bán hàng. Thời gian phát hiện sự cố chậm (4-8 giờ). Hàng ngàn giờ công bị lãng phí do đối soát thủ công và nhập liệu kép.
- **Rủi ro chiến lược (Vấn đề 2 - Mù dữ liệu thực thời):** Độ trễ dữ liệu 48 giờ khiến việc ra quyết định bị chậm trễ. Việc thiếu nguồn dữ liệu chuẩn hóa và tập trung để phân tích và dự báo nhu cầu dẫn đến lãng phí nguyên vật liệu F&B và sai lệch trong việc sắp xếp ca trực của nhân viên. Không thể bán chéo dịch vụ do khách hàng không có định danh duy nhất (SSO).
- **Rủi ro tuân thủ (Vấn đề 3 - Lỗ hổng bảo mật PII):** Việc lưu trữ dữ liệu cá nhân (PII) như ảnh CCCD, Face ID phân tán trên điện thoại cá nhân vi phạm nghiêm trọng **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân. Doanh nghiệp đối mặt với rủi ro bị phạt lên đến 5% tổng doanh thu và đánh mất uy tín thương hiệu.

## BƯỚC 3: XÁC LẬP MỤC TIÊU VÀ KPI HẠ TẦNG (TO-BE)

Bộ KPI kỹ thuật được thiết lập theo chuẩn quốc tế nhằm giải quyết triệt để 3 vấn đề nêu trên. Tính liên kết chặt chẽ được thể hiện thông qua Ma trận Truy vết (Traceability Matrix).

### Ma trận Truy vết: Vấn đề $\rightarrow$ Mục tiêu $\rightarrow$ KPI
| Vấn đề giải quyết | Mục tiêu kiến trúc | KPI Kỹ thuật đo lường (Target) |
| :--- | :--- | :--- |
| **Vấn đề 1:** Đứt gãy tích hợp, gián đoạn kinh doanh | Đảm bảo hệ thống đạt độ sẵn sàng cao, có khả năng tự phục hồi nhanh (Self-healing). | KPI 1.1: **Uptime $\ge$ 99.99%** <br> KPI 1.2: **MTTR $\le$ 30 phút** |
| **Vấn đề 2:** Mù dữ liệu, báo cáo thủ công | Cung cấp dữ liệu chuẩn thời gian thực cho kho dữ liệu và hỗ trợ thuật toán AI dự báo chính xác. | KPI 2.1: **Độ trễ dữ liệu $\le$ 5 giây** <br> KPI 2.2: **Sai số dự báo (MAPE) $<$ 15%** |
| **Vấn đề 3:** Lỗ hổng rò rỉ dữ liệu PII | Ngăn chặn rò rỉ PII và đảm bảo không mất mát dữ liệu quan trọng khi có thảm họa. | KPI 3.1: **Tỷ lệ mã hóa PII = 100%** <br> KPI 3.2: **RPO $\le$ 15 phút** |

### Định lượng KPI theo công thức chuẩn (Standards)

1. **KPI 1.1 - Tính sẵn sàng (Availability / Uptime) $\ge 99.99\%$ (Chuẩn Google SRE):**
   - *Công thức:* $Uptime = \frac{\text{Total Time} - \text{Downtime}}{\text{Total Time}} \times 100\%$
   - *Ràng buộc:* Tổng thời gian chết (Downtime) trong 1 tháng (43.200 phút) không vượt quá 4,32 phút.

2. **KPI 1.2 - Thời gian khôi phục trung bình (MTTR) $\le 30$ phút (Chuẩn Atlassian ITSM):**
   - *Công thức:* $MTTR = \frac{\text{Tổng thời gian gián đoạn (Downtime)}}{\text{Tổng số lượng sự cố}}$
   - *Ý nghĩa:* Hệ thống (VD: Kubernetes) phải tự động khởi tạo lại service lỗi trong vài phút trước khi ảnh hưởng diện rộng.

3. **KPI 2.1 - Độ trễ dữ liệu (Data Freshness) $\le 5$ giây (Chuẩn ISO/IEC 25012):**
   - *Công thức:* $\Delta t_{freshness} = t_{DataLake} - t_{POS} \le 5s$. (Rút ngắn độ trễ từ 48 giờ xuống vài giây).

4. **KPI 2.2 - Sai số dự báo mô hình AI (MAPE) $< 15\%$ (Chuẩn Scikit-Learn):**
   - *Công thức:* $MAPE = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%$ *(Với $y_i$ là số khách thực tế, $\hat{y}_i$ là dự báo).*

5. **KPI 3.2 - Mục tiêu điểm khôi phục (RPO) $\le 15$ phút (Chuẩn AWS DR):**
   - *Ý nghĩa:* Dung sai mất mát dữ liệu tối đa tính từ thời điểm thảm họa xảy ra là 15 phút.

## BƯỚC 4: XÂY DỰNG PHƯƠNG ÁN KIẾN TRÚC TO-BE

Để thỏa mãn bộ KPI khắt khe trên đồng thời đảm bảo đặc thù nghiệp vụ (các điểm bán phải tiếp tục tính tiền offline kể cả khi đứt cáp internet), dự án phân tích 3 kịch bản kiến trúc:

### 1. Bảng so sánh 3 kịch bản kiến trúc

| Tiêu chí bắt buộc để đạt KPI | On-Premise 100% (Tập trung) | Cloud-Native 100% (Thuần đám mây) | Hybrid Cloud (Lai) - Khuyến nghị |
| :--- | :---: | :---: | :---: |
| **1. Đảm bảo Uptime 99.99% khi rớt mạng chi nhánh** | [x] | [ ] | [x] |
| **2. Khả năng mở rộng tự động (Auto-scaling)** | [ ] | [x] | [x] |
| **3. Tuân thủ vị trí lưu trữ dữ liệu PII (Nghị định 13)** | [x] | [ ] | [x] |
| **4. Tối ưu chi phí đầu tư ban đầu (CAPEX) thấp** | [ ] | [x] | [x] |
| **5. Thời gian triển khai dịch vụ nhanh (Agility)** | [ ] | [x] | [x] |
| **6. Khả năng khôi phục thảm họa (Active-Active)** | [ ] | [x] | [x] |
| **Tổng số tiêu chí đáp ứng** | **2 / 6** | **4 / 6** | **6 / 6** |

### 2. Sự liên kết và Cơ sở biện luận chọn HYBRID CLOUD
**Phương án lựa chọn: Kịch bản Hybrid Cloud (Lai)**
Kiến trúc Hybrid Cloud là giải pháp duy nhất cân bằng hoàn hảo giữa Rủi ro (Risk) và Lợi ích (Reward) để xử lý triệt để bài toán mâu thuẫn (như thể hiện ở bảng trên): Vừa cần sức mạnh co giãn của Cloud (đáp ứng Tiêu chí 2, 4, 5, 6) để xử lý dữ liệu và tích hợp API, vừa cần độ ổn định độc lập tại chi nhánh để đối phó với rủi ro rớt mạng (đáp ứng Tiêu chí 1) và tuân thủ vị trí lưu trữ (đáp ứng Tiêu chí 3). Cơ sở biện luận được thiết kế liên kết chặt chẽ với các KPI như sau:

- **Hợp nhất Lớp 4 & Tăng cường Uptime (Đạt KPI 1.1 & 1.2):** Cổng API Gateway và hệ thống điều phối thông điệp (Kafka) được đặt trên Public Cloud để tiếp nhận hàng ngàn request cùng lúc. Tại 34 chi nhánh sẽ cài đặt Edge Cluster (K3s/Kafka con) hoạt động như bộ đệm. Khi chi nhánh mất kết nối mạng, phần mềm vẫn gọi API cục bộ để tính giờ ưu tiên ngoại tuyến; khi có mạng, dữ liệu tự đồng bộ bù về Cloud, đảm bảo MTTR $\le 30$ phút mà khách hàng không bị gián đoạn.
- **Hợp nhất Lớp 5 & Nâng cao chất lượng dữ liệu (Đạt KPI 2.1 & 2.2):** Xây dựng kho dữ liệu (Data Lakehouse) trên Cloud cung cấp sức mạnh điện toán vô hạn. Áp dụng luồng Data Streaming (CDC) để bắt sự kiện thay đổi dữ liệu tại chi nhánh đẩy thẳng về Cloud trong thời gian thực, đáp ứng Data Freshness $\le 5s$, làm đầu vào chất lượng cho mô hình học máy (Machine Learning) tối ưu hóa dự báo.
- **Bảo mật PII & Tuân thủ NĐ13 (Đạt KPI 3.1 & 3.2):** Kiến trúc tuân thủ mô hình Zero Trust. Các thông tin định danh nhạy cảm cực cao (Face ID, thẻ CCCD) và hệ thống Quản lý định danh (IAM) được giữ lại tại máy chủ vật lý On-Premise do doanh nghiệp tự quản lý và mã hóa AES-256 100%. Dữ liệu vận hành (hóa đơn, điểm danh) được ẩn danh trước khi đẩy lên Cloud, hoàn toàn loại bỏ rủi ro mất kiểm soát dữ liệu và tuân thủ tuyệt đối Nghị định 13/2023/NĐ-CP.

## BƯỚC 5: DANH MỤC TÀI LIỆU THAM KHẢO
<a id="ref1"></a>[1] Scikit-Learn (n.d.), *Mean absolute percentage error*, truy cập tại: https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-percentage-error
<a id="ref2"></a>[2] Atlassian ITSM (n.d.), *Incident Management Metrics (MTTD, MTTR)*, truy cập tại: https://www.atlassian.com/incident-management/kpis/common-metrics
<a id="ref3"></a>[3] AWS (n.d.), *Disaster Recovery Objectives (RTO and RPO)*, truy cập tại: https://aws.amazon.com/disaster-recovery/
<a id="ref4"></a>[4] Google Cloud (n.d.), *Site Reliability Engineering (SRE) - Availability Table and Metrics*, truy cập tại: https://sre.google/sre-book/availability-table/
<a id="ref5"></a>[5] ISO/IEC (2008), *ISO/IEC 25012: Data quality model*, truy cập tại: https://www.iso.org/standard/35736.html
