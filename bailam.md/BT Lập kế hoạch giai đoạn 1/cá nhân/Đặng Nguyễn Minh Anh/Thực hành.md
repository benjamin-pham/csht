# BÀI THỰC HÀNH — LẬP KẾ HOẠCH GIAI ĐOẠN 1

## Thuyết minh đề tài xây dựng hệ thống phần mềm ứng dụng công nghệ mới

| | |
|---|---|
| **Doanh nghiệp** | Chuỗi dịch vụ Ways Station — 34 chi nhánh tại TP.HCM |
| **Nội dung giai đoạn 1** | Bước 0 — Chuẩn bị đầu vào; Bước 1 — Tên đề tài và thông tin chung; Bước 2 — Bối cảnh và lý do chọn đề tài; Bước 3 — Mục tiêu, KPI và tiêu chí thành công; Bước 4 — Đối tượng, phạm vi, giả định và ràng buộc |

**Nguồn dữ liệu.** Thuyết minh sử dụng tài liệu nghiệp vụ nội bộ của 8 vị trí vận hành tại chi nhánh mà nhóm tiếp cận được, kết hợp nguồn công khai chính chủ của doanh nghiệp. Các chỉ số định lượng về hiệu suất vận hành là số liệu giả lập có kiểm soát, xây dựng trên cơ sở quan sát quy trình thực tế, do dữ liệu vận hành thực thuộc diện bảo mật. Nhóm không tiếp cận được tài liệu quy trình của khối văn phòng, nên mô tả hoạt động nội bộ của Phòng Nhân sự, Phòng Điều phối và Bộ phận kho hàng là suy luận từ phạm vi trách nhiệm được công bố trong tài liệu vị trí.

---

# BƯỚC 0 — CHUẨN BỊ ĐẦU VÀO

## 0.1. Bối cảnh doanh nghiệp

| Hạng mục | Nội dung |
|---|---|
| Ngành | Chuỗi tổ hợp dịch vụ giải trí, thể thao, không gian học tập và làm việc |
| Mô hình vận hành | Mỗi chi nhánh gộp nhiều mảng dịch vụ trong cùng một địa điểm |
| Quy mô | 34 chi nhánh tại TP.HCM, tăng từ 22 chi nhánh trong 24 tháng |
| Đặc thù pháp lý | Mỗi chi nhánh đăng ký là một hộ kinh doanh cá thể riêng biệt |
| Cơ cấu điều hành | Hội sở gồm Phòng Nhân sự, Phòng Điều phối và Bộ phận kho hàng; tuyến dưới là quản lý chi nhánh và nhân viên ca trực |
| Kênh giao tiếp chi nhánh với hội sở | Tổng đài một số duy nhất phân nhánh theo phím: phím 2 Phòng Nhân sự, phím 3 Phòng Điều phối, phím 8 Bộ phận kho hàng; kết hợp Zalo và email |

### Năm mảng dịch vụ và một dịch vụ hỗ trợ

| # | Mảng | Đặc điểm vận hành |
|---|---|---|
| 1 | NET | Phòng máy kết hợp bếp phục vụ tại chỗ và quầy hàng hoá; có nội quy phòng riêng; cho phép ghép ghế ngủ từ 21h đến 7h |
| 2 | BIDA | Ba loại bàn: bàn lỗ, bàn libre duy trì nhiệt độ 37–39 °C, bàn 3C duy trì 41–43 °C; tính giá theo khung giờ; bia và khăn lạnh chỉ có tại mảng này |
| 3 | CẦU LÔNG | Sân cho thuê; phục vụ trà đá theo định lượng chuẩn và 2 khăn lạnh mỗi bàn |
| 4 | GYM | Check-in bằng nhận diện khuôn mặt; hoạt động 24/7, không giới hạn thời gian tập; bán gói tập theo tháng |
| 5 | HUB | Không gian học tập và làm việc; bán vé theo block 4 tiếng, không bán lẻ, không hoàn tiền; có 13 loại đồ uống miễn phí và 7 loại thiết bị cho mượn; có dịch vụ in ấn |
| — | GIỮ XE | Dịch vụ hỗ trợ đi kèm mọi chi nhánh; dùng thẻ xe; có quy trình xử lý mất thẻ |

Bếp và quầy hàng hoá không phải mảng dịch vụ độc lập mà là dịch vụ bán kèm nằm trong NET và BIDA, dùng chung một bảng giá niêm yết.

## 0.2. Vấn đề hiện tại

| Điểm nghẽn | Mô tả |
|---|---|
| Xếp ca không có căn cứ nhu cầu | Phòng Điều phối phụ trách lịch làm việc và ca phát sinh cho toàn bộ 34 chi nhánh, nhưng đầu vào là các cuộc gọi rời rạc qua tổng đài, không phải dữ liệu dự báo |
| Ca phát sinh xử lý bị động | Tình huống ca sau chưa tới và ca làm phát sinh xuất hiện thường xuyên tới mức được đưa vào bảng hướng dẫn in cho mọi vị trí |
| Không biết trước khung giờ cao điểm | Chỉ xác định được đông hay vắng sau khi ca đã kết thúc |
| Cấp phát hàng hoá theo ước lượng | Có định mức nguyên vật liệu chuẩn nhưng không dự báo được tổng nhu cầu theo khung giờ |
| Dữ liệu lịch sử phân tán | 34 cơ sở dữ liệu độc lập, danh mục chưa chuẩn hoá |

## 0.3. Đối tượng sử dụng

| Nhóm người dùng | Vai trò với hệ thống | Mức độ số hoá hiện tại |
|---|---|---|
| Phòng Điều phối | Nhận dự báo nhu cầu nhân sự theo khung giờ cho toàn bộ 34 chi nhánh, làm căn cứ xếp lịch và bố trí ca phát sinh | Thấp, chủ yếu qua tổng đài |
| Bộ phận kho hàng | Nhận dự báo nhu cầu tiêu thụ hàng hoá và nguyên liệu để lập kế hoạch cấp phát | Thấp |
| Quản lý chi nhánh | Xem dự báo chi nhánh mình, đề xuất điều chỉnh ca, chuẩn bị nguồn lực trước khung giờ cao điểm | Thấp, dùng Excel và Zalo |
| Phòng Nhân sự | Sử dụng dự báo dài hạn để lập kế hoạch tuyển dụng theo mùa vụ | Trung bình, đã có hệ thống nhân sự nội bộ |
| Ban điều hành chuỗi | Đánh giá tỉ lệ lấp đầy theo khung giờ và theo mảng, làm căn cứ quyết định mở rộng | Trung bình |
| Quản trị viên hệ thống | Cấu hình, theo dõi chất lượng dự báo, kích hoạt huấn luyện lại mô hình | Cao |

## 0.4. Hệ thống liên quan

| Hệ thống | Vai trò trong đề tài | Dữ liệu cung cấp hoặc tiêu thụ |
|---|---|---|
| Phần mềm quản lý phòng máy | Nguồn dữ liệu chính | Thời điểm vào và ra, số máy đang sử dụng, doanh thu theo giờ |
| Phần mềm quản lý bida | Nguồn dữ liệu | Thời gian mở và đóng bàn theo loại bàn, giá theo khung giờ |
| Phần mềm đặt sân cầu lông | Nguồn dữ liệu | Lịch đặt sân, tỉ lệ lấp đầy, tỉ lệ huỷ |
| Phần mềm quản lý gym | Nguồn dữ liệu chất lượng cao | Bản ghi check-in và check-out bằng nhận diện khuôn mặt, có dấu thời gian tự động |
| Hệ thống vé HUB | Nguồn dữ liệu | Thời điểm bắt đầu và kết thúc block vé 4 tiếng |
| Máy chấm công vân tay | Nguồn dữ liệu đối chiếu | Số nhân sự thực tế có mặt theo ca, dùng để đối chiếu cung với cầu |
| Hệ thống quản lý nhân sự nội bộ | Hệ thống tiêu thụ kết quả | Nhận đề xuất số nhân sự cần cho từng ca |
| Cổng thanh toán ngân hàng | Nguồn dữ liệu đối chiếu | Giao dịch chuyển khoản |
| Nền tảng dữ liệu tập trung | Nguồn dữ liệu đã chuẩn hoá | Dữ liệu lịch sử toàn chuỗi |

Hai nguồn nhận diện khuôn mặt tại gym và chấm công vân tay cung cấp dấu thời gian chính xác, tự động, không phụ thuộc thao tác thủ công của nhân viên. Trong bài toán dự báo chuỗi thời gian, chất lượng dấu thời gian đầu vào quyết định chất lượng mô hình, nên đây là lợi thế dữ liệu sẵn có cần được ưu tiên khai thác.

## 0.5. Ràng buộc đầu vào

| Loại | Nội dung |
|---|---|
| Ngân sách | Theo hạn mức doanh nghiệp phê duyệt |
| Thời gian | 6 tháng từ khởi động tới bàn giao |
| Hạ tầng | Kế thừa hạ tầng hiện có, không đầu tư phần cứng mới tại chi nhánh |
| Dữ liệu | Chỉ sử dụng dữ liệu giao dịch và vận hành đã ẩn danh; không đưa dữ liệu sinh trắc vào mô hình, chỉ dùng dấu thời gian đã tách khỏi danh tính |
| Tuân thủ | Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân và các quy định hiện hành về an toàn thông tin |
| Nhân sự phía doanh nghiệp | Đầu mối nghiệp vụ từ Phòng Điều phối; đầu mối kỹ thuật cấp quyền truy cập dữ liệu |
| Ranh giới trách nhiệm | Hệ thống đưa ra dự báo và gợi ý; quyết định cuối cùng về xếp ca và cấp phát hàng thuộc về con người |

---

# BƯỚC 1 — TÊN ĐỀ TÀI VÀ THÔNG TIN CHUNG

## 1.1. Tên đề tài

**Xây dựng hệ thống dự báo lưu lượng khách theo khung giờ ứng dụng mô hình chuỗi thời gian, phục vụ điều phối nhân sự và cấp phát hàng hoá cho chuỗi dịch vụ Ways Station**

| Thành phần | Nội dung trong tên | Ý nghĩa |
|---|---|---|
| Động từ | Xây dựng | Xác định đây là dự án phát triển hệ thống |
| Đối tượng | Hệ thống dự báo lưu lượng khách theo khung giờ | Nêu chính xác thông tin đầu ra mà doanh nghiệp nhận được |
| Công nghệ ứng dụng | Mô hình chuỗi thời gian | Nêu nhánh kỹ thuật được khảo sát |
| Phạm vi phục vụ | Điều phối nhân sự và cấp phát hàng hoá | Khớp với chức năng của Phòng Điều phối và Bộ phận kho hàng |
| Bối cảnh | Chuỗi dịch vụ Ways Station | Neo đề tài vào doanh nghiệp cụ thể |

## 1.2. Thông tin chung

| Mục | Nội dung |
|---|---|
| Đơn vị chủ trì | |
| Đơn vị phối hợp | Chuỗi Ways Station — Phòng Điều phối và Bộ phận kho hàng |
| Chủ nhiệm đề tài | |
| Thành viên thực hiện | |
| Thời gian thực hiện | 6 tháng, chia 6 pha |
| Địa điểm triển khai | Thí điểm tại 3 chi nhánh có lưu lượng lớn nhất, ưu tiên chi nhánh có đủ năm mảng dịch vụ; sau đó mở rộng toàn chuỗi |
| Loại hình sản phẩm | Hệ thống phần mềm ứng dụng công nghệ mới |

---

# BƯỚC 2 — BỐI CẢNH VÀ LÝ DO CHỌN ĐỀ TÀI

## 2.1. Tóm tắt vấn đề

Ways Station vận hành 34 chi nhánh, mỗi chi nhánh gộp năm mảng dịch vụ có mẫu hình khách hoàn toàn khác nhau, và việc xếp lịch làm việc cho toàn bộ hệ thống này do Phòng Điều phối tại hội sở đảm nhiệm. Vấn đề là Phòng Điều phối không có bất kỳ dự báo nào về lượng khách sắp tới; đầu vào để xếp ca hiện chỉ là các cuộc gọi rời rạc từ chi nhánh qua tổng đài, nên tình huống ca sau chưa tới và ca làm phát sinh trở thành chuyện thường trực đủ để được in vào tài liệu hướng dẫn cho mọi vị trí. Hệ quả là chi nhánh vừa thừa người ở khung giờ vắng, vừa thiếu người ở khung giờ cao điểm, và chỉ xác định được mình bố trí sai sau khi ca đã kết thúc. Thông tin còn thiếu rất cụ thể: lượng khách dự kiến theo từng khung giờ, cho từng mảng dịch vụ, tại từng chi nhánh, trong bảy ngày tới. Nếu có được thông tin này với độ chính xác đủ tin cậy, cả việc xếp ca lẫn việc cấp phát hàng hoá đều chuyển từ phản ứng sang chủ động. Đề tài xây dựng hệ thống sinh ra chính thông tin đó, bằng nhánh kỹ thuật mô hình chuỗi thời gian, khai thác dữ liệu giao dịch lịch sử và dữ liệu check-in tự động sẵn có của toàn chuỗi.

## 2.2. Hiện trạng quy trình

### 2.2.1. Quy trình điều phối nhân sự

| Bước hiện tại | Công cụ | Vấn đề |
|---|---|---|
| Phòng Điều phối lập lịch làm việc cho 34 chi nhánh | Không có công cụ hoạch định chuyên dụng | Không có dự báo nhu cầu làm căn cứ |
| Chi nhánh báo ca phát sinh, nghỉ phép, ca sau chưa tới | Gọi tổng đài phím 3 | Xử lý bị động từng ca một, không sinh dữ liệu để phân tích |
| Chấm công vào ca và ra ca | Máy vân tay | Dữ liệu chất lượng tốt nhưng chỉ dùng để tính lương, chưa dùng để đối chiếu cung và cầu nhân sự |
| Đối chiếu ca thực tế với công | Thủ công cuối tháng | Phát hiện chênh lệch quá muộn để điều chỉnh |

### 2.2.2. Quy trình cấp phát hàng hoá và nguyên liệu

| Bước hiện tại | Công cụ | Vấn đề |
|---|---|---|
| Chi nhánh báo hết vật tư | Gọi tổng đài phím 8 | Phản ứng sau khi đã hết, không dự phòng trước |
| Chế biến theo định mức chuẩn | Tài liệu để nhân viên học thuộc | Có định mức chi tiết nhưng chưa số hoá nên không tổng hợp và dự báo được nhu cầu |
| Đặt hàng bổ sung | Theo lượng tiêu thụ kỳ trước | Không tính đến biến động lượng khách sắp tới |

### 2.2.3. Quy trình chuẩn bị nguồn lực tại chi nhánh

Số bàn bida mở, số máy net bật, số sân cầu lông chuẩn bị và số thiết bị làm mát vận hành đều theo mức mặc định, không co giãn theo nhu cầu thực tế. Tài liệu nghiệp vụ ghi rõ nguyên tắc điều chỉnh thủ công theo số lượng bàn và theo số lượng khách trong phòng. Doanh nghiệp đã có tư duy co giãn nguồn lực theo lượng khách, nhưng thực hiện bằng quan sát tại thời điểm phát sinh chứ không hoạch định trước.

## 2.3. Điểm đau và tác động định lượng

| Mã | Điểm đau | Chỉ số hiện trạng | Tác động |
|---|---|---|---|
| Đ1 | Thừa nhân sự ở khung giờ vắng | 18% giờ công rơi vào khung giờ có tỉ lệ lấp đầy dưới 30% | Chi phí nhân công lãng phí |
| Đ2 | Thiếu nhân sự ở khung giờ cao điểm | 12% lượt khách phải chờ trên 10 phút | Trải nghiệm kém, khách rời đi |
| Đ3 | Ca phát sinh xử lý bị động | Trung bình 46 cuộc gọi báo ca phát sinh mỗi tuần trên toàn chuỗi | Chi phí điều phối, áp lực lên nhân sự trực |
| Đ4 | Hết vật tư giữa ca | Trung bình 72 lần báo hết vật tư mỗi tháng trên toàn chuỗi | Gián đoạn phục vụ, mất doanh thu |
| Đ5 | Hao hụt nguyên liệu | 9% giá trị nguyên liệu tươi bị bỏ mỗi tháng | Chi phí trực tiếp |
| Đ6 | Không nắm được biến động trước | Chỉ biết sau khi ca kết thúc, độ trễ 24–48 giờ | Không phản ứng kịp thời |
| Đ7 | Chất lượng quyết định không đồng đều giữa 34 chi nhánh | Phụ thuộc kinh nghiệm từng quản lý | Không nhân rộng được cách làm hiệu quả |
| Đ8 | Năm mảng có mẫu hình lưu lượng khác nhau | Gym 24/7, HUB theo block 4 tiếng, bida theo khung giờ, net có phiên đêm ghép ghế ngủ | Một quy tắc kinh nghiệm không áp dụng chung được cho cả năm mảng |

Điểm đau Đ8 là đặc thù riêng của mô hình Ways Station. Trong cùng một chi nhánh, gym mở liên tục 24 giờ, HUB bán vé cố định 4 tiếng, bida tính giá theo khung giờ và net cho phép ghép ghế ngủ từ 21h tới 7h. Bốn mẫu hình lưu lượng khác nhau hoàn toàn, chồng lên nhau trong cùng một địa điểm và cùng một đội nhân sự. Bài toán này vượt quá khả năng ước lượng bằng kinh nghiệm cá nhân, và đó là lý do cần đến mô hình dự báo.

## 2.4. Nguyên nhân gốc

| Nguyên nhân gốc | Biểu hiện |
|---|---|
| Không có năng lực dự báo | Toàn bộ hoạch định vận hành là phản ứng sau sự việc |
| Kênh điều phối là kênh thoại, không sinh dữ liệu | Cuộc gọi tổng đài không tạo ra bản ghi để phân tích và học ra quy luật |
| Dữ liệu lịch sử phân tán ở 34 cơ sở dữ liệu độc lập | Không có tập dữ liệu đủ lớn và liền mạch để huấn luyện mô hình |
| Danh mục dịch vụ chưa chuẩn hoá giữa các chi nhánh | Không so sánh và tổng hợp được giữa các chi nhánh |
| Tri thức vận hành nằm trong kinh nghiệm cá nhân | Nhân sự nghỉ việc là tri thức mất theo |
| Năm mẫu hình lưu lượng chồng lên nhau | Vượt quá khả năng ước lượng bằng trực giác |

## 2.5. Giá trị của thông tin dự báo

| Bộ phận thụ hưởng | Quyết định được cải thiện | Lợi ích kỳ vọng |
|---|---|---|
| Phòng Điều phối | Xếp lịch làm việc theo nhu cầu dự báo thay vì theo cuộc gọi báo phát sinh | Giảm giờ công thừa (Đ1), giảm số ca phát sinh (Đ3) |
| Bộ phận kho hàng | Cấp phát hàng hoá và nguyên liệu theo nhu cầu dự kiến | Giảm số lần hết vật tư giữa ca (Đ4), giảm hao hụt (Đ5) |
| Quản lý chi nhánh | Chuẩn bị nhân sự và nguồn lực trước khung giờ cao điểm | Giảm tỉ lệ khách phải chờ (Đ2) |
| Phòng Nhân sự | Lập kế hoạch tuyển dụng theo mùa vụ | Giảm bị động khi bước vào giai đoạn cao điểm |
| Ban điều hành chuỗi | Đánh giá tiềm năng theo khung giờ và theo mảng dịch vụ | Quyết định mở rộng chi nhánh có căn cứ dữ liệu |
| Vận hành chi nhánh | Co giãn nguồn lực theo nhu cầu thực tế | Tiết kiệm chi phí vận hành |

Cùng một thông tin đầu ra là lượng khách dự kiến theo khung giờ phục vụ được sáu nhóm quyết định khác nhau, trong đó bốn nhóm là đơn vị có tên trong cơ cấu tổ chức của doanh nghiệp. Đây là căn cứ chứng minh đề tài đáng đầu tư thay vì chỉ giải quyết một quy trình đơn lẻ.

## 2.6. Tính cấp thiết

1. Quy mô tăng từ 22 lên 34 chi nhánh trong 24 tháng, sai số hoạch định nhân với 34 chi nhánh không còn là sai số nhỏ.
2. Mô hình tổ hợp năm mảng với năm mẫu hình lưu lượng khác nhau đã vượt quá khả năng ước lượng bằng kinh nghiệm.
3. Doanh nghiệp đã có sẵn hai nguồn dữ liệu chất lượng cao chưa được khai thác là check-in nhận diện khuôn mặt tại gym và chấm công vân tay.
4. Dữ liệu giao dịch lịch sử đã tích luỹ đủ dài để học ra quy luật mùa vụ theo giờ, theo ngày trong tuần và theo mùa.
5. Càng để lâu, dữ liệu càng tích luỹ ở dạng chưa chuẩn hoá, chi phí làm sạch về sau càng lớn.

---

# BƯỚC 3 — MỤC TIÊU, KPI VÀ TIÊU CHÍ THÀNH CÔNG

## 3.1. Mục tiêu tổng quát

Xây dựng và đưa vào vận hành hệ thống dự báo lưu lượng khách theo khung giờ và theo mảng dịch vụ cho chuỗi Ways Station, cung cấp cho Phòng Điều phối, Bộ phận kho hàng và quản lý chi nhánh một dự báo đủ chính xác và đủ ổn định để chuyển việc xếp ca và cấp phát hàng hoá từ phản ứng theo cuộc gọi sang hoạch định theo dữ liệu.

## 3.2. Mục tiêu cụ thể về kỹ thuật

| Mã | Mục tiêu |
|---|---|
| MT1 | Xây dựng mô hình dự báo lưu lượng khách theo khung giờ đạt độ chính xác vượt trội so với các phương pháp cơ sở |
| MT2 | Đảm bảo mô hình ổn định qua nhiều ngữ cảnh gồm nhiều chi nhánh, cả năm mảng dịch vụ và nhiều mốc thời gian khác nhau |
| MT3 | Xây dựng luồng dữ liệu tự động thu thập, làm sạch và chuẩn hoá dữ liệu giao dịch và check-in từ toàn chuỗi làm đầu vào cho mô hình |
| MT4 | Xây dựng giao diện và cơ chế phân phối kết quả dự báo tới đúng người dùng vào đúng thời điểm cần ra quyết định |

## 3.3. Mục tiêu cụ thể về hiệu quả nghiệp vụ

| Mã | Mục tiêu |
|---|---|
| MT5 | Giảm giờ công lãng phí do bố trí ca thừa vào khung giờ vắng |
| MT6 | Giảm tỉ lệ khách phải chờ quá lâu vào khung giờ cao điểm |
| MT7 | Giảm số lần phải xử lý ca phát sinh bị động qua tổng đài |
| MT8 | Giảm hao hụt nguyên liệu và giảm số lần hết vật tư giữa ca |

## 3.4. Bảng KPI về kỹ thuật

| Mã | Mục tiêu | Chỉ số | Hiện trạng | Cam kết | Thời điểm đo | Căn cứ nghiệm thu | Chịu trách nhiệm |
|---|---|---|---|---|---|---|---|
| KPI1.1 | MT1 | Sai số phần trăm tuyệt đối trung bình của dự báo lượng khách theo khung giờ, tầm nhìn 7 ngày | Phương pháp cơ sở theo mùa vụ đạt 28–35% | Tối đa 15% | Nghiệm thu pha thực nghiệm | Báo cáo thực nghiệm trên tập kiểm thử tách riêng theo trục thời gian | Trưởng nhóm kỹ thuật |
| KPI1.2 | MT1 | Mức cải thiện so với phương pháp cơ sở tốt nhất | Chưa có | Tối thiểu 15% | Nghiệm thu pha thực nghiệm | So sánh trực tiếp với tối thiểu 4 phương pháp cơ sở trên cùng tập dữ liệu | Trưởng nhóm kỹ thuật |
| KPI1.3 | MT1 | Sai số bình phương trung bình gốc | Theo phương pháp cơ sở | Giảm tối thiểu 15% | Nghiệm thu pha thực nghiệm | Báo cáo thực nghiệm | Trưởng nhóm kỹ thuật |
| KPI2.1 | MT2 | Biên độ dao động sai số giữa các ngữ cảnh thực nghiệm | Chưa có | Chênh lệch tối đa 10% giữa ngữ cảnh tốt nhất và tệ nhất | Nghiệm thu pha thực nghiệm | Thực nghiệm trên tối thiểu 4 phiên bản tập dữ liệu và 4 mốc thời gian khác nhau | Trưởng nhóm kỹ thuật |
| KPI2.2 | MT2 | Số mảng dịch vụ đạt ngưỡng sai số tối đa 15% | Chưa có | Tối thiểu 4 trên 5 mảng | Nghiệm thu pha thực nghiệm | Báo cáo thực nghiệm phân tách theo mảng | Trưởng nhóm kỹ thuật |
| KPI2.3 | MT2 | Mức suy giảm chất lượng sau 3 tháng không huấn luyện lại | Chưa có | Sai số tăng tối đa 5 điểm phần trăm | Sau vận hành 3 tháng | Theo dõi liên tục trên hệ thống giám sát mô hình | Trưởng nhóm kỹ thuật |
| KPI3.1 | MT3 | Tỉ lệ chạy luồng dữ liệu thành công | Chưa có luồng | Tối thiểu 99% mỗi tháng | Hàng tháng sau vận hành | Nhật ký điều phối luồng dữ liệu | Kỹ sư dữ liệu |
| KPI3.2 | MT3 | Tỉ lệ bản ghi lỗi hoặc thiếu sau bước làm sạch | Chưa đo được | Tối đa 1% | Hàng tháng sau vận hành | Báo cáo kiểm tra chất lượng dữ liệu tự động | Kỹ sư dữ liệu |
| KPI3.3 | MT3 | Số nguồn dữ liệu đã tích hợp | 0 | Tối thiểu 5 nguồn, đủ năm mảng dịch vụ | Sau vận hành 3 tháng | Biên bản tích hợp từng nguồn | Kỹ sư dữ liệu |
| KPI4.1 | MT4 | Thời gian sinh dự báo cho toàn bộ 34 chi nhánh và 5 mảng | Chưa có | Tối đa 30 phút mỗi lần chạy | Sau vận hành 1 tháng | Nhật ký tác vụ dự báo | Kỹ sư hệ thống |
| KPI4.2 | MT4 | Thời gian phản hồi khi người dùng mở màn hình dự báo | Chưa có | Dưới 3 giây | Sau vận hành 1 tháng | Báo cáo hiệu năng ứng dụng | Kỹ sư hệ thống |
| KPI4.3 | MT4 | Tỉ lệ quản lý chi nhánh sử dụng dự báo tối thiểu một lần mỗi tuần | 0% | Tối thiểu 80% | Sau vận hành 3 tháng | Nhật ký sử dụng hệ thống | Chủ nhiệm đề tài |
| KPI4.4 | MT4 | Tỉ lệ chu kỳ xếp lịch của Phòng Điều phối có tham chiếu dự báo | 0% | Tối thiểu 90% | Sau vận hành 4 tháng | Đối chiếu lịch ban hành với dự báo cùng kỳ | Phòng Điều phối |

## 3.5. Bảng KPI về hiệu quả nghiệp vụ

| Mã | Mục tiêu | Chỉ số | Hiện trạng | Cam kết | Thời điểm đo | Căn cứ nghiệm thu | Chịu trách nhiệm |
|---|---|---|---|---|---|---|---|
| KPI5.1 | MT5 | Tỉ lệ giờ công rơi vào khung giờ có tỉ lệ lấp đầy dưới 30% | 18% | Tối đa 12% | Sau vận hành 3 tháng và 6 tháng | Đối chiếu dữ liệu chấm công vân tay với dữ liệu lấp đầy thực tế | Phòng Điều phối |
| KPI6.1 | MT6 | Tỉ lệ lượt khách phải chờ trên 10 phút vào khung giờ cao điểm | 12% | Tối đa 8% | Sau vận hành 3 tháng và 6 tháng | Nhật ký thời điểm check-in và thời điểm được phục vụ | Quản lý chi nhánh |
| KPI7.1 | MT7 | Số cuộc gọi báo ca phát sinh qua tổng đài mỗi tuần | 46 cuộc | Giảm tối thiểu 30% | Sau vận hành 6 tháng | Thống kê cuộc gọi theo nhánh phím 3 | Phòng Điều phối |
| KPI8.1 | MT8 | Tỉ lệ hao hụt nguyên liệu tươi | 9% | Tối đa 6% | Hàng tháng từ tháng thứ 3 | Biên bản kiểm kê kho định kỳ | Bộ phận kho hàng |
| KPI8.2 | MT8 | Số lần báo hết vật tư giữa ca qua tổng đài mỗi tháng | 72 lần | Giảm tối thiểu 40% | Hàng tháng từ tháng thứ 3 | Thống kê cuộc gọi theo nhánh phím 8 | Bộ phận kho hàng |

## 3.6. Tiêu chí nghiệm thu tổng thể

Đề tài được đánh giá là thành công khi đồng thời thoả bốn điều kiện:

1. Đạt toàn bộ KPI về kỹ thuật tại thời điểm nghiệm thu.
2. Đạt tối thiểu 3 trên 5 KPI về hiệu quả nghiệp vụ sau 6 tháng vận hành.
3. Có biên bản nghiệm thu người dùng được ký bởi đại diện Phòng Điều phối, Bộ phận kho hàng và quản lý chi nhánh.
4. Bàn giao đầy đủ mã nguồn, tài liệu kiến trúc, tài liệu vận hành và tài liệu hướng dẫn huấn luyện lại mô hình.

## 3.7. Nhánh kỹ thuật dự kiến khảo sát

| Nhóm phương pháp | Vai trò trong đề tài | Ví dụ phương pháp thuộc nhóm |
|---|---|---|
| Phương pháp thống kê cổ điển | Làm phương pháp cơ sở để so sánh | Phương pháp cơ sở theo mùa vụ; họ mô hình tự hồi quy tích hợp trung bình trượt có yếu tố mùa vụ; mô hình phân rã xu hướng và mùa vụ |
| Học máy dạng bảng | Phương pháp cơ sở mạnh | Các mô hình cây tăng cường độ dốc kết hợp đặc trưng thời gian |
| Học sâu cho chuỗi thời gian | Nhóm ứng viên chính | Mạng hồi quy có cổng; kiến trúc dựa trên cơ chế chú ý cho chuỗi thời gian; kiến trúc chia mảnh chuỗi |
| Mô hình nền tảng cho chuỗi thời gian | Nhóm ứng viên chính, hướng công nghệ mới | Mô hình nền tảng huấn luyện trước cho dự báo chuỗi thời gian, sử dụng ở chế độ dự báo không cần huấn luyện lại hoặc tinh chỉnh nhẹ |

Đặc thù dữ liệu cần xử lý riêng trong quá trình mô hình hoá:

- Chuỗi có nhiều chu kỳ mùa vụ chồng nhau: theo giờ trong ngày, theo ngày trong tuần, theo mùa và theo ngày lễ.
- Năm mảng dịch vụ có mẫu hình khác nhau, cần cân nhắc mô hình đa chuỗi dùng chung tham số thay vì huấn luyện 34 nhân 5 mô hình rời rạc.
- HUB bán vé theo block cố định 4 tiếng nên lưu lượng bị lượng tử hoá, không liên tục như net hay bida.
- Gym hoạt động 24/7 nên chuỗi không có khoảng đóng cửa, khác biệt hoàn toàn với bốn mảng còn lại.
- Net cho phép ghép ghế ngủ từ 21h tới 7h nên có phiên siêu dài, cần xử lý riêng khi quy đổi thành lượng khách theo khung giờ.

## 3.8. Điều khoản dự phòng kỹ thuật

Nhóm cam kết đạt các KPI về chất lượng dự báo đã nêu tại mục 3.4. Phương pháp cụ thể được lựa chọn thông qua thực nghiệm so sánh trên cùng bộ dữ liệu và cùng bộ độ đo. Trong trường hợp kết quả thực nghiệm cho thấy nhóm kỹ thuật dự kiến ban đầu không đạt ngưỡng cam kết, nhóm được phép thay thế bằng phương pháp tương đương hoặc tốt hơn thuộc cùng lĩnh vực dự báo chuỗi thời gian, với điều kiện vẫn đáp ứng đầy đủ KPI đã cam kết và có báo cáo thực nghiệm chứng minh.

## 3.9. Ranh giới trách nhiệm

Hệ thống đưa ra dự báo và gợi ý, không tự động ra quyết định. Việc chốt lịch ca và chốt đơn cấp phát hàng hoá vẫn do con người quyết định.

---

# BƯỚC 4 — ĐỐI TƯỢNG, PHẠM VI, GIẢ ĐỊNH VÀ RÀNG BUỘC

## 4.1. Đối tượng áp dụng

| Nhóm | Quy mô ước tính | Quyền trên hệ thống | Tần suất sử dụng |
|---|---|---|---|
| Phòng Điều phối | 5 người | Xem dự báo nhu cầu nhân sự toàn chuỗi, xuất dữ liệu phục vụ xếp lịch | Hằng ngày |
| Bộ phận kho hàng | 6 người | Xem dự báo nhu cầu tiêu thụ hàng hoá theo chi nhánh và khung giờ | 2–3 lần mỗi tuần |
| Quản lý chi nhánh | 34 người | Xem dự báo chi nhánh mình, gửi phản hồi về độ chính xác | Hằng ngày |
| Phòng Nhân sự | 4 người | Xem xu hướng dài hạn phục vụ kế hoạch tuyển dụng | Hằng tháng |
| Ban điều hành chuỗi | 3–5 người | Xem tổng hợp toàn chuỗi và xu hướng dài hạn | Hằng tháng |
| Quản trị viên hệ thống | 1–2 người | Cấu hình, theo dõi chất lượng mô hình, kích hoạt huấn luyện lại | Liên tục |

## 4.2. Phạm vi thực hiện

### 4.2.1. Nhóm chức năng

| Nhóm chức năng | Nội dung |
|---|---|
| Thu thập dữ liệu | Kết nối tới các nguồn giao dịch và check-in, thu thập theo lịch, ghi nhật ký quá trình |
| Làm sạch và chuẩn hoá | Xử lý bản ghi thiếu, loại bản ghi bất thường, chuẩn hoá danh mục dịch vụ về danh mục dùng chung, gộp dữ liệu về đơn vị khung giờ; xử lý riêng phiên siêu dài của net ban đêm và block vé 4 tiếng của HUB |
| Kỹ thuật đặc trưng | Sinh đặc trưng thời gian gồm giờ, ngày trong tuần và ngày lễ; đặc trưng trễ; đặc trưng trung bình trượt; đặc trưng phân biệt mảng dịch vụ và chi nhánh; đặc trưng thời tiết nếu có nguồn |
| Huấn luyện và đánh giá mô hình | Huấn luyện, kiểm định chéo theo trục thời gian, so sánh với các phương pháp cơ sở, lưu vết phiên bản mô hình |
| Sinh dự báo | Dự báo lượng khách theo khung giờ, tầm nhìn 7 ngày, cho từng chi nhánh và từng mảng dịch vụ |
| Trình bày kết quả | Bảng điều khiển xem dự báo, biểu đồ theo khung giờ, xuất tệp, cảnh báo khi dự báo vượt ngưỡng |
| Gợi ý vận hành | Quy đổi dự báo thành gợi ý số nhân sự cần cho từng ca dựa trên định mức phục vụ; quy đổi thành gợi ý lượng hàng hoá cần chuẩn bị dựa trên định mức nguyên vật liệu sẵn có |
| Theo dõi chất lượng mô hình | So sánh dự báo với thực tế, cảnh báo khi sai số vượt ngưỡng, đề xuất huấn luyện lại |
| Phân quyền | Phân quyền theo vai trò tương ứng sáu nhóm người dùng tại mục 4.1 |

### 4.2.2. Phạm vi dữ liệu và triển khai

- Mảng dịch vụ: cả năm mảng gồm net, bida, cầu lông, gym và HUB.
- Chi nhánh: thí điểm tại 3 chi nhánh có lưu lượng lớn nhất, ưu tiên chi nhánh có đủ năm mảng; sau đó mở rộng toàn bộ 34 chi nhánh.
- Độ phân giải thời gian: theo khung giờ.
- Tầm nhìn dự báo: 7 ngày.
- Dữ liệu lịch sử tối thiểu: 18 tháng, đủ để nắm quy luật mùa vụ theo tuần và theo mùa.

## 4.3. Phạm vi không bao gồm

| Không bao gồm | Lý do |
|---|---|
| Tự động ra quyết định xếp ca hoặc cấp phát hàng hoá | Hệ thống chỉ đưa ra gợi ý, quyết định thuộc về con người |
| Xây dựng mới hệ thống quản lý nhân sự hoặc hệ thống quản lý kho | Doanh nghiệp đã có sẵn, đề tài chỉ tích hợp ở mức trao đổi dữ liệu |
| Giám sát thiết bị vật lý gồm nhiệt độ bàn bida, tình trạng thiết bị làm mát và thiết bị vệ sinh | Thuộc bài toán giám sát thiết bị, khác với bài toán dự báo |
| Nhận diện khách hàng cá nhân từ dữ liệu sinh trắc | Chỉ sử dụng dấu thời gian check-in đã tách khỏi danh tính |
| Dự báo doanh thu tài chính và dự báo lợi nhuận | Thuộc bài toán khác, cần dữ liệu kế toán |
| Dự báo hành vi cho từng khách hàng cá nhân | Liên quan tới dữ liệu cá nhân, cần cơ sở pháp lý riêng |
| Đầu tư phần cứng mới tại chi nhánh | Kế thừa hạ tầng hiện có |
| Chuẩn hoá dữ liệu lịch sử trước mốc 18 tháng | Chi phí làm sạch cao, giá trị biên thấp |
| Phát triển ứng dụng di động | Kỳ này chỉ xây dựng giao diện nền web đáp ứng đa thiết bị |

## 4.4. Giả định

| Mã | Giả định | Phương án xử lý nếu giả định không đúng |
|---|---|---|
| G1 | Dữ liệu giao dịch lịch sử tối thiểu 18 tháng truy xuất được từ các hệ thống hiện hữu | Rút ngắn tầm nhìn dự báo hoặc thu hẹp số chi nhánh thí điểm |
| G2 | Dữ liệu có dấu thời gian chính xác tới mức phút | Ưu tiên sử dụng nguồn nhận diện khuôn mặt tại gym và chấm công vân tay vì hai nguồn này có dấu thời gian tự động |
| G3 | Danh mục dịch vụ giữa các chi nhánh chuẩn hoá được về danh mục dùng chung | Xây dựng bảng ánh xạ thủ công cho từng chi nhánh |
| G4 | Doanh nghiệp cung cấp được định mức phục vụ theo từng mảng, tức số khách một nhân viên phục vụ được trong một giờ | Không quy đổi được dự báo thành gợi ý nhân sự; hệ thống chỉ dừng ở mức dự báo lượng khách |
| G5 | Định mức nguyên vật liệu sẵn có được số hoá | Không quy đổi được dự báo thành gợi ý cấp phát hàng hoá |
| G6 | Hạ tầng hiện có đủ để chạy tác vụ dự báo theo lịch | Thuê thêm tài nguyên tính toán, phát sinh chi phí vận hành |
| G7 | Có đầu mối nghiệp vụ từ Phòng Điều phối tham gia xuyên suốt dự án | Rủi ro hiểu sai nghiệp vụ dẫn tới phải làm lại |
| G8 | Truy xuất được thống kê cuộc gọi tổng đài theo nhánh phím 3 và phím 8 | Thay thế bằng chỉ số đo gián tiếp qua bảng chấm công và biên bản kiểm kê kho |
| G9 | Nền tảng dữ liệu tập trung sẵn sàng đúng tiến độ | Xây dựng luồng thu thập trực tiếp từ 3 chi nhánh thí điểm, không phụ thuộc nền tảng đó |

## 4.5. Ràng buộc thực hiện

| Loại | Nội dung |
|---|---|
| Thời gian | 6 tháng chia 6 pha; mốc nghiệm thu thực nghiệm mô hình vào cuối tháng thứ 3 |
| Ngân sách | Theo hạn mức doanh nghiệp phê duyệt |
| Hạ tầng | Kế thừa hạ tầng hiện có, không đầu tư phần cứng mới tại chi nhánh |
| Bảo mật và tuân thủ | Dữ liệu huấn luyện phải được ẩn danh; không đưa dữ liệu sinh trắc vào mô hình, chỉ sử dụng dấu thời gian đã tách khỏi danh tính; tuân thủ quy định hiện hành về bảo vệ dữ liệu cá nhân |
| Nhân sự | Nhóm sinh viên thực hiện; doanh nghiệp cử đầu mối nghiệp vụ và đầu mối kỹ thuật |
| Vận hành | Tác vụ dự báo chạy ngoài giờ cao điểm; do gym hoạt động 24/7 nên không có khung giờ đóng cửa chung cho mọi mảng, cần chọn cửa sổ chạy riêng theo từng mảng |
| Kỹ thuật | Ưu tiên công cụ và thư viện mã nguồn mở có giấy phép cho phép sử dụng thương mại |

---

# PHỤ LỤC — DANH MỤC TÀI LIỆU NGHIỆP VỤ ĐÃ SỬ DỤNG

| # | Tài liệu | Nội dung khai thác |
|---|---|---|
| 1 | Nghiệp vụ vị trí Giữ xe | Quy trình xử lý sự vụ tại chi nhánh; sổ giao ca; bàn giao biên bản giấy |
| 2 | Nghiệp vụ vị trí Thu ngân Gym | Quy trình tư vấn và đăng ký hội viên; check-in bằng nhận diện khuôn mặt; chính sách gói tập; mô hình hoạt động 24/7 |
| 3 | Nghiệp vụ vị trí Phục vụ Gym | Nội quy phòng tập; quy trình vệ sinh và hỗ trợ thiết bị |
| 4 | Nghiệp vụ vị trí Phục vụ Cầu lông | Định lượng pha chế đồ uống; định mức khăn lạnh theo bàn |
| 5 | Nghiệp vụ vị trí Phục vụ Bida | Phân biệt ba loại bàn; dải nhiệt độ mặt bàn; nguyên tắc tính giá theo khung giờ |
| 6 | Nghiệp vụ vị trí Phục vụ Net | Công thức chế biến; định mức nguyên liệu theo món; bảng giá hàng hoá |
| 7 | Nghiệp vụ vị trí Thu ngân Net và HUB | Quy định phòng HUB; chính sách vé 4 tiếng; danh mục hàng bán, hàng miễn phí và hàng cho mượn |
| 8 | Nghiệp vụ vị trí Thu ngân Net và Bida | Bảng giá; công thức tính giá món; nội quy phòng net và phòng bida; quy trình kiểm tra phòng |
| 9 | Bảng phân nhánh tổng đài hỗ trợ | Cơ cấu Phòng Nhân sự, Phòng Điều phối và Bộ phận kho hàng; hệ thống quản lý nhân sự nội bộ; phần mềm quản lý gym; cổng thanh toán ngân hàng |

Nguồn công khai chính chủ: website doanh nghiệp, trang dịch vụ không gian học tập và làm việc, thông tin chi nhánh, cổng tuyển dụng.
