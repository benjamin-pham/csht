# Buổi 6: Hướng dẫn thuyết minh Đồ án & Thực hành - Góp ý các nhóm

Tài liệu này tổng hợp các nhận xét, góp ý và hướng dẫn của cô Nguyễn Thị Anh Thư trong quá trình duyệt đề cương (Thuyết minh đề tài) của các nhóm cho môn học Cơ sở hạ tầng CNTT.

## 1. Nội dung bài giảng & Hướng dẫn kỹ thuật

### 1.1. Nguyên tắc viết Thuyết minh đề tài (Project Proposal)
- **Đi thẳng vào trọng tâm:** Đừng viết dài dòng, lan man hay lặp lại các lý thuyết chung chung (đặc biệt là các đoạn văn do AI sinh ra). Người đọc (khách hàng, hội đồng) cần thấy ngay:
  1. Vấn đề hiện tại (ngữ cảnh) là gì?
  2. Kỹ thuật/Công nghệ (giải pháp) đề xuất là gì?
  3. Giá trị đạt được (mục tiêu) là gì?
- **Khẳng định năng lực kỹ thuật:** Thuyết minh là để chứng minh nhóm IT có khả năng thực thi giải pháp công nghệ, chứ không phải đi diễn giải lại quy trình kinh doanh của khách hàng.
- **Tên đề tài:** Phải thể hiện rõ công nghệ áp dụng và bài toán kỹ thuật (Ví dụ: Đừng ghi chung chung là "Tổng hợp đa nguồn", hãy ghi cụ thể kỹ thuật sẽ dùng hoặc loại dữ liệu sẽ xử lý).

### 1.2. Xác định Mục tiêu và KPI / Độ đo (Metrics)
- **Đo lường sản phẩm phần mềm, không đo quy trình doanh nghiệp:** Các kỹ sư IT xây dựng phần mềm để hỗ trợ quy trình, nên KPI phải đánh giá chất lượng của chính phần mềm/hệ thống đó (VD: Thời gian phản hồi API, tỷ lệ downtime, độ chính xác của Model AI - Precision, Recall, F1-score...). KHÔNG sử dụng KPI của phòng ban kinh doanh (VD: Thời gian nhân viên xử lý hồ sơ, doanh thu tăng thêm...) vì IT không thể cam kết và kiểm soát năng suất của nhân sự.
- **Sử dụng chuẩn quốc tế:** Các độ đo (Metrics) phải là các công thức toán học chuẩn, đã được khoa học hoặc tổ chức quốc tế công nhận. 
- **Phải có tài liệu tham khảo (Citation):** Khi sử dụng một KPI/độ đo, bắt buộc phải trích dẫn (cite) nguồn tài liệu tham khảo gốc và giải thích rõ công thức tính toán.
- **Tính thống nhất:** Mục tiêu, Base-line (hiện trạng), và KPI to-be phải thống nhất xuyên suốt từ trên xuống dưới.

### 1.3. Phương pháp lập Bảng so sánh & Chọn phương án Kiến trúc (VD: Cloud vs On-premise vs Hybrid)
- **Không dùng AI liệt kê ưu/nhược điểm chung chung:** Các bảng so sánh toàn chữ, liệt kê chung chung các điểm mạnh/yếu không mang lại giá trị ra quyết định.
- **So sánh dựa trên Tiêu chí Mục tiêu:** Hãy đặt ra các tiêu chí (criteria) bắt buộc dựa trên vấn đề của doanh nghiệp (VD: Khả năng mở rộng nhanh, độ trễ thấp, tuân thủ bảo mật dữ liệu nhạy cảm).
- **Trực quan hóa:** Sử dụng các bảng có dấu tick (v), biểu đồ cột hoặc ký hiệu trực quan sao cho khách hàng nhìn vào là thấy ngay phương án nào đáp ứng đầy đủ các tiêu chí nhất. LUÔN phải có diễn giải lý do bên dưới bảng.

### 1.4. Xác định Phạm vi & Định hướng công nghệ AI
- **Giới hạn bài toán (Scope):** Không ôm đồm quá nhiều chức năng. Đối với AI, chỉ nên tập trung vào 1 ngách nhỏ để đào sâu kỹ thuật (VD: Thay vì làm cả chẩn đoán và đề xuất phác đồ điều trị cho nhiều bệnh, hãy tập trung vào chẩn đoán 1 loại bệnh cụ thể hoặc xử lý 1 loại dữ liệu y khoa).
- **Gợi ý ra quyết định, không thay thế con người:** Hệ thống AI hiện tại chỉ dừng ở mức độ "Hỗ trợ/Gợi ý" (Decision Support), người chịu trách nhiệm và ra quyết định cuối cùng vẫn là con người. Đừng cam kết phần mềm sẽ "tự động ra quyết định điều phối".
- **Limitation (Giới hạn đề tài):** Limitation là những điểm yếu kỹ thuật mà mô hình/phần mềm chưa giải quyết được (VD: Chạy còn chậm, cần tối ưu thêm), chứ không phải là liệt kê các chức năng chưa làm.

---

## 2. 📝 Bài tập & Đồ án

- **Phạm vi báo cáo:**
  - **Bài Đồ án:** Báo cáo từ Bước 1 đến Bước 4.
  - **Bài Thực hành:** Báo cáo từ Bước 0 đến Bước 4.
- **Lịch trình:** Các nhóm tiếp tục chỉnh sửa bản nháp (draft) báo cáo. **Buổi thứ 9** sẽ là buổi thi / vấn đáp cuối cùng.
- **Nhiệm vụ về nhà:** Tất cả các nhóm dựa trên góp ý của buổi 6 để tự sửa lại Thuyết minh, slide, đặc biệt là phần KPI, Bảng so sánh phương án kiến trúc, và Tên đề tài.

---

## 3. ⚠️ Yêu cầu & Nhắc nhở từ Cô

1. **Trình bày ngắn gọn:** Mỗi nhóm chỉ có **15 phút**, phải đi thẳng vào trọng tâm tóm tắt các bước, không được đọc rườm rà.
2. **Học hỏi lẫn nhau:** Các nhóm báo cáo sau BẮT BUỘC phải lắng nghe nhận xét của các nhóm trước để rút kinh nghiệm. Không được mắc lại các lỗi tương tự (như lỗi lập bảng so sánh bằng AI, lỗi nhầm KPI hệ thống thành KPI doanh nghiệp) mà cô đã cất công sửa ở các nhóm đầu.
3. **Hiểu rõ mình đang làm gì:** Sinh viên IT đi tư vấn và làm dự án phần mềm thì sản phẩm bàn giao là phần mềm/hệ thống công nghệ, do đó ngôn từ, mục tiêu, độ đo phải thể hiện được năng lực chuyên môn IT.
