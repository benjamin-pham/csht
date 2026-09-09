# Buổi 5: Hệ thống phần mềm & Hướng dẫn Đồ án - Thực hành

## 1. Nội dung bài giảng (Chương 4: Phần mềm hệ thống & Phần mềm ứng dụng)

- **Phần mềm hệ thống:**
  - Là lớp trung gian giữa phần cứng và phần mềm ứng dụng, cung cấp môi trường chạy ứng dụng, quản trị tài nguyên mạng và thiết bị.
  - Mục tiêu: Giúp duy trì, vận hành ổn định và cung cấp dịch vụ cho hệ thống.
  - Ví dụ: Hệ điều hành, chương trình hỗ trợ backup, antivirus, v.v.
  - *Lưu ý khi đầu tư:* Cần xác định danh sách phần mềm hệ thống phải cài đặt để dự toán kinh phí mua bản quyền (license) và vận hành. Phải đảm bảo tính tương thích giữa các phần mềm để tránh xung đột hệ thống.

- **Phần mềm ứng dụng:**
  - Phục vụ trực tiếp cho nhu cầu nghiệp vụ của người dùng tại đơn vị (ứng dụng văn phòng, Web/Mobile App chuyên biệt).
  - *Xu hướng hiện tại:* Xây dựng hệ thống phần mềm hỗ trợ nghiệp vụ thông minh hơn thay vì chỉ dừng ở mức độ quản lý dữ liệu thông thường. Việc tích hợp các công nghệ mới (AI, Dữ liệu lớn) giúp hệ thống có khả năng dự đoán, cá nhân hóa, đưa ra khuyến nghị (VD: Hệ thống gợi ý trên sàn TMĐT, phân tích ảnh y khoa hỗ trợ bác sĩ chẩn đoán bệnh).
  - *Quy trình phát triển:* Cần xác định rõ nhóm người dùng và quy trình nghiệp vụ. Sinh viên nên tự phân tích, thiết kế luồng xử lý thực tế thay vì dùng AI tạo biểu đồ tự động (do AI thường vẽ sai nguyên tắc, sai logic nghiệp vụ chuyên môn, dễ bị đánh rớt).

- **Lớp kết nối điều phối (Middleware/Service):**
  - Cung cấp năng lực dùng chung để kết hợp, tích hợp, điều phối trong hệ thống lớn. Bao gồm các chương trình chạy nền cung cấp chức năng qua mạng lưới (network).
  - Định hướng phát triển hệ thống thành các dịch vụ (services) để người dùng dễ sử dụng.

- **Ảo hóa và Container:**
  - *Ảo hóa (Virtual Machine):* Chạy trên phần cứng thật, tính cách ly mạnh, dễ snapshot và backup, nhưng tốn tài nguyên và hoạt động nặng hơn.
  - *Container:* Đóng gói ứng dụng để chạy nhẹ, khởi động nhanh, triển khai đồng nhất, tuy nhiên lớp cách ly mỏng hơn. Tùy vào ngữ cảnh và nhu cầu (như cần tính độc lập) để lựa chọn giải pháp cho phù hợp.

- **Quản lý vòng đời phần mềm & Tuân thủ pháp lý:**
  - Cần kế hoạch vòng đời: phát triển, triển khai, vận hành, giám sát, cập nhật vá lỗi và kết thúc/thay thế.
  - *Rủi ro pháp lý:* Bắt buộc phải dự toán chi phí mua bản quyền phần mềm đầy đủ cho doanh nghiệp, nếu sử dụng phần mềm lậu sẽ đối mặt với rủi ro pháp lý và mức phạt rất nặng.

---

## 2. 📝 Bài tập & Đồ án

### Đồ án môn học (Dự án đầu tư cơ sở hạ tầng)
**Nhiệm vụ:** Lập kế hoạch Giai đoạn 1 (từ Bước 1 đến Bước 4).
- **Bước 1: Khảo sát hiện trạng**
  - Đánh giá hiện trạng qua dữ liệu thật (nếu có công bố) hoặc **giả lập** (nếu dữ liệu thực tế bảo mật).
  - Nêu các chỉ số đo lường (SLI downtime, tỷ lệ backup thành công, tỷ lệ lỗ hổng, mức tăng trưởng người dùng...).
  - *Yêu cầu:* Các chỉ số đo lường phải được trích dẫn từ tài liệu tham khảo gốc có kiểm chứng (sách, bài báo khoa học, chuyên gia), không lấy số liệu trôi nổi trên mạng.
- **Bước 2: Nêu vấn đề và rủi ro không đầu tư**
  - Dựa trên hiện trạng, chỉ ra các "pain points", rủi ro, thiệt hại nếu không đầu tư và lợi ích mang lại khi triển khai.
- **Bước 3: Xác lập mục tiêu và KPI**
  - Đưa ra cam kết mục tiêu của dự án kèm KPI có thể đo lường (VD: tăng độ chính xác lên bao nhiêu %). Nếu doanh nghiệp không có bộ tiêu chí riêng, phải dùng các KPI chuyên môn.
- **Bước 4: Xây dựng phương án kiến trúc To-Be**
  - Chuẩn bị 3 kịch bản kiến trúc. Phải có sự so sánh và **chốt lại kịch bản phù hợp nhất** để thực hiện chi tiết.
- *Lưu ý quan trọng:* Trình bày thẳng vào lợi ích của lớp năng lực/thành phần mình đã chọn đầu tư (VD: Nhóm 2, Nhóm 3). Không nên chê bai hoặc so sánh các lớp khác để tránh tạo tranh luận và bị Hội đồng bắt bẻ, ép đổi phạm vi đề tài.

### Bài thực hành (Xây dựng phần mềm ứng dụng công nghệ mới)
**Nhiệm vụ:** Lập thuyết minh đề tài xây dựng phần mềm (có thể chọn nghiệp vụ độc lập hoặc lấy từ công ty trong đồ án).
- **Bước 0: Chuẩn bị đầu vào**
  - Xác định quy trình nghiệp vụ, bối cảnh, vấn đề, đối tượng người dùng, các ràng buộc ngân sách.
- **Bước 1: Đặt tên đề tài**
  - Đặt tên thể hiện rõ quy trình nghiệp vụ cần giải quyết và công nghệ mới áp dụng (VD: "Ứng dụng trí tuệ nhân tạo vào hệ thống...").
- **Bước 2: Bối cảnh, lý do chọn đề tài**
  - Nêu rõ vấn đề hiện tại của nghiệp vụ và khả năng giải quyết khi áp dụng công nghệ mới.
- **Bước 3 & Bước 4: Mục tiêu, Đối tượng, Phạm vi, Ràng buộc**
  - Cụ thể hóa KPI, xác định giới hạn chức năng, giả định hạ tầng.
- *Lưu ý quan trọng:* Việc ứng dụng công nghệ mới phải đi sâu vào kỹ thuật, hiểu rõ công cụ, nền tảng và lợi ích mang lại. Đưa công nghệ vào chỉ để nêu tên chung chung sẽ không được đánh giá cao.

---

## 3. 🚨 Yêu cầu & Nhắc nhở

1. **Lịch học bù:** Do tuần sau nghỉ Lễ 2/9, lớp sẽ học bù vào **ngày 3/9 (Thứ Năm), lúc 18h15**. Những sinh viên trùng lịch có thể xem lại video, nhưng mỗi nhóm bắt buộc phải có đại diện tham gia để báo cáo tiến độ và nhận xét.
2. **Quy cách nộp bài tập (Cực kỳ quan trọng):**
   - Các nhóm không được để tràn lan nhiều phiên bản file trong thư mục nộp bài.
   - Tập hợp các file phụ, tài liệu tham khảo vào thư mục riêng (VD: `refs`, `resources`).
   - Phải có **MỘT file báo cáo chính ở ngoài cùng** để cô dễ dàng tải về và chấm điểm (điểm quá trình được đánh giá qua các bài báo cáo này).
3. **Tuyệt đối không dùng AI vẽ biểu đồ phân tích:** Sinh viên phải tự phân tích nghiệp vụ. Các biểu đồ tự động vẽ bằng công cụ AI thường sai nguyên tắc, không hợp lý về logic nghiệp vụ chuyên môn và sẽ bị đánh rớt.
4. **Bảo vệ phạm vi đề tài:** Khi trình bày, không mở ra các giải pháp/hướng đi khác ngoài phạm vi đã chọn, tránh việc Hội đồng yêu cầu thay đổi phạm vi đề tài (nếu phạm vi đổi, toàn bộ mục tiêu, phương pháp phải làm lại từ đầu rất tốn thời gian).
