# Buổi 5 - Phần mềm hệ thống, ứng dụng và Hướng dẫn đồ án/thực hành

## Yêu cầu & Nhắc nhở
- **Lịch học bù:** Buổi học tiếp theo trùng lịch nghỉ lễ nên sẽ dời sang **ngày 3/9 lúc 18h15**.
- **Buổi học tới (3/9):** Các nhóm sẽ báo cáo tiến trình đồ án và thực hành. Bắt buộc phải có đại diện nhóm tham gia để báo cáo và trao đổi.
- **Nộp bài tập:** 
  - Tạo folder "Bài tập lập kế hoạch giai đoạn 1" trên Drive và nộp bài. Deadline trong ngày.
  - **Lưu ý quản lý file trên Drive:** Để file báo cáo chính ở bên ngoài cùng. Các file nháp hoặc tài liệu tham khảo phải gom vào các folder riêng biệt (như `draft` hoặc `references`). Tránh để nhiều phiên bản lộn xộn khiến giảng viên không biết chấm file nào.
- **Sử dụng AI trong học tập:** Cảnh báo việc lạm dụng AI để vẽ biểu đồ quy trình nghiệp vụ. AI có thể vẽ đẹp nhưng thường sai logic, giảng viên có chuyên môn nhìn vào sẽ phát hiện ra và **bị trừ điểm rất nặng**. Sinh viên cần tự nắm vững nghiệp vụ và kiểm soát công cụ.
- **Cách trình bày báo cáo:** Khi bảo vệ đề xuất, hãy tập trung vào lý do chọn và lợi ích của lớp năng lực mình đầu tư. **Không so sánh dìm hàng** các lựa chọn khác để tránh tạo tranh cãi và bị hội đồng yêu cầu đổi phạm vi đề tài.

## Nội dung bài giảng: Chương 4 - Hệ thống phần mềm
- **Tổng quan:** Trước khi phát triển hệ thống phần mềm, cần phân tích hệ thống thông tin để xác định rõ 2 yếu tố: **Nhóm người dùng** là ai và phục vụ **Nghiệp vụ** gì.
- **Hệ điều hành & Phần mềm hệ thống:** 
  - Đóng vai trò lớp trung gian giữa phần cứng và ứng dụng, quản trị tài nguyên và cung cấp môi trường chạy.
  - Cần lên kế hoạch dự toán chi phí bản quyền (license) cho các phần mềm hệ thống khi lên dự án đầu tư.
- **Phần mềm ứng dụng:** 
  - Phục vụ nhu cầu nghiệp vụ của người dùng.
  - **Xu hướng công nghệ:** Ứng dụng trí tuệ nhân tạo (AI), xử lý dữ liệu lớn để nâng cấp từ hệ thống quản lý cơ bản sang hệ thống thông minh (VD: Hệ thống khuyến nghị cá nhân hóa trên sàn thương mại điện tử, AI hỗ trợ y khoa như phân tích ảnh CT, dự đoán bệnh lý).
- **Lớp kết nối điều phối (Middleware/Service):** Cung cấp năng lực dùng chung, kết nối và điều phối các thành phần trong một hệ thống lớn.
- **Ảo hóa & Container:** 
  - Ảo hóa (Máy ảo): Tính cách ly mạnh, an toàn nhưng tốn tài nguyên hơn.
  - Container: Nhẹ, khởi động nhanh, dễ triển khai nhưng lớp cách ly mỏng hơn. Việc lựa chọn phụ thuộc vào ngữ cảnh và nhu cầu sử dụng thực tế.
- **Quản lý vòng đời phần mềm:** Đảm bảo hệ thống tương thích tốt với nhau, tuân thủ pháp lý (bản quyền) để tránh rủi ro và các hình phạt.

## 📝 Bài tập & Đồ án

**Lưu ý chung:** Đồ án và Thực hành là **2 cột điểm riêng biệt**, yêu cầu nộp báo cáo và video thuyết trình độc lập. Sinh viên có thể chọn làm thực hành liên kết với đồ án (lấy một phần mềm trong dự án để phân tích sâu) hoặc làm hoàn toàn độc lập với nhau.

### 1. Đồ án môn học (Dự án đầu tư hạ tầng)
Cần thực hiện từ Bước 1 đến Bước 4:
- **Bước 1: Khảo sát hiện trạng:** Dùng dữ liệu thật (nếu không bảo mật) hoặc giả lập hiện trạng công ty. Phải đưa ra các chỉ số cụ thể (VD: số lượng sự cố, tỷ lệ backup thành công). Lưu ý trích dẫn tài liệu tham khảo phải từ các nguồn uy tín, không dùng nguồn internet trôi nổi, không kiểm chứng.
- **Bước 2: Nêu vấn đề & Rủi ro:** Trình bày các vấn đề và rủi ro nếu không đầu tư (ảnh hưởng đến vận hành, bảo mật, chiến lược mở rộng).
- **Bước 3: Xác lập mục tiêu & KPI:** Mục tiêu dự án phải đi kèm với các chỉ số KPI rõ ràng, đo lường được để phục vụ cho việc nghiệm thu sau này.
- **Bước 4: Xây dựng phương án kiến trúc To-Be:** Đưa ra 3 kịch bản, sau đó so sánh và **chốt lại kịch bản tối ưu nhất** để thực hiện chi tiết.

### 2. Bài thực hành (Phát triển phần mềm ứng dụng công nghệ mới)
- **Bước 0: Chuẩn bị thông tin:** Chọn một quy trình nghiệp vụ bất kỳ tại doanh nghiệp (có thể liên quan hoặc không liên quan đến đồ án), thu thập bối cảnh, vấn đề, ngân sách, nhân sự tham gia.
- **Bước 1: Đặt tên đề tài:** Nên đặt tên rõ ràng theo cấu trúc: Động từ + Đối tượng + Phạm vi + **Công nghệ mới áp dụng**.
- **Bước 2: Bối cảnh & Lý do chọn đề tài:** Mô tả hiện trạng, "điểm đau" (pain points) của quy trình hiện tại và lợi ích mà phần mềm mới tích hợp công nghệ mang lại.
- **Bước 3 & Bước 4:** Xác lập mục tiêu, KPI, đối tượng, phạm vi sử dụng, các giả định và ràng buộc.
- **Tiêu chí đánh giá:** Điểm cao hay thấp phụ thuộc vào việc sinh viên **hiểu rõ** bài toán, công nghệ áp dụng và cách triển khai như thế nào, không nên chỉ nêu tên công nghệ mới (như AI) một cách chung chung.
