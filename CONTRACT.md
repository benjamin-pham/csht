# TIÊU CHÍ CHUNG (Trình bày & Nộp bài)
- **Ngắn gọn, súc tích:** Tránh trình bày dài dòng, lan man. Phải viết ngắn gọn, cụ thể và đi thẳng vào vấn đề chính.
- **Ngôn ngữ chuyên nghiệp:** Trình bày thẳng trực tiếp vào vấn đề kỹ thuật. Tuyệt đối không dùng từ lóng, văn nói hoặc thành ngữ trong dấu ngoặc kép.
- **Tính liên kết:** Cần có sự liên kết chặt chẽ, logic và nhất quán giữa các phần trong bài báo cáo (ví dụ: yêu cầu bài toán phải khớp với mục tiêu, giải pháp kiến trúc phải đồng bộ với dự toán chi phí và KPI).
- **Logic trình bày:** Bắt đầu từ Đồ án (Ngữ cảnh -> Lớp năng lực đầu tư) $\rightarrow$ Tài liệu tham khảo $\rightarrow$ Bài thực hành (Phần mềm ứng dụng công nghệ mới trên hạ tầng đã đầu tư).
- **Bảo vệ phạm vi:** Đi thẳng vào trọng tâm kỹ thuật, bảo vệ chặt chẽ phạm vi đã chốt, không mở rộng hay sa đà giải thích quy trình kinh doanh. Tránh việc hội đồng yêu cầu đổi phạm vi sẽ phải làm lại từ đầu.

# TIÊU CHÍ KỸ THUẬT & NGHIỆP VỤ
- **Bản chất Kỹ thuật (IT):** Đồ án và bài thực hành là sản phẩm của dân kỹ thuật. Tuyệt đối dùng **KPI hệ thống IT** (Thời gian phản hồi, Uptime, Độ chính xác F1-score/Recall...), cấm dùng KPI của phòng kinh doanh (như doanh thu, thời gian xử lý nhân sự).
- **Minh chứng khoa học:** Các công thức đo lường KPI bắt buộc phải theo chuẩn quốc tế và **phải có trích dẫn (citation)** nguồn gốc công thức.
- **Giới hạn của AI:** Khẳng định rõ AI (nếu có) chỉ đóng vai trò **Hỗ trợ ra quyết định (Decision Support)**, con người là người quyết định cuối cùng. Không cam kết phần mềm tự động điều phối.
- **Limitation (Giới hạn đề tài):** Chỉ được nêu các điểm yếu về kỹ thuật (ví dụ: mô hình chạy còn chậm, độ trễ mạng cao), không được dùng mục này để chống chế "chưa làm kịp chức năng A, B".

# TIÊU CHÍ ĐÁNH GIÁ ĐỒ ÁN & THỰC HÀNH
- **Phạm vi hẹp & Sâu:** Chỉ chọn đầu tư từ **1 đến 3 lớp năng lực** (ưu tiên Ứng dụng, Tích hợp, Dữ liệu), không ôm đồm 5 lớp. Bài thực hành chọn đúng **1 ngách nhỏ, 1 quy trình** để giải quyết triệt để.
- **Cấm dùng AI vẽ biểu đồ phân tích:** Sinh viên tự phân tích nghiệp vụ. Biểu đồ do AI tự sinh thường sai logic nghiệp vụ chuyên môn và sẽ bị đánh rớt.
- **Trực quan hóa so sánh kiến trúc:** Khi so sánh các giải pháp kiến trúc (VD: Cloud vs On-premise), cấm dùng AI liệt kê bảng chữ ưu/nhược điểm chung chung. Phải tự thiết lập tiêu chí, dùng **dấu tick (v), biểu đồ trực quan**, và phải tự diễn giải lập luận ở dưới bảng.
- **Dự toán thực tế (BoQ/TCO):** Tổng chi phí phân bổ cho từng giai đoạn (mua sắm, triển khai, vận hành, bảo trì 3-5 năm) phải cộng lại khớp hoàn toàn với tổng ngân sách xin đầu tư.