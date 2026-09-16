# KỊCH BẢN TRÌNH BÀY ĐỒ ÁN MÔN HỌC
**Dự án:** Đầu tư hạ tầng CNTT - Ways Station
**Tổng thời gian:** 45 phút
**Số người trình bày:** 9 người (Mỗi người 5 phút)
*Lưu ý: Tốc độ nói trung bình là 120-130 từ/phút. Kịch bản dưới đây được thiết kế sát với thời lượng 5 phút cho mỗi người, sử dụng văn phong kỹ thuật, chuyên nghiệp.*

---

## NGƯỜI 1: GIỚI THIỆU & TÓM TẮT DỰ ÁN (Slide 1, 2, 3)

**[Slide 1: Tiêu đề]**
Kính chào Hội đồng. Đại diện Nhóm 5, em là [Tên Người 1], xin phép trình bày Đồ án môn học: Đề xuất đầu tư Nền tảng tích hợp ứng dụng và Nền tảng dữ liệu tập trung cho chuỗi Ways Station. Nội dung trình bày trong 45 phút sắp tới sẽ bao gồm: phân tích hiện trạng, đề xuất kiến trúc giải pháp, tính toán ngân sách và lộ trình triển khai. Em xin phép bắt đầu với phần Tóm tắt dự án.

**[Slide 2: Tóm tắt dự án]**
Ways Station là hệ sinh thái dịch vụ tích hợp đa nền tảng đang vận hành với quy mô 34 chi nhánh. Sự mở rộng quy mô này dẫn đến tình trạng phân mảnh hạ tầng, đứt gãy tích hợp hệ thống, và phát sinh rủi ro rò rỉ dữ liệu định danh cá nhân (PII), vi phạm Nghị định 13/2023/NĐ-CP.
Để giải quyết các vấn đề này, dự án đề xuất triển khai 3 lớp năng lực hạ tầng: Lớp 4 - Nền tảng tích hợp ứng dụng, Lớp 5 - Nền tảng dữ liệu tập trung, và 02 thành phần thuộc Lớp 3 là Quản lý định danh IAM và Mã hóa dữ liệu. Kiến trúc Hybrid Cloud được lựa chọn làm giải pháp cốt lõi để đáp ứng đồng thời tính linh hoạt và các ràng buộc về bảo mật.

**[Slide 3: Tổng quan Đầu tư & Hiệu quả]**
Tổng mức đầu tư ban đầu (CAPEX) của dự án là khoảng 1,3 tỷ VNĐ. Tổng chi phí sở hữu (TCO) trong 3 năm dự toán là 5,2 tỷ VNĐ, tương đương 1,45% tổng doanh thu dự kiến của chuỗi trong cùng kỳ.
Thời gian hoàn vốn trên dòng tiền ròng ước tính đạt 1,7 năm. Quan trọng hơn, việc triển khai giải pháp sẽ đảm bảo tính tuân thủ pháp lý, ngăn ngừa chế tài xử phạt lên đến 5% tổng doanh thu. Tiếp theo, bạn [Tên Người 2] sẽ trình bày chi tiết về hiện trạng hệ thống.

---

## NGƯỜI 2: HIỆN TRẠNG & VẤN ĐỀ VẬN HÀNH (Slide 4, 5)

**[Slide 4: Hiện trạng AS-IS]**
Cảm ơn bạn. Kính chào Hội đồng, em là [Tên Người 2], xin tiếp tục trình bày về hiện trạng hạ tầng của Ways Station. Đặc thù pháp lý của hệ thống là 34 chi nhánh hoạt động dưới hình thức hộ kinh doanh độc lập, không tồn tại trung tâm dữ liệu dùng chung.
Mỗi chi nhánh đang vận hành 8 hệ thống phần mềm riêng biệt phục vụ các mảng dịch vụ khác nhau. Tỉ lệ tích hợp tự động (API) giữa các phần mềm hiện là 0%. Toàn bộ quy trình đồng bộ dữ liệu với Trụ sở chính (HQ) đều thực hiện thủ công thông qua tổng đài, ứng dụng nhắn tin cá nhân hoặc ghi chép sổ sách.

**[Slide 5: Vấn đề 1 - Đứt gãy tích hợp]**
Hạn chế đầu tiên là tình trạng đứt gãy tích hợp. Do thiếu API Gateway, hệ thống không có khả năng tự động mở rộng theo tải thực tế (auto-scaling) và sức chịu tải rất kém, thường xuyên dẫn đến gián đoạn dịch vụ vào giờ cao điểm.
Đồng thời, do thiếu hệ thống giám sát tự động, thời gian phát hiện sự cố (MTTD) kéo dài từ 4 đến 8 giờ, phụ thuộc hoàn toàn vào phản hồi thủ công từ nhân viên chi nhánh. Hệ quả là làm gián đoạn luồng giao dịch, gây thất thoát doanh thu và tiêu tốn hàng ngàn giờ công cho việc đối soát dữ liệu thủ công. Tiếp theo, mời bạn [Tên Người 3] phân tích các vấn đề về dữ liệu và bảo mật.

---

## NGƯỜI 3: VẤN ĐỀ DỮ LIỆU & BẢO MẬT (Slide 6, 7)

**[Slide 6: Vấn đề 2 - Phân mảnh dữ liệu]**
Kính chào Hội đồng, em là [Tên Người 3], xin tiếp nối phần trình bày với vấn đề phân mảnh dữ liệu. Ways Station hiện chưa triển khai Kho dữ liệu (Data Warehouse) tập trung. Quá trình tổng hợp báo cáo kinh doanh được thực hiện thủ công qua Excel từ dữ liệu của 8 phần mềm, tiêu tốn khoảng 2.500 giờ công mỗi năm.
Độ trễ dữ liệu thực tế lên tới 24 đến 48 giờ. Hạn chế này dẫn đến sai lệch đối soát doanh thu ở mức 3,8%, gây hao hụt nguyên vật liệu do không thể dự báo nhu cầu chính xác, và hạn chế khả năng triển khai các chiến dịch bán chéo dịch vụ.

**[Slide 7: Vấn đề 3 - Rủi ro bảo mật PII]**
Vấn đề nghiêm trọng nhất là rủi ro rò rỉ dữ liệu định danh cá nhân (PII). Quá trình lưu trữ thông tin nhạy cảm của khách hàng như Căn cước công dân và sinh trắc học (Face ID) hiện không áp dụng bất kỳ tiêu chuẩn mã hóa nào.
Tỉ lệ sao lưu thành công trên hệ thống cũ chỉ đạt 47%, với Mục tiêu thời gian phục hồi (RPO) lên tới 24 giờ. Rủi ro này không chỉ dẫn đến khả năng mất mát dữ liệu mà còn trực tiếp vi phạm Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân. Bạn [Tên Người 4] sẽ trình bày chi tiết về bộ Mục tiêu TO-BE.

---

## NGƯỜI 4: MỤC TIÊU KIẾN TRÚC & KPI (Slide 8, 9)

**[Slide 8: Mục tiêu Kiến trúc & KPI - Phần 1]**
Kính chào Hội đồng, em là [Tên Người 4]. Để khắc phục các hạn chế hiện tại, nhóm đã thiết lập bộ KPI kỹ thuật dựa trên tiêu chuẩn Google SRE và Atlassian ITSM.
- **KPI 1.1:** Độ sẵn sàng hệ thống (Uptime) phải đạt mức tối thiểu 99,99%, tương đương tổng thời gian gián đoạn (Downtime) không vượt quá 4,32 phút/tháng.
- **KPI 1.2:** Thời gian phục hồi trung bình (MTTR) được kiểm soát dưới 30 phút thông qua cơ chế tự phục hồi (Self-healing).
- **KPI 2.1:** Độ trễ dữ liệu của luồng thu thập sự kiện theo thời gian thực (CDC Streaming) từ chi nhánh lên Data Lakehouse không vượt quá 5 giây.

**[Slide 9: Mục tiêu Kiến trúc & KPI - Phần 2]**
- **KPI 2.2:** Chất lượng dữ liệu (Completeness) phải đạt mức tối thiểu 99,5%, nhằm mục tiêu giảm biên độ sai lệch đối soát doanh thu xuống dưới 0,5%.
- **KPI 3.1:** 100% dữ liệu PII phải được mã hóa theo chuẩn AES-256 ở cả hai trạng thái lưu trữ (at-rest) và truyền tải (in-transit).
- **KPI 3.2:** Khả năng khôi phục thảm họa với mức RPO tối đa là 15 phút, đảm bảo dung sai mất mát dữ liệu thấp nhất khi có sự cố vật lý. Phần định nghĩa phạm vi đầu tư sẽ do bạn [Tên Người 5] trình bày.

---

## NGƯỜI 5: PHẠM VI & RÀNG BUỘC (Slide 10, 11)

**[Slide 10: Phạm vi Đầu tư]**
Xin cảm ơn. Kính thưa Hội đồng, em là [Tên Người 5]. Để tối ưu hóa ngân sách, dự án được giới hạn trong phạm vi các lớp nền tảng cốt lõi:
- **Lớp 4 (Tích hợp):** Triển khai API Gateway, Message Queue (Kafka) và hạ tầng Container hóa (Cloud Kubernetes và Edge K3s).
- **Lớp 5 (Dữ liệu):** Triển khai Data Lakehouse, luồng xử lý ETL (Airflow) và CDC Streaming.
- **Lớp 3 (Bảo mật):** Tích hợp giải pháp định danh tập trung (Keycloak) và cơ chế mã hóa dữ liệu.
Các hạng mục như mạng truyền dẫn lõi, máy chủ lưu trữ chuyên dụng (NAS/SAN) hay hệ thống phân tích bảo mật tập trung (SOC/SIEM) không nằm trong phạm vi đầu tư của giai đoạn này.

**[Slide 11: Giả định & Ràng buộc]**
Kiến trúc giải pháp được thiết kế dựa trên các ràng buộc nghiệp vụ sau:
- Thứ nhất, duy trì cấu trúc pháp lý hiện hành của 34 hộ kinh doanh độc lập.
- Thứ hai, yêu cầu tính sẵn sàng ngoại tuyến (Offline mode): Hệ thống máy bán hàng (POS) tại chi nhánh phải duy trì hoạt động giao dịch ngay cả khi gián đoạn kết nối diện rộng.
- Thứ ba, tuân thủ lưu trữ dữ liệu PII cục bộ tại hệ thống máy chủ do Trụ sở chính quản lý, nằm trong lãnh thổ Việt Nam.
Bên cạnh đó, giải pháp phải tính đến đặc thù không triển khai nhân sự IT trực tiếp tại chi nhánh. Mời bạn [Tên Người 6] đánh giá các phương án kiến trúc.

---

## NGƯỜI 6: ĐÁNH GIÁ & LỰA CHỌN KỊCH BẢN (Slide 12, 13)

**[Slide 12: Đánh giá 3 Kịch bản]**
Kính chào Hội đồng, em là [Tên Người 6]. Từ các ràng buộc đã nêu, nhóm thực hiện phân tích 3 kịch bản kiến trúc:
- **Kịch bản A (On-Premise 100%):** Ưu điểm là đáp ứng yêu cầu vận hành ngoại tuyến và tuân thủ pháp lý. Tuy nhiên, CAPEX rất cao và hệ thống thiếu khả năng tự động mở rộng theo tải thực tế.
- **Kịch bản B (Cloud-Native 100%):** Tối ưu về mặt chi phí và khả năng mở rộng. Dù vậy, rủi ro lớn nhất là sự phụ thuộc hoàn toàn vào kết nối mạng, đồng thời không đáp ứng tiêu chuẩn lưu trữ PII theo quy định pháp luật hiện hành.
- **Kịch bản C (Hybrid Cloud):** Là phương án được đề xuất, do đáp ứng đầy đủ cả 6 tiêu chí đánh giá về kỹ thuật và nghiệp vụ.

**[Slide 13: Tại sao chọn Hybrid Cloud?]**
Mô hình Hybrid Cloud phân bổ luồng xử lý một cách tối ưu:
- **Xử lý tập trung (Public Cloud):** Quản lý luồng truy xuất API và Data Lakehouse, tận dụng khả năng tự động co giãn tài nguyên.
- **Xử lý biên (Edge):** Triển khai các cụm máy chủ cục bộ tại 34 chi nhánh để lưu đệm dữ liệu (Store-and-Forward), duy trì giao dịch khi kết nối mạng bị gián đoạn và tự động đồng bộ khi khôi phục mạng.
- **Xử lý bảo mật (On-Premise):** Triển khai hệ thống định danh SSO và Cơ sở dữ liệu PII tại Trụ sở chính, áp dụng chuẩn mã hóa 100% nhằm đảm bảo tuân thủ tính pháp lý. Sau đây, bạn [Tên Người 7] sẽ phân tích chi tiết thiết kế kỹ thuật.

---

## NGƯỜI 7: KIẾN TRÚC TO-BE & YÊU CẦU KỸ THUẬT (Slide 14, 15)

**[Slide 14: Sơ đồ Kiến trúc TO-BE]**
Kính chào Hội đồng, em là [Tên Người 7], xin trình bày về Sơ đồ kiến trúc Hybrid Cloud được thiết kế với 3 phân vùng chính:
1. **Phân vùng Public Cloud:** Vận hành cụm Kubernetes theo mô hình Active-Active, luồng Apache Airflow và Kho dữ liệu.
2. **Phân vùng Biên (Edge):** Cấu hình hệ điều hành K3s tối giản. Tại đây, hệ thống thực hiện nghiệp vụ ẩn danh hóa dữ liệu trước khi chuyển tiếp qua luồng streaming về Cloud.
3. **Phân vùng On-Premise (HQ):** Đây là phân vùng có mức độ bảo mật cao nhất, trực tiếp quản lý Keycloak IAM. Mọi truy vấn sinh trắc học đều được đối chiếu và xử lý nội bộ, cô lập hoàn toàn với môi trường bên ngoài.

**[Slide 15: Yêu cầu Kỹ thuật Trọng yếu]**
Hệ thống phải tuân thủ các Cam kết chất lượng dịch vụ (SLA) nghiêm ngặt:
- **Về Hiệu năng:** API Gateway phải chịu tải tối thiểu 2.000 kết nối đồng thời, với độ trễ (P95) dưới 200 mili-giây.
- **Về Độ sẵn sàng (HA/DR):** Cụm Cloud phân tách làm 2 vùng khả dụng, đảm bảo thời gian chuyển đổi dự phòng (failover) dưới 60 giây. Thiết bị Edge phải đủ dung lượng lưu đệm cho 48 giờ giao dịch liên tục.
- **Về Bảo mật:** Toàn bộ liên kết hệ thống sử dụng giao thức TLS 1.2 trở lên, 100% ứng dụng nội bộ phải tích hợp SSO và xác thực đa yếu tố (MFA). Tiếp theo, bạn [Tên Người 8] sẽ trình bày chi tiết về dự toán ngân sách dự án.

---

## NGƯỜI 8: NGÂN SÁCH & HIỆU QUẢ ĐẦU TƯ (Slide 16, 17)

**[Slide 16: Dự toán Ngân sách (CAPEX & OPEX)]**
Kính thưa Hội đồng, em là [Tên Người 8]. Về cơ cấu chi phí, nhóm đã lập dự toán dựa trên khảo sát báo giá thực tế:
- **Chi phí đầu tư ban đầu (CAPEX):** Ước tính 1.308.800.000 VNĐ, bao gồm thiết bị phần cứng cho cụm Edge, máy chủ tại HQ, Firewall, cùng chi phí triển khai và tài nguyên Cloud trong giai đoạn phát triển.
- **Chi phí vận hành hàng năm (OPEX):** Ước tính 1.123.400.000 VNĐ/năm, bao gồm chi phí bản quyền, chi phí duy trì Cloud Production, đường truyền mạng và nhân sự vận hành hệ thống (DevOps).
Cộng thêm quỹ dự phòng rủi ro, Tổng chi phí sở hữu (TCO) trong chu kỳ 3 năm của dự án đạt 5,2 tỷ VNĐ.

**[Slide 17: Phân tích Hiệu quả Đầu tư (ROI)]**
Với quy mô doanh thu ước tính 120 tỷ/năm, mức TCO này tương đương 1,45% doanh thu, hoàn toàn phù hợp với tiêu chuẩn phân bổ ngân sách CNTT của ngành.
Giá trị làm lợi hàng năm ước đạt 1,95 tỷ VNĐ, thông qua việc:
- Tiết kiệm chi phí nhân sự nhờ tự động hóa hệ thống báo cáo.
- Giảm thiểu sai lệch tài chính thông qua luồng đối soát tự động.
- Ngăn ngừa thất thu nhờ đảm bảo tính liên tục của dịch vụ.
Dòng tiền ròng dự kiến đạt 831 triệu VNĐ/năm, đưa thời gian hoàn vốn xuống mức 1,73 năm. Ngoài ra, giá trị bảo vệ pháp lý của hệ thống giúp tổ chức tránh rủi ro thiệt hại tài chính lên đến 6 tỷ đồng. Mời bạn [Tên Người 9] tổng kết với lộ trình triển khai.

---

## NGƯỜI 9: LỘ TRÌNH, RỦI RO & KẾT LUẬN (Slide 18, 19, 20)

**[Slide 18: Lộ trình Triển khai]**
Cảm ơn bạn. Kính chào Hội đồng, em là [Tên Người 9], xin trình bày về kế hoạch triển khai dự án kéo dài 16 tuần, chia làm 5 pha gối đầu:
- **Pha 1 & 2 (Tuần 1-6):** Xây dựng hạ tầng lõi (Foundation & Core) bao gồm thiết lập VPN, khởi tạo cụm Kubernetes và cơ sở dữ liệu nền tảng.
- **Pha 3 (Tuần 6-9):** Nâng cấp bảo mật, tích hợp phân quyền SSO, triển khai luồng CDC streaming và hệ thống mã hóa dữ liệu.
- **Pha 4 (Tuần 9-13):** Chuyển đổi dữ liệu lịch sử và vận hành thí điểm (Pilot) tại 5 chi nhánh.
- **Pha 5 (Tuần 13-16):** Mở rộng hệ thống ra 29 chi nhánh còn lại, thực hiện diễn tập thảm họa (DR Drill) và vận hành chính thức (Go-live).

**[Slide 19: Quản trị Rủi ro]**
Rủi ro kỹ thuật đáng chú ý nhất là mức độ tương thích API của 8 phần mềm hiện hữu. Biện pháp kiểm soát là tiến hành Pilot sớm; trong trường hợp không hỗ trợ API chuẩn, hệ thống sẽ sử dụng Adapter Pattern hoặc truy xuất cơ sở dữ liệu qua giao thức Read-only để đảm bảo bám sát tiến độ.
Nhằm hạn chế rủi ro lỗi phần cứng tại lớp Edge, dự án lập danh mục dự phòng các máy chủ thiết lập sẵn (hot-swap), đảm bảo khả năng thay thế linh kiện dưới 30 phút.

**[Slide 20: Kết luận]**
Tóm lại, dự án giải quyết triệt để các hạn chế về vận hành và thiết lập cơ chế đảm bảo an toàn pháp lý cho tổ chức theo quy định về bảo vệ dữ liệu cá nhân. Mô hình Hybrid Cloud cung cấp khả năng vận hành liên tục và tính linh hoạt cao, cùng với thời gian hoàn vốn tối ưu, khẳng định đây là hạng mục đầu tư khả thi và cấp bách.
Quá trình chuyển giao sẽ bàn giao toàn bộ mã nguồn hạ tầng tự động hóa (Terraform), thiết kế hệ thống chi tiết (LLD) và sổ tay vận hành (Runbook) cho đội ngũ chuyên trách.
Phần trình bày của Nhóm 5 đến đây kết thúc. Xin chân thành cảm ơn Hội đồng đã lắng nghe và nhóm rất mong nhận được các ý kiến phản biện.

---
