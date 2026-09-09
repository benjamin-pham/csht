**ĐỀ XUẤT DỰ ÁN ĐẦU TƯ CƠ SỞ HẠ TẦNG CÔNG NGHỆ THÔNG TIN**

*Đơn vị khảo sát: Hệ thống Thể thao – Giải trí Ways Station
(waysstation.vn) — 38+ chi nhánh tại 12 quận, TP. Hồ Chí Minh*

*Lớp năng lực đề xuất đầu tư: (4) Nền tảng Ứng dụng & Tích hợp và (5)
Nền tảng Dữ liệu*

*Quy ước: \[n\] = dữ kiện có nguồn công khai kiểm chứng được (xem Danh
mục nguồn) · (giả định) = số do nhóm ước tính, có nêu cơ sở tính*

**Tóm tắt điều hành**

> • **Hiện trạng.** Ways Station có 7 hệ thống công nghệ đang hoạt động
> nhưng không có thành phần tích hợp nào. Lớp tích hợp duy nhất trong
> kiến trúc hiện tại là một nhân viên nhập liệu, không phải một hệ
> thống.
>
> • **Đo lường.** Bảy trên chín chỉ số hạ tầng tối thiểu không tồn tại ở
> dạng đo được. Mức trưởng thành số đạt 1,6/5. Báo cáo doanh thu toàn hệ
> thống có sau T+~30 ngày (giả định).
>
> • **Chi phí duy trì hiện trạng.** Khoảng ~500 triệu đồng mỗi năm chỉ
> để di chuyển số liệu giữa các hệ thống, tương đương ~306 giờ lao động
> thủ công mỗi tuần (giả định).
>
> • **Rủi ro cấp thiết.** Dữ liệu sinh trắc học của toàn bộ hội viên
> đang được xử lý mà chưa có khung quản trị theo Nghị định 13/2023/NĐ-CP
> \[23\]; hai rủi ro khác đã thực sự xảy ra.
>
> • **Đề xuất.** Chọn phương án Hybrid (PA2): giữ nguyên các nền tảng
> thuê ngoài đang chạy, bổ sung lớp tích hợp và kho dữ liệu hợp nhất
> trên cloud, triển khai 6 tháng theo 3 pha.

**1. KHẢO SÁT HIỆN TRẠNG HẠ TẦNG (AS-IS)**

**1.1. Phạm vi và phương pháp khảo sát**

Khảo sát được thực hiện gián tiếp, dựa trên ba nhóm nguồn công khai: tài
liệu do chính doanh nghiệp công bố trên website và các trang landing
page \[1\]\[2\]\[8\]\[9\]\[10\]\[11\]\[12\]\[13\], cơ sở dữ liệu đăng ký
kinh doanh và tra cứu mã số thuế \[3\]\[4\]\[5\], và các tin tuyển dụng
chính thức \[2\]\[6\]\[17\]\[18\]. Doanh nghiệp không có phòng công nghệ
thông tin nên không tồn tại tài liệu kiến trúc hay nhật ký sự cố để đối
chiếu; vì vậy mọi số liệu định lượng không có nguồn đều được ghi rõ là
giả định kèm cơ sở tính, và tổng hợp lại ở Phụ lục A để kiểm chứng khi
có điều kiện phỏng vấn trực tiếp.

**1.2. Đối chiếu bộ chỉ số hạ tầng tối thiểu với hiện trạng**

| **Chỉ số tối thiểu theo yêu cầu** | **Hiện trạng Ways Station** | **Đo được?** |
|----|----|----|
| SLA / uptime hiện tại | Không có SLA được công bố cho bất kỳ hệ thống nào | Không |
| Số sự cố trong 3–6 tháng | Không ghi nhận — không có hệ thống tiếp nhận sự cố | Không |
| MTTD — thời gian phát hiện sự cố | Không có hệ thống giám sát | Không |
| MTTR — thời gian khắc phục | Không có quy trình quản lý dịch vụ | Không |
| Tỉ lệ sao lưu thành công | Dữ liệu nằm trên hệ thống nhà cung cấp, không có báo cáo sao lưu | Không |
| RPO / RTO hiện tại | Chưa từng được định nghĩa | Không |
| Tỉ lệ thiết bị hết hỗ trợ | Thuộc lớp (1), ngoài phạm vi đồ án | Ngoài phạm vi |
| Số lỗ hổng nghiêm trọng chưa vá | Không có quy trình đánh giá lỗ hổng | Không |
| Tăng trưởng người dùng / dữ liệu 12–24 tháng | Suy ra được từ tốc độ mở chi nhánh \[3\]\[4\] | **Có** |

*Bảng 1.1. Bảy trên chín chỉ số hạ tầng tối thiểu không tồn tại ở dạng
đo được*

**Đây là phát hiện quan trọng nhất của bước khảo sát.** Việc phần lớn
chỉ số không đo được không phải là thiếu sót của quá trình khảo sát, mà
chính là hiện trạng cần báo cáo: doanh nghiệp đang vận hành 38+ chi
nhánh hoạt động 24 giờ mà không có bất kỳ công cụ nào cho biết hệ thống
của mình đang chạy tốt hay không. Không thể quản trị cái không đo được,
và cũng không thể đặt mục tiêu cải thiện khi chưa có điểm khởi đầu. Vì
vậy hạng mục đầu tư đầu tiên của mọi phương án ở §4 đều phải bao gồm
năng lực giám sát và ghi nhật ký.

**1.3. Bộ chỉ số thay thế dựng được từ dữ liệu hiện có**

| **\#** | **Chỉ số** | **Giá trị hiện tại** | **Cách xác định** |
|----|----|----|----|
| P1 | Độ trễ có báo cáo doanh thu toàn hệ thống | T+~30 ngày | Giả định, suy từ chu kỳ lên sổ của kế toán từng hộ kinh doanh |
| P2 | Giờ lao động thủ công mỗi tuần để hợp nhất số liệu | ~306 giờ | Giả định: 38 chi nhánh × 3 ca × 20 phút × 7 ngày = 266 giờ, cộng ~40 giờ của nhân viên nhập liệu |
| P3 | Số hệ thống rời rạc không có lớp tích hợp | 7 | Đếm trực tiếp từ khảo sát \[8\]\[9\]\[10\]\[11\]\[13\]\[14\]\[16\] |
| P4 | Số hồ sơ tồn tại cho một khách hàng dùng nhiều dịch vụ | 3 | Suy luận từ kiến trúc: app gym, hệ thống đặt sân, quầy thu ngân |
| P5 | Số con số quy mô mâu thuẫn do chính doanh nghiệp công bố | 4 | 38+ \[2\] / 32+ \[8\] / 30 \[10\] / 22–25 \[17\] |
| P6 | Tốc độ tăng điểm kinh doanh | 1 → 38+ trong ~4 năm | Từ ngày cấp mã số thuế hộ kinh doanh đầu tiên 24/08/2022 \[3\]\[4\] |
| P7 | Tỉ lệ giao dịch đặt sân phải xử lý tay | ~3% | Giả định, dựa trên việc doanh nghiệp phải đăng cảnh báo ghi đúng mã đơn hàng \[11\] |
| P8 | Mức trưởng thành số bình quân | 1,6/5 | Tổng hợp 5 chiều đánh giá ở khảo sát Bước 0 |

*Bảng 1.2. Tám chỉ số thay thế, dùng làm baseline cho bảng KPI ở §3*

**1.4. Hiện trạng lớp (4) Nền tảng Ứng dụng và Tích hợp**

Ways Station đã đầu tư một lượng công nghệ không nhỏ so với quy mô: ứng
dụng di động cho hội viên \[13\]\[14\], hệ thống đặt sân trực tuyến có
thanh toán trước bằng mã QR \[11\]\[12\], nhận diện khuôn mặt kiểm soát
ra vào 24 giờ \[8\], phần mềm quầy tính giờ cho gaming và billiards
\[9\]\[10\]. Vấn đề không nằm ở việc thiếu công nghệ.

Vấn đề là **không tồn tại bất kỳ thành phần trung gian nào** cho phép
các hệ thống đó trao đổi dữ liệu. Không có cổng giao diện lập trình làm
điểm vào chung, không có cơ chế xác thực tập trung để một khách hàng chỉ
cần một danh tính, không có dịch vụ dùng chung nào. Biểu hiện rõ nhất:
năng lực thanh toán trực tuyến đã được xây dựng cho hệ thống đặt sân từ
năm 2024 \[11\], nhưng ứng dụng quản lý gói tập ra mắt sau đó vẫn chưa
thanh toán trực tuyến được \[13\]. Một năng lực đã tồn tại trong doanh
nghiệp mà hệ thống khác không dùng lại được — đó là định nghĩa của việc
thiếu lớp tích hợp.

<img src="media/image1.png" style="width:6.14173in;height:1.84252in" />

*Hình 1.1. Sơ đồ hiện trạng: thành phần đóng vai trò lớp tích hợp là một
con người, không phải một hệ thống*

Hai ràng buộc phái sinh cần ghi nhận ngay, vì chúng loại bỏ một số
phương án ở §4. Thứ nhất, doanh nghiệp không có phòng công nghệ thông
tin: trong toàn bộ tin tuyển dụng khảo sát được không xuất hiện vị trí
lập trình viên, quản trị hệ thống hay quản trị cơ sở dữ liệu nào
\[2\]\[17\]\[18\]. Tiêu chí chọn giải pháp vì vậy buộc phải là “tích hợp
được”, không thể là “tự phát triển”. Thứ hai, hồ sơ hội viên và dữ liệu
sinh trắc học nằm trên nền tảng của nhà cung cấp bên thứ ba
\[14\]\[15\]; nếu nhà cung cấp không mở giao diện lập trình thì mọi
thiết kế tích hợp đều phải đổi cách tiếp cận.

**1.5. Hiện trạng lớp (5) Nền tảng Dữ liệu**

Đây là lớp mà Ways Station gần như chưa xây dựng. Không có kho dữ liệu
tập trung; khâu trích xuất và hợp nhất dữ liệu do con người thực hiện
thủ công \[18\]; và không tồn tại dữ liệu chủ cho hai thực thể quan
trọng nhất là chi nhánh và khách hàng. Bằng chứng cho việc thiếu dữ liệu
chủ về chi nhánh rất trực tiếp: chính doanh nghiệp công bố bốn con số
khác nhau về quy mô của mình trên bốn trang thông tin khác nhau
\[2\]\[8\]\[10\]\[17\].

Sự phân mảnh diễn ra ở ba tầng với độ khó xử lý tăng dần. Tầng kỹ thuật
— bốn ứng dụng không nói chuyện được với nhau — là tầng dễ xử lý nhất và
thuộc phạm vi lớp (4). Tầng pháp nhân — mỗi chi nhánh hoặc cụm chi nhánh
là một hộ kinh doanh độc lập có mã số thuế và sổ sách riêng
\[3\]\[4\]\[5\] — đòi hỏi giải quyết cả về pháp lý lẫn kỹ thuật. Tầng
kênh tiếp xúc khách hàng — các trang mạng xã hội phát triển tự phát theo
từng chi nhánh \[16\] — thuộc về quy hoạch kênh nhiều hơn là công nghệ.

Hệ quả là doanh nghiệp không trả lời được những câu hỏi vốn rất cơ bản
đối với một chuỗi dịch vụ: bao nhiêu phần trăm hội viên phòng tập cũng
dùng dịch vụ cầu lông; hội viên nào sắp hết hạn gói tập mà tháng này
không đến tập lần nào; đợt phát hành mã ưu đãi vừa rồi mang về bao nhiêu
khách mới; chi nhánh nào thực sự có lãi tính theo ngày. Ngoài ra, hai
nghĩa vụ dữ liệu đang tồn đọng: dữ liệu sinh trắc học được xử lý mà chưa
có khung quản trị theo Nghị định 13/2023/NĐ-CP \[23\]\[24\], và toàn bộ
dữ liệu địa chỉ của 38+ chi nhánh cần chuẩn hóa lại sau đợt sắp xếp đơn
vị hành chính \[3\]\[7\].

**1.6. Ba lớp năng lực còn lại**

| **Lớp** | **Ghi nhận sơ bộ** | **Phạm vi** |
|----|----|----|
| \(1\) Tính toán và kết nối | Không có máy chủ nội bộ; các hệ thống đều do nhà cung cấp vận hành. Mạng tại chi nhánh phục vụ camera và phần mềm quầy. | Thành viên khác phụ trách |
| \(2\) Nền tảng vận hành | Không có giám sát, không ITSM, không CMDB, không quy trình sao lưu được công bố. | Thành viên khác phụ trách |
| \(3\) Bảo mật và định danh | Không có xác thực tập trung cho nhân viên; nhận diện khuôn mặt dùng cho khách, không dùng cho quản trị. | Thành viên khác phụ trách |

*Bảng 1.3. Ba lớp còn lại — nêu để đủ khung 5 lớp; nội dung chi tiết do
thành viên khác trong nhóm phụ trách*

**1.7. Điểm nghẽn có định lượng**

| **\#** | **Điểm nghẽn** | **Tác động định lượng** |
|----|----|----|
| B1 | Hợp nhất doanh thu toàn hệ thống làm bằng sức người | ~306 giờ/tuần; báo cáo trễ T+~30 ngày (giả định) |
| B2 | Hội viên không gia hạn gói tập trực tuyến được \[8\]\[13\] | Phòng tập mở 24 giờ nhưng chỉ gia hạn được trong khung 6–24 giờ tại quầy |
| B3 | Đối soát thanh toán phụ thuộc thao tác của khách \[11\] | ~3% giao dịch phải xử lý tay qua đường dây nóng (giả định) |
| B4 | Hai trải nghiệm thanh toán mâu thuẫn trong cùng một cơ sở \[8\]\[11\] | Cầu lông trả trước 100% trực tuyến, gaming và billiards thu tại quầy |
| B5 | Năng lực kỹ thuật không chia sẻ được giữa các ứng dụng | Thanh toán trực tuyến có từ 2024 ở đặt sân \[11\] nhưng app gym vẫn chưa có \[13\] |
| B6 | Nhượng suất chơi diễn ra ngoài hệ thống \[12\] | Doanh nghiệp không biết ai thực sự đang dùng sân |

*Bảng 1.4. Sáu điểm nghẽn, sắp theo mức nghiêm trọng*

**2. VẤN ĐỀ VÀ RỦI RO NẾU KHÔNG ĐẦU TƯ (WHY NOW?)**

**2.1. Ba cụm tác động**

> • **Tác động vận hành.** Ban điều hành ra quyết định mở hay đóng chi
> nhánh, điều chỉnh giá, phân bổ ngân sách tiếp thị trên số liệu trễ
> khoảng một tháng. Mỗi tuần có ~306 giờ lao động được chi ra chỉ để di
> chuyển số liệu, không tạo thêm giá trị nào. Giao dịch treo do sai nội
> dung chuyển khoản phải xử lý qua đường dây nóng.
>
> • **Tác động tuân thủ và an ninh.** Dữ liệu sinh trắc học của toàn bộ
> hội viên thuộc nhóm dữ liệu cá nhân nhạy cảm theo Nghị định
> 13/2023/NĐ-CP \[23\], kéo theo nghĩa vụ về lấy sự đồng ý, thông báo xử
> lý, đánh giá tác động và thời hạn lưu trữ; Luật Bảo vệ dữ liệu cá nhân
> bổ sung quyền yêu cầu xóa dữ liệu của chủ thể \[24\]. Ngay cả khi dữ
> liệu nằm trên hệ thống nhà cung cấp, Ways Station vẫn giữ vai trò Bên
> Kiểm soát dữ liệu và không chuyển giao được trách nhiệm pháp lý. Song
> song, việc doanh nghiệp phải đăng bài xác nhận danh sách trang chính
> thức \[16\] cho thấy mạo danh thương hiệu đã xảy ra, trong bối cảnh
> khách được hướng dẫn chuyển khoản để thanh toán.
>
> • **Tác động chiến lược.** Chi phí vận hành thủ công tăng tuyến tính
> theo số chi nhánh, nên mô hình hiện tại không mở rộng được: mỗi chi
> nhánh mới cộng thêm khoảng 3 ca × 20 phút mỗi ngày vào khối lượng cộng
> tay. Doanh nghiệp cũng không đo được hiệu quả tiếp thị vì mã ưu đãi
> không gắn được với hồ sơ khách hàng, và không bán chéo được giữa sáu
> dòng dịch vụ vì không nhận ra khách hàng là cùng một người.

**2.2. Bảng rủi ro**

| **Rủi ro** | **Khả năng** | **Ảnh hưởng** | **Chi phí ước tính nếu xảy ra** | **Biện pháp** |
|----|----|----|----|----|
| R1. Vi phạm nghĩa vụ về dữ liệu cá nhân nhạy cảm (sinh trắc học) \[23\]\[24\] | Trung bình | **Rất cao** | Xử phạt hành chính, buộc dừng xử lý dữ liệu, tổn hại uy tín | N5: danh mục dữ liệu cá nhân, hồ sơ tuân thủ, công bố thời hạn lưu trữ |
| R2. Nhà cung cấp app gym không mở giao diện trích xuất dữ liệu \[14\]\[15\] | **Cao** | Cao | Phải làm lại thiết kế tích hợp; mất khả năng hợp nhất hồ sơ hội viên | Đàm phán điều khoản truy xuất dữ liệu ngay khi app còn giai đoạn thử nghiệm |
| R3. Tri thức hợp nhất dữ liệu tập trung vào một cá nhân \[18\] | Trung bình | Cao | Gián đoạn toàn bộ dòng báo cáo cho tới khi có người thay thế | N4: chuyển quy trình từ con người sang kho dữ liệu tự động |
| R4. Mạo danh thương hiệu dẫn tới khách chuyển tiền sai địa chỉ \[16\] | **Đã xảy ra** | Cao | Khách mất tiền, doanh nghiệp mất uy tín và phải xử lý khiếu nại | N1 + N3: một điểm vào duy nhất và mã đơn hàng do hệ thống sinh |
| R5. Quyết định kinh doanh sai do số liệu trễ ~30 ngày | **Cao** | Cao | Có thể vượt toàn bộ chi phí nhập liệu nếu quyết định sai về một chi nhánh | N4: báo cáo hợp nhất T+1 ngày |
| R6. Dữ liệu địa chỉ lạc hậu sau sắp xếp đơn vị hành chính \[3\]\[7\] | **Đã xảy ra** | Trung bình | Sai địa chỉ trên hóa đơn và mọi kênh công bố của 38+ chi nhánh | N6: chuẩn hóa và lập dữ liệu chủ về chi nhánh |
| R7. Rào cản pháp lý khi hợp nhất dữ liệu giữa các hộ kinh doanh \[3\]\[4\] | Trung bình | Cao | Phải thiết kế lại kiến trúc dữ liệu sau khi đã triển khai | Xác lập căn cứ pháp lý chia sẻ dữ liệu trước khi thiết kế kỹ thuật |
| R8. Chi phí vận hành thủ công tăng tuyến tính theo số chi nhánh | **Chắc chắn** | Cao | ~500 triệu đồng/năm hiện tại, tăng theo mỗi chi nhánh mới (giả định) | N4: cắt bỏ khâu cộng tay khỏi quy trình |

*Bảng 2.1. Rủi ro – khả năng – ảnh hưởng – chi phí ước tính – biện pháp*

**2.3. Chi phí của việc không làm gì, và vì sao là bây giờ**

Chi phí duy trì hiện trạng hiện ở mức khoảng ~500 triệu đồng mỗi năm
(giả định: ~96 triệu lương nhân viên nhập liệu, cộng ~410 triệu quy đổi
thời gian trưởng ca theo đơn giá lao động 30.000 đồng/giờ). Điều đáng
nói không phải con số tuyệt đối, mà bản chất của khoản chi: đây là tiền
chi ra chỉ để di chuyển số liệu từ nơi này sang nơi khác. Vì khoản này
tỉ lệ với số chi nhánh, và doanh nghiệp đã đi từ 1 lên 38+ điểm trong
khoảng bốn năm \[3\]\[4\], chi phí sẽ tiếp tục tăng theo đúng tốc độ mở
rộng.

> • Sức ép pháp lý đã hiện hữu, không phải dự báo: hệ thống nhận diện
> khuôn mặt đang chạy hằng ngày trên toàn bộ hội viên \[8\].
>
> • Quy mô vừa vượt ngưỡng xử lý thủ công: ở 5 chi nhánh thì cộng tay
> còn khả thi, ở 38+ chi nhánh với 3 ca mỗi ngày thì không.
>
> • Đợt sắp xếp đơn vị hành chính buộc phải rà soát lại toàn bộ dữ liệu
> địa chỉ \[3\]\[7\] — công việc này phải làm dù có đầu tư hay không,
> nên làm cùng lúc với việc lập dữ liệu chủ sẽ tiết kiệm hơn.
>
> • Ứng dụng gym còn ở giai đoạn thử nghiệm \[13\], nên vị thế đàm phán
> điều khoản truy xuất dữ liệu với nhà cung cấp còn thuận lợi. Càng để
> lâu, dữ liệu tích lũy trong hệ thống của họ càng nhiều và chi phí
> chuyển đổi càng cao.

**3. MỤC TIÊU VÀ KPI HẠ TẦNG TO-BE**

**3.1. Mục tiêu tổng quát**

Xây dựng năng lực hạ tầng ở lớp (4) và lớp (5) để Ways Station có được
một bức tranh vận hành hợp nhất theo ngày trên toàn bộ chi nhánh, dịch
vụ và pháp nhân, thay cho quy trình cộng tay hiện tại. Đồng thời đưa
việc xử lý dữ liệu cá nhân — đặc biệt là dữ liệu sinh trắc học — vào một
khung quản trị có căn cứ pháp lý và thời hạn lưu trữ rõ ràng, để năng
lực mở rộng chuỗi không bị chặn bởi rủi ro tuân thủ.

**3.2. Bảng chỉ tiêu**

| **\#** | **Chỉ tiêu** | **Baseline hiện tại** | **Mục tiêu** | **Thời điểm đo** | **Người chịu trách nhiệm số liệu** |
|----|----|----|----|----|----|
| K1 | Độ trễ có báo cáo doanh thu toàn hệ thống | T+~30 ngày (giả định) | **T+1 ngày** | T+3 tháng | Trưởng khối Vận hành chuỗi |
| K2 | Giờ lao động thủ công hợp nhất số liệu mỗi tuần | ~306 giờ (giả định) | **\< 20 giờ** | T+3 tháng | Trưởng khối Vận hành chuỗi |
| K3 | Tỉ lệ giao dịch phải đối soát tay | ~3% (giả định) | **\< 1%** | T+3 tháng | Kế toán trưởng |
| K4 | Tỉ lệ hội viên có hồ sơ hợp nhất một danh tính | 0% | **\> 90%** | T+6 tháng | Trưởng bộ phận Khách hàng |
| K5 | Số nguồn dữ liệu chủ về danh sách chi nhánh | 4 nguồn mâu thuẫn \[2\]\[8\]\[10\]\[17\] | **1 nguồn duy nhất** | T+1 tháng | Đầu mối CNTT |
| K6 | Uptime nền tảng tích hợp | Không đo được | **≥ 99,5%** | T+1 / 3 / 6 tháng | Đối tác vận hành |
| K7 | RPO / RTO cho dữ liệu vận hành | Chưa định nghĩa | **≤ 4 giờ / ≤ 8 giờ** | T+3 tháng, qua diễn tập khôi phục | Đối tác vận hành |
| K8 | Tỉ lệ dữ liệu sinh trắc học có căn cứ pháp lý và thời hạn lưu trữ được công bố | 0% | **100%** | T+6 tháng | Ban điều hành |
| K9 | MTTD sự cố tích hợp | Không đo được | **≤ 15 phút** | T+3 tháng | Đối tác vận hành |
| K10 | Tỉ lệ giao diện lập trình đi qua xác thực tập trung | 0% | **100%** | T+6 tháng | Đầu mối CNTT |

*Bảng 3.1. Mười chỉ tiêu, mỗi chỉ tiêu có baseline, mục tiêu, thời điểm
đo và người chịu trách nhiệm số liệu*

**3.3. Cách nghiệm thu từng chỉ tiêu**

K1, K2 và K3 nghiệm thu bằng cách đối chiếu trực tiếp: so ngày phát hành
báo cáo với ngày phát sinh doanh thu, đếm số giờ ghi nhận trên bảng phân
công, và trích số giao dịch phải xử lý tay từ nhật ký hệ thống. K4 và
K10 nghiệm thu bằng truy vấn trên kho dữ liệu. K5 nghiệm thu bằng cách
rà soát toàn bộ kênh công bố và xác nhận mọi nơi đều lấy từ một nguồn.
K6 và K9 nghiệm thu bằng báo cáo từ hệ thống giám sát sau ba tháng vận
hành liên tục. K7 bắt buộc nghiệm thu bằng một buổi diễn tập khôi phục
có biên bản, không chấp nhận cam kết trên giấy. K8 nghiệm thu bằng hồ sơ
tuân thủ: văn bản lấy sự đồng ý, thông báo xử lý dữ liệu, và chính sách
thời hạn lưu trữ đã được công bố cho hội viên.

**4. PHƯƠNG ÁN KIẾN TRÚC TO-BE VÀ SO SÁNH**

Ba phương án dưới đây được xây dựng để ban điều hành có lựa chọn thực
sự, không bị đóng khung vào một hướng. Mỗi phương án được mô tả theo bốn
điểm: kiến trúc theo năm lớp, điểm sẵn sàng và khôi phục, cách tích hợp,
và khả năng mở rộng.

**4.1. PA1 — Nâng cấp tại chỗ (on-premise)**

Dựng máy chủ tại văn phòng 770 Quang Trung, tự vận hành cổng giao diện
lập trình và kho dữ liệu. Lớp compute và network do doanh nghiệp sở hữu;
lớp vận hành, bảo mật, ứng dụng và dữ liệu đều tự quản. Sẵn sàng ở mức
active-standby trong cùng một địa điểm, sao lưu ra ổ ngoài. Tích hợp
bằng cách gọi trực tiếp tới các hệ thống nhà cung cấp. Mở rộng bằng cách
mua thêm máy chủ.

**Điểm mạnh:** kiểm soát dữ liệu cao nhất, phù hợp nếu doanh nghiệp
không muốn dữ liệu sinh trắc học ra khỏi phạm vi mình quản. **Điểm yếu
quyết định:** chi phí đầu tư ban đầu cao nhất và đòi hỏi nhân sự vận
hành thường trực — thứ mà Ways Station không có và cũng chưa từng tuyển
\[2\]\[17\]\[18\]. Toàn bộ hệ thống đặt ở một địa điểm cũng là một điểm
lỗi đơn.

**4.2. PA2 — Hybrid (phương án khuyến nghị)**

Giữ nguyên các nền tảng thuê ngoài đang chạy tốt — ứng dụng gym, hệ
thống đặt sân, nhận diện khuôn mặt — và bổ sung hai lớp còn thiếu trên
cloud: lớp tích hợp (N1 cổng API, N2 định danh khách hàng dùng chung
theo chuẩn OIDC, N3 dịch vụ thanh toán và đối soát tự động) cùng lớp dữ
liệu (N4 kho dữ liệu vận hành hợp nhất, N5 danh mục dữ liệu cá nhân và
hồ sơ tuân thủ, N6 dữ liệu chủ về chi nhánh). Dữ liệu sinh trắc học để
nguyên tại nhà cung cấp, chỉ đồng bộ trạng thái gói tập và nhật ký ra
vào — cách này giảm phạm vi dữ liệu nhạy cảm phải tự bảo vệ.

<img src="media/image2.png" style="width:6.14173in;height:2.75281in" />

*Hình 4.1. Kiến trúc TO-BE của PA2 theo năm lớp*

Sẵn sàng và khôi phục: dịch vụ cloud ở mức active-standby giữa hai vùng,
sao lưu kho dữ liệu theo ngày với bản sao không thể ghi đè, mục tiêu RPO
≤ 4 giờ và RTO ≤ 8 giờ, có diễn tập khôi phục định kỳ. Tích hợp: mọi
kênh đi qua cổng API duy nhất, xác thực tập trung cho cả khách hàng và
nhân viên, nhật ký và giám sát gom về một nơi, tiếp nhận sự cố qua một
hàng đợi duy nhất. Mở rộng: thêm chi nhánh chỉ là thêm một nguồn dữ
liệu, không phát sinh thêm giờ cộng tay.

**Điều kiện tiên quyết:** đàm phán được điều khoản truy xuất dữ liệu với
nhà cung cấp ứng dụng gym (rủi ro R2), và bố trí ít nhất một đầu mối
công nghệ thông tin nội bộ làm đối tác của bên vận hành.

**4.3. PA3 — Cloud-first toàn phần**

Thay cả phần mềm quầy và hệ thống đặt sân bằng một nền tảng chuỗi thương
mại hợp nhất, chuyển toàn bộ nghiệp vụ lên cloud của một nhà cung cấp.
Lớp ứng dụng, dữ liệu, vận hành và bảo mật do nhà cung cấp đảm nhiệm
theo cam kết dịch vụ. Sẵn sàng và khôi phục theo mức nhà cung cấp công
bố. Tích hợp nội tại vì mọi thứ trong cùng một nền tảng. Mở rộng nhanh
nhất — thêm chi nhánh chỉ là cấu hình.

**Điểm mạnh:** hợp nhất triệt để, một hợp đồng, một đầu mối. **Điểm
yếu:** phải thay đổi quy trình làm việc đồng thời ở 38+ chi nhánh đang
hoạt động 24 giờ, trong khi doanh nghiệp không có đội ngũ để dẫn dắt
thay đổi diện rộng; khóa chặt vào một nhà cung cấp, làm rủi ro R2 nặng
hơn chứ không nhẹ đi; và chi phí chuyển đổi cao nhất trong ba phương án.

**4.4. So sánh và kết luận**

| **Tiêu chí** | **PA1 On-premise** | **PA2 Hybrid** | **PA3 Cloud-first** |
|----|----|----|----|
| Chi phí đầu tư ban đầu (CAPEX) | Cao | **Thấp** | Trung bình |
| Chi phí vận hành hằng năm (OPEX) | Trung bình | Trung bình | Cao |
| TCO 3 năm (tương đối) | Cao | **Thấp nhất** | Cao nhất |
| Thời gian tới báo cáo hợp nhất đầu tiên | 6–9 tháng | **2 tháng** | 6–12 tháng |
| Yêu cầu nhân sự nội bộ | Đội vận hành thường trực | **1 đầu mối CNTT** | 1 đầu mối + đội dẫn dắt thay đổi |
| Mức độ gián đoạn vận hành khi triển khai | Trung bình | **Thấp** | Cao — thay quy trình ở 38+ chi nhánh |
| Rủi ro chính | Thiếu người vận hành; điểm lỗi đơn | Phụ thuộc nhà cung cấp app gym (R2) | Khóa nhà cung cấp; rủi ro chuyển đổi |
| Phù hợp với ràng buộc của Ways Station | Không — không có phòng CNTT | **Có** | Chỉ khi có đội dẫn dắt thay đổi |

*Bảng 4.1. So sánh ba phương án theo tám tiêu chí*

**Kết luận: chọn PA2 — Hybrid.** Ba lý do. Thứ nhất, đây là phương án
duy nhất tương thích với ràng buộc cứng nhất của doanh nghiệp là không
có nhân sự công nghệ thông tin nội bộ. Thứ hai, nó không phá vỡ những gì
đang chạy tốt — hệ thống đặt sân và nhận diện khuôn mặt vẫn hoạt động
nguyên trạng — nên rủi ro triển khai thấp nhất. Thứ ba, nó cho kết quả
đo được sớm nhất: chỉ cần hoàn thành N4 ở pha một là chỉ tiêu K1 và K2
đã cải thiện, trước khi phải chạm tới bất kỳ hệ thống hướng khách hàng
nào.

**DANH MỤC NGUỒN**

**\[1\]** Website chính thức Ways Station —
[<u>https://www.waysstation.vn</u>](https://www.waysstation.vn)

**\[2\]** Trang tuyển dụng hệ thống Ways Station —
[<u>https://diachi.ways.vn/tuyendung</u>](https://diachi.ways.vn/tuyendung)

**\[3\]** Tra cứu mã số thuế hộ kinh doanh WAYS STATION – GYM —
[<u>https://masothue.com</u>](https://masothue.com)

**\[4\]** Tra cứu mã số thuế hộ kinh doanh WAYS STATION GV —
[<u>https://masothue.com</u>](https://masothue.com)

**\[5\]** Tra cứu mã số thuế hộ kinh doanh WAYS STATION N.V.L —
[<u>https://masothue.com</u>](https://masothue.com)

**\[6\]** Hồ sơ doanh nghiệp trên cổng tuyển dụng —
[<u>https://ybox.vn</u>](https://ybox.vn)

**\[7\]** Thông tin địa chỉ trụ sở theo nguồn cũ —
[<u>https://diachi.ways.vn</u>](https://diachi.ways.vn)

**\[8\]** Trang dịch vụ phòng tập gym —
[<u>https://diachi.ways.vn/g</u>](https://diachi.ways.vn/g)

**\[9\]** Trang dịch vụ billiards —
[<u>https://diachi.ways.vn/b</u>](https://diachi.ways.vn/b)

**\[10\]** Trang giới thiệu chi nhánh mới —
[<u>https://diachi.ways.vn/cnmoi</u>](https://diachi.ways.vn/cnmoi)

**\[11\]** Hướng dẫn đặt sân cầu lông —
[<u>https://diachi.ways.vn/san</u>](https://diachi.ways.vn/san)

**\[12\]** Quy định sử dụng sân cầu lông —
[<u>https://san.ways.io.vn</u>](https://san.ways.io.vn)

**\[13\]** Trang thông tin gói tập và ứng dụng hội viên —
[<u>https://diachi.ways.vn/web</u>](https://diachi.ways.vn/web)

**\[14\]** Ứng dụng di động quản lý gói tập —
[<u>https://diachi.ways.vn/web</u>](https://diachi.ways.vn/web)

**\[15\]** Thông tin nền tảng nhà cung cấp ứng dụng phòng tập —
[<u>https://diachi.ways.vn/web</u>](https://diachi.ways.vn/web)

**\[16\]** Bài công bố danh sách trang chính thức và địa chỉ cửa hàng,
03/11/2025 — [<u>https://waysstation.vn</u>](https://waysstation.vn)

**\[17\]** Tin tuyển dụng hệ thống thể thao giải trí Ways Station —
[<u>https://ybox.vn</u>](https://ybox.vn)

**\[18\]** Tin tuyển dụng vị trí nhân viên nhập liệu —
[<u>https://ybox.vn</u>](https://ybox.vn)

**\[23\]** Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân —
[<u>https://vanban.chinhphu.vn</u>](https://vanban.chinhphu.vn)

**\[24\]** Luật Bảo vệ dữ liệu cá nhân —
[<u>https://vanban.chinhphu.vn</u>](https://vanban.chinhphu.vn)

**PHỤ LỤC A. GIẢ ĐỊNH CẦN KIỂM CHỨNG**

| **Giả định** | **Cơ sở hiện tại** | **Cách kiểm chứng** |
|----|----|----|
| Báo cáo doanh thu toàn hệ thống có sau T+~30 ngày | Suy từ chu kỳ lên sổ của kế toán từng hộ kinh doanh | Phỏng vấn kế toán và quản lý khu vực |
| ~306 giờ lao động thủ công mỗi tuần | 38 chi nhánh × 3 ca × 20 phút × 7 ngày, cộng ~40 giờ nhập liệu | Quan sát một ca chốt tại chi nhánh; đối chiếu bảng phân công |
| ~3% giao dịch đặt sân phải xử lý tay | Doanh nghiệp phải đăng cảnh báo ghi đúng mã đơn hàng \[11\] | Xin số liệu giao dịch treo từ bộ phận đường dây nóng |
| Quy trình chốt ca đi qua nhân viên nhập liệu | Doanh nghiệp tuyển vị trí nhân viên nhập liệu \[18\]; mỗi chi nhánh thuộc pháp nhân riêng \[3\]\[4\] | Phỏng vấn trưởng ca và nhân viên nhập liệu |

*Bảng A.1. Bốn giả định trọng yếu — thay bằng số thật khi khảo sát trực
tiếp được*
