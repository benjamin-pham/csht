**LỚP NĂNG LỰC (3) -- AN TOÀN THÔNG TIN & ĐỊNH DANH (SECURITY +
IDENTITY)**

**1. Khái niệm**

**Security + Identity (An toàn thông tin & Định danh)** là một trong 5
lớp năng lực của bảng "Khung tham chiếu phổ biến" (slide 17), cùng với
Compute & Connectivity, Ops Platform, App & Integration Platform và Data
Platform. Ô giao giữa lớp này và cột Bảo mật ghi rõ đây là **"Lớp bao
trùm: identity + policy + detection/response cho (1)-(5)"** -- nghĩa là
Security + Identity vừa là một lớp năng lực riêng, vừa cung cấp định
danh, chính sách và năng lực phát hiện -- ứng phó cho cả bốn lớp còn
lại.

**Nguồn:** *bảng "Khung tham chiếu phổ biến", slide 17 -- Chương 2
(2.pdf)*

**Nửa Identity** của lớp này được triển khai bằng **quản lý danh tính và
truy cập (IAM)**: giải pháp "cấp quyền truy nhập an toàn vào các tài
nguyên công ty" như email, cơ sở dữ liệu, dữ liệu và ứng dụng cho các
thực thể đã được xác minh. IAM hoạt động theo hai pha: **quản lý danh
tính** đối chiếu thông tin đăng nhập với cơ sở dữ liệu người dùng được
phép, rồi **quản lý truy cập** quyết định người dùng đã xác thực đó được
truy cập những tài nguyên nào, dựa trên các yếu tố như chức danh, mức
bảo mật và dự án được phân công. IAM dùng các chuẩn **SAML, OpenID
Connect (OIDC) và SCIM** để xác minh danh tính giữa các ứng dụng và nền
tảng khác nhau.

**Nguồn:** [[Microsoft Security -- Quản lý danh tính và truy nhập (IAM)
là
gì?]{.underline}](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-identity-access-management-iam)

**Cơ sở pháp lý tại Việt Nam.** Luật An ninh mạng số 116/2025/QH15 (ban
hành 10/12/2025, hiệu lực 01/7/2026) được xây dựng trên cơ sở **kế thừa,
hợp nhất các quy định còn phù hợp của Luật An ninh mạng 2018 và Luật An
toàn thông tin mạng 2015**. Luật quy định phân loại hệ thống thông tin
theo **5 cấp độ an ninh mạng** làm căn cứ áp dụng các biện pháp bảo vệ
tương ứng, trong đó hệ thống thông tin quan trọng về an ninh quốc gia ở
cấp độ 5; đồng thời khẳng định bảo đảm an ninh dữ liệu là bộ phận quan
trọng của bảo vệ an ninh mạng.

**Nguồn:** [[Luật An ninh mạng 2025 số 116/2025/QH15 (toàn
văn)]{.underline}](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-An-ninh-mang-2025-so-116-2025-QH15-666020.aspx)

**2. Vai trò**

  ----------------- --------------------------------------------------
  **Vai trò**       **Diễn giải theo tài liệu Microsoft Security**

  Cấp quyền truy    Cho phép các thực thể đã được xác minh truy nhập
  nhập an toàn      tài nguyên công ty: email, cơ sở dữ liệu, dữ liệu,
                    ứng dụng.

  Quyết định phạm   Sau khi xác thực, hệ thống xác định người dùng
  vi truy cập       được truy cập tài nguyên nào theo chức danh, mức
                    bảo mật và dự án được phân công.

  Cân bằng bảo mật  Để nhân viên hợp lệ làm việc thuận lợi, đồng thời
  với hiệu quả làm  ngăn truy cập trái phép -- đây là mục tiêu kép của
  việc              IAM.

  Ứng phó mối đe    Giúp tổ chức thích ứng với các mối đe dọa an ninh
  dọa đang biến đổi mạng ngày càng thay đổi.

  Bảo đảm tuân thủ  Cung cấp **vết kiểm tra (audit trail)** và kiểm
                    soát truy cập để đáp ứng các quy định về bảo vệ dữ
                    liệu.

  Nền cho MFA, SSO  MFA thêm bước xác minh ngoài mật khẩu; SSO đơn
  và RBAC           giản hoá truy cập nhiều hệ thống; RBAC cấp quyền
                    theo chức năng công việc.
  ----------------- --------------------------------------------------

**Nguồn:** [[Microsoft Security -- Quản lý danh tính và truy nhập (IAM)
là
gì?]{.underline}](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-identity-access-management-iam)

**3. Thành phần cấu thành (theo 5 miền của bảng slide 17)**

  -------------- ----------------------------------------------------
  **Miền (cột    **Thành phần của lớp Security + Identity**
  của bảng slide 
  17)**          

  Phần cứng      Appliance/sensor, HSM/TPM (nếu có), firewall/WAF
                 (on-premise).

  Phần mềm       IAM/SSO/MFA, PAM, EDR/XDR, SIEM/SOAR, DLP, KMS, quản
                 lý lỗ hổng (vuln mgmt).

  Mạng           ZTNA/VPN, IDS/IPS, đường đi qua WAF, phân đoạn mạng
                 / Zero Trust.

  Quản trị       Chính sách (policy), quản lý rủi ro & tuân thủ, rà
                 soát quyền truy cập (access review), kịch bản ứng
                 phó sự cố (IR playbook).

  Bảo mật        Lớp "bao trùm": identity + policy +
                 detection/response cho (1)-(5).
  -------------- ----------------------------------------------------

**Nguồn:** *bảng "Khung tham chiếu phổ biến", slide 17 -- Chương 2
(2.pdf) -- bảng này liệt kê nguyên văn các thành phần trên.*

**4. Đặc điểm kỹ thuật**

**(a) Xác thực và cấp quyền là hai bước khác nhau.** Bước **xác thực**
đối chiếu thông tin đăng nhập của người dùng với cơ sở dữ liệu những
người dùng được phép -- tức chứng minh "bạn là ai". Bước **cấp quyền**
mới quyết định người dùng đã xác thực được truy cập tài nguyên nào và
làm gì với tài nguyên đó, dựa trên chức danh, mức bảo mật, dự án được
phân công. Ngoài ra hệ thống lưu **vết kiểm tra (audit trail)** để phục
vụ điều tra và chứng minh tuân thủ. Vì vậy đăng nhập thành công không
đồng nghĩa với việc được phép truy cập mọi tài nguyên.

**Nguồn:** [[Microsoft Security -- Quản lý danh tính và truy nhập (IAM)
là
gì?]{.underline}](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-identity-access-management-iam)

**(b) Xác thực đa yếu tố (MFA).** MFA là "một quy trình bảo mật yêu cầu
nhiều hình thức xác minh để xác nhận danh tính của bạn", dựa trên ba
loại yếu tố: **thứ bạn biết** -- mật khẩu, mã khóa, mã PIN hoặc câu hỏi
bảo mật; **thứ bạn có** -- thiết bị di động, thẻ thông minh hoặc mã
thông báo phần cứng; **thứ thuộc về bạn** -- sinh trắc học như dấu vân
tay, quét khuôn mặt, nhận dạng giọng nói. Các phương thức xác minh gồm
ứng dụng xác thực, mã qua SMS/gọi thoại, sinh trắc học và mã thông báo
phần cứng, nhưng **không tương đương nhau về độ mạnh**: tài liệu khuyến
cáo "chọn các phương thức mạnh hơn SMS" vì SMS "vẫn có nguy cơ bị đánh
chặn", và giới thiệu **passkey -- thông tin xác thực FIDO** cùng MFA
không dùng mật khẩu như phương thức **chống lừa đảo qua mạng**.

**Nguồn:** [[Microsoft Security -- Xác thực đa yếu tố (MFA) là
gì?]{.underline}](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-multifactor-authentication-mfa)

**(c) Đăng nhập một lần (SSO) và liên kết danh tính bằng SAML.** SAML là
công nghệ cơ bản cho phép người dùng **đăng nhập một lần bằng một bộ
thông tin xác thực và truy nhập nhiều ứng dụng**. Cơ chế: **nhà cung cấp
danh tính (IdP)** xác minh người dùng khi họ đăng nhập, sau đó dùng SAML
chuyển dữ liệu xác thực đó cho **nhà cung cấp dịch vụ** đang điều hành
site/ứng dụng mà người dùng muốn truy cập. Vật mang thông tin là **xác
nhận SAML (SAML assertion)** -- một tài liệu XML chứa dữ liệu khẳng định
với nhà cung cấp dịch vụ rằng người đang đăng nhập đã được xác thực. Nhờ
đó doanh nghiệp vừa tăng cường bảo mật, vừa đơn giản hoá quy trình đăng
nhập cho nhân viên, đối tác và khách hàng.

**Nguồn:** [[Microsoft Security -- SAML (Ngôn ngữ đánh dấu xác nhận bảo
mật) là
gì?]{.underline}](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-security-assertion-markup-language-saml)

**(d) Quản lý quyền truy nhập đặc quyền (PAM) và nguyên tắc đặc quyền
tối thiểu.** PAM là **một giải pháp bảo mật danh tính** bảo vệ tổ chức
trước các mối đe dọa trên mạng, và là **một tập hợp con của IAM** -- tập
trung vào quy trình và công nghệ để bảo mật các **tài khoản đặc quyền**
(tài khoản siêu người dùng, tài khoản dịch vụ, tài khoản quản trị miền,
tài khoản khẩn cấp...). Các thực hành cốt lõi: **áp dụng chính sách cấp
đặc quyền tối thiểu cho mọi thứ và mọi người**; **cung cấp quyền truy
nhập vừa đúng lúc (just-in-time)** vào các tài nguyên quan trọng thay vì
để quyền cao thường trực; bảo mật **dựa trên vai trò**; và **giám sát
các phiên đặc quyền để hỗ trợ kiểm tra điều tra**.

**Nguồn:** [[Microsoft Security -- Quản lý quyền truy nhập đặc quyền
(PAM) là
gì?]{.underline}](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-privileged-access-management-pam)

**(e) Zero Trust -- hệ quy chiếu hiện đại của lớp Security + Identity.**
Zero Trust là **"một kiến trúc bảo mật yêu cầu xác minh danh tính nghiêm
ngặt đối với người dùng và thiết bị muốn truy cập vào tài nguyên"**,
hoạt động theo tư tưởng **"không bao giờ tin tưởng, luôn xác minh"**:
mọi yêu cầu truy cập đều phải xác thực liên tục và cấp quyền theo ngữ
cảnh. Mô hình gồm **5 trụ cột (theo CISA)**: **Danh tính** -- xác thực
người dùng và cấp quyền cho tài nguyên đã phê duyệt; **Thiết bị** --
kiểm tra mức tuân thủ chính sách bảo mật của từng thiết bị; **Mạng** --
áp dụng microsegmentation thay cho phân đoạn truyền thống; **Ứng dụng và
khối lượng công việc** -- xác minh liên tục thay vì tin cậy mặc định;
**Dữ liệu** -- phân loại và mã hóa dữ liệu, giám sát liên tục. Các công
nghệ thường dùng khi triển khai: MFA, IAM, microsegmentation và EDR.

**Nguồn:** [[VNPT Cloud -- Zero Trust là gì? 05 trụ cột cốt lõi của mô
hình bảo mật Zero
Trust]{.underline}](https://cloud.vnpt.vn/blog/zero-trust-la-gi-05-tru-cot-cot-loi-cua-mo-hinh-bao-mat-zero-trust-168)

**(f) Mã hoá và quản lý khoá.** **"Độ an toàn của bất kỳ hệ thống mật mã
nào cũng đều phụ thuộc vào độ an toàn của khóa"**, vì lý do đó khóa luôn
phải được bảo vệ ở mức cao nhất. Rủi ro điển hình: nếu dùng cùng một
khóa để mã hóa nhiều thông điệp trong thời gian dài, kẻ tấn công có thể
thu thập đủ bản mã rồi khám phá ra một phần hoặc toàn bộ khóa; và khi
một khóa bị lộ thì mọi thành phần còn dùng khóa đó đều bị nguy hiểm. Do
đó vấn đề quan trọng là **quản lý khóa (key management)** -- thuật ngữ
chỉ toàn bộ hoạt động liên quan đến một **vòng đời của khóa**: sinh
khóa, phân phối, sử dụng, lưu trữ và hủy bỏ khóa.

**Nguồn:** [[Tạp chí An toàn thông tin (Ban Cơ yếu Chính phủ) -- Tiêu
chuẩn quốc gia Việt Nam về Quản lý
khóa]{.underline}](https://antoanthongtin.vn/tin/tieu-chuan-quoc-gia-viet-nam-ve-quan-ly-khoa)

**(g) Phát hiện và ứng phó: EDR -- XDR -- SIEM.** **EDR** (phát hiện và
ứng phó điểm cuối) chỉ tập trung bảo vệ điểm cuối: giám sát thiết bị để
phát hiện hoạt động đáng ngờ và cho phép **cô lập thiết bị đã bị xâm
phạm**. **XDR** (phát hiện và phản hồi mở rộng) mở rộng phạm vi đó,
**thu thập dữ liệu từ điểm cuối, mạng, đám mây, email, ứng dụng SaaS và
danh tính vào một nền tảng thống nhất**. **SIEM** thu thập và phân tích
nhật ký, nhưng thường yêu cầu liên kết các sự cố một cách thủ công. Hai
lớp này **không thay thế nhau**: "XDR bổ trợ cho các giải pháp SIEM bằng
cách tăng cường khả năng giám sát này với quy trình phát hiện theo thời
gian thực, ứng phó tự động".

**Nguồn:** [[Microsoft Security -- Phát hiện và phản hồi mở rộng (XDR)
là
gì?]{.underline}](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-xdr)

**5. Rủi ro nhắm vào danh tính và cách kiểm soát**

**Các rủi ro có thể phát hiện được** ở tầng danh tính gồm: **tấn công dò
mật khẩu** (brute force), **đăng nhập từ IP ẩn danh** và **rò rỉ thông
tin đăng nhập**. Cách kiểm soát tương ứng là **chính sách truy cập thích
ứng dựa trên rủi ro**: khi phát hiện dấu hiệu vi phạm, hệ thống **chặn,
yêu cầu xác thực đa yếu tố và khắc phục rủi ro** theo thời gian thực;
việc phát hiện và tự động khắc phục tình trạng xâm phạm danh tính áp
dụng cho cả phương thức xác thực dùng mật khẩu lẫn không dùng mật khẩu.

**Nguồn:** [[Microsoft Security -- Bảo vệ Danh tính Microsoft
Entra]{.underline}](https://www.microsoft.com/vi-vn/security/business/identity-access/microsoft-entra-id-protection)

**6. Nghĩa vụ tuân thủ tại Việt Nam**

  ------------- ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Trục**      **Nghĩa vụ / nội dung liên quan đến **Nguồn (1 link)**
                Security + Identity**               

  An ninh mạng  Phân loại hệ thống thông tin theo 5 [[Luật An ninh mạng 2025 (116/2025/QH15)]{.underline}](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-An-ninh-mang-2025-so-116-2025-QH15-666020.aspx)
  theo cấp độ   cấp độ an ninh mạng để áp dụng biện 
                pháp bảo vệ tương ứng.              

  Yêu cầu an    Yêu cầu cơ bản về an toàn hệ thống  [[TCVN 11930:2017 (VSQI)]{.underline}](https://tieuchuan.vsqi.gov.vn/tieuchuan/view?sohieu=TCVN+11930%3A2017)
  toàn theo cấp thông tin theo từng cấp độ (yêu cầu 
  độ            quản lý và yêu cầu kỹ thuật).       

  Hồ sơ đề xuất Trình tự xác định cấp độ, lập hồ sơ [[Nghị định 85/2016/NĐ-CP]{.underline}](https://vanban.chinhphu.vn/?pageid=27160&docid=185601)
  cấp độ        đề xuất cấp độ và phương án bảo đảm 
                an toàn hệ thống thông tin.         

  Định danh &   Tài khoản định danh điện tử, dịch   [[Nghị định 69/2024/NĐ-CP]{.underline}](https://vanban.chinhphu.vn/?pageid=27160&docid=210491)
  xác thực điện vụ xác thực điện tử và điều kiện    
  tử            kết nối với Hệ thống định danh và   
                xác thực điện tử.                   

  Chữ ký điện   Yêu cầu với chữ ký điện tử, chứng   [[Nghị định 23/2025/NĐ-CP]{.underline}](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-23-2025-nd-cp-quy-dinh-ve-chu-ky-dien-tu-va-dich-vu-tin-cay-119250225073330307.htm)
  tử & dịch vụ  thư chữ ký điện tử và các dịch vụ   
  tin cậy       tin cậy.                            

  Dữ liệu cá    Quyền của chủ thể dữ liệu; cấm mua  [[Luật Bảo vệ dữ liệu cá nhân 2025 (91/2025/QH15)]{.underline}](https://chinhphu.vn/?pageid=27160&docid=214590&classid=1&typegroupid=3)
  nhân          bán dữ liệu cá nhân; mạng xã hội    
                không được yêu cầu giấy tờ định     
                danh có ảnh/video làm yếu tố xác    
                thực. Hiệu lực 01/01/2026.          

  Mật mã dân sự Điều kiện kinh doanh sản phẩm, dịch [[Nghị định
                vụ mật mã dân sự và xuất nhập khẩu  58/2016/NĐ-CP]{.underline}](https://thuvienphapluat.vn/van-ban/Thuong-mai/Nghi-dinh-58-2016-ND-CP-kinh-doanh-san-pham-dich-vu-mat-ma-dan-su-xuat-nhap-khau-mat-ma-dan-su-2016-315422.aspx)
                sản phẩm mật mã dân sự (liên quan   
                HSM, giải pháp mã hoá, thiết bị     
                VPN).                               
  ------------- ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**7. Kết luận -- quan hệ với 4 lớp năng lực còn lại**

**Security + Identity là lớp "bao trùm".** Theo đúng ghi chú của bảng
slide 17, lớp này cung cấp **identity + policy + detection/response**
cho cả 5 lớp năng lực (1)-(5). Đối chiếu cột Bảo mật của các hàng còn
lại trong cùng bảng cho thấy mỗi lớp đều phải có kiểm soát an toàn nội
tại của riêng nó: lớp Compute & Connectivity có hardening, segmentation
nền, firewall baseline, TLS/VPN, firmware/patch nền; lớp Ops Platform có
audit/log integrity, kiểm soát quyền admin, quy trình vá lỗi; lớp App &
Integration Platform có AuthN/Z (OIDC/SAML), secrets mgmt, runtime
security, API security/WAF; lớp Data Platform có encryption
at-rest/in-transit, KMS, masking, row/column security, DLP, audit truy
cập dữ liệu. Nghĩa là **Security + Identity không thay thế kiểm soát an
toàn của từng lớp, mà bổ sung lớp định danh -- chính sách -- phát
hiện/ứng phó dùng chung cho tất cả**.

**Nguồn:** *bảng "Khung tham chiếu phổ biến", slide 17 -- Chương 2
(2.pdf)*
