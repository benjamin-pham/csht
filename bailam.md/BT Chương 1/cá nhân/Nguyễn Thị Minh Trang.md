**3. Danh tính & bảo mật (Security + Identity)**

- **Khái niệm**: là hệ thống quốc phòng và an ninh của toàn bộ thế giới
  số trong doanh nghiệp, lớp (1) là đất đai, lớp (2) là ban quản lý đô
  thị, lớp (3) chính là cảnh sát, đặc nhiệm, chứng minh thư và hệ thống
  camera an ninh. Lớp (3) hiện đại được xây dựng trên nguyên lý Zero
  Trust (Không tin tưởng bất kỳ ai, luôn luôn xác thực).Lớp này chia làm
  hai nhánh cộng sinh chặt chẽ

<!-- -->

- Identity (Danh tính): Xác định \"Bạn là ai?\" và \"Bạn có quyền làm
  gì?\".

- Security (Bảo mật): Phát hiện, ngăn chặn và xử lý các hành vi độc hại.

<!-- -->

- **Vai trò**: Bảo vệ tài nguyên số, kiểm soát truy cập và phòng ngừa
  rủi ro.

- **Thành phần**: IAM/SSO/MFA, PAM, EDR/XDR, SIEM/SOC, WAF, DLP, mã hóa,
  phân loại dữ liệu.

  ---------------------- --------------------- -------------------------------------------------------------------- --------------------------------------------------
  Nhóm                   Thành phần            Chức năng chính                                                      Ví dụ
  Identity (Danh tính)   IAM / SSO / MFA       Quản lý danh tính, đăng nhập một lần, xác thực nhiều lớp             Đăng nhập 1 lần vào nhiều hệ thống, xác thực OTP
                         PAM                   Quản lý tài khoản đặc quyền (Admin/Root), ghi log và thu hồi quyền   Quản trị viên chỉ được cấp quyền khi cần
  Security (Bảo mật)     EDR / XDR             Giám sát thiết bị, phát hiện hành vi bất thường                      Phát hiện ransomware trên máy nhân viên
                         SIEM / SOC            Thu thập log, phân tích sự kiện và phản ứng sự cố                    Cảnh báo tấn công từ nhiều nguồn khác nhau
                         WAF                   Bảo vệ Website và API khỏi các cuộc tấn công                         Chặn SQL Injection, XSS, DDoS
                         DLP                   Ngăn rò rỉ dữ liệu                                                   Chặn gửi danh sách khách hàng qua Gmail hoặc USB
                         Encryption            Mã hóa dữ liệu khi lưu trữ và truyền tải                             Dữ liệu bị đánh cắp nhưng không thể đọc
                         Data Classification   Phân loại dữ liệu theo mức độ nhạy cảm                               Công khai, Nội bộ, Mật, Tối mật
  ---------------------- --------------------- -------------------------------------------------------------------- --------------------------------------------------

Tài liệu tham khảo: **tài liệu chi tiết thẻ 2**

[[https://en.wikipedia.org/wiki/]{.underline}](https://en.wikipedia.org/wiki/Identity_and_access_management)

[[https://learn.microsoft.com/en-us/]{.underline}](https://learn.microsoft.com/en-us/)
