# Giải Thích Các Thuật Ngữ Kỹ Thuật & Nghiệp Vụ Trong Đồ Án Đầu Tư Cơ Sở Hạ Tầng CNTT
*(Đính kèm theo đồ án: DoAn_Final_v2.md)*

Dưới đây là danh sách giải thích các thuật ngữ chuyên môn được sử dụng trong tài liệu đề xuất đầu tư, phân nhóm theo từng lĩnh vực để người đọc (đặc biệt là Ban Giám đốc và các bên không chuyên sâu về kỹ thuật) dễ dàng tra cứu và nắm bắt.

## 1. Nhóm Tài chính & Quản lý dự án
*   **CAPEX (Capital Expenditure):** Chi phí đầu tư ban đầu. Bao gồm tiền mua sắm phần cứng, bản quyền phần mềm, phí dịch vụ triển khai hệ thống.
*   **OPEX (Operational Expenditure):** Chi phí vận hành định kỳ. Bao gồm chi phí thuê tài nguyên đám mây (Cloud), đường truyền Internet, nhân sự bảo trì, và gia hạn bản quyền hàng năm.
*   **TCO (Total Cost of Ownership):** Tổng chi phí sở hữu. Bằng tổng của CAPEX và toàn bộ OPEX trong một vòng đời dự án nhất định (trong tài liệu này là chu kỳ 3 năm).
*   **AS-IS:** Hiện trạng. Tình trạng thực tế của hệ thống và quy trình trước khi có bất kỳ sự can thiệp hay thay đổi nào từ dự án.
*   **TO-BE:** Trạng thái mục tiêu. Viễn cảnh hệ thống và quy trình kiến trúc sau khi dự án được triển khai hoàn tất.
*   **SOP (Standard Operating Procedure):** Quy trình thao tác chuẩn. Bộ tài liệu hướng dẫn chi tiết các bước vận hành nghiệp vụ hàng ngày.
*   **KPI (Key Performance Indicator):** Chỉ số đánh giá hiệu quả hoạt động chính. Các thông số đo lường mức độ đạt được mục tiêu của dự án.
*   **SPOF (Single Point of Failure):** Điểm lỗi duy nhất. Một thành phần trong hệ thống mà nếu nó hỏng, toàn bộ hệ thống sẽ ngừng hoạt động. Mục tiêu của kiến trúc là loại bỏ SPOF.

## 2. Nhóm Kiến trúc & Hạ tầng Cloud
*   **On-Premise (Tại chỗ):** Mô hình triển khai mà máy chủ và thiết bị mạng được đặt trực tiếp tại cơ sở của doanh nghiệp (ví dụ: Trụ sở chính - HQ) và do doanh nghiệp tự quản lý.
*   **Cloud-Native / Public Cloud (Điện toán đám mây):** Xây dựng và vận hành hệ thống hoàn toàn trên nền tảng hạ tầng của các nhà cung cấp dịch vụ đám mây (như AWS, Google Cloud, Azure).
*   **Hybrid Cloud (Đám mây lai):** Kiến trúc kết hợp linh hoạt giữa máy chủ tại chỗ (On-Premise / Edge) và hạ tầng điện toán đám mây. Đây là phương án được khuyến nghị trong dự án.
*   **Edge Server / Edge Cluster (Máy chủ biên):** Các máy chủ hoặc cụm máy tính nhỏ đặt tại từng chi nhánh (điểm biên). Giúp xử lý dữ liệu tại chỗ, đảm bảo phần mềm tính tiền vẫn hoạt động bình thường khi mất kết nối Internet.
*   **IaC (Infrastructure as Code):** Cơ sở hạ tầng dưới dạng mã. Phương pháp quản lý và cấu hình hạ tầng mạng, máy chủ bằng các đoạn mã tự động (như Terraform, Ansible) thay vì cấu hình thủ công bằng tay. Tăng tốc độ triển khai và giảm thiểu sai sót.
*   **K8s (Kubernetes):** Nền tảng mã nguồn mở chuyên dùng để tự động hóa việc triển khai, mở rộng và quản lý các ứng dụng container hóa. K8s sử dụng cho cụm máy chủ trên Cloud.
*   **K3s:** Một phiên bản Kubernetes siêu nhẹ, được thiết kế đặc biệt để chạy trên các thiết bị Edge (máy chủ biên tại chi nhánh) với tài nguyên phần cứng giới hạn.
*   **CI/CD (Continuous Integration / Continuous Deployment):** Tích hợp và triển khai liên tục. Hệ thống tự động hóa việc kiểm tra và cập nhật các bản vá phần mềm lên môi trường thực tế mà không gây gián đoạn dịch vụ.

## 3. Nhóm Tích hợp & Dữ liệu
*   **API (Application Programming Interface):** Giao diện lập trình ứng dụng. Cầu nối cho phép các phần mềm hoặc hệ thống độc lập giao tiếp và trao đổi dữ liệu với nhau.
*   **API Gateway:** Cổng API trung tâm. Điểm kiểm soát duy nhất quản lý, định tuyến và bảo vệ mọi luồng kết nối API từ các chi nhánh gửi lên Cloud.
*   **CDC (Change Data Capture):** Bắt dữ liệu thay đổi. Công nghệ theo dõi và thu thập tức thời bất kỳ thay đổi dữ liệu nào tại chi nhánh để đẩy lên kho dữ liệu trung tâm gần như theo thời gian thực.
*   **Data Lakehouse:** Kho dữ liệu hiện đại kết hợp ưu điểm của Data Lake (lưu trữ linh hoạt dữ liệu thô chi phí thấp) và Data Warehouse (cấu trúc hóa để phân tích nhanh).
*   **ETL/ELT (Extract, Transform/Load, Load/Transform):** Quá trình trích xuất, biến đổi và nạp dữ liệu từ các nguồn rời rạc vào kho dữ liệu tập trung để chuẩn bị cho việc báo cáo, phân tích.
*   **Kafka (Message Queue):** Hệ thống hàng đợi thông điệp mạnh mẽ, giúp tiếp nhận và xử lý hàng ngàn luồng dữ liệu giao dịch đồng thời mà không bị nghẽn mạch.
*   **MAPE (Mean Absolute Percentage Error):** Phần trăm sai số tuyệt đối trung bình. Chỉ số dùng để đánh giá mức độ sai số của mô hình Trí tuệ Nhân tạo (AI) trong việc dự báo lưu lượng khách. (MAPE càng thấp càng chính xác).

## 4. Nhóm Bảo mật & Định danh
*   **PII (Personally Identifiable Information):** Thông tin định danh cá nhân. Bao gồm hình ảnh khuôn mặt (Face ID), ảnh căn cước công dân (CCCD), số điện thoại, v.v. Đây là dữ liệu nhạy cảm cần bảo vệ theo Nghị định 13/2023/NĐ-CP.
*   **IAM (Identity and Access Management):** Nền tảng quản lý định danh và quyền truy cập, đảm bảo cấp đúng quyền cho đúng người vào hệ thống.
*   **SSO (Single Sign-On):** Đăng nhập một lần. Công nghệ cho phép nhân viên hoặc khách hàng chỉ cần dùng MỘT tài khoản và mật khẩu duy nhất để truy cập vào tất cả các phần mềm dịch vụ khác nhau trong chuỗi.
*   **MFA (Multi-Factor Authentication):** Xác thực đa yếu tố. Lớp bảo mật bổ sung (như mã OTP gửi qua điện thoại) ngoài việc nhập mật khẩu thông thường.
*   **AES-256 (Advanced Encryption Standard):** Tiêu chuẩn mã hóa dữ liệu cao cấp bằng khóa 256-bit, cực kỳ an toàn để lưu trữ dữ liệu PII tĩnh (at-rest).
*   **TLS (Transport Layer Security):** Giao thức bảo mật mã hóa dữ liệu trên đường truyền (in-transit) giữa chi nhánh và máy chủ để chống nghe lén.
*   **RBAC (Role-Based Access Control):** Kiểm soát truy cập dựa trên vai trò. Việc phân quyền được thực hiện dựa vào chức danh công việc của người đó (VD: Thu ngân chỉ thấy màn hình tính tiền, Quản lý thấy doanh thu).
*   **Zero Trust:** Kiến trúc bảo mật dựa trên nguyên tắc "Không tin cậy ai cả", luôn luôn yêu cầu xác thực và kiểm tra tính hợp lệ trước khi cho phép bất kỳ kết nối nào.

## 5. Nhóm Vận hành, HA & Khôi phục thảm họa (DR)
*   **HA (High Availability):** Tính sẵn sàng cao. Đặc tính của hệ thống được thiết kế để hoạt động liên tục, tự động chuyển đổi sang máy chủ dự phòng ngay lập tức khi máy chủ chính gặp sự cố (Failover).
*   **DR (Disaster Recovery):** Khôi phục thảm họa. Kế hoạch và quy trình khôi phục hệ thống khi xảy ra sự cố nghiêm trọng (như cháy nổ trung tâm dữ liệu, tấn công mạng diện rộng).
*   **Active-Active / Active-Passive:** Các mô hình HA. Active-Active là chạy đồng thời nhiều cụm chia sẻ tải; Active-Passive là một cụm chạy chính, cụm kia ở trạng thái chờ và chỉ bật khi cụm chính chết.
*   **RPO (Recovery Point Objective):** Mục tiêu điểm khôi phục. Mức độ chấp nhận mất mát dữ liệu tối đa. Ví dụ: RPO = 15 phút nghĩa là nếu hệ thống sập, dữ liệu bị mất cao nhất chỉ thuộc 15 phút trước đó.
*   **RTO (Recovery Time Objective):** Mục tiêu thời gian khôi phục. Thời gian tối đa cho phép hệ thống "sập" và phải khôi phục lại hoạt động bình thường (Ví dụ: RTO = 4 giờ).
*   **MTTR (Mean Time To Recovery):** Thời gian khôi phục trung bình. Mất bao lâu để giải quyết triệt để một sự cố phát sinh.
*   **PITR (Point-In-Time Recovery):** Khả năng khôi phục hệ thống và dữ liệu quay ngược chính xác về một thời điểm cụ thể bất kỳ trong quá khứ (thường để khắc phục do con người xóa nhầm dữ liệu).
*   **Store-and-Forward:** Lưu trữ và chuyển tiếp. Cơ chế tại các Edge Server cho phép dữ liệu giao dịch được lưu tạm trên ổ đĩa khi đứt cáp Internet, và tự động đẩy dữ liệu bù lên Cloud ngay khi mạng có lại.

## 6. Giải Thích Các Công Thức Tính Toán
Trong đồ án có sử dụng các công thức để lượng hóa mục tiêu và đánh giá tính khả thi. Dưới đây là phần giải thích chi tiết cho từng công thức:

### 6.1. Các công thức đánh giá năng lực hệ thống (KPI)

**1. Tính sẵn sàng (Availability / Uptime)**
*   *Công thức:* $Uptime = \frac{\text{Total Time} - \text{Downtime}}{\text{Total Time}} \times 100\%$
*   *Giải thích:* 
    *   **Total Time (Tổng thời gian):** Tổng thời gian hoạt động lý thuyết trong một chu kỳ (ví dụ: 1 tháng có 43.200 phút).
    *   **Downtime (Thời gian chết):** Thời gian hệ thống bị gián đoạn, không phục vụ được khách hàng.
    *   *Ý nghĩa:* Tỷ lệ % thời gian hệ thống hoạt động bình thường. Đồ án đặt mục tiêu $\ge 99,99\%$, nghĩa là thời gian chết tối đa chỉ được phép là 4,32 phút/tháng.

**2. Thời gian khôi phục trung bình (MTTR - Mean Time To Recovery)**
*   *Công thức:* $MTTR = \frac{\text{Tổng thời gian gián đoạn (Downtime)}}{\text{Tổng số lượng sự cố}}$
*   *Giải thích:* Lấy tổng thời gian hệ thống ngừng hoạt động chia cho số lần xảy ra sự cố.
*   *Ý nghĩa:* Cho biết trung bình mất bao lâu để bộ phận IT (hoặc hệ thống tự động) khắc phục xong một lỗi. Đồ án yêu cầu $\le 30$ phút.

**3. Độ trễ dữ liệu (Data Freshness)**
*   *Công thức:* $\Delta t_{freshness} = t_{DataLakehouse} - t_{POS} \le 5s$
*   *Giải thích:*
    *   **$t_{POS}$:** Thời điểm giao dịch phát sinh tại phần mềm tính tiền ở chi nhánh.
    *   **$t_{DataLakehouse}$:** Thời điểm giao dịch đó được ghi nhận thành công lên kho dữ liệu đám mây.
    *   *Ý nghĩa:* Chênh lệch giữa 2 mốc thời gian này là độ trễ. Yêu cầu dữ liệu phải xuất hiện trên Cloud không quá 5 giây sau khi giao dịch xảy ra (Thời gian thực).

**4. Chất lượng luồng dữ liệu (Data Completeness / Tính toàn vẹn)**
*   *Công thức:* $\text{Completeness} = \frac{\text{Số bản ghi nạp thành công vào Data Lakehouse}}{\text{Tổng số bản ghi gốc phát sinh tại POS}} \times 100\% \ge 99{,}5\%$
*   *Giải thích:* Tỷ lệ giữa dữ liệu thực tế được đưa lên Cloud so với tổng dữ liệu sinh ra tại chi nhánh.
*   *Ý nghĩa:* Đảm bảo không bị "rớt" hay mất mát dữ liệu trong quá trình truyền tải, tránh việc sai lệch doanh thu khi đối soát.

**5. Tỷ lệ mã hóa dữ liệu (Encryption Coverage)**
*   *Công thức:* $\text{Encryption Coverage} = \frac{\text{Số trường PII được mã hóa AES-256}}{\text{Tổng số trường PII trong hệ thống}} \times 100\%$
*   *Giải thích:* Tỷ lệ dữ liệu cá nhân nhạy cảm (Face ID, CCCD, v.v.) đã được mã hóa bảo mật so với tổng lượng dữ liệu nhạy cảm mà hệ thống lưu giữ.
*   *Ý nghĩa:* Đồ án đặt mục tiêu 100%, nghĩa là tuyệt đối không có dữ liệu cá nhân nào được lưu dưới dạng văn bản có thể đọc trực tiếp (plaintext).

**6. Mục tiêu điểm khôi phục (RPO)**
*   *Công thức:* $RPO = t_{\text{sự cố}} - t_{\text{bản sao lưu gần nhất}} \le 15\ \text{phút}$
*   *Giải thích:* Khoảng thời gian từ lúc hệ thống vừa được sao lưu (backup) xong cho đến khi thảm họa (sập hệ thống) xảy ra.
*   *Ý nghĩa:* Lượng dữ liệu phát sinh trong khoảng thời gian này sẽ bị mất nếu không khôi phục được. Đồ án yêu cầu RPO $\le 15$ phút, nghĩa là dung sai mất dữ liệu tối đa là 15 phút.

### 6.2. Các công thức đánh giá tài chính

**7. Tổng chi phí sở hữu (TCO - 3 năm)**
*   *Công thức:* $\text{TCO}_{3\ \text{năm}} = \text{Tổng CAPEX} + \text{Tổng OPEX (3 năm)} + \text{Dự phòng}$ 
*   *Giải thích:* Tổng số tiền doanh nghiệp phải chi ra không chỉ để xây dựng hệ thống ban đầu (CAPEX) mà còn để duy trì nó hoạt động trơn tru trong 3 năm tiếp theo (OPEX) cộng với quỹ dự phòng rủi ro.

**8. Hoàn vốn (Payback Period)**
*   *Công thức:* $\text{Payback} = \frac{\text{Vốn đầu tư ban đầu}}{\text{Dòng tiền ròng hàng năm}}$
*   *Giải thích:*
    *   **Vốn đầu tư ban đầu:** CAPEX + phần dự phòng cho CAPEX.
    *   **Dòng tiền ròng hàng năm:** Tổng lợi ích quy đổi ra tiền (nhờ tiết kiệm giờ công, giảm hao hụt, tăng doanh thu) trừ đi chi phí vận hành (OPEX) định kỳ của mỗi năm đó.
    *   *Ý nghĩa:* Thời gian cần thiết để khoản tiết kiệm/lợi nhuận sinh ra từ hệ thống bù đắp hoàn toàn số tiền đã đầu tư ban đầu. Ở dự án này là khoảng 1,73 năm (tương đương 21 tháng).
