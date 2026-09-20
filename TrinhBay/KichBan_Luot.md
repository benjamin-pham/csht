# Kịch Bản Trình Bày (Bản Nhắc Ý - Đã mở rộng)

> Bản này cân bằng giữa ý chính và lời nói. Vẫn dùng gạch đầu dòng để dễ nhìn lướt, nhưng các câu chữ được viết rõ ý hơn để bạn có thể đọc trực tiếp nếu lỡ quên bài.
> Tổng thời gian dự kiến: **~12 - 14 phút**.

---

### MỞ ĐẦU & TỔNG QUAN (Slide 1 - 3)
**Slide 1: Trang bìa**
- Kính chào cô và các bạn. Em là [TÊN], đại diện Nhóm 5.
- Hôm nay nhóm em xin trình bày Đồ án & Thực hành môn CSHT, ứng dụng cho chuỗi Ways Station.

**Slide 2: Cấu trúc**
- Bài báo cáo gồm 2 phần chạy song song trên cùng một doanh nghiệp.
- **Phần 1: Đồ án** – Xây dựng nền tảng hạ tầng CNTT.
- **Phần 2: Thực hành** – Xây dựng ứng dụng AI dự báo khách hàng.

**Slide 3: Tổng quan Ways Station (TRỌNG TÂM)**
- Ways Station là chuỗi 34 chi nhánh giải trí: Gym, Net, Bida, Cầu lông.
- **Đặc thù 1:** Khách quẹt thẻ tính tiền theo giờ $\rightarrow$ Sập mạng là mất doanh thu ngay lập tức.
- **Đặc thù 2:** 34 chi nhánh là 34 hộ kinh doanh độc lập, không có IT tại chỗ.
- **Đặc thù 3 (rất rủi ro):** Nhân viên đang chụp CCCD của khách lưu trên điện thoại cá nhân $\rightarrow$ Vi phạm nghiêm trọng Nghị định 13.

---

### PHẦN 1: ĐỒ ÁN (Slide 4 - 15)
**Slide 4: Phần 1**
- Bắt đầu Phần 1: Đề xuất đầu tư Nền tảng hạ tầng.

**Slide 5: 4 Điểm nghẽn hiện tại**
- **Hạ tầng:** Dùng 8 phần mềm rời rạc, báo cáo chậm trễ 48 giờ.
- **Vận hành:** Giao tiếp hoàn toàn thủ công qua Zalo và sổ giấy, đã tới giới hạn.
- **Bảo mật:** Lưu trữ dữ liệu nhạy cảm bừa bãi, không hề mã hóa.
- **Pháp lý:** Nguy cơ bị phạt tới 5% doanh thu do vi phạm Nghị định 13.

**Slide 6: Phạm vi đầu tư (3 Lớp Năng Lực)**
- Nhóm em giải quyết bằng 3 lớp kiến trúc:
- **Lớp 4 (Ứng dụng):** Dùng API Gateway, Kafka và Kubernetes nối liền 8 phần mềm.
- **Lớp 5 (Dữ liệu):** Xây dựng Data Lakehouse để kéo dữ liệu về Real-time.
- **Lớp 3 (Bảo mật):** Triển khai đăng nhập SSO (Keycloak) và mã hóa toàn bộ dữ liệu.

**Slide 7: Đối tượng thụ hưởng**
- Giám đốc xem được báo cáo tức thì. Nhân viên HQ giảm 2.500 giờ làm tay.
- Quan trọng nhất: Nhân viên chi nhánh **vẫn tính được tiền dù bị rớt mạng** (offline mode).

**Slide 8, 9, 10: Ma trận 6 KPI & Công thức (TRỌNG TÂM)**
- Nhóm em dùng 6 KPI để đo lường 3 vấn đề cốt lõi:
- *Đo lường tích hợp (Lớp 4):*
  - **Uptime:** Dùng để đo độ sẵn sàng của nền tảng. Target $\ge$ 99,99% (nghĩa là sập tối đa 4 phút/tháng).
  - **MTTR (Thời gian phục hồi):** Dùng để đo tốc độ tự sửa lỗi của K8s. Target $\le$ 30 phút.
- *Đo lường dữ liệu (Lớp 5):*
  - **Data Freshness:** Dùng để đo độ trễ dữ liệu từ máy POS lên Cloud. Target $\le$ 5 giây.
  - **Data Completeness:** Dùng để đo tỷ lệ chống thất thoát dữ liệu. Target $\ge$ 99,5%.
- *Đo lường bảo mật (Lớp 3):*
  - **Encryption Coverage:** Dùng để đo mức độ bảo vệ PII (chống NĐ13). Target = 100% mã hóa.
  - **RPO:** Dùng để đo giới hạn dữ liệu chấp nhận mất khi có thảm họa. Target $\le$ 15 phút.

**Slide 11: Kiến trúc Hybrid Cloud (TRỌNG TÂM)**
- Vì sao phải là **Hybrid Cloud**? Vì nó giải quyết trọn vẹn 4 đặc thù:
  1. Doanh thu theo giờ $\rightarrow$ Cần Edge server chạy offline $\rightarrow$ Bỏ Cloud-Native.
  2. Dữ liệu CCCD nhạy cảm $\rightarrow$ Phải giữ máy chủ nội bộ $\rightarrow$ Bỏ Cloud-Native.
  3. Không có IT tại chỗ $\rightarrow$ Cần tự động hóa từ xa $\rightarrow$ Bỏ On-Premise.
  4. Tăng trưởng nhanh $\rightarrow$ Cần khả năng tự co giãn $\rightarrow$ Bỏ On-Premise.
- Chỉ Hybrid Cloud mới làm được tất cả.

**Slide 12 & 13: CAPEX & OPEX**
- CAPEX (đầu tư ban đầu): 1,3 tỷ VNĐ (Chủ yếu là server và dịch vụ triển khai, bản quyền phần mềm = 0đ do dùng Open-source).
- OPEX (vận hành): 1,1 tỷ/năm (Chủ yếu là tiền thuê Cloud và nhân sự vận hành).

**Slide 14: TCO 3 năm (TRỌNG TÂM)**
- Tổng TCO 3 năm là 5,2 tỷ $\rightarrow$ Bằng 1,45% doanh thu, rất an toàn.
- Dòng tiền ròng mang lại ~832 triệu/năm.
- **Thời gian hoàn vốn:** Rất nhanh, chỉ **1,7 năm**. (Chưa tính giá trị tránh bị phạt 6 tỷ từ NĐ13).

**Slide 15: Nghiệm thu Đồ án**
- Test ngắt mạng 4h vẫn tính tiền được, load test 2.000 CCU, và quét lỗ hổng bảo mật sạch sẽ.

---

### PHẦN 2: THỰC HÀNH (Slide 16 - 29)
**Slide 16: Phần 2**
- Chuyển sang Phần 2: Xây dựng AI dự báo lưu lượng khách hàng. Đề tài này kế thừa hạ tầng từ Đồ án.

**Slide 17: Vấn đề vận hành**
- Khách đông/vắng biến động liên tục theo khung giờ.
- Xếp ca hiện tại dựa vào cảm tính $\rightarrow$ Gây lãng phí rất lớn quỹ lương (OPEX).

**Slide 18: Giải pháp AI**
- Xây AI dự báo lượng khách theo từng giờ cho 7 ngày tới.
- Output là Dashboard hỗ trợ quản lý ra quyết định xếp ca.

**Slide 19: Thụ hưởng Thực hành**
- Giúp Phòng điều phối tối ưu quỹ lương; Marketing biết giờ nào vắng để tung khuyến mãi.

**Slide 20: Các mô hình AI (TRỌNG TÂM)**
- Chạy thực nghiệm 4 mô hình: ARIMA, Prophet, LSTM, TSFM.
- **Nguyên tắc:** Cam kết đạt ngưỡng chỉ số, không fix chết thuật toán. Nếu không đạt thì dùng Moving Average dự phòng.

**Slide 21, 22, 23: KPI Nhóm A (Đo chất lượng AI)**
- **MAPE:** Dùng để đo phần trăm sai số tổng thể của mô hình. Target < 15%.
- **MAE:** Dùng để đo lượng khách lệch cụ thể. Target $\le$ 3 khách/giờ (ví dụ báo 30 thì thực tế nằm trong khoảng 27-33).
- **Precision:** Dùng để đo độ chính xác chống báo động giả (báo cao điểm là phải đúng). Target $\ge$ 85%.
- **Inference Latency:** Dùng để đo tốc độ suy luận, trả kết quả của AI. Target $\le$ 200ms.

**Slide 24 & 25: KPI Nhóm B (Đo Vận hành phần mềm)**
- **Uptime API:** Dùng để đo độ sẵn sàng của ứng dụng. Target $\ge$ 99,9%.
- **Batch Freshness:** Dùng để đo thời gian hoàn thành pipeline dữ liệu huấn luyện. Target $\le$ 24h.
- **API Response P95:** Dùng để đo tốc độ tải của màn hình Dashboard cho Quản lý. Target $\le$ 500ms.

**Slide 26: Data Pipeline**
- Kiến trúc luồng dữ liệu tự động: 
  - 1h sáng: Airflow tự rút dữ liệu từ POS. 
  - 2h sáng: AI Engine chạy dự báo. 
  - 8h sáng: Quản lý lên Dashboard duyệt ca.

**Slide 27 & 28: CAPEX & OPEX (Thực hành)**
- Đầu tư ban đầu (CAPEX): 663 triệu (chiếm chủ yếu là lương đội ngũ Dev/Data).
- Vận hành (OPEX): 325 triệu/năm (Cloud và nhân sự hỗ trợ).

**Slide 29: Nghiệm thu Thực hành**
- Phải đạt các chỉ số MAPE, Uptime. Quan trọng nhất là tự động hóa được quy trình xếp ca, tiết kiệm tối thiểu 15% OPEX lãng phí.

---

### KẾT THÚC (Slide 30)
**Slide 30: Cảm ơn**
- Trên đây là toàn bộ báo cáo của Nhóm 5. Cảm ơn cô và các bạn đã lắng nghe. Nhóm em sẵn sàng trả lời câu hỏi.
