**TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN -- ĐHQG -- HCM**

**TRUNG TÂM PHÁT TRIỂN CÔNG NGHỆ THÔNG TIN**

![](media/image1.png){width="2.425in" height="1.9625in"}🙣 🕮 🙡

**BÁO CÁO BÀI TẬP**

Giáo viên hướng dẫn: Nguyễn Thị Anh Thư

Nhóm sinh viên thực hiện:

Phạm Minh Mẫn 26410241

Lê Quang Đạt 26410183

Trần Việt Đức 26410189

Vũ Duy 26410199

Nguyễn Đức Huy 26410213

Trần Văn Phây 26410261

Huỳnh Thị Kiều Uyên 26410325

Đặng Nguyễn Minh Anh 26410163

Trần Anh Tú 26410318

TP. Hồ Chí Minh, Tháng 07 năm 2026.

# **Mục lục** {#mục-lục .TOC-Heading}

[Bước 0 Chuẩn bị đầu vào [3](#chuẩn-bị-đầu-vào)](#chuẩn-bị-đầu-vào)

[0.1 Bối cảnh Doanh nghiệp và Đặc thù Hệ sinh thái Dịch vụ Ways Station
[3](#bối-cảnh-doanh-nghiệp-và-đặc-thù-hệ-sinh-thái-dịch-vụ-ways-station)](#bối-cảnh-doanh-nghiệp-và-đặc-thù-hệ-sinh-thái-dịch-vụ-ways-station)

[0.2 Khảo sát Hạ tầng Hiện tại và Ba Điểm Nghẽn Lớn
[3](#khảo-sát-hạ-tầng-hiện-tại-và-ba-điểm-nghẽn-lớn)](#khảo-sát-hạ-tầng-hiện-tại-và-ba-điểm-nghẽn-lớn)

[0.2.1 Phân mảnh Nền tảng Ứng dụng
[3](#phân-mảnh-nền-tảng-ứng-dụng)](#phân-mảnh-nền-tảng-ứng-dụng)

[0.2.2 Dữ liệu Vận hành Thủ công và Thiếu chuẩn hóa
[4](#dữ-liệu-vận-hành-thủ-công-và-thiếu-chuẩn-hóa)](#dữ-liệu-vận-hành-thủ-công-và-thiếu-chuẩn-hóa)

[0.2.3 Cấu trúc Phân tán Khuếch đại Độ phức tạp của Mạng lưới
[4](#cấu-trúc-phân-tán-khuếch-đại-độ-phức-tạp-của-mạng-lưới)](#cấu-trúc-phân-tán-khuếch-đại-độ-phức-tạp-của-mạng-lưới)

[0.3 Công Nghệ Đề Xuất: Mô Hình Nền Tảng Dữ Liệu Chuỗi Thời Gian (TSFM)
và Kiến trúc MLOps
[4](#công-nghệ-đề-xuất-mô-hình-nền-tảng-dữ-liệu-chuỗi-thời-gian-tsfm-và-kiến-trúc-mlops)](#công-nghệ-đề-xuất-mô-hình-nền-tảng-dữ-liệu-chuỗi-thời-gian-tsfm-và-kiến-trúc-mlops)

[0.3.1 Phân tích Sâu Về Mô Hình Google TimesFM
[5](#phân-tích-sâu-về-mô-hình-google-timesfm)](#phân-tích-sâu-về-mô-hình-google-timesfm)

[0.3.2 Phân tích Sâu Về Amazon Chronos và Kiến Trúc Tách Từ
[5](#phân-tích-sâu-về-amazon-chronos-và-kiến-trúc-tách-từ)](#phân-tích-sâu-về-amazon-chronos-và-kiến-trúc-tách-từ)

[0.3.3 Tích hợp MLOps và nền tảng dữ liệu Architecture
[6](#tích-hợp-mlops-và-nền-tảng-dữ-liệu-architecture)](#tích-hợp-mlops-và-nền-tảng-dữ-liệu-architecture)

[Bước 1 Viết tên đề tài + thông tin chung
[6](#viết-tên-đề-tài-thông-tin-chung)](#viết-tên-đề-tài-thông-tin-chung)

[1.1 Tên đề tài và Phân tích tầm nhìn chiến lược chuyên sâu
[6](#tên-đề-tài-và-phân-tích-tầm-nhìn-chiến-lược-chuyên-sâu)](#tên-đề-tài-và-phân-tích-tầm-nhìn-chiến-lược-chuyên-sâu)

[1.1.1 Bối cảnh kinh doanh và Sự cấp thiết của đề tài
[6](#bối-cảnh-kinh-doanh-và-sự-cấp-thiết-của-đề-tài)](#bối-cảnh-kinh-doanh-và-sự-cấp-thiết-của-đề-tài)

[1.1.2 Sự đột phá của công nghệ TSFM
[7](#sự-đột-phá-của-công-nghệ-tsfm)](#sự-đột-phá-của-công-nghệ-tsfm)

[1.2 Thông tin chung về Tổ chức và Ma trận RACI
[7](#thông-tin-chung-về-tổ-chức-và-ma-trận-raci)](#thông-tin-chung-về-tổ-chức-và-ma-trận-raci)

[1.2.1 Vai trò của các Khối/Phòng ban
[7](#vai-trò-của-các-khốiphòng-ban)](#vai-trò-của-các-khốiphòng-ban)

[1.2.2 Ma trận RACI Chi tiết cho Dự án TSFM Ways Station
[8](#ma-trận-raci-chi-tiết-cho-dự-án-tsfm-ways-station)](#ma-trận-raci-chi-tiết-cho-dự-án-tsfm-ways-station)

[1.3 Cơ chế liên kết hệ thống: Kiến trúc Hạ tầng Lai và Dòng chảy Dữ
liệu
[8](#cơ-chế-liên-kết-hệ-thống-kiến-trúc-hạ-tầng-lai-và-dòng-chảy-dữ-liệu)](#cơ-chế-liên-kết-hệ-thống-kiến-trúc-hạ-tầng-lai-và-dòng-chảy-dữ-liệu)

[1.3.1 Kiến trúc On-Premise kết hợp Cloud
[9](#kiến-trúc-on-premise-kết-hợp-cloud)](#kiến-trúc-on-premise-kết-hợp-cloud)

[1.3.2 Kiến trúc kho dữ liệu trung tâm (Lakehouse)
[9](#kiến-trúc-kho-dữ-liệu-trung-tâm-lakehouse)](#kiến-trúc-kho-dữ-liệu-trung-tâm-lakehouse)

[Bước 2 Bối cảnh & Lý do chọn đề tài (Business Case)
[9](#bối-cảnh-lý-do-chọn-đề-tài-business-case)](#bối-cảnh-lý-do-chọn-đề-tài-business-case)

[2.1 Hiện trạng quy trình điều phối (Kiến trúc AS-IS)
[10](#hiện-trạng-quy-trình-điều-phối-kiến-trúc-as-is)](#hiện-trạng-quy-trình-điều-phối-kiến-trúc-as-is)

[2.2 Vấn đề và Điểm đau dưới góc độ Quản trị IT
[11](#vấn-đề-và-điểm-đau-dưới-góc-độ-quản-trị-it)](#vấn-đề-và-điểm-đau-dưới-góc-độ-quản-trị-it)

[2.2.1 Kiến trúc Hệ thống Rời rạc và Silo Dữ liệu
[11](#kiến-trúc-hệ-thống-rời-rạc-và-silo-dữ-liệu)](#kiến-trúc-hệ-thống-rời-rạc-và-silo-dữ-liệu)

[2.2.2 Thiếu hụt Nền tảng Giám sát và Cảnh báo
[12](#thiếu-hụt-nền-tảng-giám-sát-và-cảnh-báo)](#thiếu-hụt-nền-tảng-giám-sát-và-cảnh-báo)

[2.2.3 Hạn chế về Năng lực Tính toán và Lưu trữ
[12](#hạn-chế-về-năng-lực-tính-toán-và-lưu-trữ)](#hạn-chế-về-năng-lực-tính-toán-và-lưu-trữ)

[2.2.4 Thiếu Môi trường MLOps chuẩn mực
[12](#thiếu-môi-trường-mlops-chuẩn-mực)](#thiếu-môi-trường-mlops-chuẩn-mực)

[2.3 Phân tích Tác động Định lượng: TCO, ROI và Chi phí Vận hành
[12](#_Toc239351255)](#_Toc239351255)

[2.3.1 Chi phí Vận hành Lãng phí do Xếp ca sai
[12](#_Toc239351256)](#_Toc239351256)

[2.3.2 Tổng chi phí sở hữu hạ tầng cũ
[12](#_Toc239351257)](#_Toc239351257)

[2.3.3 Đánh giá Tỷ suất Hoàn vốn (ROI) cho dự án Chuyển đổi
[12](#_Toc239351258)](#_Toc239351258)

[2.4 Đề xuất Thay đổi (Quy trình TO-BE): Kỷ nguyên của TSFM và Tự động
hóa
[13](#đề-xuất-thay-đổi-quy-trình-to-be-kỷ-nguyên-của-tsfm-và-tự-động-hóa)](#đề-xuất-thay-đổi-quy-trình-to-be-kỷ-nguyên-của-tsfm-và-tự-động-hóa)

[2.4.1 Quy trình điều phối mới (TO-BE) với sự tích hợp của TSFM
[13](#quy-trình-điều-phối-mới-to-be-với-sự-tích-hợp-của-tsfm)](#quy-trình-điều-phối-mới-to-be-với-sự-tích-hợp-của-tsfm)

[2.5 Vai trò của CNTT như \"Đòn bẩy Chiến lược\"
[13](#vai-trò-của-cntt-như-đòn-bẩy-chiến-lược)](#vai-trò-của-cntt-như-đòn-bẩy-chiến-lược)

[Bước 3 Mục tiêu, KPI và tiêu chí thành công
[14](#mục-tiêu-kpi-và-tiêu-chí-thành-công)](#mục-tiêu-kpi-và-tiêu-chí-thành-công)

[3.1 Mục tiêu tổng quát và Giá trị cốt lõi mang lại
[14](#mục-tiêu-tổng-quát-và-giá-trị-cốt-lõi-mang-lại)](#mục-tiêu-tổng-quát-và-giá-trị-cốt-lõi-mang-lại)

[3.1.1 Tối ưu hóa chi phí và Quản trị TCO/ROI
[14](#tối-ưu-hóa-chi-phí-và-quản-trị-tcoroi)](#tối-ưu-hóa-chi-phí-và-quản-trị-tcoroi)

[3.1.2 Cải thiện Cam kết Chất lượng Dịch vụ (SLA) và Tính sẵn sàng
[14](#cải-thiện-cam-kết-chất-lượng-dịch-vụ-sla-và-tính-sẵn-sàng)](#cải-thiện-cam-kết-chất-lượng-dịch-vụ-sla-và-tính-sẵn-sàng)

[3.1.3 Nâng cao Trải nghiệm Khách hàng
[14](#nâng-cao-trải-nghiệm-khách-hàng)](#nâng-cao-trải-nghiệm-khách-hàng)

[3.2 Mục tiêu cụ thể về Hiệu suất Mô hình Dự báo
[15](#mục-tiêu-cụ-thể-về-hiệu-suất-mô-hình-dự-báo)](#mục-tiêu-cụ-thể-về-hiệu-suất-mô-hình-dự-báo)

[3.2.1 Độ chính xác dự báo: MAPE \< 15%
[15](#độ-chính-xác-dự-báo-mape-15)](#độ-chính-xác-dự-báo-mape-15)

[3.2.2 Khung thời gian dự báo: 7-14 ngày
[15](#khung-thời-gian-dự-báo-7-14-ngày)](#khung-thời-gian-dự-báo-7-14-ngày)

[3.2.3 Độ trễ suy luận: \< 1 giờ cho Batch, \< 500ms cho thời gian thực
[15](#độ-trễ-suy-luận-1-giờ-cho-batch-500ms-cho-thời-gian-thực)](#độ-trễ-suy-luận-1-giờ-cho-batch-500ms-cho-thời-gian-thực)

[3.3 Phương pháp Đo lường và Công cụ Giám sát Cơ sở hạ tầng
[16](#phương-pháp-đo-lường-và-công-cụ-giám-sát-cơ-sở-hạ-tầng)](#phương-pháp-đo-lường-và-công-cụ-giám-sát-cơ-sở-hạ-tầng)

[3.3.1 Công cụ Giám sát Cơ sở hạ tầng
[16](#công-cụ-giám-sát-cơ-sở-hạ-tầng)](#công-cụ-giám-sát-cơ-sở-hạ-tầng)

[3.3.2 Quản lý Nhật ký Tập trung (Centralized Logging với ELK Stack)
[16](#quản-lý-nhật-ký-tập-trung-centralized-logging-với-elk-stack)](#quản-lý-nhật-ký-tập-trung-centralized-logging-với-elk-stack)

[3.3.3 Truy vết Phân tán [16](#truy-vết-phân-tán)](#truy-vết-phân-tán)

[3.3.4 Cảnh báo Chủ động [16](#cảnh-báo-chủ-động)](#cảnh-báo-chủ-động)

[Bước 4 Bước 4: Đối tượng, phạm vi và giả định/ràng buộc
[16](#đối-tượng-phạm-vi-và-giả-địnhràng-buộc)](#đối-tượng-phạm-vi-và-giả-địnhràng-buộc)

[4.1 Đối tượng áp dụng và Thụ hưởng
[17](#đối-tượng-áp-dụng-và-thụ-hưởng)](#đối-tượng-áp-dụng-và-thụ-hưởng)

[4.2 Phạm vi của Dự án [17](#phạm-vi-của-dự-án)](#phạm-vi-của-dự-án)

[4.2.1 Trong phạm vi [17](#trong-phạm-vi)](#trong-phạm-vi)

[4.2.2 Ngoài phạm vi [18](#ngoài-phạm-vi)](#ngoài-phạm-vi)

[4.3 Luồng ngoại lệ và Xử lý tình huống biên
[19](#luồng-ngoại-lệ-và-xử-lý-tình-huống-biên)](#luồng-ngoại-lệ-và-xử-lý-tình-huống-biên)

[4.4 Giả định, Ràng buộc và Tuân thủ
[19](#giả-định-ràng-buộc-và-tuân-thủ)](#giả-định-ràng-buộc-và-tuân-thủ)

[4.4.1 Khía cạnh Pháp lý và Quyền riêng tư
[20](#khía-cạnh-pháp-lý-và-quyền-riêng-tư)](#khía-cạnh-pháp-lý-và-quyền-riêng-tư)

[4.4.2 Hạ tầng Mạng và Bảo mật
[20](#hạ-tầng-mạng-và-bảo-mật)](#hạ-tầng-mạng-và-bảo-mật)

[4.4.3 Giả định về Nguồn lực
[20](#giả-định-về-nguồn-lực)](#giả-định-về-nguồn-lực)

[4.5 Quản trị Rủi ro và Phương án Dự phòng
[20](#quản-trị-rủi-ro-và-phương-án-dự-phòng)](#quản-trị-rủi-ro-và-phương-án-dự-phòng)

[4.5.1 Mô hình Dự phòng [20](#mô-hình-dự-phòng)](#mô-hình-dự-phòng)

[4.5.2 Khôi phục sau thảm họa
[21](#khôi-phục-sau-thảm-họa)](#khôi-phục-sau-thảm-họa)

# Chuẩn bị đầu vào

## Bối cảnh Doanh nghiệp và Đặc thù Hệ sinh thái Dịch vụ Ways Station

Ways Station đã và đang khẳng định vị thế là một trong những chuỗi tổ
hợp dịch vụ trò chơi điện tử, bida, và dịch vụ F&B hàng đầu, với quy mô
mở rộng nhanh chóng lên tới hơn 34 chi nhánh trải dài khắp khu vực. Tuy
nhiên, sự phát triển theo chiều rộng với tốc độ cao đã kéo theo những
thách thức không nhỏ về mặt quản lý vận hành, đặc biệt là sự thiếu đồng
bộ về hạ tầng công nghệ thông tin.

Mô hình hoạt động của Ways Station dựa trên sự phân tán về mặt pháp lý:
mỗi chi nhánh thường được đăng ký dưới hình thức một hộ kinh doanh cá
thể riêng biệt. Phương thức này mặc dù mang lại sự linh hoạt tối đa về
mặt tổ chức pháp lý, tài chính cơ sở và tối ưu hóa chi phí thuế tại địa
phương, nhưng lại trở thành một \"cơn ác mộng\" đối với các kỹ sư quản
trị hệ thống và kiến trúc sư dữ liệu. Cụ thể, thay vì tồn tại một pháp
nhân duy nhất với một trung tâm dữ liệu hoặc hệ thống Cloud tập trung,
hạ tầng của Ways Station bị chia cắt thành 34 hòn đảo dữ liệu riêng
biệt.

Sự phân mảnh pháp lý này tạo ra một rào cản to lớn trong việc thu thập,
hợp nhất và phân tích dữ liệu trên quy mô toàn hệ thống. Do dữ liệu
khách hàng, giao dịch, và trạng thái hệ thống bị cô lập tại từng điểm,
ban lãnh đạo doanh nghiệp thiếu vắng một bức tranh toàn cảnh về hiệu
suất kinh doanh. Hơn nữa, với mục tiêu nâng cấp chất lượng dịch vụ thông
qua công nghệ Trí tuệ nhân tạo (AI) và Học máy nhằm tự động hóa quy
trình dự báo tài nguyên, cá nhân hóa trải nghiệm khách hàng và tối ưu
hóa chuỗi cung ứng, việc sở hữu một Hạ tầng Công nghệ Thông tin thống
nhất, tích hợp luồng dữ liệu liên tục là điều kiện tiên quyết và cấp
bách.

## Khảo sát Hạ tầng Hiện tại và Ba Điểm Nghẽn Lớn

Việc triển khai thành công một nền tảng dữ liệu tiên tiến đòi hỏi phải
hiểu rõ nền móng hiện có. Kết quả khảo sát toàn diện hạ tầng công nghệ
tại 34 chi nhánh cho thấy Ways Station đang đối mặt với 3 điểm nghẽn
nghiêm trọng thuộc cả 3 khía cạnh: Compute, Storage, và Network.

### Phân mảnh Nền tảng Ứng dụng

Sự phát triển tự phát của các chi nhánh dẫn đến sự đa dạng quá mức cần
thiết về các phần mềm quản lý và thiết bị phần cứng.

**Về phần cứng:** Các chi nhánh sử dụng các hệ thống máy chủ cục bộ với
thông số kỹ thuật không đồng nhất (từ các dòng Intel Xeon đời cũ đến các
hệ thống máy trạm PC giả lập máy chủ). Việc thiếu chuẩn hóa phần cứng
khiến việc cấp phát tài nguyên tính toán không hiệu quả, chi phí bảo trì
tăng cao, và làm giảm khả năng sẵn sàng của hệ thống.

**Về phần mềm và Hệ điều hành:** Không có một tiêu chuẩn chung về hệ
điều hành, cơ sở dữ liệu hay phần mềm quản lý (sử dụng hỗn hợp các phần
mềm tính tiền nội bộ, phần mềm mã nguồn mở tùy biến). Điều này gây cản
trở nghiêm trọng tới việc thiết lập các Middleware hay API Gateway để
giao tiếp, đồng bộ dữ liệu. Các giao thức API không được chuẩn hóa
RESTful hoặc gRPC, làm cho khả năng tích hợp gần như bằng không. Việc áp
dụng các containerization (như Docker/Kubernetes) không thể diễn ra đồng
bộ trên các nền tảng quá đứt gãy này.

### Dữ liệu Vận hành Thủ công và Thiếu chuẩn hóa

Dữ liệu là nguồn sống của các mô hình AI/ML, tuy nhiên hiện trạng lưu
trữ và xử lý dữ liệu tại Ways Station lại vô cùng lạc hậu:

**Silo Dữ liệu:** Hệ thống cơ sở dữ liệu phân tán cục bộ. Mỗi ngày, việc
tổng hợp báo cáo doanh thu, lượng khách, tồn kho F&B vẫn phải được xuất
ra file Excel từ từng chi nhánh, sau đó gửi qua email hoặc các kênh chat
về trụ sở chính. Nhân sự kế toán và quản trị phải mất hàng giờ để làm
sạch và hợp nhất.

**Thiếu Hệ thống Cảnh báo Thời gian thực:** Không có các công cụ giám
sát như Prometheus hay Grafana, cũng như các log shipper (như Fluentd,
Logstash). Khi một chi nhánh rớt mạng hoặc máy chủ quá tải, đội IT trung
tâm không nhận được cảnh báo tự động, dẫn tới chỉ số MTTR rất cao, ảnh
hưởng trực tiếp đến trải nghiệm người dùng và doanh thu.

**Thiếu kiến trúc hồ dữ liệu/kho dữ liệu/Lakehouse:** Chưa có kho lưu
trữ dữ liệu trung tâm nào đủ mạnh (như AWS S3, Google Cloud Storage kết
hợp với Snowflake hay Databricks) để đáp ứng nhu cầu phân tích Big Data.

### Cấu trúc Phân tán Khuếch đại Độ phức tạp của Mạng lưới

Mạng lưới là điểm nghẽn quyết định đối với các hệ thống phân tán:

**Mạng diện rộng (WAN) thiếu quy hoạch:** Các chi nhánh kết nối internet
thông qua các đường truyền FTTH dân dụng của nhiều ISP khác nhau với địa
chỉ IP động, thay vì sử dụng kênh truyền số liệu riêng hoặc thiết lập
mạng SD-WAN chuyên dụng.

**Rủi ro bảo mật:** Mô hình mạng hiện tại thiếu vắng tường lửa ứng dụng
web (WAF), hệ thống phát hiện/ngăn chặn xâm nhập thống nhất. Việc truy
cập từ xa chủ yếu dựa trên các phần mềm như TeamViewer, UltraViewer --
tạo ra những lỗ hổng bảo mật nghiêm trọng mà tin tặc có thể khai thác để
lây nhiễm Ransomware. Cần thiết phải thiết lập các kết nối VPN
Site-to-Site mã hóa IPsec để đảm bảo tính riêng tư và toàn vẹn của dữ
liệu trong quá trình truyền tải.

Tổng hợp lại, ROI từ việc đầu tư nhỏ lẻ vào các chi nhánh đang giảm sút
nghiêm trọng, trong khi chi phí vận hành (OPEX) gia tăng do phải duy trì
một lượng lớn nhân sự khắc phục sự cố thủ công. Đã đến lúc Ways Station
cần một cuộc đại tu hạ tầng thông qua tiếp cận Điện toán Đám mây Lai,
xây dựng Kiến trúc Dữ liệu Hiện đại và ứng dụng MLOps để giải quyết bài
toán cốt lõi.

## Công Nghệ Đề Xuất: Mô Hình Nền Tảng Dữ Liệu Chuỗi Thời Gian (TSFM) và Kiến trúc MLOps

Để chuyển mình từ một doanh nghiệp vận hành thủ công sang Data-driven
Company, Ways Station cần một nền tảng dữ liệu đủ mạnh để hỗ trợ việc ra
quyết định tự động. Bài toán lớn nhất hiện nay của Ways Station là **Dự
báo nhu cầu khách hàng và Tối ưu hóa chuỗi cung ứng/nhân sự** theo chuỗi
thời gian. Với 34 chi nhánh mang các đặc thù địa lý và tệp khách hàng
khác nhau, và việc liên tục mở mới các chi nhánh (gây ra bài toán khởi
động lạnh (thiếu dữ liệu ban đầu) - thiếu dữ liệu lịch sử), các mô hình
học máy truyền thống đã không còn đáp ứng được yêu cầu về khả năng mở
rộng và độ chính xác zero-shot.

### Phân tích Sâu Về Mô Hình Google TimesFM

**Google TimesFM** là một bước đột phá của Google trong lĩnh vực dự báo
chuỗi thời gian, áp dụng thành công kiến trúc đã tạo nên sức mạnh cho
các mô hình ngôn ngữ lớn (LLMs).

**Kiến trúc Decoder-Only:** Tương tự như GPT, TimesFM sử dụng kiến trúc
Transformer chỉ có bộ giải mã. Điều này cho phép mô hình dự báo trực
tiếp các điểm dữ liệu trong tương lai dựa trên chuỗi dữ liệu trong quá
khứ một cách liên tục.

**Cơ chế Patching:** Thay vì xử lý từng điểm thời gian đơn lẻ, TimesFM
gộp một chuỗi các điểm dữ liệu liên tiếp thành các \"patch\" (bản vá).
Cơ chế này mang lại 3 lợi ích cốt lõi:

Giảm thiểu độ phức tạp tính toán (giảm từ O(N\^2) xuống O((N/P)\^2) với
P là kích thước patch), giúp tăng tốc độ huấn luyện và suy luận.

Cải thiện khả năng trích xuất đặc trưng cục bộ, giúp mô hình nắm bắt
được cấu trúc vi mô của chuỗi thời gian (ví dụ: xu hướng tăng đột biến
vào các ngày cuối tuần tại Ways Station).

Tiết kiệm bộ nhớ trong quá trình suy luận.

**Zero-Shot Forecasting:** Được huấn luyện trên một tập dữ liệu chuỗi
thời gian khổng lồ (lên tới hàng trăm tỷ điểm dữ liệu từ Google Trends,
Wikipedia pageviews,\...), TimesFM sở hữu khả năng \"Zero-Shot\" xuất
sắc. Nghĩa là, nó có thể đưa ra dự báo với độ chính xác cao cho các tập
dữ liệu hoàn toàn mới mà không cần phải tinh chỉnh lại mô hình. Tính
năng này giải quyết triệt để **bài toán khởi động lạnh (thiếu dữ liệu
ban đầu)** khi Ways Station khai trương chi nhánh mới: chỉ cần một lượng
dữ liệu lịch sử rất ngắn (vài ngày hoặc vài tuần), TimesFM đã có thể dự
báo chính xác lượng khách hàng trong thời gian tới.

**Multivariate Support (Hỗ trợ đa biến):** Không chỉ dự báo dựa trên
chuỗi thời gian đơn (ví dụ: số lượng khách), TimesFM có thể nhận đầu vào
đa biến như: các ngày lễ tết, thời tiết, sự kiện khuyến mãi, hoặc các
biến động kinh tế vĩ mô, làm tăng độ tin cậy của các dự đoán doanh thu.

### Phân tích Sâu Về Amazon Chronos và Kiến Trúc Tách Từ

Một đối trọng và cũng là một lựa chọn bổ sung mạnh mẽ là **Amazon
Chronos**. Chronos tiếp cận chuỗi thời gian bằng một triết lý hoàn toàn
dựa trên xử lý ngôn ngữ tự nhiên (NLP).

**Language Model Approach & mã hóa (tokenization) (Tiếp cận Mô hình Ngôn
ngữ và Tách từ):** Chronos \"ngôn ngữ hóa\" chuỗi thời gian. Nó lượng tử
hóa các giá trị thực của chuỗi thời gian thành một tập hợp các token rời
rạc (tương tự như các từ trong một câu tiếng Anh). Sau đó, nó áp dụng
trực tiếp các kiến trúc LLM tiêu chuẩn (như T5) để dự báo token tiếp
theo. Bằng cách này, Chronos tận dụng được sức mạnh khổng lồ của các mô
hình LLM sẵn có.

**Khả năng Suy luận Xác suất:** Vì đầu ra là phân phối xác suất trên một
từ điển token, Chronos tự nhiên cung cấp khả năng dự báo phân phối, cho
phép Ways Station đánh giá rủi ro và các kịch bản khoảng tin cậy thay vì
chỉ đưa ra một con số dự báo điểm.

**Chronos-Bolt (Tối ưu hóa hiệu năng):** Để giải quyết vấn đề tốc độ suy
luận chậm của mô hình tự hồi quy, Amazon đã phát triển Chronos-Bolt.
Chronos-Bolt sử dụng cơ chế dự báo song song (patching kết hợp với cấu
trúc song song), giúp tăng tốc độ suy luận lên gấp nhiều lần, đặc biệt
phù hợp với các ứng dụng dự báo real-time đòi hỏi độ trễ thấp như việc
phân bổ luồng mạng hoặc tài nguyên máy chủ tại các chi nhánh Ways
Station.

### Tích hợp MLOps và nền tảng dữ liệu Architecture

Để triển khai các mô hình TSFM tiên tiến này, một hạ tầng MLOps hoàn
chỉnh phải được xây dựng, dựa trên nền tảng kho dữ liệu trung tâm
(Lakehouse):

**Ingestion & API Gateway:** Dữ liệu từ 34 chi nhánh sẽ được truyền tải
qua các đường hầm bảo mật đến API Gateway tập trung. Các luồng dữ liệu
thời gian thực (như lượt check-in, giao dịch thanh toán) sẽ được đẩy vào
message broker (như Apache Kafka hoặc Amazon Kinesis).

**Storage:** Dữ liệu thô được lưu tại hồ dữ liệu (Object Storage như AWS
S3/MinIO). Sau đó, các công cụ xử lý phân tán sẽ làm sạch, chuẩn hóa và
đưa vào kho dữ liệu theo cấu trúc Delta Lake hoặc Apache Iceberg, đảm
bảo tính ACID.

**Model Training & Registry:** Bằng cách sử dụng các nền tảng như
MLflow, Khoa học gia dữ liệu có thể quản lý vòng đời của các mô hình
TimesFM/Chronos. Mặc dù là mô hình không cần huấn luyện (zero-shot),
việc định kỳ cập nhật và tinh chỉnh hiệu quả trên lượng dữ liệu khổng lồ
mới sinh ra từ Ways Station vẫn cần thiết để cá nhân hóa mô hình cho
riêng doanh nghiệp.

**Serving & Monitoring:** Mô hình được container hóa bằng Docker, quản
lý bởi Kubernetes (K8s) để đảm bảo độ sẵn sàng cao và tự động mở rộng
quy mô. Công cụ theo dõi như Prometheus/Grafana và Evidently AI sẽ liên
tục theo dõi chất lượng dự báo và cảnh báo khi có sự sai lệch xảy ra.

Việc chuẩn hóa hạ tầng, xây dựng kiến trúc dữ liệu vững chắc và mạnh dạn
áp dụng các mô hình Mô hình nền tảng chuỗi thời gian chính là bước đệm
quan trọng (Bước 0) để Ways Station hóa giải các điểm nghẽn, kiểm soát
được độ phức tạp phân tán và tối đa hóa hiệu quả vận hành kinh doanh
trong tương lai.

# Viết tên đề tài + thông tin chung

## Tên đề tài và Phân tích tầm nhìn chiến lược chuyên sâu

**Tên đề tài chính thức:** **\"Ứng dụng Mô hình nền tảng chuỗi thời gian
(Time Series Foundation Model - TSFM) dự báo lưu lượng khách theo khung
giờ, hỗ trợ điều phối nhân sự tại hệ thống Ways Station\"**

### Bối cảnh kinh doanh và Sự cấp thiết của đề tài

Trong kỷ nguyên của nền kinh tế số và cạnh tranh khốc liệt trong ngành
F&B và bán lẻ đa kênh, việc tối ưu hóa chi phí vận hành đồng thời nâng
cao trải nghiệm khách hàng là mục tiêu sống còn của mọi chuỗi hệ thống.
Tại hệ thống Ways Station -- với quy mô hàng chục cửa hàng hoạt động với
lưu lượng khách biến động mạnh theo từng khung giờ, ngày trong tuần, và
các dịp lễ tết -- phương pháp lập kế hoạch nhân sự thủ công (dựa trên
kinh nghiệm hoặc Excel) đã bộc lộ những hạn chế nghiêm trọng. Sự thiếu
hụt nhân sự vào giờ cao điểm dẫn đến mất mát doanh thu và suy giảm mức
độ hài lòng của khách hàng, trong khi dư thừa nhân sự vào giờ thấp điểm
làm lãng phí quỹ lương, trực tiếp ăn mòn biên lợi nhuận.

Đề tài này ra đời với sứ mệnh cốt lõi là giải quyết triệt để bài toán
trên thông qua việc ứng dụng công nghệ Trí tuệ Nhân tạo (AI) tiên tiến
nhất hiện nay trong lĩnh vực dự báo: **Mô hình nền tảng chuỗi thời gian
(TSFM)**. Khác với các phương pháp thống kê truyền thống như ARIMA, hay
thậm chí các mô hình Deep Learning thế hệ trước như LSTM/RNN đòi hỏi
phải huấn luyện lại từ đầu cho từng luồng dữ liệu, TSFM đại diện cho một
bước nhảy vọt về công nghệ.

### Sự đột phá của công nghệ TSFM

Đề tài tập trung nghiên cứu và đánh giá tính khả thi, hiệu quả của các
mô hình nền tảng hàng đầu, đặc biệt là **Google TimesFM** và **Amazon
Chronos**.

**Google TimesFM:** Đây là một mô hình tiên phong áp dụng kiến trúc
Transformer -- tương tự như các mô hình ngôn ngữ lớn (LLM) -- nhưng được
thiết kế chuyên biệt cho dữ liệu chuỗi thời gian liên tục. Sức mạnh cốt
lõi của TimesFM nằm ở cơ chế **Patching**. Thay vì xử lý từng điểm dữ
liệu riêng lẻ, TimesFM gom nhóm một chuỗi các điểm dữ liệu liên tiếp
thành các \"patch\" (mảnh). Điều này không chỉ giúp mô hình nắm bắt được
các chu kỳ và xu hướng phức tạp dài hạn mà còn tăng tốc độ suy luận một
cách đáng kinh ngạc. Quan trọng hơn, TimesFM hỗ trợ dự báo **không cần
huấn luyện (zero-shot)** (hoạt động tốt trên dữ liệu mới mà không cần
fine-tuning) và xử lý dữ liệu đa biến, cho phép Ways Station kết hợp lưu
lượng khách với các biến ngoại lai (thời tiết, sự kiện địa phương,
chương trình khuyến mãi) để tăng độ chính xác lên mức tối đa (giảm chỉ
số MAPE xuống dưới 10%).

**Amazon Chronos:** Cùng với TimesFM, kiến trúc Chronos của Amazon mở ra
một cách tiếp cận đột phá khác: **mã hóa (tokenization) (Mã hóa chuỗi
thời gian thành Token)**. Chronos chia tỷ lệ và lượng tử hóa chuỗi thời
gian thành các bucket rời rạc, sau đó xem chúng như các token trong xử
lý ngôn ngữ tự nhiên (NLP). Điều này cho phép tận dụng trực tiếp các cấu
trúc ngôn ngữ T5 hoặc GPT để dự báo. Phiên bản nâng cấp **Chronos-Bolt**
tối ưu hóa bộ nhớ và tốc độ suy luận, đặc biệt phù hợp cho các luồng dữ
liệu tần suất cao. Khả năng \"Language Model Approach\" của Chronos giúp
hệ thống của Ways Station có thể xử lý các mẫu dữ liệu đứt gãy hoặc dữ
liệu nhiễu một cách mạnh mẽ.

## Thông tin chung về Tổ chức và Ma trận RACI

Một dự án AI/MLOps đòi hỏi sự phối hợp liên chức năng chặt chẽ giữa
nhiều bộ phận. Sự thất bại của các dự án AI thường không nằm ở mô hình,
mà nằm ở sự đứt gãy trong giao tiếp và chuyển giao quyền lực. Tại Ways
Station, dự án được quản trị dựa trên chuẩn mực Agile/Scrum kết hợp với
khung quản trị dự án PMP.

### Vai trò của các Khối/Phòng ban

**Khối Vận hành (Operations & Phòng Điều phối):** Cung cấp domain
knowledge (kiến thức nghiệp vụ) về đặc thù từng điểm bán. Họ là
\"End-User\" (người dùng cuối) tiêu thụ kết quả dự báo để xếp ca làm
việc.

**Khối Nhân sự (HR):** Đảm bảo bài toán phân ca tuân thủ luật lao động,
số giờ làm việc tối đa, năng lực nhân viên và quỹ lương mục tiêu.

**Đội ngũ Dữ liệu:** Đội ngũ nòng cốt chịu trách nhiệm xây dựng đường
ống dữ liệu, tinh chỉnh mô hình TSFM, và triển khai lên môi trường
Production.

**Khối hạ tầng công nghệ thông tin (Hạ tầng & DevOps):** Cung cấp và duy
trì tài nguyên Compute, Storage, Network, bảo mật hệ thống IAM, và vận
hành cụm Kubernetes (K8s).

### Ma trận RACI Chi tiết cho Dự án TSFM Ways Station

*(R: Responsible - Người thực thi, A: Accountable - Người chịu trách
nhiệm giải trình, C: Consulted - Người tư vấn, I: Informed - Người được
thông báo)*

  --------------------------------------------------------------------------
  Hạng mục /     Khối Vận    Khối Nhân   Đội ngũ Dữ  Khối IT (Hạ Ban Giám
  Giai đoạn      hành (Điều  sự (HR)     liệu        tầng)       Đốc (BOD)
                 phối)                   (AI/ML)                 
  -------------- ----------- ----------- ----------- ----------- -----------
  **1. Định      A           R           C           C           I
  nghĩa bài toán                                                 
  & Xác định                                                     
  KPI/SLA**                                                      

  **2. Thu thập  I           C           R           A           I
  & Trích xuất                                                   
  dữ liệu**                                                      

  **3. Thiết lập I           I           C           R/A         I
  Hạ tầng Cloud                                                  
  & Cấp quyền                                                    
  (IAM)**                                                        

  **4. Lựa chọn  I           I           R/A         C           I
  mô hình & Thử                                                  
  nghiệm**                                                       

  **5. Triển     C           I           R           A           I
  khai MLOps &                                                   
  Đưa lên                                                        
  Production**                                                   

  **6. Đào tạo   R/A         C           C           I           I
  người dùng &                                                   
  Áp dụng xếp ca                                                 
  thực tế**                                                      

  **7. Giám sát  R           R           C           I           A
  & Đánh giá                                                     
  hiệu quả kinh                                                  
  doanh (ROI)**                                                  
  --------------------------------------------------------------------------

Bảng RACI này đảm bảo mọi nút thắt cổ chai trong quá trình triển khai hệ
thống, từ việc thiết lập VPC/Subnet cho môi trường Hybrid đến việc phân
phối kết quả dự báo qua API, đều có một cá nhân/phòng ban chịu trách
nhiệm cao nhất.

## Cơ chế liên kết hệ thống: Kiến trúc Hạ tầng Lai và Dòng chảy Dữ liệu

Để một hệ thống AI nền tảng như Google TimesFM hoạt động với hiệu suất
tối ưu và độ trễ thấp, kiến trúc hạ tầng bên dưới phải là một kiệt tác
về kỹ thuật. Đề tài Ways Station áp dụng mô hình **Đám mây lai (Đám mây
lai)** kết hợp với kiến trúc **kho dữ liệu trung tâm (Lakehouse)**, tạo
ra một môi trường phi tập trung nhưng được quản trị thống nhất.

### Kiến trúc On-Premise kết hợp Cloud

Ways Station hiện sở hữu hệ thống máy chủ vật lý tại các cửa hàng làm
nhiệm vụ vận hành POS và hệ thống camera đếm khách.

**Máy chủ nội bộ:** Các server tại cửa hàng chạy phần mềm nhẹ dưới dạng
Docker containers, làm nhiệm vụ thu thập dữ liệu thô và làm sạch cơ bản.
Dữ liệu này bao gồm số hóa đơn, số lượng khách qua cửa, dữ liệu thời
tiết cục bộ.

**Điện toán đám mây (AWS/GCP):** Đóng vai trò là \"Bộ não trung tâm\".
Đám mây cung cấp khả năng mở rộng tài nguyên không giới hạn thông qua
các Instance có GPU (như AWS EC2 p4d hoặc GCP A2) cần thiết cho quá
trình tinh chỉnh (tinh chỉnh) hoặc Batch suy luận của các mô hình
Transformer nặng.

**Kết nối Mạng:** Cơ chế liên kết giữa máy chủ nội bộ và Cloud được thực
hiện qua kênh truyền bảo mật **Site-to-Site VPN** hoặc **AWS Direct
Connect / GCP Cloud Interconnect**. Điều này đảm bảo dữ liệu (đặc biệt
là dữ liệu doanh thu nhạy cảm) không di chuyển qua internet công cộng,
đáp ứng tiêu chuẩn an toàn thông tin ISO 27001.

### Kiến trúc kho dữ liệu trung tâm (Lakehouse)

kho dữ liệu trung tâm (Lakehouse) là sự kết tinh giữa tính linh hoạt của
hồ dữ liệu và khả năng phân tích mạnh mẽ của kho dữ liệu, được xây dựng
trên các công nghệ lưu trữ Object Storage kết hợp với định dạng bảng mở
(như Apache Iceberg, Delta Lake, hoặc Apache Hudi).

**Vùng hạ cánh:** Dữ liệu chuỗi thời gian từ các cửa hàng đổ về qua
Apache Kafka, được lưu trữ nguyên bản trong hồ dữ liệu.

**Vùng chuẩn hóa:** Các Job xử lý dữ liệu bằng Apache Spark sẽ đọc dữ
liệu từ Bronze Layer, loại bỏ nhiễu, điền khuyết cho các khoảng thời
gian bị thiếu dữ liệu do mất điện hoặc rớt mạng. Ở tầng này, dữ liệu đã
được cấu trúc hóa theo dạng Cột (Columnar format như Parquet).

**Vùng phân tích:** Dữ liệu đặc trưng phục vụ trực tiếp cho mô hình AI
được tổng hợp. Tại đây, hệ thống lưu trữ các đặc trưng đa biến: lưu
lượng khách trong quá khứ, biến chỉ báo ngày lễ, ngân sách Marketing
trong ngày. Dữ liệu Gold được truy vấn cực nhanh qua các Engine như
Presto, Trino hoặc Snowflake.

# Bối cảnh & Lý do chọn đề tài (Business Case)

Trong bối cảnh nền kinh tế số và kỷ nguyên của Dữ liệu lớn, việc vận
hành chuỗi cung ứng và dịch vụ bán lẻ không chỉ dừng lại ở kinh nghiệm
quản lý truyền thống mà đòi hỏi một sự dịch chuyển mạnh mẽ sang các hệ
thống ra quyết định dựa trên dữ liệu. Ways Station, một hệ thống chuỗi
cung ứng và bán lẻ dịch vụ, đang đứng trước ngưỡng cửa của sự tăng
trưởng quy mô, nhưng lại gặp phải những nút thắt cổ chai nghiêm trọng
trong khâu điều phối nguồn lực và dự báo nhu cầu. Do đó, việc xây dựng
một nền tảng cơ sở hạ tầng công nghệ thông tin (CNTT) hiện đại, tích hợp
các mô hình trí tuệ nhân tạo (AI) tiên tiến là một bài toán mang tính
sống còn.

Phần này sẽ trình bày chi tiết về bối cảnh kinh doanh, phân tích hiện
trạng hệ thống, những điểm đau về mặt hạ tầng quản trị, và những đánh
giá định lượng về tác động tài chính. Từ đó, định hình một giải pháp
công nghệ toàn diện nhằm giải quyết triệt để các thách thức hiện tại,
khẳng định vai trò của CNTT như một đòn bẩy chiến lược cho toàn bộ tổ
chức.

## Hiện trạng quy trình điều phối (Kiến trúc AS-IS)

Hiện nay, quy trình vận hành và điều phối nguồn lực tại các trạm của
Ways Station đang phụ thuộc phần lớn vào quy trình thủ công và các công
cụ công nghệ thông tin phân mảnh, thiếu tính đồng bộ.

Quy trình điều phối nhân sự, hàng hóa và lập kế hoạch ca làm việc đang
được thực hiện theo cơ chế \"hậu kiểm và phản ứng\" thay vì \"tiền kiểm
và dự báo\". Sự thiếu hụt trầm trọng của một kiến trúc dữ liệu tập trung
dẫn đến tình trạng các silo dữ liệu tồn tại rải rác ở từng chi nhánh,
không có khả năng hợp nhất để tạo ra bức tranh toàn cảnh theo thời gian
thực.

**Mô tả chi tiết các bước trong quy trình AS-IS:**

  --------------------------------------------------------------------------
  Bước           Tên Quy trình  Mô tả chi tiết Mức độ can     Công cụ hiện
                                hiện trạng kỹ  thiệp thủ công tại
                                thuật và vận                  
                                hành                          
  -------------- -------------- -------------- -------------- --------------
  1              Thu thập Dữ    Hệ thống POS   Rất cao        MS Excel, FTP,
                 liệu Cuối ngày tại các trạm                  Email
                                xuất dữ liệu                  
                                bán hàng và                   
                                lưu lượng                     
                                khách hàng                    
                                dưới dạng file                
                                CSV/Excel cục                 
                                bộ. Dữ liệu                   
                                này được gửi                  
                                qua email hoặc                
                                tải lên một                   
                                FTP server                    
                                trung tâm vào                 
                                cuối ngày.                    
                                Không có luồng                
                                dữ liệu truyền                
                                phát liên tục.                

  2              Tổng hợp và    Nhân viên phân Cao            VBA, Python
                 Làm sạch       tích dữ liệu                  script
                                tại hội sở tải                
                                các file rời                  
                                rạc, dùng các                 
                                macro VBA hoặc                
                                kịch bản                      
                                Python đơn                    
                                giản để gộp                   
                                file. Quá                     
                                trình này                     
                                thường xuyên                  
                                xảy ra lỗi                    
                                định dạng,                    
                                thiếu sót dữ                  
                                liệu do đường                 
                                truyền mạng ở                 
                                các trạm không                
                                ổn định.                      

  3              Dự báo Nhu cầu Cửa hàng       Tuyết đối thủ  Trực giác,
                                trưởng dựa vào công           Excel cơ bản
                                kinh nghiệm cá                
                                nhân, hoặc dữ                 
                                liệu lịch sử                  
                                của tuần trước                
                                đó để ước                     
                                lượng số lượng                
                                khách hàng cho                
                                tuần tiếp                     
                                theo. Hoàn                    
                                toàn thiếu                    
                                vắng các mô                   
                                hình học máy                  
                                hay các thuật                 
                                toán Time                     
                                Series.                       

  4              Lập lịch và    Quản lý sắp    Cao            Excel, Giấy tờ
                 Điều phối      xếp ca làm                    
                                việc cho nhân                 
                                viên và lên kế                
                                hoạch nhập                    
                                hàng dựa trên                 
                                con số dự báo                 
                                thủ công. Quy                 
                                trình này kéo                 
                                dài từ 4-6                    
                                tiếng mỗi tuần                
                                cho mỗi trạm,                 
                                gây lãng phí                  
                                nguồn lực quản                
                                trị.                          

  5              Phản ứng Cục   Khi có đột     Rất cao        Điện thoại,
                 bộ             biến lưu lượng                Zalo
                                (sự kiện, thời                
                                tiết), cửa                    
                                hàng trưởng                   
                                gọi điện thoại                
                                khẩn cấp để                   
                                huy động nhân                 
                                sự hoặc chuyển                
                                hàng từ kho                   
                                trung tâm. Sự                 
                                chậm trễ của                  
                                hệ thống thông                
                                tin dẫn đến                   
                                mất mát doanh                 
                                thu.                          
  --------------------------------------------------------------------------

Như vậy, mô hình AS-IS bộc lộ rõ sự yếu kém của hạ tầng CNTT truyền
thống: Không có tính toàn vẹn dữ liệu, độ trễ cao trong luồng thông tin,
và quy trình xử lý không có khả năng mở rộng khi số lượng trạm Ways
Station tăng lên.

## Vấn đề và Điểm đau dưới góc độ Quản trị IT

Nhìn từ góc độ kiến trúc Cơ sở hạ tầng Công nghệ thông tin và Quản trị
Vận hành, hệ thống hiện tại của Ways Station đang đối mặt với các điểm
đau cốt lõi sau:

### Kiến trúc Hệ thống Rời rạc và Silo Dữ liệu

Hệ thống tính tiền (POS), hệ thống quản lý kho (WMS), và hệ thống quản
lý nhân sự (HRIS) đang hoạt động như những ốc đảo độc lập. Không có một
hệ thống phần mềm trung gian hay nền tảng tích hợp dữ liệu như Apache
Kafka hay một Enterprise Service Bus (ESB) để liên kết chúng. Hậu quả
là, bộ phận IT phải liên tục thực hiện các truy vấn dữ liệu thủ công,
bảo trì nhiều cơ sở dữ liệu quan hệ (RDBMS) khác nhau mà không có một
kho dữ liệu trung tâm.

### Thiếu hụt Nền tảng Giám sát và Cảnh báo

Hạ tầng hiện tại hoàn toàn thiếu vắng các công cụ giám sát hiệu năng ứng
dụng và giám sát dữ liệu. Khi một thiết bị POS tại trạm gặp sự cố không
gửi được dữ liệu, bộ phận IT tại trung tâm không hề nhận được cảnh báo
tự động. Họ chỉ phát hiện ra khi quy trình tổng hợp cuối ngày bị lỗi. Sự
thiếu vắng các hệ thống như Prometheus hay Grafana khiến thời gian phản
hồi sự cố tăng vọt.

### Hạn chế về Năng lực Tính toán và Lưu trữ

Với mô hình máy chủ vật lý đặt tại chỗ hiện tại, năng lực tính toán bị
giới hạn cứng. Khi dữ liệu lịch sử phình to, các truy vấn SQL trở nên
chậm chạp. Việc không ứng dụng điện toán đám mây khiến hệ thống không
thể tự động mở rộng trong các dịp lễ Tết khi lượng giao dịch tăng đột
biến. Sự không linh hoạt của hạ tầng Storage (như thiếu Object Storage)
cản trở việc lưu trữ dữ liệu phi cấu trúc phục vụ cho AI sau này.

### Thiếu Môi trường MLOps chuẩn mực

Để triển khai AI/ML vào dự báo, quy trình hiện tại hoàn toàn trắng băng
về MLOps. Không có hệ thống theo dõi phiên bản mô hình, không có luồng
CI/CD cho các thuật toán, và không có công cụ tự động huấn luyện lại mô
hình khi xảy ra hiện tượng trôi lệch dữ liệu.

## Đề xuất Thay đổi (Quy trình TO-BE): Kỷ nguyên của TSFM và Tự động hóa

Để khắc phục triệt để những vấn đề trên, đề tài này đề xuất một sự
chuyển dịch toàn diện sang kiến trúc hệ thống hiện đại, áp dụng công
nghệ MLOps tiên tiến và tích hợp các Mô hình Nền tảng Dữ liệu Chuỗi thời
gian.

### Quy trình điều phối mới (TO-BE) với sự tích hợp của TSFM

Trong mô hình TO-BE, con người sẽ không còn đóng vai trò \"công nhân xử
lý dữ liệu\" mà trở thành \"người giám sát và ra quyết định chiến
lược\".

**Thu thập và Đẩy dữ liệu theo Thời gian thực:** Thay vì xử lý lô cuối
ngày, dữ liệu từ các POS và cảm biến tại trạm được đẩy liên tục thông
qua kiến trúc Event-Driven (sử dụng Apache Kafka hoặc AWS Kinesis). Các
luồng dữ liệu này đi vào một kiến trúc kho dữ liệu trung tâm (Lakehouse)
trung tâm (ví dụ: Delta Lake hoặc Snowflake) trên nền tảng Cloud.

**Tiền xử lý và Tính toán tự động:** Luồng dữ liệu được tự động làm sạch
và trích xuất đặc trưng thông qua các pipeline như Apache Airflow hoặc
dbt.

**Dự báo Ứng dụng Mô hình nền tảng chuỗi thời gian (TSFM):** Thay vì
huấn luyện các mô hình ARIMA/Prophet tốn kém từ đầu, hệ thống sẽ sử dụng
các TSFM tiên tiến:

**Google TimesFM:** Mô hình Decoder-only, sử dụng kỹ thuật Patching
(chia chuỗi thời gian thành các mảng nhỏ để token hóa). TimesFM có khả
năng dự báo không cần huấn luyện (zero-shot) (không cần tinh chỉnh cho
từng tập dữ liệu cụ thể của từng trạm), xử lý cực tốt dữ liệu đa biến từ
doanh thu, thời tiết đến sự kiện cục bộ.

**Amazon Chronos:** Hoạt động bằng cách token hóa dữ liệu chuỗi thời
gian và xử lý chúng như một ngôn ngữ, sử dụng kiến trúc Transformer.
Chronos mang lại khả năng dự đoán chính xác cao cho các mẫu hình mùa vụ
phức tạp của Ways Station.

**Tự động hóa qua API Gateway:** Kết quả dự báo (số lượng khách, nhu cầu
nhân lực từng khung giờ 15 phút) sẽ được một API Gateway trung tâm (ví
dụ: Kong hoặc AWS API Gateway) định tuyến trực tiếp về hệ thống WMS và
HRIS.

**Điều phối Tự động và Động:** Hệ thống tự động sinh ra lịch làm việc
tối ưu và gợi ý đặt hàng. Quản lý trạm chỉ việc phê duyệt trên thiết bị
di động.

## Vai trò của CNTT như \"Đòn bẩy Chiến lược\"

Theo lý thuyết về Cơ sở hạ tầng Công nghệ thông tin (Chương 1), CNTT
không chỉ dừng lại ở việc cung cấp cáp mạng, máy tính hay hỗ trợ kỹ
thuật. Trong dự án Ways Station, hạ tầng CNTT đã vươn lên thành một
**Đòn bẩy Chiến lược**.

**Từ Hỗ trợ Vận hành sang Định hình Mô hình Kinh doanh:** Hạ tầng Cloud
kết hợp với AI không chỉ làm tự động hóa quy trình mà còn mở ra khả năng
cá nhân hóa trải nghiệm khách hàng và tối ưu hóa chuỗi cung ứng theo
thời gian thực. Sự dịch chuyển từ mô hình máy chủ nội bộ tĩnh sang
Hybrid/điện toán đám mây cung cấp tính linh hoạt tuyệt đối.

**Kiến trúc Linh hoạt:** Việc áp dụng API Gateway, Middleware và
Microservices biến hệ thống thành một cấu trúc lego. Ways Station có thể
dễ dàng cắm thêm các đối tác giao hàng thứ ba, hoặc tích hợp các phương
thức thanh toán mới mà không làm sập hệ thống lõi.

**Quản trị An toàn và Bảo mật Kép:** Hạ tầng mới đưa hệ thống quản lý
danh tính (IAM) và bảo mật dữ liệu lên mức doanh nghiệp. Sự dịch chuyển
lên Lakehouse kèm theo các chính sách phân quyền chi tiết (RBAC) đảm bảo
tính tuân thủ và bảo vệ tài sản dữ liệu chiến lược của công ty.

# Mục tiêu, KPI và tiêu chí thành công

## Mục tiêu tổng quát và Giá trị cốt lõi mang lại

Trong bối cảnh chuyển đổi số và ứng dụng sâu rộng của trí tuệ nhân tạo
vào chuỗi cung ứng, dự án Cơ sở hạ tầng Công nghệ thông tin cho Ways
Station không chỉ dừng lại ở việc xây dựng một hệ thống phần mềm đơn
thuần, mà hướng tới việc kiến tạo một nền tảng dữ liệu và vận hành học
máy toàn diện. Mục tiêu tổng quát của bước này là định lượng hóa các kỳ
vọng của dự án thông qua các Chỉ số đo lường hiệu quả công việc và Tiêu
chí thành công rõ ràng, mang tính khả thi và bám sát vào định hướng kinh
doanh cốt lõi của doanh nghiệp.

### Tối ưu hóa chi phí và Quản trị TCO/ROI

Mục tiêu hàng đầu của hạ tầng Ways Station là tối ưu hóa chi phí hoạt
động và chi phí vốn thông qua việc áp dụng kiến trúc linh hoạt. Việc lựa
chọn mô hình triển khai --- cho dù là máy chủ nội bộ, Cloud hay Đám mây
lai --- đều ảnh hưởng trực tiếp đến Tổng chi phí sở hữu và Tỷ suất hoàn
vốn.

Hệ thống được kỳ vọng sẽ giảm thiểu 25-30% chi phí lưu kho và hao hụt
hàng hóa nhờ vào dự báo chính xác. Về mặt hạ tầng IT, việc ứng dụng kiến
trúc Đám mây lai kết hợp với công nghệ Containerization (như
Docker/Kubernetes) cho phép Ways Station tận dụng tài nguyên máy chủ nội
bộ cho các tác vụ xử lý dữ liệu nhạy cảm, đồng thời Burst sang Cloud (mở
rộng linh hoạt lên môi trường điện toán đám mây) trong các dịp cao điểm.
Sự phân bổ này mang lại một KPI về tài chính: Giảm tối đa chi phí
Compute nhàn rỗi xuống dưới 10% tổng ngân sách IT hàng tháng.

### Cải thiện Cam kết Chất lượng Dịch vụ (SLA) và Tính sẵn sàng

Hạ tầng IT phục vụ ứng dụng AI phải đảm bảo mức Cam kết chất lượng dịch
vụ ở mức doanh nghiệp. Hệ thống cốt lõi và các API Endpoint cung cấp
dịch vụ dự báo phải luôn sẵn sàng. Ways Station đặt mục tiêu đạt được
SLA 99.99%, tương đương với thời gian gián đoạn không quá 52.6 phút mỗi
năm. Sự cải thiện SLA này được củng cố bởi các thiết kế dự phòng, cân
bằng tải tại các tầng mạng và khả năng chuyển đổi dự phòng tự động của
hệ quản trị cơ sở dữ liệu và Storage.

### Nâng cao Trải nghiệm Khách hàng

Mặc dù là các chỉ số về hệ thống hậu tuyến, nhưng hiệu suất trực tiếp
tác động đến Trải nghiệm người dùng cuối. Hệ thống API Gateway của Ways
Station phải phản hồi các yêu cầu truy vấn dữ liệu từ Mobile App hoặc
Web Portal của các đối tác, nhà cung cấp trong thời gian thực. Một hệ
thống phản hồi siêu tốc giúp đối tác lập kế hoạch logistics tốt hơn,
giảm thiểu tình trạng đứt gãy cung ứng tại các điểm bán, từ đó nâng cao
mức độ hài lòng và giữ chân khách hàng.

## Mục tiêu cụ thể về Hiệu suất Mô hình Dự báo

Trong dự án này, hệ thống dự báo chuỗi thời gian sử dụng các mô hình học
sâu hiện đại, đặc biệt là các Mô hình Nền tảng Chuỗi thời gian. Việc áp
dụng công nghệ mới nhất như Google TimesFM hay Amazon Chronos đòi hỏi
việc thiết lập các KPI đánh giá khắt khe về độ chính xác toán học.

### Độ chính xác dự báo: MAPE \< 15%

Việc đánh giá độ chính xác của mô hình Time Series thường phức tạp do sự
tồn tại của các thành phần như xu hướng, tính mùa vụ và nhiễu. Ways
Station đặt mục tiêu chỉ số MAPE (Mean Absolute Percentage Error - Sai
số phần trăm tuyệt đối trung bình) duy trì ở mức **\< 15%** đối với các
mặt hàng chủ lực.

**Giải thích sâu về MAPE**: MAPE đo lường tỷ lệ phần trăm sai lệch giữa
giá trị dự báo và giá trị thực tế. Lý do MAPE được lựa chọn làm KPI
chính yếu thay vì RMSE hay MAE là vì MAPE mang tính tương đối. Điều này
cho phép Ban Giám đốc và các nhà phân tích chuỗi cung ứng dễ dàng so
sánh hiệu suất dự báo qua các danh mục sản phẩm khác nhau có quy mô
doanh số chênh lệch lớn (ví dụ: sản phẩm bán được 1000 đơn vị/ngày so
với sản phẩm bán 10 đơn vị/ngày).

### Khung thời gian dự báo: 7-14 ngày

Đặc thù ngành F&B và bán lẻ của Ways Station yêu cầu một vòng quay hàng
tồn kho tối ưu để đảm bảo độ tươi mới của sản phẩm. Do đó, Khung thời
gian dự báo được xác định là **từ 7 đến 14 ngày**.

Nếu Horizon quá ngắn (ví dụ 1-2 ngày), bộ phận mua hàng sẽ không đủ thời
gian chuẩn bị và đặt hàng từ các nhà cung cấp.

Nếu Horizon quá dài (trên 30 ngày), độ không chắc chắn trong mô hình
Time Series sẽ tăng lên theo cấp số nhân, làm suy giảm nghiêm trọng độ
chính xác. Horizon 7-14 ngày là điểm cân bằng lý tưởng, tận dụng sức
mạnh của các mô hình Transformer-based.

### Độ trễ suy luận: \< 1 giờ cho Batch, \< 500ms cho thời gian thực

Với việc tích hợp các mô hình tiên tiến như:

**Google TimesFM**: Mô hình sử dụng kiến trúc Decoder-only, cơ chế
Patching (chia chuỗi thời gian thành các mảng nhỏ) cho phép dự báo không
cần huấn luyện (zero-shot) (không cần fine-tuning) trên dữ liệu đa biến
với tốc độ cao.

**Amazon Chronos**: Mô hình tiếp cận chuỗi thời gian theo dạng xử lý
ngôn ngữ tự nhiên thông qua mã hóa (tokenization) các giá trị liên tục,
đặc biệt với phiên bản Chronos-Bolt.

Mặc dù có sức mạnh to lớn, các mô hình này cần hạ tầng Compute mạnh. Do
vậy KPI về độ trễ được định nghĩa như sau:

**Batch Prediction (Dự báo hàng loạt)**: Thực hiện vào ban đêm qua luồng
dữ liệu của kho dữ liệu/Lakehouse. Toàn bộ dự báo cho hàng trăm nghìn
SKU phải hoàn thành trong thời gian **dưới 1 giờ**.

**Thời gian thực suy luận (Suy luận thời gian thực)**: Với một số bài
toán cần điều chỉnh dự báo tức thời khi có sự kiện đột biến, mô hình dự
báo trực tuyến qua API Gateway phải phản hồi với độ trễ **nhỏ hơn 500
mili-giây**, đảm bảo không nghẽn cổ chai hệ thống mạng.

## Phương pháp Đo lường và Công cụ Giám sát Cơ sở hạ tầng

Để đảm bảo các mục tiêu và KPI khắt khe trên không chỉ nằm trên giấy, dự
án Ways Station thiết lập một kiến trúc Giám sát toàn diện dựa trên
nguyên tắc \"Three Pillars of Observability\" (Ba cột trụ của Khả năng
quan sát): Metrics (Chỉ số), Tracing (Truy vết) và Logging (Nhật ký).

### Công cụ Giám sát Cơ sở hạ tầng

**Prometheus**: Hoạt động như một cỗ máy thu thập dữ liệu chuỗi thời
gian. Prometheus sẽ liên tục \"cào\" dữ liệu từ các Node Exporter trên
các máy chủ vật lý, cAdvisor trên các container, và các exporter trên cơ
sở dữ liệu. Nó giám sát CPU, RAM, Disk I/O, và Network Throughput.

**Grafana**: Đóng vai trò là trung tâm hiển thị trực quan. Các kỹ sư
quản trị hệ thống sẽ nhìn thấy biểu đồ theo thời gian thực về tình trạng
sức khỏe của toàn bộ hệ thống. Grafana cũng hiển thị trực tiếp các KPI
toán học của mô hình học máy được đẩy lên từ môi trường Python/MLflow.

### Quản lý Nhật ký Tập trung (Centralized Logging với ELK Stack)

Việc tìm kiếm nguyên nhân gốc rễ khi hệ thống gặp sự cố là tối quan
trọng.

Các log từ API Gateway, Middleware, Backend service, và Model inference
script đều được chuẩn hóa bằng JSON và lưu trữ có cấu trúc. Nhờ vậy, khi
có một giao dịch bị lỗi (ví dụ: mất dữ liệu đơn hàng), kỹ sư có thể truy
vấn ngay lập tức thông qua Kibana.

### Truy vết Phân tán

Với kiến trúc Microservices và API Gateway, một request từ người dùng có
thể đi qua hàng tá dịch vụ. Ways Station sẽ tích hợp **Jaeger** hoặc
**OpenTelemetry**. Tracing giúp đo lường chính xác \"suy luận độ trễ \<
500ms\" bị vi phạm ở phân đoạn nào (do truy vấn DB chậm, do tính toán
GPU bị trễ, hay do nghẽn mạng).

### Cảnh báo Chủ động

Thay vì chờ đợi người dùng phản ánh lỗi, hệ thống áp dụng:

**Ngưỡng-based Alerts**: Cảnh báo dựa trên ngưỡng tĩnh (Ví dụ: Ổ cứng
đầy quá 85%, Prometheus Alertmanager sẽ gửi tin nhắn qua Slack/Email cho
kỹ sư trực hệ thống).

**Anomaly Detection (Phát hiện bất thường)**: Ứng dụng chính các mô hình
AI để theo dõi metrics. Nếu lượng truy cập qua Middleware API tăng đột
biến 500% so với ngày bình thường, hệ thống tự động nghi ngờ có tấn công
DDoS hoặc botnet và lập tức báo cáo tới hệ thống Security Information
and Event Management (SIEM).

# Đối tượng, phạm vi và giả định/ràng buộc

Trong bối cảnh chuyển đổi số và tối ưu hóa vận hành tại chuỗi Ways
Station, việc xác định rõ ràng đối tượng phục vụ, phạm vi triển khai,
cũng như các giả định, ràng buộc và rủi ro đi kèm là bước nền tảng vô
cùng quan trọng. Dự án này không chỉ đơn thuần là việc áp dụng các thuật
toán máy học, mà là một sự chuyển đổi toàn diện về kiến trúc cơ sở hạ
tầng công nghệ thông tin, từ quy trình xử lý dữ liệu, nền tảng vận hành,
cho đến việc ứng dụng các mô hình ngôn ngữ/thời gian tiên tiến nhất hiện
nay như Mô hình nền tảng chuỗi thời gian (TSFM).

Phần này sẽ đi sâu vào việc phân tích và thiết kế chi tiết kiến trúc
giải pháp, vạch ra ranh giới rõ ràng của dự án và các phương án dự phòng
chiến lược, đảm bảo hệ thống có khả năng mở rộng, tính sẵn sàng cao và
tuân thủ chặt chẽ các tiêu chuẩn bảo mật và pháp lý hiện hành.

## Đối tượng áp dụng và Thụ hưởng

Hệ thống hạ tầng phân tích và dự báo chuỗi thời gian của Ways Station
được thiết kế để phục vụ đa dạng các nhóm đối tượng, từ cấp độ chiến
lược đến cấp độ vận hành chi tiết:

**Ban Giám đốc và C-level:**

- **Mục đích:** Hỗ trợ ra quyết định chiến lược về mở rộng chuỗi, phân
  bổ nguồn lực vốn và quản trị rủi ro doanh thu.

- **Giá trị mang lại (ROI):** Thông qua các báo cáo Dashboard được tổng
  hợp từ nền tảng kho dữ liệu trung tâm (Lakehouse), Ban Giám đốc có cái
  nhìn toàn cảnh về dự báo doanh thu dài hạn. Các mô hình TSFM cung cấp
  khoảng tin cậy giúp lượng hóa rủi ro kinh doanh, từ đó tối ưu hóa tổng
  chi phí sở hữu và cải thiện lợi tức đầu tư (ROI).

**Quản lý chi nhánh:**

- **Mục đích:** Tối ưu hóa vận hành hàng ngày, chuẩn bị nguồn lực (thực
  phẩm, trang thiết bị) dựa trên dự báo lượng khách hàng theo từng khung
  giờ.

- **Giá trị mang lại:** Giảm thiểu lãng phí thông qua các dự báo ngắn
  hạn. Quản lý chi nhánh tương tác với hệ thống qua các API Gateway được
  bảo mật, nhận thông báo đẩy theo thời gian thực về những đợt tăng vọt
  khách hàng bất thường.

**Bộ phận Công nghệ thông tin và Dữ liệu:**

- **Mục đích:** Quản trị, duy trì và nâng cấp kiến trúc dữ liệu, đường
  ống CI/CD/CT.

- **Giá trị mang lại:** Nền tảng MLOps tự động hóa hoàn toàn vòng đời
  của mô hình AI, từ thu thập dữ liệu, huấn luyện, đánh giá đến triển
  khai. Việc sử dụng Containerization và Orchestration giúp đội ngũ
  DevOps dễ dàng quản lý tài nguyên, thực hiện rolling updates mà không
  gây gián đoạn dịch vụ.

**Bộ phận Marketing & Sales:**

- **Mục đích:** Đánh giá hiệu quả của các chiến dịch khuyến mãi, sự kiện
  eSports và lập kế hoạch ngân sách quảng cáo.

- **Giá trị mang lại:** Hệ thống cung cấp khả năng phân tích nhân quả
  kết hợp dự báo, giúp phân tách rõ ràng sự gia tăng doanh thu do yếu tố
  tự nhiên và do tác động của sự kiện.

## Phạm vi của Dự án

Để đảm bảo tính khả thi và tập trung nguồn lực, dự án thiết lập ranh
giới rõ ràng thông qua hai phân nhóm chính: Trong phạm vi và Ngoài phạm
vi.

### Trong phạm vi

Phạm vi cốt lõi của dự án xoay quanh việc xây dựng một hệ sinh thái kiến
trúc dữ liệu vững chắc và ứng dụng các mô hình trí tuệ nhân tạo chuyên
biệt cho chuỗi thời gian:

**Kiến trúc Dữ liệu và Tích hợp:**

- **Mô hình Dữ liệu:** Triển khai kiến trúc **kho dữ liệu trung tâm
  (Lakehouse)** (kết hợp ưu điểm của hồ dữ liệu và kho dữ liệu), sử dụng
  các định dạng dữ liệu mở như Delta Lake hoặc Apache Hudi trên hạ tầng
  lưu trữ Object Storage (ví dụ: Amazon S3, MinIO máy chủ nội bộ). Điều
  này cho phép xử lý hiệu quả cả dữ liệu có cấu trúc (giao dịch POS) và
  bán cấu trúc (log hệ thống, JSON từ API).

<!-- -->

- **Luồng xử lý:** Xây dựng các đường ống ETL/ELT theo cả cơ chế Batch
  Processing (xử lý lô hàng ngày qua Apache Airflow/Spark) và Stream
  Processing (xử lý luồng thời gian thực qua Apache Kafka/Flink) để bắt
  kịp các sự kiện phát sinh tức thì.

<!-- -->

- **Tích hợp hệ thống:** Kết nối qua các chuẩn API RESTful/gRPC với các
  hệ thống ERP, CRM và POS hiện tại của Ways Station thông qua một API
  Gateway nội bộ để chuẩn hóa và định tuyến lưu lượng.

**Mô hình Dự báo Chuỗi thời gian:**

Thay vì sử dụng các mô hình học máy truyền thống cần đào tạo lại từ đầu,
dự án sẽ tích hợp các TSFM tân tiến mang tính đột phá:

**Google TimesFM:**

Khai thác kiến trúc *Decoder-only transformer* tương tự như các mô hình
ngôn ngữ lớn, nhưng được tinh chỉnh đặc biệt cho dữ liệu số.

Áp dụng cơ chế *Patching* (chia chuỗi thời gian thành các \"mảnh\" thay
vì từng điểm dữ liệu đơn lẻ), giúp tăng tốc độ suy luận lên nhiều lần và
giảm tải tính toán.

Khả năng *không cần huấn luyện (zero-shot) forecasting*: Dự báo cho các
chuỗi thời gian mới (như chi nhánh mới mở) mà không cần hoặc cần rất ít
dữ liệu fine-tuning, giải quyết triệt để bài toán Cold Start.

Xử lý *Multivariate*: Tích hợp nhiều biến số ngoại sinh như thời tiết,
lịch nghỉ lễ, giá cả để tăng độ chính xác.

**Amazon Chronos:**

Ứng dụng phương pháp *mã hóa (tokenization)* lên dữ liệu chuỗi thời
gian, biến đổi dữ liệu định lượng thành một dạng \"ngôn ngữ\" và sử dụng
các kiến trúc Language Model (LM) để dự đoán chuỗi token tiếp theo.

Tích hợp phiên bản *Chronos-Bolt* cho hiệu năng inference siêu tốc với
tài nguyên Compute tối thiểu, phù hợp cho việc triển khai ở các Edge
Nodes tại các cụm máy chủ cục bộ của Ways Station.

Hệ thống Containerization và Hạ tầng triển khai

**Môi trường Container:** Toàn bộ các dịch vụ từ Backend API, Data
Workers đến suy luận Endpoints đều được đóng gói bằng **Docker**. Việc
này đảm bảo tính nhất quán giữa môi trường phát triển và sản xuất.

**Điều phối:** Triển khai hệ thống trên cụm **Kubernetes (K8s)**. K8s
cung cấp khả năng tự động mở rộng dựa trên các metric tải CPU/GPU hoặc
độ trễ. Cấu hình Helm Charts để quản lý các bản phát hành một cách có hệ
thống.

**Mô hình Hybrid-Cloud:** Tận dụng hạ tầng Compute máy chủ nội bộ cho
các workload mang tính bảo mật cao (xử lý thông tin người dùng) và
Bursting lên Cloud (AWS/GCP) để thuê GPU linh hoạt trong những giai đoạn
retrain mô hình nặng.

### Ngoài phạm vi

Để giữ vững tiến độ và tránh lạm dụng công nghệ, dự án cam kết KHÔNG bao
gồm các hạng mục sau:

**Không tích hợp Mô hình Ngôn ngữ Lớn (LLM) cho giao tiếp:** Dự án không
phát triển chatbot tương tác với khách hàng hay hệ thống sinh văn bản tự
động. Mọi công nghệ AI (như TimesFM/Chronos) được sử dụng thuần túy dưới
góc độ tính toán chuỗi thời gian định lượng, không xử lý ngôn ngữ tự
nhiên (NLP).

**Không tự động hóa xếp lịch nhân sự:** Hệ thống chỉ dừng lại ở bước
\"Cung cấp dự báo về lượng khách và khối lượng công việc dự kiến\". Các
quy trình quản trị nhân sự (HR), phân ca làm việc, chấm công tự động sẽ
thuộc về một module ERP riêng biệt và không nằm trong phạm vi kỹ thuật
số của dự án này.

**Không thay đổi phần cứng máy trạm của khách hàng:** Các nâng cấp hạ
tầng chỉ áp dụng ở cấp độ máy chủ, các máy tính phục vụ game thủ tại
Ways Station không thuộc đối tượng can thiệp của dự án.

## Luồng ngoại lệ và Xử lý tình huống biên

Hệ thống học máy trong thực tế luôn phải đối mặt với các tình huống bất
thường. Việc thiết kế các luồng ngoại lệ là tiêu chuẩn bắt buộc trong
kiến trúc MLOps chuyên nghiệp.

**Hiện tượng khởi động lạnh cho chi nhánh mới mở:**

- **Tình huống:** Một cơ sở Ways Station mới khai trương sẽ không có dữ
  liệu lịch sử để dự báo doanh thu. Các mô hình truyền thống sẽ thất bại
  do thiếu hụt chuỗi dữ liệu đầu vào tối thiểu.

- **Luồng xử lý:** Hệ thống sẽ kích hoạt tính năng **không cần huấn
  luyện (zero-shot) forecasting** của Google TimesFM, sử dụng các tham
  số pre-trained từ tập dữ liệu khổng lồ của các chi nhánh khác có đặc
  điểm tương đồng làm Proxy Data. Ngay khi cơ sở mới tạo ra dữ liệu,
  kiến trúc Continuous Training sẽ thu thập luồng Kafka stream và bắt
  đầu quá trình fine-tuning vi mô để điều chỉnh trọng số mô hình cho
  riêng chi nhánh đó sau 7-14 ngày.

**Biến động bất thường và Ngoại lai:**

- **Tình huống:** Có các sự kiện đột biến phá vỡ xu hướng chuỗi thời
  gian như: Giải đấu eSports khu vực, chương trình Flash Sale khốc liệt,
  hoặc thiên tai, sự cố cúp điện diện rộng.

- **Luồng xử lý:** Kiến trúc pipeline sẽ tích hợp module **Anomaly
  Detection** (ví dụ: Isolation Forest, Autoencoders). Khi dữ liệu đầu
  vào vượt qua ngưỡng kiểm soát hoặc có độ lệch chuẩn lớn hơn 3 Sigma,
  hệ thống tự động gắn cờ. Dữ liệu này sẽ được cô lập vào bảng
  \"Exception Data\" trên Lakehouse. Mô hình dự báo sẽ tự động chuyển
  đổi sang chế độ đánh trọng số thấp cho các điểm dữ liệu này để tránh
  bị nhiễu (overfitting vào noise).

**Xử lý lỗi và mất mát dữ liệu:**

- **Tình huống:** API thu thập dữ liệu từ hệ thống POS bị lỗi mạng dẫn
  đến mất dữ liệu trong nhiều giờ, hoặc quá trình đồng bộ gửi lên các
  bản ghi bị trùng lặp.

<!-- -->

- **Luồng xử lý:** Áp dụng nguyên tắc **Data Quality Gates** tại lớp
  Ingestion. Sử dụng công cụ như Great Expectations để kiểm thử chất
  lượng dữ liệu tự động. Nếu phát hiện Missing Values, hệ thống kích
  hoạt thuật toán Imputation (như KNN Imputer, Spline Interpolation) đối
  với các khoảng trống ngắn. Nếu mất dữ liệu trên 24 giờ, hệ thống cảnh
  báo tức thì cho Kỹ sư dữ liệu và mô hình AI sẽ dùng giá trị dự báo
  thay thế để điền vào cho mục đích hiển thị tạm thời.

## Giả định, Ràng buộc và Tuân thủ

Việc thiết kế cơ sở hạ tầng CNTT phải bị ràng buộc bởi các quy định pháp
lý, năng lực phần cứng và các chuẩn mực bảo mật ngành.

### Khía cạnh Pháp lý và Quyền riêng tư

**Tuân thủ Nghị định 13/2023/NĐ-CP (PDPB):** Vì Ways Station lưu trữ
thông tin hội viên (tên, số điện thoại, lịch sử nạp tiền/tiêu dùng),
toàn bộ luồng dữ liệu bắt buộc tuân thủ quy định bảo vệ Dữ liệu Cá nhân
của Việt Nam.

**Ràng buộc kỹ thuật:** Không có bất kỳ dữ liệu định danh cá nhân (PII)
nào dạng văn bản rõ được phép đưa vào hồ dữ liệu để huấn luyện mô hình.
Ở tầng ETL, mọi trường nhạy cảm phải được băm (Hashing với Salt) hoặc mã
hóa. Các kỹ sư dữ liệu chỉ được cấp quyền truy cập vào các tập dữ liệu
đã ẩn danh hóa hoàn toàn để phân tích hành vi vĩ mô.

### Hạ tầng Mạng và Bảo mật

**Tường lửa thế hệ mới và Ứng dụng web:** Toàn bộ các API Endpoints công
khai phải đứng sau một Web Application Firewall để chống lại các cuộc
tấn công OWASP Top 10 (như SQL Injection, DDoS, API Abuse).

**Mạng Rêng Ảo (VPN) & Zero Trust Network Access (ZTNA):** Giả định rằng
toàn bộ các chi nhánh Ways Station kết nối về trung tâm dữ liệu thông
qua đường truyền SD-WAN có mã hóa IPsec VPN. Tuy nhiên, hệ thống nội bộ
vẫn tuân thủ mô hình Zero Trust: \"Không tin tưởng bất cứ thiết bị/người
dùng nào dù ở bên trong hay bên ngoài mạng\". Việc giao tiếp giữa các
microservices trong cụm Kubernetes bắt buộc phải qua cơ chế xác thực
mTLS do Service Mesh (như Istio) điều phối.

**Quản lý Định danh và Truy cập:** Việc quản trị cơ sở hạ tầng được ràng
buộc bởi Role-Based Access Control chặt chẽ. Chỉ có các DevOps được cấp
quyền \`admin\` tạm thời mới được phép thực thi cấu hình hạ tầng.

### Giả định về Nguồn lực

**Chi phí sở hữu (TCO):** Ràng buộc không sử dụng các dịch vụ Cloud
Managed (như AWS SageMaker) quá mức, nhằm kiểm soát chi phí vận hành
(OPEX). Kiến trúc phải linh hoạt thông qua Docker để có thể di dời về hệ
thống máy chủ vật lý giá rẻ khi cần.

**Chất lượng băng thông:** Giả định rằng đường truyền mạng ở các chi
nhánh ngoại ô có thể không ổn định, do đó Edge Node tại chi nhánh phải
có khả năng lưu trữ tạm dữ liệu và gửi bù khi có kết nối mạng trở lại.

## Quản trị Rủi ro và Phương án Dự phòng

Kiến trúc hạ tầng IT hiện đại đòi hỏi một chiến lược phản ứng dự phòng
khép kín để đảm bảo tính liên tục của hoạt động kinh doanh.

### Mô hình Dự phòng

Các mô hình TSFM tiên tiến tuy hiệu năng vượt trội nhưng đòi hỏi cao về
khả năng tính toán. Rủi ro phát sinh khi API server quá tải, hoặc
Tensor/Out-Of-Memory (OOM) trong môi trường Kubernetes.

**Phương án Fallback:** Thiết lập kiến trúc **Shadow Deployment** và
**Graceful Degradation**. Khi request tới mô hình TSFM vượt quá Timeout
giới hạn (ví dụ: \> 2000ms), API Gateway sẽ lập tức định tuyến yêu cầu
xuống các mô hình nhẹ hơn đã được huấn luyện song song. Các mô hình này
là thuật toán học máy cổ điển như **XGBoost, LightGBM**, hoặc các mô
hình thống kê như **ARIMA, Facebook Prophet**. Dù độ chính xác có thể
giảm đi 5-10%, hệ thống vẫn đảm bảo trả về kết quả khả dụng, tránh để UI
hiển thị lỗi \"503 Service Unavailable\" cho người dùng.

### Khôi phục sau thảm họa

Hệ thống phải chịu đựng được những thảm họa lớn như cháy nổ trung tâm dữ
liệu, mã độc tống tiền hoặc lỗi con người xóa nhầm Database.

**RPO:** Giới hạn tối đa lượng dữ liệu có thể bị mất là **1 giờ**. Mọi
transaction quan trọng phải được sao lưu đồng bộ/bán đồng bộ sang một
cụm lưu trữ Standby.

**RTO:** Thời gian tối đa để đưa hệ thống hoạt động trở lại sau thảm họa
là **4 giờ**. Nhờ toàn bộ kiến trúc hạ tầng được code hóa
(Infrastructure-as-Code - IaC bằng Terraform) và ứng dụng container hóa,
việc dựng lại toàn bộ môi trường từ đầu ở một trung tâm dữ liệu khác
(Multi-AZ hoặc Multi-Region) diễn ra hoàn toàn tự động.

**Chiến lược Sao lưu:**

**Dữ liệu:** Áp dụng quy tắc dự phòng chuẩn công nghiệp 3-2-1. Thực hiện
*Incremental Backup* (sao lưu tăng dần) mỗi 1 giờ đối với cơ sở dữ liệu
giao dịch, và *Full Backup* định kỳ vào 2:00 sáng chủ nhật hàng tuần đối
với hệ thống hồ dữ liệu. Các bản backup được lưu tại phân vùng lưu trữ
bất biến ngăn chặn hoàn toàn khả năng ransomware mã hóa ghi đè.

**Source Code & Model Artifacts:** Quản lý phiên bản chặt chẽ qua Git và
các công cụ như MLflow/DVC. Các trọng số mô hình của TimesFM/Chronos
được sao lưu định kỳ vào kho Artifact Registry an toàn.

Bằng việc thiết lập rõ ràng ranh giới phạm vi, dự báo các tình huống
ngoại lệ, tuân thủ pháp luật về dữ liệu, và xây dựng các lớp dự phòng
chuẩn chỉ từ ứng dụng đến hạ tầng, BƯỚC 4 đảm bảo dự án phân tích dữ
liệu cho Ways Station sẽ đứng vững trước các rủi ro vận hành phức tạp
nhất trong thực tế.
