# Kịch Bản Thuyết Trình Giai Đoạn 2 (Đồ Án & Thực Hành)

> **Hướng dẫn:** Kịch bản này được thiết kế để đọc trực tiếp (như MC đọc teleprompter) khi thuyết trình online. Các ý chính được bôi đậm và chia đầu dòng để dễ theo dõi bằng mắt khi đang nói. Tổng thời lượng khoảng 15 phút.

---

## 🎤 PHẦN 1: ĐỒ ÁN - NỀN TẢNG TÍCH HỢP VÀ DỮ LIỆU TẬP TRUNG (7.5 Phút)

Kính chào cô và các bạn. Tiếp nối các phân tích ở Giai đoạn 1, hôm nay nhóm em xin trình bày Giai đoạn 2 của Đồ án và Bài thực hành.

Phần 1 của bài thuyết trình sẽ tập trung vào Đồ án, mang tên: Đề xuất đầu tư Nền tảng Tích hợp Ứng dụng và Dữ liệu tập trung cho chuỗi Ways Station. Phần này bao gồm các bước từ 5 đến 8.

### Bước 5: Chuẩn hoá yêu cầu kỹ thuật

Trước tiên là Bước 5, Chuẩn hoá yêu cầu kỹ thuật. Nhóm đã cụ thể hóa các yêu cầu kỹ thuật thành 4 nhóm chính để làm cơ sở cho việc chào thầu và nghiệm thu sau này. Điểm quan trọng nhất ở đây là **mọi yêu cầu đều được chúng em liên kết ngược một cách chặt chẽ với các KPI ở Bước 3**. Điều này đảm bảo không có tính năng nào là dư thừa hay lãng phí.

- **Về Hiệu năng:** Hệ thống phải xử lý mượt mà hơn 2.000 kết nối đồng thời từ 34 chi nhánh. Tốc độ phản hồi API cam kết dưới 200 mili-giây. Ngoài ra, hạ tầng server tại chi nhánh phải đủ khả năng duy trì hoạt động bán hàng bình thường ngay cả khi đứt mạng internet trong suốt 4 giờ liền.
- **Về mức độ sẵn sàng:** Nhóm thiết kế trên nền tảng Cloud theo chuẩn Multi-zone, tự động phục hồi sự cố dưới 60 giây. Khả năng khôi phục dữ liệu luôn được đảm bảo dưới 15 phút.
- **Về Bảo mật:** Áp dụng đăng nhập một lần bằng Keycloak, và bắt buộc xác thực đa bước cho admin. Chúng em tuân thủ khắt khe Nghị định 13 của Chính phủ bằng cách: 100% dữ liệu cá nhân khách hàng được mã hóa chuẩn AES-256, và ẩn danh hóa hoàn toàn trước khi đưa lên Cloud.
- **Về Vận hành:** Chúng em tự động hóa quy trình triển khai bằng CI/CD, và thiết lập hệ thống giám sát tự động cảnh báo sự cố qua nền tảng chat nội bộ trong chưa tới 5 phút.

### Bước 6: Lập danh mục hạng mục đầu tư

Dựa trên kiến trúc kỹ thuật đó, chuyển sang Bước 6, chúng em lập danh mục hạng mục đầu tư chia làm 4 phần rõ rệt: Thiết bị cứng, Phần mềm bản quyền, Dịch vụ triển khai và Chi phí Cloud định kỳ.

- **Ưu tiên mã nguồn mở:** Điểm nhấn chiến lược của nhóm ở bước này là ưu tiên tối đa phần mềm mã nguồn mở để tiết kiệm chi phí mua bản quyền cho doanh nghiệp. Chúng em chọn sử dụng Kubernetes, Kafka, Keycloak và PostgreSQL thay vì các giải pháp Enterprise đắt đỏ ngoài thị trường.
- **Phân bổ phần cứng:** Về phần cứng, chúng em trang bị 34 bộ Edge Mini Server cho 34 chi nhánh, và 2 Server mạnh đặt tại Trụ sở chính để chứa dữ liệu nhạy cảm. Các cấu phần còn lại của hệ thống sẽ chạy hoàn toàn trên dịch vụ Cloud.

### Bước 7: Dự toán chi phí & Phân tích tài chính

Tiếp theo, chuyển sang Bước 7. Bài toán tài chính luôn là cốt lõi để Ban giám đốc ra quyết định đầu tư.

- **Chi phí ban đầu (CAPEX):** Nhóm ước tính tổng cần khoảng 1 phẩy 3 tỷ đồng. Trong đó, 564 triệu dành cho thiết bị phần cứng, 632 triệu cho dịch vụ triển khai và hơn 100 triệu thuê Cloud cho môi trường lập trình.
- **Chi phí vận hành năm đầu (OPEX):** Rơi vào khoảng 1 phẩy 12 tỷ đồng, bao gồm phí thuê Cloud, trả lương nhân sự vận hành, phí đường truyền mạng và phí bảo trì. Nhóm cũng đã tính toán và trích lập mức dự phòng rủi ro là 10 phần trăm. 
- **Tổng chi phí sở hữu (TCO):** Nhìn chung, tổng chi phí dự án trong chu kỳ 3 năm là khoảng 5 phẩy 2 tỷ đồng. 
- **Phân tích lợi ích (ROI):** Khi phân tích Lợi ích quy đổi tài chính, hệ thống này dự kiến mang lại giá trị khoảng 475 triệu một năm. Con số này đến từ việc giảm thất thoát doanh thu từ 3.8% xuống dưới 0.5%, và tiết kiệm hàng ngàn giờ làm báo cáo thủ công. Nhờ vậy, thời gian hoàn vốn của hệ thống ước tính chỉ là 2.75 năm — một con số rất khả thi và nằm gọn trong chu kỳ đầu tư.
- **Lý do chọn Hybrid Cloud:** Nếu dùng 100% On-Premise thì chi phí mua server ban đầu quá cao lên tới 2.8 tỷ; còn nếu dùng 100% Cloud thì chi phí duy trì hàng tháng đắt đỏ, và chi nhánh sẽ ngưng bán hàng ngay lập tức nếu rớt mạng. Vậy nên Hybrid Cloud là phương án duy nhất cân bằng được chi phí và đáp ứng 100% tiêu chí KPI kỹ thuật.

### Bước 8: Kế hoạch triển khai theo giai đoạn

Về kế hoạch thực thi ở Bước 8, dự án sẽ kéo dài 16 tuần - tương đương 4 tháng, và được chia làm 5 pha để quản trị rủi ro chặt chẽ.

- **Pha 1 & Pha 2:** Là xây dựng nền tảng mạng và bảo mật. Sau đó là dựng Cloud và cơ chế Backup.
- **Pha 3:** Là lập trình tích hợp luồng dữ liệu theo thời gian thực.
- **Pha 4 (Pilot):** Nhóm sẽ chuyển đổi dữ liệu và tiến hành chạy thử nghiệm - hay còn gọi là Pilot - ở 5 chi nhánh để đo lường thực tế trước khi nghiệm thu. 
- **Pha 5:** Mới là Go-live toàn bộ 29 chi nhánh còn lại.

- **Minh bạch ngân sách:** Điểm đáng lưu ý là bảng phân bổ dòng tiền đầu tư theo 5 pha này khớp hoàn toàn với tổng 1.3 tỷ mà nhóm đã dự toán ở bước 7. 
- **Quản trị rủi ro:** Đối với rủi ro như chậm tích hợp hệ thống phần mềm cũ, nhóm đã có kế hoạch dự phòng là thiết kế chuẩn giao tiếp chung và áp dụng chạy thử ngay từ khâu Pilot.

Tóm lại, phương án Hybrid Cloud với tổng chi phí 5.2 tỷ trong 3 năm là một khoản đầu tư chiến lược. Sau đây, em xin phép chuyển sang Phần 2 của bài thuyết trình: Bài Thực hành, để đi sâu vào hệ thống Mô hình AI dự báo lưu lượng khách hàng. Hệ thống AI này sẽ chạy trực tiếp trên nền tảng tích hợp mà chúng ta vừa xây dựng.

---

## 🎤 PHẦN 2: THỰC HÀNH - MÔ HÌNH AI DỰ BÁO LƯU LƯỢNG (7.5 Phút)

### Bước 5: Yêu cầu nghiệp vụ và yêu cầu hệ thống

Ở phần Thực hành, bắt đầu với Bước 5, chúng em tập trung đi sâu vào phân hệ AI Forecasting. Hệ thống này đóng vai trò là một **Hệ thống hỗ trợ ra quyết định (DSS)**, mang lại 3 giá trị cốt lõi làm động lực đầu tư:
- **Thứ nhất, tối ưu hóa điều phối nhân lực:** Hỗ trợ lên lịch ca làm việc linh hoạt, hạn chế dư thừa nhân sự lúc vắng và đảm bảo đủ người lúc cao điểm.
- **Thứ hai, hỗ trợ cung ứng:** Dự báo sát thực tế giúp luân chuyển hàng hóa kịp thời, tránh tình trạng đứt gãy hoặc tồn kho quá hạn.
- **Thứ ba, định hướng tiếp thị:** Nhận diện chính xác khung giờ thấp điểm để chạy khuyến mãi, tránh lãng phí ngân sách marketing vào giờ đã quá tải.

Để đạt được những giá trị đó, nhóm đã chuẩn hóa các yêu cầu hệ thống:
- **Về mặt nghiệp vụ:** Phần mềm này phục vụ 4 luồng công việc chính: Xem dự báo khách hàng, Nhận cảnh báo tự động khi phát hiện khung giờ quá tải, Chạy luồng trích xuất dữ liệu tự động hàng đêm, và Giám sát tình trạng hệ thống.
- **Về mặt chức năng, hệ thống chia làm 3 Module cụ thể:** Thứ nhất là Data Pipeline lo việc trích xuất dữ liệu. Thứ hai là AI Engine, dùng để huấn luyện thuật toán từ 12 tháng dữ liệu lịch sử, xuất ra dự báo cho 7 ngày tiếp theo. Và thứ ba là API Service để phân phối số liệu dự báo đó ra màn hình cho người quản lý xem.
- **Về các yêu cầu phi chức năng:** Chúng em cũng ánh xạ trực tiếp từ KPI tổng. Ví dụ, thời gian trích xuất khối lượng dữ liệu khổng lồ cho cả 34 chi nhánh phải chạy xong trong dưới 30 phút, API phải trả kết quả lên màn hình dưới 500 mili-giây, và quan trọng nhất là vẫn phải đảm bảo ẩn danh hoàn toàn dữ liệu người dùng.

### Bước 6: Thiết kế giải pháp và kiến trúc tổng thể

Sang Bước 6, với hệ thống này, quy trình làm việc tại chi nhánh sẽ được tự động hóa tới 90%.

- **Quy trình luân chuyển dữ liệu:** Cứ 1 giờ sáng hệ thống sẽ tự động rút dữ liệu từ chi nhánh, 2 giờ sáng AI chạy dự báo, và sáng sớm hệ thống sẽ quét, tự động gửi Email cảnh báo cho quản lý nếu phát hiện hôm nay sẽ có khung giờ quá tải. Từ đó, người Quản lý chi nhánh chỉ việc mở màn hình lên, nhìn vào số liệu để ra quyết định xếp ca nhân viên và chuẩn bị kho bãi. Mô hình AI ở đây đóng vai trò là một Hệ thống hỗ trợ ra quyết định.
- **Về kiến trúc Cloud-Native 3 tầng:**
  - **Tầng Trình bày:** Có Dashboard cho Quản lý và Grafana cho team IT.
  - **Tầng Ứng dụng:** Dùng API Gateway, dùng FastAPI, và quan trọng nhất là dùng Apache Airflow để điều phối toàn bộ luồng luân chuyển dữ liệu.
  - **Tầng Dữ liệu:** Dùng PostgreSQL làm kho chứa, dùng MLflow để lưu trữ các phiên bản mô hình AI, và S3 để lưu dữ liệu thô. Tất cả dữ liệu đều được mã hóa chuẩn TLS (Transport Layer Security) khi truyền tải và mã hóa AES-256 khi lưu trữ.

### Bước 7 & Bước 8: Kế hoạch triển khai và Tổ chức nhân sự

Tiếp theo là Bước 7 và Bước 8, nói về tiến độ và tổ chức nhân sự.

- **Tiến độ dự án:** Dự án phần mềm AI này sẽ được thực thi trong 15 tuần, chia làm 5 pha bài bản: bắt đầu từ Khảo sát và làm sạch dữ liệu, Thiết kế kiến trúc, Viết Code và Train AI, Kiểm thử, cho đến Triển khai thực tế.
- **Ma trận phối hợp nhân sự:** Đội ngũ dự án bao gồm Quản lý dự án, Kỹ sư Dữ liệu, Kỹ sư AI, Kỹ sư Backend, Kỹ sư hạ tầng DevOps, QC và Người dùng chủ chốt. Chúng em lập một Ma trận phối hợp rất rõ ràng để không ai bị giẫm chân lên nhau. Chẳng hạn: Kỹ sư Dữ liệu sẽ chịu trách nhiệm chính về chất lượng Data ở Pha 1, trong khi Kỹ sư AI sẽ chịu trách nhiệm phần thuật toán ở Pha 3.
- **Cơ chế quản trị rủi ro:** Mọi lỗi liên quan đến việc dữ liệu bị sai lệch phải được giải quyết trong dưới 24 giờ. Đồng thời, nghiêm cấm tuyệt đối việc đội dự án tự ý phát triển thêm tính năng nếu không có phiếu yêu cầu thay đổi chính thức.

### Bước 9: Dự toán chi phí và phương án tài chính

Cuối cùng là Bước 9: Dự toán chi phí cho dự án AI.

- **Chi phí đầu tư ban đầu:** Tổng chi phí cho 15 tuần phát triển phần mềm này là khoảng 663 triệu đồng. Trong đó phần lớn là chi phí trả lương cho nhân sự kỹ thuật. Chi phí bản quyền phần mềm hoàn toàn bằng 0 vì chúng ta dùng 100% tài nguyên nguồn mở.
- **Chi phí vận hành năm đầu tiên:** Ước tính khoảng 325 phẩy 8 triệu đồng, bao gồm tiền thuê server, thuê sức mạnh tính toán Card Đồ họa GPU để huấn luyện lại mô hình mỗi tháng, và phí nhân sự bảo trì.
- **Tổng ngân sách:** Cộng thêm 10% quỹ dự phòng rủi ro, tổng ngân sách sở hữu năm đầu tiên của phân hệ AI này rơi vào khoảng 1 phẩy 08 tỷ đồng.
- **Tính minh bạch ngân sách:** Đặc biệt, nhóm đã lập bảng đối chiếu để kiểm chứng tính minh bạch của dòng tiền. Tổng ngân sách phân bổ theo 5 pha của kế hoạch triển khai cộng lại, vừa khít với 663 triệu đồng dự toán. Điều này minh chứng cho tính logic và khả thi của toàn bộ dự án.

### Kết luận

Kính thưa cô và các bạn. Toàn bộ Hệ thống Tích hợp nền tảng và Mô hình AI dự báo này được nhóm thiết kế theo tư duy Cloud-Native hiện đại, ưu tiên tính thực tiễn và tối ưu hóa chi phí. Khả năng mở rộng của kiến trúc này có thể lên tới 50 chi nhánh mà không sợ hệ thống bị vỡ, rất phù hợp với quy mô và định hướng phát triển trong tương lai của doanh nghiệp Ways Station.

Nhóm em xin phép kết thúc phần trình bày Giai đoạn 2 tại đây. Rất mong nhận được sự góp ý và câu hỏi từ cô cùng các bạn để nhóm có thể hoàn thiện đề tài tốt hơn. Em xin chân thành cảm ơn!
