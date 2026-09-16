# NỘI DUNG SLIDE THUYẾT TRÌNH ĐỒ ÁN MÔN HỌC
**Dự án:** Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station
**Quy mô:** 9 người trình bày
**Thời lượng tối đa:** 45 phút (Mỗi người ~5 phút)

---

## Người 1: Tổng quan dự án & Hiện trạng hệ thống (AS-IS)

**Slide 1: Tiêu đề dự án**
*   **Đồ án:** Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station.
*   **Nhóm thực hiện:** [Tên các thành viên]
*   **Mục tiêu cốt lõi:** Hiện đại hóa hạ tầng, xóa bỏ sự phân mảnh dữ liệu, xây dựng nền tảng vững chắc cho phân tích AI.

**Slide 2: Bối cảnh nghiệp vụ Ways Station**
*   **Quy mô:** 34 chi nhánh hoạt động theo mô hình 34 hộ kinh doanh cá thể riêng biệt.
*   **Mô hình kinh doanh đa dịch vụ:** Gym (24/7), Net/Gaming, Bida, Cầu lông, Hub, F&B.
*   **Đặc thù tác động hạ tầng:**
    *   Tính tiền theo giờ sử dụng (Khách vào/ra liên tục).
    *   Không có nhân sự IT thường trực tại các chi nhánh.

**Slide 3: Sơ đồ kiến trúc hiện trạng (AS-IS)**
*   *(Chèn Sơ đồ kiến trúc AS-IS: 34 chi nhánh rời rạc)*
*   **Hệ thống phân mảnh:** Tồn tại 8 phần mềm hoạt động cô lập và độc lập (POS Net, PM Gym, Kế toán, Kho...).
*   **Tỷ lệ tích hợp hệ thống:** 0% (Không có luồng API tự động).
*   **Giao tiếp thủ công:** 100% trao đổi qua Tổng đài (phím 2/3/8), Zalo cá nhân nhân viên, và Sổ giao ca bằng giấy.

**Slide 4: 3 Rủi ro & Điểm nghẽn kỹ thuật lõi**
*   **1. Đứt gãy tích hợp (Vận hành):** SPOF (Single Point of Failure) tại chi nhánh, mất kết nối mạng là không tính được tiền. Khắc phục chậm (4-8 giờ).
*   **2. Mù dữ liệu (Ra quyết định):** Không có Data Warehouse. Trễ dữ liệu 48h. Tỷ lệ sai lệch đối soát doanh thu lên đến 3.8%.
*   **3. Rủi ro tuân thủ NĐ13 (Bảo mật):** Hình ảnh CCCD, Face ID lưu/truyền tải trên điện thoại cá nhân (0% mã hóa), đối mặt nguy cơ phạt pháp lý cao.

---

## Người 2: Mục tiêu TO-BE & Bộ KPI Kỹ thuật

**Slide 5: Ma trận truy vết Vấn đề & Mục tiêu**
*   Vấn đề 1 (Đứt gãy tích hợp) → Mục tiêu: Hệ thống độ sẵn sàng cao, hoạt động được offline.
*   Vấn đề 2 (Mù dữ liệu) → Mục tiêu: Luồng dữ liệu tự động, chuẩn hóa thời gian thực.
*   Vấn đề 3 (Lộ lọt PII) → Mục tiêu: Zero Trust, bảo mật 100% dữ liệu định danh theo quy định.

**Slide 6: Bộ KPI Kỹ thuật (Nền tảng, Bảo mật) & Phân định ranh giới**
*   *(Cam kết theo chuẩn quốc tế Google SRE, Atlassian ITSM, ISO 25012)*
*   **KPI 1.1 - Tính sẵn sàng (Uptime):** ≥ 99.99% (Downtime ≤ 4,32 phút/tháng).
*   **KPI 1.2 - Khôi phục trung bình (MTTR):** ≤ 30 phút (Hệ thống tự phục hồi).
*   **KPI 2.1 - Độ trễ dữ liệu (Data Freshness):** CDC luồng giao dịch POS về Data Lakehouse ≤ 5 giây.
*   **KPI 2.2 - Độ toàn vẹn (Completeness):** ≥ 99.5% bản ghi đẩy thành công, sai lệch doanh thu < 0.5%.
*   **KPI 3.1 - Độ phủ mã hóa (Encryption Coverage):** 100% cho mọi trường PII (at-rest & in-transit).
*   **KPI 3.2 - Điểm khôi phục (RPO):** ≤ 15 phút.
*   **Ranh giới kỹ thuật:** 
    *   *Đồ án Hạ tầng:* Đảm bảo Uptime 99.99% và Dữ liệu < 5s (Cung cấp hạ tầng và khối lượng dữ liệu đầu vào).
    *   *Đồ án AI (Thực hành):* Chịu trách nhiệm độ chính xác thuật toán MAPE < 15% (Thực thi mô hình phân tích AI trên nền tảng).

---

## Người 3: Phạm vi dự án & So sánh Kịch bản Kiến trúc

**Slide 7: Quy hoạch 5 lớp năng lực hạ tầng**
*   **Trong phạm vi đầu tư:**
    *   Lớp 4 (App & Integration Platform): API Gateway, Kafka, Container (K8s/K3s).
    *   Lớp 5 (Data Platform): Data Lakehouse, Airflow, CDC Streaming.
    *   Lớp 3 (Security + Identity): Hệ thống IAM/SSO và giải pháp mã hóa PII.
*   **Ngoài phạm vi (Tận dụng hiện có):** Cáp/Mạng lõi vật lý, Ứng dụng nghiệp vụ người dùng cuối.

**Slide 8: Bốn ràng buộc quyết định kiến trúc**
*   **Ràng buộc 1:** Bắt buộc có chế độ Offline Mode (Mất mạng vẫn phải tính tiền giờ cho khách).
*   **Ràng buộc 2:** Hạ tầng phân mảnh, không thể thiết lập phòng máy chủ đạt chuẩn tại 34 điểm thuê.
*   **Ràng buộc 3:** Dữ liệu cá nhân (PII) không được giao phó cho Cloud public (Tuân thủ NĐ13).
*   **Ràng buộc 4:** Phải có khả năng tự động mở rộng (Auto-scaling) theo biến động tải.

**Slide 9: Bảng Đánh giá 3 kịch bản kiến trúc**

| Tiêu chí bắt buộc để đạt KPI | On-Premise 100% | Cloud-Native 100% | Hybrid Cloud (Đề xuất) |
| :--- | :---: | :---: | :---: |
| **1. Đảm bảo Uptime 99,99% khi mất kết nối mạng chi nhánh** | ✓ | ✗ | ✓ |
| **2. Khả năng mở rộng tự động (Auto-scaling)** | ✗ | ✓ | ✓ |
| **3. Tuân thủ vị trí lưu trữ dữ liệu PII (Nghị định 13)** | ✓ | ✗ | ✓ |
| **4. Tối ưu chi phí đầu tư ban đầu (CAPEX) thấp** | ✗ | ✓ | ✓ |
| **5. Thời gian triển khai dịch vụ nhanh (Agility)** | ✗ | ✓ | ✓ |
| **6. Khả năng khôi phục thảm họa (Active-Active)** | ✗ | ✓ | ✓ |
| **Tổng số tiêu chí đáp ứng** | **2 / 6** | **4 / 6** | **6 / 6** |

---

## Người 4: Thiết kế Tổng thể Kiến trúc Hybrid Cloud

**Slide 10: Sơ đồ Kiến trúc TO-BE (Hybrid Cloud)**
*   *(Chèn Sơ đồ kiến trúc tổng thể Hybrid)*
*   **Public Cloud:** Đảm nhận Lớp 4 (K8s, API Gateway) và Lớp 5 (Lakehouse, Kafka). Năng lực điện toán tải nặng.
*   **On-Premise (HQ):** Máy chủ vật lý nội bộ kiểm soát Lớp 3 (Bảo mật IAM, PII DB).
*   **Edge (34 Chi nhánh):** Edge Cluster làm bộ đệm tính toán cục bộ.

**Slide 11: Giải quyết bài toán Tích hợp & Đứt gãy (Lớp 4)**
*   **Tại Cloud:** API Gateway xử lý tập trung (rate limiting, auth).
*   **Tại Edge (Chi nhánh):** Triển khai K3s + Kafka mini.
*   **Cơ chế Store-and-Forward (Offline Mode):** Khi mất kết nối internet, POS chi nhánh tự động gọi API cục bộ tại Edge để tính tiền. Khi mạng có lại, Edge tự động đồng bộ bù dữ liệu lên Cloud.

**Slide 12: Giải quyết bài toán Dữ liệu & PII (Lớp 5 & Lớp 3)**
*   **Luồng CDC Streaming:** Đọc thay đổi Database từ POS, đẩy lên Lakehouse qua Kafka dưới 5 giây.
*   **Kiểm soát PII Zero-Trust:** Dữ liệu CCCD/Face ID được đẩy trực tiếp về On-Premise Server ở HQ.
*   **Tại Cloud:** Toàn bộ dữ liệu trước khi lên Lakehouse đã qua màng lọc ẩn danh hóa dữ liệu. Cloud chỉ chứa dữ liệu phục vụ báo cáo doanh thu & huấn luyện AI.

---

## Người 5: Tiêu chuẩn Kỹ thuật - Hiệu năng & Khôi phục (HA/DR)

**Slide 13: Yêu cầu Hiệu năng & Dung lượng (TR-P)**
*   **Khả năng chịu tải (API):** ≥ 2.000 kết nối đồng thời (Concurrent connections).
*   **Độ trễ API (P95):** Round-trip từ Edge → Cloud → Edge ≤ 200 ms.
*   **Thông lượng dữ liệu (CDC):** Xử lý ≥ 5.000 sự kiện/giây (Tải cao điểm 34 CN).
*   **Thời gian phản hồi AI:** Truy vấn dự báo end-to-end ≤ 500ms/request.

**Slide 14: Độ sẵn sàng cao (High Availability)**
*   **Cloud Kubernetes:** Cấu hình Multi-zone Active-Active, tự động failover node lỗi ≤ 60 giây.
*   **Kafka Cluster:** Hệ số Replication Factor ≥ 3, vô hiệu hóa trực tiếp 1 broker không làm thất thoát tin nhắn.
*   **Edge Queue:** Dung lượng đệm cục bộ chứa tối thiểu 48 giờ giao dịch cho mỗi chi nhánh.

**Slide 15: Chiến lược Khôi phục sau Thảm họa (Disaster Recovery)**
*   **Immutable Backup:** Cloud Storage chống ghi đè/xóa (Ransomware protection), lưu trữ 30 ngày.
*   **Khôi phục Point-In-Time (PITR):** Quay ngược Database về bất kỳ giây nào trong vòng 7 ngày.
*   **Cam kết DR:** RPO (Lượng dữ liệu mất tối đa) ≤ 15 phút; RTO (Thời gian dựng lại hệ thống) ≤ 4 giờ.

---

## Người 6: Tiêu chuẩn Kỹ thuật - Bảo mật & Vận hành (Security & Ops)

**Slide 16: Quản trị Danh tính tập trung (IAM/SSO)**
*   **Hệ thống lõi:** Triển khai Keycloak quản lý tập trung.
*   **Trải nghiệm người dùng:** Single Sign-On (SSO) - Đăng nhập 1 lần vào được cả 8 phần mềm hiện hữu.
*   **Bảo mật:** Ép buộc xác thực đa yếu tố (MFA) với 100% tài khoản Admin. Phân quyền chặt chẽ theo Rule-Based Access Control (RBAC).

**Slide 17: Bảo mật PII & Tuân thủ NĐ13**
*   **Mã hóa lưu trữ (At-rest):** Áp dụng AES-256 cho 100% cột chứa CCCD, Face ID, SĐT.
*   **Mã hóa truyền tải (In-transit):** Giao thức TLS 1.2+ bắt buộc trên toàn mạng.
*   **Quét lỗ hổng tự động (Vulnerability Scan):** Định kỳ hàng tuần. Ràng buộc kỹ thuật: Không tồn tại lỗ hổng Critical/High quá 72 giờ.

**Slide 18: Observability & Tự động hóa Vận hành**
*   **Monitoring tập trung:** Cụm Prometheus + Grafana (Metrics) và Loki (Centralized Logging lưu ≥ 90 ngày).
*   **Infrastructure as Code (IaC):** 100% cấu hình quản lý bằng Terraform/Ansible. Thời gian Rollback hệ thống cũ ≤ 15 phút.
*   **CI/CD Pipeline:** Tự động Build → Test → Deploy cho mọi bản cập nhật phần mềm.

---

## Người 7: Danh mục Đầu tư (BOM) & Dự toán Chi phí

**Slide 19: Chiến lược BOM & Giấy phép (License)**
*   **Nguyên tắc:** Tối đa hóa công nghệ Open-source (K3s, Kafka, Airflow, PostgreSQL, Keycloak) để tránh chi phí phần mềm đắt đỏ.
*   **Phần cứng Edge:** 36 thiết bị Mini Server (Intel NUC + UPS) cho 34 chi nhánh (2 máy dự phòng thay thế trực tiếp).
*   **Phần cứng On-Premise:** 2 Máy chủ Rack Server 2U chạy Active-Passive, kèm thiết bị Tường lửa NGFW.

**Slide 20: Dự toán Chi phí Đầu tư ban đầu (CAPEX)**
*   **Tổng phần cứng thiết bị:** 564.800.000 VNĐ.
*   **Tổng dịch vụ triển khai:** 632.000.000 VNĐ (Thiết kế, Deploy Cloud, Migrate dữ liệu, code Tích hợp API 8 phần mềm).
*   **Hạ tầng Cloud (4 tháng Dev):** 112.000.000 VNĐ.
*   **TỔNG NGÂN SÁCH CAPEX:** 1.308.800.000 VNĐ.

**Slide 21: Dự toán Chi phí Vận hành (OPEX)**
*   **Thuê bao Cloud định kỳ:** K8s, PostgreSQL, Kafka, S3 Storage.
*   **Hạ tầng mạng:** Nâng cấp băng thông Internet tại 34 chi nhánh.
*   **Nhân sự Ops:** 1 Kỹ sư SRE/DevOps, 0.5 Data Engineer.
*   **License & Bảo trì:** Gia hạn tường lửa, Pentest thuê ngoài định kỳ.
*   **TỔNG OPEX DỰ KIẾN:** 1.123.400.000 VNĐ/năm.

---

## Người 8: Tổng chi phí sở hữu (TCO) & Phân tích ROI

**Slide 22: Tổng chi phí sở hữu (TCO 3 năm)**
*   **Năm 1 (CAPEX + OPEX):** ~2,67 tỷ VNĐ.
*   **Năm 2 & Năm 3 (OPEX):** ~2,53 tỷ VNĐ.
*   **Quỹ dự phòng (Contingency 10%):** ~473 triệu VNĐ.
*   **TỔNG TCO 3 NĂM:** 5.209.160.000 VNĐ.
*   **Tỷ trọng:** Chiếm khoảng 1.45% tổng doanh thu chuỗi trong cùng kỳ (Mức đầu tư lý tưởng của ngành).

**Slide 23: Lượng hóa Lợi ích Tài chính (Hàng năm)**
*   **Tiết kiệm nhân lực:** Giảm 2.500h công làm báo cáo thủ công (~125 tr).
*   **Giảm thất thoát:** Thu hồi nhờ tự động đối soát chính xác (~700 tr).
*   **Duy trì kinh doanh:** Giảm thiệt hại doanh thu nhờ xóa bỏ downtime kéo dài (~400 tr).
*   **Lợi ích kế thừa từ AI:** Tối ưu giờ công, giảm hao hụt nguyên liệu F&B (~580 tr).
*   **TỔNG LỢI ÍCH QUY ĐỔI:** ~1.955.000.000 VNĐ/năm.

**Slide 24: Dòng tiền ròng & Điểm hoàn vốn (Payback)**
*   **Dòng tiền thuần (Lợi ích - OPEX):** + 831.600.000 VNĐ/năm.
*   **Thời gian hoàn vốn (Payback Period):** ~1,73 năm (21 tháng).
*   **Đánh giá rủi ro biên:** Kể cả khi loại bỏ hoàn toàn dòng lợi ích từ AI, dự án vẫn BẮT BUỘC khả thi vì chi phí này rẻ hơn mức phạt 5% doanh thu (lên đến 6 tỷ) khi bị thanh tra Nghị định 13.

---

## Người 9: Lộ trình Triển khai, Rủi ro & Nghiệm thu

**Slide 25: Lộ trình Triển khai (Roadmap 16 tuần)**
*   *Thiết kế gối đầu 5 pha, hoàn thành trong 16 tuần lịch:*
    *   **Pha 1 (T1-T3):** Foundation (VPN, Tường lửa, Cài đặt nền tảng PII).
    *   **Pha 2 (T3-T6):** Core (Dựng cụm Cloud K8s HA, Database).
    *   **Pha 3 (T6-T9):** Security Uplift (Tích hợp API khó nhất, luồng CDC).
    *   **Pha 4 (T9-T13):** Migration, AI & Chạy Pilot tại 5 chi nhánh.
    *   **Pha 5 (T13-T16):** Rollout hàng loạt 29 chi nhánh còn lại.

**Slide 26: Nhận diện & Quản trị Rủi ro**
*   **Kháng cự mở API từ Vendor POS:** Dùng Adapter pattern đọc trực tiếp CSDL Read-Only để không bị nghẽn tiến độ.
*   **Lỗi phần cứng Edge khi Rollout:** Sử dụng 2 server dự phòng, cài lại bằng Golden Image trong 30 phút.
*   **Mô hình AI không đạt chuẩn:** Hạ tầng Cloud và Lakehouse vẫn Go-live độc lập, dùng thuật toán Moving Average tạm thời.

**Slide 27: Tổ chức mua sắm & Dự án (RACI)**
*   **Đấu thầu:** Gọi thầu cạnh tranh (RFP), chọn nhà thầu theo tỷ trọng 70% Điểm kỹ thuật, 30% Tài chính.
*   **Pháp lý:** Ràng buộc chặt bằng NDA bảo mật dữ liệu PII và SLA phạt tài chính nếu trễ tiến độ.
*   **Quản trị thay đổi:** Khóa phạm vi chặt chẽ. Mọi thay đổi quy mô (CR) phải lập vé qua ITSM Jira và có phê duyệt.

**Slide 28: Kế hoạch Nghiệm thu & Bàn giao hệ thống**
*   **Tiêu chuẩn Kỹ thuật:** API chịu được Load Test 2.000 concurrent; Rút dây mạng thử nghiệm tính tiền hoạt động ngoại tuyến thành công 100%.
*   **Tiêu chuẩn Bảo mật:** Diễn tập thảm họa (DR Drill) < 4h; Quét bảo mật trả về không có lỗi Critical/High.
*   **Bàn giao:** Chuyển giao toàn bộ Source code IaC, thiết kế LLD, Hệ thống Monitor, và đào tạo vận hành qua 10 bộ SOP Runbook chuẩn mực.
