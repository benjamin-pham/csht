**THUYẾT MINH ĐỀ TÀI XÂY DỰNG HỆ THỐNG PHẦN MỀM**

*Xây dựng nền tảng tích hợp và kho dữ liệu vận hành hợp nhất cho hệ
thống thể thao – giải trí Ways Station*

*Quy ước: \[n\] = dữ kiện có nguồn công khai · (giả định) = số do nhóm
ước tính, có nêu cơ sở tính*

**0. ĐẦU VÀO ĐÃ THU THẬP**

| **Nhóm đầu vào** | **Kết quả thu thập** |
|----|----|
| Bối cảnh doanh nghiệp | Dịch vụ thể thao – giải trí theo mô hình chuỗi; 38+ chi nhánh tại 12 quận TP.HCM \[2\]; 6 dòng dịch vụ (gym, gym nữ, không gian học và làm, billiards, gaming, cầu lông); hoạt động 24 giờ; vận hành dưới nhiều hộ kinh doanh cá thể độc lập, mỗi hộ có mã số thuế riêng \[3\]\[4\]\[5\]; 50–249 người đóng bảo hiểm xã hội \[6\] |
| Vấn đề hiện tại | 7 hệ thống công nghệ hoạt động độc lập, không có thành phần tích hợp; hợp nhất doanh thu làm thủ công qua một nhân viên nhập liệu \[18\]; báo cáo toàn hệ thống trễ T+~30 ngày (giả định); một khách hàng tồn tại dưới 3 hồ sơ rời nhau; mức trưởng thành số 1,6/5 |
| Đối tượng sử dụng | Nội bộ: ban điều hành, quản lý khu vực, ~38 trưởng ca, thu ngân, nhân viên nhập liệu, kế toán từng hộ kinh doanh. Bên ngoài: hội viên phòng tập, khách đặt sân, khách gaming và billiards |
| Hệ thống liên quan | Ứng dụng gym thuê ngoài \[13\]\[14\], hệ thống đặt sân trực tuyến \[11\], nhận diện khuôn mặt \[8\], phần mềm quầy thu ngân \[9\]\[10\], website và landing page \[1\]\[2\], bảng tính tổng hợp doanh thu |
| Ràng buộc | Không có phòng công nghệ thông tin \[2\]\[17\]\[18\] nên giải pháp phải tích hợp được chứ không tự phát triển; dữ liệu hội viên và sinh trắc học nằm ở nhà cung cấp bên thứ ba; nhiều pháp nhân độc lập nên hợp nhất dữ liệu cần căn cứ pháp lý; tuân thủ Nghị định 13/2023/NĐ-CP \[23\] |

*Bảng 0.1. Đầu vào thu thập được trước khi viết thuyết minh*

**1. TÊN ĐỀ TÀI VÀ THÔNG TIN CHUNG**

| **Hạng mục** | **Nội dung** |
|----|----|
| **Tên đề tài** | **Xây dựng nền tảng tích hợp và kho dữ liệu vận hành hợp nhất cho hệ thống thể thao – giải trí Ways Station** |
| Đơn vị chủ trì | Hệ thống Thể thao – Giải trí Ways Station — Lầu 3, số 770 Quang Trung, Phường Thông Tây Hội, TP. Hồ Chí Minh \[3\] |
| Đơn vị phối hợp | Nhà cung cấp ứng dụng quản lý phòng tập; nhà cung cấp hệ thống đặt sân; đối tác triển khai nền tảng tích hợp và kho dữ liệu |
| Chủ nhiệm đề tài | Đầu mối công nghệ thông tin của doanh nghiệp (vị trí cần bố trí — hiện chưa tồn tại trong cơ cấu) |
| Thời gian thực hiện | 6 tháng, chia 3 pha: pha 1 kho dữ liệu và báo cáo hợp nhất; pha 2 cổng API và định danh dùng chung; pha 3 tuân thủ dữ liệu cá nhân, thanh toán trực tuyến, chuẩn hóa địa chỉ |
| Địa điểm triển khai | Văn phòng điều hành và toàn bộ 38+ chi nhánh tại TP. Hồ Chí Minh |

*Bảng 1.1. Thông tin chung về đề tài*

**Về cách đặt tên:** tên đề tài nêu rõ động từ (xây dựng), đối tượng
(nền tảng tích hợp và kho dữ liệu vận hành hợp nhất), phạm vi nghiệp vụ
(hợp nhất vận hành, không phải toàn bộ hoạt động), và bối cảnh (hệ thống
Ways Station). Tên không dùng các từ mơ hồ như “nâng cấp” hay “cải tiến”
mà không nói rõ nâng cấp cái gì.

**2. BỐI CẢNH VÀ LÝ DO CHỌN ĐỀ TÀI**

**2.1. Hiện trạng quy trình chốt ca và tổng hợp doanh thu**

Trong sáu quy trình nghiệp vụ chính của Ways Station, quy trình chốt ca
và tổng hợp doanh thu là quy trình có mức số hóa thấp nhất, đồng thời là
quy trình mà mọi cấp quản lý đều phụ thuộc vào. Mô tả dưới đây dựa trên
hai dữ kiện kiểm chứng được: doanh nghiệp tuyển vị trí nhân viên nhập
liệu \[18\], và mỗi chi nhánh hoặc cụm chi nhánh thuộc một hộ kinh doanh
riêng có sổ sách riêng \[3\]\[4\]\[5\].

<img src="media/image1.png" style="width:5.11811in;height:2.0374in" />

*Hình 2.1. Luồng AS-IS: doanh thu đi qua bốn khâu thủ công trước khi tới
ban điều hành*

**2.2. Điểm đau và tác động định lượng**

| **Điểm đau** | **Tác động** |
|----|----|
| Hợp nhất doanh thu bằng sức người | ~306 giờ lao động thủ công mỗi tuần (giả định: 38 chi nhánh × 3 ca × 20 phút × 7 ngày, cộng ~40 giờ nhập liệu) |
| Báo cáo toàn hệ thống luôn trễ | T+~30 ngày (giả định) — quyết định mở hay đóng chi nhánh dựa trên số liệu tháng trước |
| Số liệu qua nhiều bước tay nên tiềm ẩn sai sót | Không có bước đối chiếu tự động nào giữa số của chi nhánh và số lên sổ |
| Một khách hàng tồn tại dưới 3 hồ sơ rời nhau | Không trả lời được: bao nhiêu phần trăm hội viên gym cũng đặt sân cầu lông |
| Đối soát thanh toán phụ thuộc thao tác của khách \[11\] | ~3% giao dịch phải xử lý tay qua đường dây nóng (giả định) |
| Tri thức quy trình nằm ở một cá nhân \[18\] | Người này nghỉ việc thì dòng báo cáo toàn hệ thống gián đoạn |

*Bảng 2.1. Sáu điểm đau của quy trình hiện tại*

**Quy đổi thành tiền:** khoảng **~500 triệu đồng mỗi năm** (giả định:
~96 triệu lương nhân viên nhập liệu, cộng ~410 triệu quy đổi thời gian
trưởng ca theo đơn giá 30.000 đồng/giờ). Đây là chi phí chi ra chỉ để di
chuyển số liệu từ nơi này sang nơi khác, không tạo thêm giá trị cho
khách hàng hay doanh nghiệp — và nó tăng tuyến tính theo mỗi chi nhánh
mở mới.

**2.3. Nguyên nhân gốc**

> • **Thiếu lớp tích hợp.** 7 hệ thống hoạt động độc lập, không có cổng
> API hay dịch vụ dùng chung nào; năng lực thanh toán trực tuyến đã có ở
> hệ thống đặt sân từ 2024 \[11\] mà ứng dụng gym vẫn không dùng lại
> được \[13\].
>
> • **Thiếu dữ liệu chủ.** Không có nguồn duy nhất cho danh sách chi
> nhánh và hồ sơ khách hàng — bằng chứng là chính doanh nghiệp công bố
> bốn con số quy mô khác nhau \[2\]\[8\]\[10\]\[17\].
>
> • **Dữ liệu bị chia cắt theo pháp nhân ngay từ gốc.** Mỗi hộ kinh
> doanh là một pháp nhân độc lập với sổ sách riêng \[3\]\[4\]\[5\], nên
> không tồn tại nơi tập trung tự nhiên nào cho số liệu toàn hệ thống.
>
> • **Không có nhân sự công nghệ thông tin.** Không có ai trong tổ chức
> chịu trách nhiệm về kiến trúc hệ thống, nên mỗi nhu cầu mới được giải
> quyết bằng cách mua thêm một ứng dụng rời \[2\]\[17\]\[18\].

**3. MỤC TIÊU, KPI VÀ TIÊU CHÍ THÀNH CÔNG**

**3.1. Mục tiêu tổng quát**

Đưa việc hợp nhất số liệu vận hành của Ways Station từ quy trình thủ
công qua con người sang một hệ thống tự động, để ban điều hành có bức
tranh toàn chuỗi theo ngày thay vì theo tháng. Đồng thời hợp nhất danh
tính khách hàng giữa các dịch vụ, tạo nền cho việc bán chéo và đo hiệu
quả tiếp thị mà hiện nay chưa làm được.

**3.2. Mục tiêu cụ thể (SMART)**

> • Giảm thời gian có báo cáo doanh thu toàn hệ thống từ T+~30 ngày (giả
> định) xuống T+1 ngày, trong 3 tháng sau khi vận hành chính thức.
>
> • Giảm giờ lao động thủ công cho việc hợp nhất số liệu từ ~306 giờ
> (giả định) xuống dưới 20 giờ mỗi tuần, trong 3 tháng.
>
> • Giảm tỉ lệ giao dịch phải đối soát tay từ ~3% (giả định) xuống dưới
> 1%, trong 3 tháng.
>
> • Đạt trên 90% hội viên có hồ sơ hợp nhất một danh tính duy nhất dùng
> cho mọi dịch vụ, trong 6 tháng.
>
> • 100% giao dịch và thay đổi dữ liệu có nhật ký truy vết và phân quyền
> theo vai trò, ngay từ khi vận hành chính thức.
>
> • 100% dữ liệu sinh trắc học có căn cứ pháp lý xử lý và thời hạn lưu
> trữ được công bố cho hội viên, trong 6 tháng \[23\]\[24\].

**3.3. Bảng chỉ tiêu và tiêu chí thành công**

| **Chỉ tiêu** | **Baseline** | **Mục tiêu** | **Thời điểm đo** | **Người chịu trách nhiệm số liệu** |
|----|----|----|----|----|
| Độ trễ báo cáo doanh thu toàn hệ thống | T+~30 ngày (giả định) | **T+1 ngày** | T+3 tháng | Trưởng khối Vận hành chuỗi |
| Giờ thủ công hợp nhất số liệu mỗi tuần | ~306 giờ (giả định) | **\< 20 giờ** | T+3 tháng | Trưởng khối Vận hành chuỗi |
| Tỉ lệ giao dịch đối soát tay | ~3% (giả định) | **\< 1%** | T+3 tháng | Kế toán trưởng |
| Tỉ lệ hội viên có hồ sơ hợp nhất | 0% | **\> 90%** | T+6 tháng | Trưởng bộ phận Khách hàng |
| Số nguồn dữ liệu chủ về chi nhánh | 4 nguồn mâu thuẫn | **1 nguồn** | T+1 tháng | Đầu mối CNTT |
| Tỉ lệ giao dịch có nhật ký truy vết | 0% | **100%** | T+1 tháng | Đầu mối CNTT |
| Mức trưởng thành số bình quân | 1,6/5 | **≥ 3,0/5** | T+6 tháng | Ban điều hành |

*Bảng 3.1. Bảy chỉ tiêu — mỗi chỉ tiêu có baseline, mục tiêu, thời điểm
đo và người chịu trách nhiệm số liệu*

**Tiêu chí thành công của đề tài:** đạt đồng thời hai chỉ tiêu đầu tiên
tại mốc T+3 tháng. Lý do chọn hai chỉ tiêu này làm điều kiện tiên quyết:
chúng đo trực tiếp việc khâu thủ công đã bị loại bỏ khỏi quy trình hay
chưa, và có thể kiểm chứng khách quan bằng cách đối chiếu ngày phát hành
báo cáo với bảng phân công lao động.

**4. ĐỐI TƯỢNG, PHẠM VI, GIẢ ĐỊNH VÀ RÀNG BUỘC**

**4.1. Đối tượng áp dụng**

| **Nhóm người dùng** | **Vai trò trong hệ thống** | **Số lượng** | **Mức số hóa hiện tại** |
|----|----|----|----|
| Ban điều hành | Xem báo cáo hợp nhất, ra quyết định | 3–5 | 1 |
| Quản lý khu vực | Giám sát cụm chi nhánh theo ngày | 4–6 | 1 |
| Trưởng ca | Xác nhận số liệu cuối ca — điểm kiểm soát chính | ~38 | 1 |
| Nhân viên thu ngân | Ghi nhận giao dịch tại quầy | 40–80 | 2 |
| Nhân viên nhập liệu | Chuyển từ nhập liệu sang đối chiếu và phân tích | 1–2 | 2 |
| Kế toán các hộ kinh doanh | Xuất sổ theo pháp nhân từ cùng một nguồn | 3–6 | 2 |
| Hội viên gym, khách đặt sân | Một danh tính dùng chung cho mọi dịch vụ | Hàng nghìn | 2–3 |

*Bảng 4.1. Bảy nhóm người dùng — số lượng là ước tính của nhóm (giả
định)*

**Lưu ý về nhóm nhân viên nhập liệu:** mục tiêu của đề tài là loại bỏ
chính công việc hiện tại của nhóm này. Điều đó không đồng nghĩa với cắt
giảm nhân sự — thời gian được giải phóng chuyển sang công việc đối chiếu
và phân tích có giá trị cao hơn. Đây là yếu tố phải truyền thông cẩn
thận, vì phản kháng từ người trực tiếp bị ảnh hưởng là rủi ro thực tế
của mọi dự án tự động hóa.

**4.2. Phạm vi**

| **Trong phạm vi (in-scope)** | **Ngoài phạm vi (out-of-scope)** |
|----|----|
| **N1** Cổng API làm điểm vào duy nhất cho app gym, web đặt sân và quầy thu ngân | Thay thế hệ thống nhận diện khuôn mặt đang chạy |
| **N2** Định danh khách hàng dùng chung theo chuẩn OIDC — một số điện thoại là một hồ sơ | Xây ứng dụng di động mới thay ứng dụng hiện có |
| **N3** Dịch vụ thanh toán dùng chung và đối soát tự động theo mã đơn hàng do hệ thống sinh | Hệ thống nhân sự và chấm công |
| **N4** Kho dữ liệu vận hành hợp nhất — gộp doanh thu đa dịch vụ, đa pháp nhân | Ba lớp năng lực (1)(2)(3) — hạ tầng tính toán, vận hành, bảo mật |
| **N5** Danh mục dữ liệu cá nhân và hồ sơ tuân thủ Nghị định 13/2023/NĐ-CP, ưu tiên dữ liệu sinh trắc học | Mở rộng chi nhánh mới trong thời gian thực hiện đề tài |
| **N6** Chuẩn hóa dữ liệu địa chỉ chi nhánh sau sắp xếp đơn vị hành chính | Tính năng nhượng suất chơi trong hệ thống (ghi nhận để làm sau) |

*Bảng 4.2. Sáu hạng mục trong phạm vi và sáu hạng mục để lại — tách rõ
để tránh phình phạm vi*

**4.3. Giả định và ràng buộc**

> • **Giả định.** Nhà cung cấp ứng dụng gym đồng ý mở giao diện trích
> xuất dữ liệu; các hộ kinh doanh đạt được thỏa thuận pháp lý cho phép
> hợp nhất dữ liệu; doanh nghiệp bố trí được ít nhất một đầu mối công
> nghệ thông tin chuyên trách; số liệu chốt ca hiện tại đủ chính xác để
> làm dữ liệu đối chiếu ban đầu.
>
> • **Ràng buộc hạ tầng.** Không có phòng công nghệ thông tin nội bộ,
> nên hệ thống phải chạy trên nền tảng cloud do đối tác vận hành, và mọi
> hạng mục phải “tích hợp được” chứ không “tự phát triển”.
>
> • **Ràng buộc pháp lý.** Dữ liệu sinh trắc học thuộc nhóm dữ liệu cá
> nhân nhạy cảm \[23\]; doanh nghiệp giữ vai trò Bên Kiểm soát dữ liệu
> và không chuyển giao được trách nhiệm cho nhà cung cấp, kể cả khi dữ
> liệu nằm trên hệ thống của họ.
>
> • **Ràng buộc vận hành.** Các chi nhánh hoạt động 24 giờ nên không có
> cửa sổ dừng hệ thống; mọi thay đổi phải triển khai theo hình thức chạy
> song song rồi chuyển dần, không cắt chuyển một lần.
>
> • **Ràng buộc thời gian và nguồn lực.** 6 tháng, 3 pha; pha 1 phải cho
> kết quả đo được trước khi bước sang pha 2.

**5. QUY TRÌNH TO-BE — ÁP DỤNG CÔNG NGHỆ VÀO QUY TRÌNH**

Phần này trình bày quy trình chốt ca và hợp nhất doanh thu sau khi áp
dụng hệ thống, đặt cạnh luồng AS-IS ở Hình 2.1 để thấy rõ chỗ nào công
nghệ thay thế thao tác tay và chỗ nào con người vẫn giữ quyền quyết
định.

<img src="media/image2.png" style="width:5.11811in;height:2.32283in" />

*Hình 5.1. Luồng TO-BE: bốn khâu thủ công được thay bằng đồng bộ tự
động, con người chỉ còn giữ một điểm kiểm soát*

| **Khía cạnh** | **AS-IS hiện nay** | **TO-BE sau khi áp dụng** |
|----|----|----|
| Nguồn số liệu | Trưởng ca cộng tay cuối ca | Phần mềm quầy ghi nhận từng giao dịch, tự đẩy về kho dữ liệu qua cổng API |
| Cách chuyển dữ liệu | Tệp, ảnh chụp hoặc tin nhắn, không có định dạng chuẩn | Đồng bộ tự động theo lịch, có nhật ký và cảnh báo khi thất bại |
| Vai trò con người | Nhập lại toàn bộ số liệu vào bảng tính | Chỉ xác nhận số hệ thống đã tính; lệch quá 2% thì bắt buộc ghi lý do |
| Người phê duyệt | Không có bước phê duyệt tường minh | Trưởng ca xác nhận ca; quản lý khu vực phê duyệt trường hợp lệch bất thường |
| Trạng thái theo dõi được | Không có | ĐÃ GHI → ĐÃ ĐỒNG BỘ → ĐÃ XÁC NHẬN → ĐÃ HỢP NHẤT |
| Đầu ra | Báo cáo sau T+~30 ngày (giả định) | Báo cáo tự động T+1 ngày, kế toán từng hộ xuất sổ từ cùng một nguồn |

*Bảng 5.1. So sánh AS-IS và TO-BE của quy trình chốt ca*

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

**\[8\]** Trang dịch vụ phòng tập gym —
[<u>https://diachi.ways.vn/g</u>](https://diachi.ways.vn/g)

**\[9\]** Trang dịch vụ billiards —
[<u>https://diachi.ways.vn/b</u>](https://diachi.ways.vn/b)

**\[10\]** Trang giới thiệu chi nhánh mới —
[<u>https://diachi.ways.vn/cnmoi</u>](https://diachi.ways.vn/cnmoi)

**\[11\]** Hướng dẫn đặt sân cầu lông —
[<u>https://diachi.ways.vn/san</u>](https://diachi.ways.vn/san)

**\[13\]** Trang thông tin gói tập và ứng dụng hội viên —
[<u>https://diachi.ways.vn/web</u>](https://diachi.ways.vn/web)

**\[14\]** Ứng dụng di động quản lý gói tập —
[<u>https://diachi.ways.vn/web</u>](https://diachi.ways.vn/web)

**\[17\]** Tin tuyển dụng hệ thống thể thao giải trí Ways Station —
[<u>https://ybox.vn</u>](https://ybox.vn)

**\[18\]** Tin tuyển dụng vị trí nhân viên nhập liệu —
[<u>https://ybox.vn</u>](https://ybox.vn)

**\[23\]** Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân —
[<u>https://vanban.chinhphu.vn</u>](https://vanban.chinhphu.vn)

**\[24\]** Luật Bảo vệ dữ liệu cá nhân —
[<u>https://vanban.chinhphu.vn</u>](https://vanban.chinhphu.vn)
