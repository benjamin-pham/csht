## Phân công

| Người | Slide | Nội dung | Thời lượng |
|:---|:---:|:---|:---:|
| Phạm Minh Mẫn — Nhóm trưởng | 1–2 | Mở đầu, giới thiệu đề tài, phân công | 1'05" |
| Đặng Nguyễn Minh Anh | 3–4 | Bối cảnh, hiện trạng, tính cấp thiết | 1'50" |
| Trần Văn Phây | 5–6 | Mục tiêu tổng quát, KPI (Key Performance Indicator) nhóm A | 1'50" |
| Huỳnh Thị Kiều Uyên | 7–8 | KPI nhóm B, ánh xạ KPI theo giai đoạn | 1'45" |
| Trần Việt Đức | 9–10 | Phạm vi, giới hạn AI (Artificial Intelligence), yêu cầu nghiệp vụ | 1'50" |
| Nguyễn Đức Huy | 11–12 | Yêu cầu chức năng và phi chức năng | 1'45" |
| Vũ Duy | 13–14 | Quy trình TO-BE, pipeline, kiến trúc | 1'50" |
| Trần Anh Tú | 15–16 | Kế hoạch triển khai, nhân sự, dự toán | 1'55" |
| Lê Quang Đạt | 17–18 | Rủi ro, kiểm thử, vận hành, nghiệm thu | 1'50" |
| Phạm Minh Mẫn — Nhóm trưởng | 19 | Kết luận | 0'45" |

## Phạm Minh Mẫn · Slide 1 (40 giây)

> "Kính chào cô. Em là Phạm Minh Mẫn, nhóm trưởng nhóm 5. Nhóm em xin báo cáo **bài thực hành**: ứng dụng mô hình học sâu và mô hình nền tảng chuỗi thời gian để dự báo lưu lượng khách hàng đa chi nhánh, triển khai cho chuỗi Ways Station.
>
> Nhóm em đặt tên đề tài theo **nhánh kỹ thuật** chứ không khóa vào một thuật toán cụ thể, vì với bài toán dữ liệu thì chưa chạy thực nghiệm sẽ chưa biết phương pháp nào cho kết quả tốt nhất."

## Phạm Minh Mẫn · Slide 2 (25 giây)

> "Nhóm em có 9 bạn, mỗi bạn phụ trách một mục và trực tiếp báo cáo đúng mục mình làm. Toàn bộ 9 bạn đều tham gia cả video thực hành và video đồ án."

## Đặng Nguyễn Minh Anh · Slide 3 (55 giây)

> "Em là Đặng Nguyễn Minh Anh, em trình bày bối cảnh và hiện trạng.
>
> Bài toán nhóm em nhắm vào là **quy trình điều phối nguồn lực tại chi nhánh**, hiện đang hoàn toàn dựa vào cảm tính.
>
> Thứ nhất, dữ liệu giao dịch POS (Point of Sale) tại 34 chi nhánh xử lý thủ công và lưu trữ phân tán, độ trễ tổng hợp từ 48 đến 72 giờ.
>
> Thứ hai, vào giờ cao điểm thì thiếu nhân lực phục vụ, gián đoạn nguồn cung vật tư, khách chờ lâu. Ngược lại giờ thấp điểm lại dư thừa nhân lực phân bổ cố định, lãng phí chi phí vận hành.
>
> Thứ ba, máy chủ tại chi nhánh không đủ năng lực để làm sạch và huấn luyện mô hình trên tập dữ liệu lịch sử lớn.
>
> Nguyên nhân gốc là doanh nghiệp **không có công cụ dự báo định lượng theo chuỗi thời gian**."

## Đặng Nguyễn Minh Anh · Slide 4 (55 giây)

> "Vì sao bài toán này cấp thiết? Vì **một kết quả dự báo duy nhất phục vụ đồng thời bốn quy trình và ba phòng ban**.
>
> Phòng Điều phối dùng để xếp ca theo dữ liệu thay vì cảm tính. Bộ phận Kho hàng dùng để lập kế hoạch luân chuyển hàng, tránh đứt gãy cung ứng hoặc tồn đọng quá hạn. Bộ phận Marketing dùng để nhận diện khung giờ thấp điểm mà kích cầu, thay vì đốt ngân sách khuyến mãi vào giờ đã kín chỗ. Và quản lý chi nhánh dùng để lường trước đột biến, giữ chất lượng dịch vụ.
>
> Đây là lý do nhóm em cho rằng giá trị dự báo đủ sức nặng để doanh nghiệp đầu tư."

> ⚠ **Đặng Nguyễn Minh Anh:** đây chính là điều cô hướng dẫn ở Buổi 6 — phải tối đa hóa giá trị của thông tin dự báo, không gói gọn vào một phòng ban.

## Trần Văn Phây · Slide 5 (50 giây)

> "Em là Trần Văn Phây, em trình bày mục tiêu và cấu trúc KPI.
>
> Mục tiêu tổng quát: xây dựng nền tảng tự động thu thập dữ liệu giao dịch, huấn luyện mô hình học máy phân tích chuỗi thời gian, và cung cấp kết quả dự báo qua API (Application Programming Interface) phục vụ nội bộ.
>
> Bộ KPI được tách thành **hai nhóm độc lập**. Nhóm A đo năng lực và độ chính xác của mô hình AI. Nhóm B đo tính sẵn sàng và chất lượng kỹ thuật của phần mềm trong vận hành.
>
> Bài thực hành **không dùng KPI phân rã theo tầng hạ tầng** như bên đồ án, vì hai bài đo hai đối tượng khác nhau."

## Trần Văn Phây · Slide 6 (60 giây)

> "Nhóm A có 5 chỉ số.
>
> **MAPE (Mean Absolute Percentage Error)** là chỉ số lõi, thiết kế theo lộ trình siết dần: **dưới 15% tại thời điểm nghiệm thu Pilot, và dưới 10% sau go-live 3 tháng**. Lý do có hai mốc là tại Pilot dữ liệu vừa được migrate, chưa đủ chu kỳ mùa vụ; đến mốc 3 tháng, khi độ đầy đủ dữ liệu đã ổn định và mô hình đã qua hai chu kỳ tái huấn luyện, thì mới siết xuống 10%.
>
> Baseline đối chứng: Moving Average 7 ngày cho MAPE khoảng 25 đến 30%, ARIMA (AutoRegressive Integrated Moving Average) khoảng 18 đến 22%. Nhóm cam kết cải thiện tối thiểu 10% so với baseline tốt nhất.
>
> Ngoài ra có MAE (Mean Absolute Error) không quá 3 khách mỗi khung giờ, Precision nhận diện giờ cao điểm từ 85%, độ trễ suy luận dưới 200 mili-giây, và **chỉ số A.5 là độ ổn định đa ngữ cảnh** — chênh lệch MAPE không quá 10% giữa chi nhánh gym, gaming và hub, thử trên tối thiểu 4 bộ dữ liệu.
>
> Các độ đo đều theo chuẩn có sẵn, trích dẫn scikit-learn, Powers và Hyndman."

## Huỳnh Thị Kiều Uyên · Slide 7 (55 giây)

> "Em là Huỳnh Thị Kiều Uyên, em trình bày nhóm KPI thứ hai.
>
> Nhóm B đo phần mềm và vận hành, gồm 7 chỉ số. Em nói ba cái quan trọng nhất.
>
> **Thời gian phản hồi API ở phân vị 95 không quá 500 mili-giây** — đây là ngưỡng end-to-end, đã bao gồm 200 mili-giây suy luận mô hình của chỉ số A.4.
>
> **Uptime dịch vụ API từ 99,9%**, tức gián đoạn tối đa 43,2 phút mỗi tháng.
>
> **Độ đầy đủ dữ liệu từ 99,5%** và **độ tươi dữ liệu batch dưới 24 giờ**, hoàn tất đồng bộ lúc 1 giờ sáng mỗi ngày.
>
> Còn lại là thời gian chạy batch dưới 30 phút cho cả 34 chi nhánh, tỷ lệ lỗi HTTP (Hypertext Transfer Protocol) 5xx dưới 0,1%, và thời gian phát hiện sự cố dưới 15 phút — giảm từ mức 4 đến 8 giờ hiện nay khi phải chờ nhân viên báo qua Zalo.
>
> Mọi độ đo đều dùng khung chuẩn quốc tế, có công thức và trích dẫn ngay tại chỗ."

## Huỳnh Thị Kiều Uyên · Slide 8 (50 giây)

> "Để bảo đảm tính xuyên suốt từ thiết kế đến nghiệm thu, nhóm em **gắn KPI vào từng giai đoạn triển khai**.
>
> Giai đoạn khảo sát nghiệm thu bằng độ đầy đủ dữ liệu. Giai đoạn thiết kế nghiệm thu bằng chuẩn RESTful (Representational State Transfer) của API Contract. Giai đoạn phát triển nghiệm thu bằng MAPE, Precision, độ trễ suy luận và độ ổn định. Giai đoạn kiểm thử nghiệm thu bằng độ trễ API và tỷ lệ lỗi. Giai đoạn triển khai nghiệm thu bằng uptime và độ tươi dữ liệu.
>
> Và sau go-live 3 tháng còn một mốc nữa: MAPE phải đạt dưới 10%.
>
> **Mỗi giai đoạn chỉ được nghiệm thu khi đạt đúng KPI của giai đoạn đó.**"

## Trần Việt Đức · Slide 9 (60 giây)

> "Em là Trần Việt Đức, em trình bày phạm vi và giới hạn.
>
> Trong phạm vi: luồng tích hợp dữ liệu từ POS lên Cloud, huấn luyện mô hình dự báo, và cung cấp kết quả qua RESTful API và dashboard.
>
> Ngoài phạm vi: nhóm không sửa kiến trúc phần mềm kho, nhân sự hay ERP (Enterprise Resource Planning) hiện hành. Và **không bao gồm đầu tư hạ tầng Lớp 4 và Lớp 5** — phần đó thuộc đồ án môn học cùng nhóm. Bài này giả định một môi trường Cloud độc lập, không phụ thuộc vào việc đồ án có được phê duyệt hay không.
>
> Về giới hạn vai trò AI: hệ thống **chỉ hỗ trợ ra quyết định**, quản lý con người chốt quyết định cuối cùng. Độ chính xác sẽ suy giảm với sự kiện đột biến không có mẫu trong lịch sử, nên mô hình cần tái huấn luyện định kỳ hàng tháng.
>
> Và điểm cuối cùng: **nhóm cam kết ngưỡng chỉ số, không cam kết một thuật toán cụ thể.** Quy trình là thực nghiệm song song tối thiểu bốn phương pháp rồi chọn cái tốt và ổn định nhất. Nếu tại Pilot chưa phương pháp nào đạt, hệ thống phát hành ở chế độ beta không ràng buộc nghiệm thu, giữ Moving Average làm fallback và lập Change Request gia hạn."

## Trần Việt Đức · Slide 10 (50 giây)

> "Về yêu cầu nghiệp vụ, nhóm em mô tả theo use case với đầy đủ tác nhân, luồng chính và luồng ngoại lệ. Em nói hai cái chính.
>
> **BR-01 — xem dự báo:** quản lý chi nhánh đăng nhập, chọn chi nhánh và khoảng thời gian, hệ thống gọi API trả về dữ liệu. Nếu API lỗi hoặc chưa có dự báo mới thì hiển thị dữ liệu lịch sử tuần trước.
>
> **BR-03 — pipeline tự động:** 1 giờ sáng hệ thống kết nối POS, trích xuất, làm sạch rồi nạp vào Data Warehouse. Nếu rớt kết nối thì retry 3 lần, thất bại thì cảnh báo cho kỹ sư dữ liệu.
>
> Ba use case còn lại là cảnh báo giờ cao điểm, giám sát hệ thống, và lập kế hoạch nhập hàng cho bộ phận kho."

## Nguyễn Đức Huy · Slide 11 (55 giây)

> "Em là Nguyễn Đức Huy, em trình bày yêu cầu chức năng, gồm 13 yêu cầu chia theo ba module.
>
> **Module Data Pipeline**: trích xuất POS tự động qua kênh mã hóa, làm sạch và chuẩn hóa schema, nạp vào kho theo quy trình ELT (Extract, Load, Transform), và ghi log trạng thái mỗi lần chạy.
>
> **Module AI Forecasting Engine**: huấn luyện trên tối thiểu 12 tháng dữ liệu, dự báo theo khung giờ cho 7 ngày tới, tự động gán nhãn giờ cao điểm khi vượt 1,5 lần trung bình, quản lý phiên bản mô hình có hỗ trợ rollback. Và có một yêu cầu nhóm em bổ sung là **FR-13 — benchmark song song ít nhất 4 phương pháp** trên cùng bộ độ đo.
>
> **Module API và Dashboard**: hai endpoint cho dự báo và cảnh báo, dashboard giám sát, và xác thực API Key hoặc JWT (JSON Web Token) với phân quyền theo vai trò."

## Nguyễn Đức Huy · Slide 12 (50 giây)

> "Yêu cầu phi chức năng được thiết lập **khớp trực tiếp với bộ KPI** đã cam kết — cột bên phải là mã KPI tương ứng.
>
> Về hiệu năng: API dưới 500 mili-giây, suy luận mô hình dưới 200 mili-giây. Về sẵn sàng: uptime 99,9%, phát hiện sự cố dưới 15 phút. Về dữ liệu: đầy đủ 99,5%, độ trễ đồng bộ dưới 24 giờ. Về bảo mật: bắt buộc TLS (Transport Layer Security) 1.2 trở lên và xác thực API Key hoặc JWT. Về mở rộng: hỗ trợ lên 50 chi nhánh không cần đổi kiến trúc. Về tuân thủ: dữ liệu giao dịch được ẩn danh 100% theo Nghị định 13.
>
> Điểm nhóm em chú ý là **mỗi yêu cầu đều có con số kiểm thử được**, không có yêu cầu nào mô tả bằng lời suông."

## Vũ Duy · Slide 13 (55 giây)

> "Em là Vũ Duy, em trình bày quy trình TO-BE.
>
> Khách hàng giao dịch tại POS 24/7. Đúng 1 giờ sáng, Airflow rút dữ liệu từ 34 chi nhánh qua kênh mã hóa TLS về vùng dữ liệu thô trên S3 (Simple Storage Service). 1 giờ 15, hệ thống làm sạch, khử trùng lặp và **ẩn danh dữ liệu cá nhân** trước khi nạp vào PostgreSQL. 2 giờ sáng, AI Engine chạy dự báo hàng loạt cho 34 chi nhánh trong 7 ngày tới. Sau đó Alert Service tự động quét kết quả và đẩy cảnh báo nếu phát hiện khung giờ vượt 1,5 lần lưu lượng trung bình.
>
> Và **8 giờ sáng là điểm kiểm soát** — quản lý chi nhánh xem kết quả rồi duyệt lịch phân ca. Đây là chỗ con người chốt quyết định.
>
> Song song đó, Airflow chạy DAG (Directed Acyclic Graph) tái huấn luyện theo chu kỳ hàng tháng, lưu phiên bản mô hình tại MLflow kèm bộ chỉ số để so sánh với phiên bản trước."

## Vũ Duy · Slide 14 (55 giây)

> "Kiến trúc chia ba tầng. Tầng trình bày gồm web dashboard cho quản lý, Grafana cho đội IT (Information Technology), và kênh webhook/email. Tầng ứng dụng gồm API Gateway xử lý xác thực và giới hạn tải, hai dịch vụ FastAPI cho dự báo và cảnh báo, cùng Airflow điều phối luồng dữ liệu. Tầng dữ liệu gồm PostgreSQL làm kho dữ liệu, MLflow quản lý phiên bản mô hình, S3 lưu dữ liệu thô, và Prometheus cùng Loki thu thập metrics và log.
>
> Ba tầng tách bạch để có thể mở rộng lên 50 chi nhánh mà không phải đổi kiến trúc.
>
> Về thiết kế dữ liệu, mô hình có bốn thực thể chính: danh mục chi nhánh, lượng khách thực tế theo giờ, kết quả dự báo, và metadata mô hình — trong đó bảng metadata lưu cả thuật toán thực tế được chọn sau benchmark."

## Trần Anh Tú · Slide 15 (55 giây)

> "Em là Trần Anh Tú, em trình bày kế hoạch triển khai.
>
> Dự án chia 6 pha: 15 tuần phát triển cộng 4 tuần hypercare. Khảo sát và phân tích 3 tuần, thiết kế 2 tuần, phát triển 5 tuần, kiểm thử 3 tuần, triển khai 2 tuần, và hypercare 4 tuần sau go-live.
>
> Điểm nhóm em muốn nhấn: **mỗi pha gắn với đúng KPI nghiệm thu của pha đó**, nên không có pha nào bàn giao mà không đo được.
>
> Về nhân sự: 1 quản lý dự án, 2 kỹ sư dữ liệu, 2 kỹ sư AI, 1 backend, 1 DevOps/SRE (Site Reliability Engineering), 1 kiểm thử và 2 key user là quản lý chi nhánh — những người cung cấp logic xếp ca thực tế và ký nghiệm thu UAT (User Acceptance Testing).
>
> Cơ chế phối hợp: standup hàng tuần, sprint review hai tuần một lần, milestone review với Sponsor cuối mỗi pha. Mọi thay đổi phạm vi phải qua Change Request trên Jira."

## Trần Anh Tú · Slide 16 (60 giây)

> "Về chi phí: **CAPEX (Capital Expenditure) 663 triệu** cho giai đoạn 15 tuần, **OPEX (Operational Expenditure) năm đầu 325,8 triệu**, cộng dự phòng 10% thì **TCO (Total Cost of Ownership) năm 1 là 1,088 tỷ**.
>
> CAPEX chủ yếu là nhân công — 594 triệu cho khoảng 27 người-tháng. Chi phí bản quyền bằng 0 vì toàn bộ dùng mã nguồn mở: Airflow, MLflow, FastAPI.
>
> Và đây là điểm nhóm em đã tính trước: **nếu doanh nghiệp triển khai bài này cùng với nền tảng của đồ án thì chi phí hạ tầng Cloud được hấp thụ vào OPEX nền tảng, GPU tái huấn luyện dùng chung — TCO năm 1 giảm còn khoảng 925 triệu. Hai bài không cộng dồn chi phí.**
>
> Về phương án tài chính, nhóm chủ trương chuyển toàn bộ chi phí hạ tầng máy chủ thành OPEX thuê Cloud thay vì mua thiết bị vật lý."

> ⚠ **Trần Anh Tú:** ô "không cộng dồn" là điểm phòng thủ quan trọng nếu cô đối chiếu với video đồ án.

## Lê Quang Đạt · Slide 17 (55 giây)

> "Em là Lê Quang Đạt, em trình bày rủi ro và chất lượng.
>
> Nhóm em nhận diện 6 rủi ro. Ba cái mức cao.
>
> **R01 — dữ liệu POS bẩn hoặc thiếu**: xử lý bằng cơ chế làm sạch tự động trong pipeline, kèm cảnh báo chất lượng dữ liệu cho key user.
>
> **R02 — mô hình không đạt ngưỡng MAPE**: đây là rủi ro nghề nghiệp của bài toán dữ liệu. Nhóm xử lý bằng cách thực nghiệm ít nhất 4 phương pháp, và nếu vẫn chưa đạt thì phát hành chế độ beta không ràng buộc nghiệm thu, giữ Moving Average làm fallback.
>
> **R03 — data drift**: đặt ngưỡng cảnh báo MAPE vượt 15% là tự động kích hoạt tái huấn luyện.
>
> Về kiểm thử: kiểm thử dữ liệu yêu cầu 100% schema hợp lệ; kiểm thử mô hình chạy backtesting trên dữ liệu lịch sử; kiểm thử tải dùng JMeter giả lập 500 người dùng đồng thời; và UAT do key user ký sign-off trước go-live."

## Lê Quang Đạt · Slide 18 (55 giây)

> "Về vận hành và chuyển giao.
>
> Sau go-live có **1 tháng hypercare**, đội dự án hỗ trợ mức cao nhất với daily standup lúc 9 giờ sáng. Hỗ trợ theo mô hình ITSM (Information Technology Service Management) ba tier, cam kết SLA (Service Level Agreement) xử lý lỗi nghiêm trọng dưới 4 giờ.
>
> Sao lưu áp dụng **nguyên tắc 3-2-1** cho PostgreSQL, diễn tập khôi phục thảm họa 6 tháng một lần với RPO (Recovery Point Objective) dưới 24 giờ và RTO (Recovery Time Objective) dưới 4 giờ.
>
> Gói bàn giao gồm mã nguồn, tài khoản quản trị, tài liệu kiến trúc, runbook, và **báo cáo benchmark đa mô hình** để đội IT có cơ sở cho các lần tái huấn luyện sau.
>
> Về nghiệm thu: UAT ký xác nhận, hệ thống chạy 14 ngày Production không có sự cố nghiêm trọng, và **đo lại toàn bộ KPI tại mốc 1, 3 và 6 tháng** — trong đó mốc 3 tháng MAPE phải đạt dưới 10%."

## Phạm Minh Mẫn · Slide 19 (45 giây)

> "Em xin kết luận. Đề tài của nhóm có bốn điểm.
>
> Một, bài toán có giá trị đa phòng ban — một kết quả dự báo phục vụ cả điều phối nhân sự, kho vận và marketing.
>
> Hai, KPI đo được và có baseline đối chứng rõ ràng, độ đo theo chuẩn quốc tế, có mốc đo tại 1, 3, 6 tháng sau go-live.
>
> Ba, nhóm có phương án kỹ thuật dự phòng — cam kết ngưỡng chỉ số chứ không cam kết thuật toán, có fallback rõ ràng.
>
> Bốn, chi phí hợp lý và không trùng lặp với đồ án nếu triển khai chung.
>
> Phần báo cáo bài thực hành của nhóm 5 đến đây là hết. Nhóm em xin cảm ơn cô."

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
