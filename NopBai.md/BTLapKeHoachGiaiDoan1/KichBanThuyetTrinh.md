# Kịch Bản Thuyết Trình Giai Đoạn 1 (Đồ Án & Thực Hành)

> **Hướng dẫn:** Kịch bản này được thiết kế để đọc trực tiếp (như MC đọc teleprompter) khi thuyết trình online. Các ý chính được bôi đậm và chia đầu dòng để dễ theo dõi bằng mắt khi đang nói. Tổng thời lượng khoảng 15 phút.

---

## 🎤 PHẦN 1: ĐỒ ÁN - ĐỀ XUẤT ĐẦU TƯ CƠ SỞ HẠ TẦNG CNTT (7.5 Phút)

Kính chào cô và các bạn. Hôm nay, nhóm 5 xin phép trình bày báo cáo Giai đoạn 1 của Đồ án và Bài thực hành.

Phần 1 của bài thuyết trình sẽ tập trung vào Đồ án, mang tên: Đề xuất đầu tư Nền tảng Tích hợp Ứng dụng và Dữ liệu tập trung cho chuỗi Ways Station. Phần này bao gồm các bước từ 1 đến 4.

### Bước 1: Khảo sát hiện trạng hạ tầng (AS-IS)

Đầu tiên là Bước 1, nhóm đã khảo sát hiện trạng của chuỗi Ways Station với quy mô 34 chi nhánh đa dịch vụ. Chúng em nhận diện được 3 điểm nghẽn cốt lõi bằng các số liệu định lượng cụ thể:
- **Tích hợp & Vận hành:** 34 chi nhánh đang sử dụng 8 hệ thống rời rạc hoàn toàn, tỉ lệ tích hợp tự động là **0%**. Mọi giao tiếp đều làm thủ công qua Zalo hoặc sổ giấy.
- **Dữ liệu & Quyết định:** Không có kho dữ liệu chung. Việc làm báo cáo Excel tiêu tốn khoảng **2.500 giờ công mỗi năm**, độ trễ dữ liệu lên tới **48 giờ** và sai lệch đối soát là **3,8%**.
- **Bảo mật & Định danh:** Dữ liệu cá nhân khách hàng như Face ID hay ảnh CCCD đang được gửi qua Zalo cá nhân của nhân viên, hoàn toàn không được mã hóa. Tỉ lệ sao lưu dữ liệu cục bộ chỉ thành công **47%**.

### Bước 2: Nêu vấn đề và rủi ro nếu không đầu tư (Why Now?)

Chuyển sang Bước 2, từ những điểm nghẽn vừa nêu, nếu doanh nghiệp không đầu tư nâng cấp hạ tầng ngay bây giờ, sẽ đối mặt với 3 rủi ro cực kỳ nghiêm trọng:
- **Rủi ro vận hành:** Việc thiếu nền tảng tích hợp khiến hệ thống dễ sập vào giờ cao điểm. Quá trình phát hiện sự cố mất từ 4-8 giờ, gây gián đoạn bán hàng và lãng phí hàng ngàn giờ công cho việc đối soát.
- **Rủi ro chiến lược:** Độ trễ dữ liệu 48 giờ khiến Ban giám đốc ra quyết định chậm trễ, dẫn đến lãng phí nguyên liệu và sai sót trong việc xếp ca nhân viên. Đồng thời, không thể bán chéo dịch vụ vì khách hàng không có tài khoản định danh duy nhất.
- **Rủi ro tuân thủ:** Đây là rủi ro lớn nhất. Việc lưu trữ PII phân tán vi phạm nghiêm trọng **Nghị định 13 của Chính phủ**. Doanh nghiệp có thể bị phạt tới 5% tổng doanh thu và tổn hại danh tiếng.

### Bước 3: Xác lập mục tiêu và KPI hạ tầng (TO-BE)

Để giải quyết triệt để các vấn đề trên, ở Bước 3, nhóm đã thiết lập một bộ KPI kỹ thuật theo chuẩn quốc tế, gắn kết chặt chẽ qua Ma trận Truy vết:
- **Giải quyết vấn đề vận hành:** Nhóm đặt KPI tính sẵn sàng của hệ thống phải đạt **Uptime 99.99%** theo chuẩn Google, và thời gian phục hồi sự cố **MTTR dưới 30 phút**.
- **Giải quyết vấn đề dữ liệu:** Rút ngắn độ trễ dữ liệu xuống **dưới 5 giây** (Data Freshness), cung cấp dữ liệu thực thời để hỗ trợ mô hình AI dự báo với sai số **MAPE dưới 15%**.
- **Giải quyết rủi ro bảo mật:** Cam kết **100% dữ liệu nhạy cảm được mã hóa AES-256** theo chuẩn NIST, và mục tiêu điểm khôi phục **RPO dưới 15 phút**.

### Bước 4: Xây dựng phương án kiến trúc TO-BE

Sang Bước 4, để đạt được bộ KPI khắt khe này mà vẫn đảm bảo chi nhánh bán hàng bình thường khi đứt mạng internet, nhóm đã phân tích và quyết định chọn **Kiến trúc Hybrid Cloud (Lai)** thay vì 100% On-Premise hay 100% Cloud.
- **Hợp nhất ứng dụng:** Chúng em sẽ đặt API Gateway trên Cloud và cài đặt bộ đệm Edge Cluster tại chi nhánh. Nhờ vậy, rớt mạng vẫn tính tiền được, có mạng dữ liệu sẽ tự đồng bộ, đảm bảo **Uptime 99.99%**.
- **Hợp nhất dữ liệu:** Xây dựng Data Lakehouse trên Cloud kết hợp luồng dữ liệu thời gian thực CDC, đảm bảo độ trễ **dưới 5 giây**, tạo tiền đề cho hệ thống AI.
- **Tuân thủ bảo mật tuyệt đối:** Các dữ liệu nhạy cảm nhất (như Face ID) sẽ được lưu trữ tại máy chủ vật lý ở Trụ sở (On-Premise) và mã hóa 100%. Dữ liệu đưa lên Cloud đều được ẩn danh hóa. Qua đó tuân thủ 100% Nghị định 13 của Chính phủ.

Phương án Hybrid Cloud này chính là nền tảng vững chắc nhất. Tiếp theo, em xin phép chuyển sang Phần 2 để đi sâu vào hệ thống AI sẽ chạy trên nền tảng này.

---

## 🎤 PHẦN 2: THỰC HÀNH - MÔ HÌNH AI DỰ BÁO LƯU LƯỢNG (7.5 Phút)

### Bước 0 & Bước 1: Bối cảnh và Tên đề tài

Ở phần Thực hành, nhóm em lựa chọn đề tài: **Ứng dụng mô hình AI Time-Series Forecasting dự báo lưu lượng khách hàng đa chi nhánh**. Hệ thống sẽ giải quyết bài toán dự báo thủ công, chậm trễ hiện tại bằng cách tự động hóa luồng dữ liệu và triển khai trên hạ tầng Cloud của Ways Station.

### Bước 2: Bối cảnh và Động lực đầu tư

Chuyển sang Bước 2, tại sao lại là mô hình AI này? Vì cách làm thủ công hiện tại khiến việc phân bổ nhân sự hoàn toàn theo cảm tính. Khung giờ cao điểm thì thiếu người, vắng khách thì lại dư người, lãng phí chi phí vận hành.

Việc đầu tư hệ thống AI này đóng vai trò là một **Hệ thống hỗ trợ ra quyết định (DSS)**, mang lại 3 giá trị thiết thực:
- **Tối ưu hóa nhân lực:** Hỗ trợ điều phối ca làm việc linh hoạt, hạn chế dư thừa nhân viên lúc vắng khách.
- **Tối ưu hóa cung ứng:** Dự báo sát thực tế giúp luân chuyển hàng hóa kịp thời.
- **Hỗ trợ Marketing:** Nhận diện các khung giờ thấp điểm để chạy khuyến mãi một cách hiệu quả, tránh kích cầu nhầm vào giờ cao điểm.

Bên cạnh đó, việc chạy hệ thống này trên Cloud giúp doanh nghiệp chuyển đổi từ chi phí CAPEX sang OPEX linh hoạt, tự động mở rộng tài nguyên và cam kết Uptime 99.9%.

### Bước 3: Mục tiêu và KPI Kỹ thuật

Đến Bước 3, thay vì chia KPI theo tầng hạ tầng như Đồ án, chúng em phân tách mục tiêu của Bài thực hành thành 2 nhóm KPI độc lập rất rõ ràng:

- **Nhóm 1 là KPI cho Mô hình AI:**
  - Nhóm cam kết độ sai số **MAPE phải dưới 10%**, tức là độ chính xác trên 90%, cải thiện ít nhất 10% so với phương pháp thủ công.
  - Mức sai số tuyệt đối **MAE không quá 3 khách** trong một khung giờ.
  - Độ chính xác khi nhận diện giờ cao điểm **Precision đạt trên 85%**. Và thời gian suy luận của AI **dưới 200 mili-giây**.

- **Nhóm 2 là KPI cho Phần mềm và Vận hành:**
  - Thời gian phản hồi **API dưới 500 mili-giây** cho 95% lượng truy cập.
  - **Uptime đạt 99.9%**. Tỷ lệ lỗi API **dưới 0.1%**.
  - Đặc biệt, về chất lượng dữ liệu, **99.5% dữ liệu** phải được nạp thành công vào kho, và do AI chạy theo lô hàng đêm, độ trễ dữ liệu được cam kết là **dưới 24 giờ**.

Các KPI này được chúng em ánh xạ trực tiếp thành tiêu chí nghiệm thu bàn giao cho 5 giai đoạn phát triển, gắn liền với trách nhiệm của từng nhân sự từ Kỹ sư Dữ liệu, Kỹ sư AI đến Kỹ sư DevOps.

### Bước 4: Đối tượng, Phạm vi và Giới hạn

Cuối cùng là Bước 4, về phạm vi triển khai.
- Nhóm chỉ tập trung vào luồng tích hợp dữ liệu từ máy POS lên Cloud, huấn luyện AI và xuất dữ liệu qua API. 
- Nhóm sẽ **không can thiệp** vào các phần mềm quản lý kho hay ERP hiện tại, mà chúng sẽ giao tiếp qua API.
- Đặc biệt, hệ thống AI chỉ đóng vai trò **hỗ trợ tham khảo**, quyết định điều phối cuối cùng vẫn là của con người. Và mô hình sẽ cần huấn luyện lại hàng tháng để duy trì độ chính xác khi xu hướng khách hàng thay đổi.

### Kết luận

Kính thưa cô và các bạn, toàn bộ nội dung của Giai đoạn 1 đã làm rõ hiện trạng, thiết lập các mục tiêu đo lường được và định hình phương án kiến trúc tổng thể cho cả Đồ án Hạ tầng và Bài thực hành AI. 

Nhóm em xin phép kết thúc phần trình bày tại đây. Rất mong nhận được sự góp ý từ cô và các bạn. Em xin chân thành cảm ơn!

