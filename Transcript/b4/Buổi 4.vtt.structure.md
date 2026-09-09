# Buổi 4 - Hướng dẫn và Sửa bài báo cáo Đồ án & Thực hành

## 📝 Bài tập & Đồ án
### 1. Đồ án môn học (Dự án đầu tư cơ sở hạ tầng CNTT)
- **Sản phẩm yêu cầu:** 
  - Một file báo cáo đề xuất dự án.
  - Khi báo cáo trên lớp, trình bày dạng **One-pager (1 trang)** xác định rõ phạm vi đề xuất dự án.
  - Kèm theo danh sách tài liệu tham khảo.
- **Yêu cầu khi chọn phạm vi và lớp năng lực:**
  - Nêu ngắn gọn ngữ cảnh, hiện trạng công ty và vấn đề cần giải quyết.
  - Chọn đầu tư từ **2 đến 3 lớp năng lực** để giải quyết đúng một vấn đề cụ thể, tránh việc chọn cả 5 lớp năng lực một cách dàn trải, lan man.
  - Có thể giả lập một số thành phần (như phần cứng, mạng) đã có sẵn hoặc được kế thừa, để tập trung đầu tư phát triển mới các lớp năng lực khác (như nền tảng tích hợp, dữ liệu, bảo mật).
  - **Tính liền mạch:** Việc đầu tư các lớp năng lực phải có sự liên kết chặt chẽ với nhau, cùng hướng tới giải quyết một vấn đề lớn của doanh nghiệp. Tránh tình trạng mỗi lớp năng lực lại giải quyết một vấn đề rời rạc.
  - Trong thuyết minh, cần liệt kê các "công nghệ tiềm năng dự kiến triển khai" chứ không khẳng định tuyệt đối (vì chưa thực nghiệm). Nên chuẩn bị sẵn các công nghệ thay thế để phòng rủi ro.

### 2. Bài thực hành (Phát triển phần mềm ứng dụng công nghệ mới)
- **Yêu cầu:** Xây dựng thuyết minh hệ thống phần mềm ứng dụng một **công nghệ mới** (ví dụ: AI, Machine Learning, Deep Learning, Khai thác dữ liệu lớn, Blockchain, Web3...) để giải quyết một quy trình cụ thể.
- **Tính liên kết:** Khuyến khích bài thực hành bám sát và nằm trong phạm vi các lớp năng lực đã được đầu tư ở phần đồ án để tạo sự xuyên suốt (ví dụ: đầu tư hạ tầng dữ liệu ở Đồ án, sau đó làm phần mềm dự báo bằng AI ở bài Thực hành).
- **Cách thức thực hiện:**
  - Đi sâu tìm hiểu một công nghệ lõi mới, làm chủ công nghệ, tìm hiểu kỹ thuật và quy trình để **tự triển khai** (ví dụ tự build model AI/Chatbot riêng cho lĩnh vực của mình), thay vì chỉ đơn thuần sử dụng như một công cụ hay gọi các API có sẵn.
  - **Giới hạn phạm vi:** Chỉ chọn 1 quy trình, 1 nhóm người dùng cụ thể để giải quyết 1-2 vấn đề. Không nên quá tham lam giải quyết toàn bộ hệ thống.
  - Cần phân biệt rõ các khái niệm (ví dụ: Phân biệt giữa "Xuất báo cáo BI/Dashboard thông thường" và "Dự báo lưu lượng/tồn kho ứng dụng AI").

---

## 💡 Yêu cầu & Nhắc nhở qua phần nhận xét các nhóm
Trong quá trình sửa bài cho các nhóm (Nhóm 1, 3, 4, 5, 6, 7, 8, 9), cô nhấn mạnh các lỗi sai và lưu ý sau:

1. **Về cách trình bày:**
   - Cần đi thẳng vào trọng tâm: Trình bày ngay phạm vi, các lớp năng lực dự kiến đầu tư, hạng mục, hiện trạng. **Bỏ qua** các thông tin dài dòng về lịch sử phát triển hay quy mô tổ chức của công ty vì không cần thiết.
   - Sắp xếp thứ tự trình bày logic: Bắt đầu từ Đồ án (Ngữ cảnh -> Lớp năng lực đầu tư) -> Tài liệu tham khảo -> Bài thực hành (Phần mềm ứng dụng công nghệ mới trên hạ tầng đó).

2. **Về xác định bài toán & Công nghệ:**
   - **Tránh chọn bài toán quá rộng:** Ví dụ như xử lý dữ liệu video/camera phát hiện trộm là một bài toán rất lớn và phức tạp, cần xác định rõ chuẩn đầu vào, hành vi bất thường là gì.
   - **Sử dụng đúng công nghệ:** Không phải bài toán nào cũng dùng LLM. LLM chuyên về NLP (xử lý ngôn ngữ tự nhiên); nếu xử lý dữ liệu dạng Time-series thì nên đi theo nhánh Transformer chuyên biệt phù hợp.
   - **Phân biệt bài toán Phát hiện (Detect) và Giải thích:** Bài toán phát hiện bất thường (phân lớp) dễ khả thi hơn. Bài toán giải thích lý do vì sao xảy ra bất thường/gian lận là cực kỳ khó và liên quan đến yếu tố con người.
   - Nếu áp dụng công nghệ mới cho hệ thống như Chatbot CSKH, hãy giới hạn nó trả lời chuyên sâu về lĩnh vực cụ thể (ví dụ tài liệu pháp luật hoặc dịch vụ của đúng công ty đó) thay vì cố gắng làm đa năng đa nhiệm.
   - Việc chỉ kiểm tra tín hiệu có Internet hay không là bài toán IoT cơ bản (cảm biến nhận tín hiệu), không phải là bài toán Detect gian lận/tắt mạng bất thường phức tạp bằng AI.

3. **Lưu ý cập nhật bài làm (Trên Google Drive):**
   - Các nhóm làm sai yêu cầu phải họp nhóm thảo luận và chọn lại phạm vi, bài toán.
   - Khi cập nhật lại file báo cáo trên Drive, nếu nhóm có thay đổi/làm mới thì cần tạo file mới hoặc báo để cô biết. Đối với những file cô đã highlight (đánh dấu) tức là cô đã xem qua, nếu nhóm sửa đè lên (edit) mà không báo thì cô sẽ không biết để kiểm tra lại.
