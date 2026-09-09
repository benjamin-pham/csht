**NỘI DUNG KPI VÀ CÁC MIỀN HOẠT ĐỘNG CNTT**

- **Khái Niệm:**

**Miền Vận hành (Operations) là bộ phận chịu trách nhiệm duy trì hoạt
động ổn định, liên tục và an toàn của toàn bộ hệ thống CNTT sau khi hệ
thống đã được triển khai.**

**Mục tiêu chính là:**

- Đảm bảo hệ thống luôn sẵn sàng phục vụ người dùng.

- Giảm thiểu sự cố và thời gian gián đoạn.

- Khôi phục hệ thống nhanh khi có lỗi.

- Bảo vệ dữ liệu và đảm bảo tính liên tục của dịch vụ.

<!-- -->

- **Vai Trò:**

**Bao gồm các hoạt động:**

- **ITSM (IT Service Management)**\
  Quản lý dịch vụ CNTT như quản lý sự cố, yêu cầu hỗ trợ, thay đổi và
  cấu hình.

- **SRE (Site Reliability Engineering)**\
  Áp dụng kỹ thuật để nâng cao độ tin cậy, hiệu năng và khả năng mở rộng
  của hệ thống.

- **DR (Disaster Recovery)**\
  Lập kế hoạch và khôi phục hệ thống khi xảy ra thảm họa hoặc mất dữ
  liệu.

- **SOC (Security Operations Center)**\
  Giám sát, phát hiện và xử lý các mối đe dọa an ninh mạng 24/7.

#  Bảng đo lường (KPI) -- Miền Vận hành 

# 

  ---------------------- ---------------------- ----------------------
  KPI                    Mô tả                  Cách thức đo lường

  Availability (Uptime)  Mức độ sẵn sàng của hệ (Thời gian hoạt
                         thống                  động/Tổng thời gian) ×
                                                100%

  MTTR                   Khả năng khôi phục sau Tổng thời gian khắc
                         sự cố                  phục / Số lượng sự cố

  Incident Rate          Tần suất phát sinh sự  Đếm số sự cố theo
                         cố                     ngày/tuần/tháng

  Backup Success Rate    Mức độ thành công của  (Số lần sao lưu thành
                         sao lưu                công/Tổng số lần sao
                                                lưu) × 100%

  RPO                    Lượng dữ liệu tối đa   So sánh dữ liệu mất
                         có thể mất             thực tế với mục tiêu
                                                RPO

  RTO                    Thời gian tối đa để    So sánh thời gian khôi
                         khôi phục hệ thống     phục thực tế với mục
                                                tiêu RTO
  ---------------------- ---------------------- ----------------------

#  

# 

# I. Nhóm KPI đánh giá năng lực CNTT

## 1. Vận hành -- IT Reliability

Đánh giá mức độ ổn định, sẵn sàng và khả năng phục hồi của hệ thống
CNTT. Các KPI tiêu biểu gồm Availability/Uptime, MTTR, sự cố P1/P2,
Backup Success Rate và RPO/RTO.

Vai trò: Giúp doanh nghiệp duy trì các hệ thống quan trọng hoạt động
liên tục, giảm thời gian gián đoạn và đảm bảo có phương án khôi phục khi
xảy ra sự cố.

## 2. Chuyển đổi -- Delivery & Agility

Đánh giá khả năng phát triển, triển khai và thay đổi hệ thống nhanh
chóng, linh hoạt nhưng vẫn kiểm soát chất lượng. Các KPI tiêu biểu gồm
Deployment Frequency, Lead Time for Change, Change Failure Rate, tỷ lệ
số hóa End-to-End và thời gian tích hợp API/hệ thống.

Vai trò: Giúp CNTT đáp ứng nhanh nhu cầu kinh doanh, rút ngắn thời gian
đưa tính năng mới vào sử dụng và cân bằng giữa tốc độ triển khai với độ
ổn định.

## 3. Dữ liệu & An ninh

Đánh giá chất lượng dữ liệu và mức độ an toàn của hệ thống. Các nội dung
gồm Data Quality, Security Incident, thời gian phát hiện và ứng cứu sự
cố, cùng các biện pháp bảo mật như MFA, EDR và Patching.

Vai trò: Đảm bảo dữ liệu chính xác, đáng tin cậy và hệ thống được bảo vệ
trước các nguy cơ mất dữ liệu, tấn công mạng và truy cập trái phép.

# II. Các miền hoạt động chính của doanh nghiệp

## 1. Quản trị

CNTT hỗ trợ quản lý chi phí, rủi ro, tuân thủ và lộ trình phát triển.

**Vai trò: Cung cấp thông tin và công cụ giúp lãnh đạo ra quyết định,
kiểm soát ngân sách, quản lý danh mục dự án và giảm rủi ro CNTT.**

## 2. Miền Vận hành

Đảm bảo các hệ thống và dịch vụ CNTT hoạt động ổn định, liên tục thông
qua các hoạt động như ITSM, SRE, DR và SOC.

**Vai trò: Duy trì tính sẵn sàng của dịch vụ, xử lý sự cố, giám sát an
toàn và đảm bảo khả năng phục hồi khi có sự cố hoặc thảm họa.**

## 3. Kinh doanh

CNTT hỗ trợ hoạt động kinh doanh thông qua ứng dụng, dữ liệu, AI và tích
hợp hệ thống.

**Vai trò: Tạo giá trị trực tiếp cho doanh nghiệp bằng cách tăng doanh
thu số, tối ưu chi phí, rút ngắn thời gian xử lý và nâng cao hiệu quả
hoạt động.**

## 4. Truyền thông

CNTT hỗ trợ quản lý và hiểu khách hàng thông qua CRM, CDP, Analytics và
Omni-channel.

**Vai trò: Kết nối dữ liệu khách hàng, nâng cao trải nghiệm, tăng mức độ
tương tác và hỗ trợ doanh nghiệp giữ chân khách hàng.**

## 5. Dịch vụ số

Tập trung xây dựng và cung cấp các sản phẩm, dịch vụ số đáng tin cậy, an
toàn và có khả năng phát hành nhanh thông qua DevSecOps, Platform và
Service Catalog.

**Vai trò: Rút ngắn thời gian đưa sản phẩm số ra thị trường, nâng cao
chất lượng dịch vụ và tạo trải nghiệm tốt hơn cho người dùng.**

# III. Tài liệu tham khảo

[**[https://digital.fpt.com/dich-vu-tu-van-chuyen-doi-so?utm_source]{.underline}**](https://digital.fpt.com/dich-vu-tu-van-chuyen-doi-so?utm_source)
