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
  Điều này thể hiện ngay trong tài liệu đào tạo nội bộ, vốn được biên
  soạn riêng theo từng cụm dịch vụ: \'Thu ngân Net + Bida\', \'Thu ngân
  Net + Hub\', \'Thu ngân Gym\'.

**1.4. Cơ cấu tổ chức**

Cơ cấu được xác định trực tiếp từ tài liệu đào tạo nội bộ dành cho nhân
viên. Hệ thống vận hành một tổng đài hỗ trợ duy nhất (0889 555 559) phân
nhánh theo phím tới từng phòng ban chức năng:

  -----------------------------------------------------------------
  **Bộ phận**      **Phạm vi phụ trách (theo tài liệu nội bộ)**
  ---------------- ------------------------------------------------
  Phòng Nhân sự    Tuyển dụng, đào tạo, hướng dẫn ký quỹ, cấp phát
  (phím 2)         đồng phục, ghi nhận công, tính lương; xử lý yêu
                   cầu đổi vị trí/chi nhánh/ca làm; thủ tục thôi
                   việc. Kênh email: hr@waysstation.vn

  Phòng Điều phối  Lịch làm việc, xử lý tình huống ca sau chưa tới,
  (phím 3)         bố trí học việc, ca làm phát sinh, nghỉ phép;
                   lấy vân tay và chấm công in/out

  Bộ phận Kho hàng Vật tư, hàng hóa tại chi nhánh; đồng thời hỗ trợ
  (phím 8)         đăng nhập phần mềm MODUN gym và ACB portal

  Quản lý chi      Tiếp nhận báo cáo cuối ca; xử lý sự vụ phát
  nhánh (QLCN)     sinh; là đầu mối tiếp nhận ảnh biên bản gửi qua
                   Zalo

  Quản lý ca /     Làm việc 9 tiếng/ca (có trực đêm); giám sát nhân
  Trưởng ca        viên, xử lý sự vụ, lập báo cáo trên Google Drive
                   và Excel

  Nhân viên vận    Thu ngân, Phục vụ (net/bida/gym/cầu lông), Giữ
  hành             xe, Nhập liệu, Giám sát camera --- ca cố định
                   4--9 tiếng; ca đêm có thể kiêm nhiệm nhiều vị
                   trí tùy chi nhánh
  -----------------------------------------------------------------

**Quy trình gia nhập:** ứng viên đăng ký ứng tuyển → nhận bộ tài liệu
nghiệp vụ theo vị trí (yêu cầu \'cần học thuộc\') → học việc tại chi
nhánh → nếu đạt sẽ được nhận làm chính thức. Nhân sự thời vụ được bố trí
linh hoạt theo ca trống của các chi nhánh trong khu vực đã đăng ký.

**1.5. Quy trình nghiệp vụ chính**

**(a) Quy trình phục vụ khách hàng tại chi nhánh**

Khách đăng ký gói / đặt chỗ (tại quầy hoặc qua ứng dụng) → Check-in → Sử
dụng dịch vụ tính theo giờ hoặc theo gói → Thanh toán tiền mặt hoặc
chuyển khoản qua ACB portal → Ghi nhận vào báo cáo ca.

**(b) Quy trình tạo hội viên Gym**

Nhân viên dẫn khách tham quan 5 khu vực phòng tập (quầy lễ tân và phòng
thay đồ, khu khởi động, khu tạ, khu tạ khối, khu cardio) → tư vấn gói
tập tại quầy → khách chọn gói → nhân viên đưa phiếu giấy để khách điền
thông tin → nhập thông tin tạo hội viên trên hệ thống → lấy Face ID cho
khách → thu tiền mặt hoặc chuyển khoản. Khách check-in các lần sau bằng
Face ID, không dùng thẻ hội viên.

**(c) Quy trình bàn giao và báo cáo ca**

- Chấm công đầu ca bằng vân tay; kiểm tra máy lạnh, thiết bị, hàng hóa,
  tủ nước, hạn sử dụng

- Xử lý tab dịch vụ cho khách; mở/đóng bàn bida; theo dõi camera

- **Báo cáo số lượng bàn -- máy theo khung giờ chẵn** (thao tác đếm và
  ghi thủ công, lặp lại nhiều lần trong ca)

- Kiểm kê tiền -- vật tư -- hàng hóa cuối ca, gửi báo cáo cho Quản lý
  chi nhánh

- Nhận/bàn giao sổ giao ca, chìa khóa, tiền, vật dụng giá trị giữa các
  ca

**(d) Quy trình xử lý sự vụ -- ví dụ: khách làm mất thẻ giữ xe**

Đây là quy trình thể hiện rõ nhất mức độ thủ công trong vận hành: nhân
viên lập biên bản giấy → chụp ảnh CCCD, cà vẹt xe, biên bản, thân xe,
biển số và hình ảnh khách → gửi toàn bộ qua Zalo cho Quản lý → ghi số
thẻ bị mất vào sổ giao ca giấy → nộp biên bản cho Thu ngân. Tùy trường
hợp giấy tờ, xe hoặc cà vẹt có thể bị tạm giữ 24--36 giờ, và việc theo
dõi thời hạn này cũng được bàn giao thủ công giữa các ca.

**1.6. Hiện trạng số hóa**

**(a) Bản đồ các hệ thống đang sử dụng**

Khảo sát tài liệu nội bộ cho thấy Ways Station đang vận hành song song
nhiều hệ thống độc lập, trong đó một phần đáng kể vẫn là quy trình thủ
công trên giấy:

  -----------------------------------------------------------------
  **Hệ thống /     **Chức năng**          **Đặc điểm**
  công cụ**                               
  ---------------- ---------------------- -------------------------
  Nhân sự Ways     Quản lý thông tin nhân Nền tảng web riêng cho
  (ns.ways.vn)     sự, tra cứu chức năng  khối nhân sự
                   nội bộ                 

  PM MODUN gym     Quản lý hội viên và    Phần mềm riêng, cần hỗ
                   gói tập mảng Gym       trợ đăng nhập từ Bộ phận
                                          Kho hàng

  ACB portal       Cổng thanh toán chuyển Hệ thống của bên thứ ba,
                   khoản                  tách rời khỏi hệ thống
                                          bán hàng

  Face ID          Check-in hội viên Gym  Chỉ áp dụng cho mảng Gym

  Máy chấm công    Chấm công in/out nhân  Thiết bị riêng, do Phòng
  vân tay          viên                   Điều phối quản lý

  Google Drive /   Lập báo cáo ca của     File rời rạc theo từng
  Excel            Quản lý ca             ca, từng chi nhánh

  Zalo             Gửi ảnh biên bản, sự   Kênh cá nhân, không lưu
                   vụ cho Quản lý         vết hệ thống

  Sổ giao ca, biên Ghi nhận sự vụ, bàn    Hoàn toàn thủ công, không
  bản, phiếu giấy  giao ca, đăng ký hội   số hóa
                   viên                   
  -----------------------------------------------------------------

**(b) Ba điểm nghẽn chính**

1.  **Phân mảnh nền tảng ứng dụng ---** mỗi mảng dịch vụ và mỗi nghiệp
    vụ chạy trên một hệ thống độc lập (MODUN gym, ACB portal,
    ns.ways.vn, Face ID, máy chấm công), không có lớp tích hợp chung.
    Chính tài liệu đào tạo cũng được biên soạn tách riêng theo cụm dịch
    vụ, phản ánh sự thiếu thống nhất về quy trình và hệ thống giữa các
    mảng.

2.  **Dữ liệu vận hành thủ công và không truy vết được ---** báo cáo ca
    lập bằng Excel/Google Drive theo từng chi nhánh; số lượng bàn--máy
    đếm và ghi tay theo khung giờ chẵn; sự vụ được gửi qua Zalo cá nhân
    và ghi vào sổ giấy. Không có nguồn dữ liệu tập trung để phân tích tỷ
    lệ lấp đầy, doanh thu theo khung giờ hay hiệu quả từng chi nhánh.

3.  **Cấu trúc phân tán làm khuếch đại độ phức tạp khi mở rộng ---** mỗi
    chi nhánh là một hộ kinh doanh độc lập với mã số thuế riêng, trong
    khi chuỗi tăng từ khoảng 22 lên 34+ chi nhánh trong chưa đầy hai năm
    và liên tục bổ sung loại hình dịch vụ mới. Mô hình quản lý thủ công
    hiện tại sẽ ngày càng khó mở rộng tương ứng.

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

**Vấn đề cần giải quyết**

Ways Station đang vận hành song song nhiều hệ thống độc lập (MODUN gym,
ACB portal, ns.ways.vn, Face ID, chấm công vân tay) cùng với các quy
trình thủ công trên giấy và Zalo. Dữ liệu vận hành phân tán theo từng
chi nhánh --- vốn là các hộ kinh doanh độc lập --- nên không thể tổng
hợp kịp thời cho quyết định kinh doanh. Trong bối cảnh chuỗi mở rộng
nhanh và vừa bổ sung mảng dịch vụ mới, mô hình này làm tăng chi phí vận
hành và rủi ro sai sót.

**Mục tiêu đầu tư**

- **Lớp (4):** xây dựng lớp tích hợp (API Gateway + middleware) kết nối
  các hệ thống hiện có thành nền tảng thống nhất; số hóa các nghiệp vụ
  đang thực hiện thủ công (báo cáo ca, biên bản sự vụ, đăng ký hội
  viên).

- **Lớp (5):** xây dựng kho dữ liệu tập trung và quy trình ETL thu thập
  dữ liệu từ toàn hệ thống; thay thế báo cáo ca thủ công bằng dashboard
  tự động cho quản lý chi nhánh và khu vực.

**Đối tượng thụ hưởng**

  ------------------------------------------------------------------
  **Nhóm**         **Quy trình liên     **Lợi ích kỳ vọng**
                   quan**               
  ---------------- -------------------- ----------------------------
  Nhân viên ca     Bàn giao ca, báo cáo Giảm thao tác thủ công lặp
  trực             bàn--máy theo khung  lại; dữ liệu ghi nhận tự
                   giờ, lập biên bản sự động thay vì đếm và ghi tay
                   vụ                   

  Quản lý chi      Tổng hợp báo cáo     Xem dashboard tổng hợp; sự
  nhánh / khu vực  cuối ca, tiếp nhận   vụ có lưu vết trên hệ thống
                   sự vụ qua Zalo       thay vì tin nhắn cá nhân

  Ban điều hành    Quyết định mở rộng,  Có dữ liệu tỷ lệ lấp đầy,
  chuỗi            bố trí nhân sự theo  doanh thu theo khung giờ và
                   khung giờ            theo chi nhánh

  Khách hàng       Đăng ký gói, đặt     Một tài khoản dùng chung
                   chỗ, check-in        nhiều dịch vụ; giảm khâu
                                        điền phiếu giấy
  ------------------------------------------------------------------

**Phạm vi KHÔNG bao gồm**

- Đầu tư mới phần cứng máy chủ, thiết bị đầu cuối, hạ tầng mạng chi
  nhánh (giả định đã có sẵn)

- Ba lớp năng lực còn lại (1), (2), (3) --- chỉ kế thừa, không đầu tư
  mới trong phạm vi dự án

**PHẦN 3. DANH SÁCH TÀI LIỆU KHẢO SÁT / THAM KHẢO**

Thông tin trong báo cáo được thu thập từ ba nhóm nguồn: tài liệu nội bộ
do thành viên nhóm tiếp cận được, nguồn công khai chính chủ từ doanh
nghiệp, và nguồn thứ cấp dùng để đối chiếu.

**A. Tài liệu nội bộ của doanh nghiệp**

*Bộ tài liệu đào tạo nghiệp vụ cấp cho ứng viên sau khi đăng ký ứng
tuyển, sử dụng trong giai đoạn học việc trước khi được nhận chính thức.
Đây là nguồn quan trọng nhất, cung cấp thông tin về cơ cấu tổ chức, hệ
thống phần mềm đang dùng và quy trình vận hành thực tế.*

**\[1\]** Tài liệu nghiệp vụ vị trí GIỮ XE --- quy trình xử lý khi khách
làm mất thẻ xe, cơ chế lập biên bản và bàn giao.

**\[2\]** Tài liệu nghiệp vụ vị trí PHỤC VỤ BIDA --- phân biệt loại bàn,
tiêu chuẩn nhiệt độ bàn, quy trình vệ sinh thiết bị.

**\[3\]** Tài liệu nghiệp vụ vị trí PHỤC VỤ CẦU LÔNG.

**\[4\]** Tài liệu nghiệp vụ vị trí PHỤC VỤ GYM --- nội quy phòng tập,
quy trình hỗ trợ khách.

**\[5\]** Tài liệu nghiệp vụ vị trí PHỤC VỤ NET --- hướng dẫn chế biến
món, danh mục và giá hàng hóa.

**\[6\]** Tài liệu nghiệp vụ vị trí THU NGÂN GYM --- quy trình dẫn khách
tham quan, tư vấn gói tập, tạo hội viên và lấy Face ID; danh mục vật tư
phòng tập.

**\[7\]** Tài liệu nghiệp vụ vị trí THU NGÂN NET + BIDA --- bảng giá
hàng hóa, công thức tính giá món, nội quy phòng, quy trình kiểm tra
phòng.

**\[8\]** Tài liệu nghiệp vụ vị trí THU NGÂN NET + HUB --- quy định
phòng Hub, danh mục hàng bán, hàng miễn phí và hàng cho mượn.

**B. Nguồn công khai chính chủ từ doanh nghiệp**

**\[9\]** Ways Station -- Trang chủ chính thức.
<https://www.waysstation.vn/>

**\[10\]** Ways Station Hub -- Trang dịch vụ không gian học tập và làm
việc. <https://hub.waysstation.vn/> --- Giá dịch vụ, địa điểm, giờ hoạt
động, tiện ích.

**\[11\]** Ways Station -- Danh sách chi nhánh.
<https://diachi.waysstation.vn/>

**\[12\]** Ways Station -- Cổng tuyển dụng chính thức.
<https://diachi.ways.vn/tuyendung> --- Mô tả quy trình bàn giao ca và
báo cáo số lượng bàn--máy theo khung giờ.

**\[13\]** Ways Station -- Thông báo tuyển dụng Quản lý ca.
[waysstation.vn](https://waysstation.vn/%F0%9F%92%BC-ways-station-tuyen-dung-quan-ly-ca-quan-tan-binh-tan-phu/)
--- Phân cấp quản lý; yêu cầu lập báo cáo trên Google Drive, Excel.

**\[14\]** Ways Station -- Tuyển thời vụ ngắn hạn.
<https://td.ways.vn/tv> --- Cơ chế bố trí nhân sự linh hoạt theo ca
trống.

**\[15\]** Ways Station -- Tin khai trương chi nhánh Lê Lợi và Quang
Trung.
[waysstation.vn](https://waysstation.vn/khai-truong-phong-gym-moi-chi-nhanh-quang-trung/)
--- Mốc phát triển và mục tiêu mở rộng chuỗi.

**C. Nguồn thứ cấp (đối chiếu quy mô và pháp lý)**

**\[16\]** MaSoThue -- Tra cứu thông tin các hộ kinh doanh mang thương
hiệu Ways Station.
[https://masothue.com/](https://masothue.com/083097012959-ho-kinh-doanh-ways-station-dh)
--- Căn cứ xác định mô hình đa hộ kinh doanh.

**\[17\]** VietnamWorks -- Hồ sơ nhà tuyển dụng Ways Station.
<https://www.vietnamworks.com/nha-tuyen-dung/ways-station-c409679> ---
Quy mô 30+ chi nhánh trên 11 quận.

**\[18\]** CareerViet -- Hồ sơ nhà tuyển dụng Ways Station.
<https://careerviet.vn/vi/nha-tuyen-dung/ways-station.35AA15F2.html>

**\[19\]** Vieclam24h -- Tin tuyển dụng Ways Station.
<https://vieclam24h.vn/danh-sach-tin-tuyen-dung-ways-station-ntd5989966p122.html>
--- Ghi nhận 32 chi nhánh; địa chỉ trụ sở.

**\[20\]** YBOX / JobOKO -- Tin tuyển dụng Ways Station 2024.
[https://ybox.vn](https://ybox.vn/tuyen-dung/hcm-he-thong-the-thao-giai-tri-ways-station-tuyen-dung-nhan-vien-thiet-ke-3d-kiem-nghiem-thu-cong-trinh-giam-sat-camera-nhap-lieu-phuc-vu-thu-ngan-giu-xe-full-time-2024-6741a7abcd2058080faeadde)
--- Quy mô 25 chi nhánh (2024); phân loại doanh nghiệp vừa.

**\[21\]** Eagle Fitness -- Danh sách hệ thống phòng gym Ways Station.
<https://www.eaglefitness.vn/ways-station/> --- Quy mô 22 chi nhánh và
khu vực phân bố.

**\[22\]** Trustindex -- Tổng hợp đánh giá khách hàng về Ways Station.
<https://www.trustindex.io/reviews/waysstation.vn> --- Phản hồi thực tế
về dịch vụ Hub và chất lượng vận hành.

**D. Ghi chú về độ tin cậy của dữ liệu**

- Cơ cấu tổ chức, danh mục hệ thống phần mềm và các quy trình vận hành
  trong Phần 1 được trích trực tiếp từ tài liệu đào tạo nội bộ
  \[1\]--\[8\], không phải suy luận.

- Không xác định được ngày thành lập chính thức do doanh nghiệp vận hành
  theo mô hình nhiều hộ kinh doanh độc lập, không có pháp nhân mẹ được
  công bố.

- Số lượng chi nhánh chênh lệch giữa các nguồn do công bố ở các thời
  điểm khác nhau; nhóm sử dụng con số từ nguồn gần nhất và ghi nhận biên
  độ 22--38 để thể hiện tốc độ tăng trưởng.

- Tài liệu nội bộ được cấp cho ứng viên trong quá trình tuyển dụng và
  học việc; nhóm chỉ sử dụng phần thông tin liên quan đến cơ cấu tổ chức
  và quy trình vận hành phục vụ mục đích học thuật.
