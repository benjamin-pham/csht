# CƠ SỞ HẠ TẦNG CÔNG NGHỆ THÔNG TIN - HƯỚNG DẪN THỰC HÀNH

**Biên soạn:** ThS. Nguyễn Thị Anh Thư
**Email:** thunta@uit.edu.vn

**Yêu cầu sản phẩm:** Thuyết minh đề tài xây dựng hệ thống phần mềm cho doanh nghiệp.
**Yêu cầu thuyết trình:** Slides báo cáo và video báo cáo.

---

## Bước 0 — Chuẩn bị đầu vào (đừng viết ngay)

**Mục tiêu:** gom đủ thông tin để thuyết minh “đúng vấn đề – đúng phạm vi – đúng chi phí – đúng hiệu quả”.

**Thu thập tối thiểu:**
*   **Bối cảnh DN:** ngành, quy mô, cơ cấu phòng ban, quy trình nghiệp vụ chính.
*   **Vấn đề hiện tại:** điểm nghẽn vận hành, rủi ro, chi phí ẩn, dữ liệu rời rạc.
*   **Đối tượng sử dụng:** nhóm người dùng, vai trò, mức độ số hóa hiện tại.
*   **Hệ thống liên quan:** ERP/CRM/Kế toán/HRM/Email/SSO, các API/DB đang có.
*   **Ràng buộc:** ngân sách, thời gian, tuân thủ (ISO, SOC2, NĐ 13/2023…), hạ tầng (on-prem/cloud).

## Bước 1 — Viết Tên đề tài + Thông tin chung

**Viết sao cho “đúng định danh” và đo được.**

*   **Tên đề tài:** *Động từ + đối tượng + phạm vi + bối cảnh*
    *   Ví dụ: “Xây dựng hệ thống quản lý đơn hàng & tồn kho đa kênh cho DN bán lẻ X”.
*   **Thông tin chung:** đơn vị chủ trì, đơn vị phối hợp, chủ nhiệm, thời gian, địa điểm triển khai.

**Checklist:**
*   Tên không mơ hồ (“nâng cấp”, “cải tiến” phải nêu nâng cấp cái gì).
*   Có phạm vi nghiệp vụ rõ (đơn hàng/tồn kho/CSKH…).

## Bước 2 — Bối cảnh & Lý do chọn đề tài (Business Case)

**Mục tiêu:** chứng minh “phải làm” và “làm bây giờ”.

**Nội dung nên có:**
*   **Hiện trạng (AS-IS):** mô tả quy trình hiện tại, công cụ đang dùng (Excel, Zalo, phần mềm rời rạc).
*   **Vấn đề/điểm đau:** sai lệch dữ liệu, trễ xử lý, thất thoát, không truy vết, phụ thuộc cá nhân.
*   **Tác động định lượng (càng tốt):**
    *   thời gian xử lý/đơn, tỉ lệ lỗi, tồn kho lệch, chi phí nhân sự, doanh thu thất thoát…
*   **Nguyên nhân gốc (root cause):** thiếu chuẩn dữ liệu, thiếu workflow, không tích hợp, phân quyền yếu…

## Bước 3 — Mục tiêu, KPI và tiêu chí thành công

**Chia 2 lớp:**

### 3.1 Mục tiêu tổng quát
1–2 câu, gắn với chiến lược DN (tăng năng suất, kiểm soát rủi ro, mở rộng vận hành).

### 3.2 Mục tiêu cụ thể (SMART)
Ví dụ:
*   Giảm **30%** thời gian xử lý đơn hàng trong **3 tháng** sau go-live.
*   Giảm chênh lệch tồn kho xuống **<2%**.
*   100% giao dịch có log truy vết, phân quyền theo vai trò.

**Checklist KPI:**
*   Có baseline hiện tại + target tương lai.
*   Có thời điểm đo (sau go-live 1/3/6 tháng).
*   Có “owner” chịu trách nhiệm số liệu.

## Bước 4 — Đối tượng, phạm vi và giả định/ràng buộc

### 4.1 Đối tượng áp dụng
Phòng ban, chi nhánh, nhóm người dùng (Admin/Manager/Staff/Partner…).

### 4.2 Phạm vi (Scope)
Tách rõ:
*   **In-scope:** module chức năng, báo cáo, tích hợp, dữ liệu chuyển đổi.
*   **Out-of-scope:** những phần chưa làm kỳ này (để tránh “scope creep”).

### 4.3 Giả định & ràng buộc
*   Hạ tầng (cloud/on-prem), ngân sách, timeline, tiêu chuẩn bảo mật, nhân sự DN tham gia.

## Bước 5 — Yêu cầu nghiệp vụ và yêu cầu hệ thống

### 5.1 Yêu cầu nghiệp vụ (BRD level)
Trình bày theo **use case / user story**:
*   Tên nghiệp vụ, tác nhân, luồng chính, ngoại lệ, đầu vào/đầu ra.

### 5.2 Yêu cầu chức năng (FR)
Nhóm theo module:
*   Ví dụ: Quản lý khách hàng, Đơn hàng, Kho, Báo cáo, Phân quyền…

### 5.3 Yêu cầu phi chức năng (NFR)
Bắt buộc phải có:
*   Hiệu năng: số người dùng đồng thời, SLA, thời gian phản hồi.
*   Sẵn sàng: uptime, backup, DR (RPO/RTO).
*   Bảo mật: IAM/SSO/MFA, audit log, mã hóa, phân quyền RBAC.
*   Mở rộng: scale theo chi nhánh/người dùng.
*   Tuân thủ: dữ liệu cá nhân, lưu trữ, nhật ký.

**Checklist:**
*   Có tiêu chí test được cho NFR (con số, ngưỡng).
*   Có ma trận phân quyền (Role → quyền).

## Bước 6 — Thiết kế giải pháp (TO-BE) và kiến trúc tổng thể

### 6.1 Quy trình TO-BE
Vẽ sơ đồ BPMN hoặc flow đơn giản, nêu:
*   bước xử lý, điểm kiểm soát, người phê duyệt, trạng thái.

### 6.2 Kiến trúc hệ thống
Trình bày theo 3 lớp:
*   **Presentation:** Web/Mobile, portal.
*   **Application:** services, workflow engine, API gateway.
*   **Data:** DB, cache, warehouse/lakehouse (nếu có).

### 6.3 Tích hợp
*   Hệ thống nào tích hợp, giao thức (REST, SOAP, MQ), tần suất đồng bộ, mapping dữ liệu.

### 6.4 Thiết kế dữ liệu
*   Mô hình dữ liệu mức khái niệm (ERD high-level).
*   Quy tắc mã hóa danh mục, khóa định danh, chuẩn hóa.

## Bước 7 — Kế hoạch triển khai (WBS) và tiến độ

Chia theo pha chuẩn:
1.  Khảo sát & phân tích (SRS/BRD)
2.  Thiết kế (HLD/LLD)
3.  Phát triển (Dev)
4.  Kiểm thử (SIT/UAT)
5.  Triển khai (Pilot → Rollout)
6.  Vận hành & bảo trì (Hypercare)

Mỗi pha cần:
*   đầu ra (deliverables), thời lượng, người chịu trách nhiệm, tiêu chí hoàn thành.

**Khuyến nghị:** đưa bảng tiến độ theo tuần/tháng + mốc nghiệm thu.

## Bước 8 — Nhân sự, tổ chức dự án, cơ chế phối hợp

### 8.1 Cơ cấu
*   Sponsor / Steering committee / PM / BA / Tech lead / Dev / QA / Sec / Ops / Key users.

### 8.2 RACI
Bảng RACI cho các đầu việc lớn: yêu cầu, duyệt UAT, dữ liệu, hạ tầng, go-live.

### 8.3 Cơ chế làm việc
*   Lịch họp, quy trình xử lý change request, quản lý issue/risk.

## Bước 9 — Dự toán chi phí và phương án tài chính

Tách nhóm chi phí:
*   Phần mềm: license, công cụ, bản quyền.
*   Phát triển: nhân công, outsource.
*   Hạ tầng: server/cloud, domain, SSL, monitoring.
*   Bảo mật & tuân thủ: pentest, audit.
*   Đào tạo & chuyển giao.
*   Vận hành: bảo trì, hỗ trợ, nâng cấp.

**Nên có:** bảng CAPEX/OPEX + giả định đơn giá + phương án dự phòng (contingency 5–15%).

## Bước 10 — Quản trị rủi ro, chất lượng và thay đổi

### 10.1 Rủi ro
Bảng risk register: rủi ro – xác suất – ảnh hưởng – mức – biện pháp – owner.

Rủi ro thường gặp:
*   scope creep, dữ liệu bẩn, tích hợp thất bại, thiếu key user, bảo mật, chậm UAT.

### 10.2 Kế hoạch kiểm thử & đảm bảo chất lượng
*   Test plan, test case, tiêu chí pass/fail, coverage.
*   UAT sign-off.

### 10.3 Quản lý thay đổi (Change Management)
*   Truyền thông nội bộ, đào tạo theo vai trò, tài liệu hướng dẫn, hỗ trợ go-live.

## Bước 11 — Kế hoạch vận hành, bảo trì và chuyển giao

*   Mô hình vận hành: On-call, ticket ITSM, SLA hỗ trợ.
*   Monitoring/Logging, backup, DR drill.
*   Bàn giao: source code, tài liệu, tài khoản, runbook, hướng dẫn triển khai.
*   Lộ trình nâng cấp: roadmap 6–12 tháng.

## Bước 12 — Nghiệm thu, đánh giá hiệu quả sau triển khai

*   Tiêu chí nghiệm thu theo deliverables + KPI.
*   Kế hoạch đo hiệu quả (benefit realization): đo lại KPI sau 1–3–6 tháng.
*   Biên bản nghiệm thu, checklist go-live, checklist an toàn dữ liệu.

---

## Khung mục lục thuyết minh

1.  Thông tin chung & tên đề tài
2.  Bối cảnh – hiện trạng – vấn đề
3.  Mục tiêu & KPI
4.  Đối tượng áp dụng, phạm vi, giả định/ràng buộc
5.  Yêu cầu nghiệp vụ & yêu cầu hệ thống (FR/NFR)
6.  Giải pháp đề xuất & kiến trúc (TO-BE, tích hợp, dữ liệu)
7.  Kế hoạch triển khai & tiến độ (WBS)
8.  Tổ chức nhân sự & cơ chế phối hợp (RACI)
9.  Dự toán chi phí & phương án tài chính
10. Rủi ro, chất lượng, kiểm thử, quản lý thay đổi
11. Vận hành – bảo trì – chuyển giao
12. Nghiệm thu & đánh giá hiệu quả

*Phụ lục: sơ đồ quy trình, mockup, ERD, ma trận phân quyền, danh mục thuật ngữ*
