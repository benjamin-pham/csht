# KHẢO SÁT HIỆN TRẠNG HẠ TẦNG CÔNG NGHỆ THÔNG TIN TẠI HỆ THỐNG THỂ THAO -- GIẢI TRÍ WAYS STATION

## Định hướng đầu tư lớp năng lực Nền tảng Ứng dụng & Tích hợp và Nền tảng Dữ liệu

> **Môn học:** Cơ sở hạ tầng Công nghệ thông tin
>
> **Chương tham chiếu:** Chương 2 -- Kiến trúc hạ tầng CNTT doanh nghiệp
> và tư duy hệ thống

**Giảng viên hướng dẫn:** ThS. Nguyễn Thị Anh Thư

**Trường:** Đại học Công nghệ Thông tin -- Đại học Quốc gia TP. Hồ Chí
Minh

**Lớp năng lực phụ trách:** (4) Nền tảng Ứng dụng & Tích hợp và (5) Nền
tảng Dữ liệu

**Thời gian thực hiện:** Tháng 8 năm 2026

## MỤC LỤC

> **DANH MỤC TỪ VIẾT TẮT** **DANH MỤC BẢNG BIỂU VÀ HÌNH VẼ** **MỞ ĐẦU**
>
> **CHƯƠNG 1. TỔNG QUAN VỀ ĐƠN VỊ KHẢO SÁT**
>
> 1.1. Giới thiệu chung về đơn vị
>
> 1.2. Hệ thống website và các kênh trực tuyến
>
> 1.3. Lớp năng lực dự kiến đầu tư
>
> **CHƯƠNG 2. BỐI CẢNH HOẠT ĐỘNG CỦA DOANH NGHIỆP**
>
> 2.1. Ngành nghề và mô hình kinh doanh
>
> 2.2. Quy mô và phạm vi hoạt động
>
> 2.3. Cơ cấu tổ chức
>
> 2.4. Các quy trình nghiệp vụ chính
>
> **CHƯƠNG 3. PHÂN TÍCH HIỆN TRẠNG VÀ CÁC VẤN ĐỀ TỒN TẠI**
>
> 3.1. Bản đồ hệ thống công nghệ thông tin hiện có
>
> 3.2. Các điểm nghẽn trong vận hành
>
> 3.3. Các rủi ro tiềm ẩn
>
> 3.4. Chi phí ẩn
>
> 3.5. Tình trạng phân mảnh dữ liệu
>
> **CHƯƠNG 4. ĐỐI TƯỢNG SỬ DỤNG VÀ MỨC ĐỘ SỐ HÓA**
>
> 4.1. Thang đánh giá mức độ số hóa
>
> 4.2. Nhóm người dùng nội bộ
>
> 4.3. Nhóm người dùng bên ngoài
>
> 4.4. Đánh giá chung về mức độ trưởng thành số
>
> **KẾT LUẬN** **TÀI LIỆU THAM KHẢO** **PHỤ LỤC**
>
> **A. Các giả định cần kiểm chứng** **PHỤ LỤC**
>
> **B. Bộ câu hỏi phỏng vấn dự kiến**

## DANH MỤC TỪ VIẾT TẮT

+:-----------------:+--------------------------------------------------+
| > **Từ viết tắt** | > **Diễn giải**                                  |
+-------------------+--------------------------------------------------+
| > API             | > Application Programming Interface -- Giao diện |
|                   | > lập trình ứng dụng                             |
+-------------------+--------------------------------------------------+
| > BHXH            | > Bảo hiểm xã hội                                |
+-------------------+--------------------------------------------------+
| > CNTT            | > Công nghệ thông tin                            |
+-------------------+--------------------------------------------------+
| > ETL             | > Extract -- Transform -- Load, quy trình trích  |
|                   | > xuất, biến đổi và nạp dữ liệu                  |
+-------------------+--------------------------------------------------+
| > HKD             | > Hộ kinh doanh                                  |
+-------------------+--------------------------------------------------+
| > MST             | > Mã số thuế                                     |
+-------------------+--------------------------------------------------+
| > NĐ              | > Nghị định                                      |
+-------------------+--------------------------------------------------+
| > OIDC            | > OpenID Connect, giao thức xác thực mở          |
+-------------------+--------------------------------------------------+
| > SSO             | > Single Sign-On -- Đăng nhập một lần            |
+-------------------+--------------------------------------------------+
| > TCVN            | > Tiêu chuẩn quốc gia Việt Nam                   |
+-------------------+--------------------------------------------------+

## DANH MỤC BẢNG BIỂU VÀ HÌNH VẼ

> **Bảng 1.1.** Thông tin nhận diện đơn vị khảo sát
>
> **Bảng 1.2.** Các pháp nhân mang thương hiệu Ways Station đã xác định
>
> **Bảng 1.3.** Hệ thống tên miền đang được sử dụng
>
> **Bảng 2.1.** Các dòng dịch vụ và mô hình giá
>
> **Bảng 2.2.** Mốc phát triển tái dựng từ dữ liệu đăng ký kinh doanh
>
> **Bảng 3.1.** Các hệ thống công nghệ thông tin hiện có
>
> **Bảng 3.2.** Ước tính chi phí ẩn hằng năm
>
> **Bảng 4.1.** Thang đánh giá mức độ số hóa
>
> **Bảng 4.2.** Mức độ số hóa của các nhóm người dùng nội bộ
>
> **Bảng 4.3.** Mức độ số hóa của các nhóm người dùng bên ngoài
>
> **Hình 2.1.** Sơ đồ cơ cấu tổ chức tái dựng
>
> **Hình 2.2.** Luồng quy trình đặt và thanh toán sân cầu lông
>
> **Hình 3.1.** Sơ đồ phân mảnh dữ liệu hiện tại

# MỞ ĐẦU

> Chương 2 của môn học đặt ra một khung tham chiếu gồm năm lớp năng lực
> để mô tả hạ tầng công nghệ thông tin của một tổ chức, trong đó mỗi lớp
> được xem xét theo năm khía cạnh: phần cứng, phần mềm, mạng, quản trị
> và bảo mật \[28\]. Điểm mấu chốt của khung này nằm ở chỗ nó không mô
> tả thiết bị, mà mô tả *năng lực mà tổ chức phải sở hữu*. Một tổ chức
> có thể mua đủ máy móc nhưng vẫn thiếu năng lực, và ngược lại.
>
> Đồ án lựa chọn hệ thống thể thao -- giải trí Ways Station tại Thành
> phố Hồ Chí Minh làm đối tượng khảo sát. Trong phân công của nhóm,
> người viết phụ trách hai lớp năng lực trên cùng của khung tham chiếu:
> lớp (4) Nền tảng Ứng dụng và Tích hợp, và lớp (5) Nền tảng Dữ liệu.
>
> Lý do lựa chọn đơn vị này khá đơn giản. Ways Station là một doanh
> nghiệp dịch vụ tăng trưởng nhanh, đã có những bước số hóa nhất định
> nhưng chưa đồng đều, và quan trọng hơn cả là **phần lớn hiện trạng
> công nghệ của họ có thể quan sát được từ bên ngoài** thông qua chính
> các trang thông tin, hướng dẫn sử dụng dịch vụ và tin tuyển dụng mà
> doanh nghiệp công bố. Điều này cho phép một đồ án môn học có thể dựa
> trên minh chứng thực tế thay vì phải giả định toàn bộ.
>
> Về phương pháp, người viết sử dụng ba nguồn dữ liệu. Thứ nhất là các
> trang thông tin chính thức của doanh nghiệp, bao gồm website, các
> trang hướng dẫn dịch vụ và trang tuyển dụng. Thứ hai là dữ liệu đăng
> ký kinh doanh tra cứu qua cơ sở dữ liệu mã số thuế, dùng để xác định
> pháp nhân và tái dựng mốc thời gian phát triển. Thứ ba là các nguồn
> thứ cấp độc lập như bài đánh giá dịch vụ và tin tuyển dụng đăng trên
> các cổng việc làm.
>
> Do chưa có điều kiện tiếp cận tài liệu nội bộ và phỏng vấn trực tiếp,
> một số nội dung --- cụ thể là sơ đồ phòng ban chi tiết, số liệu doanh
> thu và danh tính các nhà cung cấp phần mềm --- phải dựa trên suy luận
> từ dữ kiện gián tiếp. Những nội dung này đều được nêu rõ trong phần
> trình bày và tổng hợp lại tại Phụ lục A, kèm phương án kiểm chứng cho
> giai đoạn khảo sát tiếp theo.

# CHƯƠNG 1. TỔNG QUAN VỀ ĐƠN VỊ KHẢO SÁT

## 1.1. Giới thiệu chung về đơn vị

> Ways Station là một hệ thống cơ sở thể thao và giải trí hoạt động chủ
> yếu tại Thành phố Hồ Chí Minh. Doanh nghiệp tự giới thiệu là *\"hệ
> sinh thái Thể thao, Giải trí, Không gian học và làm\"* \[1\], với sứ
> mệnh được công bố là *\"mang đến trải nghiệm giải trí lành mạnh, thúc
> đẩy lối sống năng động và tích cực cho cộng đồng\"* \[17\].
>
> **Bảng 1.1. Thông tin nhận diện đơn vị khảo sát**

+:---------:+----------------------------------------------------------+
| > **Hạng  | > **Nội dung**                                           |
| > mục**   |                                                          |
+-----------+----------------------------------------------------------+
| > Tên     | > Ways Station (tin tuyển dụng đôi khi dùng \"Ways       |
| > thương  | > Station Group\")                                       |
| > hiệu    |                                                          |
+-----------+----------------------------------------------------------+
| > Website | > https://www.waysstation.vn                             |
| > chính   |                                                          |
+-----------+----------------------------------------------------------+
| > Trụ sở  | > Lầu 3, số 770 Quang Trung, Phường Thông Tây Hội, TP.   |
| > điều    | > Hồ Chí Minh                                            |
| > hành    |                                                          |
+-----------+----------------------------------------------------------+
| > Lĩnh    | > Dịch vụ thể thao, giải trí, vui chơi                   |
| > vực     |                                                          |
| > hoạt    |                                                          |
| > động    |                                                          |
+-----------+----------------------------------------------------------+
| > Dịch vụ | > Phòng tập gym, gym dành riêng cho nữ, không gian học   |
| > cung    | > và làm việc, billiards, gaming, sân cầu lông,          |
| > cấp     | > kickfit/boxing                                         |
+-----------+----------------------------------------------------------+
| > Quy mô  | > Trên 38 chi nhánh tại 12 quận                          |
| > mạng    |                                                          |
| > lưới    |                                                          |
+-----------+----------------------------------------------------------+
| > Quy mô  | > 50 đến 249 người có đóng bảo hiểm xã hội               |
| > nhân sự |                                                          |
+-----------+----------------------------------------------------------+
| > Thời    | > 24 giờ mỗi ngày tại phần lớn chi nhánh                 |
| > gian    |                                                          |
| > hoạt    |                                                          |
| > động    |                                                          |
+-----------+----------------------------------------------------------+
| > Điện    | > 0889.555.559, hoạt động từ 7 giờ đến 23 giờ            |
| > thoại   |                                                          |
| > liên hệ |                                                          |
+-----------+----------------------------------------------------------+
| > Thư     | > admin@ways.io.vn                                       |
| > điện tử |                                                          |
| > hệ      |                                                          |
| > thống   |                                                          |
+-----------+----------------------------------------------------------+

> *Nguồn: tổng hợp từ \[1\], \[2\], \[5\], \[6\], \[7\].*
>
> Một đặc điểm cần được nêu ngay từ đầu, bởi nó chi phối gần như toàn bộ
> phần phân tích về sau, là **Ways Station không hoạt động dưới hình
> thức một công ty duy nhất**. Kết quả tra cứu cơ sở dữ liệu đăng ký
> kinh doanh cho thấy thương hiệu này được vận hành thông qua một chuỗi
> các hộ kinh doanh cá thể độc lập, mỗi hộ có mã số thuế riêng và chủ hộ
> riêng.
>
> **Bảng 1.2. Các pháp nhân mang thương hiệu Ways Station đã xác định**

+:--------------:+------------------+-----------+----------------------+--------------+
| > **Tên hộ     | > **Mã số thuế** | > **Chủ   | > **Địa chỉ**        | > **Ngày     |
| > kinh doanh** |                  | > hộ**    |                      | > cấp**      |
+----------------+------------------+-----------+----------------------+--------------+
| > WAYS STATION | > 8509739366-001 | > Nguyễn  | > 770 Quang Trung,   | > 24/08/2022 |
| > -- GYM       |                  | > Thị Thu | > Phường Thông Tây   |              |
|                |                  | > Huệ     | > Hội                |              |
+----------------+------------------+-----------+----------------------+--------------+
| > (địa điểm    | > 8509739366-002 | > ---     | > 340 Tô Ký, Quận 12 | > ---        |
| > kinh doanh   |                  |           |                      |              |
| > trực thuộc)  |                  |           |                      |              |
+----------------+------------------+-----------+----------------------+--------------+
| > WAYS STATION | > 8609700179-001 | > Vũ Thị  | > 66 Lê Lợi, Phường  | > 27/09/2023 |
| > GV           |                  | > Minh    | > 4, Gò Vấp          |              |
|                |                  | > Nguyệt  |                      |              |
+----------------+------------------+-----------+----------------------+--------------+
| > WAYS STATION | > 8853107310-001 | > ---     | > 70 Nguyễn Văn      | > Chưa xác   |
| > N.V.L        |                  |           | > Lượng, Phường 10,  | > định       |
|                |                  |           | > Gò Vấp             |              |
+----------------+------------------+-----------+----------------------+--------------+
| > WAYS STATION | > Chưa xác định  | > ---     | > Chưa xác định      | > Chưa xác   |
| > QT           |                  |           |                      | > định       |
+----------------+------------------+-----------+----------------------+--------------+
| > WAYS STATION | > Chưa xác định  | > ---     | > Chưa xác định      | > Chưa xác   |
| > DH           |                  |           |                      | > định       |
+----------------+------------------+-----------+----------------------+--------------+

> *Nguồn: \[3\], \[4\], \[5\], \[6\].*
>
> Việc mở rộng bằng cách lập thêm hộ kinh doanh mới cho từng địa điểm là
> một lựa chọn phổ biến và hợp lý đối với chuỗi dịch vụ quy mô vừa tại
> Việt Nam, vì thủ tục đơn giản và nghĩa vụ kế toán nhẹ hơn so với doanh
> nghiệp. Tuy nhiên, xét từ góc độ hạ tầng thông tin, lựa chọn này tạo
> ra một hệ quả quan trọng: **dữ liệu tài chính của hệ thống bị chia cắt
> theo pháp nhân ngay từ gốc, trước khi phát sinh bất kỳ vấn đề kỹ thuật
> nào**. Đây là điểm sẽ được phân tích kỹ ở Chương 3.

## 1.2. Hệ thống website và các kênh trực tuyến

> Website chính thức của đơn vị là **waysstation.vn** \[1\]. Tuy nhiên,
> quá trình khảo sát cho thấy Ways Station không vận hành một cổng thông
> tin thống nhất, mà đang sử dụng song song bốn tên miền trên ba nền
> tảng công nghệ khác nhau.
>
> **Bảng 1.3. Hệ thống tên miền đang được sử dụng**

+:------------------------:+------------------+-------------+--------------------------+
| > **Tên miền**           | > **Vai trò**    | > **Nền     | > **Ghi nhận khi khảo    |
|                          |                  | > tảng**    | > sát**                  |
+--------------------------+------------------+-------------+--------------------------+
| > waysstation.vn         | > Website chính, | > WordPress | > Hoạt động; một số      |
|                          | > giới thiệu hệ  |             | > trang con trả về thông |
|                          | > sinh thái, tin |             | > báo lỗi \"Trang chưa   |
|                          | > bài, trang     |             | > được xuất bản\" của    |
|                          | > từng chi nhánh |             | > nền tảng landing page  |
+--------------------------+------------------+-------------+--------------------------+
| > diachi.ways.vn         | > Danh sách địa  | > Webcake   | > Hoạt động, chứa thông  |
|                          | > chỉ, bảng giá, |             | > tin vận hành đầy đủ    |
|                          | > tuyển dụng,    |             | > nhất                   |
|                          | > hướng dẫn đặt  |             |                          |
|                          | > sân            |             |                          |
+--------------------------+------------------+-------------+--------------------------+
| > san.ways.io.vn         | > Hệ thống đặt   | > Chưa xác  | > Hoạt động              |
|                          | > sân cầu lông   | > định      |                          |
|                          | > trực tuyến     |             |                          |
+--------------------------+------------------+-------------+--------------------------+
| > diachi.waysstation.vn, | > Tên miền song  | > ---       | > Hoạt động              |
| > san.waysstation.vn     | > song, trỏ tới  |             |                          |
|                          | > cùng nội dung  |             |                          |
+--------------------------+------------------+-------------+--------------------------+

> *Nguồn: \[1\], \[2\], \[10\], \[11\], \[16\].*
>
> Điểm đáng chú ý ở đây không nằm ở số lượng tên miền, mà ở chỗ **những
> thông tin vận hành quan trọng nhất lại không nằm trên website chính**.
> Bảng giá dịch vụ, quy trình đặt sân, quy trình đăng ký gói tập và
> thông tin tuyển dụng đều được đặt trên các trang landing page dựng
> bằng công cụ tiếp thị, trong khi website chính chủ yếu đóng vai trò
> giới thiệu. Khách hàng muốn biết giá một dịch vụ phải đi qua một tên
> miền khác với tên miền thương hiệu.
>
> Bên cạnh website, doanh nghiệp còn hiện diện trên nhiều kênh mạng xã
> hội. Đáng chú ý là ngày 03 tháng 11 năm 2025, Ways Station đã phải
> đăng một bài viết chính thức nhằm xác nhận danh sách các trang
> Facebook thuộc hệ thống và danh sách địa chỉ cửa hàng \[16\]. Việc một
> doanh nghiệp phải công bố như vậy cho thấy hệ thống đã đủ lớn để phát
> sinh tình trạng phân tán kênh và nguy cơ mạo danh.

## 1.3. Lớp năng lực dự kiến đầu tư

> Theo khung tham chiếu tại Chương 2 của môn học, năm lớp năng lực được
> sắp xếp theo thứ tự phụ thuộc kỹ thuật, từ nền tảng vật lý lên tới dữ
> liệu \[28\]. Trong phạm vi phân công, đồ án tập trung vào hai lớp trên
> cùng.
>
> **Lớp (4) Nền tảng Ứng dụng và Tích hợp** là lớp biến hạ tầng thành
> chức năng nghiệp vụ và kết nối các chức năng đó với nhau. Đối chiếu
> với hiện trạng của Ways Station, nhóm nhận thấy khoảng trống lớn nhất
> nằm ở cột phần mềm và cột bảo mật. Doanh nghiệp hiện có bốn ứng dụng
> hoạt động độc lập nhưng không có bất kỳ thành phần trung gian nào cho
> phép chúng trao đổi dữ liệu, cũng chưa có cơ chế xác thực tập trung để
> một khách hàng chỉ cần một danh tính duy nhất khi sử dụng nhiều dịch
> vụ. Vì vậy, hai hạng mục dự kiến đầu tư ở lớp này là cổng giao diện
> lập trình ứng dụng đóng vai trò điểm vào chung, và cơ chế định danh
> khách hàng dùng chung theo chuẩn mở.
>
> Ở cột quản trị, do doanh nghiệp không có nhân sự công nghệ thông tin
> chuyên trách, nhóm cho rằng chỉ nên đặt mục tiêu ở mức tối thiểu là
> quản lý phiên bản giao diện lập trình và giám sát hoạt động ứng dụng,
> thay vì xây dựng quy trình tích hợp và triển khai liên tục vốn đòi hỏi
> đội ngũ kỹ thuật thường trực. Cột phần cứng nằm ngoài phạm vi, vì lớp
> (4) sử dụng chung hạ tầng tính toán của lớp (1).
>
> **Lớp (5) Nền tảng Dữ liệu** là lớp lưu giữ, di chuyển, biến đổi và
> cung cấp dữ liệu cho toàn tổ chức. Đây là lớp mà Ways Station gần như
> chưa xây dựng. Doanh nghiệp chưa có kho dữ liệu tập trung, chưa có quy
> trình trích xuất và nạp dữ liệu tự động, và việc hợp nhất số liệu hiện
> đang do con người thực hiện thủ công. Ba hạng mục dự kiến đầu tư gồm:
> kho dữ liệu vận hành hợp nhất cho toàn hệ thống, danh mục dữ liệu cá
> nhân kèm hồ sơ tuân thủ pháp luật, và việc chuẩn hóa lại dữ liệu địa
> chỉ chi nhánh sau đợt sắp xếp đơn vị hành chính.
>
> Có bốn lý do khiến nhóm cho rằng hai lớp này là lựa chọn đầu tư hợp lý
> nhất đối với Ways Station.
>
> Thứ nhất, đây là hai lớp có khoảng trống lớn nhất. Với mô hình chuỗi
> cơ sở dịch vụ, các lớp hạ tầng tính toán và vận hành ở mức hiện tại đã
> tạm đủ dùng, trong khi lớp ứng dụng, tích hợp và lớp dữ liệu gần như
> còn trống.
>
> Thứ hai, hai lớp này chạm trực tiếp vào doanh thu. Việc đặt sân, bán
> gói tập và hợp nhất doanh thu toàn hệ thống đều nằm ở đây, nên hiệu
> quả đầu tư có thể đo lường được bằng con số kinh doanh chứ không chỉ
> bằng chỉ số kỹ thuật.
>
> Thứ ba, doanh nghiệp đã chứng minh được năng lực tiếp nhận. Việc số
> hóa hoàn chỉnh quy trình đặt sân cầu lông cho thấy tổ chức đủ khả năng
> vận hành một hệ thống tự phục vụ; vấn đề còn lại chỉ là nhân rộng đúng
> cách sang các dịch vụ khác.
>
> Thứ tư, đã tồn tại sức ép pháp lý cụ thể. Việc sử dụng nhận diện khuôn
> mặt để kiểm soát ra vào tạo ra dữ liệu sinh trắc học, kéo theo các
> nghĩa vụ được quy định tại Nghị định 13/2023/NĐ-CP \[23\]. Đây là vấn
> đề không thể trì hoãn vô thời hạn.

# CHƯƠNG 2. BỐI CẢNH HOẠT ĐỘNG CỦA DOANH NGHIỆP

## 2.1. Ngành nghề và mô hình kinh doanh

> Ways Station hoạt động trong lĩnh vực dịch vụ thể thao và giải trí,
> theo mô hình chuỗi cơ sở vật lý. Doanh thu đến từ hai nguồn có bản
> chất khác nhau: doanh thu thuê bao theo tháng đối với dịch vụ phòng
> tập, và doanh thu theo lượt sử dụng đối với các dịch vụ còn lại.
>
> **Bảng 2.1. Các dòng dịch vụ và mô hình giá**

+:-----------:+-----------+--------------------------+---------------------+
| > **Dịch    | > **Mô    | > **Giá công bố**        | > **Kênh bán và     |
| > vụ**      | > hình    |                          | > hình thức thanh   |
|             | > doanh   |                          | > toán**            |
|             | > thu**   |                          |                     |
+-------------+-----------+--------------------------+---------------------+
| > Gym       | > Thuê    | > 320.000 đồng/tháng;    | > Tại quầy, từ 6    |
|             | > bao     | > gói ba tháng tặng một  | > giờ đến 24 giờ;   |
|             | > tháng,  | > tháng 960.000 đồng     | > tiền mặt, VietQR  |
|             | > dùng    |                          | > hoặc chuyển       |
|             | > chung   |                          | > khoản; không chấp |
|             | > mọi chi |                          | > nhận thẻ tín dụng |
|             | > nhánh   |                          |                     |
+-------------+-----------+--------------------------+---------------------+
| > KickFit,  | > Thuê    | > 299.000 đồng/tháng;    | > Tại quầy          |
| > Boxing    | > bao     | > 897.000 đồng cho gói   |                     |
|             | > tháng   | > ba tháng tặng một      |                     |
+-------------+-----------+--------------------------+---------------------+
| > Gaming    | > Tính    | > 6.000 đến 10.000       | > Thu ngân tại quầy |
|             | > theo    | > đồng/giờ, có khuyến    |                     |
|             | > giờ     | > mãi 5.000 đồng         |                     |
+-------------+-----------+--------------------------+---------------------+
| > Billiards | > Tính    | > Bàn pool và libre      | > Thu ngân tại      |
|             | > theo    | > 29.000 đồng khung      | > quầy; phụ thu     |
|             | > giờ,    | > 14--16 giờ, 39.000     | > 5.000 đồng nếu    |
|             | > phân    | > đồng khung 16 giờ đến  | > mang đồ ăn uống   |
|             | > biệt    | > 2 giờ; bàn ba băng     | > từ ngoài vào      |
|             | > loại    | > 39.000 và 49.000 đồng  |                     |
|             | > bàn và  |                          |                     |
|             | > khung   |                          |                     |
|             | > giờ     |                          |                     |
+-------------+-----------+--------------------------+---------------------+
| > Cầu lông  | > Đặt sân | > 139.000 đồng/giờ;      | > Trực tuyến, thanh |
|             | > theo    | > 150.000 đồng/giờ khung | > toán trước toàn   |
|             | > giờ     | > 18--22 giờ             | > bộ bằng mã QR     |
+-------------+-----------+--------------------------+---------------------+
| > Không     | > Chưa    | > Chưa công bố           | > Chưa xác định     |
| > gian học  | > xác     |                          |                     |
| > và làm    | > định    |                          |                     |
| > việc      |           |                          |                     |
+-------------+-----------+--------------------------+---------------------+

> *Nguồn: \[8\], \[9\], \[10\], \[11\], \[12\], \[20\], \[21\].*
>
> Từ bảng trên có thể rút ra ba đặc điểm của mô hình kinh doanh, và cả
> ba đều ảnh hưởng trực tiếp tới bài toán hạ tầng thông tin.
>
> Đặc điểm thứ nhất là **tính đa dịch vụ trong cùng một mặt bằng**. Một
> chi nhánh của Ways Station có thể đồng thời là phòng tập, tiệm
> billiards, phòng game và sân cầu lông. Điều này có nghĩa một khách
> hàng hoàn toàn có thể sử dụng nhiều dịch vụ trong cùng một lần đến.
> Tuy nhiên, như sẽ phân tích ở Chương 3, hệ thống hiện tại không có khả
> năng nhận ra rằng đó là cùng một người.
>
> Đặc điểm thứ hai là **sự tồn tại song song của hai mô hình thanh toán
> trái ngược nhau trong cùng một cơ sở**. Dịch vụ cầu lông yêu cầu thanh
> toán trước toàn bộ qua mạng, và trang hướng dẫn của doanh nghiệp ghi
> rõ *\"Ways không có thu ngân tại tiệm\"* \[11\]. Trong khi đó, gym,
> gaming và billiards vẫn thu tiền tại quầy \[8\], \[9\], \[10\]. Một
> nhóm khách vừa chơi cầu lông vừa uống nước hoặc chơi billiards sẽ trải
> qua hai quy trình thanh toán hoàn toàn khác nhau tại cùng một địa
> điểm.
>
> Đặc điểm thứ ba là **mô hình đa pháp nhân** đã trình bày ở mục 1.1.
> Việc mỗi chi nhánh là một hộ kinh doanh riêng khiến số liệu tài chính
> không có một nơi tập trung tự nhiên nào.

## 2.2. Quy mô và phạm vi hoạt động

> Về quy mô mạng lưới, số liệu do doanh nghiệp công bố có sự chênh lệch
> giữa các kênh. Trang tuyển dụng ghi nhận trên 38 chi nhánh tại 12 quận
> \[2\]; trang giới thiệu chi nhánh mới ghi 30 chi nhánh \[10\]; trang
> dịch vụ gym ghi trên 32 điểm \[8\]; trong khi một số nguồn thứ cấp cũ
> hơn ghi 22 đến 25 chi nhánh \[17\], \[19\]. Riêng dịch vụ billiards
> được công bố tại trên 20 chi nhánh \[9\].
>
> Bản thân sự chênh lệch này đã là một dữ kiện đáng chú ý. Khi cùng một
> tổ chức công bố bốn con số khác nhau về quy mô của chính mình trên bốn
> trang thông tin khác nhau, điều đó cho thấy **không tồn tại một nguồn
> dữ liệu gốc duy nhất về danh sách chi nhánh**. Trong thuật ngữ quản
> trị dữ liệu, đây chính là biểu hiện của việc thiếu dữ liệu chủ, một
> vấn đề thuộc phạm vi lớp (5).
>
> Về địa bàn, hoạt động tập trung tại Thành phố Hồ Chí Minh, với các chi
> nhánh đã xác định được tại Gò Vấp, Bình Thạnh, Tân Bình, Tân Phú, Quận
> 7, Quận 10, Quận 12, Thủ Đức và Bình Chánh. Ngoài ra, tin tuyển dụng
> còn nhắc tới sự hiện diện tại Bình Dương và Huế \[17\], và tồn tại một
> trang mạng xã hội riêng cho cơ sở tại Biên Hòa \[22\].
>
> Về lịch sử phát triển, do doanh nghiệp không công bố thông tin này,
> nhóm đã tái dựng mốc thời gian dựa trên ngày cấp mã số thuế của các hộ
> kinh doanh --- một nguồn minh chứng khách quan và kiểm chứng được.
>
> **Bảng 2.2. Mốc phát triển tái dựng từ dữ liệu đăng ký kinh doanh**

+:------------:+---------------------------------------------------------------+
| > **Thời     | > **Sự kiện**                                                 |
| > điểm**     |                                                               |
+--------------+---------------------------------------------------------------+
| > 24/08/2022 | > Hộ kinh doanh WAYS STATION -- GYM được cấp mã số thuế tại   |
|              | > 770 Quang Trung, cũng chính là địa chỉ trụ sở điều hành     |
|              | > hiện nay. Đây được xem là mốc khởi đầu của hệ thống         |
+--------------+---------------------------------------------------------------+
| > 2023       | > Mở địa điểm kinh doanh thứ hai tại 340 Tô Ký, Quận 12. Ngày |
|              | > 27/09/2023 thành lập hộ kinh doanh WAYS STATION GV tại 66   |
|              | > Lê Lợi                                                      |
+--------------+---------------------------------------------------------------+
| > 2023 đến   | > Chuyển đổi định vị thương hiệu từ \"Gaming và Billiards\"   |
| > 2024       | > sang \"Hệ thống Thể thao Giải trí\" đa dịch vụ, thể hiện    |
|              | > qua sự thay đổi cách tự giới thiệu trong các tin tuyển dụng |
+--------------+---------------------------------------------------------------+
| > 2024       | > Đưa vào vận hành hệ thống đặt sân cầu lông trực tuyến       |
+--------------+---------------------------------------------------------------+
| > 2024 đến   | > Ra mắt ứng dụng di động quản lý gói tập dành cho hội viên   |
| > 2025       | > phòng gym                                                   |
+--------------+---------------------------------------------------------------+
| > 03/11/2025 | > Công bố chính thức danh sách trang mạng xã hội và địa chỉ   |
|              | > cửa hàng của hệ thống                                       |
+--------------+---------------------------------------------------------------+
| > 2025 đến   | > Quy mô công bố tăng dần từ 25 lên trên 38 chi nhánh         |
| > 2026       |                                                               |
+--------------+---------------------------------------------------------------+

> *Nguồn: \[3\], \[4\], \[11\], \[13\], \[16\], \[17\].*
>
> Như vậy, chỉ trong khoảng bốn năm, Ways Station đã đi từ một điểm kinh
> doanh lên hơn ba mươi điểm. Tốc độ này chính là bối cảnh gốc của toàn
> bộ vấn đề công nghệ thông tin được phân tích ở Chương 3: **hạ tầng ứng
> dụng và dữ liệu được lắp thêm theo từng nhu cầu phát sinh, chứ không
> được thiết kế trước cho quy mô chuỗi**. Đây là hiện tượng phổ biến ở
> các doanh nghiệp tăng trưởng nhanh và không phải là lỗi quản trị,
> nhưng nếu không được xử lý thì nợ kỹ thuật sẽ tích lũy theo cấp số
> nhân cùng với số điểm kinh doanh.
>
> Về nhân sự, hồ sơ doanh nghiệp trên cổng tuyển dụng ghi nhận quy mô từ
> 50 đến 249 người có đóng bảo hiểm xã hội \[6\]. Tuy nhiên, nếu ước
> tính theo số chi nhánh và mô hình vận hành liên tục 24 giờ, với khoảng
> ba đến năm nhân sự cho mỗi ca, tổng số lao động thực tế có thể vào
> khoảng 250 đến 400 người. Con số này cần được kiểm chứng.
>
> Mô hình tổ chức lao động của Ways Station có một điểm khác biệt đáng
> chú ý: nhân viên làm **ca cố định từ 4 đến 9 giờ, không xoay ca**, và
> ứng viên được **tự chọn chi nhánh, vị trí và ca làm việc** ngay khi
> đăng ký \[2\]. Cách tổ chức này giúp tuyển dụng dễ hơn với lao động
> bán thời gian, nhưng đồng thời tạo ra một yêu cầu kỹ thuật: vì một
> nhân viên có thể làm việc tại nhiều chi nhánh, hệ thống cần một cơ chế
> định danh nhân sự tập trung thay vì danh sách riêng lẻ từng điểm.
>
> Lộ trình thăng tiến được công bố gồm ba bậc: nhân viên, trưởng ca với
> thu nhập khoảng 12 triệu đồng, và quản lý khu vực với thu nhập khoảng
> 14 triệu đồng \[2\]. Sự tồn tại sẵn của cấp quản lý khu vực là một
> thuận lợi cho việc triển khai hệ thống báo cáo phân cấp về sau.

## 2.3. Cơ cấu tổ chức

> Ways Station không công bố sơ đồ tổ chức. Nhóm đã tái dựng cơ cấu dưới
> đây dựa trên các chức danh xuất hiện trong tin tuyển dụng chính thức
> của doanh nghiệp \[2\], \[17\], \[18\]. Cần lưu ý rằng đây là sơ đồ
> suy luận, cần được xác nhận lại khi có điều kiện phỏng vấn.
>
> **Hình 2.1. Sơ đồ cơ cấu tổ chức tái dựng**
>
> ![Hình 2.1. Sơ đồ cơ cấu tổ chức tái
> dựng](media/image3.png){width="6.851388888888889in"
> height="3.605994094488189in"}
>
> Sơ đồ này cho thấy một tổ chức có cấu trúc điển hình của chuỗi bán lẻ
> dịch vụ: một khối vận hành lớn theo chiều dọc từ quản lý khu vực xuống
> tới nhân viên chi nhánh, cùng các khối chức năng hỗ trợ.
>
> Tuy nhiên, có ba đặc điểm về cơ cấu cần được nhấn mạnh vì chúng liên
> quan trực tiếp tới hai lớp năng lực mà đồ án phụ trách.
>
> Thứ nhất, **không có phòng công nghệ thông tin**. Trong toàn bộ các
> tin tuyển dụng khảo sát được, không xuất hiện bất kỳ vị trí nào thuộc
> lĩnh vực công nghệ thông tin: không có lập trình viên, không có quản
> trị hệ thống, không có quản trị cơ sở dữ liệu \[2\], \[17\], \[18\].
> Hai vị trí gần nhất với lĩnh vực này là \"nhân viên nhập liệu\" và
> \"nhân viên giám sát camera\", nhưng cả hai đều là công việc vận hành
> chứ không phải công việc kỹ thuật. Hệ quả là mọi hệ thống của doanh
> nghiệp đều phải thuê ngoài, và tiêu chí lựa chọn giải pháp bắt buộc
> phải là \"tích hợp được\" chứ không thể là \"tự phát triển\".
>
> Thứ hai, **sự tồn tại của chức danh nhân viên nhập liệu là một bằng
> chứng gián tiếp nhưng rất rõ ràng**. Việc một doanh nghiệp dịch vụ
> phải tuyển người chuyên trách nhập liệu cho thấy khâu tổng hợp dữ liệu
> giữa các hệ thống hiện đang được thực hiện thủ công bằng sức người.
> Đây là dữ kiện quan trọng nhất mà quá trình khảo sát gián tiếp thu
> được, và sẽ được phân tích chi tiết ở mục 3.2 và 3.4.
>
> Thứ ba, **bộ phận kế toán bị phân tán theo pháp nhân**. Do mỗi chi
> nhánh hoặc cụm chi nhánh là một hộ kinh doanh độc lập với mã số thuế
> riêng \[3\], \[4\], \[5\], sổ sách kế toán cũng được lập riêng cho
> từng hộ. Không tồn tại một sổ hợp nhất cho toàn hệ thống. Đây chính là
> gốc rễ của bài toán dữ liệu ở lớp (5).

## 2.4. Các quy trình nghiệp vụ chính

> Từ tài liệu công khai của doanh nghiệp, nhóm xác định được sáu quy
> trình nghiệp vụ chính. Trong đó, ba quy trình đầu liên quan trực tiếp
> tới khách hàng, quy trình thứ tư và thứ năm thuộc về vận hành nội bộ,
> và quy trình cuối cùng thuộc về quản trị nhân sự.

### 2.4.1. Quy trình đặt và thanh toán sân cầu lông

> Đây là quy trình được số hóa hoàn chỉnh nhất trong toàn bộ hoạt động
> của Ways Station, và cũng là quy trình duy nhất mà khách hàng không
> cần tiếp xúc với nhân viên.
>
> **Hình 2.2. Luồng quy trình đặt và thanh toán sân cầu lông**
>
> ![Hình 2.2. Luồng quy trình đặt và thanh toán sân cầu
> lông](media/image2.png){width="5.833333333333333in"
> height="4.895833333333333in"}
>
> *Nguồn: \[11\], \[12\].*
>
> Kèm theo quy trình này là một số quy định vận hành: khách phải thanh
> toán trước toàn bộ, lịch đã chốt không được hủy hoặc dời, mỗi sân tối
> đa 10 người, và các suất chơi cách nhau 5 phút để nhân viên dọn dẹp
> \[12\]. Trường hợp khách bận không đến được, doanh nghiệp gợi ý khách
> tự đăng nhượng suất chơi lên các nhóm trò chuyện trên Zalo hoặc
> Facebook, và không thu phí cho việc chuyển nhượng này \[12\].
>
> Quy trình này thể hiện tư duy vận hành khá tiến bộ: bằng cách chuyển
> toàn bộ khâu thanh toán ra trực tuyến, doanh nghiệp loại bỏ được nhu
> cầu bố trí thu ngân tại khu vực sân cầu lông. Tuy nhiên, chính trong
> quy trình này cũng tồn tại một mắt xích thủ công đáng chú ý, sẽ được
> phân tích ở mục 3.2.

### 2.4.2. Quy trình đăng ký và gia hạn gói tập

> Trái ngược với quy trình trên, việc đăng ký gói tập gym gần như chưa
> được số hóa. Khách hàng đến bất kỳ chi nhánh nào trong khung giờ từ 6
> giờ đến 24 giờ, được nhân viên dẫn tham quan, sau đó điền một biểu mẫu
> đơn giản gồm họ tên và số điện thoại, rồi thanh toán ngay tại quầy
> bằng tiền mặt, mã VietQR hoặc chuyển khoản. Doanh nghiệp không chấp
> nhận thẻ tín dụng. Sau khi thanh toán, khách được đăng ký nhận diện
> khuôn mặt để có thể ra vào 24 giờ, và gói tập được kích hoạt trên ứng
> dụng di động \[8\].
>
> Chính trang thông tin của doanh nghiệp ghi rõ rằng *\"đăng ký và gia
> hạn trực tuyến hiện đang được nghiên cứu, hiện tại việc đăng ký và gia
> hạn được thực hiện tại quầy\"* \[13\]. Cần lưu ý rằng gói tập của Ways
> Station được dùng chung cho mọi chi nhánh \[8\], nghĩa là về mặt kỹ
> thuật, hồ sơ hội viên bắt buộc phải được lưu tập trung chứ không thể
> lưu cục bộ tại từng điểm. Như vậy, hạ tầng dữ liệu cần thiết đã tồn
> tại ở mức độ nào đó, nhưng chưa được khai thác để phục vụ giao dịch
> trực tuyến.

### 2.4.3. Quy trình kiểm soát ra vào bằng nhận diện khuôn mặt

> Hội viên khi đến phòng tập sẽ được camera nhận diện khuôn mặt, hệ
> thống đối chiếu với hồ sơ hội viên và trạng thái gói tập, sau đó mở
> cửa. Lịch sử ra vào được ghi nhận và hiển thị trên ứng dụng di động
> \[8\].
>
> Cơ chế này giải quyết được một bài toán vận hành thực tế: phòng tập mở
> cửa 24 giờ nhưng không thể bố trí nhân viên trực suốt đêm. Tuy nhiên,
> xét từ góc độ quản trị dữ liệu, đây là quy trình phát sinh nghĩa vụ
> pháp lý nặng nhất trong toàn bộ hoạt động của doanh nghiệp, vì dữ liệu
> khuôn mặt thuộc nhóm dữ liệu cá nhân nhạy cảm theo quy định hiện hành
> \[23\]. Nội dung này được phân tích tại mục 3.3.

### 2.4.4. Quy trình bán hàng tại quầy

> Đối với dịch vụ gaming và billiards, khách đến quầy, nhân viên thu
> ngân mở máy hoặc mở bàn và bắt đầu tính giờ. Khi khách kết thúc, thu
> ngân tính tiền theo khung giờ tương ứng và thu bằng tiền mặt hoặc mã
> VietQR. Doanh nghiệp cho phép mang đồ ăn uống từ ngoài vào nhưng thu
> phụ phí 5.000 đồng \[9\], \[10\].
>
> Điểm cần lưu ý là trong quy trình này, **khách hàng hoàn toàn vô
> danh**. Hệ thống chỉ ghi nhận một giao dịch và một khoảng thời gian sử
> dụng, không gắn với bất kỳ danh tính nào. Một hội viên gym thân thiết
> của Ways Station khi sang chơi billiards tại chính chi nhánh đó vẫn
> chỉ là một khách vãng lai đối với hệ thống.

### 2.4.5. Quy trình chốt ca và tổng hợp doanh thu

> Đây là quy trình mà nhóm không quan sát trực tiếp được, nên phần mô tả
> dưới đây mang tính suy luận, dựa trên hai dữ kiện: doanh nghiệp có
> tuyển vị trí nhân viên nhập liệu \[18\], và mỗi chi nhánh thuộc một
> pháp nhân riêng có sổ sách riêng \[3\], \[4\].
>
> Theo suy luận đó, trưởng ca tại mỗi chi nhánh chốt doanh thu cuối ca
> và gửi số liệu về văn phòng, nhiều khả năng dưới dạng tệp, ảnh chụp
> hoặc tin nhắn. Nhân viên nhập liệu tại văn phòng nhập các số liệu này
> vào một bảng tổng hợp chung. Kế toán của từng hộ kinh doanh lên sổ
> riêng cho pháp nhân của mình. Cuối cùng, ban điều hành nhận được báo
> cáo hợp nhất sau khi các bước trên hoàn tất.
>
> Nếu suy luận này chính xác, thì mắt xích quan trọng nhất trong toàn bộ
> hệ thống thông tin của Ways Station hiện nay là **một con người ngồi
> nhập số liệu**, chứ không phải một phần mềm.

### 2.4.6. Quy trình tuyển dụng và phân ca

> Ứng viên truy cập trang tuyển dụng, tương tác với một chatbot trên nền
> tảng nhắn tin, điền biểu mẫu trong đó tự chọn chi nhánh, vị trí và ca
> làm việc mong muốn, sau đó tham gia phỏng vấn trực tuyến, được đào tạo
> và trải qua thời gian thử việc trước khi trở thành nhân viên chính
> thức \[2\], \[10\].
>
> Đây là quy trình được số hóa ở mức khá, cho thấy doanh nghiệp không hề
> xa lạ với việc ứng dụng công cụ trực tuyến. Vấn đề nằm ở chỗ mức độ số
> hóa này chưa lan tới các quy trình cốt lõi của hoạt động kinh doanh.

# CHƯƠNG 3. PHÂN TÍCH HIỆN TRẠNG VÀ CÁC VẤN ĐỀ TỒN TẠI

## 3.1. Bản đồ hệ thống công nghệ thông tin hiện có

> Trước khi phân tích các vấn đề, cần liệt kê những gì Ways Station đang
> có. Điều này quan trọng, vì kết luận của chương này không phải là
> doanh nghiệp thiếu công nghệ.
>
> **Bảng 3.1. Các hệ thống công nghệ thông tin hiện có**

+:---------:+------------+-------------------------+--------------------+
| > **Hệ    | > **Chức   | > **Nhà cung cấp**      | > **Tình trạng**   |
| > thống** | > năng**   |                         |                    |
+-----------+------------+-------------------------+--------------------+
| > Ứng     | > Theo dõi | > Nền tảng bên thứ ba   | > Đang hoạt động,  |
| > dụng di | > gói tập, | > (định danh gói ứng    | > chưa hỗ trợ      |
| > động    | > xem lịch | > dụng cho thấy do một  | > thanh toán trực  |
| > quản lý | > sử ra    | > đơn vị chuyên cung    | > tuyến, được mô   |
| > gói tập | > vào      | > cấp giải pháp phòng   | > tả là đang trong |
|           |            | > tập phát triển)       | > giai đoạn thử    |
|           |            |                         | > nghiệm           |
+-----------+------------+-------------------------+--------------------+
| > Hệ      | > Đặt và   | > Chưa xác định         | > Đang hoạt động   |
| > thống   | > thanh    |                         | > ổn định          |
| > đặt sân | > toán sân |                         |                    |
| > trực    | > cầu lông |                         |                    |
| > tuyến   |            |                         |                    |
+-----------+------------+-------------------------+--------------------+
| > Hệ      | > Kiểm     | > Chưa xác định         | > Đang hoạt động   |
| > thống   | > soát ra  |                         |                    |
| > nhận    | > vào      |                         |                    |
| > diện    | > phòng    |                         |                    |
| > khuôn   | > tập 24   |                         |                    |
| > mặt     | > giờ      |                         |                    |
+-----------+------------+-------------------------+--------------------+
| > Phần    | > Tính     | > Chưa xác định         | > Đang hoạt động   |
| > mềm     | > giờ, thu |                         |                    |
| > quầy    | > tiền tại |                         |                    |
| > thu     | > chi      |                         |                    |
| > ngân    | > nhánh    |                         |                    |
+-----------+------------+-------------------------+--------------------+
| > Website | > Giới     | > WordPress và Webcake  | > Đang hoạt động,  |
| > và các  | > thiệu,   |                         | > có trang lỗi     |
| > trang   | > công bố  |                         |                    |
| > landing | > giá và   |                         |                    |
| > page    | > địa chỉ  |                         |                    |
+-----------+------------+-------------------------+--------------------+
| > Kênh    | > Tiếp     | > Nền tảng bên ngoài    | > Phân tán nhiều   |
| > mạng xã | > thị, hỗ  |                         | > trang            |
| > hội     | > trợ      |                         |                    |
|           | > khách    |                         |                    |
|           | > hàng,    |                         |                    |
|           | > chuyển   |                         |                    |
|           | > nhượng   |                         |                    |
|           | > suất     |                         |                    |
|           | > chơi     |                         |                    |
+-----------+------------+-------------------------+--------------------+
| > Bảng    | > Hợp nhất | > Nội bộ, nhiều khả     | > Do nhân viên     |
| > tổng    | > số liệu  | > năng là bảng tính     | > nhập liệu vận    |
| > hợp     | > toàn hệ  |                         | > hành thủ công    |
| > doanh   | > thống    |                         |                    |
| > thu     |            |                         |                    |
+-----------+------------+-------------------------+--------------------+

> *Nguồn: \[8\], \[9\], \[10\], \[11\], \[13\], \[14\], \[15\], \[16\],
> \[18\].*
>
> Có thể thấy Ways Station đã đầu tư một lượng công nghệ không nhỏ so
> với quy mô một doanh nghiệp dịch vụ vừa: ứng dụng di động cho hội
> viên, hệ thống đặt chỗ trực tuyến có thanh toán, nhận diện sinh trắc
> học, thanh toán bằng mã QR. Vấn đề, như sẽ phân tích dưới đây, không
> nằm ở việc thiếu công nghệ mà nằm ở việc **các mảnh công nghệ đó không
> liên kết với nhau**.

## 3.2. Các điểm nghẽn trong vận hành

> Qua khảo sát, nhóm xác định được sáu điểm nghẽn chính.
>
> **Điểm nghẽn nghiêm trọng nhất là việc hợp nhất doanh thu vẫn phải làm
> bằng sức người.** Với hơn 38 chi nhánh, sáu dòng dịch vụ và nhiều pháp
> nhân độc lập, để có được một con số doanh thu toàn hệ thống, doanh
> nghiệp cần một nhân sự chuyên trách ngồi nhập lại số liệu \[18\]. Điều
> này không chỉ tốn chi phí, mà còn khiến báo cáo luôn trễ so với thực
> tế và tiềm ẩn sai sót do thao tác thủ công.
>
> **Điểm nghẽn thứ hai nằm ở việc hội viên không thể gia hạn gói tập
> trực tuyến.** Phòng tập mở cửa 24 giờ, nhưng muốn gia hạn thì hội viên
> phải đến quầy trong khung 6 giờ đến 24 giờ \[8\], \[13\]. Đây là một
> nghịch lý về trải nghiệm: khách hàng có thể vào tập lúc 3 giờ sáng nhờ
> nhận diện khuôn mặt, nhưng không thể trả tiền cho tháng tiếp theo vào
> thời điểm đó. Mỗi lần gia hạn là một lần khách phải chủ động sắp xếp
> thời gian, và mỗi lần như vậy đều là một cơ hội để khách bỏ cuộc.
>
> **Điểm nghẽn thứ ba là việc đối soát thanh toán phụ thuộc vào thao tác
> của khách hàng.** Trong quy trình đặt sân, nếu khách chọn chuyển khoản
> thủ công thay vì quét mã QR, họ bắt buộc phải ghi đúng mã đơn hàng vào
> nội dung chuyển khoản. Chính trang hướng dẫn của doanh nghiệp phải đưa
> ra cảnh báo về việc này để tránh trường hợp hệ thống không xác nhận
> được thanh toán \[11\]. Nói cách khác, tính đúng đắn của một giao dịch
> tài chính đang được đặt vào tay người dùng cuối. Mỗi trường hợp sai
> sót đều phải xử lý thủ công qua đường dây nóng.
>
> **Điểm nghẽn thứ tư là sự tồn tại của hai trải nghiệm thanh toán mâu
> thuẫn trong cùng một cơ sở**, như đã trình bày ở mục 2.1.
>
> **Điểm nghẽn thứ năm, và cũng là điểm bộc lộ rõ nhất sự thiếu vắng lớp
> tích hợp, là việc các năng lực kỹ thuật không được chia sẻ giữa các
> ứng dụng.** Hệ thống đặt sân trực tuyến đã thanh toán qua mạng được từ
> năm 2024 \[11\], trong khi ứng dụng quản lý gói tập ra mắt sau đó vẫn
> chưa có tính năng này \[13\]. Nếu tồn tại một lớp dịch vụ thanh toán
> dùng chung, năng lực đã xây dựng cho hệ thống đặt sân hoàn toàn có thể
> được ứng dụng gym sử dụng lại. Việc mỗi hệ thống phải tự xây dựng lại
> từ đầu là triệu chứng điển hình của kiến trúc thiếu tích hợp.
>
> **Điểm nghẽn thứ sáu liên quan tới việc xử lý nhượng suất chơi.** Do
> quy định không cho hủy hoặc dời lịch, khách bận đột xuất phải tự đăng
> bài lên các nhóm trò chuyện để tìm người thay thế \[12\]. Việc này
> diễn ra hoàn toàn bên ngoài hệ thống của doanh nghiệp, khiến Ways
> Station không kiểm soát được ai thực sự đang sử dụng sân, đồng thời bỏ
> lỡ cơ hội biến một nhu cầu có thật thành một tính năng.

## 3.3. Các rủi ro tiềm ẩn

> Bên cạnh các điểm nghẽn đang diễn ra hằng ngày, hiện trạng công nghệ
> của Ways Station còn tiềm ẩn một số rủi ro có thể gây hậu quả lớn hơn.
>
> **Rủi ro pháp lý liên quan tới dữ liệu cá nhân nhạy cảm** là rủi ro có
> mức độ tác động cao nhất. Việc sử dụng nhận diện khuôn mặt để kiểm
> soát ra vào \[8\] đồng nghĩa với việc doanh nghiệp đang thu thập và
> lưu trữ dữ liệu sinh trắc học của toàn bộ hội viên. Theo Nghị định
> 13/2023/NĐ-CP, dữ liệu sinh trắc học thuộc nhóm dữ liệu cá nhân nhạy
> cảm, kéo theo các nghĩa vụ chặt chẽ hơn về việc lấy sự đồng ý, thông
> báo xử lý dữ liệu, đánh giá tác động và quy định thời hạn lưu trữ
> \[23\]. Luật Bảo vệ dữ liệu cá nhân tiếp tục bổ sung các quyền của chủ
> thể dữ liệu, trong đó có quyền yêu cầu xóa dữ liệu của mình \[24\].
>
> Điều đáng lưu ý là ngay cả khi dữ liệu này được lưu trên hệ thống của
> nhà cung cấp bên thứ ba, Ways Station vẫn giữ vai trò Bên Kiểm soát dữ
> liệu và **không thể chuyển giao trách nhiệm pháp lý** cho nhà cung
> cấp. Trong khi đó, doanh nghiệp lại không có nhân sự công nghệ thông
> tin chuyên trách để theo dõi vấn đề này.
>
> **Rủi ro phụ thuộc nhà cung cấp** là rủi ro có khả năng xảy ra cao
> nhất. Ứng dụng quản lý gói tập được xây dựng trên nền tảng của một đơn
> vị bên ngoài \[14\], \[15\]. Toàn bộ hồ sơ hội viên, lịch sử ra vào và
> dữ liệu sinh trắc học nằm trong hệ thống này. Nếu nhà cung cấp không
> mở giao diện lập trình để trích xuất dữ liệu, hoặc thay đổi chính
> sách, hoặc ngừng cung cấp dịch vụ, Ways Station sẽ ở vào thế bị động.
> Với một doanh nghiệp không có nhân sự kỹ thuật nội bộ, khả năng ứng
> phó trong tình huống đó là rất hạn chế.
>
> **Rủi ro mạo danh thương hiệu** đã thực sự xảy ra, thể hiện qua việc
> doanh nghiệp phải đăng bài công bố danh sách trang mạng xã hội chính
> thức \[16\]. Trong bối cảnh khách hàng được hướng dẫn chuyển khoản để
> thanh toán, việc tồn tại các trang mạo danh tạo ra nguy cơ thực tế là
> khách chuyển tiền vào tài khoản giả.
>
> **Rủi ro dữ liệu địa chỉ lạc hậu về mặt hành chính** cũng đã hiện hữu.
> So sánh hai nguồn về cùng một địa chỉ trụ sở cho thấy nguồn cũ ghi
> \"770 Quang Trung, Phường 8, Quận Gò Vấp\" \[7\], trong khi dữ liệu
> tra cứu thuế cập nhật tháng 8 năm 2026 ghi \"770 Quang Trung, Phường
> Thông Tây Hội, Thành phố Hồ Chí Minh\" \[3\]. Sau đợt sắp xếp đơn vị
> hành chính, toàn bộ dữ liệu địa chỉ của hơn 38 chi nhánh trên mọi
> website, hóa đơn và hệ thống nội bộ đều cần được chuẩn hóa lại. Đây là
> một công việc thuần túy thuộc lớp (5) và nếu không có danh mục dữ liệu
> chi nhánh tập trung thì việc rà soát sẽ rất tốn công.
>
> **Rủi ro tập trung tri thức vào cá nhân** phát sinh từ chính điểm
> nghẽn thứ nhất. Quy trình hợp nhất dữ liệu hiện nằm trong hiểu biết
> của nhân viên nhập liệu. Nếu người này nghỉ việc, dòng chảy báo cáo
> của toàn hệ thống có thể bị gián đoạn cho tới khi có người khác nắm
> được công việc.
>
> Cuối cùng, cần nhắc tới **rào cản pháp lý khi hợp nhất dữ liệu giữa
> các pháp nhân**. Do các hộ kinh doanh là những pháp nhân độc lập với
> chủ hộ khác nhau \[3\], \[4\], việc gộp dữ liệu khách hàng và doanh
> thu của các hộ này về một nơi cần có căn cứ pháp lý rõ ràng, đặc biệt
> khi dữ liệu đó bao gồm dữ liệu cá nhân. Đây không phải là bài toán kỹ
> thuật, và nếu không được giải quyết trước thì mọi thiết kế kỹ thuật
> đều có thể phải làm lại.

## 3.4. Chi phí ẩn

> Phần này ước tính những khoản chi phí mà doanh nghiệp đang thực trả
> nhưng không xuất hiện dưới dạng một khoản mục nào trong sổ sách. Cần
> nhấn mạnh rằng các con số dưới đây là **ước tính dựa trên giả định của
> nhóm**, được trình bày nhằm minh họa quy mô vấn đề chứ không phải số
> liệu thực tế của doanh nghiệp. Các giả định sử dụng được ghi rõ để có
> thể thay thế bằng số thật khi khảo sát trực tiếp.
>
> **Bảng 3.2. Ước tính chi phí ẩn hằng năm**

+:-----------------:+-------------------------------------+-----------+
| > **Khoản mục**   | > **Giả định sử dụng**              | > **Ước   |
|                   |                                     | > tính    |
|                   |                                     | > mỗi     |
|                   |                                     | > năm**   |
+-------------------+-------------------------------------+-----------+
| > Lương nhân sự   | > Một nhân viên toàn thời gian, thu | > Khoảng  |
| > chuyên trách    | > nhập khoảng 8 triệu đồng mỗi      | > 96      |
| > nhập liệu       | > tháng                             | > triệu   |
|                   |                                     | > đồng    |
+-------------------+-------------------------------------+-----------+
| > Thời gian       | > 38 chi nhánh, 3 ca mỗi ngày, 20   | > Khoảng  |
| > trưởng ca tổng  | > phút mỗi ca, đơn giá lao động     | > 410     |
| > hợp và gửi số   | > khoảng 30.000 đồng mỗi giờ        | > triệu   |
| > liệu            |                                     | > đồng    |
+-------------------+-------------------------------------+-----------+
| > Xử lý giao dịch | > 3 phần trăm số đơn đặt sân sai    | > Khoảng  |
| > treo do sai nội | > nội dung, mỗi trường hợp mất      | > 40 đến  |
| > dung chuyển     | > khoảng 10 phút xử lý qua đường    | > 80      |
| > khoản           | > dây nóng                          | > triệu   |
|                   |                                     | > đồng    |
+-------------------+-------------------------------------+-----------+
| > Doanh thu mất   | > Chưa đủ dữ liệu để ước tính, cần  | > Chưa    |
| > do không gia    | > số lượng hội viên thực tế         | > xác     |
| > hạn trực tuyến  |                                     | > định    |
| > được            |                                     |           |
+-------------------+-------------------------------------+-----------+
| > Chi phí cơ hội  | > Không lượng hóa được bằng tiền    | > Chưa    |
| > của việc ra     |                                     | > xác     |
| > quyết định trên |                                     | > định    |
| > số liệu trễ     |                                     |           |
+-------------------+-------------------------------------+-----------+
| > Chi phí tiếp    | > Mã ưu đãi được phát hành nhưng    | > Chưa    |
| > thị không đo    | > không gắn được với hồ sơ khách    | > xác     |
| > được hiệu quả   | > hàng                              | > định    |
+-------------------+-------------------------------------+-----------+

> Hai khoản mục đầu tiên, vốn có thể ước tính tương đối, đã lên tới
> khoảng **500 triệu đồng mỗi năm**. Điều đáng nói không nằm ở con số
> tuyệt đối, mà ở bản chất của khoản chi này: đây là tiền được chi ra
> **chỉ để di chuyển số liệu từ nơi này sang nơi khác**, không tạo ra
> thêm bất kỳ giá trị nào cho khách hàng hay cho doanh nghiệp. Trong
> phân tích đầu tư hạ tầng, đây thường là luận cứ thuyết phục nhất, vì
> nó cho phép so sánh trực tiếp chi phí duy trì hiện trạng với chi phí
> đầu tư thay đổi.
>
> Ba khoản mục cuối chưa lượng hóa được, nhưng cần được nêu ra vì chúng
> có thể lớn hơn ba khoản đầu. Đặc biệt là chi phí cơ hội: khi ban điều
> hành phải ra quyết định mở hay đóng một chi nhánh, hay điều chỉnh giá
> dịch vụ, dựa trên số liệu của tháng trước thay vì của tuần này, cái
> giá phải trả cho một quyết định sai có thể vượt xa toàn bộ chi phí
> nhập liệu.

## 3.5. Tình trạng phân mảnh dữ liệu

> Phần này tổng hợp lại vấn đề trung tâm mà toàn bộ chương đã dẫn tới.
>
> **Hình 3.1. Sơ đồ phân mảnh dữ liệu hiện tại**
>
> ![Hình 3.1. Sơ đồ phân mảnh dữ liệu hiện
> tại](media/image1.png){width="6.851388888888889in"
> height="3.689209317585302in"}
>
> Sơ đồ trên cho thấy một thực tế: **thành phần đóng vai trò lớp tích
> hợp trong kiến trúc hiện tại của Ways Station là một con người, không
> phải một hệ thống**. Đây là cách diễn đạt trực quan nhất cho việc
> thiếu vắng lớp năng lực (4).
>
> Hệ quả cụ thể của tình trạng này có thể thấy rõ khi xem xét một khách
> hàng giả định. Giả sử một người vừa là hội viên phòng tập, vừa thường
> xuyên đặt sân cầu lông, và thỉnh thoảng chơi billiards tại cùng một
> chi nhánh. Trong hệ thống của Ways Station, người này tồn tại dưới ba
> hồ sơ hoàn toàn tách biệt: một hồ sơ hội viên kèm dữ liệu khuôn mặt
> trong ứng dụng gym, một bản ghi họ tên và số điện thoại phải nhập lại
> mỗi lần đặt sân, và một chuỗi giao dịch vô danh tại quầy billiards.
> Không có bất kỳ liên kết nào giữa ba hồ sơ này.
>
> Từ đó, doanh nghiệp không thể trả lời những câu hỏi vốn rất cơ bản đối
> với một chuỗi dịch vụ:

- Bao nhiêu phần trăm hội viên phòng tập cũng sử dụng dịch vụ cầu lông?

- Những hội viên nào sắp hết hạn gói tập mà tháng này không đến tập lần
  nào, để chủ động liên hệ?

- Đợt phát hành mã ưu đãi vừa rồi mang về bao nhiêu khách mới và bao
  nhiêu khách cũ?

- Chi nhánh nào thực sự có lãi sau khi trừ chi phí, tính trên toàn hệ
  thống và theo từng ngày?

> Cần lưu ý rằng sự phân mảnh này diễn ra ở ba tầng khác nhau, với mức
> độ khó xử lý tăng dần. Tầng thứ nhất là phân mảnh kỹ thuật, tức bốn
> ứng dụng không nói chuyện được với nhau; đây là tầng dễ xử lý nhất,
> thuộc phạm vi lớp (4). Tầng thứ hai là phân mảnh theo pháp nhân, do mô
> hình nhiều hộ kinh doanh; tầng này đòi hỏi giải quyết cả về mặt pháp
> lý lẫn kỹ thuật, thuộc phạm vi lớp (5). Tầng thứ ba là phân mảnh theo
> kênh tiếp xúc khách hàng, do các trang mạng xã hội phát triển tự phát
> theo từng chi nhánh; tầng này thuộc về quy hoạch kênh tiếp thị nhiều
> hơn là công nghệ.
>
> Tóm lại, vấn đề của Ways Station không phải là thiếu công nghệ. Doanh
> nghiệp đã có ứng dụng di động, có hệ thống đặt chỗ trực tuyến, có nhận
> diện sinh trắc học, có thanh toán bằng mã QR. Vấn đề là **những thành
> phần đó không được nối với nhau, và không tồn tại nơi nào lưu giữ bức
> tranh toàn hệ thống**. Đó chính xác là định nghĩa của việc thiếu lớp
> năng lực Nền tảng Ứng dụng và Tích hợp, cùng lớp Nền tảng Dữ liệu.

# CHƯƠNG 4. ĐỐI TƯỢNG SỬ DỤNG VÀ MỨC ĐỘ SỐ HÓA

## 4.1. Thang đánh giá mức độ số hóa

> Để đánh giá hiện trạng một cách nhất quán giữa các nhóm người dùng
> khác nhau, nhóm sử dụng thang năm mức dưới đây. Thang này được xây
> dựng dựa trên tinh thần của mục \"Mức độ trưởng thành\" trong khung
> phân tích lớp năng lực, điều chỉnh cho phù hợp với đặc thù một doanh
> nghiệp dịch vụ.
>
> **Bảng 4.1. Thang đánh giá mức độ số hóa**

+:---------:+-------------+---------------------------------------------------+
| > **Mức** | > **Tên     | > **Đặc trưng nhận biết**                         |
|           | > gọi**     |                                                   |
+-----------+-------------+---------------------------------------------------+
| > 1       | > Thủ công  | > Công việc thực hiện bằng giấy tờ, lời nói hoặc  |
|           |             | > tin nhắn; không có hệ thống hỗ trợ              |
+-----------+-------------+---------------------------------------------------+
| > 2       | > Số hóa    | > Có phần mềm nhưng sử dụng độc lập; dữ liệu phải |
|           | > rời rạc   | > nhập tay khi chuyển giữa các hệ thống           |
+-----------+-------------+---------------------------------------------------+
| > 3       | > Số hóa    | > Mỗi nghiệp vụ có hệ thống riêng vận hành tốt,   |
|           | > theo chức | > nhưng các hệ thống chưa kết nối với nhau        |
|           | > năng      |                                                   |
+-----------+-------------+---------------------------------------------------+
| > 4       | > Tích hợp  | > Các hệ thống trao đổi dữ liệu tự động; tồn tại  |
|           |             | > nguồn dữ liệu dùng chung                        |
+-----------+-------------+---------------------------------------------------+
| > 5       | > Dựa trên  | > Quyết định vận hành được đưa ra dựa trên dữ     |
|           | > dữ liệu   | > liệu cập nhật theo thời gian thực               |
+-----------+-------------+---------------------------------------------------+

## 4.2. Nhóm người dùng nội bộ

> Về phía nội bộ, có thể chia thành chín nhóm người dùng với vai trò và
> mức độ số hóa khác nhau.
>
> **Bảng 4.2. Mức độ số hóa của các nhóm người dùng nội bộ**

+:-----------:+----------------+----------+--------------------+---------+
| > **Nhóm    | > **Vai trò    | > **Số   | > **Công cụ đang   | > **Mức |
| > người     | > đối với hệ   | > lượng  | > sử dụng**        | > số    |
| > dùng**    | > thống**      | > ước    |                    | > hóa** |
|             |                | > tính** |                    |         |
+-------------+----------------+----------+--------------------+---------+
| > Ban điều  | > Ra quyết     | > 3 đến  | > Bảng tổng hợp do | > 1     |
| > hành      | > định, sử     | > 5      | > nhân viên nhập   |         |
|             | > dụng báo cáo | > người  | > liệu lập         |         |
+-------------+----------------+----------+--------------------+---------+
| > Quản lý   | > Giám sát cụm | > 4 đến  | > Báo cáo tổng hợp | > 1     |
| > khu vực   | > chi nhánh    | > 6      | > và hệ thống      |         |
|             |                | > người  | > camera           |         |
+-------------+----------------+----------+--------------------+---------+
| > Trưởng ca | > Vận hành     | > Khoảng | > Sổ ghi chép và   | > 1     |
|             | > trực tiếp    | > 38     | > tin nhắn         |         |
|             | > tại chi      | > người  |                    |         |
|             | > nhánh        |          |                    |         |
+-------------+----------------+----------+--------------------+---------+
| > Nhân viên | > Ghi nhận     | > 40 đến | > Phần mềm quầy    | > 2     |
| > thu ngân  | > giao dịch    | > 80     |                    |         |
|             | > tại quầy     | > người  |                    |         |
+-------------+----------------+----------+--------------------+---------+
| > Nhân viên | > Hợp nhất dữ  | > 1 đến  | > Bảng tính        | > 2     |
| > nhập liệu | > liệu toàn hệ | > 2      |                    |         |
|             | > thống        | > người  |                    |         |
+-------------+----------------+----------+--------------------+---------+
| > Kế toán   | > Lập sổ sách  | > 3 đến  | > Phần mềm kế toán | > 2     |
| > các hộ    | > theo từng    | > 6      |                    |         |
| > kinh      | > pháp nhân    | > người  |                    |         |
| > doanh     |                |          |                    |         |
+-------------+----------------+----------+--------------------+---------+
| > Bộ phận   | > Vận hành     | > 3 đến  | > Mạng xã hội,     | > 2     |
| > tiếp thị  | > kênh, phát   | > 5      | > công cụ landing  |         |
|             | > hành ưu đãi  | > người  | > page             |         |
+-------------+----------------+----------+--------------------+---------+
| > Bộ phận   | > Tuyển dụng,  | > 2 đến  | > Biểu mẫu trực    | > 3     |
| > nhân sự   | > phân ca      | > 3      | > tuyến, chatbot   |         |
|             |                | > người  |                    |         |
+-------------+----------------+----------+--------------------+---------+
| > Nhân viên | > Giám sát an  | > 2 đến  | > Hệ thống camera  | > 3     |
| > giám sát  | > ninh từ xa   | > 4      |                    |         |
| > camera    |                | > người  |                    |         |
+-------------+----------------+----------+--------------------+---------+

> *Ghi chú: số lượng nhân sự là ước tính của nhóm, chưa được kiểm
> chứng.*
>
> Ba nhóm cần được phân tích kỹ hơn.
>
> **Trưởng ca** là nhóm người dùng quan trọng nhất trong toàn bộ hệ
> thống nội bộ, vì đây là cấp trực tiếp tạo ra dữ liệu gốc. Mỗi chi
> nhánh có một trưởng ca cho mỗi ca làm việc, và người này chịu trách
> nhiệm chốt doanh thu cuối ca. Nếu khâu này còn thủ công thì mọi lớp
> phía trên đều nhận được dữ liệu chậm và có nguy cơ sai. Đây cũng là
> nhóm nên được ưu tiên trong giai đoạn đầu triển khai, vì cải thiện ở
> đây tạo hiệu ứng lan tỏa lên toàn bộ chuỗi báo cáo.
>
> **Nhân viên nhập liệu** là một trường hợp đặc biệt: đây là nhóm người
> dùng mà mục tiêu của dự án là **loại bỏ chính công việc hiện tại của
> họ**. Cần lưu ý rằng điều này không đồng nghĩa với cắt giảm nhân sự;
> thời gian được giải phóng hoàn toàn có thể chuyển sang các công việc
> phân tích có giá trị cao hơn. Tuy nhiên, đây là yếu tố cần được truyền
> thông cẩn thận khi triển khai, vì sự phản kháng từ người trực tiếp bị
> ảnh hưởng là một rủi ro thực tế của mọi dự án tự động hóa.
>
> **Ban điều hành và quản lý khu vực** hiện đang ở mức số hóa thấp nhất,
> dù đây là những người có nhu cầu thông tin cao nhất. Họ ra các quyết
> định có giá trị lớn --- mở hay đóng chi nhánh, điều chỉnh giá, phân bổ
> ngân sách tiếp thị --- nhưng lại làm việc trên số liệu đã qua nhiều
> bước xử lý thủ công và có độ trễ đáng kể.

## 4.3. Nhóm người dùng bên ngoài

> Về phía khách hàng và các đối tượng bên ngoài, có thể chia thành sáu
> nhóm.
>
> **Bảng 4.3. Mức độ số hóa của các nhóm người dùng bên ngoài**

+:-----------:+--------------------------+---------+------------------------+
| > **Nhóm    | > **Cách tương tác hiện  | > **Mức | > **Nhu cầu chưa được  |
| > người     | > nay**                  | > số    | > đáp ứng**            |
| > dùng**    |                          | > hóa** |                        |
+-------------+--------------------------+---------+------------------------+
| > Hội viên  | > Đăng ký tại quầy, ra   | > 2     | > Gia hạn trực tuyến,  |
| > phòng gym | > vào bằng nhận diện     |         | > xem lịch sử tập      |
|             | > khuôn mặt, xem gói tập |         | > luyện đầy đủ, ưu đãi |
|             | > trên ứng dụng, không   |         | > theo mức độ gắn bó   |
|             | > thanh toán trực tuyến  |         |                        |
|             | > được                   |         |                        |
+-------------+--------------------------+---------+------------------------+
| > Khách đặt | > Tự phục vụ hoàn toàn   | > 3     | > Không phải nhập lại  |
| > sân cầu   | > qua mạng, không tiếp   |         | > thông tin mỗi lần,   |
| > lông      | > xúc nhân viên          |         | > được hủy hoặc dời    |
|             |                          |         | > lịch, nhượng suất    |
|             |                          |         | > chơi ngay trong hệ   |
|             |                          |         | > thống                |
+-------------+--------------------------+---------+------------------------+
| > Khách     | > Đến quầy, giao dịch    | > 1     | > Tích lũy điểm và     |
| > gaming và | > hoàn toàn vô danh      |         | > nhận ưu đãi, hiện    |
| > billiards |                          |         | > không thực hiện được |
|             |                          |         | > vì không có danh     |
|             |                          |         | > tính                 |
+-------------+--------------------------+---------+------------------------+
| > Khách sử  | > Chưa xác định          | > Chưa  | > Cần khảo sát bổ sung |
| > dụng      |                          | > xác   |                        |
| > không     |                          | > định  |                        |
| > gian học  |                          |         |                        |
| > và làm    |                          |         |                        |
| > việc      |                          |         |                        |
+-------------+--------------------------+---------+------------------------+
| > Huấn      | > Được vào phòng tập     | > 1     | > Nhóm hiện diện hằng  |
| > luyện     | > miễn phí, không có hệ  |         | > ngày nhưng hoàn toàn |
| > viên tự   | > thống quản lý          |         | > nằm ngoài mọi hệ     |
| > do        |                          |         | > thống                |
+-------------+--------------------------+---------+------------------------+
| > Ứng viên  | > Biểu mẫu trực tuyến và | > 3     | > Nằm ngoài phạm vi đồ |
| > tuyển     | > chatbot                |         | > án                   |
| > dụng      |                          |         |                        |
+-------------+--------------------------+---------+------------------------+

> Trường hợp **huấn luyện viên tự do** đáng được nhắc tới như một điểm
> mù. Ways Station không sử dụng huấn luyện viên cơ hữu mà cho phép các
> huấn luyện viên tự do vào làm việc với hội viên miễn phí, kèm điều
> kiện không được chào mời hay làm phiền các hội viên khác \[19\]. Đây
> là một nhóm có mặt thường xuyên tại cơ sở, có ảnh hưởng trực tiếp tới
> trải nghiệm của hội viên, nhưng doanh nghiệp không có bất kỳ dữ liệu
> nào về họ.

## 4.4. Đánh giá chung về mức độ trưởng thành số

> Tổng hợp các nội dung đã phân tích, nhóm đưa ra đánh giá theo năm
> chiều như sau. Về số hóa hoạt động bán hàng, mức độ không đồng đều:
> dịch vụ cầu lông đạt mức 3, gym đạt mức 2, trong khi gaming và
> billiards chỉ ở mức 1. Về số hóa vận hành nội bộ, mức đánh giá là 1,
> do khâu chốt ca và hợp nhất doanh thu vẫn hoàn toàn thủ công. Về khả
> năng tích hợp giữa các hệ thống, mức đánh giá cũng là 1, vì thành phần
> tích hợp duy nhất là con người. Về năng lực khai thác dữ liệu, mức 1,
> do chưa tồn tại kho dữ liệu hay báo cáo tự động. Về quản trị dữ liệu
> cá nhân, mức 1, vì doanh nghiệp đang xử lý dữ liệu sinh trắc học nhưng
> chưa có khung quản trị tương ứng.
>
> Bình quân các chiều trên, mức độ trưởng thành số của Ways Station vào
> khoảng **1,6 trên thang 5**, tương ứng với giai đoạn \"số hóa rời
> rạc\": đã có công cụ nhưng chưa thành hệ thống.
>
> Từ bảng đánh giá ở hai mục trên, có thể rút ra một nhận xét mà nhóm
> cho là kết luận quan trọng nhất của chương này. **Nhóm người dùng có
> mức số hóa cao nhất trong toàn bộ hệ sinh thái Ways Station là khách
> hàng đặt sân cầu lông, đạt mức 3 với khả năng tự phục vụ hoàn toàn.
> Trong khi đó, nhóm có mức số hóa thấp nhất lại là ban điều hành và
> trưởng ca, chỉ ở mức 1.**
>
> Nói cách khác, doanh nghiệp đã số hóa phần hướng ra khách hàng nhưng
> chưa số hóa phần hướng vào bên trong. Điều này hoàn toàn dễ hiểu về
> mặt động cơ kinh doanh, vì phần hướng ra ngoài mang lại hiệu quả nhìn
> thấy được ngay. Tuy nhiên, xét theo khung năm lớp năng lực, đây chính
> là biểu hiện của việc **đầu tư vào ứng dụng mà bỏ quên tích hợp và dữ
> liệu**: doanh nghiệp mua thêm ứng dụng mỗi khi có nhu cầu mới, nhưng
> không xây dựng nền tảng để các ứng dụng đó phối hợp với nhau và không
> xây dựng nơi lưu giữ dữ liệu chung.
>
> Trên cơ sở đó, nhóm đề xuất thứ tự ưu tiên triển khai theo ba giai
> đoạn. Giai đoạn đầu tập trung vào nhóm nội bộ gồm trưởng ca, quản lý
> khu vực, nhân viên nhập liệu và ban điều hành, nhằm giải quyết khâu
> chốt ca và báo cáo hợp nhất. Giai đoạn thứ hai hướng tới hội viên
> phòng gym, khách đặt sân và bộ phận tiếp thị, thông qua việc xây dựng
> định danh khách hàng dùng chung. Giai đoạn thứ ba tập trung vào tuân
> thủ pháp lý về dữ liệu cá nhân, thanh toán trực tuyến trong ứng dụng
> và chuẩn hóa dữ liệu địa chỉ.
>
> Lý do đặt nhóm nội bộ lên trước là vì đây là nhóm có mức số hóa thấp
> nhất, đồng thời cải thiện ở nhóm này cho kết quả đo lường được nhanh
> nhất --- cụ thể là thời gian có báo cáo doanh thu toàn hệ thống và số
> giờ lao động thủ công tiết kiệm được.

# KẾT LUẬN

> Qua quá trình khảo sát Ways Station bằng các nguồn thông tin công
> khai, nhóm rút ra ba kết luận chính.
>
> Thứ nhất, **hiện trạng của Ways Station là một minh họa điển hình cho
> việc tăng trưởng nhanh vượt trước năng lực hạ tầng thông tin**. Trong
> khoảng bốn năm, doanh nghiệp mở rộng từ một điểm lên hơn ba mươi điểm
> kinh doanh. Mỗi khi phát sinh nhu cầu mới, một hệ thống mới được bổ
> sung: ứng dụng cho hội viên, trang đặt sân cho khách cầu lông, nhận
> diện khuôn mặt cho cửa ra vào. Từng hệ thống đều hợp lý xét riêng lẻ,
> nhưng tổng thể lại không tạo thành một kiến trúc.
>
> Thứ hai, **vấn đề cốt lõi không nằm ở việc thiếu công nghệ mà ở việc
> thiếu liên kết**. Doanh nghiệp đã có đủ các thành phần cần thiết,
> nhưng thành phần đóng vai trò tích hợp lại là một nhân viên nhập liệu.
> Đây là biểu hiện chính xác của việc thiếu hai lớp năng lực mà đồ án
> phụ trách: lớp Nền tảng Ứng dụng và Tích hợp, và lớp Nền tảng Dữ liệu.
>
> Thứ ba, **đã tồn tại cả động lực kinh tế lẫn sức ép pháp lý để đầu tư
> vào hai lớp này**. Về kinh tế, riêng chi phí cho việc di chuyển số
> liệu bằng sức người đã ước tính vào khoảng 500 triệu đồng mỗi năm mà
> không tạo ra giá trị mới. Về pháp lý, việc sử dụng dữ liệu sinh trắc
> học đặt doanh nghiệp vào phạm vi điều chỉnh của các quy định về bảo vệ
> dữ liệu cá nhân, và trách nhiệm này không thể chuyển giao cho nhà cung
> cấp phần mềm.
>
> Về giới hạn của đồ án, do toàn bộ khảo sát được thực hiện qua nguồn
> công khai, các nội dung về sơ đồ tổ chức chi tiết, số liệu tài chính
> và danh tính nhà cung cấp phần mềm vẫn ở mức suy luận. Bước tiếp theo
> cần thực hiện là khảo sát thực địa tại một chi nhánh có đủ các dòng
> dịch vụ, kết hợp phỏng vấn đại diện ban điều hành và trưởng ca, nhằm
> kiểm chứng các giả định đã nêu tại Phụ lục A.

# TÀI LIỆU THAM KHẢO

> *Các nguồn trực tuyến đều được truy cập ngày 15 tháng 8 năm 2026.*
>
> **A. Tài liệu do đơn vị khảo sát công bố**
>
> \[1\] Ways Station. *Trang chủ: Hệ sinh thái Thể thao, Giải trí, Không
> gian học và làm tại TP.HCM.* https://www.waysstation.vn/
>
> \[2\] Ways Station. *Tuyển dụng Ways Station -- 38+ chi nhánh TP.HCM.*
> https://diachi.ways.vn/tuyendung
>
> \[7\] Ways Station. *Ways Station Quang Trung -- Gaming và Gym.*
> https://waysstation.vn/ways-station-quang-trung/
>
> \[8\] Ways Station. *Gym tại Ways Station -- bảng giá, quy trình đăng
> ký và chính sách hội viên.* https://diachi.ways.vn/g
>
> \[9\] Ways Station. *Bida tại Ways Station -- danh sách chi nhánh và
> bảng giá.* https://diachi.ways.vn/b
>
> \[10\] Ways Station. *Chi nhánh mới -- bảng giá dịch vụ và thông tin
> liên hệ.* https://diachi.ways.vn/cnmoi
>
> \[11\] Ways Station. *Hướng dẫn đặt sân cầu lông Ways Station
> Badminton trực tuyến qua website.* https://diachi.ways.vn/web
>
> \[12\] Ways Station. *Bảng giá và lưu ý đặt sân -- Sân cầu lông Ways
> Station Badminton.* https://diachi.ways.vn/san
>
> \[13\] Ways Station. *Ứng dụng gym mới của Ways Station -- quản lý gói
> tập và lịch tập luyện.*
> https://waysstation.vn/ung-dung-gym-moi-cua-ways-station-quan-ly-goi-tap-va-lich-tap-luyen-tien-loi/
>
> \[14\] Ways Station. *Ứng dụng WaysStation Gym trên Google Play.*
> https://play.google.com/store/apps/details?id=com.moduncorp.ways
>
> \[16\] Ways Station. *Xác nhận trang Facebook của hệ thống Ways
> Station và danh sách địa chỉ cửa hàng tính đến 3/11/2025.*
> https://waysstation.vn/xac-nhan-trang-facebook-cua-he-thong-ways-station-va-danh-sach-dia-chi-cua-hang-tinh-den-3-11-2025/
>
> \[21\] Ways Station. *Khu vực KickFit Boxing -- chào đón huấn luyện
> viên tự do.* https://diachi.ways.vn/kb
>
> \[22\] Ways Station Biên Hòa. *Trang thông tin Gaming và Billiards.*
> https://www.facebook.com/waysstationbh/
>
> **B. Tài liệu đăng ký kinh doanh**
>
> \[3\] MaSoThue. *Hộ kinh doanh Ways Station -- Gym, mã số thuế
> 8509739366-001.*
> https://masothue.com/8509739366-001-ho-kinh-doanh-ways-station-gym
>
> \[4\] MaSoThue. *Hộ kinh doanh Ways Station GV, mã số thuế
> 8609700179-001.*
> https://masothue.com/8609700179-001-ho-kinh-doanh-ways-station-gv
>
> \[5\] Đại lý Chữ ký số. *Hộ kinh doanh Ways Station N.V.L, mã số thuế
> 8853107310-001.*
> https://dailychukyso.vn/ttdn/8853107310-001-ho-kinh-doanh-ways-station-nvl
>
> \[6\] TopCV. *Hồ sơ Hộ kinh doanh Ways Station QT.*
> https://www.topcv.vn/cong-ty/ho-kinh-doanh-ways-station-qt/235572.html
>
> **C. Nguồn thứ cấp**
>
> \[15\] ModunFit. *Địa điểm Ways Station Gym và Fitness.*
> https://modunfit.com/dia-diem/ways-station-gym-fitness
>
> \[17\] YBOX. *Hệ thống Thể thao Giải trí Ways Station tuyển dụng nhân
> viên, năm 2024.* https://ybox.vn/
>
> \[18\] Vieclam24h. *Danh sách tin tuyển dụng Ways Station.*
> https://vieclam24h.vn/danh-sach-tin-tuyen-dung-ways-station-ntd5989966p122.html
>
> \[19\] Eagle Fitness. *Danh sách hệ thống phòng gym Ways Station tại
> TP. Hồ Chí Minh.* https://www.eaglefitness.vn/ways-station/
>
> \[20\] ShopVNB. *Tìm hiểu chi tiết về sân cầu lông Ways Station ở
> Dương Quảng Hàm, Quận Gò Vấp.*
> https://shopvnb.com/san-cau-long-ways-station.html
>
> **D. Văn bản quy phạm pháp luật và tiêu chuẩn**
>
> \[23\] Chính phủ. *Nghị định số 13/2023/NĐ-CP về bảo vệ dữ liệu cá
> nhân.*
>
> \[24\] Quốc hội. *Luật Bảo vệ dữ liệu cá nhân.*
>
> \[25\] Bộ Khoa học và Công nghệ. *TCVN 11930:2017 -- Công nghệ thông
> tin, các kỹ thuật an toàn, yêu cầu cơ bản về an toàn hệ thống thông
> tin theo cấp độ.*
>
> \[26\] Bộ Thông tin và Truyền thông. *Quyết định số 2568/QĐ-BTTTT ngày
> 29/12/2023 ban hành Khung Kiến trúc Chính phủ điện tử Việt Nam, phiên
> bản 3.0.*
>
> \[27\] Bộ Thông tin và Truyền thông. *Thông tư số 12/2022/TT-BTTTT quy
> định chi tiết về bảo đảm an toàn hệ thống thông tin theo cấp độ.*
>
> **E. Tài liệu môn học**
>
> \[28\] Nguyễn Thị Anh Thư. *Chương 2 -- Kiến trúc hạ tầng CNTT doanh
> nghiệp và tư duy hệ thống.* Trường Đại học Công nghệ Thông tin, Đại
> học Quốc gia TP. Hồ Chí Minh.

# PHỤ LỤC A. CÁC GIẢ ĐỊNH CẦN KIỂM CHỨNG

> Bảng dưới đây tổng hợp những nội dung mà nhóm chưa có minh chứng trực
> tiếp, kèm phương án kiểm chứng cho giai đoạn khảo sát thực địa.

+:--------------------------:+----------+-------------------------------+
| > **Nội dung giả định**    | > **Xuất | > **Phương án kiểm chứng**    |
|                            | > hiện   |                               |
|                            | > tại    |                               |
|                            | > mục**  |                               |
+----------------------------+----------+-------------------------------+
| > Tổng số nhân sự thực tế  | > 2.2    | > Phỏng vấn bộ phận nhân sự   |
| > khoảng 250 đến 400 người |          |                               |
+----------------------------+----------+-------------------------------+
| > Sơ đồ cơ cấu tổ chức như | > 2.3    | > Đề nghị cung cấp sơ đồ tổ   |
| > Hình 2.1                 |          | > chức chính thức             |
+----------------------------+----------+-------------------------------+
| > Doanh thu và cơ cấu      | > 3.4    | > Đề nghị cung cấp số liệu    |
| > doanh thu theo dịch vụ   |          | > tổng hợp, có thể ẩn danh    |
+----------------------------+----------+-------------------------------+
| > Quy trình chốt ca gửi số | > 2.4.5  | > Quan sát trực tiếp một ca   |
| > liệu về văn phòng bằng   |          | > làm việc tại một chi nhánh  |
| > tệp hoặc tin nhắn        |          |                               |
+----------------------------+----------+-------------------------------+
| > Phần mềm quầy thu ngân   | > 3.1    | > Hỏi trưởng ca hoặc liên hệ  |
| > đang sử dụng và khả năng |          | > nhà cung cấp                |
| > trích xuất dữ liệu       |          |                               |
+----------------------------+----------+-------------------------------+
| > Đơn vị cung cấp hệ thống | > 3.3    | > Phỏng vấn ban điều hành,    |
| > nhận diện khuôn mặt và   |          | > xem điều khoản hợp đồng     |
| > nơi lưu trữ dữ liệu      |          |                               |
+----------------------------+----------+-------------------------------+
| > Hệ thống đặt sân do đơn  | > 3.1    | > Phỏng vấn ban điều hành     |
| > vị nào phát triển        |          |                               |
+----------------------------+----------+-------------------------------+
| > Doanh nghiệp không có    | > 2.3    | > Phỏng vấn bộ phận nhân sự   |
| > nhân sự công nghệ thông  |          |                               |
| > tin chuyên trách         |          |                               |
+----------------------------+----------+-------------------------------+
| > Quan hệ sở hữu giữa các  | > 3.3    | > Phỏng vấn ban điều hành;    |
| > hộ kinh doanh cùng       |          | > ảnh hưởng trực tiếp tới khả |
| > thương hiệu              |          | > năng hợp nhất dữ liệu       |
+----------------------------+----------+-------------------------------+
| > Số lượng hội viên phòng  | > 3.4    | > Đề nghị cung cấp số liệu    |
| > gym đang hoạt động       |          |                               |
+----------------------------+----------+-------------------------------+
| > Mô hình và giá dịch vụ   | > 2.1    | > Khảo sát trực tiếp tại chi  |
| > không gian học và làm    |          | > nhánh có dịch vụ này        |
| > việc                     |          |                               |
+----------------------------+----------+-------------------------------+
| > Tần suất và định dạng    | > 4.2    | > Phỏng vấn ban điều hành     |
| > báo cáo hiện tại của ban |          |                               |
| > điều hành                |          |                               |
+----------------------------+----------+-------------------------------+

# PHỤ LỤC B. BỘ CÂU HỎI PHỎNG VẤN DỰ KIẾN

> **Đối với ban điều hành**

1.  Báo cáo doanh thu toàn hệ thống hiện được lập theo cách nào và mất
    bao lâu kể từ khi kết thúc kỳ báo cáo?

2.  Vì sao doanh nghiệp lựa chọn mô hình mỗi chi nhánh là một hộ kinh
    doanh riêng, và mô hình này có ràng buộc gì khi muốn hợp nhất dữ
    liệu?

3.  Kế hoạch mở rộng trong mười hai tháng tới là gì?

> **Đối với trưởng ca và quản lý khu vực**

1.  Trong một ca làm việc, anh chị phải ghi chép và nhập tay bao nhiêu
    loại sổ hoặc biểu mẫu?

2.  Khi một khách vừa là hội viên phòng tập vừa đặt sân cầu lông, anh
    chị tra cứu thông tin của họ ở đâu?

3.  Công việc nào chiếm nhiều thời gian nhất trong một ca?

> **Đối với nhân viên nhập liệu**

1.  Dữ liệu được gửi về từ những nguồn nào và dưới định dạng gì?

2.  Mỗi ngày công việc này chiếm bao nhiêu thời gian?

3.  Sai sót thường phát sinh ở khâu nào?

> **Đối với người phụ trách hệ thống**

1.  Ứng dụng quản lý gói tập có cung cấp giao diện lập trình để trích
    xuất dữ liệu không, và hợp đồng với nhà cung cấp có điều khoản về
    quyền sở hữu dữ liệu không?

2.  Dữ liệu khuôn mặt của hội viên được lưu trữ ở đâu, trong thời hạn
    bao lâu, và những ai có quyền truy cập?

3.  Khi khách hàng yêu cầu xóa dữ liệu cá nhân của mình, quy trình xử lý
    hiện nay là gì?
