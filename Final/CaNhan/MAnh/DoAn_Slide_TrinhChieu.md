---
marp: true
theme: default
paginate: true
header: 'Đồ án: Đề xuất đầu tư hạ tầng CNTT - Ways Station'
footer: 'Nhóm 5 - Lớp IE101.F32'
---

# ĐỒ ÁN MÔN HỌC
## ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT
**Dự án:** Đầu tư nền tảng tích hợp ứng dụng và dữ liệu tập trung cho chuỗi Ways Station
**Nhóm thực hiện:** Nhóm 5 (9 thành viên)
**Thời lượng:** 45 Phút

---
<!-- Người 1 -->
## 1. Tóm tắt dự án (Executive Summary)
- **Bối cảnh:** Ways Station sở hữu 34 chi nhánh (Net, Gym, Bida...) đang phát triển nóng.
- **Thách thức:** 
  - Phân mảnh dữ liệu thành 34 "ốc đảo".
  - Đứt gãy tích hợp hệ thống.
  - Rủi ro pháp lý nghiêm trọng về dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP).
- **Giải pháp:** Đầu tư Nền tảng tích hợp (Lớp 4), Dữ liệu (Lớp 5) và Bảo mật IAM (Lớp 3).
- **Kiến trúc đề xuất:** Hybrid Cloud (Đám mây lai).

---
<!-- Người 1 -->
## 2. Tổng quan Đầu tư & Hiệu quả
- **Tổng mức đầu tư (CAPEX):** 1.308.800.000 VNĐ.
- **Chi phí sở hữu (TCO 3 năm):** ~5,2 tỷ VNĐ (chỉ chiếm ~1,45% doanh thu).
- **Thời gian hoàn vốn:** Khoảng 1,7 năm.
- **Khuyến nghị:** 
  - Phê duyệt khởi động dự án (Pha 1) ngay trong quý tới.
  - Ngăn chặn triệt để rủi ro bị phạt đến 5% doanh thu do vi phạm Nghị định 13.

---
<!-- Người 2 -->
## 3. Hiện trạng AS-IS: 34 "Ốc đảo" dữ liệu
- **Đặc thù pháp lý:** 34 chi nhánh là 34 hộ kinh doanh cá thể riêng biệt.
- **Hệ thống phần mềm:** 8 phần mềm rời rạc (POS Net, POS Bida, PM Gym, Kho, Nhân sự...).
- **Tích hợp tự động (0%):** Các phần mềm không có API liên thông.
- **Giao tiếp thủ công (100%):** Mọi tương tác chi nhánh - Trụ sở (HQ) qua:
  - Tổng đài duy nhất 0889 555 559.
  - Zalo cá nhân.
  - Sổ giao ca bằng giấy.

---
<!-- Người 2 -->
## 4. Vấn đề 1: Đứt gãy tích hợp (Rủi ro Vận hành)
- **Thiếu API Gateway:** 
  - Hệ thống dễ quá tải, sập nguồn vào giờ cao điểm.
  - Không tự động mở rộng (Auto-scaling).
- **Phát hiện sự cố chậm:** Thời gian phát hiện lỗi từ 4-8 giờ do phụ thuộc báo cáo Zalo.
- **Hậu quả:** 
  - Khách hàng không thể tính tiền, gián đoạn kinh doanh.
  - Lãng phí hàng ngàn giờ công nhập liệu kép giữa các bộ phận.

---
<!-- Người 3 -->
## 5. Vấn đề 2: Mù dữ liệu thực thời (Rủi ro Chiến lược)
- **Không có Data Warehouse tập trung:** 
  - HQ tổng hợp báo cáo thủ công qua Excel.
  - Tiêu tốn ~2.500 giờ công/năm.
- **Độ trễ dữ liệu cực cao:** Lên tới 24 - 48 giờ mới có báo cáo cho Ban Giám đốc.
- **Hậu quả:** 
  - Quyết định kinh doanh chậm trễ.
  - Tỉ lệ sai lệch số liệu doanh thu 3,8%.
  - Lãng phí nguyên liệu F&B và không thể bán chéo dịch vụ.

---
<!-- Người 3 -->
## 6. Vấn đề 3: Lỗ hổng bảo mật PII (Rủi ro Tuân thủ)
- **Thực trạng thu thập PII:**
  - Ảnh CCCD, Cà vẹt xe, Face ID của khách hàng thu thập tràn lan.
  - Gửi qua Zalo cá nhân của nhân viên lên cho Quản lý.
- **Bảo mật:** 0% dữ liệu được mã hóa (lưu plaintext).
- **Hậu quả:**
  - Vi phạm nghiêm trọng Nghị định 13/2023/NĐ-CP (Mức phạt: 5% tổng doanh thu).
  - Tỉ lệ sao lưu thành công chỉ 47%, RPO lên tới 24h $\rightarrow$ Dễ mất sạch dữ liệu khi có thảm họa.

---
<!-- Người 4 -->
## 7. Mục tiêu Kiến trúc & KPI (Phần 1)
Thiết lập KPI dựa trên chuẩn quốc tế (Google SRE, Atlassian ITSM):
- **KPI 1.1 - Tính sẵn sàng (Availability):** $\ge$ 99,99% (Downtime $\le$ 4,32 phút/tháng).
- **KPI 1.2 - Thời gian phục hồi (MTTR):** $\le$ 30 phút (Hệ thống tự động Self-healing).
- **KPI 2.1 - Độ trễ dữ liệu (Data Freshness):** $\le$ 5 giây cho luồng CDC (Change Data Capture) từ chi nhánh về Cloud.

---
<!-- Người 4 -->
## 8. Mục tiêu Kiến trúc & KPI (Phần 2)
- **KPI 2.2 - Chất lượng dữ liệu:**
  - Completeness $\ge$ 99,5%.
  - Sai lệch đối soát doanh thu giảm từ 3,8% xuống $\le$ 0,5%.
- **KPI 3.1 - Bảo mật (Encryption):** 100% dữ liệu PII được mã hóa (at-rest & in-transit).
- **KPI 3.2 - Điểm khôi phục (RPO):** $\le$ 15 phút.

---
<!-- Người 5 -->
## 9. Phạm vi Đầu tư theo Lớp năng lực
*Không mua sắm thiết bị rời rạc, đầu tư nền tảng:*
- **Lớp 4 (Ứng dụng & Tích hợp):** API Gateway, Kafka, Container (Cloud K8s + Edge K3s).
- **Lớp 5 (Dữ liệu):** Data Lakehouse, Airflow ETL, CDC Streaming.
- **Lớp 3 (Bảo mật - Chọn lọc):** IAM/SSO (Keycloak), Mã hóa PII.
- **Ngoài phạm vi:** Network đường truyền lõi, thiết bị mạng chi nhánh, hệ thống SIEM/SOC, AI Inference (được làm ở đề tài thực hành).

---
<!-- Người 5 -->
## 10. Giả định & Ràng buộc thiết kế
- **Đặc thù pháp lý:** 34 chi nhánh vẫn là các hộ kinh doanh riêng biệt (không dùng chung pháp nhân).
- **Ràng buộc sinh tử (Offline Mode):** Hệ thống tại chi nhánh phải tiếp tục hoạt động, tính tiền được kể cả khi đứt cáp Internet.
- **Ràng buộc pháp lý:** Dữ liệu cá nhân nhạy cảm phải nằm trên máy chủ tại Việt Nam do chính HQ kiểm soát.
- **Vận hành:** Không có nhân viên IT túc trực tại 34 chi nhánh.

---
<!-- Người 6 -->
## 11. Đánh giá 3 Kịch bản Kiến trúc
1. **On-Premise 100%:**
   - Ưu: Đáp ứng luật pháp, bán hàng offline tốt.
   - Nhược: CAPEX quá cao (~2,8 tỷ), không mở rộng tự động.
2. **Cloud-Native 100%:**
   - Ưu: Rẻ, co giãn tốt, triển khai nhanh.
   - Nhược: **Mất mạng là mất doanh thu**, rủi ro rò rỉ dữ liệu, OPEX cao nhất.
3. **Hybrid Cloud (Đám mây lai) - ĐỀ XUẤT:**
   - Đáp ứng cả 6/6 tiêu chí cốt lõi.

---
<!-- Người 6 -->
## 12. Tại sao chọn Hybrid Cloud?
Kiến trúc đáp ứng trực tiếp đặc thù của Ways Station:
- **Xử lý tải nặng:** Đẩy lên Public Cloud (API, Kafka, Data Lake).
- **Hoạt động Offline:** Cắm các Edge Server mini tại 34 chi nhánh, lưu đệm giao dịch 48h (Store-and-Forward), tự đồng bộ khi có mạng.
- **Bảo mật tuyệt đối:** Server chứa định danh (SSO) và DB PII đặt On-Premise tại Trụ sở chính (HQ).

---
<!-- Người 7 -->
## 13. Sơ đồ Kiến trúc TO-BE
*(Vui lòng trình chiếu trực tiếp hình ảnh sơ đồ kiến trúc Hybrid Cloud từ tài liệu v2)*
**Ba khối chính:**
1. **Public Cloud:** API Gateway, Kafka Cluster, K8s, Data Lakehouse.
2. **34 Chi nhánh (Edge):** Edge K3s, Kafka con, Local DB. Dữ liệu vận hành được ẩn danh trước khi đẩy lên Cloud.
3. **HQ On-Premise:** Keycloak IAM, PII DB mã hóa AES-256. Dữ liệu PII không bao giờ rời khỏi HQ.

---
<!-- Người 7 -->
## 14. Yêu cầu Kỹ thuật Trọng yếu
- **Hiệu năng (Performance):** 
  - API Gateway gánh 2.000 concurrent connections.
  - Thời gian phản hồi API (P95) $\le$ 200ms.
- **Độ sẵn sàng (HA/DR):**
  - K8s Cloud: Multi-zone Active-Active, Failover $\le$ 60s.
  - Edge: Cache cục bộ chứa được 48 giờ giao dịch mất mạng.
- **Bảo mật:** SSO bắt buộc MFA, 100% kết nối truyền tải qua TLS 1.2+.

---
<!-- Người 8 -->
## 15. Dự toán Ngân sách (CAPEX & OPEX)
- **Chi phí đầu tư ban đầu (CAPEX):**
  - Phần cứng: ~565 triệu (Edge Server, Server HQ, Firewall).
  - Triển khai & Nhân sự: ~632 triệu.
  - Cloud Dev: ~112 triệu.
  - **Tổng CAPEX:** 1.308.800.000 VNĐ.
- **Chi phí vận hành (OPEX):** 1.123.400.000 VNĐ/năm.
- **Dự phòng rủi ro:** 243.220.000 VNĐ.
- **TCO (Tổng sở hữu 3 năm):** 5.209.160.000 VNĐ.

---
<!-- Người 8 -->
## 16. Phân tích Hiệu quả Đầu tư (ROI)
- **TCO / Doanh thu:** Chiếm ~1,45% doanh thu chuỗi (Mức rất lý tưởng).
- **Lợi ích quy đổi hàng năm: ~1.955.000.000 VNĐ**
  - Tiết kiệm 2.500h làm báo cáo (125tr).
  - Giảm sai lệch đối soát (700tr).
  - Chống gián đoạn downtime (400tr).
- **Dòng tiền ròng:** ~831 triệu VNĐ/năm.
- **Thời gian hoàn vốn (Payback):** Khoảng 1,73 năm.
*(Chưa tính giá trị tránh rủi ro phạt 5% doanh thu).*

---
<!-- Người 9 -->
## 17. Lộ trình Triển khai (16 Tuần)
Chia làm 5 Pha (Gối đầu liên tục):
- **Pha 1 (Tuần 1-3):** Foundation (VPN, SSO, Firewall, Monitoring).
- **Pha 2 (Tuần 3-6):** Core (K8s, Kafka, Backup).
- **Pha 3 (Tuần 6-9):** Security & Integration (Tích hợp API, CDC, Mã hóa).
- **Pha 4 (Tuần 9-13):** Migration & Pilot tại 5 chi nhánh.
- **Pha 5 (Tuần 13-16):** Rollout toàn bộ 34 CN & Bàn giao.

---
<!-- Người 9 -->
## 18. Quản trị Rủi ro
| Rủi ro chính | Mức độ | Biện pháp giảm thiểu |
|---|---|---|
| Chậm tích hợp do 8 phần mềm khác vendor | Rất Cao | Pilot sớm; Dùng Adapter Pattern hoặc đọc thẳng Database Read-only. |
| AI chưa đạt độ chuẩn xác (Đề tài TH) | Cao | Go-live nền tảng hạ tầng trước, AI Beta. |
| Sự cố phần cứng diện rộng khi Rollout | Trung bình | Dự phòng Edge thay thế nóng (≤30 phút). |

---
<!-- Người 9 -->
## 19. Kết luận & Chuyển giao
- **Chuyển giao:** Bàn giao tài liệu thiết kế (LLD), mã nguồn (IaC). Đào tạo 3 buổi cho IT, 2 buổi cho Admin chi nhánh.
- **Kết luận:**
  - Dự án không chỉ giải quyết bài toán vận hành mà là "tấm khiên" pháp lý cho Ways Station.
  - Kiến trúc Hybrid Cloud vừa đảm bảo tính liên tục (Offline) vừa sẵn sàng nhân bản nhanh chóng khi chuỗi tiếp tục mở rộng.

---
# XIN CẢM ƠN THẦY CÔ VÀ CÁC BẠN ĐÃ LẮNG NGHE!
**Q&A - Hỏi Đáp**

