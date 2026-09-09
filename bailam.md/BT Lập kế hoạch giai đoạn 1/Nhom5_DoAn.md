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

[Bước 0 Xác định phạm vi đề xuất
[2](#xác-định-phạm-vi-đề-xuất)](#xác-định-phạm-vi-đề-xuất)

[0.1 Tóm tắt bối cảnh và vấn đề
[2](#tóm-tắt-bối-cảnh-và-vấn-đề)](#tóm-tắt-bối-cảnh-và-vấn-đề)

[0.2 Phạm vi đầu tư hạ tầng cốt lõi
[2](#phạm-vi-đầu-tư-hạ-tầng-cốt-lõi)](#phạm-vi-đầu-tư-hạ-tầng-cốt-lõi)

[0.3 Đối tượng thụ hưởng & Mục tiêu thời gian
[2](#đối-tượng-thụ-hưởng-mục-tiêu-thời-gian)](#đối-tượng-thụ-hưởng-mục-tiêu-thời-gian)

[Bước 1 Khảo sát hiện trạng hạ tầng có số liệu
[3](#khảo-sát-hiện-trạng-hạ-tầng-có-số-liệu)](#khảo-sát-hiện-trạng-hạ-tầng-có-số-liệu)

[1.1 Tính toán & Kết nối [3](#tính-toán-kết-nối)](#tính-toán-kết-nối)

[1.2 Vận hành [3](#vận-hành)](#vận-hành)

[1.3 Bảo mật & Danh tính (Bảo mật + Định danh)
[4](#bảo-mật-danh-tính-bảo-mật-định-danh)](#bảo-mật-danh-tính-bảo-mật-định-danh)

[1.4 Ứng dụng & Tích hợp [4](#ứng-dụng-tích-hợp)](#ứng-dụng-tích-hợp)

[1.5 Nền tảng Dữ liệu [4](#nền-tảng-dữ-liệu)](#nền-tảng-dữ-liệu)

[Bước 2 Nêu vấn đề & rủi ro nếu không đầu tư (Tại sao phải làm ngay?)
[4](#nêu-vấn-đề-rủi-ro-nếu-không-đầu-tư-tại-sao-phải-làm-ngay)](#nêu-vấn-đề-rủi-ro-nếu-không-đầu-tư-tại-sao-phải-làm-ngay)

[2.1 Tác động Vận hành [5](#tác-động-vận-hành)](#tác-động-vận-hành)

[2.2 Tác động Tuân thủ & Bảo mật (Tác động Tuân thủ & Bảo mật theo Nghị
định 13/2023/NĐ-CP)
[5](#tác-động-tuân-thủ-bảo-mật-tác-động-tuân-thủ-bảo-mật-theo-nghị-định-132023nđ-cp)](#tác-động-tuân-thủ-bảo-mật-tác-động-tuân-thủ-bảo-mật-theo-nghị-định-132023nđ-cp)

[2.3 Tác động Chiến lược
[6](#tác-động-chiến-lược)](#tác-động-chiến-lược)

[Bước 3 Xác lập mục tiêu & KPI hạ tầng
[7](#xác-lập-mục-tiêu-kpi-hạ-tầng)](#xác-lập-mục-tiêu-kpi-hạ-tầng)

[Bước 4 Xây dựng phương án kiến trúc Mục tiêu tương lai (2--3 lựa chọn)
[8](#xây-dựng-phương-án-kiến-trúc-mục-tiêu-tương-lai-23-lựa-chọn)](#xây-dựng-phương-án-kiến-trúc-mục-tiêu-tương-lai-23-lựa-chọn)

# Xác định phạm vi đề xuất

## Tóm tắt bối cảnh và vấn đề

Ways Station là một hệ sinh thái dịch vụ tích hợp đa nền tảng, bao gồm
các mảng kinh doanh cốt lõi: Gaming, Billiards, Gym & Fitness, Cầu lông,
và Hub F&B. Chỉ trong chưa đầy 2 năm, quy mô của Ways Station đã phát
triển thần tốc từ 22 lên hơn 34 chi nhánh, phủ rộng khắp các quận huyện
tại TP. Hồ Chí Minh.

Tuy nhiên, sự mở rộng vật lý diễn ra quá nhanh trong khi hạ tầng công
nghệ thông tin không theo kịp đã tạo ra \"trần nhà bằng kính\" cản trở
sự phát triển. Các phần mềm nghiệp vụ hiện tại (MODUN gym, hệ thống CSM
Net, máy Máy tính tiền Bida) hoạt động như những \"ốc đảo dữ liệu\" độc
lập. Mọi tác vụ đồng bộ, kết nối dữ liệu giữa các chi nhánh và hội sở
đều được thực hiện thủ công bằng sức người (thông qua Excel và Zalo).

## Phạm vi đầu tư hạ tầng cốt lõi

Để giải quyết bài toán cốt lõi về sự phân mảnh hệ thống, dự án này không
đề xuất mua sắm các thiết bị phần cứng một cách rời rạc tại từng chi
nhánh. Thay vào đó, dự án tập trung ngân sách để đầu tư xây dựng năng
lực hạ tầng ở 2 phân lớp lõi trên môi trường Điện toán đám mây lai:

\- Lớp 4 (App & Integration Platform): Xây dựng hệ thống Cổng giao tiếp
ứng dụng tập trung để kết nối và chuẩn hóa luồng giao tiếp giữa các phần
mềm hiện hữu. Triển khai kiến trúc Kiến trúc dịch vụ vi mô và hệ thống
định danh tập trung để đồng nhất tài khoản khách hàng trên toàn bộ hệ
sinh thái.

\- Lớp 5 (Data Platform): Xây dựng kho dữ liệu tập trung có khả năng thu
thập, xử lý luồng dữ liệu tự động từ 34+ chi nhánh. Triển khai các hệ
thống báo cáo thông minh theo thời gian thực.

## Đối tượng thụ hưởng & Mục tiêu thời gian

\- Ban điều hành & Quản lý: Có khả năng ra quyết định dựa trên dữ liệu
nhờ báo cáo doanh thu, tồn kho thời gian thực.

\- Nhân viên chi nhánh: Xóa bỏ 100% công việc nhập liệu báo cáo Excel
thủ công, giải phóng hàng chục giờ công mỗi ca trực.

\- Khách hàng: Trải nghiệm dịch vụ liền mạch với một tài khoản duy nhất
để tích điểm và thanh toán cho tất cả các dịch vụ (Gym, Net, Bida).

\- Thời gian triển khai: Lộ trình 12 tháng (chia làm 4 giai đoạn theo mô
hình Phát triển linh hoạt / Triển khai cuốn chiếu):

\- Giai đoạn 1 (Tháng 1 - 3) - Thiết lập nền móng: Khảo sát toàn bộ
Database chi nhánh; thiết lập môi trường Container trên Điện toán đám
mây; triển khai cấu trúc lõi của Cổng giao tiếp ứng dụng tập trung và
Kho dữ liệu hội tụ; cấu hình mạng an toàn.

\- Giai đoạn 2 (Tháng 4 - 6) - Tích hợp & App nội bộ: Xây dựng luồng dữ
liệu đồng bộ tự động mỗi 15 phút; triển khai Quản trị dữ liệu chủ chuẩn
hóa danh mục; ra mắt App vận hành nội bộ (chốt ca, báo cáo sự cố).

\- Giai đoạn 3 (Tháng 7 - 9) - Định danh & Phân tích: Triển khai hệ
thống định danh dùng chung; ra mắt hệ thống BI Dashboard thời gian thực;
chạy thử nghiệm tại 3 chi nhánh lớn nhất.

\- Giai đoạn 4 (Tháng 10 - 12) - Go-Live & Tối ưu: Mở rộng hệ thống
xuống 30+ chi nhánh còn lại; tổ chức đào tạo người dùng; thiết lập quy
trình giám sát vận hành và bảo mật.

# Khảo sát hiện trạng hạ tầng có số liệu

Hệ thống vận hành hiện tại phụ thuộc hoàn toàn vào sức người. Việc thiếu
hụt một hạ tầng số tập trung đã bộc lộ những con số đáng báo động trên
cả 5 phân lớp:

## Tính toán & Kết nối

\- Máy chủ cục bộ: Mỗi chi nhánh được trang bị 1 PC hoặc Server dạng
Tower tự lắp ráp, tuổi đời phần cứng trung bình từ 2-4 năm. Cấu hình cực
kỳ phân mảnh (Core i5/i7 thế hệ cũ, 16-32GB RAM). Các thiết bị này chạy
liên tục 24/7 trong môi trường nhiều bụi (phòng Net, Gym) dẫn đến tỷ lệ
hỏng hóc phần cứng lên tới 15%/năm.

\- Băng thông & Mạng: Sử dụng đường truyền Internet cáp quang hoặc
Leased Line đơn kênh cấp phát IP động. Đa số các chi nhánh sử dụng
Router nhà mạng cấp hoặc các dòng Router phổ thông (DrayTek, MikroTik
phân khúc thấp).

\- Vấn đề Cấu trúc mạng mạng: Hệ thống mạng nội bộ tại chi nhánh sử dụng
Switch Không quản trị, hoàn toàn không chia VMạng nội bộ rõ ràng giữa
mạng khách và mạng nội bộ. Bất kỳ khách hàng nào kết nối vào Wi-Fi quán
đều có khả năng scan ra IP của máy tính tiền, tạo ra một lỗ hổng mạng vô
cùng lớn. Không có cấu hình SD-WAN để tối ưu định tuyến băng thông.

\- Điểm sự cố duy nhất (Điểm sự cố duy nhất): Mô hình mạng hình sao giả
lập thông qua VPN thủ công. 100% chi nhánh đối mặt với rủi ro Điểm sự cố
duy nhất. Nếu ổ cứng máy chủ Máy tính tiền hoặc Router mạng tại chi
nhánh bị hỏng, toàn bộ hoạt động kinh doanh (tính tiền, thẻ xe, hội
viên) sẽ ngưng trệ hoàn toàn. Tỷ lệ dự phòng tại chi nhánh bằng 0.

## Vận hành

\- Hệ thống giám sát: Không tồn tại hệ thống giám sát tập trung (như
Zabbix, Prometheus, Grafana). Các thông số về CPU/RAM Mức độ sử dụng,
nhiệt độ Server, hay tình trạng ổ cứng hoàn toàn là một \"hộp đen\". Đội
IT chỉ nhận biết sự cố khi nhân viên chi nhánh nhắn tin báo lỗi qua Zalo
(Hỗ trợ bị động thay vì Chủ động).

\- Chỉ số Thời gian phát hiện (Thời gian phát hiện trung bình - Thời
gian phát hiện sự cố): Kéo dài từ 4 đến 8 tiếng đồng hồ. Thường xuyên bị
báo cáo muộn do nhân viên chi nhánh bận phục vụ khách hàng.

\- Chỉ số Thời gian phục hồi (Thời gian phục hồi trung bình - Thời gian
phục hồi): Từ 12 đến 24 tiếng đồng hồ. Do không có công cụ điều khiển từ
xa chuyên sâu và phụ thuộc phần cứng, nhân viên IT buộc phải di chuyển
vật lý đến tận chi nhánh để cài lại Windows, cấu hình lại Database hoặc
thay thế linh kiện.

\- Sao lưu & Phục hồi thảm họa: Không có cơ chế Backup tự động đồng bộ.
Dữ liệu SQL Server nội bộ được nhân viên thu ngân sao lưu thủ công ra
USB, ổ cứng ngoài hoặc tải lên Google Drive cá nhân. Điểm phục hồi hiện
tại lên tới 24 giờ. Đã từng xảy ra sự cố hỏng ổ cứng vào tháng 3/2025
tại chi nhánh Quận 7 khiến toàn bộ dữ liệu hội viên và doanh thu trong
ngày biến mất vĩnh viễn, tốn hơn 48 giờ để IT phục hồi thủ công (Thời
gian phục hồi = 48h).

## Bảo mật & Danh tính (Bảo mật + Định danh)

\- Quản lý định danh: Định danh khách hàng bị phân mảnh. Máy quét khuôn
mặt tại phòng Gym không liên thông với tài khoản chơi Net. Khách hàng
phải tạo nhiều tài khoản, mỗi hệ thống cấp 1 ID riêng, không thể gộp
điểm thành viên.

\- Bảo mật dữ liệu Điểm cuối: Hình ảnh giấy tờ tùy thân và thông tin cá
nhân khách hàng được thu ngân chụp và gửi qua Zalo nhóm. Không có hệ
thống Phòng chống thất thoát dữ liệu, không có Điểm cuối Detection and
Response trên các máy Máy tính tiền. Các máy Máy tính tiền thường xuyên
bị dính mã độc do nhân viên vô tình lướt web.

\- Tuân thủ: Vi phạm nghiêm trọng Nghị định 13/2023/NĐ-CP về Bảo vệ dữ
liệu cá nhân (chưa có sự đồng ý bằng văn bản của khách, dữ liệu Dữ liệu
cá nhân nhạy cảm lưu dạng plain-text).

## Ứng dụng & Tích hợp

\- Các phần mềm hiện hữu (MODUN gym, CSM Net, Ocha Máy tính tiền) là hệ
thống đóng. Mọi tích hợp đều phải chọc thẳng vào Database thay vì qua
API, gây lỗi nghẽn cổ chai thường xuyên.

\- Quy trình nghiệp vụ đứt gãy: Ví dụ để tạo tài khoản cho 1 khách hàng
VIP chơi cả Bida và Net, nhân viên phải mở 2 phần mềm lên gõ lại thông
tin 2 lần.

\- Quá trình cấu hình phần mềm cho một chi nhánh mới khai trương hoàn
toàn thủ công. Lead time triển khai phần mềm kéo dài từ 5 đến 7 ngày.

## Nền tảng Dữ liệu

\- Lưu trữ & Phân tán: Phân tán trên 34+ ổ cứng vật lý và hàng trăm file
Google Sheet rời rạc. Không có Quản trị dữ liệu chủ. Một món nước
\"Sting Dâu\" có thể có 34 mã SKU khác nhau tại 34 chi nhánh.

\- Luồng dữ liệu thủ công: Thu ngân phải đếm tiền, đối soát Momo/ACB
bằng tay. Cuối ca trực, thu ngân phải gõ lại báo cáo tổng kết ngày vào
bảng tính Excel chung của Kế toán.

\- Độ trễ dữ liệu: Mất từ 24 đến 48 giờ để dữ liệu từ chi nhánh được
tổng hợp, làm sạch (làm sạch dữ liệu thủ công) lên hội sở. Ban giám đốc
luôn xem báo cáo của \"ngày hôm kia\".

**Định lượng Điểm nhức nhối tổng thể:**

\- Lãng phí lao động: 2 giờ x 34 chi nhánh = 68 giờ công lãng phí mỗi
ngày chỉ để nhập liệu thủ công.

\- Tắc nghẽn thanh toán: Tốc độ phục vụ giảm 40% trong khung giờ cao
điểm do quy trình thủ công rời rạc.

# Nêu vấn đề & rủi ro nếu không đầu tư (Tại sao phải làm ngay?)

Việc duy trì hệ thống \"chạy bằng sức người\" không phải là một giải
pháp tiết kiệm (như lầm tưởng ban đầu). Thực chất, chuỗi đang vay mượn
một khoản \"Nợ kỹ thuật\" khổng lồ với lãi suất rất cao. Tổng thiệt hại
ước tính do sự yếu kém của hạ tầng gây ra cho toàn chuỗi Ways Station
lên đến hơn 6.3 Tỷ VNĐ/năm.

## Tác động Vận hành

\- Sự cố gián đoạn hệ thống giờ cao điểm: Theo thống kê, trung bình mỗi
chi nhánh gặp 2-3 sự cố gián đoạn/tháng, đặc biệt thường rơi vào \"giờ
vàng\" cuối tuần khi lượng giao dịch tăng vọt làm quá tải Database cục
bộ. Khi hệ thống Máy tính tiền sập, nhân viên không thể tính tiền, không
thể nhận order F&B, khách hàng chờ đợi lâu và bỏ đi. Bài toán chi phí
Thời gian gián đoạn: Giả sử 1 giờ vàng của 1 chi nhánh mang lại
5.000.000 VNĐ. Với 34 chi nhánh, trung bình 2 giờ downtime/tháng. Tổng
thiệt hại trực tiếp: 34 x 5.000.000 x 2 giờ x 12 tháng = 4.080.000.000
VNĐ (Ước lượng bảo thủ thực tế thiệt hại trực tiếp khoảng 2.4 Tỷ
VNĐ/năm).

\- Lãng phí nguồn lực vận hành (Chi phí vận hành vô ích): Với 68 giờ
công/ngày tiêu tốn cho việc đếm tiền, đối soát giao dịch Momo/VietQR và
nhập báo cáo Excel. Bài toán chi phí Chi phí vận hành: 68 giờ x 30 ngày
= 2040 giờ/tháng. Tương đương với việc chuỗi phải thuê thêm 10 nhân viên
(ca 8 tiếng) chỉ để \"gõ số liệu\". Quy đổi chi phí lương, thưởng và bảo
hiểm (trung bình 8 triệu/người/tháng), sự lãng phí này lên tới khoảng 1
Tỷ VNĐ/năm trực tiếp, và 1.7 Tỷ VNĐ chi phí ẩn từ các sai số kế toán
không thể truy vết (tổng 2.7 Tỷ VNĐ/năm).

\- Tồn kho & Thất thoát chuỗi cung ứng: Độ trễ dữ liệu 24-48h khiến công
tác dự báo nhu cầu cho nguyên vật liệu F&B hoàn toàn bị tê liệt. Hội sở
không thể điều phối hàng hóa kịp thời, dẫn đến tình trạng chi nhánh A
thiếu hàng khách gọi, trong khi chi nhánh B lại dư thừa hàng hóa chờ hủy
do hết hạn. Tổn thất từ việc đứt gãy cung ứng và hao hụt này ước tính
khoảng 1.2 Tỷ VNĐ/năm.

## Tác động Tuân thủ & Bảo mật (Tác động Tuân thủ & Bảo mật theo Nghị định 13/2023/NĐ-CP)

\- Rủi ro vi phạm pháp luật cực kỳ nghiêm trọng: Hệ thống hiện tại đang
vi phạm trực tiếp các điều khoản cốt lõi của Nghị định 13/2023/NĐ-CP về
Bảo vệ dữ liệu cá nhân (chính thức có hiệu lực từ 01/07/2023). Cụ thể:

\- Vi phạm nguyên tắc xử lý dữ liệu (Điều 3): Dữ liệu sinh trắc học
(Face ID tại Gym) và hình ảnh Căn cước công dân (CCCD tại phòng Net)
đang được nhân viên chụp bằng điện thoại cá nhân và gửi qua ứng dụng
Zalo (chat nhóm). Hành vi này làm mất hoàn toàn khả năng kiểm soát luồng
dữ liệu, dữ liệu không được mã hóa đầu cuối và dễ dàng bị phát tán ra
bên ngoài.

\- Thiếu cơ chế đồng ý (Điều 11): Khách hàng hiện tại chưa có bất kỳ
giao diện nào (như App/Web form) để tick chọn \"Đồng ý\" cho phép Ways
Station thu thập và xử lý dữ liệu cá nhân. Mọi thao tác thu thập đang
diễn ra mang tính chất ép buộc (không có vân tay/khuôn mặt thì không
được vào tập).

\- Thiếu các biện pháp bảo vệ (Điều 26): Dữ liệu nhạy cảm trên máy Máy
tính tiền được lưu trữ dưới dạng văn bản rõ, không được áp dụng các tiêu
chuẩn mã hóa như AES-256. Không có hệ thống lưu vết để biết nhân viên
nào đã truy xuất hồ sơ của khách hàng nào.

\- Hậu quả chế tài:

\- Mức phạt hành chính cho hành vi làm lộ lọt dữ liệu cá nhân quy mô lớn
có thể lên tới 5% tổng doanh thu năm của toàn công ty (Theo quy định xử
phạt vi phạm hành chính). Đối với một chuỗi 34 chi nhánh, đây là một con
số khổng lồ có thể dẫn đến phá sản.

\- Ngoài phạt tiền, doanh nghiệp có thể bị đình chỉ hoạt động xử lý dữ
liệu, đồng nghĩa với việc toàn bộ hệ thống quản lý hội viên Gym và Net
bị buộc phải dừng hoạt động cho đến khi khắc phục xong.

\- Hậu quả về danh tiếng: Nếu xảy ra một đợt tấn công Mã độc tống tiền
mã hóa toàn bộ dữ liệu máy chủ và Hacker đe dọa tung ảnh CCCD của hàng
ngàn khách hàng lên mạng, làn sóng tẩy chay từ người tiêu dùng sẽ lập
tức phá hủy định vị thương hiệu mà Ways Station đã cất công xây dựng,
đặc biệt là tệp khách hàng Gen Z cực kỳ quan tâm đến quyền riêng tư số.

## Tác động Chiến lược

\- Mù dữ liệu: Ban lãnh đạo không thể triển khai các chiến dịch
Marketing cá nhân hóa vì không có hồ sơ khách hàng 360 độ. Khách hàng
VIP chơi bida hằng tuần lại không nhận được voucher nào khi đăng ký tập
Gym.

**Bảng Tổng hợp Rủi ro & Ma trận Biện pháp**

  ---------------------------------------------------------------------
  Hạng mục Rủi  Khả năng      Tác động      Ước tính      Biện pháp
  ro                                        Thiệt hại     Khắc phục Kỹ
                                                          thuật (Đề
                                                          xuất đầu tư)
  ------------- ------------- ------------- ------------- -------------
  Vi phạm dữ    Rất Cao       Cực kỳ Nghiêm Phạt tỷ trọng Triển khai
  liệu KH                     trọng         DT (\>10 Tỷ)  Quản lý định
  (NĐ13)                                                  danh tập
                                                          trung, mã hóa
                                                          AES-256 Data
                                                          At Rest,
                                                          Chống thất
                                                          thoát dữ
                                                          liệu, Zero
                                                          Trust Mạng.

  Lãng phí Chi  Chắc chắn     Cao           \~2.7 Tỷ      Xây dựng ETL
  phí vận hành                              VNĐ/Năm       Pipeline, tự
  (nhập thủ                                               động hóa
  công)                                                   luồng bán
                                                          hàng vào Kho
                                                          dữ liệu hội
                                                          tụ.

  Thời gian     Rất Cao       Cao           \~2.4 Tỷ      Ảo hóa ứng
  gián đoạn Máy                             VNĐ/Năm       dụng (K3s tại
  tính tiền tại                                           chi nhánh),
  chi nhánh                                               Kiến trúc
                                                          dịch vụ vi mô
                                                          trên Điện
                                                          toán đám mây
                                                          Kubernetes,
                                                          cơ chế Tự
                                                          động mở rộng
                                                          quy mô.

  Thất thoát    Cao           Trung bình    \~1.2 Tỷ      Real-time BI
  chuỗi cung                                VNĐ/Năm       Dashboard
  ứng F&B                                                 cung cấp cái
                                                          nhìn 360 độ
                                                          về tồn kho
                                                          toàn chuỗi.
  ---------------------------------------------------------------------

# Xác lập mục tiêu & KPI hạ tầng

Định hướng Mục tiêu tương lai của dự án là loại bỏ sự phụ thuộc vào con
người trong các tác vụ tích hợp, chuyển dịch toàn bộ lên tự động hóa.
Việc đo lường sự thành công của dự án hạ tầng không thể dựa vào cảm tính
mà phải được đánh giá qua các chỉ số đo lường hiệu năng cốt lõi nghiêm
ngặt.

**Bộ tiêu chuẩn Đo lường Năng lực** Hệ thống mục tiêu được xây dựng dựa
trên tiêu chuẩn Chỉ số đo lường hiệu suất để đảm bảo năng lực Vận hành
kết hợp với các Yêu cầu phi chức năng.

\- Tần suất triển khai: Chuyển từ việc triển khai phần mềm thủ công (mỗi
1-2 tháng/lần) sang triển khai tự động nhiều lần/ngày thông qua Đường
ống triển khai tự động.

\- Năng lực đáp ứng người dùng đồng thời: Hệ thống Cổng giao tiếp ứng
dụng tập trung phải xử lý mượt mà tối thiểu 10.000 Người dùng đồng thời
trong các khung giờ cao điểm, với độ trễ Thời gian phản hồi cam kết dưới
200ms ở phân vị thứ 95 (p95 latency \< 200ms).

**Bảng Cam kết Cam kết dịch vụ và Mục tiêu KPI:**

  --------------------------------------------------------------------------
  Nhóm Chỉ số KPI   Hiện trạng        Mục tiêu Cam kết  Căn cứ Đo lường &
                                                        Nghiệm thu
  ----------------- ----------------- ----------------- --------------------
  **1. Tính Sẵn     Không xác định    Đạt Uptime **≥    Báo cáo uptime từ
  sàng**            (Thời gian gián   99.99%** cho Core Điện toán đám mây
                    đoạn cao, tỷ lệ   Cổng giao tiếp    Provider liên tục
                    Điểm sự cố duy    ứng dụng tập      hàng tháng.
                    nhất = 100%)      trung và Dịch vụ  
                                      Quản lý định danh 
                                      lõi (Chỉ cho phép 
                                      downtime tối đa   
                                      52 phút/năm).     

  **2. Tốc độ Khôi  Từ 12 đến 24 giờ  Giảm xuống **\<   Log hệ thống K8s ghi
  phục**            (Phải cử IT       15 phút** (Hệ     nhận thời gian tự
                    On-site xử lý sự  thống tự động Tự  động restart Bộ chứa
                    cố máy chủ vật    động phục hồi qua bị lỗi.
                    lý)               Kubernetes kiểm   
                                      tra trạng thái).  

  **3. Khả năng     Từ 4 đến 8 giờ    Giảm xuống **\< 5 Hệ thống
  Giám sát**        (Chờ nhân viên    phút** (Hệ thống  Prometheus/Grafana
                    chi nhánh báo lỗi Monitoring cảnh   Hệ thống cảnh báo
                    Zalo)             báo tự động qua   ghi nhận thời điểm
                                      Đo lường & Phản   bắn alert.
                                      hồi về            
                                      Slack/Teams).     

  **4. Phục hồi Dữ  Backup thủ công   Đạt Điểm phục hồi Đánh giá qua Diễn
  liệu**            bằng tay ra USB,  **≤ 15 phút** và  tập Phục hồi thảm
                    Điểm phục hồi =   Thời gian phục    họa định kỳ mỗi 6
                    24 giờ, Thời gian hồi **≤ 4 giờ**   tháng.
                    phục hồi = 48 giờ (Tự động khôi     
                                      phục bản sao lưu) 
                                      cho các Database  
                                      trọng yếu.        

  **5. Độ trễ Dữ    Từ 24 đến 48 giờ  Độ trễ **\< 5     Quá trình đối soát
  liệu**            (Phụ thuộc vào    phút**. Dữ liệu   dấu thời gian giữa
                    tốc độ gõ Excel   doanh thu nhảy số giao dịch tại chi
                    của con người)    trực tiếp lên màn nhánh và dữ liệu
                                      hình BI           hiển thị trên Kho dữ
                                      Dashboard.        liệu hội tụ.

  **6. Tuân thủ Bảo 0% dữ liệu mã     Đạt **100%** dữ   Đánh giá qua bản Báo
  mật & Dữ liệu cá  hóa, log rời rạc, liệu nhạy cảm     cáo kiểm thử xâm
  nhân nhạy cảm**   truyền tải        được mã hóa (Khi  nhập và Kiểm toán
                    Plain-text qua    lưu trữ & Khi     bảo mật định kỳ.
                    Zalo              truyền tải bằng   
                                      AES-256/TLS 1.3); 
                                      Log hệ thống lưu  
                                      trữ tập trung bất 
                                      biến tối thiểu 1  
                                      năm.              

  **7. Tốc độ Triển 5 - 7 ngày cho    Giảm xuống **\< 4 Giai đoạn thực tế
  khai**            mỗi lần mở chi    giờ**/chi nhánh   khi mở rộng chi
                    nhánh mới         mới (Áp dụng hoàn nhánh thứ 35.
                                      toàn Hạ tầng dưới 
                                      dạng mã - Hạ tầng 
                                      dạng mã bằng      
                                      Terraform).       

  **8. Tỷ lệ Lỗi**  \> 30% cập nhật   Giảm xuống **\<   Số lượng Phiếu báo
                    phần mềm gây lỗi  5%** nhờ áp dụng  lỗi trên Jira liên
                    hệ thống cục bộ   Phát hành thử     quan đến hạ tầng sau
                                      nghiệm.           mỗi đợt Release.
  --------------------------------------------------------------------------

# Xây dựng phương án kiến trúc Mục tiêu tương lai (2--3 lựa chọn)

Để hiện thực hóa bộ DORA metrics và Cam kết dịch vụ khắt khe trên, đội
ngũ kiến trúc sư đề xuất 3 kịch bản kiến trúc nền tảng tích hợp. Mọi
kịch bản đều tuân thủ chặt chẽ nguyên tắc thiết kế 5 lớp chuẩn công
nghiệp, tập trung giải quyết bài toán: Không chỉ mua thiết bị, mà mua
\"Năng lực tính toán và tự động hóa\".

**Kịch bản 1: Tại chỗ (Trung tâm dữ liệu nội bộ) Nâng cấp Toàn diện
(Trung tâm dữ liệu Tập trung)**

\- Mô tả chi tiết giải pháp: Khắc phục triệt để các Whitebox Server yếu
kém, Ways Station sẽ thuê tủ Rack tại Trung tâm dữ liệu đạt chuẩn Tier 3
(như VNPT, FPT). Tự mua sắm toàn bộ cụm Máy chủ phiến vật lý cao cấp,
SAN Lưu trữ thuần SSD, Chuyển mạch lõi và Tường lửa thế hệ mới phần
cứng. Triển khai VMware vSphere (có bản quyền) để ảo hóa hạ tầng. Toàn
bộ Cổng giao tiếp ứng dụng tập trung và Kho dữ liệu chạy trên nền hạ
tầng vật lý này. Chi nhánh kết nối về Trung tâm dữ liệu qua kênh thuê
riêng trực tiếp.

\- Điểm mạnh: Quyền kiểm soát tài sản số ở mức tuyệt đối (100% Chủ quyền
dữ liệu), đáp ứng hoàn hảo mọi đợt Audit bảo mật khó tính nhất. Chi phí
vận hành dài hạn sẽ rất thấp và ổn định sau khoảng 3 năm khi thiết bị đã
được khấu hao xong tài sản. Độ trễ cực kỳ ổn định do sở hữu riêng đường
truyền và phần cứng tính toán.

\- Điểm yếu: Chi phí đầu tư ban đầu cực kỳ đắt đỏ, tiêu tốn hàng chục tỷ
đồng ngay lập tức, gây áp lực khủng khiếp lên dòng tiền của Startup. Khả
năng mở rộng mất rất nhiều thời gian do quy trình đặt hàng, thông quan
và lắp đặt phần cứng (Thời gian chờ từ 8-12 tuần). Đòi hỏi phải tuyển
dụng đội ngũ chuyên gia IT (Quản trị hệ thống, Mạng CCNA/CCNP, Quản trị
cơ sở dữ liệu) lương cao để trực và vận hành hệ thống phần cứng vật lý
24/7.

\- Kết luận đánh giá: Phương án này hoàn toàn không phù hợp với mô hình
kinh doanh thay đổi liên tục, mở mới chi nhánh liên tục và có tính biến
động lưu lượng thất thường theo khung giờ của Ways Station.

**Kịch bản 2: Hybrid Điện toán đám mây (Đám mây lai - Phân tán tải thông
minh) - \[PHƯƠNG ÁN KHUYẾN NGHỊ\]**

\- Mô tả chi tiết giải pháp: Kiến trúc này áp dụng triết lý \"Think
Global, Act Local\", là sự kết hợp hoàn hảo giữa On-premise và Public
Điện toán đám mây. Đây là kiến trúc tối ưu nhất, được nhiều chuỗi bán lẻ
quốc tế như Starbucks hay chuỗi F&B lớn áp dụng.

\- Lớp Edge (Tại 34+ chi nhánh): Cài đặt các bản phân phối Kubernetes
gọn nhẹ (K3s hoặc MicroK8s) trên phần cứng Server hiện có. Giữ lại các
ứng dụng nội bộ cốt lõi tại máy chủ cục bộ (Local Máy tính tiền Service,
Local Cache Redis/SQLite) theo cơ chế Kiến trúc ưu tiên ngoại tuyến.
Điều này đảm bảo chi nhánh vẫn có thể tính tiền, mở máy cho khách, in
bill ngay cả khi cáp quang Internet bị xe tải cắt đứt. Khi đường truyền
mạng khôi phục, hệ thống tự động đồng bộ gói dữ liệu lên Điện toán đám
mây.

\- Lớp Điện toán đám mây (Tại Public Điện toán đám mây Đám mây riêng):
Đẩy toàn bộ các năng lực tính toán nặng và hội tụ dữ liệu lên Điện toán
đám mây. Lớp trung gian bảo mật dùng Tường lửa ứng dụng web của Điện
toán đám mâyflare. Lớp ứng dụng dùng Cổng giao tiếp ứng dụng tập trung
và Quản lý định danh. Lớp dữ liệu trung chuyển sử dụng Bộ điều phối
luồng (Apache Kafka xử lý hàng triệu event/giây thông qua CDC Debezium)
truyền tải vào Enterprise Kho dữ liệu hội tụ (Amazon S3 + Snowflake /
AWS Redshift).

\- Cơ chế Sẵn sàng cao/DR & Mạng lõi: Hạ tầng mạng sử dụng giải pháp
SD-WAN (như Fortinet FortiGate / Cisco Meraki) thiết lập luồng IPsec VPN
mã hóa điểm-điểm từ Router chi nhánh đâm thẳng về Virtual Private Điện
toán đám mây trên AWS. Trái tim của hệ thống trên Điện toán đám mây là
cụm Dịch vụ bộ chứa chạy các Kiến trúc dịch vụ vi mô (Dịch vụ Hội viên,
Thanh toán, Báo cáo). Dữ liệu được Nhân bản (nhân bản tự động) đa vùng
để chống chịu thảm họa.

\- Điểm mạnh:

\- Tài chính: Chuyển dịch toàn bộ Chi phí đầu tư vốn mua sắm thiết bị
nặng nề thành Chi phí vận hành linh hoạt. Doanh nghiệp chỉ trả tiền cho
những tài nguyên tính toán thực sự xài.

\- Khả năng mở rộng: Tuyệt vời. Hệ thống tự động nhân bản các Máy chủ xử
lý vào khung giờ vàng (cuối tuần, lễ Tết) và tự động thu hẹp vào ban đêm
lúc đóng cửa để tối ưu hóa hóa đơn Điện toán đám mây.

\- Tính linh hoạt: Cổng giao tiếp ứng dụng tập trung tập trung giúp dễ
dàng Cắm và chạy với các nền tảng bên thứ ba (Ví điện tử MoMo, ZaloPay,
OpenAPI Ngân hàng, đối tác giao đồ ăn GrabFood) mà không cần code lại
các hệ thống cũ.

\- Điểm yếu: Độ phức tạp về mặt kiến trúc phần mềm cực cao. Đội ngũ IT
Sysadmin truyền thống hiện tại bắt buộc phải tái đào tạo để làm quen với
hệ sinh thái Điện toán đám mây-Native, DevOps và Hạ tầng dưới dạng mã.
Cần có chuyên gia Tối ưu chi phí đám mây để kiểm soát băng thông Băng
thông đầu ra (tải dữ liệu ra khỏi Điện toán đám mây) nhằm tránh rò rỉ
ngân sách. Chuyển đổi từ kiến trúc nguyên khối sang Kiến trúc dịch vụ vi
mô sẽ tốn thời gian.

\- Kết luận đánh giá: Đây là PHƯƠNG ÁN LỰA CHỌN TỐI ƯU NHẤT, cân bằng
hoàn hảo giữa tính bảo mật, khả năng Scale không giới hạn, đảm bảo hoạt
động liên tục tại chi nhánh kể cả khi rớt mạng, và tối ưu dòng tiền Chi
phí vận hành.

**Kịch bản 3: Điện toán đám mây-First (Thuần Điện toán đám mây & Phần
mềm dạng dịch vụ)**

\- Mô tả chi tiết giải pháp: Chiến lược Bê và đặt toàn bộ hệ thống hoặc
chuyển đổi hoàn toàn lên các dịch vụ Phần mềm dạng dịch vụ. Loại bỏ hoàn
toàn PC Server tại 34 chi nhánh. Thu ngân chỉ cần sử dụng máy tính bảng
hoặc màn hình mỏng có trình duyệt Web để truy cập trực tiếp vào hệ thống
Điện toán đám mây ERP/Máy tính tiền. Mọi thao tác tính tiền, xuất bill
đều được gọi lên Server Điện toán đám mây qua Internet để xử lý.

\- Điểm mạnh: Việc triển khai chi nhánh mới diễn ra siêu tốc, chỉ cần
cắm mạng và mở Tablet là bán hàng. Loại bỏ hoàn toàn sự cố phần cứng
Server hỏng tại chi nhánh, IT không bao giờ phải xuống hiện trường sửa
máy. Khả năng Scale vô hạn.

\- Điểm yếu: Sự phụ thuộc sinh tử vào đường truyền Internet. Chỉ cần nhà
mạng đứt cáp hoặc Router chi nhánh trục trặc, toàn bộ 34 chi nhánh sẽ tê
liệt hoàn toàn (không thể tính tiền, không thể mở máy Net, không thể tra
thông tin hội viên). Chi phí Chi phí vận hành khổng lồ khi dữ liệu phình
to và băng thông truy vấn 2 chiều liên tục. Bài toán tuân thủ cực kỳ đau
đầu khi phó mặc 100% dữ liệu nhạy cảm Dữ liệu cá nhân nhạy cảm ra ngoài
biên giới doanh nghiệp.

\- Kết luận đánh giá: Chứa đựng rủi ro quá lớn về tính liên tục của kinh
doanh đối với ngành bán lẻ offline. Phương án này nên được loại trừ đối
với mô hình Ways Station hiện tại, chỉ mang tính chất tham khảo học
thuật.

**Bảng So sánh & Đánh giá Tổng chi phí/Hiệu quả cơ bản**

**Lí do chọn kịch bản 2 dựa vào bối cảnh da.**

  -----------------------------------------------------------------------
  Tiêu chí Trọng    Kịch bản 1        Kịch bản 2        Kịch bản 3
  yếu                                                   
  ----------------- ----------------- ----------------- -----------------
  **Vốn đầu tư ban  Rất Cao           Thấp (Chỉ nâng    Rất Thấp
  đầu**                               cấp Router Edge)  

  **Chi phí vận     Trung Bình (Điện, Trung Bình (Linh  Rất Cao (Phí Phần
  hành**            Cooling, DC)      hoạt theo         mềm dạng dịch
                                      Traffic)          vụ/PaaS, Băng
                                                        thông đầu ra)

  **Tốc độ Triển    Chậm chạp (8-12   Vô hạn & Tức thời Vô hạn & Tức thời
  khai & Scale**    tuần Hardware)                      

  **Sự cố đứt cáp   Ổn định (Chi      **Ổn định**       Tê liệt hoàn toàn
  Internet**        nhánh độc lập)                      100%

  **Bảo mật & Tuân  Tốt nhất          **Rất Tốt** (Mã   Rủi ro rò rỉ rất
  thủ NĐ13**                          hóa VPN & Quản lý cao nếu Cấu hình
                                      định danh Truy    sai
                                      cập)              

  **Trình độ Nhân   SysAdmin truyền   Điện toán đám mây Không yêu cầu
  sự IT**           thống, CCNA       Architect, DevOps chuyên sâu
                                      Engineer          

  **Khả năng tích   Khó khăn (Mở port **Rất dễ dàng**   Rất dễ dàng
  hợp bên thứ 3**   Firewall thủ                        
                    công)                               

  **KHUYẾN NGHỊ CỦA Loại bỏ           **CHỌN PHƯƠNG ÁN  Loại bỏ
  NHÓM**                              NÀY**             
  -----------------------------------------------------------------------
