## Phân công

| Người | Slide | Nội dung | Thời lượng |
|:---|:---:|:---|:---:|
| Phạm Minh Mẫn — Nhóm trưởng | 1–3 | Mở đầu, phân công, tóm tắt điều hành | 2'00" |
| Đặng Nguyễn Minh Anh | 4–5 | Bối cảnh doanh nghiệp, kiến trúc AS-IS | 2'00" |
| Trần Văn Phây | 6–7 | Ba điểm nghẽn định lượng, minh chứng | 1'35" |
| Huỳnh Thị Kiều Uyên | 8–9 | Rủi ro nếu không đầu tư, phạm vi lớp năng lực | 1'40" |
| Trần Việt Đức | 10–11 | Bộ 6 KPI, phương pháp đo lường | 1'50" |
| Nguyễn Đức Huy | 12–13 | Ba kịch bản, cơ sở chọn Hybrid Cloud | 1'45" |
| Vũ Duy | 14–15 | Kiến trúc TO-BE, yêu cầu kỹ thuật, BOM | 1'50" |
| Trần Anh Tú | 16–17 | CAPEX/OPEX/TCO, hiệu quả đầu tư | 2'00" |
| Lê Quang Đạt | 18–19 | Lộ trình, rủi ro, RACI, mua sắm, nghiệm thu | 1'50" |
| Phạm Minh Mẫn — Nhóm trưởng | 20 | Kết luận | 0'45" |

## Phạm Minh Mẫn · Slide 1 (40 giây)

> "Kính chào cô. Em là Phạm Minh Mẫn, nhóm trưởng nhóm 5. Nhóm em xin báo cáo **đồ án môn học**: đề xuất đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station.
>
> Tổng mức đầu tư ban đầu là 1,309 tỷ đồng, tổng chi phí sở hữu 3 năm là 5,209 tỷ, triển khai trong 16 tuần."

## Phạm Minh Mẫn · Slide 2 (25 giây)

> "Nhóm 9 bạn, mỗi bạn phụ trách một mục và trực tiếp báo cáo phần mình làm."

## Phạm Minh Mẫn · Slide 3 (55 giây)

> "Trước khi vào chi tiết, em tóm tắt toàn bộ đề xuất trong một slide.
>
> **Vấn đề:** 34 chi nhánh, 8 hệ thống rời rạc, không có luồng tích hợp tự động nào, dữ liệu trễ 24 đến 48 giờ, và dữ liệu cá nhân của khách hàng chưa được mã hóa.
>
> **Giải pháp:** đầu tư Lớp 4 là nền tảng tích hợp ứng dụng, Lớp 5 là nền tảng dữ liệu, cộng 02 thành phần của Lớp 3, theo kiến trúc Hybrid Cloud.
>
> **Ngân sách:** CAPEX 1,309 tỷ, OPEX 1,123 tỷ mỗi năm, TCO 3 năm 5,209 tỷ — tương đương khoảng 1,45% doanh thu chuỗi trong cùng kỳ.
>
> **Lợi ích:** quy đổi khoảng 1,955 tỷ mỗi năm, hoàn vốn khoảng 1,7 năm, và quan trọng nhất là loại bỏ rủi ro vi phạm Nghị định 13.
>
> Nhóm em khuyến nghị phê duyệt chủ trương đầu tư và khởi động Pha 1 trong quý tới."

## Đặng Nguyễn Minh Anh · Slide 4 (60 giây)

> "Em là Đặng Nguyễn Minh Anh. Em nói về doanh nghiệp trước, vì **chính đặc điểm doanh nghiệp quyết định lựa chọn kỹ thuật**, chứ không phải nhóm chọn công nghệ trước.
>
> Ways Station có 34 chi nhánh, tăng từ 22 trong khoảng 2 năm, mỗi chi nhánh vận hành cùng lúc 5 mảng dịch vụ, khoảng 300 nhân sự theo ca.
>
> Ba đặc điểm chi phối toàn bộ bài toán.
>
> Một, **mỗi chi nhánh là một hộ kinh doanh cá thể riêng biệt** — không có pháp nhân trung tâm sở hữu kho dữ liệu chung, nên hạ tầng bị chia thành 34 ốc đảo.
>
> Hai, **doanh thu tính theo giờ sử dụng** — mất mạng vài phút là không tính được tiền, không trả được bàn hay trả xe.
>
> Ba, doanh nghiệp **thu thập dữ liệu cá nhân nhạy cảm ngay tại quầy**: ảnh căn cước, cà vẹt xe, và Face ID hội viên.
>
> Ba đặc điểm này sẽ quay lại ở phần chọn kiến trúc."

## Đặng Nguyễn Minh Anh · Slide 5 (60 giây)

> "Đây là kiến trúc hiện tại. 34 chi nhánh, mỗi nơi chạy các phần mềm riêng — POS cho net và bida, phần mềm MODUN cho gym, ACB portal, phần mềm kho, và sổ giao ca giấy. **Các hệ thống không nối với nhau, tỉ lệ tích hợp tự động là 0%.**
>
> Toàn bộ giao tiếp giữa chi nhánh và trụ sở đi qua ba kênh thủ công: một tổng đài duy nhất phân luồng theo phím số, Zalo cá nhân, và sổ giấy.
>
> Hệ quả: không có định danh duy nhất nên không bán chéo được dịch vụ; phát hiện sự cố mất 4 đến 8 giờ vì phụ thuộc nhân viên báo qua Zalo; sao lưu cục bộ chỉ thành công 47%."

## Trần Văn Phây · Slide 6 (50 giây)

> "Em là Trần Văn Phây. Nhóm em quy ba điểm nghẽn về đúng ba lớp năng lực sẽ đầu tư, **mỗi điểm nghẽn đều có số làm baseline**.
>
> Lớp 4: 0% tự động, 8 hệ thống rời rạc, phát hiện sự cố 4–8 giờ.
> Lớp 5: khoảng 2.500 giờ công Excel mỗi năm, dữ liệu trễ 24–48 giờ, sai lệch đối soát doanh thu 3,8%.
> Lớp 3: mã hóa PII (Personally Identifiable Information) bằng 0%, backup thành công 47%, RPO 24 giờ.
>
> Về nguồn số liệu, nhóm không có quyền truy cập hệ thống vận hành thật nên dùng **phương pháp mô phỏng có căn cứ**, kết hợp tài liệu quy trình nội bộ, chuẩn ngành, và nguyên lý kỹ thuật phổ quát."

## Trần Văn Phây · Slide 7 (45 giây)

> "Đây là phần minh chứng. Các khẳng định về hiện trạng **dẫn từ 8 bộ tài liệu quy trình đang áp dụng tại chi nhánh Ways Station**.
>
> Tài liệu thu ngân ghi bộ phận kho phụ trách *hỗ trợ đăng nhập PM (Project Manager) MODUN gym và ACB portal* — minh chứng cho phần mềm rời rạc, không có SSO (Single Sign-On).
>
> Tài liệu giữ xe ghi quy trình khi khách mất thẻ là chụp ảnh căn cước và cà vẹt xe rồi *gửi qua Zalo cho Quản lý* — minh chứng trực tiếp cho rủi ro dữ liệu cá nhân.
>
> Và tài liệu thu ngân gym cho thấy phòng tập *check-in bằng Face ID*, tức doanh nghiệp đang thu thập dữ liệu sinh trắc học.
>
> Đầy đủ 10 dòng minh chứng nằm ở Phụ lục A của báo cáo."

## Huỳnh Thị Kiều Uyên · Slide 8 (50 giây)

> "Em là Huỳnh Thị Kiều Uyên. Rủi ro nếu không đầu tư chia ba nhóm.
>
> Vận hành: nghẽn tải giờ cao điểm gây gián đoạn bán hàng, hàng ngàn giờ công lãng phí vì đối soát và nhập liệu kép.
>
> Chiến lược: độ trễ 48 giờ khiến quyết định luôn đi sau thực tế, không dự báo được nhu cầu nên lãng phí nguyên vật liệu và xếp ca sai.
>
> Nhưng **nghiêm trọng nhất là rủi ro tuân thủ**. Lưu ảnh căn cước và Face ID phân tán trên điện thoại cá nhân vi phạm Nghị định 13, mức phạt có thể lên tới 5% tổng doanh thu. Và mức phơi nhiễm **tăng tuyến tính theo số lượt khách và số chi nhánh mới** — đây là lý do phải làm ngay."

## Huỳnh Thị Kiều Uyên · Slide 9 (50 giây)

> "Về phạm vi, nhóm **đầu tư theo lớp năng lực**, không mua thiết bị rời rạc.
>
> Trọng tâm là Lớp 4 và Lớp 5. Ngoài ra nhóm khai báo thêm **đúng 02 thành phần của Lớp 3**: quản lý định danh và mã hóa dữ liệu cá nhân — vì vấn đề rò rỉ PII **không thể giải quyết chỉ bằng Lớp 4 và Lớp 5**. Các thành phần khác của Lớp 3 như PAM (Privileged Access Management), EDR (Endpoint Detection and Response), SIEM (Security Information and Event Management), DLP (Data Loss Prevention) thì ghi rõ là ngoài phạm vi, chưa đầu tư kỳ này.
>
> Nhờ vậy toàn bộ KPI bảo mật và các yêu cầu kỹ thuật nhóm bảo mật đều nằm trong phạm vi đã cam kết, thống nhất từ trên xuống dưới."

## Trần Việt Đức · Slide 10 (60 giây)

> "Em là Trần Việt Đức. Nhóm em có **ba mục tiêu tương ứng ba vấn đề, mỗi mục tiêu hai KPI**, tổng sáu KPI.
>
> Vấn đề đứt gãy tích hợp: Uptime từ không đo lường được lên 99,99%, MTTR (Mean Time To Recovery) từ 12–24 giờ xuống dưới 30 phút.
>
> Vấn đề mù dữ liệu: độ trễ dữ liệu từ 24–48 giờ xuống 5 giây, và độ đầy đủ dữ liệu đạt 99,5%, kéo sai lệch đối soát doanh thu từ 3,8% xuống dưới 0,5%.
>
> Vấn đề rò rỉ PII: tỷ lệ mã hóa từ 0% lên 100%, RPO từ 24 giờ xuống 15 phút.
>
> Mỗi KPI đều có đủ bốn thứ: **baseline, target, mốc đo và người chịu trách nhiệm số liệu**. Mốc đo là tại go-live rồi đo lại tại 1, 3, 6 tháng sau.
>
> Tiêu chí thành công: đạt 6 trên 6 KPI tại go-live, giữ tối thiểu 5 trên 6 tại mốc 3 tháng."

## Trần Việt Đức · Slide 11 (50 giây)

> "Về phương pháp đo, nhóm **không tự đặt độ đo bằng lời** mà dùng khung đã chuẩn hóa quốc tế và trích dẫn ngay tại vị trí sử dụng.
>
> Uptime theo Google SRE, có công thức và ràng buộc downtime không quá 4,32 phút mỗi tháng. MTTR theo Atlassian ITSM. Độ trễ và độ đầy đủ dữ liệu theo ISO/IEC 25012. Tỷ lệ mã hóa theo NIST SP 800-175B. RPO theo khung Disaster Recovery của AWS.
>
> Nhờ dùng chuẩn có sẵn nên mỗi chỉ số đều có công thức toán học rõ ràng và **nghiệm thu được**, không phải cam kết suông."

## Nguyễn Đức Huy · Slide 12 (45 giây)

> "Em là Nguyễn Đức Huy. Nhóm phân tích ba kịch bản kiến trúc, mỗi kịch bản trong báo cáo đều mô tả đầy đủ kiến trúc theo lớp, điểm HA (High Availability)/DR (Disaster Recovery), khả năng tích hợp và mở rộng.
>
> Đối chiếu sáu tiêu chí bắt buộc: **On-Premise chỉ đạt 2 trên 6** — được offline và tuân thủ nhưng CAPEX quá cao, không co giãn. **Cloud-Native đạt 4 trên 6** — mạnh về co giãn và khôi phục thảm họa nhưng hỏng đúng hai tiêu chí cứng là offline và vị trí lưu trữ dữ liệu cá nhân.
>
> **Chỉ Hybrid Cloud đạt 6 trên 6.**"

## Nguyễn Đức Huy · Slide 13 (60 giây)

> "Nhưng đạt 6 trên 6 chưa đủ thuyết phục. Câu hỏi quan trọng hơn là **sáu tiêu chí đó từ đâu ra và có đúng với doanh nghiệp này không**.
>
> Chúng được rút ra trực tiếp từ bốn đặc điểm của Ways Station.
>
> Doanh thu tính theo giờ, tính tiền tại quầy — mất mạng là mất doanh thu ngay. Đặc điểm này **loại Cloud-Native**.
>
> 34 hộ kinh doanh riêng, mặt bằng thuê, không có phòng máy chủ và không có IT thường trực — không thể vận hành cụm máy chủ đầy đủ tại 34 điểm. Đặc điểm này **loại On-Premise**.
>
> Thu thập căn cước và Face ID tại quầy — dữ liệu định danh phải nằm dưới quyền kiểm soát trực tiếp của doanh nghiệp. Lại **loại Cloud-Native**.
>
> Tăng trưởng 22 lên 34 chi nhánh trong hai năm, tải biến động mạnh — cần co giãn và nhân bản chi nhánh mới trong vài giờ. Lại **loại On-Premise**.
>
> Kết luận: Hybrid Cloud là phương án duy nhất thỏa mãn đồng thời cả bốn. **Đây là lựa chọn bị ràng buộc bởi doanh nghiệp, không phải theo xu hướng công nghệ.**"

> ⚠ **Nguyễn Đức Huy:** slide quan trọng nhất cả video. Đây là điểm cô yêu cầu nhóm bổ sung ở Buổi 6.

## Vũ Duy · Slide 14 (60 giây)

> "Em là Vũ Duy. Kiến trúc mục tiêu chia ba khối.
>
> **Trên Public Cloud** đặt Lớp 4 và Lớp 5: API Gateway có xác thực JWT và giới hạn tải, cụm Kafka với replication factor 3, Data Lakehouse và PostgreSQL HA, Airflow, dịch vụ suy luận AI, và hệ giám sát.
>
> **Tại trụ sở chính**, nhóm giữ lại đúng phần nhạy cảm nhất: Keycloak cho định danh tập trung và cơ sở dữ liệu PII mã hóa AES (Advanced Encryption Standard)-256, đặt sau tường lửa, nối lên Cloud qua VPN.
>
> **Tại 34 chi nhánh** là Edge Cluster chạy K3s cùng Kafka broker con và cache cục bộ, có UPS. Khi mất mạng, phần mềm vẫn gọi API cục bộ để tính tiền; có mạng lại thì dữ liệu tự đồng bộ bù về Cloud.
>
> Điểm mấu chốt: **dữ liệu PII không rời khỏi On-Premise, dữ liệu vận hành được ẩn danh trước khi đẩy lên Cloud.** Đây là cách nhóm vừa đạt yêu cầu offline vừa tuân thủ Nghị định 13."

## Vũ Duy · Slide 15 (50 giây)

> "Từ kiến trúc đó, nhóm chuẩn hóa yêu cầu kỹ thuật thành bốn nhóm, tổng 28 yêu cầu, **mỗi yêu cầu có ngưỡng đo và tiêu chí nghiệm thu, truy vết ngược về đúng KPI**.
>
> Hiệu năng: API chịu 2.000 kết nối đồng thời, P95 dưới 200 mili-giây, CDC (Change Data Capture) tối thiểu 5.000 sự kiện mỗi giây. HA/DR: đa vùng Active-Active, chuyển đổi dưới 60 giây, hàng đợi tại chi nhánh chứa 48 giờ giao dịch. Bảo mật: SSO cho 100% ứng dụng, MFA (Multi-Factor Authentication) cho admin, AES-256 và TLS 1.2 trở lên. Vận hành: giám sát, cảnh báo dưới 5 phút, CMDB (Configuration Management Database), hạ tầng dạng mã cho phép rollback dưới 15 phút.
>
> Về danh mục đầu tư, **toàn bộ phần mềm nền tảng là mã nguồn mở** nên chi phí bản quyền bằng 0, phù hợp ngân sách doanh nghiệp vừa."

## Trần Anh Tú · Slide 16 (60 giây)

> "Em là Trần Anh Tú. Ba con số chính: **CAPEX 1,309 tỷ**, **OPEX 1,123 tỷ mỗi năm**, **TCO 3 năm 5,209 tỷ** — tương đương khoảng 1,45% doanh thu chuỗi cùng kỳ.
>
> Biểu đồ cho thấy năm 1 gánh toàn bộ CAPEX, từ năm 2 chỉ còn chi phí vận hành, năm 3 cộng thêm 5% trượt giá.
>
> Cấu thành CAPEX: phần cứng 43%, dịch vụ triển khai và nhân công 48%, hạ tầng Cloud trong 4 tháng triển khai 9%.
>
> Đơn giá phần cứng dựa trên khảo sát giá thị trường, biên độ dao động 10% đã được hấp thụ bởi quỹ dự phòng; giá chính thức chốt qua vòng chào giá cạnh tranh."

## Trần Anh Tú · Slide 17 (60 giây)

> "Về hiệu quả đầu tư, nhóm quy đổi được **khoảng 1,955 tỷ lợi ích mỗi năm**.
>
> Lớn nhất là thu hồi thất thoát nhờ đối soát tự động — 700 triệu, trên cơ sở thất thoát thực ước tính khoảng 1% doanh thu. Tiếp theo là giảm thiệt hại downtime 400 triệu, tối ưu giờ công nhờ dự báo 400 triệu, giảm hao hụt F&B (Food and Beverage) 180 triệu, bán chéo nhờ SSO 150 triệu, và giảm giờ công làm báo cáo 125 triệu.
>
> Trừ OPEX 1,123 tỷ thì **dòng tiền ròng là 832 triệu mỗi năm**, hoàn vốn khoảng **1,73 năm**.
>
> Nhóm cũng tính sẵn **kịch bản thận trọng**: nếu loại hoàn toàn hai dòng phụ thuộc chất lượng mô hình AI, tổng 580 triệu, thì payback kéo dài khoảng 5,7 năm. Kể cả vậy nhóm vẫn khuyến nghị phê duyệt, vì **giá trị lớn nhất là tránh rủi ro vi phạm Nghị định 13** — thứ không quy đổi ra tiền được nhưng mức phạt có thể tới 5% doanh thu."

> ⚠ **Trần Anh Tú:** phải **chủ động** nêu kịch bản thận trọng, đừng đợi bị vặn.

## Lê Quang Đạt · Slide 18 (55 giây)

> "Em là Lê Quang Đạt. Dự án chia 5 pha trong 16 tuần.
>
> Pha 1 ba tuần đầu là nền móng: VPN, Keycloak, tường lửa, hệ giám sát. Pha 2 bốn tuần là phần lõi: Kubernetes đa vùng, Kafka HA, backup và DR. Pha 3 bốn tuần là nâng cấp bảo mật: tích hợp SSO vào 8 hệ thống, mã hóa PII, dựng luồng CDC.
>
> **Pha 4 là quan trọng nhất** — migrate dữ liệu 12 tháng, triển khai 34 Edge, và đặc biệt là **Pilot 5 chi nhánh trong 2 tuần trước khi rollout toàn bộ**, kèm pentest và UAT. Pha 5 rollout 29 chi nhánh còn lại rồi chuyển giao.
>
> Về tổng thời gian, các pha **gối đầu một tuần**, nên tổng danh nghĩa 20 tuần rút còn 16 tuần lịch. Mỗi pha có tiêu chí hoàn thành và kế hoạch dự phòng riêng."

## Lê Quang Đạt · Slide 19 (55 giây)

> "Bốn nội dung quản trị cuối.
>
> **Rủi ro cao nhất** là chậm tích hợp API vì 8 hệ thống POS từ nhiều nhà cung cấp. Biện pháp: pilot hai hệ thống phổ biến nhất trước, dùng adapter pattern, và nếu vẫn tắc thì đọc trực tiếp cơ sở dữ liệu ở chế độ chỉ đọc. Rủi ro thứ hai là mô hình AI không đạt ngưỡng — xử lý bằng cách **tách go-live nền tảng khỏi kết quả AI**.
>
> **Tổ chức:** Sponsor duyệt ngân sách và go-live, PM chịu trách nhiệm tiến độ. Mọi thay đổi phạm vi phải qua Change Request trên Jira.
>
> **Mua sắm:** chào giá cạnh tranh, tối thiểu 3 nhà thầu, chấm 70% kỹ thuật 30% tài chính, ràng buộc SLA, NDA (Non-Disclosure Agreement) theo Nghị định 13, bảo hành 12 tháng.
>
> **Nghiệm thu:** load test 2.000 người dùng, ngắt mạng chi nhánh 4 giờ, diễn tập DR với RTO dưới 4 giờ và RPO dưới 15 phút, pentest không còn lỗi Critical hay High. Toàn bộ là con số kiểm chứng được."

## Phạm Minh Mẫn · Slide 20 (45 giây)

> "Em xin kết luận. Nhóm em đề xuất phê duyệt chủ trương đầu tư, với bốn lý do.
>
> Một, dự án giải quyết đúng ba vấn đề gốc đã khảo sát có số liệu và có minh chứng.
>
> Hai, Hybrid Cloud là phương án duy nhất đạt 6 trên 6 tiêu chí bắt buộc, và lựa chọn xuất phát từ đặc điểm thật của doanh nghiệp.
>
> Ba, toàn bộ cam kết đều có số để nghiệm thu.
>
> Bốn, khả thi tài chính: TCO 3 năm khoảng 1,45% doanh thu, hoàn vốn khoảng 1,7 năm.
>
> Phần báo cáo đồ án môn học của nhóm 5 đến đây là hết. Nhóm em xin cảm ơn cô."

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
