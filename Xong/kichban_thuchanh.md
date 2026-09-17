## Phân công

| Người | Slide | Nội dung | Thời lượng |
|:---|:---:|:---|:---:|
| Phạm Minh Mẫn — Nhóm trưởng | 1–2 | Mở đầu, giới thiệu đề tài, phân công | 2'00" |
| Đặng Nguyễn Minh Anh | 3–4 | Bối cảnh, hiện trạng, tính cấp thiết | 3'00" |
| Trần Văn Phây | 5–6 | Mục tiêu tổng quát, KPI (Key Performance Indicator) nhóm A | 3'00" |
| Huỳnh Thị Kiều Uyên | 7–8 | KPI nhóm B, ánh xạ KPI theo giai đoạn | 3'00" |
| Trần Việt Đức | 9–10 | Phạm vi, giới hạn AI (Artificial Intelligence), yêu cầu nghiệp vụ | 3'00" |
| Nguyễn Đức Huy | 11–12 | Yêu cầu chức năng và phi chức năng | 3'00" |
| Vũ Duy | 13–14 | Quy trình TO-BE, pipeline, kiến trúc | 3'00" |
| Trần Anh Tú | 15–16 | Kế hoạch triển khai, nhân sự, dự toán | 3'00" |
| Lê Quang Đạt | 17–18 | Rủi ro, kiểm thử, vận hành, nghiệm thu | 3'00" |
| Phạm Minh Mẫn — Nhóm trưởng | 19 | Kết luận | 1'00" |

## Phạm Minh Mẫn · Slide 1 (90 giây)

> "Kính chào cô. Em là Phạm Minh Mẫn, nhóm trưởng nhóm 5. Nhóm em xin báo cáo **bài thực hành**: Ứng dụng mô hình học sâu và mô hình nền tảng chuỗi thời gian (Deep Learning & Time-Series Foundation Models) để dự báo lưu lượng khách hàng đa chi nhánh, triển khai áp dụng cho chuỗi Ways Station.
>
> Điểm đặc biệt ngay từ tên đề tài là nhóm em đặt tên theo **nhánh kỹ thuật** chứ không khóa chặt vào một thuật toán cụ thể nào. Bởi lẽ với bài toán dữ liệu, nếu chưa chạy thực nghiệm thì sẽ chưa biết phương pháp nào mang lại kết quả tối ưu nhất. Nhóm dự kiến sẽ chạy benchmark song song ít nhất 4 thuật toán khác nhau thuộc nhánh này, bao gồm cả Time-Series Foundation Models, LSTM, Prophet và ARIMA để tìm ra mô hình dự báo chính xác và ổn định nhất."

## Phạm Minh Mẫn · Slide 2 (30 giây)

> "Về đội ngũ thực hiện, nhóm em vẫn gồm 9 thành viên. Mỗi bạn sẽ phụ trách trình bày sâu vào một hạng mục chuyên môn và trực tiếp báo cáo đúng phần việc mà mình đã đảm nhiệm. Toàn bộ 9 bạn đều tham gia xuyên suốt cả video thực hành này và video đồ án môn học."

## Đặng Nguyễn Minh Anh · Slide 3 (90 giây)

> "Em là Đặng Nguyễn Minh Anh, em xin trình bày bối cảnh và hiện trạng của doanh nghiệp.
>
> Bài toán trọng tâm mà nhóm em nhắm vào là **quy trình điều phối nguồn lực tại chi nhánh**, một quy trình hiện đang phải phụ thuộc hoàn toàn vào cảm tính của người quản lý.
>
> Thứ nhất, dữ liệu giao dịch POS (Point of Sale) tại 34 chi nhánh hiện đang được xử lý thủ công và lưu trữ phân tán, dẫn đến độ trễ khi tổng hợp dữ liệu lên tới 48 đến 72 giờ.
>
> Thứ hai, việc thiếu công cụ dự báo định lượng gây ra hệ lụy trực tiếp: vào giờ cao điểm thì thường xuyên thiếu nhân lực phục vụ, đứt gãy cung ứng vật tư khiến khách hàng phải chờ đợi lâu. Ngược lại, vào giờ thấp điểm lại dư thừa nhân lực do phân bổ ca cố định, gây lãng phí nghiêm trọng chi phí vận hành (OPEX).
>
> Thứ ba, hệ thống máy chủ hiện tại ở chi nhánh không có đủ năng lực tính toán để thực hiện việc làm sạch dữ liệu, trích xuất đặc trưng và huấn luyện các mô hình học máy phức tạp trên tập dữ liệu lịch sử lớn. Nguyên nhân gốc rễ của mọi vấn đề này là do doanh nghiệp **chưa có một công cụ dự báo định lượng theo chuỗi thời gian**."

## Đặng Nguyễn Minh Anh · Slide 4 (90 giây)

> "Vậy vì sao bài toán dự báo này lại mang tính cấp thiết cao? Lý do là vì **một kết quả dự báo duy nhất có thể phục vụ đồng thời cho bốn quy trình nghiệp vụ của ba phòng ban khác nhau**.
>
> Cụ thể, Phòng Điều phối sẽ dùng kết quả dự báo để xếp lịch ca làm việc dựa trên dữ liệu thay vì cảm tính. Bộ phận Kho hàng sẽ dùng nó để lập kế hoạch luân chuyển hàng hóa kịp thời, tránh tình trạng đứt gãy cung ứng hoặc tồn đọng hàng quá hạn. Bộ phận Marketing dùng dự báo để nhận diện chính xác các khung giờ thấp điểm nhằm tung chương trình kích cầu, thay vì đốt ngân sách khuyến mãi vào những giờ đã kín chỗ. Cuối cùng, quản lý chi nhánh dùng nó để lường trước các đợt khách đột biến, từ đó duy trì chất lượng dịch vụ.
>
> Khả năng phục vụ đa phòng ban này chính là lý do cốt lõi khiến nhóm tin rằng nền tảng dự báo này mang lại giá trị đủ lớn để doanh nghiệp quyết định đầu tư."

> ⚠ **Đặng Nguyễn Minh Anh:** đây chính là điều cô hướng dẫn ở Buổi 6 — phải tối đa hóa giá trị của thông tin dự báo, không gói gọn vào một phòng ban.

## Trần Văn Phây · Slide 5 (90 giây)

> "Em là Trần Văn Phây, em xin trình bày về mục tiêu tổng quát và cấu trúc bộ KPI của dự án.
>
> Mục tiêu tổng quát của hệ thống là: Xây dựng một nền tảng tự động thu thập dữ liệu giao dịch từ máy POS, thực hiện huấn luyện mô hình học máy phân tích chuỗi thời gian, và sau đó cung cấp kết quả dự báo lưu lượng khách qua các API chuyên dụng để phục vụ nội bộ.
>
> Để đo lường mức độ thành công, bộ KPI được tách bạch thành **hai nhóm chỉ số hoàn toàn độc lập**. Nhóm A tập trung đo lường năng lực và độ chính xác toán học của mô hình AI. Nhóm B tập trung đo lường tính sẵn sàng và chất lượng kỹ thuật của bản thân hệ thống phần mềm trong môi trường vận hành thực tế.
>
> Đặc biệt, bài thực hành này **không sử dụng cấu trúc KPI phân rã theo tầng hạ tầng** giống như bên đồ án nền tảng. Lý do là vì hai bài báo cáo tập trung đo lường hai đối tượng khác nhau: một bên đo năng lực nền tảng hạ tầng, một bên đo lường chất lượng của sản phẩm phần mềm chạy trên nền tảng đó."

## Trần Văn Phây · Slide 6 (90 giây)

> "Đi vào chi tiết Nhóm A, chúng ta có 5 chỉ số đo lường mô hình.
>
> Chỉ số lõi là **MAPE (Mean Absolute Percentage Error)**, được thiết kế theo lộ trình siết dần: **yêu cầu dưới 15% tại thời điểm nghiệm thu Pilot, và siết chặt xuống dưới 10% sau go-live 3 tháng**. Lý do nhóm chia làm hai mốc là vì tại thời điểm Pilot, dữ liệu mới được migrate nên chưa phản ánh đủ chu kỳ mùa vụ; sau 3 tháng, khi dữ liệu đầy đủ và mô hình đã qua hai chu kỳ tái huấn luyện, mức sai số mới có thể đạt ngưỡng 10%.
>
> Để đối chứng, baseline của phương pháp Moving Average 7 ngày cho MAPE khoảng 25-30%, còn ARIMA rơi vào khoảng 18-22%. Nhóm cam kết mô hình AI sẽ cải thiện tối thiểu 10% so với baseline tốt nhất này.
>
> Các chỉ số bổ trợ bao gồm MAE (Mean Absolute Error) không được lệch quá 3 khách mỗi khung giờ, độ chính xác (Precision) nhận diện đúng giờ cao điểm phải từ 85%, độ trễ suy luận (Inference Latency) dưới 200 mili-giây. Cuối cùng, **chỉ số A.5 là độ ổn định đa ngữ cảnh** — yêu cầu mức chênh lệch MAPE không quá 10% giữa các chi nhánh có đặc thù khác nhau như gym, gaming và hub. Mọi công thức đo lường đều tham chiếu từ Scikit-learn và các tài liệu chuẩn quốc tế."

## Huỳnh Thị Kiều Uyên · Slide 7 (90 giây)

> "Em là Huỳnh Thị Kiều Uyên, em xin trình bày chi tiết về nhóm KPI B.
>
> Nhóm B dùng để đo lường chất lượng phần mềm và khâu vận hành, bao gồm 7 chỉ số. Em xin nhấn mạnh ba chỉ số quan trọng nhất:
>
> Thứ nhất, **Thời gian phản hồi API (Response Time) ở phân vị 95 không được vượt quá 500 mili-giây**. Đây là ngưỡng đo end-to-end (từ đầu đến cuối), đã bao hàm luôn 200 mili-giây thời gian suy luận thuần của mô hình AI ở chỉ số A.4.
>
> Thứ hai, **Uptime dịch vụ API phải đạt từ 99,9%**, nghĩa là thời gian gián đoạn tối đa không quá 43,2 phút mỗi tháng.
>
> Thứ ba, **Độ đầy đủ của dữ liệu (Data Completeness) phải đạt từ 99,5%** và **Độ tươi của dữ liệu batch (Batch Data Freshness) phải dưới 24 giờ**, với yêu cầu hoàn tất đồng bộ lúc 1 giờ sáng mỗi ngày.
>
> Các chỉ số còn lại bao gồm: Thời gian chạy trọn vẹn tiến trình batch cho 34 chi nhánh phải dưới 30 phút, tỷ lệ lỗi HTTP 5xx phải dưới 0,1%, và Thời gian trung bình phát hiện sự cố (MTTD) phải dưới 15 phút — một bước tiến lớn so với mức 4 đến 8 giờ hiện nay do phụ thuộc nhân viên báo lỗi thủ công qua Zalo. Mọi độ đo đều sử dụng khung chuẩn quốc tế như Google SRE hay ISO/IEC 25012."

## Huỳnh Thị Kiều Uyên · Slide 8 (90 giây)

> "Nhằm bảo đảm tính xuyên suốt từ khâu thiết kế đến lúc nghiệm thu, nhóm em đã **gắn kết chặt chẽ từng KPI vào từng giai đoạn triển khai dự án**.
>
> Cụ thể: Giai đoạn Khảo sát được nghiệm thu bằng chỉ số độ đầy đủ dữ liệu (B.4). Giai đoạn Thiết kế kiến trúc được nghiệm thu bằng chuẩn RESTful của hợp đồng API (API Contract). Giai đoạn Phát triển (Dev) được nghiệm thu trực tiếp bằng các chỉ số cốt lõi của mô hình như MAPE (A.1), Precision (A.3), độ trễ suy luận (A.4) và độ ổn định đa ngữ cảnh (A.5).
>
> Tiếp đó, Giai đoạn Kiểm thử đóng gói được đánh giá bằng độ trễ API (B.1) và tỷ lệ lỗi (B.6). Giai đoạn Triển khai (Go-live) được nghiệm thu bằng Uptime hệ thống (B.3) và độ tươi dữ liệu (B.5).
>
> Đặc biệt, sau Go-live 3 tháng sẽ có thêm một mốc kiểm tra độc lập: MAPE lúc này phải đạt chuẩn dưới 10% như đã cam kết. Điều quan trọng nhất trong chiến lược này là: **Mỗi giai đoạn chỉ được ký biên bản chuyển sang pha tiếp theo nếu đã hoàn thành đúng và đủ KPI của giai đoạn đó.**"

## Trần Việt Đức · Slide 9 (90 giây)

> "Em là Trần Việt Đức, em xin trình bày về phạm vi và giới hạn của đề tài.
>
> Về phạm vi thực hiện: Hệ thống tập trung xây dựng luồng tích hợp dữ liệu từ máy POS tại chi nhánh lên Cloud, sau đó huấn luyện mô hình dự báo chuỗi thời gian, và cuối cùng cung cấp kết quả qua RESTful API cũng như hiển thị trên dashboard nội bộ.
>
> Về những phần nằm ngoài phạm vi: Nhóm sẽ **không** can thiệp hay sửa đổi kiến trúc của phần mềm quản lý kho, phần mềm nhân sự hay hệ thống ERP hiện hữu; chúng chỉ giao tiếp với nhau qua API. Đặc biệt, bài toán **không bao gồm việc đầu tư cơ sở hạ tầng Lớp 4 và Lớp 5** (như hệ thống Kubernetes, cụm Kafka, IAM Keycloak), vì phần này thuộc đề tài đồ án môn học. Bài thực hành này giả định mô hình chạy trên một môi trường Cloud độc lập, không phụ thuộc vào việc đồ án nền tảng có được phê duyệt hay không.
>
> Về giới hạn vai trò của AI: Nền tảng chỉ đóng vai trò **hỗ trợ ra quyết định (Decision Support System)**; quyết định điều phối lịch làm việc cuối cùng vẫn hoàn toàn thuộc về con người. Đồng thời, độ chính xác của AI sẽ giảm sút khi gặp các sự kiện đột biến chưa từng có trong quá khứ (như bão lũ), do đó mô hình bắt buộc phải tái huấn luyện định kỳ hàng tháng.
>
> Về phương án dự phòng: Nhóm **chỉ cam kết đạt ngưỡng chỉ số, không cam kết phải sử dụng một thuật toán duy nhất**. Nhóm sẽ benchmark song song tối thiểu 4 phương pháp. Nếu khi Pilot mà chưa có phương pháp nào đạt MAPE dưới 15%, hệ thống sẽ phát hành ở chế độ beta không bắt buộc nghiệm thu, dùng Moving Average làm lớp phòng ngự (fallback) và lập Change Request gia hạn."

## Trần Việt Đức · Slide 10 (90 giây)

> "Về yêu cầu nghiệp vụ, nhóm em đã đặc tả chi tiết dưới dạng Use Case, bao gồm đầy đủ các tác nhân, luồng xử lý chính và các luồng ngoại lệ. Em xin nêu bật hai Use Case cốt lõi nhất.
>
> **BR-01 — Xem dự báo lưu lượng khách:** Tác nhân chính là quản lý chi nhánh. Người dùng đăng nhập, chọn chi nhánh và khung thời gian cần xem. Hệ thống sẽ gọi API và trả về biểu đồ dự báo. Tuy nhiên, ở luồng ngoại lệ, nếu API gặp lỗi hoặc chưa kịp sinh dự báo mới, hệ thống sẽ fallback hiển thị dữ liệu lưu lượng thực tế của đúng ngày này tuần trước để người dùng vẫn có cơ sở tham khảo.
>
> **BR-03 — Tự động hóa Pipeline dữ liệu:** Đây là luồng ngầm của hệ thống. Đúng 1 giờ sáng, Cronjob sẽ tự động kết nối vào POS DB, trích xuất dữ liệu batch, làm sạch, chuẩn hóa và nạp vào Data Warehouse. Nếu rớt kết nối mạng, hệ thống tự động retry tối đa 3 lần; nếu vẫn thất bại, hệ thống sẽ đẩy cảnh báo khẩn cấp cho Kỹ sư dữ liệu xử lý.
>
> Ba Use Case quan trọng còn lại bao gồm: BR-02 (Cảnh báo giờ cao điểm tự động), BR-04 (Giám sát trạng thái hệ thống dành cho Kỹ sư IT), và BR-05 (Lập kế hoạch nhập hàng theo dự báo dành cho Bộ phận Kho)."

## Nguyễn Đức Huy · Slide 11 (90 giây)

> "Em là Nguyễn Đức Huy, em xin trình bày về các Yêu cầu chức năng (FR). Có tổng cộng 13 yêu cầu được chia đều cho ba module chính.
>
> **Module thứ nhất là Data Pipeline (Thu thập và xử lý dữ liệu):** Module này đảm nhiệm việc trích xuất tự động dữ liệu từ POS qua kênh kết nối mã hóa, làm sạch và chuẩn hóa schema, sau đó nạp vào kho dữ liệu theo luồng ELT. Nó cũng chịu trách nhiệm ghi lại log chi tiết về tỷ lệ thành công của mỗi lần chạy batch.
>
> **Module thứ hai là AI Forecasting Engine (Động cơ dự báo):** Yêu cầu mô hình phải được huấn luyện trên tối thiểu 12 tháng dữ liệu lịch sử. Nó phải dự báo theo khung 1 giờ cho 7 ngày tiếp theo, đồng thời tự động gán nhãn cảnh báo 'cao điểm' nếu lưu lượng dự kiến vượt 1,5 lần trung bình. Module cũng quản lý phiên bản mô hình trên MLflow, hỗ trợ tính năng rollback. Đặc biệt, yêu cầu **FR-13** bắt buộc hệ thống phải cho phép benchmark song song ít nhất 4 thuật toán trên cùng bộ độ đo.
>
> **Module thứ ba là API Service và Dashboard:** Module này cung cấp hai endpoint API riêng biệt cho dữ liệu dự báo và dữ liệu cảnh báo. Nó cung cấp dashboard trực quan để giám sát, đồng thời xử lý việc bảo mật thông qua xác thực API Key hoặc token JWT, với cơ chế phân quyền RBAC rõ ràng."

## Nguyễn Đức Huy · Slide 12 (90 giây)

> "Đối với các Yêu cầu phi chức năng (NFR), điểm sáng trong thiết kế của nhóm là **mỗi NFR đều được ánh xạ trực tiếp và ăn khớp với bộ KPI** đã cam kết ở phần trước. Ở cột bên phải của bảng yêu cầu, mọi người có thể thấy các mã KPI tương ứng.
>
> Về hiệu năng: Thời gian phản hồi API (P95) phải dưới 500 mili-giây (khớp với KPI B.1), và thời gian suy luận thuần của mô hình AI phải dưới 200 mili-giây (khớp KPI A.4).
>
> Về tính sẵn sàng: Hệ thống đảm bảo Uptime ở mức 99,9% (KPI B.3) và phát hiện sự cố dưới 15 phút (KPI B.7).
>
> Về chất lượng dữ liệu: Đảm bảo độ đầy đủ đạt 99,5% (KPI B.4) và độ trễ đồng bộ của dữ liệu batch dưới 24 giờ (KPI B.5).
>
> Về bảo mật và tuân thủ: Mọi kết nối đều phải mã hóa TLS 1.2+ trở lên. Quan trọng nhất, để tuân thủ Nghị định 13/2023/NĐ-CP, **toàn bộ dữ liệu giao dịch từ chi nhánh phải được ẩn danh hóa (anonymized) 100%** trước khi đưa vào huấn luyện mô hình. Hệ thống cũng được thiết kế sẵn sàng mở rộng (scale) lên 50 chi nhánh mà không cần phải đập đi xây lại kiến trúc."

## Vũ Duy · Slide 13 (90 giây)

> "Em là Vũ Duy, em xin phép trình bày chi tiết về luồng quy trình nghiệp vụ TO-BE.
>
> Đầu tiên, vào ban ngày (24/7), khách hàng liên tục giao dịch tại hệ thống POS của 34 chi nhánh.
>
> Đúng 01:00 AM mỗi ngày, tiến trình Airflow DAG sẽ tự động kích hoạt, trích xuất dữ liệu batch từ máy POS thông qua kênh truyền TLS mã hóa, đẩy về vùng lưu trữ thô (Raw Zone) trên Cloud S3.
>
> Lúc 01:15 AM, dữ liệu chuyển sang khâu Transform (Làm sạch). Tại đây, hệ thống khử trùng lặp và **đặc biệt là ẩn danh hóa các trường thông tin PII** trước khi nạp vào kho dữ liệu sạch PostgreSQL.
>
> Đến 02:00 AM, mô hình AI Engine sẽ chạy Batch Inference dự báo lưu lượng khách cho 34 chi nhánh trong 7 ngày tiếp theo. Ngay sau đó, Alert Service tự động quét toàn bộ kết quả. Nếu phát hiện khung giờ nào có lưu lượng dự báo vượt 150% so với mức trung bình, hệ thống sẽ đẩy thông báo khẩn qua Webhook hoặc Email.
>
> Cuối cùng, **08:00 AM sáng là Điểm kiểm soát quan trọng nhất**. Quản lý chi nhánh sẽ xem kết quả dự báo qua Dashboard. Từ thông số đó, họ đưa ra quyết định duyệt lịch phân ca và kế hoạch xuất nhập kho. Quyết định cuối cùng vẫn thuộc về bộ óc con người.
>
> Song song với luồng chạy hàng ngày này, hệ thống còn có một tiến trình tái huấn luyện định kỳ hàng tháng, trong đó mô hình mới sẽ được lưu lại phiên bản tại MLflow để so sánh với mô hình cũ."

## Vũ Duy · Slide 14 (90 giây)

> "Về tổng thể, kiến trúc hệ thống được thiết kế phân rã thành ba tầng độc lập để đảm bảo khả năng mở rộng.
>
> **Tầng trên cùng là Tầng trình bày (Presentation):** Bao gồm Web Dashboard dành cho người dùng nghiệp vụ (quản lý), Grafana dành cho đội ngũ IT theo dõi metrics, và các kênh thông báo Webhook/Email.
>
> **Ở giữa là Tầng ứng dụng (Application):** Tầng này giao tiếp thông qua API Gateway có tích hợp xác thực JWT và giới hạn tải. Chạy phía sau Gateway là hai dịch vụ FastAPI xử lý dự báo và cảnh báo, cùng với 'nhạc trưởng' Apache Airflow để điều phối các luồng xử lý dữ liệu tự động.
>
> **Dưới cùng là Tầng dữ liệu (Data):** Nền tảng cốt lõi sử dụng PostgreSQL làm Data Warehouse, Object Storage S3 để lưu trữ dữ liệu thô và file mô hình. MLflow đóng vai trò Model Registry quản lý các phiên bản AI. Prometheus và Loki đảm nhiệm việc thu thập log và metric của toàn hệ thống.
>
> Việc tách bạch ba tầng như thế này giúp doanh nghiệp có thể dễ dàng mở rộng quy mô lên 50 chi nhánh mà không cần phải đập đi xây lại kiến trúc. Về mặt thiết kế cơ sở dữ liệu, chúng em có bốn thực thể chính: Danh mục chi nhánh, Lưu lượng khách thực tế, Lưu lượng khách dự báo, và Metadata mô hình. Bảng Metadata này rất quan trọng vì nó lưu lại kết quả đánh giá của cả 4 thuật toán sau quá trình benchmark."

## Trần Anh Tú · Slide 15 (90 giây)

> "Em là Trần Anh Tú, em xin trình bày về Kế hoạch triển khai dự án.
>
> Dự án được chia thành 6 pha chuẩn mực, kéo dài 15 tuần phát triển và cộng thêm 4 tuần Hypercare. Cụ thể: Khảo sát và Phân tích (3 tuần), Thiết kế kiến trúc (2 tuần), Phát triển mô hình và API (5 tuần), Kiểm thử (3 tuần), Triển khai Go-live (2 tuần), và cuối cùng là Vận hành bảo trì Hypercare (4 tuần).
>
> Điểm cốt lõi mà nhóm muốn nhấn mạnh là: **Mỗi pha đều được gắn chặt với một KPI nghiệm thu cụ thể của pha đó**. Ví dụ, Pha Khảo sát phải đạt độ đầy đủ dữ liệu > 99,5%, Pha Phát triển phải đạt MAPE < 15%. Tuyệt đối không có chuyện chuyển pha mà không đo lường được kết quả.
>
> Về bộ máy nhân sự, dự án cần một đội ngũ đa nhiệm gồm 1 Project Manager, 2 Kỹ sư dữ liệu, 2 Kỹ sư AI, 1 Kỹ sư Backend, 1 Kỹ sư SRE, 1 QA và sự tham gia cực kỳ quan trọng của 2 Key User (Quản lý chi nhánh). Key User là người cung cấp logic nghiệp vụ thực tế và là người trực tiếp ký biên bản UAT.
>
> Về cơ chế làm việc, nhóm duy trì họp Daily Standup hàng tuần, Sprint Review mỗi hai tuần, và nghiệm thu Milestone với Ban Giám đốc cuối mỗi pha. Mọi thay đổi về phạm vi bắt buộc phải xử lý qua Change Request."

## Trần Anh Tú · Slide 16 (90 giây)

> "Về bức tranh tài chính, nhóm đã tính toán chi tiết dự toán: **Chi phí đầu tư ban đầu (CAPEX) trong giai đoạn 15 tuần là 663 triệu đồng**. Chi phí vận hành năm đầu tiên (OPEX) là khoảng 325,8 triệu. Cộng thêm quỹ dự phòng rủi ro 10%, **Tổng chi phí sở hữu (TCO) của riêng dự án này trong năm đầu là khoảng 1,088 tỷ đồng**.
>
> Khoản CAPEX 663 triệu chủ yếu là chi phí chất xám và nhân công (chiếm khoảng 594 triệu cho 27 người-tháng). Dự án không tốn chi phí mua bản quyền phần mềm nhờ áp dụng toàn bộ hệ sinh thái mã nguồn mở như Airflow, MLflow và FastAPI. Nhóm cũng thiết kế phương án tài chính linh hoạt bằng cách chuyển toàn bộ chi phí mua sắm máy chủ vật lý thành phí thuê bao Cloud (OPEX) hàng tháng.
>
> Đặc biệt, đây là điểm chiến lược mà nhóm đã tính trước: **Nếu Ban Giám đốc quyết định triển khai bài thực hành này đồng thời với nền tảng của đồ án môn học, thì phần lớn chi phí hạ tầng Cloud sẽ được hấp thụ chung vào nền tảng.** GPU phục vụ huấn luyện cũng được dùng chung. Nhờ vậy, TCO thực tế trong năm 1 của bài thực hành này sẽ giảm xuống chỉ còn khoảng **925 triệu đồng**. Hai bài toán độc lập nhưng chi phí không bị cộng dồn vô lý."

> ⚠ **Trần Anh Tú:** ô "không cộng dồn" là điểm phòng thủ quan trọng nếu cô đối chiếu với video đồ án.

## Lê Quang Đạt · Slide 17 (90 giây)

> "Em là Lê Quang Đạt, em xin trình bày về các rủi ro hệ thống và kế hoạch kiểm thử chất lượng.
>
> Nhóm đã nhận diện được 6 rủi ro tiềm ẩn, trong đó có 3 rủi ro được xếp loại mức độ Cao cần phải có biện pháp đối phó trực tiếp:
>
> **R01 — Dữ liệu POS bị bẩn hoặc thiếu hụt:** Máy POS mất mạng hoặc nhân viên nhập sai dữ liệu. Nhóm đối phó bằng cách thiết lập cơ chế làm sạch tự động (như Fill NA, Drop Outliers) ngay trong Data Pipeline, đồng thời phát cảnh báo tự động về chất lượng dữ liệu để Key User xử lý thủ công nếu cần.
>
> **R02 — Mô hình không đạt ngưỡng MAPE cam kết:** Đây là rủi ro nghề nghiệp kinh điển của bất kỳ bài toán AI nào. Nhóm cam kết sẽ thực nghiệm song song ít nhất 4 phương pháp dự báo. Nếu rủi ro xảy ra (không thuật toán nào đạt ngưỡng), hệ thống sẽ phát hành ở chế độ Beta không ràng buộc nghiệm thu, tự động chuyển về dùng thuật toán Moving Average cơ bản làm fallback an toàn.
>
> **R03 — Hiện tượng Data Drift:** Xảy ra khi hành vi khách hàng thay đổi đột ngột làm mô hình sai số. Biện pháp là thiết lập ngưỡng cảnh báo: Nếu MAPE vượt 15%, hệ thống sẽ tự động kích hoạt quá trình tái huấn luyện lại mô hình với tập dữ liệu mới nhất.
>
> Về kế hoạch kiểm thử (QA/QC), nhóm thiết kế thành 4 lớp: Kiểm thử tính toàn vẹn của dữ liệu pipeline; Chạy Backtesting để kiểm tra mô hình trên dữ liệu lịch sử; Sử dụng công cụ JMeter để Load Test **giả lập 500 người dùng truy cập API cùng lúc**; và cuối cùng là bước UAT do chính Key User trải nghiệm và ký biên bản Sign-off."

## Lê Quang Đạt · Slide 18 (90 giây)

> "Phần cuối cùng của em là về Kế hoạch vận hành và Chuyển giao công nghệ.
>
> Ngay sau ngày Go-live, hệ thống sẽ bước vào **1 tháng Hypercare (hỗ trợ đặc biệt)**. Đội dự án cam kết duy trì hỗ trợ ở mức cao nhất, với các buổi họp Daily Standup đúng 09:00 sáng mỗi ngày để rà soát lỗi API và độ trễ dữ liệu. Quy trình hỗ trợ tuân theo chuẩn ITSM 3 cấp độ (Tier 1-2-3), cam kết SLA xử lý các lỗi mức độ nghiêm trọng (P0/P1) trong vòng dưới 4 giờ.
>
> Về an toàn dữ liệu, hệ thống áp dụng **nguyên tắc sao lưu 3-2-1 kinh điển** cho Database PostgreSQL, đồng thời tổ chức diễn tập khôi phục thảm họa (DR Drill) mỗi 6 tháng một lần, đảm bảo thời gian khôi phục RTO dưới 4 giờ và RPO dưới 24 giờ.
>
> Gói bàn giao công nghệ cho doanh nghiệp cực kỳ chi tiết, bao gồm: Mã nguồn hệ thống trên GitLab, toàn bộ tài khoản quản trị Cloud, tài liệu kiến trúc kỹ thuật (HLD/LLD), Sổ tay vận hành (Runbook), và đặc biệt là **Báo cáo benchmark kết quả của đa mô hình AI**, để đội ngũ IT nội bộ có cơ sở tinh chỉnh cho các lần tái huấn luyện trong tương lai.
>
> Để hoàn tất nghiệm thu toàn bộ, hệ thống phải chạy ổn định 14 ngày trên Production không lỗi nghiêm trọng, và phải **vượt qua bài kiểm tra đo lại toàn bộ KPI tại các mốc 1, 3 và 6 tháng** — đặc biệt mốc 3 tháng là lúc MAPE bắt buộc phải đạt dưới 10%."

## Phạm Minh Mẫn · Slide 19 (60 giây)

> "Em xin kết luận. Đề tài thực hành của nhóm 5 thành công giải quyết bài toán với bốn điểm nhấn quan trọng.
>
> Một, bài toán mang lại giá trị thực tiễn cho đa phòng ban — chỉ một kết quả dự báo nhưng phục vụ đắc lực cho cả điều phối nhân sự, kho vận và chiến lược marketing.
>
> Hai, toàn bộ KPI đều đo lường được bằng các chỉ số toán học, có baseline đối chứng rõ ràng theo chuẩn quốc tế và lộ trình đo đạc thực tế tại các mốc 1, 3, 6 tháng sau go-live.
>
> Ba, nhóm đã chuẩn bị phương án kỹ thuật dự phòng bài bản — cam kết ngưỡng chỉ số thay vì cam kết thuật toán, có kịch bản fallback rõ ràng nếu AI gặp trục trặc.
>
> Bốn, chi phí đầu tư hợp lý, rõ ràng và có cơ chế không trùng lặp chi phí với dự án nền tảng hạ tầng đồ án nếu được triển khai song song.
>
> Phần báo cáo bài thực hành của nhóm 5 đến đây là hết. Nhóm em xin chân thành cảm ơn cô đã lắng nghe."

---

# CHUẨN BỊ VẤN ĐÁP

Vấn đáp diễn ra **sau khi cô xem video**, hỏi trên **cả hai nội dung**. Cô hỏi chung thì cả nhóm hỗ trợ trả lời; khi cô chỉ đích danh thì bạn đó bắt buộc trả lời một mình.

## Phân luồng câu hỏi

| Chủ đề | Người chính | Hỗ trợ |
|:---|:---|:---|
| Doanh nghiệp, phạm vi, ranh giới hai bài | Phạm Minh Mẫn | Huỳnh Thị Kiều Uyên (đồ án) / Trần Việt Đức (thực hành) |
| Số liệu hiện trạng, nguồn minh chứng | Đặng Nguyễn Minh Anh, Trần Văn Phây | Phạm Minh Mẫn |
| KPI, độ đo, công thức | Trần Việt Đức (đồ án), Trần Văn Phây & Huỳnh Thị Kiều Uyên (thực hành) | Phạm Minh Mẫn |
| Kiến trúc, so sánh phương án | Nguyễn Đức Huy (đồ án), Vũ Duy (thực hành) | Vũ Duy |
| Yêu cầu kỹ thuật, sizing | Vũ Duy (đồ án), Nguyễn Đức Huy (thực hành) | Nguyễn Đức Huy |
| Chi phí, TCO, hoàn vốn | Trần Anh Tú | Phạm Minh Mẫn |
| Tiến độ, rủi ro, nghiệm thu | Lê Quang Đạt | Trần Anh Tú |
| Mô hình AI, pipeline, thuật toán | Trần Văn Phây, Vũ Duy (thực hành) | Lê Quang Đạt |

## 12 câu hỏi khả năng cao nhất

**1. "Số liệu 2.500 giờ công, 3,8%, 47% ở đâu ra?"**
Nhóm không có quyền truy cập hệ thống vận hành thật nên dùng phương pháp mô phỏng có căn cứ, kết hợp ba nguồn. Những khẳng định về quy trình có minh chứng trực tiếp từ 8 bộ tài liệu SOP (Standard Operating Procedure) — liệt kê ở Phụ lục A. Các con số định lượng thì ghi rõ là suy luận, cần xác nhận lại ở Pha 1.

**2. "Phạm vi là Lớp 4 và 5, sao KPI lại có bảo mật Lớp 3?"**
Nhóm khai báo thẳng 02 thành phần Lớp 3 vào phạm vi ngay từ bước 0, có bảng in-scope / out-of-scope. Vấn đề rò rỉ PII không giải quyết được chỉ bằng Lớp 4 và 5. Các thành phần Lớp 3 còn lại ghi rõ là ngoài phạm vi.

**3. "Có mấy mục tiêu, KPI nào ứng với mục tiêu nào?"**
Ba mục tiêu, sáu KPI. Mã KPI đánh theo vấn đề: 1.x cho đứt gãy tích hợp, 2.x cho mù dữ liệu, 3.x cho rò rỉ PII.

**4. "Vì sao chọn Hybrid mà không phải Cloud cho rẻ?"**
Cloud-Native rẻ CAPEX nhất nhưng hỏng hai tiêu chí cứng: chi nhánh mất mạng là mất doanh thu ngay, và dữ liệu PII đặt trên hạ tầng bên thứ ba gây rủi ro tuân thủ. Với mô hình tính tiền theo giờ thì hai điều đó không đánh đổi được.

**5. "Doanh thu chuỗi bao nhiêu mà dám nói TCO chỉ 1,45%?"**
Ước tính khoảng 120 tỷ mỗi năm, trên cơ sở 34 chi nhánh nhân trung bình khoảng 294 triệu mỗi chi nhánh mỗi tháng cho tổ hợp 5 mảng dịch vụ cộng F&B. Đây là ước tính và nhóm ghi rõ cần doanh nghiệp xác nhận.

**6. "Lợi ích 1,955 tỷ có bị thổi phồng không?"**
Nhóm đã tính sẵn kịch bản thận trọng: loại hai dòng phụ thuộc mô hình AI thì dòng tiền ròng còn 252 triệu và payback kéo dài 5,7 năm. Kể cả vậy dự án vẫn được khuyến nghị vì nghĩa vụ tuân thủ.

**7. "Sao 3+4+4+5+4 = 20 tuần mà ghi 16 tuần?"**
Các pha gối đầu một tuần — pha sau khởi động trong tuần cuối của pha trước để chuẩn bị môi trường. Trừ 4 tuần gối đầu còn 16 tuần lịch, mốc M1–M5 đặt tại tuần 3, 6, 9, 13, 16.

**8. "Cùng một mô hình AI mà sao đồ án ghi MAPE 15%, thực hành ghi 10%?"**
Là một KPI đo ở hai mốc khác nhau: 15% là ngưỡng nghiệm thu tại Pilot khi dữ liệu chưa đủ chu kỳ mùa vụ, 10% là mục tiêu sản phẩm sau go-live 3 tháng. Trong đồ án, MAPE không phải KPI nền tảng mà chỉ là tiêu chí nghiệm thu hạng mục.

**9. "Hai bài có tính trùng chi phí không?"**
Không. Đồ án chỉ tính 90 triệu cho tích hợp và triển khai Inference Service, không bao gồm nghiên cứu mô hình. Bài thực hành có bảng ghi rõ nếu triển khai chung thì hạ tầng Cloud không cộng dồn, TCO giảm còn khoảng 925 triệu.

**10. "Nếu mô hình chạy ra không đạt thì sao?"**
Nhóm cam kết ngưỡng chỉ số chứ không cam kết thuật toán. Thực nghiệm song song 4 phương pháp rồi chọn cái tốt nhất. Nếu không phương pháp nào đạt tại Pilot thì phát hành ở chế độ beta không ràng buộc nghiệm thu, giữ Moving Average làm fallback và lập Change Request gia hạn.

**11. "Vì sao dùng mã nguồn mở hết, không sợ rủi ro vận hành à?"**
Nhóm chọn các dự án có cộng đồng lớn và bản LTS (Long Term Support) ổn định, đồng thời có thể chuyển sang bản managed trên Cloud cho Kafka và PostgreSQL — đã tính vào OPEX. Rủi ro pháp lý bản quyền kiểm soát bằng việc tuân thủ đúng điều khoản giấy phép OSS (Open Source Software).

**12. "Tại sao chỉ Pilot 5 chi nhánh, không làm luôn 34?"**
Vì 8 hệ thống POS từ nhiều nhà cung cấp là rủi ro cao nhất. Pilot cho phép phát hiện lỗi tích hợp trên quy mô nhỏ, và nếu có sự cố thì vẫn chạy song song hệ thống cũ thêm 2 tuần thay vì làm gián đoạn cả chuỗi.

---

# CHECKLIST TRƯỚC NGÀY THI

**Nội dung**
- [ ] Điền tên thật vào 9 vị trí TV1-TV9 trong slide 2 của **cả hai** deck và trong kịch bản này
- [ ] Mỗi bạn đọc thử phần của mình ở **cả hai** bài, bấm đồng hồ
- [ ] Chạy thử liền mạch từng video một lần, tập riêng các câu chuyển người
- [ ] Mỗi bạn học thuộc 2–3 câu trả lời trong bảng Q&A

**Quay video**
- [ ] Chốt lịch quay, ưu tiên phương án họp online quay một lần cho đỡ phải ghép
- [ ] Bật camera trong suốt phần báo cáo của mình
- [ ] **Hai video riêng biệt**, mỗi video ≤ 1 tiếng (nhắm 15–20 phút)
- [ ] Ghép thành **một file final duy nhất cho mỗi bài**, không để clip rời rạc trên Drive
- [ ] Đủ mặt cả 9 thành viên trong **cả hai** video

**Nộp bài**
- [ ] Bài thực hành: file thuyết minh + slide + video final
- [ ] Đồ án: file báo cáo đầu tư + slide + video final
- [ ] Để hai bộ vào hai thư mục riêng trên Drive, file final đặt ngoài cùng cho dễ thấy
- [ ] Nộp đủ link trên e-learning; file nào chưa nộp thì nộp bổ sung
- [ ] Có mặt đủ ngày vấn đáp; ai vắng phải báo cô trước và có lý do chính đáng
