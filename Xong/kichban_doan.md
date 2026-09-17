## Phân công

| Người | Slide | Nội dung | Thời lượng |
|:---|:---:|:---|:---:|
| Phạm Minh Mẫn — Nhóm trưởng | 1–3 | Mở đầu, phân công, tóm tắt điều hành | 3'00" |
| Đặng Nguyễn Minh Anh | 4–5 | Bối cảnh doanh nghiệp, kiến trúc AS-IS | 3'00" |
| Trần Văn Phây | 6–7 | Ba điểm nghẽn định lượng, minh chứng | 3'00" |
| Huỳnh Thị Kiều Uyên | 8–9 | Rủi ro nếu không đầu tư, phạm vi lớp năng lực | 3'00" |
| Trần Việt Đức | 10–11 | Bộ 6 KPI, phương pháp đo lường | 3'00" |
| Nguyễn Đức Huy | 12–13 | Ba kịch bản, cơ sở chọn Hybrid Cloud | 3'00" |
| Vũ Duy | 14–15 | Kiến trúc TO-BE, yêu cầu kỹ thuật, BOM | 3'00" |
| Trần Anh Tú | 16–17 | CAPEX/OPEX/TCO, hiệu quả đầu tư | 3'00" |
| Lê Quang Đạt | 18–19 | Lộ trình, rủi ro, RACI, mua sắm, nghiệm thu | 3'00" |
| Phạm Minh Mẫn — Nhóm trưởng | 20 | Kết luận | 0'55" |

## Phạm Minh Mẫn · Slide 1 (50 giây)

> "Kính chào cô. Em là Phạm Minh Mẫn, nhóm trưởng nhóm 5. Nhóm em xin báo cáo **đồ án môn học**: đề xuất đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station.
>
> Báo cáo này giải quyết bài toán đứt gãy kết nối giữa 34 chi nhánh và sự cấp thiết phải tuân thủ Nghị định 13 về bảo vệ dữ liệu cá nhân. Tổng mức đầu tư ban đầu (CAPEX) là 1,308 tỷ đồng, tổng chi phí sở hữu (TCO) 3 năm là 5,209 tỷ, và dự án được lên kế hoạch triển khai trong vòng 16 tuần, chia làm 5 pha rõ ràng."

## Phạm Minh Mẫn · Slide 2 (25 giây)

> "Về đội ngũ thực hiện, nhóm em gồm 9 bạn, mỗi bạn sẽ phụ trách trình bày sâu vào một hạng mục và trực tiếp báo cáo phần việc mà mình đảm nhiệm."

## Phạm Minh Mẫn · Slide 3 (90 giây)

> "Trước khi đi vào các phân tích kỹ thuật chi tiết, em xin tóm tắt toàn bộ đề xuất đầu tư trong một slide.
>
> **Về vấn đề hiện tại:** Chuỗi đang có 34 chi nhánh hoạt động như 34 ốc đảo với 8 hệ thống phần mềm rời rạc. Tỉ lệ tích hợp tự động là 0%, dữ liệu phục vụ quản trị luôn bị trễ từ 24 đến 48 giờ. Đáng lo ngại nhất là dữ liệu cá nhân của hội viên như Face ID, hình CCCD chưa hề được mã hóa.
>
> **Về giải pháp đề xuất:** Nhóm quyết định đầu tư Lớp 4 (Nền tảng tích hợp ứng dụng) và Lớp 5 (Nền tảng dữ liệu), bổ sung thêm 2 thành phần thiết yếu của Lớp 3 là quản lý định danh IAM và mã hóa dữ liệu. Kiến trúc được chọn là **Hybrid Cloud (Lai)**, vừa tận dụng sức mạnh điện toán đám mây, vừa giữ dữ liệu nhạy cảm ở máy chủ vật lý nhằm tuân thủ pháp luật.
>
> **Về bức tranh tài chính:** Tổng mức đầu tư CAPEX là 1,308 tỷ, chi phí vận hành OPEX khoảng 1,123 tỷ/năm. TCO 3 năm là 5,209 tỷ, tương đương chỉ 1,45% doanh thu chuỗi trong cùng kỳ.
>
> **Về hiệu quả:** Lợi ích quy đổi khoảng 1,955 tỷ/năm, thời gian hoàn vốn dòng tiền khoảng 1,7 năm. Hơn hết, dự án giúp doanh nghiệp tránh được rủi ro phạt lên đến 5% doanh thu theo Nghị định 13.
>
> Nhóm em khuyến nghị Ban Giám đốc phê duyệt ngân sách và khởi động Pha 1 ngay trong quý tới."

## Đặng Nguyễn Minh Anh · Slide 4 (90 giây)

> "Em là Đặng Nguyễn Minh Anh. Em xin trình bày về bối cảnh doanh nghiệp trước, vì **chính đặc thù của doanh nghiệp sẽ quyết định giải pháp kiến trúc kỹ thuật**, chứ không phải nhóm chọn công nghệ trước rồi mới áp đặt vào.
>
> Chuỗi Ways Station hiện có 34 chi nhánh trên địa bàn TP. Hồ Chí Minh và lân cận, tăng nhanh từ 22 chi nhánh chỉ trong khoảng 2 năm. Cơ cấu trụ sở chính gồm 3 phòng ban tập trung: Nhân sự, Điều phối, Kho hàng. Đáng chú ý, mỗi chi nhánh vận hành đồng thời 5 mảng dịch vụ gồm Gym 24/7, Gaming, Billiards, Cầu lông, Hub và F&B, với tổng cộng khoảng 300 nhân sự làm việc theo ca.
>
> Từ bức tranh tổng quan đó, nhóm nhận diện ba đặc điểm cốt lõi chi phối toàn bộ bài toán đầu tư:
>
> Một, **mỗi chi nhánh được đăng ký là một hộ kinh doanh cá thể riêng biệt**. Doanh nghiệp không có một pháp nhân trung tâm sở hữu kho dữ liệu chung, điều này khiến hạ tầng bị chia cắt thành 34 ốc đảo dữ liệu.
>
> Hai, **doanh thu tính theo giờ sử dụng liên tục**. Khách vào ra liên tục và tính tiền tại quầy, nếu mất mạng vài phút là không thể tính tiền, không trả được bàn bida hay trả xe.
>
> Ba, doanh nghiệp đang **thu thập dữ liệu cá nhân (PII) nhạy cảm ngay tại quầy** như ảnh căn cước, cà vẹt xe, và Face ID hội viên.
>
> Ba đặc điểm này sẽ là chìa khóa để nhóm loại trừ các phương án ở phần lựa chọn kiến trúc."

## Đặng Nguyễn Minh Anh · Slide 5 (90 giây)

> "Đây là sơ đồ kiến trúc hiện tại (AS-IS). Như mọi người thấy, 34 chi nhánh đang vận hành độc lập với 8 hệ thống phần mềm rời rạc: POS cho net và bida, phần mềm MODUN Gym, ACB portal, phần mềm nhân sự, phần mềm kho, và sổ giao ca giấy. **Giữa các hệ thống này không hề có API kết nối, tỉ lệ tích hợp luồng tự động là 0%.**
>
> Toàn bộ giao tiếp giữa chi nhánh và trụ sở đi qua ba kênh thủ công: một tổng đài duy nhất 0889 555 559 phải phân luồng theo phím số, các nhóm Zalo cá nhân, và sổ giao ca giấy hoặc biên bản giấy. Nhân viên phòng ban phải lập báo cáo thủ công bằng Excel tiêu tốn khoảng 2.500 giờ công mỗi năm, và dữ liệu phục vụ quản trị luôn có độ trễ từ 24 đến 48 giờ.
>
> Hệ quả của kiến trúc này rất rõ ràng: Khách hàng không có định danh duy nhất (SSO) nên không thể bán chéo dịch vụ; Thời gian phát hiện sự cố mất từ 4 đến 8 giờ vì hoàn toàn phụ thuộc vào việc nhân viên chi nhánh chủ động nhắn tin báo lỗi qua Zalo; và việc sao lưu dữ liệu cục bộ rất rủi ro với tỉ lệ thành công chỉ đạt 47%. Nhường lời lại cho bạn Phây trình bày sâu hơn về các điểm nghẽn này."

## Trần Văn Phây · Slide 6 (90 giây)

> "Em là Trần Văn Phây. Tiếp nối phần bối cảnh, nhóm em đã định lượng hóa các vấn đề thành ba điểm nghẽn chính tương ứng với ba lớp năng lực cần đầu tư. **Mỗi điểm nghẽn đều được gắn với một con số baseline cụ thể** để có cơ sở nghiệm thu sau này.
>
> Thứ nhất, ở Lớp 4 (Tích hợp ứng dụng): Tỉ lệ tự động hóa là 0%, với 8 hệ thống phần mềm hoạt động rời rạc ở 34 chi nhánh. Do không có luồng giám sát tập trung, thời gian phát hiện sự cố hệ thống kéo dài từ 4 đến 8 giờ.
>
> Thứ hai, ở Lớp 5 (Nền tảng dữ liệu): Đội ngũ HQ phải tiêu tốn khoảng 2.500 giờ công mỗi năm chỉ để làm báo cáo Excel thủ công. Dữ liệu trễ 24 đến 48 giờ khiến quyết định chậm trễ, và tỉ lệ sai lệch khi đối soát số liệu doanh thu lên đến 3,8%.
>
> Thứ ba, ở Lớp 3 (Bảo mật và Danh tính): Tỉ lệ mã hóa dữ liệu cá nhân (PII) đang là 0%. Dữ liệu nhạy cảm được truyền qua Zalo. Sao lưu dữ liệu phân tán cục bộ có tỉ lệ thành công chỉ đạt 47%, với RPO (Recovery Point Objective) lên tới 24 giờ.
>
> Về nguồn gốc các số liệu này, do nhóm không có quyền truy cập trực tiếp vào hệ thống vận hành thực tế của Ways Station, chúng em sử dụng **phương pháp mô phỏng có căn cứ (evidence-based simulation)**. Phương pháp này kết hợp tài liệu quy trình vận hành nội bộ (SOP), các chuẩn ngành quốc tế như Google SRE, Atlassian ITSM, AWS DR, NIST, và các nguyên lý kỹ thuật phổ quát để suy luận."

## Trần Văn Phây · Slide 7 (90 giây)

> "Slide này cung cấp minh chứng cho những khẳng định ở hiện trạng. Các kết luận không phải do nhóm tự nghĩ ra, mà được **dẫn chứng trực tiếp từ 8 bộ tài liệu quy trình chuẩn (SOP) đang áp dụng thực tế** tại các chi nhánh Ways Station.
>
> Ví dụ, trong tài liệu Thu ngân có ghi rõ bộ phận kho hàng phụ trách *'hỗ trợ đăng nhập phần mềm MODUN gym và ACB portal'*. Điều này là minh chứng trực tiếp cho thấy hệ thống rất phân mảnh, nhân viên phải đăng nhập nhiều lần và hoàn toàn không có giải pháp SSO (Single Sign-On). Hệ thống nhân sự cũng được tách rời trên một cổng riêng `ns.ways.vn`.
>
> Nghiêm trọng hơn, trong tài liệu Giữ xe quy định khi khách mất thẻ, nhân viên phải *'chụp ảnh căn cước công dân, cà vẹt xe, biên bản, và hình ảnh khách, sau đó gửi qua Zalo cho Quản lý'*. Trong khi đó, tài liệu Thu ngân Gym yêu cầu *'check-in bằng Face ID'* và thu thập thông tin cá nhân trên giấy. Đây là minh chứng trực tiếp không thể chối cãi cho việc doanh nghiệp đang thu thập dữ liệu sinh trắc học và giấy tờ tùy thân nhạy cảm nhưng lại xử lý qua mạng xã hội cá nhân với 0% cơ chế mã hóa bảo vệ.
>
> Nhóm có liệt kê đầy đủ 10 dòng minh chứng trích dẫn chi tiết nằm ở Phụ lục A của báo cáo."

## Huỳnh Thị Kiều Uyên · Slide 8 (90 giây)

> "Em là Huỳnh Thị Kiều Uyên. Dựa trên các điểm nghẽn mà bạn Phây vừa nêu, nếu không có một dự án đầu tư để giải quyết, doanh nghiệp sẽ phải đối mặt với ba nhóm rủi ro lớn.
>
> Thứ nhất là rủi ro vận hành: Việc thiếu API Gateway khiến hệ thống chịu tải rất kém vào các giờ cao điểm, trực tiếp gây gián đoạn hoạt động bán hàng. Đồng thời, hàng ngàn giờ công đang bị lãng phí vô ích do phải đối soát số liệu thủ công và nhập liệu kép giữa các hệ thống.
>
> Thứ hai là rủi ro chiến lược: Tình trạng 'mù dữ liệu' với độ trễ 48 giờ khiến ban lãnh đạo luôn ra quyết định sau thực tế. Thiếu dữ liệu phân tích tập trung dẫn đến việc không thể dự báo nhu cầu, gây lãng phí lớn nguyên vật liệu F&B và sai lệch trong xếp ca nhân viên. Đồng thời, doanh nghiệp mất đi cơ hội bán chéo dịch vụ giữa 5 mảng kinh doanh do không định danh được khách hàng.
>
> Tuy nhiên, **nghiêm trọng nhất và cấp bách nhất là rủi ro tuân thủ**. Việc lưu trữ hình ảnh căn cước, cà vẹt xe, Face ID trên thiết bị cá nhân và Zalo vi phạm nghiêm trọng Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân. Doanh nghiệp đang đối mặt với rủi ro phạt lên tới 5% tổng doanh thu và đánh mất uy tín. Đây là rủi ro không thể trì hoãn vì mức độ phơi nhiễm tăng tuyến tính theo số lượng chi nhánh mới được mở."

## Huỳnh Thị Kiều Uyên · Slide 9 (90 giây)

> "Để giải quyết các rủi ro đó, nhóm xác định **phạm vi đầu tư theo lớp năng lực hạ tầng**, không mua sắm thiết bị rời rạc thiếu định hướng.
>
> Trọng tâm của dự án là Lớp 4 và Lớp 5. Lớp 4 (Nền tảng ứng dụng) bao gồm API Gateway, Message Queue (Kafka), và hệ thống Container K8s/K3s. Lớp 5 (Nền tảng dữ liệu) bao gồm Data Lakehouse, luồng ETL Airflow và CDC Streaming thời gian thực.
>
> Điều đặc biệt trong kiến trúc của nhóm là chúng em **chủ động khai báo thêm đúng 2 thành phần của Lớp 3 (Bảo mật & Danh tính)** vào phạm vi đầu tư: Hệ thống quản lý định danh IAM/SSO (Keycloak) và cơ chế Mã hóa dữ liệu PII. Lý do là vì Vấn đề rò rỉ dữ liệu (Vấn đề 3) không thể giải quyết được chỉ bằng Lớp 4 và Lớp 5. Các hạng mục bảo mật khác như PAM, EDR, SIEM, hay DLP được làm rõ là ngoài phạm vi và chưa đầu tư trong kỳ này. Tương tự, hệ thống lưu trữ SAN/NAS, đường truyền lõi của Lớp 1 cũng nằm ngoài phạm vi.
>
> Nhờ phân định rõ ràng như vậy, toàn bộ KPI bảo mật và các yêu cầu kỹ thuật liên quan đều có cơ sở vững chắc, đảm bảo tính nhất quán từ mục tiêu xuống đến giải pháp kỹ thuật."

## Trần Việt Đức · Slide 10 (90 giây)

> "Em là Trần Việt Đức. Dựa vào 3 vấn đề cốt lõi, nhóm em đã thiết lập ma trận truy vết với **ba mục tiêu kiến trúc và sáu KPI kỹ thuật tương ứng**.
>
> Đối với Vấn đề 1 (Đứt gãy tích hợp), nhóm đặt hai KPI: Nâng Uptime từ mức 'không đo lường được' lên tối thiểu 99,99% (tức downtime dưới 4,32 phút/tháng), và giảm MTTR (thời gian khôi phục sự cố) từ 12-24 giờ xuống dưới 30 phút bằng cơ chế tự phục hồi.
>
> Với Vấn đề 2 (Mù dữ liệu), nhóm cam kết kéo giảm độ trễ luồng dữ liệu (Data Freshness) từ 24-48 giờ xuống dưới 5 giây. Đồng thời, độ đầy đủ của dữ liệu (Completeness) phải đạt tối thiểu 99,5%, giúp kéo tỉ lệ sai lệch khi đối soát doanh thu từ 3,8% xuống dưới 0,5%.
>
> Với Vấn đề 3 (Rò rỉ PII), nhóm đưa ra KPI mã hóa 100% dữ liệu nhạy cảm cả khi lưu trữ và truyền tải. Mục tiêu RPO (thời gian tối đa mất mát dữ liệu) phải giảm từ 24 giờ xuống dưới 15 phút.
>
> Mỗi KPI được thiết kế không phải để gọi cho có, mà **phải có đầy đủ baseline hiện tại, target mục tiêu, mốc đo lường và cá nhân chịu trách nhiệm số liệu**. Tiêu chí thành công của dự án là phải đạt 6/6 KPI tại mốc Go-live (Tháng 5) và duy trì tối thiểu 5/6 KPI tại mốc 3 tháng sau Go-live."

## Trần Việt Đức · Slide 11 (90 giây)

> "Để đảm bảo các KPI có thể nghiệm thu khách quan, nhóm **không tự định nghĩa độ đo bằng lời nói suông**, mà sử dụng trực tiếp các khung đo lường đã được chuẩn hóa quốc tế.
>
> Cụ thể, KPI Uptime được tính theo chuẩn Google SRE (Site Reliability Engineering) với công thức tổng thời gian trừ downtime chia tổng thời gian. MTTR đo theo chuẩn Atlassian ITSM.
>
> Các độ đo về dữ liệu bao gồm Data Freshness và Completeness tuân theo tiêu chuẩn chất lượng dữ liệu quốc tế ISO/IEC 25012. Tỉ lệ mã hóa PII 100% tham chiếu chuẩn bảo mật của chính phủ Mỹ NIST SP 800-175B. Mục tiêu RPO được tính theo khung Disaster Recovery của AWS. Nhờ vậy, mỗi KPI đều là một công thức toán học rõ ràng và có thể kiểm chứng được bằng log hệ thống hoặc báo cáo hệ thống giám sát.
>
> Đồng thời, em cũng xin phân định rõ: Đồ án môn học đo lường **năng lực của nền tảng**. Do đó, độ chính xác của mô hình dự báo AI (như MAPE < 15%) không phải là KPI của dự án nền tảng này, mà chỉ là tiêu chí nghiệm thu hạng mục liên quan đến sản phẩm phần mềm ở bài thực hành. Nền tảng chỉ cam kết cung cấp luồng dữ liệu đạt chuẩn (tươi dưới 5s, đầy đủ >99.5%) để mô hình đó có thể chạy tốt."

## Nguyễn Đức Huy · Slide 12 (90 giây)

> "Em là Nguyễn Đức Huy. Để đạt được 6 KPI khắt khe trên, nhóm đã phân tích chi tiết 3 kịch bản kiến trúc: On-Premise 100%, Cloud-Native 100%, và Hybrid Cloud.
>
> Kịch bản A là On-Premise 100%. Lợi thế lớn nhất là khả năng kiểm soát dữ liệu tuyệt đối và hoạt động offline hoàn hảo. Tuy nhiên, kiến trúc này yêu cầu CAPEX cực kỳ cao (lên tới 2,8 tỷ) do phải mua sắm máy chủ cấu hình lớn cho cả HQ và 34 chi nhánh. Nó không có khả năng co giãn tự động và cơ chế khôi phục thảm họa (DR) rất yếu. Nó chỉ đáp ứng được 2 trên 6 tiêu chí bắt buộc.
>
> Kịch bản B là Cloud-Native 100%. Mọi thứ chạy trên Cloud giúp CAPEX thấp nhất (chỉ khoảng 650 triệu) và khả năng mở rộng tuyệt vời. Tuy nhiên, điểm chết của nó là nếu chi nhánh rớt mạng thì không thể bán hàng, và việc đặt dữ liệu nhạy cảm lên máy chủ bên thứ ba gây rủi ro tuân thủ pháp lý. Kịch bản này đáp ứng được 4 trên 6 tiêu chí.
>
> Cuối cùng là **kịch bản C - Hybrid Cloud (Lai)**. Kịch bản này đặt các tải nặng lên Cloud để tận dụng auto-scaling, và giữ phần IAM, dữ liệu nhạy cảm PII ở máy chủ tại trụ sở chính. Đối chiếu với 6 tiêu chí bắt buộc (Uptime 99.99%, Auto-scaling, Tuân thủ NĐ13, CAPEX thấp, Agility cao, Active-Active DR), **chỉ có Hybrid Cloud đáp ứng trọn vẹn 6/6 tiêu chí**."

## Nguyễn Đức Huy · Slide 13 (90 giây)

> "Tuy nhiên, việc đáp ứng 6/6 tiêu chí chưa phải là điểm mấu chốt. Câu hỏi quan trọng hơn là: **sáu tiêu chí đó từ đâu ra và có thực sự phản ánh đúng nhu cầu của doanh nghiệp này hay không?**
>
> Chúng em không tự vẽ ra tiêu chí, mà rút ra trực tiếp từ 4 đặc điểm cốt lõi của Ways Station.
>
> Một: Doanh thu của chuỗi tính theo giờ sử dụng (Net, Bida) và thu tiền tại quầy. Rớt mạng vài phút là không tính được tiền và không trả được bàn. Đặc điểm này yêu cầu hệ thống phải tính được tiền offline, qua đó **loại bỏ phương án Cloud-Native 100%**.
>
> Hai: 34 hộ kinh doanh là mặt bằng thuê, không có phòng máy chủ, không có IT thường trực. Không thể vận hành cụm máy chủ On-Prem tại từng điểm, đòi hỏi thiết bị phải nhỏ gọn, dễ cấu hình từ xa. Đặc điểm này **loại bỏ phương án On-Premise**.
>
> Ba: Doanh nghiệp thu thập trực tiếp ảnh căn cước, Face ID tại quầy. Dữ liệu định danh buộc phải nằm dưới quyền kiểm soát vật lý của doanh nghiệp để tuân thủ luật pháp. Lại tiếp tục **loại bỏ Cloud-Native**.
>
> Bốn: Tăng trưởng nhanh, mở chi nhánh liên tục. Cần khả năng nhân bản cấu hình mới trong vài giờ và co giãn theo tải. Lại tiếp tục **loại bỏ On-Premise**.
>
> Từ sự đối chiếu này, kết luận của nhóm rất rõ ràng: **Hybrid Cloud là lựa chọn bắt buộc bị ràng buộc bởi thực tế doanh nghiệp, chứ không phải do nhóm chạy theo xu hướng công nghệ.**"

> ⚠ **Nguyễn Đức Huy:** slide quan trọng nhất cả video. Đây là điểm cô yêu cầu nhóm bổ sung ở Buổi 6.

## Vũ Duy · Slide 14 (90 giây)

> "Em là Vũ Duy. Từ chiến lược Hybrid Cloud, nhóm thiết kế kiến trúc mục tiêu chia làm ba khối (zones) phối hợp chặt chẽ với nhau.
>
> **Khối thứ nhất nằm trên Public Cloud**, nơi chứa các cấu phần hạng nặng của Lớp 4 và 5: API Gateway chịu tải 2.000 kết nối đồng thời với xác thực JWT, cụm Kafka với replication factor bằng 3 để đảm bảo không mất thông điệp. Data Lakehouse, PostgreSQL HA, luồng ETL Airflow và dịch vụ AI Inference đều chạy trên nền tảng K8s (Kubernetes) Multi-zone tự động failover dưới 60 giây.
>
> **Khối thứ hai đặt tại Trụ sở chính (HQ - On-Premise)**, nơi nhóm khoanh vùng Lớp 3. Đây là 'vùng an toàn' giữ đúng phần nhạy cảm nhất: Keycloak xử lý SSO/IAM đa yếu tố và Cơ sở dữ liệu PII mã hóa chuẩn AES-256 (cho CCCD, số điện thoại, Face ID). Khối này được đặt sau tường lửa NGFW, chỉ kết nối an toàn lên Cloud thông qua VPN Site-to-Site.
>
> **Khối thứ ba phân tán tại 34 Chi nhánh (Edge)**. Mỗi chi nhánh trang bị một Mini Server chạy K3s siêu nhẹ, chứa Kafka broker con, bộ nhớ đệm (Local DB) và hệ thống lưu điện UPS 650VA. Khi mất kết nối mạng, phần mềm POS vẫn tính tiền trơn tru bằng cách gọi API cục bộ xuống Edge Server. Hàng đợi Store-and-Forward có thể chứa giao dịch trong 48 giờ. Khi có mạng trở lại, CDC Streaming sẽ tự động đồng bộ bù dữ liệu về Cloud.
>
> Điểm mấu chốt của kiến trúc này: **Dữ liệu PII định danh nhạy cảm không bao giờ rời khỏi máy chủ On-Premise. Dữ liệu vận hành (hóa đơn, điểm danh) được ẩn danh hóa trước khi được đẩy lên Cloud.** Cách thiết kế này là lời giải hoàn hảo vừa đáp ứng khả năng offline, vừa tuân thủ tuyệt đối Nghị định 13."

## Vũ Duy · Slide 15 (90 giây)

> "Từ sơ đồ kiến trúc, nhóm đã chi tiết hóa thành Bộ 28 Yêu cầu Kỹ thuật, chia làm 4 nhóm để làm cơ sở nghiệm thu và truy vết ngược về từng KPI.
>
> **Nhóm 1 - Hiệu năng & Dung lượng:** API Gateway chịu tải 2.000 kết nối đồng thời (đáp ứng giờ cao điểm của 34 CN), thời gian phản hồi P95 phải dưới 200ms. Luồng CDC streaming phải xử lý 5.000 events/giây. Thời gian truy vấn API dự báo đầu cuối phải dưới 500ms.
>
> **Nhóm 2 - Sẵn sàng cao & DR:** Môi trường Cloud thiết lập 2 availability zones, failover dưới 60s. Kafka nhân bản 3 bản. Cơ chế dự phòng tại Edge lưu 48 giờ giao dịch. Backup dữ liệu tự động với RPO dưới 15 phút.
>
> **Nhóm 3 - Bảo mật:** 100% ứng dụng bắt buộc sử dụng SSO, tài khoản quản trị phải có MFA. Dữ liệu phải mã hóa AES-256 (lưu trữ) và TLS 1.2+ (truyền tải). Log bảo mật lưu trữ trung tâm, và không được có lỗ hổng Critical/High tồn tại quá 72 giờ.
>
> **Nhóm 4 - Vận hành:** Giám sát thời gian thực bằng Prometheus/Grafana, cảnh báo gửi về điện thoại trong dưới 5 phút. Quản lý toàn bộ cấu hình bằng mã (IaC - Terraform) cho phép rollback hệ thống chỉ trong 15 phút.
>
> Về danh mục đầu tư (BOM), để đảm bảo tính khả thi về ngân sách cho doanh nghiệp vừa (SMB), **toàn bộ phần mềm nền tảng sử dụng mã nguồn mở** (như Kubernetes, Kafka, Keycloak, Airflow). Nhờ đó, chi phí bản quyền là 0 đồng."

## Trần Anh Tú · Slide 16 (90 giây)

> "Em là Trần Anh Tú. Phần tiếp theo, em xin trình bày về bài toán ngân sách và hiệu quả đầu tư. Ở đây có ba con số chính cần nhớ: **Tổng mức đầu tư ban đầu (CAPEX) là 1,309 tỷ đồng**, **Chi phí vận hành định kỳ (OPEX) là 1,123 tỷ/năm**, và **Tổng chi phí sở hữu (TCO) trong chu kỳ 3 năm là 5,209 tỷ đồng**.
>
> TCO 3 năm tương đương khoảng 1,45% tổng doanh thu của chuỗi trong cùng kỳ, nằm hoàn toàn trong biên độ an toàn cho đầu tư CNTT của ngành dịch vụ bán lẻ. Nhìn vào biểu đồ TCO, năm đầu tiên sẽ gánh toàn bộ chi phí CAPEX. Bắt đầu từ năm thứ hai trở đi, chỉ còn chi phí vận hành thuần túy, và đến năm 3 nhóm đã tính cộng thêm 5% trượt giá lạm phát.
>
> Bóc tách cấu thành của CAPEX 1,309 tỷ, có 3 mảng lớn: Phần cứng chiếm 43% (~564,8 triệu), Dịch vụ triển khai và nhân công chiếm 48% (~632 triệu), và Hạ tầng Cloud trong 4 tháng chạy thử nghiệm chiếm 9% (~112 triệu).
>
> Về phần cứng, nó bao gồm 36 bộ Edge Mini Server trang bị UPS cho chi nhánh, 2 bộ Server 2U cấu hình mạnh, Switch và NGFW Firewall đặt tại Trụ sở chính. Các đơn giá phần cứng được nhóm thiết lập dựa trên khảo sát báo giá thực tế thị trường. Biên độ dao động thị trường ±10% cũng đã được nhóm bao hàm bằng một quỹ dự phòng rủi ro kỹ thuật (Contingency) riêng lẻ. Giá chính thức cuối cùng sẽ được chốt qua vòng đấu thầu RFP."

## Trần Anh Tú · Slide 17 (90 giây)

> "Vậy bỏ ra hơn 1,3 tỷ, doanh nghiệp thu lại được gì? Nhóm đã tính toán lợi ích quy đổi thành tiền mặt ước tính đạt **1,955 tỷ đồng mỗi năm**.
>
> Trong đó, lợi ích lớn nhất (700 triệu) đến từ việc thu hồi thất thoát thông qua đối soát tự động. Hiện tại chuỗi đang chịu mức thất thoát ước tính khoảng 1% doanh thu, việc giảm tỉ lệ sai lệch từ 3,8% xuống dưới 0,5% sẽ giúp thu hồi khoản này. Các khoản tiếp theo là: Giảm thiệt hại do gián đoạn hệ thống (400 triệu), Tối ưu quỹ lương vận hành nhờ dự báo lượng khách (400 triệu), Giảm hao hụt nguyên vật liệu F&B (180 triệu), Tăng doanh thu bán chéo nhờ có SSO (150 triệu), và Tiết kiệm 2.500 giờ công làm báo cáo thủ công (125 triệu).
>
> Nếu lấy lợi ích 1,955 tỷ trừ đi OPEX hàng năm là 1,123 tỷ, ta có **dòng tiền ròng tạo ra là 832 triệu đồng/năm**. Với mức đầu tư ban đầu 1,439 tỷ (đã cộng dự phòng), thời gian hoàn vốn trên dòng tiền (Payback period) chỉ khoảng **1,73 năm, tức là 21 tháng**.
>
> Để đảm bảo tính chặt chẽ, nhóm xây dựng thêm một **kịch bản cực kỳ thận trọng**: Nếu loại bỏ hoàn toàn 580 triệu tiền lợi ích có nguồn gốc từ kết quả của mô hình học máy (tối ưu quỹ lương và F&B), thì dòng tiền ròng giảm xuống, khiến thời gian hoàn vốn kéo dài lên 5,7 năm. Tuy nhiên, kể cả trong kịch bản xấu nhất này, nhóm vẫn kiên quyết khuyến nghị phê duyệt đầu tư. Bởi lẽ **giá trị cốt lõi và lớn nhất của dự án không nằm ở việc tiết kiệm chi phí, mà nằm ở việc xóa bỏ rủi ro vi phạm Nghị định 13** — một rủi ro không thể quy đổi ra tiền, nhưng nếu bị thanh tra, mức phạt có thể lên tới 5% doanh thu, tương đương gần 6 tỷ đồng."

> ⚠ **Trần Anh Tú:** phải **chủ động** nêu kịch bản thận trọng, đừng đợi bị vặn.

## Lê Quang Đạt · Slide 18 (90 giây)

> "Em là Lê Quang Đạt. Để hiện thực hóa kiến trúc mục tiêu, nhóm thiết kế lộ trình triển khai gồm **5 pha, kéo dài trong 16 tuần lịch** (tương đương 4 tháng). Do các pha được thiết kế gối đầu nhau 1 tuần để chuẩn bị môi trường, nên tổng thời lượng gộp lại là 20 tuần, trừ đi 4 tuần gối đầu sẽ còn đúng 16 tuần thực tế.
>
> **Pha 1 (3 tuần) - Nền móng:** Nhóm sẽ tập trung thiết lập kết nối VPN bảo mật, cài đặt IAM Keycloak, cấu hình tường lửa NGFW và hệ thống giám sát. Nếu thiếu bước này, các hệ thống phía sau sẽ không có môi trường an toàn để chạy.
>
> **Pha 2 (4 tuần) - Phần lõi (Core):** Triển khai Kubernetes đa vùng, Kafka HA, luồng sao lưu Immutable và DR trên Cloud.
>
> **Pha 3 (4 tuần) - Nâng cấp bảo mật:** Đây là pha bắt đầu đụng đến ứng dụng. Nhóm sẽ tích hợp SSO vào 8 hệ thống hiện có, mã hóa toàn bộ cơ sở dữ liệu PII và thiết lập luồng CDC để đẩy dữ liệu thời gian thực.
>
> **Pha 4 (5 tuần) - Migration & Pilot:** Đây là pha quyết định sự sống còn của dự án. Sau khi migrate dữ liệu lịch sử 12 tháng, nhóm sẽ triển khai Edge Cluster và **chạy Pilot nghiệm thu trên 5 chi nhánh thử nghiệm trong vòng 2 tuần**. Pha này cũng bao gồm kiểm thử bảo mật (Pentest) và UAT.
>
> **Pha 5 (4 tuần) - Tối ưu và Rollout:** Khi Pilot thành công, nhóm mới tự tin rollout ra 29 chi nhánh còn lại, thực hiện diễn tập khôi phục thảm họa (DR Drill), chuyển giao Runbook và bàn giao hệ thống."

## Lê Quang Đạt · Slide 19 (90 giây)

> "Slide cuối cùng trong phần trình bày của em là 4 nhóm nội dung quản trị quan trọng: Rủi ro, Tổ chức (RACI), Mua sắm và Nghiệm thu.
>
> **Về Rủi ro:** Rủi ro cao nhất là việc chậm tích hợp API vì doanh nghiệp đang dùng 8 hệ thống POS từ nhiều nhà cung cấp khác nhau. Biện pháp của nhóm là Pilot tích hợp 2 phần mềm phổ biến nhất trước, và chuẩn bị phương án dùng Adapter Pattern hoặc đọc thẳng vào cơ sở dữ liệu ở chế độ read-only. Rủi ro thứ hai là mô hình AI không đạt ngưỡng, nhóm sẽ xử lý bằng cách tách việc Go-live nền tảng khỏi kết quả của mô hình AI.
>
> **Về Tổ chức RACI:** Sponsor phê duyệt ngân sách và quyết định Go-live; Quản trị viên dự án (PM) chịu trách nhiệm tiến độ. Tuyệt đối không cho phép trôi phạm vi (scope creep); mọi thay đổi bắt buộc phải qua Change Request (CR) trên Jira.
>
> **Về Mua sắm:** Dự án áp dụng chào giá cạnh tranh (RFP) với tối thiểu 3 nhà thầu độc lập. Tiêu chí chấm thầu nghiêng 70% về năng lực kỹ thuật và 30% tài chính. Nhà thầu bắt buộc ký NDA để bảo vệ dữ liệu PII.
>
> **Về Nghiệm thu:** Toàn bộ cam kết được chuyển hóa thành các bài kiểm tra thực tế: Load test API đạt 2.000 người dùng; Ngắt mạng chi nhánh 4 giờ để kiểm tra đồng bộ offline; Diễn tập DR đảm bảo RTO dưới 4 giờ và RPO dưới 15 phút; và báo cáo Pentest không được phép tồn tại lỗ hổng Critical hay High. Mọi con số đều được kiểm chứng độc lập chứ không nghiệm thu trên giấy."

## Phạm Minh Mẫn · Slide 20 (55 giây)

> "Em xin kết luận. Nhóm 5 đề xuất phê duyệt chủ trương đầu tư dự án này với bốn lý do cốt lõi.
>
> Một, dự án giải quyết triệt để ba vấn đề gốc rễ đã được khảo sát thực tế có số liệu định lượng và có minh chứng rõ ràng.
>
> Hai, kiến trúc Hybrid Cloud là phương án duy nhất đạt 6/6 tiêu chí bắt buộc, và lựa chọn này hoàn toàn xuất phát từ đặc thù nghiệp vụ của doanh nghiệp.
>
> Ba, toàn bộ các cam kết kỹ thuật đều được gắn với chỉ số đo lường chuẩn quốc tế để có thể nghiệm thu khách quan.
>
> Bốn, dự án rất khả thi về mặt tài chính: TCO 3 năm chỉ chiếm khoảng 1,45% doanh thu và hoàn vốn nhanh trong vòng 1,7 năm.
>
> Phần báo cáo đồ án môn học của nhóm 5 đến đây là hết. Nhóm em xin chân thành cảm ơn cô đã lắng nghe."

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
