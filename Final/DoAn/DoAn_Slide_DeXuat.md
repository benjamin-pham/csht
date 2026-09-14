# Cấu trúc Slide Thuyết Trình Đồ Án Đầu Tư Cơ Sở Hạ Tầng CNTT

Bản đề xuất này gồm 13 Slide chắt lọc những nội dung quan trọng nhất từ bản báo cáo `DoAn_Final.md`. Mỗi slide có hướng dẫn chi tiết về nội dung (Text) và hình ảnh (Visual) cần đưa vào.

---

## Slide 1: Tiêu đề
*   **Tiêu đề:** ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT
*   **Phụ đề:** Đầu tư nền tảng tích hợp ứng dụng & Nền tảng dữ liệu tập trung 
*   **Đơn vị thụ hưởng:** Chuỗi Ways Station
*   **Nhóm thực hiện:** [Tên Nhóm / Tên Sinh viên]
*   **Visual:** Logo Ways Station (nếu có) hoặc một hình ảnh minh họa về hệ thống công nghệ hiện đại.

## Slide 2: Tóm tắt điều hành (Executive Summary)
*   **Vấn đề:** 34+ chi nhánh đối mặt với tình trạng đứt gãy tích hợp, phân mảnh dữ liệu và rủi ro rò rỉ dữ liệu (PII).
*   **Giải pháp:** Đầu tư Nền tảng tích hợp (Lớp 4) và Nền tảng dữ liệu (Lớp 5) với kiến trúc **Hybrid Cloud**.
*   **Ngân sách:** CAPEX ~ 1.3 tỷ VNĐ | TCO 3 năm ~ 5.2 tỷ VNĐ.
*   **Lợi ích:** Tiết kiệm 2.500 giờ công/năm, Uptime 99.99%, hoàn vốn trong 2.75 năm.
*   **Visual:** Các con số nổi bật được thiết kế dạng Infographic (1.3 tỷ, 99.99%, 2.75 năm).

## Slide 3: Hiện trạng & Điểm nghẽn (AS-IS)
*   **Vận hành:** 8 hệ thống rời rạc, tích hợp thủ công 100% qua Zalo/Tổng đài/Giấy.
*   **Dữ liệu:** Báo cáo thủ công (2.500h/năm), trễ 24-48 giờ, sai lệch doanh thu 3.8%.
*   **Bảo mật:** Lưu trữ dữ liệu khách hàng (FaceID, CCCD) trên điện thoại nhân viên (0% mã hóa). Sao lưu tỷ lệ thành công chỉ 47%.
*   **Visual:** Sơ đồ minh họa hệ thống rối rắm, mũi tên chỉ sự thủ công giữa các điểm bán và tổng đài.

## Slide 4: Tại sao phải đầu tư ngay? (WHY NOW?)
*   **Rủi ro Vận hành:** Gián đoạn kinh doanh giờ cao điểm, tốn thời gian xử lý sự cố.
*   **Rủi ro Chiến lược:** Chậm ra quyết định, lãng phí nguyên vật liệu, không bán chéo được dịch vụ do thiếu định danh chung.
*   **Rủi ro Tuân thủ (Nghiêm trọng):** Vi phạm Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân (PII), có thể bị phạt tới 5% tổng doanh thu.
*   **Visual:** Icon cảnh báo rủi ro (Warning icons) cho 3 khía cạnh: Vận hành, Chiến lược, Pháp lý.

## Slide 5: Mục tiêu & KPI kỹ thuật (TO-BE)
*   **Tính sẵn sàng:** Uptime $\ge$ 99.99% | MTTR $\le$ 30 phút.
*   **Chất lượng dữ liệu:** Trễ dữ liệu $\le$ 5s | Sai số dự báo AI (MAPE) < 15%.
*   **Bảo mật & DR:** Mã hóa PII 100% | RPO $\le$ 15 phút.
*   **Visual:** Bảng ma trận đối chiếu ngắn gọn: Vấn đề $\rightarrow$ Mục tiêu $\rightarrow$ KPI hoặc dạng biểu đồ mạng nhện.

## Slide 6: Lựa chọn Kiến trúc (Phân tích phương án)
*   **Các phương án:** On-Premise 100% vs. Cloud-Native 100% vs. **Hybrid Cloud (Chọn)**
*   **Lý do chọn Hybrid Cloud:**
    *   Đáp ứng khả năng tiếp tục bán hàng ngoại tuyến khi rớt mạng chi nhánh (Khắc phục điểm yếu của thuần Cloud).
    *   Tận dụng sức mạnh điện toán vô hạn của Cloud để phân tích dữ liệu, Auto-scaling.
    *   Lưu trữ dữ liệu nhạy cảm PII tại On-Premise để tuân thủ luật pháp.
*   **Visual:** Bảng so sánh tick checkmark ($\checkmark$) làm nổi bật Hybrid Cloud đạt 6/6 tiêu chí.

## Slide 7: Tổng quan Kiến trúc Đề xuất
*   **Lớp 4 (Tích hợp):** API Gateway & Kafka trên Cloud. Edge Cluster (K3s) tại 34 chi nhánh (Store-and-Forward khi mất mạng).
*   **Lớp 5 (Dữ liệu):** Data Lakehouse trên Cloud, xử lý Streaming Data (CDC) real-time.
*   **Bảo mật:** Zero Trust, IAM/SSO tập trung tại HQ, ẩn danh dữ liệu trước khi lên Cloud.
*   **Visual:** Sơ đồ High-Level Architecture (Rất quan trọng): Thể hiện 3 khối Cloud, HQ (On-Prem), và Edge (Các chi nhánh).

## Slide 8: Năng lực Vận hành & Bảo mật
*   **HA/DR:** Multi-zone Active-Active, Auto-failover $\le$ 60s, Immutable backup.
*   **Bảo mật:** SSO/IAM (Keycloak), mã hóa AES-256 (at-rest) và TLS 1.2+ (in-transit).
*   **Monitoring (Ops):** Prometheus + Grafana giám sát toàn hệ thống, tự động alert. CI/CD tự động hóa.
*   **Visual:** Các logo công nghệ (Kubernetes, Kafka, PostgreSQL, Grafana, Terraform).

## Slide 9: Kế hoạch Triển khai (Roadmap 5 pha)
*   **Thời gian tổng:** 16 tuần (4 tháng).
*   **Pha 1 (T1-T3):** Foundation (Mạng, Bảo mật nền, Monitoring).
*   **Pha 2 (T3-T6):** Core (K8s, DB, HA, Data Storage).
*   **Pha 3 (T6-T9):** Security Uplift (SSO, CDC, API Gateway).
*   **Pha 4 (T9-T13):** Migrate dữ liệu, Triển khai AI & Pilot 5 chi nhánh.
*   **Pha 5 (T13-T16):** Rollout 29 chi nhánh còn lại & Chuyển giao.
*   **Visual:** Biểu đồ Gantt hoặc Timeline (Lộ trình mũi tên) hiển thị 5 mốc Milestone chính.

## Slide 10: Dự toán Đầu tư (CAPEX)
*   **Tổng mức đầu tư ban đầu:** 1.308.800.000 VNĐ.
    *   Phần cứng (Edge Servers, HQ Servers...): ~43%
    *   Dịch vụ triển khai & Nhân sự: ~48%
    *   Hạ tầng Cloud (trong kỳ triển khai): ~9%
*   **Chiến lược tối ưu:** Sử dụng tối đa công nghệ mã nguồn mở (Open-source) như K3s, Kafka, PostgreSQL, Keycloak để không tốn phí License phần mềm.
*   **Visual:** Biểu đồ tròn (Pie chart) phân bổ tỷ trọng cấu thành CAPEX.

## Slide 11: TCO & Hiệu quả Đầu tư (Cost-Benefit)
*   **TCO (Tổng chi phí sở hữu 3 năm):** ~5.2 tỷ VNĐ (Bao gồm CAPEX, OPEX và Dự phòng).
*   **Lợi ích quy đổi (hàng năm):** ~475.000.000 VNĐ.
    *   Tiết kiệm giờ công làm báo cáo.
    *   Giảm sai lệch và thất thoát doanh thu.
    *   Tránh thiệt hại do downtime và rủi ro phạt NĐ13.
*   **Thời gian hoàn vốn (Payback Period):** ~2.75 năm.
*   **Visual:** Biểu đồ cột chồng (Stacked bar chart) thể hiện TCO phân bổ qua Năm 1, Năm 2, Năm 3.

## Slide 12: Tổ chức Dự án & Mua sắm
*   **Tổ chức & RACI:** Có sự phân quyền rõ ràng giữa PM, Tech Leads, Nhà thầu và Admin chi nhánh. Quản trị qua hệ thống Jira.
*   **Lựa chọn nhà thầu:** Đấu thầu / Chào giá cạnh tranh (RFP). Trọng số 70% Kỹ thuật - 30% Tài chính.
*   **Yêu cầu Hợp đồng:** Ràng buộc chặt chẽ NDA (Bảo mật dữ liệu) và cam kết SLA hỗ trợ 12 tháng.
*   **Visual:** Ma trận RACI thu nhỏ hoặc icon thể hiện quy trình chọn thầu khắt khe.

## Slide 13: Lộ trình Nghiệm thu & Chuyển giao
*   **Nghiệm thu thực tế:** Load Test (2000 users), Failover Test (Offline chi nhánh 4h), Diễn tập DR.
*   **Chuyển giao:** Tài liệu HLD/LLD, 10+ Runbook/SOP vận hành.
*   **Đào tạo:** IT nội bộ (3 buổi Kỹ thuật chuyên sâu) + Admin chi nhánh (2 buổi).
*   **Visual:** Hình ảnh mũi tên hướng tới đích "GO-LIVE Thành công".

---
*Ghi chú: Khi chuẩn bị thuyết trình, bạn có thể tập trung nói nhiều hơn vào Slide 4 (Tại sao cần đầu tư) và Slide 6, 7 (Lý do chọn Hybrid Cloud). Đây là những điểm "ăn tiền" nhất đối với Hội đồng / Ban Giám đốc.*

