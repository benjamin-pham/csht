# KỊCH BẢN TRÌNH BÀY ĐỒ ÁN MÔN HỌC (9 NGƯỜI)
**Thời gian:** 45 phút (Mỗi người trình bày trong 5 phút, tập trung không ngắt quãng).
**Văn phong:** Kỹ thuật, trực diện, không dài dòng. Mọi con số đều phải bám sát đặc tả kỹ thuật.

---

## Người 1: Tổng quan & Hiện trạng hệ thống (Phút 00:00 - 05:00)

**Slide 1:** 
Kính chào hội đồng. Em là [Tên Người 1], thay mặt nhóm, em xin trình bày đồ án Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station. Dự án này giải quyết bài toán hạ tầng nền tảng, tạo tiền đề bắt buộc để triển khai các ứng dụng phân tích AI (Artificial Intelligence).

**Slide 2:** 
Ways Station đang vận hành 34 chi nhánh theo mô hình 34 hộ kinh doanh cá thể riêng biệt. Mỗi chi nhánh cung cấp đa dịch vụ (Gym, Net, Bida, Hub) với đặc thù tính tiền theo giờ và không có IT (Information Technology) trực tại chỗ. 

**Slide 3:** 
Về mặt kiến trúc AS-IS hiện tại, đây là sơ đồ 34 hệ thống dữ liệu hoàn toàn bị cô lập. Tỷ lệ tích hợp luồng tự động là 0%. Các phần mềm POS (Point of Sale), quản lý Gym hay Cổng nhân sự không giao tiếp được với nhau. 100% việc đối soát dữ liệu và hỗ trợ vận hành bị đẩy qua 3 kênh thủ công: Tổng đài phân luồng, Zalo cá nhân, và sổ giao ca giấy.

**Slide 4:** 
Từ kiến trúc này sinh ra 3 điểm nghẽn kỹ thuật nghiêm trọng:
Thứ nhất, đứt gãy tích hợp. Không có API (Application Programming Interface) Gateway, mất kết nối mạng đồng nghĩa với gián đoạn bán hàng, thời gian phát hiện sự cố lên tới 4-8 giờ.
Thứ hai, mù dữ liệu. Do không có kho tập trung, độ trễ báo cáo là 48h, sai lệch số liệu doanh thu ở mức 3.8%.
Thứ ba, và cũng là rủi ro lớn nhất: Lỗ hổng tuân thủ Nghị định 13. Dữ liệu nhạy cảm PII (Personally Identifiable Information) như ảnh CCCD, Face ID của khách hàng đang truyền tải hoàn toàn dạng plaintext qua Zalo cá nhân của nhân viên, đối mặt rủi ro phạt tới 5% doanh thu chuỗi.

---

## Người 2: Mục tiêu TO-BE & Bộ KPI (Key Performance Indicator) Kỹ thuật (Phút 05:00 - 10:00)

**Slide 5:** 
Kính chào hội đồng, em là [Tên Người 2]. Tiếp nối phần hiện trạng, nhóm em ánh xạ 3 điểm nghẽn vừa nêu thành 3 mục tiêu kiến trúc hệ thống: Đạt độ sẵn sàng cao, Xây dựng luồng dữ liệu thời gian thực tin cậy, và Bảo mật 100% dữ liệu PII. Tất cả được lượng hóa bằng bộ KPI chuẩn quốc tế.

**Slide 6:** 
Về các chỉ số nền tảng, nhóm em cam kết 6 KPI như sau:
- KPI 1.1: Đo lường tính sẵn sàng theo chuẩn Google SRE (Site Reliability Engineering). Uptime cam kết tối thiểu 99.99%, nghĩa là downtime không vượt quá 4,32 phút/tháng.
- KPI 1.2: Thời gian khôi phục trung bình (MTTR - Mean Time To Recovery) theo chuẩn Atlassian ITSM (IT Service Management), bắt buộc hệ thống tự phục hồi dưới 30 phút.
- KPI 2.1: Độ trễ luồng Change Data Capture (CDC) không vượt quá 5 giây từ POS lên Cloud.
- KPI 2.2: Độ toàn vẹn dữ liệu (Completeness) khi đẩy lên Cloud phải đạt 99.5%.
- KPI 3.1: Về bảo mật, tỷ lệ mã hóa PII phải đạt 100% cho cả dữ liệu lưu trữ và truyền tải.
- KPI 3.2: Điểm khôi phục dữ liệu (RPO - Recovery Point Objective) khi có sự cố không được quá 15 phút.

---

## Người 3: Phạm vi dự án & So sánh Kịch bản Kiến trúc (Phút 10:00 - 15:00)

**Slide 7:** 
Kính chào hội đồng, em là [Tên Người 3]. Để đạt được các KPI trên, nhóm em không đầu tư thiết bị rời rạc mà quy hoạch theo Lớp năng lực hạ tầng. Dự án tập trung vào Lớp 4 (Nền tảng tích hợp ứng dụng - API Gateway, Kafka), Lớp 5 (Nền tảng dữ liệu Data Lakehouse) và 2 thành phần cốt lõi của Lớp 3 là Quản lý định danh IAM (Identity and Access Management)/SSO (Single Sign-On) và Mã hóa PII. Lớp 1 (Network) chỉ tận dụng và nâng cấp nhỏ.

**Slide 8:** 
Quyết định kiến trúc bị chi phối bởi 4 ràng buộc cứng từ doanh nghiệp:
1. Mô hình tính tiền theo giờ bắt buộc chi nhánh phải hoạt động offline khi mất mạng.
2. 34 pháp nhân riêng rẽ, không có IT tại chỗ.
3. Dữ liệu PII thu thập tại quầy bắt buộc tự lưu trữ tại Việt Nam để tuân thủ luật.
4. Cần khả năng mở rộng tự động do tải biến động mạnh.

**Slide 9:** 
Nhóm em đánh giá 3 kịch bản:
- On-Premise 100% đáp ứng tốt Offline và bảo mật PII, nhưng CAPEX (Capital Expenditure) rất lớn (gần 3 tỷ), không thể auto-scale và bắt buộc phải có IT tại chỗ.
- Cloud-Native 100% có chi phí CAPEX thấp nhất, co giãn tốt, nhưng vi phạm hai ràng buộc cứng: Mất kết nối mạng là tổn thất doanh thu ngay lập tức, và dữ liệu PII phơi nhiễm trên hạ tầng bên thứ ba.
- Kịch bản Hybrid Cloud (Lai) là phương án duy nhất thỏa mãn 6/6 tiêu chí kỹ thuật.

---

## Người 4: Thiết kế Tổng thể Kiến trúc Hybrid Cloud (Phút 15:00 - 20:00)

**Slide 10:** 
Kính chào hội đồng, em là [Tên Người 4]. Tiếp theo, em xin trình bày thiết kế kiến trúc Hybrid Cloud đề xuất. Khối lượng điện toán nặng (API Gateway, Lakehouse) được đưa lên Public Cloud. Tại trụ sở (HQ - Headquarters), nhóm em đề xuất giữ hệ thống Server nội bộ chỉ để xử lý định danh và PII. Tại 34 chi nhánh, nhóm em đề xuất đặt các Edge Cluster nhỏ gọn.

**Slide 11:** 
Đi sâu vào Lớp 4. Để giải bài toán mất kết nối mạng, tại 34 chi nhánh cài đặt cụm K3s (Edge Cluster) đóng vai trò làm bộ đệm (Store-and-Forward). Khi mạng ổn định, POS gọi API lên Cloud. Khi mất kết nối mạng, phần mềm tự động chuyển sang gọi API nội bộ trên Edge Cluster để tính giờ bình thường. Dữ liệu lưu tạm vào Local Queue và tự động đẩy bù lên Cloud khi mạng phục hồi, đảm bảo MTTR dưới 30 phút.

**Slide 12:** 
Về Lớp 5 và Bảo mật dữ liệu. Luồng CDC lấy dữ liệu từ POS, đi qua tiến trình ẩn danh hóa (loại bỏ toàn bộ CCCD/FaceID) trước khi nạp lên Data Lakehouse trên Cloud theo thời gian thực (dưới 5s). Thông tin nhạy cảm PII được điều hướng về máy chủ vật lý On-Premise tại HQ. Cloud hoàn toàn không nắm giữ dữ liệu định danh, giúp doanh nghiệp an toàn trước NĐ13.

---

## Người 5: Tiêu chuẩn Kỹ thuật - Hiệu năng & Khôi phục thảm họa (Phút 20:00 - 25:00)

**Slide 13:** 
Kính chào hội đồng, em là [Tên Người 5]. Kiến trúc vừa rồi được chuyển hóa thành các yêu cầu kỹ thuật cứng (Specs) để chào thầu.
Về hiệu năng, API Gateway (TR-P01) phải chịu tải đồng thời 2.000 kết nối. Độ trễ round-trip API (TR-P02) không vượt quá 200ms. Luồng dữ liệu CDC throughput duy trì mức 5.000 sự kiện/giây vào giờ cao điểm, không được phép rớt gói tin.

**Slide 14:** 
Về độ sẵn sàng cao (High Availability). Trên Cloud Kubernetes phải chạy kiến trúc Multi-zone Active-Active, tự động failover node lỗi dưới 60 giây. Cụm Kafka streaming yêu cầu Replication factor tối thiểu là 3, đảm bảo vô hiệu hóa trực tiếp 1 broker thì luồng dữ liệu vẫn tiếp tục mà không thất thoát.

**Slide 15:** 
Về chiến lược dự phòng thảm họa (Disaster Recovery). Data Lakehouse phải có backup dạng Immutable lưu 30 ngày (chống Ransomware). Database có cơ chế PITR (Point-in-Time Recovery) cho phép khôi phục về bất cứ thời điểm nào trong 7 ngày gần nhất, đảm bảo mức RPO dưới 15 phút.

---

## Người 6: Tiêu chuẩn Kỹ thuật - Bảo mật & Vận hành (Phút 25:00 - 30:00)

**Slide 16:** 
Kính chào hội đồng, em là [Tên Người 6]. Chuyển sang lớp Bảo mật, toàn hệ thống áp dụng mô hình Zero Trust thông qua giải pháp IAM Keycloak. Nhân viên chỉ đăng nhập 1 lần (SSO) để truy cập 8 phần mềm. Tất cả tài khoản quản trị viên đều bị ép buộc xác thực đa yếu tố (MFA - Multi-Factor Authentication).

**Slide 17:** 
Để tuân thủ tuyệt đối NĐ13 (TR-S03 đến S05), 100% dữ liệu PII lưu tại On-Premise được mã hóa AES-256 (Advanced Encryption Standard) ở trạng thái nghỉ (at-rest) và dùng TLS (Transport Layer Security) 1.2+ khi truyền tải (in-transit). Định kỳ hàng tuần hệ thống sẽ rà quét tự động (Vulnerability Scan), không cho phép lỗ hổng Critical tồn tại quá 72 giờ.

**Slide 18:** 
Về tiêu chuẩn vận hành nền tảng (TR-O). Năng lực Observability cấu thành từ Prometheus, Grafana và Loki giúp giám sát sâu tài nguyên toàn cụm. Mọi thay đổi hạ tầng phải được quản lý bằng mã (Infrastructure as Code) với Terraform, cho phép rollback cấu hình lỗi dưới 15 phút.

---

## Người 7: Danh mục Đầu tư (BOM - Bill of Materials) & Dự toán Chi phí (Phút 30:00 - 35:00)

**Slide 19:** 
Kính chào hội đồng, em là [Tên Người 7]. Dựa trên Specs kỹ thuật, nhóm em xây dựng BOM đầu tư. Chiến lược là tối đa hóa phần mềm Open-Source (như K3s, Kafka, Airflow) để tránh phụ thuộc chi phí bản quyền. Phần cứng vật lý chỉ bao gồm 36 bộ Edge Mini Server cho chi nhánh (có tính dự phòng), 2 máy chủ Rack Server HA (High Availability) cho HQ cùng hệ thống Firewall NGFW (Next-Generation Firewall).

**Slide 20:** 
Dự toán Đầu tư ban đầu (CAPEX). Ngân sách chi cho phần cứng là 564,8 triệu. Dịch vụ triển khai (bao gồm thiết kế, deploy Cloud, setup Edge, và quan trọng nhất là migrate tích hợp API 8 hệ thống) là 632 triệu. Cùng với chi phí hạ tầng Cloud dev 4 tháng. Tổng ngân sách CAPEX là 1,308 tỷ VNĐ.

**Slide 21:** 
Dự toán Vận hành (OPEX - Operational Expenditure). Để duy trì sau Go-live, doanh nghiệp cần chi trả chi phí Managed K8s, PostgreSQL, Kafka trên Cloud, chi phí nâng cấp băng thông Internet tại 34 chi nhánh và lương cho kỹ sư DevOps/SRE giám sát hệ thống. Tổng OPEX định kỳ ước tính 1,123 tỷ VNĐ/năm.

---

## Người 8: TCO (Total Cost of Ownership) & Đánh giá hiệu quả đầu tư (ROI - Return on Investment) (Phút 35:00 - 40:00)

**Slide 22:** 
Kính chào hội đồng, em là [Tên Người 8]. Về mặt tài chính, Tổng chi phí sở hữu (TCO) trong chu kỳ 3 năm (bao gồm CAPEX, OPEX 3 năm và 10% quỹ dự phòng rủi ro) rơi vào khoảng 5,209 tỷ VNĐ. Con số này tương đương 1,45% tổng doanh thu chuỗi trong cùng kỳ, hoàn toàn nằm trong biên độ đầu tư CNTT chuẩn của ngành bán lẻ.

**Slide 23:** 
Giá trị hệ thống mang lại được lượng hóa: Tiết kiệm 2.500 giờ công đối soát (~125 triệu); thu hồi thất thoát nhờ làm sạch số liệu (~700 triệu); giảm downtime (~400 triệu). Các hạng mục phụ thuộc mô hình AI như tối ưu quỹ lương và giảm hao hụt F&B (Food and Beverage) cũng mang lại ~580 triệu. Tổng lợi ích quy đổi khoảng 1,95 tỷ VNĐ/năm.

**Slide 24:** 
Với dòng tiền ròng hàng năm sau khi trừ OPEX đạt 831 triệu, dự án sẽ hoàn vốn đầu tư (Payback) trong khoảng 1.7 năm. Ngay cả trong kịch bản mô hình AI thất bại hoàn toàn, dòng tiền thuần giảm sút, dự án vẫn được khuyến nghị triển khai bắt buộc, vì mức chi phí này rẻ hơn rất nhiều so với rủi ro bị phạt thanh tra 5% doanh thu (tương đương 6 tỷ VNĐ) do vi phạm NĐ13.

---

## Người 9: Lộ trình triển khai, Rủi ro & Nghiệm thu (Phút 40:00 - 45:00)

**Slide 25:** 
Kính chào hội đồng, em là [Tên Người 9]. Phần cuối cùng, lộ trình thực thi (Roadmap) thiết kế trong 16 tuần lịch, chia thành 5 pha gối đầu. 
Pha 1: Hạ tầng mạng & Bảo mật nền. Pha 2: Core Cloud (K8s, HA). Pha 3: Tích hợp API và SSO (Giai đoạn phức tạp nhất). Pha 4: Pilot 5 chi nhánh. Pha 5: Rollout toàn bộ 34 chi nhánh.

**Slide 26:** 
Về quản trị rủi ro, dự án nhận diện nguy cơ cao nhất nằm ở Pha 3 khi phải mở API kết nối với các POS đa vendor. Kế hoạch giảm thiểu là xây dựng adapter pattern truy xuất trực tiếp Database read-only nếu vendor từ chối mở API. Rủi ro Edge Server hỏng khi rollout được xử lý bằng 2 bộ dự phòng thay thế trực tiếp cùng cơ chế cài đặt qua Golden Image trong 30 phút.

**Slide 27:** 
Để vận hành dự án, ma trận RACI (Responsible, Accountable, Consulted, Informed) phân quyền rõ ràng. Phương thức mua sắm là chào giá cạnh tranh (RFP - Request for Proposal) với trọng số kỹ thuật 70%. Vendor bắt buộc cam kết SLA (Service Level Agreement) bằng tài chính.

**Slide 28:** 
Hoạt động nghiệm thu bám sát KPI. Tiêu chuẩn kỹ thuật yêu cầu: Hệ thống vượt qua bài Load Test 2.000 concurrent; Test ngắt mạng 4 giờ tại chi nhánh không rớt dữ liệu (hoạt động ngoại tuyến thành công 100%); DR (Disaster Recovery) khôi phục dưới 4 tiếng; và Quét bảo mật trả về không có lỗi Critical. Chuyển giao đầy đủ Runbook, mã nguồn IaC (Infrastructure as Code) và hệ thống giám sát. 

Cảm ơn hội đồng đã lắng nghe phần thuyết minh giải pháp kiến trúc của nhóm.

