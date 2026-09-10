# BÀI LÀM: XÁC ĐỊNH PHẠM VI ĐỀ XUẤT

## 1. Khảo sát tổng quan về doanh nghiệp

**Tên thương hiệu:** Ways Station

**Lịch sử phát triển:** 
Từ những cơ sở kinh doanh dịch vụ đơn lẻ, Ways Station đã phát triển thành một hệ sinh thái tổ hợp dịch vụ thể thao, giải trí và không gian làm việc tập trung. Quá trình phát triển gắn liền với việc mở rộng liên tục các loại hình dịch vụ theo nhu cầu thị trường.

**Quy mô và phạm vi hoạt động:**
- Hệ thống sở hữu hơn 30 chi nhánh phân bố tại nhiều quận trọng điểm trên địa bàn Thành phố Hồ Chí Minh.
- Cung cấp đa dạng dịch vụ bao gồm phòng máy tính, bida, thể hình, sân cầu lông và không gian làm việc chung.
- Đa số các chi nhánh vận hành xuyên suốt 24/7.

**Cơ cấu tổ chức và quy trình hoạt động:**
- Doanh nghiệp không vận hành dưới một pháp nhân duy nhất mà theo mô hình chuỗi các hộ kinh doanh độc lập cùng thương hiệu.
- Quy trình phục vụ khách hàng, đăng ký hội viên và quản lý ca làm việc hiện đang phụ thuộc nhiều vào các thao tác thủ công, chứng từ giấy và tin nhắn cá nhân.
- Các bộ phận chính bao gồm Phòng Nhân sự, Phòng Điều phối, Kho hàng, Quản lý chi nhánh, Quản lý ca và Nhân viên vận hành.

## 2. Phạm vi dự án tổng quát (Project scope one-pager)

**Tên dự án:** Đầu tư nền tảng ứng dụng và nền tảng dữ liệu cho hệ thống Ways Station
**Đơn vị thụ hưởng:** Chuỗi hệ thống Ways Station
**Lớp năng lực đầu tư:** Lớp (4) App & Integration Platform và Lớp (5) Data Platform

**Bối cảnh và vấn đề:**
Hiện tại Ways Station sở hữu hơn 30 chi nhánh với các mô hình dịch vụ đa dạng (Gaming, Gym, Billiards, Cầu lông, Ways Hub). Các ứng dụng đặt chỗ và phần mềm quản lý tại từng mảng dịch vụ đang vận hành độc lập, dẫn đến tình trạng dữ liệu không đồng bộ, xung đột lịch đặt sân/máy và gây khó khăn cho trải nghiệm đa dịch vụ của khách hàng.

**Mục tiêu đầu tư:**
- **Lớp năng lực ứng dụng và tích hợp (App & Integration Platform):** Đầu tư xây dựng hệ thống nền tảng nhằm kết nối, đồng bộ hóa và tích hợp toàn bộ các ứng dụng hiện có (Gym FaceID App, phần mềm quản lý quán Net, hệ thống đặt sân Cầu lông, Bida, Hub) thông qua cổng giao tiếp ứng dụng (API Gateway) và trục sự kiện (Event Bus) theo thời gian thực.
- **Lớp năng lực nền tảng dữ liệu (Data Platform):** Triển khai kho dữ liệu tập trung và quy trình tự động thu thập, đồng bộ dữ liệu giao dịch từ toàn bộ chi nhánh. Thiết lập các bảng điều khiển trực quan để hỗ trợ công tác quản trị và ra quyết định kinh doanh.

**Đối tượng phục vụ và phạm vi tác động:**
- **Khách hàng:** Sử dụng một định danh duy nhất để truy cập toàn bộ dịch vụ trong hệ sinh thái.
- **Nhân viên vận hành chi nhánh:** Sử dụng giao diện phần mềm hợp nhất, loại bỏ quy trình lập báo cáo thủ công và đối soát giấy tờ.
- **Ban điều hành chuỗi:** Giám sát hiệu quả hoạt động, tỷ lệ khai thác dịch vụ và doanh thu của từng chi nhánh thông qua dữ liệu trực quan theo thời gian thực.

## 3. Danh sách tài liệu khảo sát và tham khảo

**A. Tài liệu nội bộ của doanh nghiệp:**
1. Tài liệu nghiệp vụ vị trí GIỮ XE: Quy trình xử lý khi khách làm mất thẻ xe, cơ chế lập biên bản và bàn giao.
2. Tài liệu nghiệp vụ vị trí PHỤC VỤ BIDA: Phân biệt loại bàn, tiêu chuẩn nhiệt độ bàn, quy trình vệ sinh thiết bị.
3. Tài liệu nghiệp vụ vị trí PHỤC VỤ CẦU LÔNG.
4. Tài liệu nghiệp vụ vị trí PHỤC VỤ GYM: Nội quy phòng tập, quy trình hỗ trợ khách.
5. Tài liệu nghiệp vụ vị trí PHỤC VỤ NET: Hướng dẫn chế biến món, danh mục và giá hàng hóa.
6. Tài liệu nghiệp vụ vị trí THU NGÂN GYM: Quy trình dẫn khách tham quan, tư vấn gói tập, tạo hội viên và lấy định danh khuôn mặt (Face ID); danh mục vật tư phòng tập.
7. Tài liệu nghiệp vụ vị trí THU NGÂN NET + BIDA: Bảng giá hàng hóa, công thức tính giá món, nội quy phòng, quy trình kiểm tra phòng.
8. Tài liệu nghiệp vụ vị trí THU NGÂN NET + HUB: Quy định phòng Hub, danh mục hàng bán, hàng miễn phí và hàng cho mượn.

**B. Nguồn công khai chính chủ từ doanh nghiệp:**
9. Trang chủ chính thức Ways Station: [https://www.waysstation.vn/](https://www.waysstation.vn/)
10. Trang dịch vụ không gian học tập và làm việc Ways Station Hub: [https://hub.waysstation.vn/](https://hub.waysstation.vn/) (Giá dịch vụ, địa điểm, giờ hoạt động, tiện ích).
11. Danh sách chi nhánh Ways Station: [https://diachi.waysstation.vn/](https://diachi.waysstation.vn/)
12. Cổng tuyển dụng chính thức: [https://diachi.ways.vn/tuyendung](https://diachi.ways.vn/tuyendung) (Mô tả quy trình bàn giao ca và báo cáo số lượng bàn - máy theo khung giờ).
13. Thông báo tuyển dụng Quản lý ca (waysstation.vn): Phân cấp quản lý; yêu cầu lập báo cáo trên Google Drive, Excel.
14. Tuyển thời vụ ngắn hạn: [https://td.ways.vn/tv](https://td.ways.vn/tv) (Cơ chế bố trí nhân sự linh hoạt theo ca trống).
15. Tin khai trương chi nhánh Lê Lợi và Quang Trung (waysstation.vn): Mốc phát triển và mục tiêu mở rộng chuỗi.

**C. Nguồn thứ cấp (đối chiếu quy mô và pháp lý):**
16. Tra cứu thông tin hộ kinh doanh (MaSoThue): [https://masothue.com/083097012959-ho-kinh-doanh-ways-station-dh](https://masothue.com/083097012959-ho-kinh-doanh-ways-station-dh) (Căn cứ xác định mô hình đa hộ kinh doanh).
17. Hồ sơ nhà tuyển dụng (VietnamWorks): [https://www.vietnamworks.com/nha-tuyen-dung/ways-station-c409679](https://www.vietnamworks.com/nha-tuyen-dung/ways-station-c409679) (Quy mô 30+ chi nhánh trên 11 quận).
18. Hồ sơ nhà tuyển dụng (CareerViet): [https://careerviet.vn/vi/nha-tuyen-dung/ways-station.35AA15F2.html](https://careerviet.vn/vi/nha-tuyen-dung/ways-station.35AA15F2.html)
19. Tin tuyển dụng (Vieclam24h): [https://vieclam24h.vn/danh-sach-tin-tuyen-dung-ways-station-ntd5989966p122.html](https://vieclam24h.vn/danh-sach-tin-tuyen-dung-ways-station-ntd5989966p122.html) (Ghi nhận 32 chi nhánh; địa chỉ trụ sở).
20. Tin tuyển dụng 2024 (YBOX / JobOKO): [https://ybox.vn](https://ybox.vn) (Quy mô 25 chi nhánh; phân loại doanh nghiệp vừa).
21. Danh sách hệ thống phòng gym (Eagle Fitness): [https://www.eaglefitness.vn/ways-station/](https://www.eaglefitness.vn/ways-station/) (Quy mô 22 chi nhánh và khu vực phân bố).
22. Tổng hợp đánh giá khách hàng (Trustindex): [https://www.trustindex.io/reviews/waysstation.vn](https://www.trustindex.io/reviews/waysstation.vn) (Phản hồi thực tế về dịch vụ Hub và chất lượng vận hành).
