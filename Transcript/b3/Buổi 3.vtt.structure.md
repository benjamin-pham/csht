# Buổi 3: Khảo Sát Kiến Trúc Hạ Tầng, Phần Cứng & Lưu Trữ

## 1. Sửa Bài Tập & Góp Ý Đồ Án (Nhóm 6 - Giao Hàng Nhanh)
- **Đánh giá chung:** Bài làm khảo sát các lớp năng lực của nhóm khá tốt, đã tìm hiểu được các thành phần, thiết bị công nghệ phổ biến. Tuy nhiên, bài tập trên lớp chỉ yêu cầu tìm hiểu khái quát, không bắt buộc phải đặt vào ngữ cảnh một doanh nghiệp cụ thể (trừ khi đó là doanh nghiệp làm đồ án).
- **Yêu cầu đối với đề xuất thuyết minh đồ án:** 
  - Các sinh viên phải đóng vai trò là người đưa ra giải pháp, kế hoạch đầu tư hạ tầng cho doanh nghiệp.
  - Cần phải giải thích lý do lựa chọn công nghệ/thiết bị, đưa ra các luận điểm về hiệu quả và lợi ích mang lại nhằm thuyết phục nhà đầu tư phê duyệt dự án.

## 2. Hướng Dẫn & Yêu Cầu Về Đồ Án Môn Học
- **Phạm vi đầu tư & Lựa chọn lớp năng lực:**
  - **Không nên ôm đồm cả 5 lớp năng lực.** Cô khuyến nghị chỉ nên chọn từ **1 đến 3 lớp năng lực** để nghiên cứu sâu. 
  - Với đặc thù ngành CNTT, sinh viên nên tập trung vào **lớp 2 (Ứng dụng), lớp 4 (Tích hợp) và lớp 5 (Dữ liệu)**. Đặc biệt lớp dữ liệu (Data Platform) là nền tảng cốt lõi không thể thiếu cho các công nghệ mới hiện nay như Trí tuệ nhân tạo (AI), Data Lake, Data Warehouse.
  - **Giả lập hạ tầng:** Sinh viên có quyền giả lập phần cứng và mạng của doanh nghiệp đã ổn định, chỉ tập trung đề xuất đầu tư cho các thành phần: **Phần mềm, Quản trị và Bảo mật**.
- **Cách đặt vấn đề (Tính cấp thiết & Tính mới):**
  - Phải khảo sát bối cảnh doanh nghiệp, xác định các nút thắt/nhu cầu hiện tại (VD: Dữ liệu chưa đồng bộ giữa các chi nhánh, tỷ lệ sinh viên rớt tốt nghiệp cao do không có cảnh báo sớm...).
  - **Tính cấp thiết:** Việc đầu tư hệ thống/nền tảng sẽ giải quyết triệt để vấn đề thực tế nào của doanh nghiệp.
  - **Tính mới:** Áp dụng các công nghệ mới (như AI dự đoán/cảnh báo sớm) vào hệ thống thay vì chỉ quản lý dữ liệu thông thường.
- **Quy định đổi đề tài:** 
  - Hạn chế tối đa việc đổi đề tài vì sẽ mất thời gian làm lại từ đầu. 
  - Nếu bắt buộc đổi, hạn chót là **buổi sửa bài đồ án (buổi 7 hoặc 8)**. Phải chốt đề tài trước ngày thi vấn đáp.

## 3. Lý Thuyết Chương 3: Phần Cứng & Thiết Bị Lưu Trữ
### Vai trò của Phần cứng
- Là tập hợp các thiết bị vật lý tạo nên nền tảng vận hành cốt lõi cho toàn bộ hệ thống CNTT (xử lý, lưu trữ, kết nối mạng, duy trì hoạt động).
- Trong dự án, phần cứng thường chiếm kinh phí đầu tư lớn nhất. Do đó, cần dự toán kỹ lưỡng cả chi phí mua sắm lẫn **chi phí vận hành**.
- Thiết bị đầu tư cần đáp ứng nhu cầu tăng trưởng mở rộng của doanh nghiệp trong một chu kỳ dài hạn (thường tính toán cho chu kỳ **5 năm**).

### Máy chủ (Server)
- **Đặc điểm:** Hệ thống máy tính cấu hình cao, hoạt động 24/7, có tính dự phòng tốt. Đảm nhiệm việc chạy các ứng dụng chung, lưu trữ dữ liệu tập trung, quản lý cổng thông tin, hệ thống email, hoặc chạy các model AI.
- **Tiêu chí lựa chọn:** Đánh giá kỹ về CPU, RAM, ổ cứng (SSD/HDD), khả năng dự phòng (nguồn điện, mạng) và ngân sách.
- **Xu hướng:** Nhiều tác vụ nặng hiện nay được chuyển lên hệ thống máy chủ Cloud, tuy nhiên với các hệ thống đòi hỏi an toàn và bảo mật cao (như ngân hàng, dữ liệu quốc gia), doanh nghiệp vẫn tự đầu tư và quản lý hệ thống máy chủ riêng.

### Máy trạm (Workstation / Client)
- **Đặc điểm (trong mô hình LAN-Server):** Máy tính phục vụ trực tiếp cho người dùng cuối trong quá trình làm việc, học tập.
- **Tiêu chí đầu tư:** Tùy thuộc vào nhóm đối tượng người dùng (ví dụ: máy tính cho đồ họa/kỹ thuật cần cấu hình mạnh, phòng máy thực hành tại trường học cần cấu hình đồng nhất để dễ quản lý, tối ưu chi phí).

### Thiết bị lưu trữ
- **Các mô hình lưu trữ phổ biến theo quy mô:**
  - **DAS (Direct Attached Storage):** Lưu trữ gắn trực tiếp, chi phí thấp, phù hợp cho cá nhân hoặc doanh nghiệp nhỏ.
  - **NAS (Network Attached Storage):** Lưu trữ qua mạng, dùng chung để chia sẻ file, phù hợp cho doanh nghiệp vừa và nhỏ.
  - **SAN (Storage Area Network):** Mạng lưu trữ chuyên dụng, tốc độ truy xuất cực cao, nhiều lớp bảo mật và dự phòng, dùng cho các doanh nghiệp lớn (trung tâm dữ liệu, ngân hàng).

### Trung tâm dữ liệu (Data Center)
- Là nơi quy tụ và bảo vệ các thiết bị quan trọng nhất (máy chủ, hệ thống SAN, thiết bị mạng lõi) kèm theo các hệ thống phụ trợ (điều hòa nhiệt độ, điện dự phòng, an ninh vật lý) nhằm đảm bảo hoạt động liên tục, không gián đoạn.

## 📝 Bài tập & Đồ án
**1. Bài tập về nhà tuần này: "Xác định phạm vi đề xuất" (Bước 0 của Đồ án)**
- **Yêu cầu nộp bài:**
  - Thư ký/Đại diện nhóm tạo folder bài tập có tên **"Xác định phạm vi đề xuất"** và nộp link lên hệ thống eLearning trước thời hạn (trong ngày hôm nay).
  - Lập bảng phân công công việc cụ thể cho từng thành viên trong nhóm dựa trên đề tài đã đăng ký.
- **Nội dung thực hiện Bước 0:**
  - **Khảo sát doanh nghiệp:** Tìm hiểu lịch sử, quy mô, cơ cấu tổ chức và các quy trình hoạt động cốt lõi của doanh nghiệp lựa chọn.
  - **Xác định tính cấp thiết & tính mới:** Nêu rõ những khó khăn, vấn đề hiện tại của doanh nghiệp, từ đó làm cơ sở lập luận cho việc đầu tư hệ thống/ứng dụng công nghệ mới.
  - **Xác định phạm vi đầu tư:** Trả lời ngắn gọn 3 ý chính: **Đầu tư lớp năng lực nào? Cho đối tượng/phòng ban nào? Định hướng sử dụng trong bao lâu (chu kỳ 5 năm)?**

**2. Yêu cầu bổ sung cho các nhóm:**
- **Nhóm 4 & Nhóm 11:** Phải chốt thông tin và cập nhật nội dung đề tài ngay trong tối nay.
- **Nhóm 1, 7, 8, 10:** Yêu cầu nhanh chóng bổ sung phần "khảo sát bối cảnh doanh nghiệp và vấn đề hiện tại" vào file đăng ký đề tài để cô duyệt.
