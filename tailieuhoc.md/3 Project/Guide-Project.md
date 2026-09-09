# CƠ SỞ HẠ TẦNG CÔNG NGHỆ THÔNG TIN - HƯỚNG DẪN ĐỒ ÁN MÔN HỌC

**Biên soạn:** ThS. Nguyễn Thị Anh Thư  
**Email:** thunta@uit.edu.vn  
**Yêu cầu sản phẩm:** Đề xuất dự án đầu tư cơ sở hạ tầng CNTT cho doanh nghiệp (Báo cáo).  
**Yêu cầu thuyết trình:** Slides báo cáo và video báo cáo.  

---

## Bước 0 — Xác định phạm vi đề xuất (đầu tư cái gì?)

**Mục tiêu:** Tránh đề xuất “mua thiết bị” rời rạc, chuyển sang “đầu tư năng lực hạ tầng”.

### 1. Khảo sát tổng quan về cơ quan / doanh nghiệp (cung cấp tài liệu minh chứng)
*   Lịch sử phát triển.
*   Quy mô và phạm vi hoạt động.
*   Cơ cấu tổ chức và các quy trình hoạt động.

### 2. Chọn 1 hoặc kết hợp các nhóm năng lực
1.  **Compute / Storage / Network:** Server, SAN/NAS, switch/router, Wi-Fi, SD-WAN, đường truyền.
2.  **Nền tảng vận hành (Ops Platform):** Monitoring/observability, ITSM, CMDB, backup, DR, patching, capacity, FinOps.
3.  **Bảo mật & danh tính (Security + Identity):** IAM/SSO/MFA, PAM, EDR/XDR, SIEM/SOC, WAF, DLP, mã hóa, phân loại dữ liệu.
4.  **Nền tảng ứng dụng & tích hợp:** Virtualization, container/K8s, API gateway, message queue, CI/CD.
5.  **Nền tảng dữ liệu:** Lakehouse/DWH, ETL/ELT, data governance, data quality, catalog.

> **Sản phẩm đầu ra bước 0:** “Project scope one-pager” (1 trang) nêu rõ đầu tư năng lực nào, cho đối tượng nào (nhân viên / phòng ban / quy trình hoạt động), trong bao lâu.

---

## Bước 1 — Khảo sát hiện trạng hạ tầng (AS-IS) có số liệu

**Mục tiêu:** Thuyết phục bằng dữ liệu, không bằng cảm tính.

### 1. Thu thập theo 5 lớp
*   **Tính toán & kết nối:** CPU/RAM utilization, tuổi đời thiết bị, băng thông, độ trễ, topology, single point of failure (SPOF).
*   **Ops:** Có/không monitoring, thời gian phát hiện sự cố (MTTD), thời gian khôi phục (MTTR), backup coverage, DR hiện hữu.
*   **Security + Identity:** MFA/SSO, EDR, log tập trung, phân quyền, tình trạng vá lỗi, đánh giá lỗ hổng.
*   **Ứng dụng & tích hợp:** Mức độ ảo hóa/container, CI/CD, API, phụ thuộc hệ thống.
*   **Dữ liệu:** Nơi lưu trữ, phân quyền, sao lưu, chất lượng dữ liệu, truy vết.

### 2. Chỉ số nên có (tối thiểu)
*   SLA/uptime hiện tại; số sự cố/3–6 tháng; MTTR/MTTD.
*   Tỉ lệ backup thành công; RPO/RTO hiện tại.
*   Tỉ lệ thiết bị end-of-support; số lỗ hổng critical chưa vá.
*   Tăng trưởng người dùng/dữ liệu trong 12–24 tháng.

> **Sản phẩm đầu ra bước 1:** Báo cáo AS-IS + Sơ đồ kiến trúc hiện tại + “Pain points” có định lượng.

---

## Bước 2 — Nêu vấn đề & rủi ro nếu không đầu tư (Why now?)

**Mục tiêu:** Chuyển từ “đề nghị mua” sang “giảm rủi ro & tăng năng lực”.

### Viết theo 3 cụm tác động chính:
1.  **Tác động vận hành:** Downtime, nghẽn hiệu năng, mất dữ liệu, gián đoạn sản xuất/bán hàng.
2.  **Tác động tuân thủ & an ninh:** Rò rỉ dữ liệu, không đáp ứng yêu cầu audit/khách hàng.
3.  **Tác động chiến lược:** Không mở rộng được chi nhánh/kênh số, tích hợp chậm.

> **Khuyến nghị trình bày:** Đưa 1 bảng “Rủi ro – Khả năng – Ảnh hưởng – Chi phí ước tính – Biện pháp”.

---

## Bước 3 — Xác lập mục tiêu & KPI hạ tầng (TO-BE)

**Mục tiêu:** KPI phải đo được và gắn liền với vận hành.

### Ví dụ KPI chuẩn:
*   **Sẵn sàng:** Uptime $\ge$ 99.9% (hoặc theo hệ thống trọng yếu).
*   **Khôi phục:** RPO $\le$ X giờ; RTO $\le$ Y giờ.
*   **Hiệu năng:** Response time < Z ms cho nghiệp vụ A; băng thông tối thiểu.
*   **Bảo mật:** 100% endpoint có EDR; MFA cho tài khoản đặc quyền; log tập trung $\ge$ N ngày.
*   **Vận hành:**
    *   MTTD (*Mean Time To Detect* = thời gian trung bình để phát hiện một sự cố) giảm 50%.
    *   MTTR (*Mean Time To Repair/Restore/Recover* = thời gian trung bình để khắc phục và đưa dịch vụ trở lại bình thường) giảm 30%.
    *   90% ticket xử lý theo SLA (*Service Level Agreement* = thỏa thuận mức dịch vụ).

> **Sản phẩm đầu ra bước 3:** Bảng KPI + Baseline hiện tại + Target + Thời điểm đo (sau go-live 1/3/6 tháng).

---

## Bước 4 — Xây dựng phương án kiến trúc TO-BE (2–3 lựa chọn)

**Mục tiêu:** Cho lãnh đạo thấy có sự so sánh, lựa chọn; không “đóng khung” vào một phương án duy nhất.

### 1. Chuẩn bị 3 kịch bản kiến trúc:
1.  **On-prem nâng cấp:** CAPEX cao, kiểm soát tốt.
2.  **Hybrid:** Tối ưu chi phí, linh hoạt, phổ biến.
3.  **Cloud-first:** OPEX, mở rộng nhanh, yêu cầu governance tốt.

### 2. Mỗi kịch bản cần mô tả:
*   Kiến trúc 5 lớp (compute/network/ops/security/app/data).
*   Điểm HA/DR: Active-active / active-standby, backup immutability.
*   Tích hợp: SSO, log, monitoring, ITSM.
*   Khả năng mở rộng: Theo người dùng / dữ liệu / chi nhánh.

> **Sản phẩm đầu ra bước 4:** Sơ đồ TO-BE + So sánh ưu/nhược/chi phí/rủi ro giữa các phương án.

---

## Bước 5 — Chuẩn hoá yêu cầu kỹ thuật (Technical Requirements)

**Mục tiêu:** Yêu cầu đủ chi tiết, rõ ràng để chào thầu / mua sắm và nghiệm thu.

### Chia 4 nhóm yêu cầu:
1.  **Hiệu năng & dung lượng:** Sizing CPU/RAM/Storage, IOPS, bandwidth, concurrent users.
2.  **HA/DR:** RPO/RTO, số site, diễn tập DR, backup retention.
3.  **Security:** IAM/MFA/PAM, EDR, SIEM, WAF, DLP, encryption at rest / in transit.
4.  **Ops:** Monitoring, alerting, log, CMDB, patching, capacity, runbook.

> **Sản phẩm đầu ra bước 5:** Bộ “Yêu cầu kỹ thuật” + Tiêu chí nghiệm thu tương ứng.

---

## Bước 6 — Lập danh mục hạng mục đầu tư (BOM/BoQ ở mức đề xuất)

**Mục tiêu:** Tách rõ phần cứng mua sắm, phần mềm bản quyền và dịch vụ triển khai.

### Gợi ý cấu trúc danh mục:
*   **Thiết bị / Phần cứng:** Server, storage, switch, firewall, UPS, rack…
*   **Phần mềm bản quyền:** Hypervisor, backup, monitoring, EDR, SIEM…
*   **Dịch vụ:** Thiết kế, triển khai, migrate, hardening, đào tạo, vận hành chuyển giao.
*   **Chi phí hạ tầng định kỳ:** Đường truyền, cloud, support, bảo trì.

> **Sản phẩm đầu ra bước 6:** Bảng danh mục + Số lượng + Giả định sizing + Phạm vi dịch vụ.

---

## Bước 7 — Dự toán chi phí & phân tích tài chính (CAPEX/OPEX + TCO)

**Mục tiêu:** Nói chuyện trên phương diện “tổng chi phí sở hữu” (TCO), không chỉ đơn thuần là giá mua ban đầu.

### Bảng cần có:
*   **CAPEX:** Mua sắm ban đầu + triển khai.
*   **OPEX:** Bảo trì, support, license renewal, cloud, đường truyền, nhân sự vận hành.
*   **TCO 3–5 năm:** Tổng CAPEX + OPEX trong vòng đời 3–5 năm.
*   **Lợi ích quy đổi:** Giảm downtime, giảm rủi ro mất dữ liệu, giảm giờ công vận hành.

### Thuyết phục nâng cao (nếu cần):
*   Tính toán ROI / Payback period (ước lượng hợp lý).
*   So sánh bảng TCO giữa 3 kịch bản (On-prem / Hybrid / Cloud).

---

## Bước 8 — Kế hoạch triển khai theo giai đoạn (Roadmap)

**Mục tiêu:** Giảm thiểu rủi ro thông qua “triển khai có kiểm soát”.

### Khuyến nghị chia 5 pha:
1.  **Foundation:** Mạng, phân đoạn mạng (segmentation), baseline security, monitoring/log.
2.  **Core:** Compute/storage, HA, backup/DR.
3.  **Security uplift:** EDR, SIEM, PAM, WAF/DLP (tùy theo ưu tiên).
4.  **Migration:** Chuyển dịch workload theo thứ tự ưu tiên nghiệp vụ.
5.  **Optimize:** Capacity, FinOps, hardening, hoàn thiện SOP/runbook.

> **Mỗi pha bao gồm:** Deliverables (sản phẩm bàn giao), thời lượng, quan hệ phụ thuộc, tiêu chí hoàn thành.

---

## Bước 9 — Quản trị rủi ro, thay đổi & đảm bảo chất lượng

**Mục tiêu:** Chứng minh dự án được quản trị an toàn và kiểm soát được rủi ro phát sinh.

### Bắt buộc nên có:
*   **Risk register:** Rủi ro kỹ thuật, vendor, downtime khi migrate, thiếu nhân sự, thay đổi phạm vi (scope creep).
*   **Change management:** Truyền thông nội bộ, lịch cắt chuyển (cut-over), kế hoạch rollback khi có sự cố.
*   **QA/Acceptance:** Test hiệu năng, test failover, test restore backup, security test (vulnerability scan / pentest nếu có).

---

## Bước 10 — Tổ chức dự án & cơ chế phối hợp (RACI)

**Mục tiêu:** Phân định rõ ràng ai là người quyết định, ai thực hiện, ai tham vấn và ai phê duyệt.

### Vai trò tối thiểu:
*   **Sponsor / Steering Committee** (Ban chỉ đạo dự án)
*   **PM** (Quản lý dự án)
*   **Infra Lead / Security Lead / App Owner / Data Owner**
*   **Vendor PM / Engineer**
*   **Key users** (nếu có thay đổi quy trình vận hành)

> **Sản phẩm đầu ra bước 10:** Bảng ma trận RACI + Lịch họp định kỳ + Quy trình quản lý Issue / Change Request.

---

## Bước 11 — Phương án mua sắm / chọn nhà thầu

**Tùy theo quy định của doanh nghiệp, tối thiểu cần:**
*   **Hình thức:** Chào giá cạnh tranh / Đấu thầu / Chỉ định thầu (nếu có lý do chính đáng).
*   **Bộ tiêu chí chấm:** Kỹ thuật (chiếm 60–70%), Tài chính (chiếm 30–40%).
*   **Yêu cầu ràng buộc:** Cam kết SLA, bảo hành, hỗ trợ kỹ thuật, điều khoản phạt vi phạm, cam kết bảo mật thông tin (NDA).

---

## Bước 12 — Kế hoạch nghiệm thu, vận hành & chuyển giao

**Mục tiêu:** Đảm bảo hệ thống “đưa vào vận hành thực tế được”, không chỉ dừng lại ở mức “lắp đặt xong”.

### 1. Nghiệm thu theo từng lớp:
*   **Kỹ thuật:** Throughput, latency, HA failover, restore backup, kịch bản diễn tập DR (DR drill).
*   **Bảo mật:** MFA, logging, policy tuân thủ, checklist hardening.
*   **Vận hành:** Dashboard giám sát, cảnh báo (alert), runbook xử lý sự cố, quy trình ITSM, bàn giao toàn bộ tài khoản và tài liệu kỹ thuật.

### 2. Chuyển giao:
*   Tài liệu kiến trúc, tài liệu cấu hình chi tiết, SOP / Runbook vận hành, chương trình đào tạo chuyển giao, danh sách tài sản (Asset list), cập nhật CMDB.

---

## Mẫu mục lục đề xuất dự án đầu tư hạ tầng CNTT

1.  **Tóm tắt điều hành (Executive Summary)**
2.  **Hiện trạng AS-IS & vấn đề**
3.  **Mục tiêu & KPI TO-BE**
4.  **Phạm vi & giả định / ràng buộc**
5.  **Các phương án kiến trúc (On-prem / Hybrid / Cloud) + so sánh**
6.  **Yêu cầu kỹ thuật (HA / DR / Security / Ops / Performance)**
7.  **Danh mục hạng mục đầu tư (thiết bị / bản quyền / dịch vụ)**
8.  **Dự toán CAPEX / OPEX & TCO 3–5 năm**
9.  **Kế hoạch triển khai (Roadmap / WBS)**
10. **Rủi ro & kế hoạch kiểm soát**
11. **Tổ chức dự án & RACI**
12. **Mua sắm / chọn nhà thầu**
13. **Nghiệm thu – vận hành – chuyển giao**

*Phụ lục: Sơ đồ AS-IS / TO-BE, tài liệu sizing, checklist hardening, test plan.*
