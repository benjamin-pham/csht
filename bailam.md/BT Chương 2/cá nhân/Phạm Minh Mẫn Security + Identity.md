TÌM HIỂU KIẾN TRÚC HẠ TẦNG CNTT DOANH NGHIỆP THEO KHUNG THAM CHIẾU

Lớp năng lực (3): Security và Identity

I.  Khái niệm

Lớp năng lực Security (bảo mật) và Identity (danh tính) là lớp chịu
trách nhiệm bảo vệ toàn bộ hạ tầng CNTT của doanh nghiệp thông qua việc:

- Quản lý danh tính người dùng (Identity)

- Xác thực (Authentication)

- Phân quyền truy cập (Authorization)

- Giám sát và phát hiện tấn công

- Bảo vệ dữ liệu

- Ứng phó sự cố an toàn thông tin

Đây là lớp bao trùm lên toàn bộ các lớp còn lại (Compute, Network,
Application, Data) nhằm đảm bảo mọi truy cập đều được kiểm soát theo
nguyên tắc Zero Trust (Không mặc định tin cậy).

Theo NIST SP 800-207, Zero Trust yêu cầu mọi người dùng, thiết bị, ứng
dụng và dịch vụ đều phải được xác minh liên tục trước khi được cấp quyền
truy cập.

Tài liệu tham khảo:

[[What is Identity Security? \|
IBM]{.underline}](https://www.ibm.com/think/topics/identity-security)

[[What is Identity Access Management (IAM)? \| Microsoft
Security]{.underline}](https://www.microsoft.com/en-us/security/business/security-101/what-is-identity-access-management-iam)

II. Vai trò

- Bảo vệ trung tâm tài sản số: Kiểm soát quyền truy cập dựa trên nguyên
  tắc \"Không tin tưởng bất kỳ ai\" (*Zero Trust Architecture*).

- Mở đường cho chuyển đổi số: Cho phép nhân viên làm việc từ xa
  (Remote/Hybrid) và khách hàng/đối tác kết nối an toàn vào ứng dụng
  doanh nghiệp.

- Đảm bảo Tuân thủ Pháp lý (Compliance): Đáp ứng các yêu cầu khắt khe
  của Luật An ninh mạng, Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá
  nhân (điều kiện quản lý quyền truy cập và mã hóa KMS).

[[Nghị định 13/2023/NĐ-CP bảo vệ dữ liệu cá
nhân]{.underline}](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-13-2023-ND-CP-bao-ve-du-lieu-ca-nhan-465185.aspx)

[[What Is Zero Trust Architecture? \| Microsoft
Security]{.underline}](https://www.microsoft.com/en-us/security/business/security-101/what-is-zero-trust-architecture)

III. Đặc điểm kĩ thuật

## Quản lý danh tính tập trung (Centralized Identity Management)

Một trong những đặc điểm quan trọng nhất của lớp Security + Identity là
mọi danh tính (Identity) của người dùng, thiết bị, ứng dụng và dịch vụ
đều được quản lý tập trung thông qua hệ thống Identity and Access
Management (IAM).

Hệ thống IAM cung cấp các chức năng:

- Quản lý vòng đời tài khoản (Identity Lifecycle Management).

- Đồng bộ tài khoản giữa nhiều hệ thống.

- Quản lý vai trò (Role Management).

- Quản lý nhóm người dùng.

- Liên kết danh tính giữa các hệ thống (Identity Federation).

Việc quản lý tập trung giúp giảm tài khoản trùng lặp, hạn chế tài khoản
\"mồ côi\" và đảm bảo việc cấp hoặc thu hồi quyền truy cập được thực
hiện đồng bộ trong toàn doanh nghiệp.

2.  Xác thực mạnh (Strong Authentication)

Lớp Security + Identity sử dụng nhiều cơ chế xác thực để đảm bảo người
dùng truy cập là đúng đối tượng đã đăng ký.

Các cơ chế phổ biến gồm:

- Password.

- Multi-Factor Authentication (MFA).

- Biometrics.

- Smart Card.

- FIDO2 Security Key.

- Passwordless Authentication.

Theo NIST, việc sử dụng nhiều yếu tố xác thực giúp giảm đáng kể nguy cơ
bị đánh cắp tài khoản so với chỉ sử dụng mật khẩu truyền thống.

##  Kiểm soát truy cập theo chính sách (Policy-based Access Control)

Thay vì cấp quyền cố định, các hệ thống hiện đại áp dụng cơ chế cấp
quyền dựa trên chính sách (Policy-based Access Control).

Một số mô hình kiểm soát truy cập phổ biến gồm:

- Role-Based Access Control (RBAC).

- Attribute-Based Access Control (ABAC).

- Least Privilege Access.

- Just-In-Time Access (JIT).

- Just-Enough Administration (JEA).

Nhờ đó, mỗi người dùng chỉ được cấp đúng quyền cần thiết để thực hiện
công việc.

##  Kiến trúc Zero Trust

Theo NIST SP 800-207, lớp Security + Identity được xây dựng theo mô hình
Zero Trust, trong đó không có người dùng hoặc thiết bị nào được mặc định
tin cậy.

Mọi yêu cầu truy cập đều phải được đánh giá dựa trên:

- Danh tính người dùng.

- Trạng thái thiết bị.

- Địa điểm truy cập.

- Thời gian truy cập.

- Mức độ rủi ro.

- Chính sách bảo mật của tổ chức.

Quá trình xác minh được thực hiện liên tục trong suốt phiên làm việc
thay vì chỉ khi đăng nhập.

##  Giám sát và phát hiện liên tục (Continuous Monitoring)

Lớp Security + Identity có khả năng thu thập và phân tích nhật ký bảo
mật (Security Logs) từ nhiều nguồn khác nhau như:

- Máy chủ.

- Thiết bị đầu cuối.

- Firewall.

- Thiết bị mạng.

- Ứng dụng.

- Dịch vụ Cloud.

Các dữ liệu này được tổng hợp trên hệ thống SIEM (Security Information
and Event Management) để phát hiện hành vi bất thường và hỗ trợ phản ứng
sự cố.

Nhiều hệ thống còn tích hợp SOAR (Security Orchestration, Automation and
Response) nhằm tự động hóa quá trình điều tra và xử lý các sự cố an toàn
thông tin.

## 7. Bảo mật dữ liệu bằng mã hóa (Data Protection)

Lớp Security + Identity hỗ trợ bảo vệ dữ liệu thông qua các kỹ thuật:

- Mã hóa dữ liệu khi lưu trữ (Encryption at Rest).

- Mã hóa dữ liệu khi truyền (Encryption in Transit).

- Quản lý khóa mã hóa (Key Management System - KMS).

- Hardware Security Module (HSM).

- Data Masking.

- Tokenization.

Các cơ chế này đảm bảo dữ liệu vẫn được bảo vệ ngay cả khi bị truy cập
trái phép.
