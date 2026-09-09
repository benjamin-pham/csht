**BƯỚC 0 -- XÁC ĐỊNH PHẠM VI ĐỀ XUẤT**

*Đồ án môn học -- Cơ sở hạ tầng Công nghệ thông tin*

**Đề tài: Ways Station** \| Lớp năng lực: (4) App & Integration
Platform + (5) Data Platform

**PHẦN 1. KHẢO SÁT TỔNG QUAN VỀ DOANH NGHIỆP**

**1.1. Giới thiệu chung**

Ways Station là hệ sinh thái thể thao -- giải trí -- không gian học tập
và làm việc tại Thành phố Hồ Chí Minh. Doanh nghiệp cung cấp tổ hợp
nhiều loại hình dịch vụ trong cùng một thương hiệu, bao gồm: Gaming
(net), Billiards (bida), Gym & Fitness, Sân cầu lông máy lạnh, và Ways
Station Hub --- không gian dành cho học tập và làm việc.

**Sứ mệnh doanh nghiệp công bố:** mang đến trải nghiệm giải trí lành
mạnh, thúc đẩy lối sống thể thao năng động và tích cực cho cộng đồng;
xây dựng môi trường vui chơi và rèn luyện thể chất văn minh, thoải mái.

**1.2. Mô hình pháp lý và quá trình phát triển**

**(a) Đặc điểm mô hình pháp lý**

Ways Station không đăng ký dưới dạng một pháp nhân duy nhất mà vận hành
theo mô hình chuỗi gồm nhiều hộ kinh doanh độc lập cùng thương hiệu. Tra
cứu trên hệ thống thông tin mã số thuế ghi nhận các chủ thể riêng biệt
như: HỘ KINH DOANH WAYS STATION DH, WAYS STATION GV, WAYS STATION QT,
WAYS STATION N.V.L, WAYS STATION -- GYM... Mỗi hộ kinh doanh có mã số
thuế và người đại diện riêng.

Mô hình này phổ biến với các chuỗi bán lẻ, F&B và giải trí tại Việt Nam
nhờ thủ tục thành lập nhanh, cơ chế thuế khoán đơn giản, khoanh vùng
được rủi ro pháp lý theo từng điểm và linh hoạt trong hợp tác đầu tư tại
mỗi mặt bằng.

**Ý nghĩa đối với đề tài:** cấu trúc pháp lý phân tán là nguyên nhân gốc
rễ khiến dữ liệu vận hành, sổ sách và doanh thu của từng chi nhánh mặc
định tồn tại độc lập, không có cơ chế hợp nhất tự nhiên. Đây là căn cứ
quan trọng lý giải điểm nghẽn dữ liệu phân tán được nêu ở mục 1.6.

**(b) Quá trình phát triển**

Do không có pháp nhân mẹ được công bố, không xác định được một mốc thành
lập chính thức của toàn hệ thống. Quá trình phát triển được tái dựng qua
các mốc khai trương chi nhánh công bố trên website và quy mô ghi nhận
trên các cổng tuyển dụng theo từng thời điểm:

  --------------------------------------------------------------------
  **Thời       **Cột mốc ghi nhận được** **Ý nghĩa**
  điểm**                                 
  ------------ ------------------------- -----------------------------
  10/2023      Khai trương chi nhánh Gym Cho thấy hệ thống đã hoạt
               thứ 5 -- Ways Station Lê  động trước đó; mở rộng dịch
               Lợi (66 Lê Lợi, Gò Vấp),  vụ theo chiều sâu
               quy mô gần 1.000 m², bổ   
               sung khu vực Boxing       

  12/2023      Khai trương chi nhánh Gym Công bố mục tiêu mở rộng
               Quang Trung (770 Quang    chuỗi ra các tỉnh thành
               Trung, Gò Vấp)            

  2024         Quy mô ghi nhận 22--25    Giai đoạn tăng trưởng nhanh
               chi nhánh tại TP.HCM      về số điểm bán

  2025         Quy mô ghi nhận 30+ chi   Mở rộng đồng thời chiều rộng
               nhánh trên 11 quận; bổ    và chiều sâu dịch vụ
               sung Boxing và Sân cầu    
               lông máy lạnh             

  2025--2026   Ra mắt Ways Station Hub   Chuyển từ \'giải trí -- thể
               --- trạm đầu tiên tại 262 thao\' sang hệ sinh thái có
               Dương Quảng Hàm, Gò Vấp;  thêm mảng học tập -- làm việc
               quy mô ghi nhận 34--38    
               chi nhánh                 
  --------------------------------------------------------------------

*Ghi chú: số chi nhánh chênh lệch giữa các nguồn (22 → 25 → 30+ → 34+ →
38+) phản ánh tốc độ mở rộng nhanh qua từng thời điểm công bố; cần kiểm
tra lại tại thời điểm bảo vệ đồ án.*

**1.3. Quy mô và phạm vi hoạt động**

- **Số chi nhánh:** 34+ chi nhánh (một số nguồn ghi nhận 38+), phân bố
  trên 11 quận tại TP.HCM.

- **Khu vực phân bố:** Bình Thạnh, Tân Bình, Thủ Đức, Quận 12, Tân Phú,
  Quận 7, Gò Vấp, Quận 6 và các quận lân cận.

- **Quy mô nhân sự:** thuộc nhóm doanh nghiệp vừa (khoảng 50--249 người
  có BHXH theo phân loại trên cổng tuyển dụng), chưa kể nhân viên thời
  vụ và bán thời gian theo ca.

- **Thời gian hoạt động:** phần lớn chi nhánh vận hành 24/7. Ways
  Station Hub mở cửa 24/24, quầy thu ngân trực từ 6h00 đến 2h00 sáng hôm
  sau.

- **Danh mục dịch vụ:** Gaming, Billiards, Gym & Fitness, Sân cầu lông
  máy lạnh, Ways Station Hub (25.000đ/4 giờ/người). Gym có gói tập
  320.000đ/tháng, ưu đãi đăng ký 3 tháng tặng 1 tháng.

- **Đặc điểm quan trọng:** mỗi chi nhánh có tổ hợp dịch vụ khác nhau.
  Nghiệp vụ tại quầy cũng được tổ chức theo từng cụm dịch vụ riêng
  (Net + Bida, Net + Hub, Gym), phản ánh sự thiếu thống nhất về quy
  trình giữa các mảng.

**1.4. Cơ cấu tổ chức**

Cơ cấu được xác định từ khảo sát thực tế của nhóm. Hệ thống vận hành một
tổng đài hỗ trợ duy nhất, phân nhánh theo phím tới từng phòng ban chức
năng:

  -----------------------------------------------------------------
  **Bộ phận**      **Phạm vi phụ trách**
  ---------------- ------------------------------------------------
  Phòng Nhân sự    Tuyển dụng, đào tạo, hướng dẫn ký quỹ, cấp phát
  (phím 2)         đồng phục, ghi nhận công, tính lương; xử lý yêu
                   cầu đổi vị trí/chi nhánh/ca làm; thủ tục thôi
                   việc. Kênh email: hr@waysstation.vn

  Phòng Điều phối  Lịch làm việc, xử lý tình huống ca sau chưa tới,
  (phím 3)         bố trí học việc, ca làm phát sinh, nghỉ phép;
                   lấy vân tay và chấm công in/out

  Bộ phận Kho hàng Vật tư, hàng hóa tại chi nhánh; đồng thời hỗ trợ
  (phím 8)         nhân viên truy cập phần mềm quản lý gym và cổng
                   thanh toán

  Quản lý chi      Tiếp nhận báo cáo cuối ca; xử lý sự vụ phát
  nhánh (QLCN)     sinh; là đầu mối tiếp nhận ảnh biên bản gửi qua
                   tin nhắn

  Quản lý ca /     Làm việc 9 tiếng/ca (có trực đêm); giám sát nhân
  Trưởng ca        viên, xử lý sự vụ, lập báo cáo trên Google Drive
                   và Excel

  Nhân viên vận    Thu ngân, Phục vụ (net/bida/gym/cầu lông), Giữ
  hành             xe, Nhập liệu, Giám sát camera --- ca cố định
                   4--9 tiếng; ca đêm có thể kiêm nhiệm nhiều vị
                   trí tùy chi nhánh
  -----------------------------------------------------------------

**Quy trình gia nhập:** ứng viên đăng ký ứng tuyển → được đào tạo nghiệp
vụ theo vị trí → học việc tại chi nhánh → nếu đạt sẽ được nhận làm chính
thức. Nhân sự thời vụ được bố trí linh hoạt theo ca trống của các chi
nhánh trong khu vực đã đăng ký.

**1.5. Quy trình nghiệp vụ chính**

Ways Station vận hành nhiều nhóm quy trình song song. Xét theo cách
khách hàng chi trả và cách hệ thống ghi nhận việc sử dụng dịch vụ, các
mảng hiện chia thành ba mô hình khác nhau:

  -----------------------------------------------------------------
  **Mô hình**      **Mảng áp    **Cách vận hành**
                   dụng**       
  ---------------- ------------ -----------------------------------
  Trả trước theo   Gaming       Khách tạo tài khoản tại quầy và nạp
  số dư tài khoản               tiền vào số dư; hệ thống trừ dần
                                theo thời gian sử dụng với đơn giá
                                tùy loại máy. Các lần sau khách chỉ
                                cần nạp thêm, không tạo lại tài
                                khoản

  Trả sau theo     Billiards,   Nhân viên mở lượt và bắt đầu tính
  lượt sử dụng     Cầu lông     giờ; khách thanh toán khi kết thúc
                                lượt. Cầu lông có thêm kênh đặt sân
                                trực tuyến riêng

  Trả trước theo   Hub, Gym     Khách mua trước một suất thời gian
  suất hoặc gói                 (Hub) hoặc một gói tập có thời hạn
                                (Gym) và sử dụng trong phạm vi đã
                                mua
  -----------------------------------------------------------------

**Nhận định quan trọng:** hai mảng Gaming và Gym đều đã có khái niệm tài
khoản khách hàng --- một bên là tài khoản có số dư, một bên là hồ sơ hội
viên với nhận diện khuôn mặt. Tuy nhiên hai hệ thống tài khoản này hoàn
toàn tách biệt. Một khách hàng vừa chơi Gaming vừa tập Gym được ghi nhận
như hai khách hàng khác nhau. Vấn đề do đó không nằm ở việc thiếu hệ
thống quản lý khách hàng, mà ở việc tồn tại nhiều hệ thống định danh
song song không liên thông được với nhau.

**(a) Quy trình phục vụ tại chi nhánh**

Dù khác nhau về mô hình thu phí, cả ba nhóm đều đi theo cùng một cấu
trúc: khách đăng ký hoặc chọn dịch vụ tại quầy → nhân viên mở quyền sử
dụng (nạp số dư, mở lượt, kích hoạt suất hoặc gói) → chuẩn bị vị trí và
phục vụ trong quá trình sử dụng → khách có thể gọi thêm hàng hóa hoặc
mượn thiết bị phụ trợ → kết thúc, thanh toán phần phát sinh và ghi nhận
vào báo cáo ca.

**(b) Quy trình nhập và quản lý hàng hóa tại chi nhánh**

Bên cạnh dịch vụ chính, các chi nhánh còn kinh doanh đồ ăn, nước uống và
hàng tiêu dùng, đồng thời cho khách mượn một số thiết bị phụ trợ. Vòng
luân chuyển hàng hóa tại chi nhánh diễn ra như sau:

- **Nhập hàng:** chi nhánh đề xuất nhu cầu và tiếp nhận hàng hóa, vật tư
  từ bộ phận phụ trách kho của hệ thống.

- **Lưu trữ tại quầy:** hàng hóa được sắp xếp tại khu vực phục vụ, có
  theo dõi hạn sử dụng đối với thực phẩm và đồ uống.

- **Bán và phục vụ:** thu ngân ghi nhận từng giao dịch phát sinh trong
  ca, bao gồm cả các món chế biến tại chỗ.

- **Cho mượn thiết bị:** một số thiết bị phụ trợ được cho khách mượn
  trong thời gian sử dụng dịch vụ và thu hồi khi khách rời đi.

- **Kiểm kê cuối ca:** nhân viên đối chiếu số lượng hàng đã bán, tồn còn
  lại và tình trạng thiết bị, ghi vào báo cáo ca.

- **Đề xuất nhập bổ sung:** khi hàng sắp hết, chi nhánh liên hệ bộ phận
  kho để bổ sung.

**Đặc điểm:** danh mục hàng hóa khác nhau giữa các chi nhánh tùy theo tổ
hợp dịch vụ. Toàn bộ vòng luân chuyển này hiện được theo dõi thủ công
theo từng ca và từng chi nhánh, chưa có dữ liệu tồn kho tập trung ở cấp
hệ thống.

**(c) Quy trình bàn giao và báo cáo ca --- áp dụng chung cho mọi chi
nhánh**

- Chấm công đầu ca; kiểm tra thiết bị, hàng hóa và điều kiện phục vụ

- Theo dõi tình trạng sử dụng của các vị trí dịch vụ trong suốt ca trực

- **Ghi nhận số lượng vị trí đang sử dụng theo khung giờ** --- thao tác
  đếm và ghi thủ công, lặp lại nhiều lần trong ca

- Kiểm kê tiền, vật tư và hàng hóa cuối ca, gửi báo cáo cho Quản lý chi
  nhánh

- Bàn giao sổ ghi chép, chìa khóa, tiền và vật dụng giá trị giữa các ca

**(d) Quy trình xử lý sự vụ phát sinh**

Khi có sự vụ tại chi nhánh (khách làm mất thẻ gửi xe, thiết bị hỏng,
khách vi phạm nội quy), nhân viên lập biên bản trên giấy, chụp ảnh hiện
trạng và gửi cho Quản lý qua ứng dụng nhắn tin, đồng thời ghi lại vào sổ
bàn giao ca. Một số trường hợp cần theo dõi trong nhiều ngày, và việc
theo dõi này cũng được bàn giao thủ công giữa các ca.

**Nhận định chung:** các quy trình trên có cùng cấu trúc cốt lõi --- mở
quyền sử dụng, phục vụ, thanh toán và ghi nhận --- nhưng đang được thực
hiện trên những hệ thống và biểu mẫu khác nhau tùy theo mảng dịch vụ.
Đây là biểu hiện trực tiếp của việc thiếu một lớp tích hợp và một nền
tảng dữ liệu dùng chung.

**1.6. Hiện trạng số hóa**

**(a) Bản đồ các hệ thống đang sử dụng**

Khảo sát cho thấy Ways Station đang vận hành song song nhiều hệ thống
độc lập, trong đó một phần đáng kể vẫn là quy trình thủ công trên giấy:

  -----------------------------------------------------------------
  **Hệ thống /     **Chức năng**          **Đặc điểm**
  công cụ**                               
  ---------------- ---------------------- -------------------------
  Hệ thống nhân sự Quản lý thông tin nhân Nền tảng web riêng cho
  nội bộ           sự, tra cứu chức năng  khối nhân sự
                   nội bộ                 

  Phần mềm quản lý Quản lý hội viên và    Phần mềm của bên thứ ba,
  gym              gói tập mảng Gym       tách biệt với các mảng
                                          khác

  Cổng thanh toán  Giao dịch chuyển khoản Hệ thống của bên thứ ba,
  ngân hàng                               tách rời khỏi hệ thống
                                          bán hàng

  Face ID          Check-in hội viên Gym  Chỉ áp dụng cho mảng Gym

  Máy chấm công    Chấm công in/out nhân  Thiết bị riêng, do Phòng
  vân tay          viên                   Điều phối quản lý

  Google Drive /   Lập báo cáo ca của     File rời rạc theo từng
  Excel            Quản lý ca             ca, từng chi nhánh

  Ứng dụng nhắn    Gửi ảnh biên bản, sự   Kênh cá nhân, không lưu
  tin              vụ cho Quản lý         vết hệ thống

  Sổ giao ca, biên Ghi nhận sự vụ, bàn    Hoàn toàn thủ công, không
  bản, phiếu giấy  giao ca, đăng ký hội   số hóa
                   viên                   
  -----------------------------------------------------------------

**(b) Ba điểm nghẽn chính**

Các biểu hiện nêu ở mục (a) là triệu chứng ở tầng vận hành; nguyên nhân
gốc nằm ở tầng hạ tầng công nghệ thông tin, cụ thể là thiếu lớp tích hợp
ứng dụng và thiếu nền tảng dữ liệu tập trung. Đây là căn cứ để dự án đầu
tư vào lớp (4) và lớp (5) thay vì chỉ cải tiến quy trình thủ công.

1.  **Phân mảnh nền tảng ứng dụng ---** mỗi mảng dịch vụ và mỗi nghiệp
    vụ chạy trên một hệ thống độc lập, không có lớp tích hợp chung (API
    Gateway, middleware) để trao đổi dữ liệu. Đáng chú ý, doanh nghiệp
    đã có tới hai hệ thống định danh khách hàng riêng biệt --- tài khoản
    số dư của mảng Gaming và hồ sơ hội viên của mảng Gym --- nhưng hai
    hệ thống này không liên thông, khiến cùng một khách hàng được ghi
    nhận thành nhiều thực thể khác nhau. Vấn đề vì vậy không phải là
    thiếu hệ thống, mà là thiếu cơ chế hợp nhất giữa các hệ thống đã có.

2.  **Dữ liệu vận hành thủ công và không truy vết được ---** báo cáo ca
    lập bằng Excel/Google Drive theo từng chi nhánh; số lượng bàn--máy
    đếm và ghi tay theo khung giờ chẵn; sự vụ được gửi qua ứng dụng nhắn
    tin cá nhân và ghi vào sổ giấy. Nguyên nhân kỹ thuật là hệ thống
    chưa có cơ chế thu thập dữ liệu trạng thái tự động (telemetry/event
    ingestion) và chưa có nơi lưu trữ tập trung, buộc phải bù bằng thao
    tác thủ công.

3.  **Cấu trúc phân tán làm khuếch đại độ phức tạp khi mở rộng ---** mỗi
    chi nhánh là một hộ kinh doanh độc lập với mã số thuế riêng, trong
    khi chuỗi tăng từ khoảng 22 lên 34+ chi nhánh trong chưa đầy hai
    năm. Do chưa có chuẩn cấu hình và cơ chế triển khai tự động, mỗi lần
    mở chi nhánh mới đều phải thiết lập hệ thống thủ công --- chi phí
    tích hợp tăng tuyến tính theo số chi nhánh thay vì được khấu hao
    trên nền tảng dùng chung.

**1.7. Hệ thống liên quan và khả năng tích hợp**

Xét dưới góc độ tích hợp, các hệ thống hiện có của Ways Station được
phân loại theo khả năng kết nối để làm căn cứ thiết kế lớp tích hợp:

  ------------------------------------------------------------------
  **Hệ thống**    **Loại**          **Dữ liệu quản   **Khả năng tích
                                    lý**             hợp (đánh giá
                                                     sơ bộ)**
  --------------- ----------------- ---------------- ---------------
  Phần mềm quản   Phần mềm nghiệp   Hội viên, gói    Cần khảo sát
  lý gym          vụ của bên thứ ba tập, lịch sử     API do nhà cung
                                    check-in Face ID cấp công bố;
                                                     nếu không có,
                                                     phải tích hợp
                                                     qua tầng trung
                                                     gian

  Cổng thanh toán Dịch vụ bên thứ   Giao dịch chuyển Ngân hàng
  ngân hàng       ba                khoản            thường cung cấp
                                                     API đối soát;
                                                     cần thỏa thuận
                                                     với đơn vị cung
                                                     cấp

  Hệ thống nhân   Ứng dụng web nội  Hồ sơ nhân sự,   Hệ thống nội
  sự nội bộ       bộ                chấm công        bộ, khả năng mở
                                                     API cao nhất

  Máy chấm công   Thiết bị đầu cuối Dữ liệu chấm     Thường xuất dữ
  vân tay                           công in/out      liệu theo tệp
                                                     hoặc API thiết
                                                     bị; cần khảo
                                                     sát model cụ
                                                     thể

  Google Drive /  Công cụ văn phòng Báo cáo ca theo  Không phải hệ
  Excel                             tệp rời          thống nghiệp
                                                     vụ; dữ liệu cần
                                                     được số hóa
                                                     thay vì tích
                                                     hợp

  Ứng dụng nhắn   Công cụ trao đổi  Ảnh biên bản,    Kênh cá nhân,
  tin                               trao đổi sự vụ   không có lưu
                                                     vết hệ thống;
                                                     cần thay thế
                                                     bằng quy trình
                                                     có kiểm soát
  ------------------------------------------------------------------

**Nhận định:** chưa ghi nhận cơ sở dữ liệu dùng chung giữa các mảng dịch
vụ. Mỗi hệ thống quản lý tập dữ liệu riêng với định danh khách hàng
riêng, do đó chưa thể liên kết một khách hàng sử dụng nhiều dịch vụ
thành một hồ sơ thống nhất. Đây là căn cứ kỹ thuật cho việc đầu tư lớp
(4) App & Integration Platform.

*Ghi chú: khả năng tích hợp nêu trên là đánh giá sơ bộ dựa trên loại
hình hệ thống. Việc xác định chính xác giao thức, tần suất đồng bộ và
cách ánh xạ dữ liệu sẽ được thực hiện ở bước thiết kế giải pháp.*

**1.8. Ràng buộc của dự án**

**(a) Ràng buộc tuân thủ pháp lý**

Ways Station thu thập và xử lý dữ liệu cá nhân của khách hàng, trong đó
có số điện thoại đăng ký hội viên và dữ liệu sinh trắc học khuôn mặt
phục vụ check-in Face ID tại phòng tập. Theo Nghị định 13/2023/NĐ-CP về
bảo vệ dữ liệu cá nhân, dữ liệu sinh trắc học thuộc nhóm dữ liệu cá nhân
nhạy cảm và chịu các yêu cầu chặt chẽ hơn về sự đồng ý của chủ thể dữ
liệu, biện pháp bảo vệ và nghĩa vụ thông báo.

Đây là ràng buộc bắt buộc, chi phối trực tiếp các hạng mục thuộc cột Bảo
mật của cả hai lớp năng lực: mã hóa dữ liệu khi lưu trữ và truyền tải,
phân quyền truy cập theo vai trò, và nhật ký kiểm toán truy cập dữ liệu.

**(b) Ràng buộc hạ tầng**

- Dự án kế thừa hạ tầng phần cứng và mạng hiện có của doanh nghiệp,
  không đầu tư mới.

- Hệ thống phải vận hành liên tục 24/7 theo đặc thù kinh doanh; việc
  triển khai và nâng cấp cần thực hiện theo cơ chế không gây gián đoạn
  dịch vụ tại chi nhánh.

- Phương án triển khai dự kiến theo mô hình hybrid: giữ dữ liệu vận hành
  cốt lõi tại chỗ, đưa phần phân tích và mở rộng lên cloud.

**(c) Ràng buộc tổ chức và nguồn lực**

- Doanh nghiệp vận hành theo mô hình nhiều hộ kinh doanh độc lập, do đó
  việc thống nhất chuẩn dữ liệu và quy trình giữa các chi nhánh cần cơ
  chế phối hợp thay vì áp đặt bằng mệnh lệnh hành chính.

- Nhân sự vận hành tại chi nhánh làm việc theo ca, có luân chuyển và sử
  dụng lao động thời vụ; giải pháp cần đơn giản trong thao tác và chi
  phí đào tạo thấp.

- Chưa xác định được quy mô đội ngũ công nghệ thông tin nội bộ từ nguồn
  công khai; đây là thông tin cần làm rõ khi lập kế hoạch nhân sự dự án.

**(d) Ràng buộc thời gian và ngân sách**

- Thời gian triển khai dự kiến 12 tháng, thiết kế đáp ứng chu kỳ vận
  hành 5 năm.

- Ngân sách chưa được xác lập ở bước này; dự toán chi tiết sẽ được xây
  dựng ở bước lập kế hoạch tài chính của thuyết minh.

**PHẦN 2. PROJECT SCOPE ONE-PAGER**

  -----------------------------------------------------------------
  **Hạng mục**     **Nội dung**
  ---------------- ------------------------------------------------
  Tên dự án        Đầu tư nền tảng tích hợp dịch vụ và nền tảng dữ
                   liệu tập trung cho hệ thống Ways Station

  Đơn vị thụ hưởng Ways Station -- hệ sinh thái thể thao, giải trí,
                   học tập và làm việc; 34+ chi nhánh tại TP.HCM

  Lớp năng lực đầu \(4\) App & Integration Platform + (5) Data
  tư               Platform

  Thành phần đầu   Phần mềm -- Quản trị -- Bảo mật. Giả định phần
  tư               cứng và hạ tầng mạng hiện có đã đáp ứng đủ, dự
                   án kế thừa và tận dụng.

  Thời gian        12 tháng triển khai; thiết kế đáp ứng nhu cầu
                   vận hành và mở rộng trong chu kỳ 5 năm
  -----------------------------------------------------------------

**Ma trận phạm vi đầu tư theo khung tham chiếu**

Dự án đầu tư 6 ô trong khung tham chiếu 5 lớp năng lực (tương ứng 2 lớp
× 3 thành phần):

  -------------------------------------------------------------------------
  **Lớp năng     **Phần mềm**       **Quản trị**      **Bảo mật**
  lực**                                               
  -------------- ------------------ ----------------- ---------------------
  \(4\) App &    API Gateway,       CI/CD,            AuthN/Z (OIDC/SAML),
  Integration    middleware/ESB,    release/change,   secrets management,
  Platform       container, message versioning API,   API security, runtime
                 queue/event bus    app observability security

  \(5\) Data     DBMS, Data         Data governance,  Mã hóa
  Platform       Warehouse/Lake,    stewardship,      at-rest/in-transit,
                 ETL/ELT,           retention, data   phân quyền theo
                 catalog/lineage,   quality rules,    hàng/cột, audit truy
                 DQ tooling         metadata          cập dữ liệu
                                    standards         
  -------------------------------------------------------------------------

*Không đầu tư: cột Phần cứng và cột Mạng của cả hai lớp --- kế thừa hạ
tầng hiện có của doanh nghiệp.*

**Vấn đề cần giải quyết**

Các mảng dịch vụ của Ways Station vận hành trên những hệ thống độc lập,
chưa có lớp tích hợp chung và chưa có nền tảng dữ liệu tập trung. Hệ quả
là dữ liệu phân tán theo từng chi nhánh và nhiều nghiệp vụ phải bù bằng
thao tác thủ công; chi phí tích hợp tăng theo tốc độ mở rộng của chuỗi.

**Mục tiêu đầu tư**

- **Lớp (4):** xây dựng lớp tích hợp kết nối các hệ thống hiện có thành
  nền tảng thống nhất; số hóa các nghiệp vụ đang làm thủ công.

- **Lớp (5):** xây dựng kho dữ liệu tập trung và quy trình ETL; thay thế
  báo cáo ca thủ công bằng báo cáo tự động.

**Đối tượng thụ hưởng**

- **Nhân viên ca trực:** giảm thao tác thủ công khi bàn giao ca và ghi
  nhận số liệu.

- **Quản lý chi nhánh và khu vực:** xem báo cáo tổng hợp tự động thay vì
  đối chiếu nhiều tệp rời rạc.

- **Ban điều hành chuỗi:** có dữ liệu tỷ lệ lấp đầy và doanh thu theo
  khung giờ để ra quyết định.

- **Khách hàng:** một tài khoản dùng chung cho nhiều dịch vụ.

**Lý do đầu tư hai lớp năng lực này**

**Lớp (4) App & Integration Platform**

- **Nếu không đầu tư:** mỗi mảng dịch vụ tiếp tục vận hành trên hệ thống
  riêng, không có định danh khách hàng thống nhất. Mỗi chi nhánh hoặc
  dịch vụ mới đều phải thiết lập kết nối thủ công, khiến chi phí tích
  hợp tăng tuyến tính theo tốc độ mở rộng của chuỗi.

- **Khi đầu tư:** các hệ thống hiện có trao đổi dữ liệu qua một lớp
  trung gian thống nhất; chi nhánh và dịch vụ mới được kết nối theo
  chuẩn có sẵn thay vì làm lại từ đầu.

**Lớp (5) Data Platform**

- **Nếu không đầu tư:** dữ liệu vận hành tiếp tục nằm rời rạc theo từng
  ca và từng chi nhánh, không thể tổng hợp kịp thời để ra quyết định;
  các nghiệp vụ ghi nhận số liệu vẫn phải bù bằng thao tác thủ công.

- **Khi đầu tư:** có nguồn dữ liệu tập trung cho toàn hệ thống, phục vụ
  báo cáo tự động và làm nền tảng để triển khai các chức năng phân tích,
  dự báo về sau.

**Phạm vi loại trừ:** dự án không đầu tư mới phần cứng máy chủ, thiết bị
đầu cuối và hạ tầng mạng tại chi nhánh; các thành phần này được giả định
đã đáp ứng đủ nhu cầu và sẽ được kế thừa.

**PHẦN 3. Ý TƯỞNG BÀI THỰC HÀNH**

*Thuyết minh đề tài phát triển hệ thống phần mềm ứng dụng công nghệ mới
--- nằm trong phạm vi lớp năng lực đã chọn ở đồ án môn học.*

  -----------------------------------------------------------------
  **Hạng mục**     **Nội dung**
  ---------------- ------------------------------------------------
  Tên đề tài       Ứng dụng học máy dự báo lưu lượng khách theo
                   khung giờ hỗ trợ điều phối nhân sự tại hệ thống
                   Ways Station

  Công nghệ áp     Trí tuệ nhân tạo --- Mô hình nền tảng cho chuỗi
  dụng             thời gian (Time Series Foundation Model), hướng
                   tiếp cận mới cho phép dự báo zero-shot /
                   few-shot

  Quy trình nghiệp Điều phối nhân sự và xếp ca trực tại chi nhánh
  vụ               

  Nhóm người dùng  Phòng Điều phối (chính); Quản lý chi nhánh và
  (actor)          Quản lý khu vực (phụ)

  Liên kết với đồ  Khai thác trực tiếp kho dữ liệu tập trung của
  án               lớp (5) Data Platform và dữ liệu check-in được
                   hợp nhất qua lớp (4) App & Integration Platform
  -----------------------------------------------------------------

**1. Vấn đề thực tế**

Khảo sát cho thấy Phòng Điều phối hiện phụ trách lịch làm việc, xử lý
tình huống ca sau chưa tới, bố trí ca làm phát sinh và nghỉ phép. Doanh
nghiệp đồng thời vận hành một kênh tuyển thời vụ ngắn hạn riêng để bù
nhân sự vào các ca trống của những chi nhánh trong cùng khu vực.

Điều này phản ánh cơ chế điều phối hiện tại mang tính bị động: việc bố
trí nhân sự chủ yếu dựa trên kinh nghiệm và xử lý phát sinh khi ca đã
thiếu người, thay vì dự báo trước nhu cầu. Với hệ thống 34+ chi nhánh
vận hành 24/7, mỗi chi nhánh có tổ hợp dịch vụ khác nhau và lưu lượng
khách biến động mạnh theo khung giờ, ngày trong tuần và mùa vụ, cách làm
này dẫn tới hai trạng thái đều gây tổn thất: thừa nhân sự ở khung giờ
vắng làm tăng chi phí, và thiếu nhân sự ở khung giờ cao điểm làm giảm
chất lượng phục vụ.

**2. Mục tiêu và phạm vi**

**Mục tiêu:** xây dựng mô hình học máy dự báo số lượt khách theo khung
giờ cho từng chi nhánh và từng loại hình dịch vụ, với tầm dự báo đủ xa
(từ 1 đến 2 tuần) để Phòng Điều phối chủ động lập lịch ca thay vì xử lý
phát sinh.

**Phạm vi:** giới hạn ở một bài toán duy nhất là dự báo lưu lượng khách.
Đề tài không bao gồm bài toán tối ưu xếp lịch tự động, không bao gồm
phân tích hành vi khách hàng và không bao gồm các bài toán trên dữ liệu
hình ảnh hay video.

*Phân biệt: đề tài hướng tới dự báo (forecasting) --- ước lượng giá trị
tương lai chưa xảy ra bằng mô hình học máy, khác với báo cáo (reporting)
là tổng hợp và trực quan hóa dữ liệu đã phát sinh bằng công cụ BI thông
thường.*

**3. Mô tả quy trình nghiệp vụ**

**Tên nghiệp vụ:** Lập lịch ca trực và bố trí nhân sự tại chi nhánh.

**Tác nhân:** Phòng Điều phối (chủ trì); Quản lý chi nhánh và Quản lý
khu vực (đề xuất, phê duyệt); Nhân viên vận hành (xác nhận ca); Phòng
Nhân sự (tuyển bổ sung khi thiếu).

*Quy trình dưới đây được tái dựng từ kết quả khảo sát về phạm vi phụ
trách của Phòng Điều phối và cơ chế tuyển thời vụ theo ca trống; không
phải quy trình chuẩn do doanh nghiệp công bố chính thức.*

**(a) Quy trình hiện tại (AS-IS)**

  -----------------------------------------------------------------------
  **Bước**   **Tác nhân**      **Hoạt động**          **Công cụ / cách
                                                      làm hiện nay**
  ---------- ----------------- ---------------------- -------------------
  1          Quản lý chi nhánh Ước lượng nhu cầu nhân Dựa trên kinh
                               sự cho tuần kế tiếp    nghiệm cá nhân và
                                                      cảm nhận về mức độ
                                                      đông khách

  2          Phòng Điều phối   Lập lịch ca cho các    Bảng tính, trao đổi
                               chi nhánh trong khu    qua tin nhắn
                               vực phụ trách          

  3          Nhân viên vận     Xác nhận ca được phân, Hệ thống nhân sự
             hành              đăng ký nghỉ phép      nội bộ

  4          Phòng Điều phối   Rà soát ca còn trống,  Kênh tuyển thời vụ
                               đăng tuyển nhân sự     ngắn hạn theo khu
                               thời vụ bù ca          vực

  5          Trưởng ca         Xử lý phát sinh trong  Gọi tổng đài Phòng
                               ngày: ca sau chưa tới, Điều phối, điều
                               lượng khách tăng đột   người tại chỗ
                               biến                   
  -----------------------------------------------------------------------

**Điểm đau của quy trình:** bước 1 không có căn cứ định lượng. Sai lệch
trong ước lượng ban đầu không được phát hiện sớm mà dồn xuống bước 4 và
bước 5, khiến việc điều phối chuyển thành xử lý tình huống. Hệ quả là
thừa nhân sự ở khung giờ vắng và thiếu nhân sự ở khung giờ cao điểm ---
cả hai đều gây tổn thất nhưng không được đo lường.

**(b) Quy trình sau khi triển khai (TO-BE)**

Hệ thống dự báo được chèn vào trước bước 1, chuyển bước này từ ước lượng
cảm tính sang xác nhận và điều chỉnh đề xuất có căn cứ dữ liệu:

  -----------------------------------------------------------------------
  **Bước**   **Tác nhân**      **Hoạt động**          **Thay đổi so với
                                                      AS-IS**
  ---------- ----------------- ---------------------- -------------------
  0          Hệ thống dự báo   Dự báo lưu lượng khách Bước mới. Chạy tự
                               theo khung giờ cho     động theo lịch,
                               từng chi nhánh trong   không cần thao tác
                               7--14 ngày tới, kèm    người
                               khoảng bất định và mức 
                               nhân sự đề xuất        

  1          Quản lý chi nhánh Xem đề xuất của hệ     Chuyển từ ước lượng
                               thống, xác nhận hoặc   sang rà soát; con
                               điều chỉnh theo hiểu   người vẫn giữ quyền
                               biết thực tế           quyết định cuối

  2          Phòng Điều phối   Lập lịch ca dựa trên   Có căn cứ định
                               mức nhân sự đã chốt    lượng thay vì phân
                                                      bổ đều

  3          Nhân viên vận     Xác nhận ca, đăng ký   Không thay đổi
             hành              nghỉ phép              

  4          Phòng Điều phối   Rà soát ca trống,      Tần suất giảm do
                               tuyển bổ sung nếu cần  nhu cầu được dự báo
                                                      sớm hơn

  5          Trưởng ca         Xử lý phát sinh trong  Giảm tần suất; chỉ
                               ngày                   còn các tình huống
                                                      thực sự bất thường
  -----------------------------------------------------------------------

**(c) Đầu vào -- đầu ra của phần mềm**

- **Đầu vào:** dữ liệu lịch sử check-in theo chi nhánh và loại hình dịch
  vụ; lịch nghỉ lễ, kỳ thi và kỳ nghỉ của sinh viên; cấu hình chi nhánh
  (khu vực, tổ hợp dịch vụ, quy mô).

- **Đầu ra:** bảng dự báo lưu lượng theo khung giờ kèm khoảng tin cậy;
  mức nhân sự đề xuất tương ứng; cảnh báo các khung giờ dự báo vượt
  ngưỡng năng lực phục vụ hiện tại.

**(d) Các luồng ngoại lệ**

- **Chi nhánh mới khai trương chưa có dữ liệu lịch sử:** hệ thống sử
  dụng dự báo zero-shot từ mô hình nền tảng, tham chiếu các chi nhánh
  tương đồng về khu vực và tổ hợp dịch vụ; chuyển sang chế độ tinh chỉnh
  khi tích lũy đủ dữ liệu.

- **Sự kiện bất thường (giải đấu, khuyến mãi lớn, sự cố):** hệ thống
  đánh dấu độ tin cậy thấp cho khoảng thời gian liên quan và nhường
  quyết định cho người điều phối, thay vì đưa ra con số gây hiểu nhầm.

- **Dữ liệu đầu vào thiếu hoặc lỗi:** hệ thống giữ lại kết quả dự báo
  của kỳ trước và phát cảnh báo về chất lượng dữ liệu cho bộ phận quản
  trị dữ liệu.

**4. Dữ liệu đầu vào dự kiến**

- **Dữ liệu lịch sử check-in:** thời điểm khách vào và ra, phân theo chi
  nhánh và loại hình dịch vụ (Gaming, Billiards, Gym, Cầu lông, Hub).

- **Dữ liệu báo cáo ca:** số lượng bàn và máy đang sử dụng theo khung
  giờ --- dữ liệu này hiện đã được ghi nhận thủ công theo khung giờ
  chẵn, sẽ được số hóa qua đầu tư lớp (4).

- **Đặc trưng thời gian:** giờ trong ngày, ngày trong tuần, ngày lễ, kỳ
  thi và kỳ nghỉ của sinh viên --- nhóm khách hàng chiếm tỷ trọng đáng
  kể với dịch vụ Gaming và Hub.

- **Đặc trưng chi nhánh:** khu vực địa lý, tổ hợp dịch vụ có tại chi
  nhánh, quy mô.

**5. Quy trình triển khai dự kiến**

1.  **Thu thập và tiền xử lý dữ liệu:** trích xuất dữ liệu lịch sử từ
    kho dữ liệu tập trung; làm sạch, xử lý giá trị thiếu và chuẩn hóa về
    dạng chuỗi thời gian theo khung giờ.

2.  **Xây dựng đặc trưng (feature engineering):** tạo các đặc trưng trễ
    (lag features), trung bình trượt và đặc trưng chu kỳ để mô hình nắm
    được tính lặp theo tuần và theo mùa.

3.  **Huấn luyện và lựa chọn mô hình:** thử nghiệm và so sánh các nhóm
    kỹ thuật khác nhau trên cùng tập dữ liệu để chọn phương án phù hợp.

4.  **Đánh giá mô hình:** sử dụng các độ đo sai số dự báo tiêu chuẩn
    (MAE, RMSE, MAPE) với phương pháp kiểm định phù hợp cho dữ liệu
    chuỗi thời gian.

5.  **Tích hợp và trực quan hóa:** đưa kết quả dự báo lên giao diện để
    Phòng Điều phối tham khảo khi lập lịch ca, kèm cảnh báo các khung
    giờ dự báo vượt ngưỡng.

**6. Công nghệ mới áp dụng**

**Mô hình nền tảng cho chuỗi thời gian (Time Series Foundation Model --
TSFM)**

Đây là hướng tiếp cận mới nổi trong giai đoạn 2023--2025, khi các tổ
chức công nghệ lớn lần lượt công bố những mô hình được huấn luyện trước
trên khối lượng dữ liệu chuỗi thời gian đa lĩnh vực, tiêu biểu như
TimesFM (Google), Chronos (Amazon), Moirai (Salesforce), TimeGPT và
Lag-Llama. Điểm khác biệt so với cách làm truyền thống nằm ở chỗ: thay
vì huấn luyện một mô hình riêng cho từng chuỗi dữ liệu, TSFM áp dụng
kiến trúc Transformer và tư duy tiền huấn luyện quy mô lớn để có thể dự
báo ngay trên dữ liệu chưa từng gặp (zero-shot), hoặc chỉ cần rất ít dữ
liệu để tinh chỉnh (few-shot).

**Vì sao công nghệ này phù hợp với bài toán của Ways Station**

Doanh nghiệp mở chi nhánh liên tục --- tăng từ khoảng 22 lên 34+ chi
nhánh trong chưa đầy hai năm. Mỗi chi nhánh mới khai trương đều không có
dữ liệu lịch sử, trong khi đây lại chính là thời điểm cần dự báo lưu
lượng nhất để bố trí nhân sự. Các mô hình thống kê và học sâu truyền
thống đều yêu cầu một lượng dữ liệu lịch sử đủ dài mới huấn luyện được,
nên không xử lý được tình huống này.

TSFM cho phép dự báo ngay từ những ngày đầu vận hành của chi nhánh mới
dựa trên năng lực khái quát hóa đã học được từ pha tiền huấn luyện, sau
đó tinh chỉnh dần khi dữ liệu tích lũy đủ. Đây là năng lực đặc thù mà
các nhóm kỹ thuật cũ không có, và cũng là lý do đề tài lựa chọn hướng
công nghệ này thay vì chỉ áp dụng mô hình dự báo thông thường.

**Các nhóm kỹ thuật dự kiến khảo sát và so sánh**

Ở giai đoạn thuyết minh, đề tài liệt kê các nhóm kỹ thuật tiềm năng,
chưa khẳng định phương án cuối cùng vì chưa có kết quả thực nghiệm:

  ------------------------------------------------------------------
  **Nhóm kỹ thuật** **Đại diện**          **Vai trò trong đề tài**
  ----------------- --------------------- --------------------------
  Mô hình nền tảng  Chronos, TimesFM,     Hướng công nghệ chính. Dự
  chuỗi thời gian   Lag-Llama             báo zero-shot cho chi
                                          nhánh mới; Lag-Llama cho
                                          ra phân phối xác suất kèm
                                          khoảng bất định, hữu ích
                                          khi bố trí nhân sự

  Thống kê chuỗi    ARIMA, SARIMA,        Mô hình cơ sở (baseline)
  thời gian         Prophet               để đối chiếu, kiểm chứng
                                          TSFM thực sự cho kết quả
                                          tốt hơn

  Học máy dạng cây  XGBoost, LightGBM     Phương án thay thế cho các
                                          chi nhánh đã có dữ liệu
                                          lịch sử dài, tận dụng tốt
                                          các đặc trưng bổ sung
  ------------------------------------------------------------------

**Lưu ý về phạm vi công nghệ:** đề tài sử dụng các mô hình nền tảng được
thiết kế riêng cho dữ liệu chuỗi thời gian, không sử dụng mô hình ngôn
ngữ lớn (LLM) tái lập trình cho bài toán dự báo. Các nghiên cứu gần đây
cho thấy hướng tái sử dụng LLM cho chuỗi thời gian chưa mang lại lợi ích
rõ rệt so với các mô hình chuyên dụng đơn giản hơn.

**Phương án dự phòng:** nếu mô hình nền tảng không đạt sai số kỳ vọng
trên dữ liệu thực tế của doanh nghiệp, đề tài sẽ chuyển sang nhóm học
máy dạng cây kết hợp đặc trưng thời gian. Việc dự trù phương án thay thế
nhằm bảo đảm tính khả thi của cam kết mà không phải điều chỉnh phạm vi
đề tài.

**7. Liên kết với hạ tầng đầu tư ở đồ án môn học**

Bài thực hành không phải một đề tài độc lập mà được xây dựng trên chính
hạ tầng được đầu tư ở đồ án môn học. Bảng dưới đây ánh xạ từng thành
phần hạ tầng sang vai trò của nó trong bài toán dự báo:

  ------------------------------------------------------------------
  **Lớp năng     **Thành phần đã đầu  **Vai trò trong bài toán dự
  lực**          tư**                 báo**
  -------------- -------------------- ------------------------------
  \(5\) Data     Kho dữ liệu tập      Cung cấp dữ liệu lịch sử
  Platform --    trung, quy trình     check-in đã được hợp nhất từ
  Phần mềm       ETL/ELT              34+ chi nhánh --- nguồn đầu
                                      vào để huấn luyện và tinh
                                      chỉnh mô hình

  \(5\) Data     Data quality rules,  Bảo đảm dữ liệu đầu vào thống
  Platform --    metadata standards   nhất về chuẩn giữa các chi
  Quản trị                            nhánh; chất lượng dữ liệu
                                      quyết định trực tiếp độ chính
                                      xác dự báo

  \(4\) App &    API Gateway,         Thu thập dữ liệu trạng thái từ
  Integration -- middleware           các hệ thống dịch vụ; đưa kết
  Phần mềm                            quả dự báo tới giao diện của
                                      Phòng Điều phối

  \(4\) App &    AuthN/Z, phân quyền  Kiểm soát ai được xem kết quả
  Integration -- theo vai trò         dự báo của chi nhánh nào
  Bảo mật                             
  ------------------------------------------------------------------

**Quan hệ phụ thuộc:** nếu không đầu tư lớp (5), dữ liệu vận hành vẫn
nằm rời rạc trong các tệp Excel theo từng ca và từng chi nhánh, không đủ
điều kiện để huấn luyện mô hình. Nếu không đầu tư lớp (4), kết quả dự
báo không có kênh để đưa tới người sử dụng trong quy trình làm việc hằng
ngày. Bài thực hành vì vậy chỉ khả thi khi hạ tầng ở đồ án môn học đã
được triển khai.

**Hướng mở rộng tiềm năng:** cùng nền tảng dữ liệu và cùng lớp mô hình
dự báo có thể được tái sử dụng cho các bài toán khác của doanh nghiệp,
chẳng hạn dự báo nhu cầu nhập hàng hóa tại quầy hoặc lập lịch bảo trì
thiết bị theo cường độ sử dụng. Các hướng này nằm ngoài phạm vi đề tài
lần này nhằm bảo đảm chiều sâu cho một bài toán duy nhất, nhưng cho thấy
giá trị đầu tư ban đầu có thể được khấu hao trên nhiều ứng dụng về sau.

**8. Giá trị mang lại**

- **Với Phòng Điều phối:** chuyển từ xử lý ca thiếu người sang lập lịch
  chủ động dựa trên dự báo, giảm tần suất phải tuyển thời vụ gấp.

- **Với Quản lý chi nhánh và khu vực:** có căn cứ định lượng để đề xuất
  nhân sự cho chi nhánh phụ trách thay vì dựa hoàn toàn vào kinh nghiệm.

- **Với doanh nghiệp:** tối ưu chi phí nhân sự theo lưu lượng thực tế và
  duy trì chất lượng phục vụ ổn định ở khung giờ cao điểm.

- **Với khách hàng:** giảm thời gian chờ được phục vụ tại các khung giờ
  đông.

**9. KPI đề xuất**

*Các chỉ số dưới đây là mục tiêu cam kết, cần khảo sát để xác lập giá
trị hiện trạng (baseline) khi bắt đầu triển khai; chưa phải số liệu đã
đo được tại doanh nghiệp.*

- Sai số phần trăm tuyệt đối trung bình (MAPE) của dự báo lưu lượng dưới
  15% trên tập kiểm thử.

- Tầm dự báo tối thiểu 7 ngày, đủ để Phòng Điều phối hoàn tất chu trình
  lập lịch ca.

- Giảm tỷ lệ ca phải bổ sung nhân sự phát sinh trong ngày so với hiện
  trạng.

- Độ trễ cập nhật kết quả dự báo không quá 24 giờ kể từ khi có dữ liệu
  mới.

**PHẦN 4. DANH SÁCH TÀI LIỆU KHẢO SÁT / THAM KHẢO**

Tài liệu được phân thành ba nhóm theo mức độ tin cậy và vai trò sử dụng.
Mọi nguồn trực tuyến đều ghi kèm đường dẫn và ngày truy cập; các nhận
định trong Phần 1 đều dẫn về nguồn cụ thể trong danh mục này.

**A. Khảo sát thực tế (nguồn sơ cấp)**

**Phương pháp:** thành viên nhóm đã trực tiếp trải nghiệm dịch vụ và
tiếp cận quy trình vận hành của Ways Station thông qua quá trình ứng
tuyển và tìm hiểu tại chi nhánh. Các thông tin về cơ cấu tổ chức, hệ
thống phần mềm đang sử dụng và quy trình nghiệp vụ trong Phần 1 được ghi
nhận từ nguồn này.

**Phạm vi sử dụng:** nhóm chỉ sử dụng thông tin ở mức mô tả cơ cấu và
quy trình phục vụ mục đích học thuật. Nhóm không sử dụng và không công
bố dữ liệu kinh doanh, dữ liệu khách hàng hay tài liệu nội bộ của doanh
nghiệp trong báo cáo này.

**Nội dung ghi nhận được:** cơ cấu phòng ban và cơ chế hỗ trợ theo tổng
đài phân nhánh; danh mục các hệ thống phần mềm đang vận hành; quy trình
bàn giao ca và lập báo cáo; quy trình đăng ký hội viên và check-in bằng
Face ID; quy trình xử lý sự vụ tại chi nhánh.

**B. Nguồn công khai chính chủ từ doanh nghiệp**

**Vai trò:** xác định danh mục dịch vụ, quy mô, giá dịch vụ và các mốc
phát triển. Ngày truy cập: 17/08/2026.

**\[1\]** Ways Station. *Trang chủ chính thức*.
<https://www.waysstation.vn/> (truy cập 17/08/2026).

**\[2\]** Ways Station. *Ways Station Hub -- không gian học tập và làm
việc*. <https://hub.waysstation.vn/> (truy cập 17/08/2026). --- Giá
25.000đ/4 giờ/người; địa điểm 262 Dương Quảng Hàm, Gò Vấp; giờ hoạt động
24/24, quầy thu ngân 6h00--2h00.

**\[3\]** Ways Station. *Danh sách chi nhánh*.
<https://diachi.waysstation.vn/> (truy cập 17/08/2026). --- Địa chỉ và
tổ hợp dịch vụ từng chi nhánh.

**\[4\]** Ways Station. *Cổng tuyển dụng chính thức*.
<https://diachi.ways.vn/tuyendung> (truy cập 17/08/2026). --- Mô tả quy
trình bàn giao ca và yêu cầu báo cáo số lượng bàn--máy theo khung giờ
chẵn.

**\[5\]** Ways Station. *Tuyển dụng Quản lý ca khu vực Tân Bình -- Tân
Phú*.
[waysstation.vn](https://waysstation.vn/%F0%9F%92%BC-ways-station-tuyen-dung-quan-ly-ca-quan-tan-binh-tan-phu/)
(truy cập 17/08/2026). --- Phân cấp quản lý; yêu cầu lập báo cáo trên
Google Drive và Excel.

**\[6\]** Ways Station. *Tuyển thời vụ ngắn hạn*.
<https://td.ways.vn/tv> (truy cập 17/08/2026). --- Cơ chế bố trí nhân sự
linh hoạt theo ca trống trong khu vực.

**\[7\]** Ways Station. *Khai trương phòng gym mới chi nhánh Quang
Trung*.
[waysstation.vn](https://waysstation.vn/khai-truong-phong-gym-moi-chi-nhanh-quang-trung/)
(truy cập 17/08/2026). --- Mốc 12/2023 và mục tiêu mở rộng chuỗi.

**C. Nguồn thứ cấp --- dùng để đối chiếu chéo**

**Vai trò và giới hạn:** các nguồn dưới đây là cổng tuyển dụng, trang
tra cứu doanh nghiệp và nền tảng đánh giá của bên thứ ba. Nhóm chỉ dùng
để đối chiếu quy mô chi nhánh qua từng thời điểm và xác định mô hình
pháp lý, không dùng làm căn cứ khẳng định. Khi số liệu giữa các nguồn
chênh lệch, nhóm ghi nhận biên độ thay vì chọn một con số duy nhất.

**\[8\]** MaSoThue. *Tra cứu thông tin các hộ kinh doanh mang tên Ways
Station*.
[https://masothue.com/](https://masothue.com/083097012959-ho-kinh-doanh-ways-station-dh)
(truy cập 17/08/2026). --- Căn cứ xác định mô hình đa hộ kinh doanh; ghi
nhận các chủ thể WAYS STATION DH, GV, QT, N.V.L, GYM với mã số thuế
riêng.

**\[9\]** VietnamWorks. *Hồ sơ nhà tuyển dụng Ways Station*.
<https://www.vietnamworks.com/nha-tuyen-dung/ways-station-c409679> (truy
cập 17/08/2026). --- Ghi nhận 30+ chi nhánh trên 11 quận.

**\[10\]** Vieclam24h. *Danh sách tin tuyển dụng Ways Station*.
<https://vieclam24h.vn/danh-sach-tin-tuyen-dung-ways-station-ntd5989966p122.html>
(truy cập 17/08/2026). --- Ghi nhận 32 chi nhánh tại thời điểm đăng tin.

**\[11\]** YBOX. *Tin tuyển dụng Ways Station 2024*.
[ybox.vn](https://ybox.vn/tuyen-dung/hcm-he-thong-the-thao-giai-tri-ways-station-tuyen-dung-nhan-vien-thiet-ke-3d-kiem-nghiem-thu-cong-trinh-giam-sat-camera-nhap-lieu-phuc-vu-thu-ngan-giu-xe-full-time-2024-6741a7abcd2058080faeadde)
(truy cập 17/08/2026). --- Ghi nhận 25 chi nhánh (2024); phân loại quy
mô doanh nghiệp vừa.

**\[12\]** Eagle Fitness. *Hệ thống phòng gym Ways Station tại TP.HCM*.
<https://www.eaglefitness.vn/ways-station/> (truy cập 17/08/2026). ---
Ghi nhận 22 chi nhánh và khu vực phân bố.

**D. Tài liệu tham khảo cho phần thực hành**

**Vai trò:** tài liệu kỹ thuật về bài toán dự báo chuỗi thời gian và các
mô hình nền tảng, dùng để mô tả đúng bản chất công nghệ và các kỹ thuật
dự kiến khảo sát. Nhóm sẽ bổ sung và cập nhật danh mục này trong quá
trình thực hiện bài thực hành.

**\[13\]** Hyndman, R.J. & Athanasopoulos, G. *Forecasting: Principles
and Practice*, 3rd ed. OTexts, 2021. \[Online\]. Available:
<https://otexts.com/fpp3/> --- Giáo trình tham chiếu về dự báo chuỗi
thời gian và các độ đo sai số.

**\[14\]** Taylor, S.J. & Letham, B. *Forecasting at Scale*. The
American Statistician, 2018. --- Cơ sở kỹ thuật của Prophet, mô hình dự
báo có xử lý tính mùa vụ và ngày lễ.

**\[15\]** Ansari, A.F. et al. *Chronos: Learning the Language of Time
Series*. Transactions on Machine Learning Research, 2024. \[Online\].
Available: <https://arxiv.org/abs/2403.07815> --- Mô hình nền tảng chuỗi
thời gian của Amazon.

**\[16\]** Das, A., Kong, W., Sen, R. & Zhou, Y. *A Decoder-Only
Foundation Model for Time-Series Forecasting*. ICML, 2024. \[Online\].
Available: <https://arxiv.org/abs/2310.10688> --- Cơ sở kỹ thuật của
TimesFM (Google).

**\[17\]** Rasul, K. et al. *Lag-Llama: Towards Foundation Models for
Probabilistic Time Series Forecasting*, 2023. \[Online\]. Available:
<https://arxiv.org/abs/2310.08278> --- Mô hình mã nguồn mở, cho ra dự
báo dạng phân phối xác suất.

*Ghi chú: nhóm sẽ bổ sung tài liệu kỹ thuật chi tiết cho mô hình được
lựa chọn sau khi hoàn tất bước khảo sát và so sánh trong bài thực hành.*

**E. Ghi chú về phương pháp và độ tin cậy**

- **Phân định rõ nguồn khảo sát và suy luận:** cơ cấu tổ chức, danh mục
  hệ thống phần mềm và các quy trình vận hành trong Phần 1 được ghi nhận
  từ khảo sát thực tế (mục A). Các nhận định mang tính suy luận đã được
  ghi nhãn rõ trong mục 1.6.

- **Về ngày thành lập:** không xác định được mốc thành lập chính thức vì
  doanh nghiệp vận hành theo mô hình nhiều hộ kinh doanh độc lập, không
  có pháp nhân mẹ được công bố \[8\]. Nhóm không suy đoán mốc này.

- **Về số lượng chi nhánh:** các nguồn ghi nhận 22 → 25 → 30+ → 32 → 34+
  ở những thời điểm khác nhau \[9\]--\[12\]. Nhóm trình bày dưới dạng
  biên độ và mốc thời gian thay vì khẳng định một con số.

- **Về các chỉ số KPI:** dự án chưa có số liệu vận hành thực tế của
  doanh nghiệp. Mọi KPI đề xuất ở các bước sau sẽ được xác lập dưới dạng
  mục tiêu cam kết cần khảo sát baseline khi triển khai, không phải số
  liệu đã đo được.

- **Về nguồn không sử dụng:** nhóm không dùng Wikipedia, blog cá nhân,
  diễn đàn hay nội dung do công cụ AI sinh ra làm nguồn dẫn chứng.

- **Về bảo mật thông tin doanh nghiệp:** nhóm không đưa vào báo cáo bất
  kỳ tài liệu, dữ liệu kinh doanh hay thông tin khách hàng nào mà doanh
  nghiệp không công bố công khai.
