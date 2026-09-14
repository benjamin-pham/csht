# Buổi 3: Sửa bài tập, Khái niệm Phần cứng & Lưu trữ, Hướng dẫn Đồ án (Bước 0)

## 1. Sửa bài tập nhóm & Góp ý của cô
- **Phần trình bày của Nhóm 6 (Giao Hàng Nhanh):** Nhóm trình bày về 5 lớp năng lực hạ tầng CNTT tại công ty Giao Hàng Nhanh (GHN), bao gồm các phân tích chi tiết về phần cứng, phần mềm, mạng, quản trị, bảo mật và nền tảng dữ liệu.
- **Nhận xét & Định hướng của cô:**
  - Đánh giá cao phần tìm hiểu công nghệ và thiết bị của nhóm.
  - **Lưu ý chung cho các nhóm:** Khi làm bài tập/đồ án, không bắt buộc phải chọn một doanh nghiệp quá cụ thể (có thể giả định bối cảnh chung). Tuy nhiên, khi làm đồ án, cần đưa ra quyết định lựa chọn thiết bị/công nghệ cụ thể và **phải giải thích được lý do** lựa chọn để thuyết phục nhà đầu tư.
  - **Giới hạn phạm vi đồ án:** Khuyến khích các nhóm **không nên ôm đồm cả 5 lớp năng lực**. Nên chọn từ **1 đến 3 lớp** (thường là lớp 2, 4, 5) để nghiên cứu sâu. 
  - Có thể **giả lập hiện trạng**: Cho phép giả định công ty đã có sẵn hạ tầng phần cứng và mạng ổn định, chỉ tập trung đề xuất đầu tư vào **phần mềm, quản trị và bảo mật** (phù hợp hơn với sinh viên chuyên ngành CNTT/Phần mềm).

## 2. Lý thuyết Chương 3: Phần cứng và Lưu trữ
### 2.1. Thiết bị Phần cứng
- **Vai trò:** Là nền tảng vật lý (móng nhà) để vận hành các phần mềm, mạng, quản trị và bảo mật. Hạ tầng phần cứng tốt giúp hệ thống chạy ổn định, an toàn và dễ dàng mở rộng.
- **Chu kỳ đầu tư:** Thường dự toán để thiết bị có thể đáp ứng nhu cầu sử dụng và mở rộng trong khoảng **5 năm**.
- **Máy chủ (Server):** 
  - Là trung tâm cung cấp dịch vụ, tài nguyên, xử lý và lưu trữ dữ liệu.
  - Cấu hình cần quan tâm: CPU, RAM, ổ cứng (SSD/HDD), nguồn dự phòng, cổng mạng, khả năng quản trị từ xa, khả năng mở rộng.
  - Có thể tự đầu tư quản lý (với dữ liệu nhạy cảm) hoặc thuê cloud (AWS, Azure...) tùy theo nhu cầu và ngân sách.
- **Máy trạm (Workstation/Client):** Phục vụ trực tiếp người dùng (văn phòng, đồ họa, phòng máy đào tạo...). Cấu hình phụ thuộc vào chức năng và nhóm người dùng.
- **Thiết bị ngoại vi:** Hỗ trợ nhập/xuất, tương tác (máy in, mạng, máy quét...).

### 2.2. Thiết bị Lưu trữ
- **Phân loại công nghệ lưu trữ phổ biến:**
  - **DAS (Direct Attached Storage):** Lưu trữ gắn trực tiếp, phù hợp cá nhân/doanh nghiệp nhỏ.
  - **NAS (Network Attached Storage):** Lưu trữ qua mạng, phù hợp chia sẻ file nội bộ cho doanh nghiệp vừa.
  - **SAN (Storage Area Network):** Mạng lưu trữ chuyên dụng, tốc độ cao, dùng cho trung tâm dữ liệu hoặc doanh nghiệp lớn.
- **Trung tâm dữ liệu (Data Center):** Nơi tập trung các thiết bị quan trọng (máy chủ, lưu trữ, mạng) với hệ thống làm mát và bảo mật cao.

## 3. Hướng dẫn Đồ án (Bước 0 - Xác định phạm vi đề xuất)
- **Mục tiêu:** Xác định rõ đề xuất đầu tư cái gì, cho đối tượng nào và trong bao lâu (ví dụ 5 năm). Tránh đầu tư thiết bị rời rạc mà phải hướng tới nâng cao năng lực hạ tầng.
- **Yêu cầu khảo sát hiện trạng doanh nghiệp:** 
  - Phải nắm được các thông tin cơ bản: Lịch sử, quy mô, cơ cấu tổ chức, quy trình hoạt động (không cần thanh tra chi tiết).
  - Từ hiện trạng, chỉ ra được các **vấn đề đang tồn tại** (Ví dụ: dữ liệu không đồng bộ giữa các chi nhánh, tỷ lệ rớt tốt nghiệp cao do không cảnh báo sớm).
- **Tính cấp thiết & Tính mới:**
  - **Tính cấp thiết:** Giải quyết được các vấn đề/nhược điểm trong hiện trạng.
  - **Tính mới:** Ứng dụng công nghệ mới (ví dụ AI, Data Warehouse, Data Lake) để tối ưu quy trình.
- **Cấu trúc Thuyết minh:** Dựa trên các form chuẩn (như của ĐHQG), cần trình bày rõ ràng, logic để các bên (chuyên môn, tài chính) dễ dàng kiểm tra.

## 📝 Bài tập & Đồ án
1. **Hoàn thành Bước 0 (Xác định phạm vi đề xuất):** 
   - Xác định doanh nghiệp, bối cảnh, vấn đề, và đề xuất lớp năng lực cần đầu tư.
   - Thống nhất các thông tin trên file đăng ký đồ án.
2. **Nộp bài tập:** 
   - Tạo thư mục bài tập "Xác định phạm vi đề xuất".
   - Nộp đường link bài làm theo hạn (deadline) của ngày hôm nay.
3. **Phân công nhóm:** Các nhóm (đặc biệt là nhóm 4, 8, 10, 11) nhanh chóng cập nhật đầy đủ bối cảnh doanh nghiệp và phân chia công việc cho thành viên.

## ⚠️ Yêu cầu & Nhắc nhở
- **Chốt đề tài:** Khuyến cáo các nhóm trao đổi kỹ và **chốt đề tài/lớp năng lực** ngay từ đầu. Hạn chế thay đổi sau này vì sẽ phải làm lại toàn bộ hồ sơ từ đầu, nếu sai lệch sẽ không được hỗ trợ thêm.
- **Trình bày tài liệu minh chứng:** Cần có link hoặc file báo cáo rõ ràng về hiện trạng doanh nghiệp.
- **Không chọn cả 5 lớp năng lực:** Tránh làm quá rộng, hãy chọn nội dung sát với chuyên ngành CNTT (Phần mềm, Dữ liệu, Quản trị, Bảo mật).
