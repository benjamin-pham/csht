**TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN -- ĐHQG -- HCM**

**TRUNG TÂM PHÁT TRIỂN CÔNG NGHỆ THÔNG TIN**

![](media/image1.png){width="2.425in" height="1.9625in"}🙣 🕮 🙡

**BÁO CÁO BÀI TẬP**

Giáo viên hướng dẫn: Nguyễn Thị Anh Thư

Nhóm sinh viên thực hiện:

Phạm Minh Mẫn 26410241

Lê Quang Đạt 26410183

Trần Việt Đức 26410189

Vũ Duy 26410199

Nguyễn Đức Huy 26410213

Trần Văn Phây 26410261

Huỳnh Thị Kiều Uyên 26410325

Đặng Nguyễn Minh Anh 26410163

Trần Anh Tú 26410318

TP. Hồ Chí Minh, Tháng 08 năm 2026.

# **Mục lục** {#mục-lục .TOC-Heading}

[1 Compute & Connectivity
[5](#compute-connectivity)](#compute-connectivity)

[1.1 Khái niệm [5](#khái-niệm)](#khái-niệm)

[1.2 Vai trò [5](#vai-trò)](#vai-trò)

[1.2.1 Trụ cột vận hành & Nền tảng cho các lớp năng lực khác
(Infrastructure Foundation)
[5](#trụ-cột-vận-hành-nền-tảng-cho-các-lớp-năng-lực-khác-infrastructure-foundation)](#trụ-cột-vận-hành-nền-tảng-cho-các-lớp-năng-lực-khác-infrastructure-foundation)

[1.2.2 Cung cấp năng lực xử lý, lưu trữ & Đảm bảo hiệu năng (Performance
& Scalability)
[5](#cung-cấp-năng-lực-xử-lý-lưu-trữ-đảm-bảo-hiệu-năng-performance-scalability)](#cung-cấp-năng-lực-xử-lý-lưu-trữ-đảm-bảo-hiệu-năng-performance-scalability)

[1.2.3 Kết nối & Luân chuyển dữ liệu hệ thống (Connectivity &
Circulation)
[6](#kết-nối-luân-chuyển-dữ-liệu-hệ-thống-connectivity-circulation)](#kết-nối-luân-chuyển-dữ-liệu-hệ-thống-connectivity-circulation)

[1.2.4 4. Thiết lập ranh giới an toàn hạ tầng ban đầu (Infrastructure
Security Baseline)
[6](#thiết-lập-ranh-giới-an-toàn-hạ-tầng-ban-đầu-infrastructure-security-baseline)](#thiết-lập-ranh-giới-an-toàn-hạ-tầng-ban-đầu-infrastructure-security-baseline)

[1.2.5 Tối ưu hóa chi phí & Lập kế hoạch năng lực (TCO & Capacity
Baseline)
[6](#tối-ưu-hóa-chi-phí-lập-kế-hoạch-năng-lực-tco-capacity-baseline)](#tối-ưu-hóa-chi-phí-lập-kế-hoạch-năng-lực-tco-capacity-baseline)

[1.3 Các thành phần [6](#các-thành-phần)](#các-thành-phần)

[1.4 Đặc điểm kĩ thuật [6](#đặc-điểm-kĩ-thuật)](#đặc-điểm-kĩ-thuật)

[1.4.1 Khả năng mở rộng (Scalability & Elasticity)
[6](#khả-năng-mở-rộng-scalability-elasticity)](#khả-năng-mở-rộng-scalability-elasticity)

[1.4.2 Tính sẵn sàng cao & Khả năng chịu lỗi (High Availability - HA &
Fault Tolerance)
[6](#tính-sẵn-sàng-cao-khả-năng-chịu-lỗi-high-availability---ha-fault-tolerance)](#tính-sẵn-sàng-cao-khả-năng-chịu-lỗi-high-availability---ha-fault-tolerance)

[1.4.3 Mềm hóa bằng phần mềm (Software-Defined Everything - SDx)
[6](#mềm-hóa-bằng-phần-mềm-software-defined-everything---sdx)](#mềm-hóa-bằng-phần-mềm-software-defined-everything---sdx)

[1.4.4 Hiệu năng & Độ trễ thấp (Performance & Low Latency)
[6](#hiệu-năng-độ-trễ-thấp-performance-low-latency)](#hiệu-năng-độ-trễ-thấp-performance-low-latency)

[1.4.5 Chuẩn hóa & Cô lập (Standardization & Multi-tenancy):
[7](#chuẩn-hóa-cô-lập-standardization-multi-tenancy)](#chuẩn-hóa-cô-lập-standardization-multi-tenancy)

[1.5 Các mô hình triển khai
[7](#các-mô-hình-triển-khai)](#các-mô-hình-triển-khai)

[1.6 Xu hướng công nghệ mới
[7](#xu-hướng-công-nghệ-mới)](#xu-hướng-công-nghệ-mới)

[1.7 Quan hệ với các lớp năng lực khác
[7](#quan-hệ-với-các-lớp-năng-lực-khác)](#quan-hệ-với-các-lớp-năng-lực-khác)

[2 Ops Platform [7](#ops-platform)](#ops-platform)

[2.1 Khái niệm [7](#khái-niệm-1)](#khái-niệm-1)

[2.2 Vai trò [8](#vai-trò-1)](#vai-trò-1)

[2.3 Các thành phần [8](#các-thành-phần-1)](#các-thành-phần-1)

[2.3.1 Phần mềm Vận hành (Software)
[8](#phần-mềm-vận-hành-software)](#phần-mềm-vận-hành-software)

[2.3.2 Mạng Vận hành & Dữ liệu Giám sát (Network)
[8](#mạng-vận-hành-dữ-liệu-giám-sát-network)](#mạng-vận-hành-dữ-liệu-giám-sát-network)

[2.3.3 Quy trình & Chuẩn Vận hành (Governance / Ops)
[9](#quy-trình-chuẩn-vận-hành-governance-ops)](#quy-trình-chuẩn-vận-hành-governance-ops)

[2.3.4 Bảo mật Vận hành (Security)
[9](#bảo-mật-vận-hành-security)](#bảo-mật-vận-hành-security)

[2.3.5 Phần cứng Phụ trợ (Hardware)
[9](#phần-cứng-phụ-trợ-hardware)](#phần-cứng-phụ-trợ-hardware)

[2.4 Đặc điểm kĩ thuật [9](#đặc-điểm-kĩ-thuật-1)](#đặc-điểm-kĩ-thuật-1)

[2.4.1 Kiến trúc Mô-đun và Khả năng Mở rộng (Modular & Scalable
Architecture)
[9](#kiến-trúc-mô-đun-và-khả-năng-mở-rộng-modular-scalable-architecture)](#kiến-trúc-mô-đun-và-khả-năng-mở-rộng-modular-scalable-architecture)

[2.4.2 Mô hình Thu thập & Xử lý Dữ liệu Vận hành (Telemetry & Data
Pipeline)
[10](#mô-hình-thu-thập-xử-lý-dữ-liệu-vận-hành-telemetry-data-pipeline)](#mô-hình-thu-thập-xử-lý-dữ-liệu-vận-hành-telemetry-data-pipeline)

[2.4.3 Tự động hóa dựa trên Khai báo (Declarative Automation & GitOps)
[10](#tự-động-hóa-dựa-trên-khai-báo-declarative-automation-gitops)](#tự-động-hóa-dựa-trên-khai-báo-declarative-automation-gitops)

[2.4.4 Tầm nhìn Toàn diện (Full-stack Observability)
[10](#tầm-nhìn-toàn-diện-full-stack-observability)](#tầm-nhìn-toàn-diện-full-stack-observability)

[2.4.5 Quản lý Độ tin cậy dựa trên Data-Driven (SRE-driven Reliability)
[10](#quản-lý-độ-tin-cậy-dựa-trên-data-driven-sre-driven-reliability)](#quản-lý-độ-tin-cậy-dựa-trên-data-driven-sre-driven-reliability)

[2.4.6 6. Cách ly & Bảo vệ Mặt phẳng Quản trị (Management Plane
Isolation)
[10](#cách-ly-bảo-vệ-mặt-phẳng-quản-trị-management-plane-isolation)](#cách-ly-bảo-vệ-mặt-phẳng-quản-trị-management-plane-isolation)

[2.5 Quan hệ với các lớp năng lực khác
[10](#quan-hệ-với-các-lớp-năng-lực-khác-1)](#quan-hệ-với-các-lớp-năng-lực-khác-1)

[3 Security & Identity [11](#security-identity)](#security-identity)

[3.1 Khái niệm [11](#khái-niệm-2)](#khái-niệm-2)

[3.2 Vai trò [12](#vai-trò-2)](#vai-trò-2)

[3.3 Các thành phần [12](#các-thành-phần-2)](#các-thành-phần-2)

[3.4 Đặc điểm kĩ thuật [12](#đặc-điểm-kĩ-thuật-2)](#đặc-điểm-kĩ-thuật-2)

[3.5 Rủi ro nhắm vào danh tính và cách kiểm soát
[14](#rủi-ro-nhắm-vào-danh-tính-và-cách-kiểm-soát)](#rủi-ro-nhắm-vào-danh-tính-và-cách-kiểm-soát)

[3.6 Nghĩa vụ tuân thủ tại Việt Nam
[14](#nghĩa-vụ-tuân-thủ-tại-việt-nam)](#nghĩa-vụ-tuân-thủ-tại-việt-nam)

[3.7 Quan hệ với 4 lớp năng lực còn lại
[15](#quan-hệ-với-4-lớp-năng-lực-còn-lại)](#quan-hệ-với-4-lớp-năng-lực-còn-lại)

[4 App & Integration Platform
[15](#app-integration-platform)](#app-integration-platform)

[4.1 Khái niệm [15](#khái-niệm-3)](#khái-niệm-3)

[4.2 Vai trò [16](#vai-trò-3)](#vai-trò-3)

[4.2.1 Cầu nối tích hợp & Xóa bỏ ốc đảo dữ liệu (Data Silos)
[16](#cầu-nối-tích-hợp-xóa-bỏ-ốc-đảo-dữ-liệu-data-silos)](#cầu-nối-tích-hợp-xóa-bỏ-ốc-đảo-dữ-liệu-data-silos)

[4.2.2 Nền tảng phát triển & Tăng tốc đổi mới (Agility & Innovation)
[16](#nền-tảng-phát-triển-tăng-tốc-đổi-mới-agility-innovation)](#nền-tảng-phát-triển-tăng-tốc-đổi-mới-agility-innovation)

[4.2.3 Kiểm soát luồng giao tiếp & Chuẩn hóa điểm truy cập
[16](#kiểm-soát-luồng-giao-tiếp-chuẩn-hóa-điểm-truy-cập)](#kiểm-soát-luồng-giao-tiếp-chuẩn-hóa-điểm-truy-cập)

[4.2.4 Mở rộng linh hoạt & Tăng khả năng chịu lỗi (Scalability &
Resilience)
[16](#mở-rộng-linh-hoạt-tăng-khả-năng-chịu-lỗi-scalability-resilience)](#mở-rộng-linh-hoạt-tăng-khả-năng-chịu-lỗi-scalability-resilience)

[4.2.5 Nền tảng thực thi phương pháp luận DevOps / SRE
[16](#nền-tảng-thực-thi-phương-pháp-luận-devops-sre)](#nền-tảng-thực-thi-phương-pháp-luận-devops-sre)

[4.2.6 Điểm thực thi chính sách bảo mật ứng dụng
[16](#điểm-thực-thi-chính-sách-bảo-mật-ứng-dụng)](#điểm-thực-thi-chính-sách-bảo-mật-ứng-dụng)

[4.3 Các thành phần [17](#các-thành-phần-3)](#các-thành-phần-3)

[4.3.1 Phần cứng (Hardware - HW)
[17](#phần-cứng-hardware---hw)](#phần-cứng-hardware---hw)

[4.3.2 2. Phần mềm (Software - SW) --- Trọng tâm của lớp
[17](#phần-mềm-software---sw-trọng-tâm-của-lớp)](#phần-mềm-software---sw-trọng-tâm-của-lớp)

[4.3.3 3. Mạng (Network) [18](#mạng-network)](#mạng-network)

[4.3.4 4. Quản trị (Governance / Ops)
[18](#quản-trị-governance-ops)](#quản-trị-governance-ops)

[4.3.5 5. Bảo mật (Security) [18](#bảo-mật-security)](#bảo-mật-security)

[4.4 Đặc điểm kĩ thuật [19](#đặc-điểm-kĩ-thuật-3)](#đặc-điểm-kĩ-thuật-3)

[4.5 Quan hệ với các lớp năng lực khác
[19](#quan-hệ-với-các-lớp-năng-lực-khác-2)](#quan-hệ-với-các-lớp-năng-lực-khác-2)

[5 Data Platform [20](#data-platform)](#data-platform)

[5.1 Khái niệm [20](#khái-niệm-4)](#khái-niệm-4)

[5.2 Vai trò [20](#vai-trò-4)](#vai-trò-4)

[5.3 Các thành phần [20](#các-thành-phần-4)](#các-thành-phần-4)

[5.3.1 Hạ Tầng Phần Cứng (Hardware - HW)
[20](#hạ-tầng-phần-cứng-hardware---hw)](#hạ-tầng-phần-cứng-hardware---hw)

[5.3.2 Lớp Phần Mềm Và Dịch Vụ (Software - SW)
[21](#lớp-phần-mềm-và-dịch-vụ-software---sw)](#lớp-phần-mềm-và-dịch-vụ-software---sw)

[5.3.3 Mạng Và Hạ Tầng Truyền Dẫn (Network)
[21](#mạng-và-hạ-tầng-truyền-dẫn-network)](#mạng-và-hạ-tầng-truyền-dẫn-network)

[5.3.4 Quản Trị Và Vận Hành Dữ Liệu (Governance / Ops)
[21](#quản-trị-và-vận-hành-dữ-liệu-governance-ops)](#quản-trị-và-vận-hành-dữ-liệu-governance-ops)

[5.3.5 Bảo Mật Và An Toàn Dữ Liệu (Security)
[22](#bảo-mật-và-an-toàn-dữ-liệu-security)](#bảo-mật-và-an-toàn-dữ-liệu-security)

[5.4 Đặc điểm kĩ thuật [22](#đặc-điểm-kĩ-thuật-4)](#đặc-điểm-kĩ-thuật-4)

[5.5 Quan hệ với các lớp năng lực khác
[23](#quan-hệ-với-các-lớp-năng-lực-khác-3)](#quan-hệ-với-các-lớp-năng-lực-khác-3)

**Nguồn trích dẫn**

1.  *Khung tham chiếu hạ tầng CNTT doanh nghiệp (Slide 17 Chương 2).*

2.  *Mell, P. & Grance, T. (2011). The NIST Definition of Cloud
    Computing, NIST Special Publication 800-145, National Institute of
    Standards and Technology.*
    [*https://doi.org/10.6028/NIST.SP.800-145*](https://doi.org/10.6028/NIST.SP.800-145)

3.  [*Kết nối mạng máy tính là gì? - Giải thích về Kết nối mạng trong
    máy tính -
    AWS*](https://aws.amazon.com/vi/what-is/computer-networking/)

4.  [*ITSM: IT Service Management Definition, Benefits & Tools \|
    Atlassian*](https://www.atlassian.com/itsm)

5.  [*Documentation \| OpenTelemetry*](https://opentelemetry.io/docs/)

6.  [*Data Management Framework: Development & Implementation \| SPD
    Technology*](https://spd.tech/data/data-management-framework-shaping-an-approach-for-controlling-data/)

7.  [*What is Data Architecture? Types, Components &
    Principles*](https://atlan.com/what-is-data-architecture/)

8.  [*US11818156B1 - Data lake-enabled security platform - Google
    Patents*](https://patents.google.com/patent/US11818156B1/en)

9.  [*Effective Data Architecture Design Guide \| PDF \| Cloud Computing
    \| Enterprise
    Architecture*](https://www.scribd.com/document/976917545/Unit-3-Designing-Good-Data-Architecture)

10. [*NIST SP 800-145, The NIST Definition of Cloud
    Computing*](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)

11. [*What Are Hypervisors? \|
    IBM*](https://www.ibm.com/think/topics/hypervisors)

12. [*Type 1 vs Type 2 Hypervisors - Difference Between Hypervisor
    Types -
    AWS*](https://aws.amazon.com/compare/the-difference-between-type-1-and-type-2-hypervisors/)

13. [*What Is SD-WAN? - Software-Defined WAN (SDWAN) -
    Cisco*](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-sd-wan.html)

14. [*What is block storage? \|
    NetApp*](https://www.netapp.com/data-storage/what-is-block-storage/)

**\**

# Compute & Connectivity

## Khái niệm

**Compute & Connectivity** là lớp năng lực nền tảng nhất trong 5 lớp
năng lực của kiến trúc hạ tầng CNTT doanh nghiệp. Đây là lớp cung cấp
tài nguyên tính toán thô (compute), năng lực lưu trữ (storage) và khả
năng kết nối (connectivity) --- những thành phần vật lý và phần mềm hạ
tầng cơ bản mà mọi lớp năng lực khác *(Ops Platform, Security, App &
Integration Platform, Data Platform)* đều phải dựa vào để vận hành.

Nếu ví toàn bộ hệ thống CNTT của doanh nghiệp như một thành phố, thì lớp
Compute & Connectivity chính là nền đất, hệ thống điện và mạng lưới
đường xá. Mọi công trình (ứng dụng, dữ liệu, dịch vụ) đều phải được xây
dựng và duy trì trên nền tảng này.

Lớp năng lực này bao gồm 2 mảng chính:

- **Compute (Tính toán & Lưu trữ):** Năng lực xử lý (CPU/RAM) và lưu trữ
  dữ liệu (Storage) để chạy hệ điều hành, các trình quản lý ảo hóa và
  ứng dụng.

- **Connectivity (Kết nối):** Khả năng liên lạc, truyền tải dữ liệu giữa
  các thiết bị và hệ thống, bao gồm cả mạng nội bộ (LAN), mạng diện rộng
  (WAN/SD-WAN), mạng ảo hóa trên đám mây và đường truyền $Internet$.

## Vai trò

Mặc dù không trực tiếp xử lý các logic nghiệp vụ cho người dùng cuối,
lớp **Compute & Connectivity** đóng giữ các vai trò sống còn trong tổng
thể kiến trúc CNTT doanh nghiệp:

### Trụ cột vận hành & Nền tảng cho các lớp năng lực khác (Infrastructure Foundation)

**Giá đỡ hệ thống:** Là \"mặt đất\" vật lý và ảo hóa để tất cả các lớp
năng lực còn lại *(Ops Platform, Security, App & Integration, Data
Platform)* khởi tạo và thực thi.

- *Ops Platform* cần compute để chạy công cụ giám sát, quản lý ITSM.

- *Security* cần hạ tầng để triển khai tường lửa, hệ thống định danh
  IAM.

- *App & Data Platform* đều vận hành trực tiếp trên tài nguyên tính toán
  và lưu trữ của lớp này.

**Tính sống còn:** Nếu lớp (1) gặp sự cố hoặc thiếu ổn định, toàn bộ các
ứng dụng nghiệp vụ phía trên ($ERP,CRM$, website, app di động\...) đều
sẽ dừng hoạt động.

### Cung cấp năng lực xử lý, lưu trữ & Đảm bảo hiệu năng (Performance & Scalability)

**Xử lý & Truy xuất:** Cung cấp tài nguyên CPU, RAM để thực thi ứng dụng
và hệ thống Storage để lưu trữ, truy xuất dữ liệu vận hành.

**Định hình giới hạn chịu tải:** Tốc độ xử lý I/O và băng thông mạng tại
lớp này quyết định trực tiếp đến độ trễ (latency) và hiệu năng của phần
mềm --- tránh hiện tượng nghẽn mạng hay gián đoạn hệ thống.

**Khả năng mở rộng:** Quyết định năng lực mở rộng dọc (Vertical
Scaling - nâng cấp CPU/RAM) hoặc mở rộng ngang (Hoirizontal Scaling-
nhân bản máy chủ) cho toàn bộ kiến trúc khi lưu lượng truy cập tăng cao.

### Kết nối & Luân chuyển dữ liệu hệ thống (Connectivity & Circulation)

**Hệ tuần hoàn mạng:** Mạng kết nối đóng vai trò liên kết các thành phần
máy chủ và lưu trữ đứng độc lập thành một hệ thống thống nhất.

**Giao tiếp đa chiều:** Đảm bảo luồng thông tin diễn ra liên tục, an
toàn và thông suốt giữa: *Người dùng* $\leftrightarrow$ *Ứng dụng*
$\leftrightarrow$ *Cơ sở dữ liệu* $\leftrightarrow$ *Dịch vụ bên ngoài*.

### 4. Thiết lập ranh giới an toàn hạ tầng ban đầu (Infrastructure Security Baseline)

Tạo dựng lớp bảo mật nền tảng ngay từ cấp độ phần cứng và đường truyền
thông qua việc phân vùng mạng (Network Segmentation), gia cố thiết bị
(Hardening), cấu hình mã hóa (TLS/VPN) và cập nhật bản vá lỗi (Patching)
cấp độ Firmware/OS.

Bảo vệ tài nguyên hạ tầng trước các nguy cơ tấn công mạng trước khi truy
cập chạm tới lớp ứng dụng.

### Tối ưu hóa chi phí & Lập kế hoạch năng lực (TCO & Capacity Baseline)

Giúp doanh nghiệp đo lường và định lượng chính xác mức độ tiêu thụ tài
nguyên (CPU, RAM, đĩa cứng, băng thông).

Làm cơ sở để lập kế hoạch năng lực (Capacity Planning), tự động hóa dự
báo nhu cầu nâng cấp và tối ưu hóa chi phí đầu tư hạ tầng (CapEx/OpEx).

Cụ thể:

- **Tối ưu CapEx (Capital Expenditure -- Chi phí đầu tư):**

  - Tránh đầu tư dư thừa máy chủ, lưu trữ hoặc thiết bị mạng do ước
    lượng sai nhu cầu.

  - Xác định đúng thời điểm cần nâng cấp hoặc mở rộng hạ tầng dựa trên
    dữ liệu thực tế.

  - Hỗ trợ lập kế hoạch ngân sách đầu tư theo từng giai đoạn, giảm rủi
    ro đầu tư không hiệu quả.

<!-- -->

- **Tối ưu OpEx (Operational Expenditure -- Chi phí vận hành):**

  - Giảm chi phí điện năng, làm mát, bảo trì và vận hành hệ thống.

  - Tối ưu việc sử dụng tài nguyên, hạn chế tình trạng máy chủ nhàn rỗi
    hoặc cấp phát quá mức (over-provisioning).

  - Đối với môi trường Cloud, kiểm soát và giảm chi phí sử dụng tài
    nguyên theo mô hình trả theo mức sử dụng (pay-as-you-go), đồng thời
    phát hiện tài nguyên lãng phí để tối ưu hóa hóa đơn dịch vụ.

## Các thành phần

## Đặc điểm kĩ thuật

### Khả năng mở rộng (Scalability & Elasticity)

Hỗ trợ mở rộng theo chiều ngang (*Horizontal Scaling* - thêm
node/server) và chiều dọc (*Vertical Scaling* - nâng cấp CPU/RAM).

Trong môi trường Cloud/SDN, tài nguyên compute và mạng có thể tự động co
giãn (*Auto-scaling*) theo tải thực tế.

### Tính sẵn sàng cao & Khả năng chịu lỗi (High Availability - HA & Fault Tolerance)

Thiết kế dự phòng N+1 hoặc 2N cho các thành phần quan trọng (Nguồn, NIC,
Switch, Storage Controller).

Hỗ trợ các công cụ như Clustering, Live Migration (vMotion), Multi-AZ
(Availability Zones).

### Mềm hóa bằng phần mềm (Software-Defined Everything - SDx)

Dần chuyển dịch từ cấu hình phần cứng thủ công sang quản lý bằng mã
nguồn (*Infrastructure as Code - IaC*), SD-WAN, SDN (Software-Defined
Networking) và SDS (Software-Defined Storage).

### Hiệu năng & Độ trễ thấp (Performance & Low Latency)

Tối ưu hóa băng thông mạng (10GbE, 25GbE, 100GbE+), giao thức lưu trữ
tốc độ cao (NVMe-oF, SAN Fibre Channel) và xử lý tính toán song song.

### Chuẩn hóa & Cô lập (Standardization & Multi-tenancy):

Phân chia tài nguyên an toàn cho nhiều ứng dụng/đơn vị sử dụng chung
thông qua công nghệ ảo hóa (Hypervisor) hoặc phân đoạn mạng
(VLAN/VXLAN/VPC).

## Các mô hình triển khai

- **On-premise:** Doanh nghiệp tự đầu tư, sở hữu và vận hành phần cứng
  tại Trung tâm dữ liệu (Data Center) riêng.

- **Cloud:** Thuê tài nguyên tính toán, lưu trữ và mạng từ các nhà cung
  cấp đám mây (AWS, Azure, GCP\...) theo mô hình trả tiền theo nhu cầu.
  Theo chuẩn hóa của **NIST (Viện Tiêu chuẩn và Công nghệ Hoa Kỳ)**,
  điện toán đám mây là mô hình cho phép truy cập mạng thuận tiện, theo
  yêu cầu, tới một tập hợp tài nguyên tính toán có thể cấu hình (mạng,
  máy chủ, lưu trữ, ứng dụng) và có thể cấp phát/thu hồi nhanh chóng.

- **Hybrid:** Mô hình kết hợp linh hoạt giữa On-premise và Cloud.

## Xu hướng công nghệ mới

Chuyển dịch từ IaaS truyền thống sang mô hình serverless/compute co giãn
tự động: giảm gánh nặng quản lý hạ tầng, tài nguyên tự động co giãn theo
tải thực tế.

SD-WAN kết hợp SASE (Secure Access Service Edge): xu hướng hội tụ giữa
mạng diện rộng và bảo mật thành một nền tảng thống nhất, được dự báo sẽ
trở thành lựa chọn chủ đạo khi doanh nghiệp mở rộng sử dụng cloud và làm
việc từ xa.

Container hóa thay thế một phần vai trò của máy ảo truyền thống: giúp
tận dụng tài nguyên compute hiệu quả hơn so với ảo hóa toàn bộ hệ điều
hành.

## Quan hệ với các lớp năng lực khác

Lớp **Compute & Connectivity** đóng vai trò hạt nhân hạ tầng, chuyển hóa
các tài nguyên vật lý thô (CPU, RAM, ổ đĩa, switch) thành các môi trường
điện toán và mạng được mềm hóa, chia sẻ an toàn. Bằng việc kết hợp hệ
điều hành, hypervisor cùng các công nghệ SDN và SDS, lớp này tạo ra các
phân đoạn ảo hóa (VM, VPC, Subnet) có khả năng tự động co giãn và dự
phòng cao. Đây chính là nền tảng trực tiếp để **Ops Platform** điều
khiển qua mã nguồn (IaC), giúp **App Platform** đóng gói ứng dụng trong
container, đồng thời đáp ứng yêu cầu đọc/ghi tốc độ cao cho **Data
Platform**.

Trên bức tranh tổng thể, toàn bộ bề mặt tính toán và luồng truyền thông
này được bao bọc trực tiếp bởi các chính sách từ **Security &
Identity**. Việc gia cố cấu hình (hardening), mã hóa đường truyền
(TLS/VPN) và phân đoạn mạng giúp thiết lập ranh giới bảo vệ sơ cấp ngay
từ cấp độ phần cứng. Bất kỳ nghẽn mạch hay đứt gãy nào ở lớp móng này
cũng sẽ ngay lập tức làm ngưng trệ toàn bộ các nền tảng phía trên, bất
kể phần mềm hay dữ liệu được thiết kế tối ưu đến đâu.

# Ops Platform

## Khái niệm

**Ops Platform (Nền tảng Vận hành)** là tập hợp các công cụ, phần mềm,
quy trình tự động hóa và đường ống dữ liệu (data pipelines) được thiết
kế nhằm quản lý, giám sát, điều phối và tối ưu hóa toàn bộ vòng đời của
hạ tầng và ứng dụng CNTT.

Ops Platform chuyển đổi các hoạt động quản trị thủ công (manual toil)
thành các quy trình chuẩn hóa, có thể lập trình (*Programmable
Infrastructure*) và giám sát toàn diện từ end-to-end.

## Vai trò

Ops Platform đóng vai trò là \"trung tâm chỉ huy\" (Command Center) của
phòng CNTT với các vai trò cốt lõi sau:

- **Đảm bảo độ tin cậy và sẵn sàng (Reliability & Availability):** Giám
  sát trạng thái hệ thống theo thời gian thực, phát hiện sự cố trước khi
  người dùng phát hiện và phục hồi nhanh chóng khi có gián đoạn.

- **Thúc đẩy Tự động hóa & Tốc độ (Automation & Agility):** Giảm thiểu
  công việc thủ công bằng cách sử dụng Mã hóa hạ tầng (IaC) và các kịch
  bản tự động hóa (Orchestration/Playbooks), giúp triển khai tài nguyên
  trong vài phút thay vì vài tuần.

- **Tối ưu hóa Chi phí (FinOps):** Cung cấp tầm nhìn chi tiết về mức độ
  sử dụng tài nguyên (Compute, Storage, Network) và chi phí phát sinh
  trên Cloud/On-premise, giúp cắt giảm lãng phí.

- **Chuẩn hóa Quy trình CNTT (Governance & ITSM):** Đảm bảo mọi thay đổi
  (Change), sự cố (Incident) hay yêu cầu dịch vụ (Service Request) đều
  được ghi nhận, phê duyệt và xử lý theo các tiêu chuẩn quốc tế như
  ITIL.

## Các thành phần

### Phần mềm Vận hành (Software)

Đây là \"bộ não\" xử lý tác vụ của Ops Platform, bao gồm các công cụ cốt
lõi:

- **Giám sát & Tận quan (Monitoring & Observability):** Thu thập và phân
  tích 3 trụ cột dữ liệu (Metrics, Logs, Traces) để theo dõi sức khỏe hệ
  thống theo thời gian thực (ví dụ: Prometheus, Grafana, Datadog, ELK
  Stack).

- **Quản lý Dịch vụ IT (ITSM & CMDB):** Quản lý yêu cầu, sự cố, sự thay
  đổi và cơ sở dữ liệu cấu hình tài sản IT (như ServiceNow, Jira Service
  Management).

- **Tự động hóa & Hạ tầng dạng Mã (IaC & Orchestration):** Tự động khởi
  tạo và cấu hình hệ thống bằng mã lệnh (như Terraform, Ansible,
  SaltStack).

- **Sao lưu & Phục hồi sự cố (Backup & DR Tooling):** Công cụ tự động
  sao lưu dữ liệu và sẵn sàng kịch bản khôi phục khi gặp sự cố (như
  Veeam, Commvault).

- **Quản lý Chi phí (FinOps Tooling):** Theo dõi, dự báo và tối ưu hóa
  chi phí sử dụng tài nguyên (đặc biệt là Cloud).

### Mạng Vận hành & Dữ liệu Giám sát (Network)

Lớp này đảm bảo luồng thông tin vận hành được truyền tải an toàn và
thông suốt:

- **Telemetry / Log / Metric Pipeline:** Đường ống thu thập, lọc và
  chuyển tiếp dữ liệu nhật ký (logs) và chỉ số (metrics) từ các
  server/ứng dụng về trung tâm xử lý mà không làm nghẽn hệ thống chính
  (ví dụ: Fluentd, Logstash, Vector).

- **Management Plane (Mặt phẳng Quản lý):** Mạng/phân đoạn mạng riêng
  tách biệt (Out-of-Band Management) dành riêng cho luồng truy cập quản
  trị, tránh đi chung với lưu lượng truy cập của người dùng cuối.

### Quy trình & Chuẩn Vận hành (Governance / Ops)

Yếu tố con người và quy trình giúp công cụ phát huy hiệu quả:

- **Quản lý Sự cố / Thay đổi / Bối cảnh (Incident / Change / Problem
  Management):** Quy trình phân loại lỗi, xử lý nhanh sự cố và kiểm soát
  rủi ro khi cập nhật hệ thống mới.

- **SLO / SLA Management:** Theo dõi chỉ số cam kết chất lượng dịch vụ
  (SLA) và mục tiêu mức dịch vụ nội bộ (SLO).

- **Kịch bản Diễn tập DR (DR Drills):** Quy trình định kỳ diễn tập khôi
  phục hệ thống sau thảm họa để kiểm tra tính sẵn sàng.

- **Quy hoạch Dung lượng (Capacity Planning):** Dự báo nhu cầu tăng
  trưởng tài nguyên cứng dựa trên dữ liệu quá khứ.

### Bảo mật Vận hành (Security)

Đảm bảo bản thân nền tảng vận hành không trở thành lỗ hổng bị khai thác:

- **Audit & Log Integrity:** Đảm bảo nhật ký hệ thống không bị chỉnh sửa
  hay xóa bỏ (chống xóa vết khi bị xâm nhập).

- **Kiểm soát Quyền Admin:** Áp dụng nguyên tắc quyền tối thiểu (Least
  Privilege) đối với các tài khoản quản trị vận hành.

- **Quy trình Vá lỗi (Patch Management):** Quy trình tự động hoặc bán tự
  động cập nhật các bản vá an ninh cho OS, middleware.

- **Cảnh báo An ninh Vận hành:** Phát hiện các hành vi bất thường từ
  chính các công cụ quản trị hoặc tài khoản admin.

### Phần cứng Phụ trợ (Hardware)

Ops Platform thường không đòi hỏi hạ tầng quá đắt đỏ:

- Tận dụng hạ tầng Compute có sẵn ở lớp (1).

- Sử dụng các máy chủ/tiến trình nhẹ (Lightweight Agents) cài đặt rải
  rác trên các endpoint/server để thu thập dữ liệu và thực thi lệnh.

## Đặc điểm kĩ thuật

### Kiến trúc Mô-đun và Khả năng Mở rộng (Modular & Scalable Architecture)

**Thiết kế Microservices / Container-native:** Hệ thống Ops Platform
hiện đại được xây dựng trên kiến trúc dịch vụ nhỏ (microservices), cho
phép mở rộng linh hoạt (horizontal scaling) từng thành phần (như công cụ
thu thập log, engine xử lý cảnh báo) khi quy mô hạ tầng tăng lên.

**Agent-based & Agentless Hybrid:** Hỗ trợ linh hoạt cả hai phương thức
thu thập dữ liệu:

- *Agent-based:* Cài đặt các trình thu thập siêu nhẹ (lightweight
  collectors như Prometheus Node Exporter, Fluentbit, Datadog Agent)
  trên đối tượng cần giám sát để lấy dữ liệu chuyên sâu.

- *Agentless:* Thu thập qua các giao thức tiêu chuẩn (SNMP, SSH, WinRM,
  Cloud Provider APIs) đối với các thiết bị không cho phép cài phần mềm
  thứ ba.

### Mô hình Thu thập & Xử lý Dữ liệu Vận hành (Telemetry & Data Pipeline)

**Xử lý theo Thời gian thực (Real-time Stream Processing):** Khả năng
tiếp nhận và xử lý hàng triệu sự kiện (events), chỉ số (metrics) và dòng
log mỗi giây thông qua các hàng đợi tin nhắn (Message Queue / Event Bus
như Apache Kafka, RabbitMQ) trước khi lưu trữ hoặc phân tích.

**Chuẩn hóa dữ liệu (Data Normalization & Correlation):** Tự động chuẩn
hóa dữ liệu telemetry từ nhiều nguồn khác nhau (On-premise, AWS, Azure,
GCP) về một định dạng thống nhất (ví dụ: chuẩn **OpenTelemetry**). Tự
động liên kết (correlate) giữa Log, Metric và Trace để tìm nguyên nhân
gốc rễ (Root Cause Analysis - RCA).

### Tự động hóa dựa trên Khai báo (Declarative Automation & GitOps)

**Mã hóa hạ tầng và cấu hình (Infrastructure as Code - IaC):** Toàn bộ
trạng thái hạ tầng, quy trình triển khai và cấu hình vận hành được định
nghĩa bằng mã (code) lưu trữ trên hệ thống quản lý phiên bản (Git).

**Cơ chế Tự phục hồi (Self-Healing & Auto-remediation):** Tích hợp các
động cơ thực thi kịch bản (Automation Engines/Playbooks). Khi phát hiện
sự cố theo ngưỡng định trước (ví dụ: đầy đĩa quạt, service bị crash), hệ
thống tự động kích hoạt kịch bản khắc phục mà không cần sự can thiệp của
con người.

### Tầm nhìn Toàn diện (Full-stack Observability)

Hỗ trợ 3 Trụ cột Observability (MELT - Metrics, Events, Logs, Traces):

- *Metrics:* Thu thập các chỉ số định lượng theo chuỗi thời gian
  (Time-series data).

- *Logs:* Ghi nhận chi tiết các sự kiện diễn ra trong hệ thống.

- *Traces:* Truy vết đường đi của một request xuyên suốt qua nhiều dịch
  vụ microservices.

### Quản lý Độ tin cậy dựa trên Data-Driven (SRE-driven Reliability)

Đo lường chỉ số tin cậy tự động (SLI/SLO Tracing): Tự động tính toán các
chỉ số cam kết (SLI/SLO) và ngân sách rủi ro (Error Budget).

Phân tích Dự báo & AI/ML (AIOps): Áp dụng thuật toán học máy để phát
hiện bất thường (Anomaly Detection), dự báo sớm cạn kiệt tài nguyên
(Capacity Forecasting) và lọc bớt tín hiệu cảnh báo nhiễu (Alert Noise
Reduction).

### 6. Cách ly & Bảo vệ Mặt phẳng Quản trị (Management Plane Isolation)

**Tách biệt lưu lượng vận hành:** Lưu lượng truyền tải dữ liệu giám sát,
điều khiển và quản trị (O&M Traffic) được cô lập hoàn toàn với lưu lượng
ứng dụng end-user (Data Plane), đảm bảo khi ứng dụng bị quá tải hoặc tấn
công DDoS, Ops Platform vẫn hoạt động bình thường để xử lý sự cố.

**Tính toàn vẹn & Bất biến của Log (Log Immutability):** Dữ liệu nhật ký
vận hành và audit được ghi theo cơ chế WORM (Write Once Read Many), đảm
bảo chống sửa đổi/xóa bỏ nhằm phục vụ công tác điều tra sự cố và tuân
thủ pháp lý.

## Quan hệ với các lớp năng lực khác

Ops Platform giữ vai trò **\"hệ thần kinh và bộ máy điều phối trung
tâm\"**, kết nối 4 lớp năng lực qua các luồng tương tác 2 chiều:

- **Điều khiển & Giám sát Hạ tầng với (1) Compute & Connectivity:** Ops
  Platform nhận tài nguyên thô từ Lớp 1 để chạy bộ công cụ quản lý.
  Ngược lại, nó chuyển đổi hạ tầng thô thành *Infrastructure as Code*
  (mã hóa hạ tầng) để tự động khởi tạo, mở rộng máy chủ/mạng và liên tục
  đo lường sức khỏe phần cứng.

- **Thi hành & Báo cáo an ninh với (3) Security & Identity:** Lớp 3 đặt
  ra quy tắc định danh và chính sách bảo mật; Ops Platform trực tiếp thi
  hành thông qua kiểm soát quyền Admin (RBAC/PAM) và tự động hóa quy
  trình vá lỗ hổng. Đồng thời, nó liên tục thu thập nhật ký (audit log)
  từ toàn hệ thống để đẩy về SIEM/EDR của Lớp 3 phân tích đe dọa.

- **Thúc đẩy vòng đời ứng dụng với (4) App & Integration:** Ops Platform
  cung cấp đường ống CI/CD giúp tự động hóa việc đóng gói và triển khai
  phần mềm từ dev lên production. Khi ứng dụng chạy, Ops Platform cắm
  các sensor thu thập chỉ số (latency, error rate) và truy vết (tracing)
  để phát hiện và cảnh báo sớm các điểm nghẽn microservices hay API.

- **Bảo vệ & Tối ưu dữ liệu với (5) Data Platform:** Ops Platform liên
  tục theo dõi tải của cơ sở dữ liệu và các đường ống luồng dữ liệu
  (ETL/Stream) để tránh nghẽn I/O. Nó tự động hóa hoàn toàn lịch trình
  sao lưu/phục hồi thảm họa (Backup/DR), đồng thời áp dụng FinOps để tự
  động phân tầng dữ liệu cũ xuống bộ nhớ giá rẻ, giúp tối ưu chi phí.

**Bản chất:** Ops Platform là **\"lớp keo dính\"** biến các thành phần
phần cứng, ứng dụng và dữ liệu rời rạc thành một hệ thống tự động, có
khả năng tự quan sát (observability) và vận hành an toàn dưới khung
chính sách bảo mật chung.

# Security & Identity

## Khái niệm

**Security & Identity (An toàn thông tin & Định danh)** là một trong 5
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

**Nguồn:** [Microsoft Security -- Quản lý danh tính và truy nhập (IAM)
là
gì?](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-identity-access-management-iam)

**Cơ sở pháp lý tại Việt Nam.** Luật An ninh mạng số 116/2025/QH15 (ban
hành 10/12/2025, hiệu lực 01/7/2026) được xây dựng trên cơ sở **kế thừa,
hợp nhất các quy định còn phù hợp của Luật An ninh mạng 2018 và Luật An
toàn thông tin mạng 2015**. Luật quy định phân loại hệ thống thông tin
theo **5 cấp độ an ninh mạng** làm căn cứ áp dụng các biện pháp bảo vệ
tương ứng, trong đó hệ thống thông tin quan trọng về an ninh quốc gia ở
cấp độ 5; đồng thời khẳng định bảo đảm an ninh dữ liệu là bộ phận quan
trọng của bảo vệ an ninh mạng.

**Nguồn:** [Luật An ninh mạng 2025 số 116/2025/QH15 (toàn
văn)](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-An-ninh-mang-2025-so-116-2025-QH15-666020.aspx)

## Vai trò

  -----------------------------------------------------------------------
  **Vai trò**        **Diễn giải theo tài liệu Microsoft Security**
  ------------------ ----------------------------------------------------
  Cấp quyền truy     Cho phép các thực thể đã được xác minh truy nhập tài
  nhập an toàn       nguyên công ty: email, cơ sở dữ liệu, dữ liệu, ứng
                     dụng.

  Quyết định phạm vi Sau khi xác thực, hệ thống xác định người dùng được
  truy cập           truy cập tài nguyên nào theo chức danh, mức bảo mật
                     và dự án được phân công.

  Cân bằng bảo mật   Để nhân viên hợp lệ làm việc thuận lợi, đồng thời
  với hiệu quả làm   ngăn truy cập trái phép -- đây là mục tiêu kép của
  việc               IAM.

  Ứng phó mối đe dọa Giúp tổ chức thích ứng với các mối đe dọa an ninh
  đang biến đổi      mạng ngày càng thay đổi.

  Bảo đảm tuân thủ   Cung cấp **vết kiểm tra (audit trail)** và kiểm soát
                     truy cập để đáp ứng các quy định về bảo vệ dữ liệu.

  Nền cho MFA, SSO   MFA thêm bước xác minh ngoài mật khẩu; SSO đơn giản
  và RBAC            hoá truy cập nhiều hệ thống; RBAC cấp quyền theo
                     chức năng công việc.
  -----------------------------------------------------------------------

**Nguồn:** [Microsoft Security -- Quản lý danh tính và truy nhập (IAM)
là
gì?](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-identity-access-management-iam)

## Các thành phần

  -----------------------------------------------------------------------
  **Miền (cột    **Thành phần của lớp Security + Identity**
  của bảng slide 
  17)**          
  -------------- --------------------------------------------------------
  Phần cứng      Appliance/sensor, HSM/TPM (nếu có), firewall/WAF
                 (on-premise).

  Phần mềm       IAM/SSO/MFA, PAM, EDR/XDR, SIEM/SOAR, DLP, KMS, quản lý
                 lỗ hổng (vuln mgmt).

  Mạng           ZTNA/VPN, IDS/IPS, đường đi qua WAF, phân đoạn mạng /
                 Zero Trust.

  Quản trị       Chính sách (policy), quản lý rủi ro & tuân thủ, rà soát
                 quyền truy cập (access review), kịch bản ứng phó sự cố
                 (IR playbook).

  Bảo mật        Lớp "bao trùm": identity + policy + detection/response
                 cho (1)-(5).
  -----------------------------------------------------------------------

**Nguồn:** bảng "Khung tham chiếu phổ biến", slide 17 -- Chương 2
(2.pdf) -- bảng này liệt kê nguyên văn các thành phần trên.

## Đặc điểm kĩ thuật

**(a) Xác thực và cấp quyền là hai bước khác nhau.** Bước **xác thực**
đối chiếu thông tin đăng nhập của người dùng với cơ sở dữ liệu những
người dùng được phép -- tức chứng minh "bạn là ai". Bước **cấp quyền**
mới quyết định người dùng đã xác thực được truy cập tài nguyên nào và
làm gì với tài nguyên đó, dựa trên chức danh, mức bảo mật, dự án được
phân công. Ngoài ra hệ thống lưu **vết kiểm tra (audit trail)** để phục
vụ điều tra và chứng minh tuân thủ. Vì vậy đăng nhập thành công không
đồng nghĩa với việc được phép truy cập mọi tài nguyên.

**Nguồn:** [Microsoft Security -- Quản lý danh tính và truy nhập (IAM)
là
gì?](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-identity-access-management-iam)

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

**Nguồn:** [Microsoft Security -- Xác thực đa yếu tố (MFA) là
gì?](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-multifactor-authentication-mfa)

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

**Nguồn:** [Microsoft Security -- SAML (Ngôn ngữ đánh dấu xác nhận bảo
mật) là
gì?](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-security-assertion-markup-language-saml)

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

**Nguồn:** [Microsoft Security -- Quản lý quyền truy nhập đặc quyền
(PAM) là
gì?](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-privileged-access-management-pam)

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

**Nguồn:** [VNPT Cloud -- Zero Trust là gì? 05 trụ cột cốt lõi của mô
hình bảo mật Zero
Trust](https://cloud.vnpt.vn/blog/zero-trust-la-gi-05-tru-cot-cot-loi-cua-mo-hinh-bao-mat-zero-trust-168)

**(f) Mã hoá và quản lý khoá.** **"Độ an toàn của bất kỳ hệ thống mật mã
nào cũng đều phụ thuộc vào độ an toàn của khóa"**, vì lý do đó khóa luôn
phải được bảo vệ ở mức cao nhất. Rủi ro điển hình: nếu dùng cùng một
khóa để mã hóa nhiều thông điệp trong thời gian dài, kẻ tấn công có thể
thu thập đủ bản mã rồi khám phá ra một phần hoặc toàn bộ khóa; và khi
một khóa bị lộ thì mọi thành phần còn dùng khóa đó đều bị nguy hiểm. Do
đó vấn đề quan trọng là **quản lý khóa (key management)** -- thuật ngữ
chỉ toàn bộ hoạt động liên quan đến một **vòng đời của khóa**: sinh
khóa, phân phối, sử dụng, lưu trữ và hủy bỏ khóa.

**Nguồn:** [Tạp chí An toàn thông tin (Ban Cơ yếu Chính phủ) -- Tiêu
chuẩn quốc gia Việt Nam về Quản lý
khóa](https://antoanthongtin.vn/tin/tieu-chuan-quoc-gia-viet-nam-ve-quan-ly-khoa)

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

**Nguồn:** [Microsoft Security -- Phát hiện và phản hồi mở rộng (XDR) là
gì?](https://www.microsoft.com/vi-vn/security/business/security-101/what-is-xdr)

## Rủi ro nhắm vào danh tính và cách kiểm soát

**Các rủi ro có thể phát hiện được** ở tầng danh tính gồm: **tấn công dò
mật khẩu** (brute force), **đăng nhập từ IP ẩn danh** và **rò rỉ thông
tin đăng nhập**. Cách kiểm soát tương ứng là **chính sách truy cập thích
ứng dựa trên rủi ro**: khi phát hiện dấu hiệu vi phạm, hệ thống **chặn,
yêu cầu xác thực đa yếu tố và khắc phục rủi ro** theo thời gian thực;
việc phát hiện và tự động khắc phục tình trạng xâm phạm danh tính áp
dụng cho cả phương thức xác thực dùng mật khẩu lẫn không dùng mật khẩu.

**Nguồn:** [Microsoft Security -- Bảo vệ Danh tính Microsoft
Entra](https://www.microsoft.com/vi-vn/security/business/identity-access/microsoft-entra-id-protection)

## Nghĩa vụ tuân thủ tại Việt Nam

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Trục**   **Nghĩa vụ / nội dung liên quan đến     **Nguồn (1 link)**
             Security + Identity**                   
  ---------- --------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  An ninh    Phân loại hệ thống thông tin theo 5 cấp [Luật An ninh mạng 2025 (116/2025/QH15)](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-An-ninh-mang-2025-so-116-2025-QH15-666020.aspx)
  mạng theo  độ an ninh mạng để áp dụng biện pháp    
  cấp độ     bảo vệ tương ứng.                       

  Yêu cầu an Yêu cầu cơ bản về an toàn hệ thống      [TCVN 11930:2017 (VSQI)](https://tieuchuan.vsqi.gov.vn/tieuchuan/view?sohieu=TCVN+11930%3A2017)
  toàn theo  thông tin theo từng cấp độ (yêu cầu     
  cấp độ     quản lý và yêu cầu kỹ thuật).           

  Hồ sơ đề   Trình tự xác định cấp độ, lập hồ sơ đề  [Nghị định 85/2016/NĐ-CP](https://vanban.chinhphu.vn/?pageid=27160&docid=185601)
  xuất cấp   xuất cấp độ và phương án bảo đảm an     
  độ         toàn hệ thống thông tin.                

  Định danh  Tài khoản định danh điện tử, dịch vụ    [Nghị định 69/2024/NĐ-CP](https://vanban.chinhphu.vn/?pageid=27160&docid=210491)
  & xác thực xác thực điện tử và điều kiện kết nối   
  điện tử    với Hệ thống định danh và xác thực điện 
             tử.                                     

  Chữ ký     Yêu cầu với chữ ký điện tử, chứng thư   [Nghị định 23/2025/NĐ-CP](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-23-2025-nd-cp-quy-dinh-ve-chu-ky-dien-tu-va-dich-vu-tin-cay-119250225073330307.htm)
  điện tử &  chữ ký điện tử và các dịch vụ tin cậy.  
  dịch vụ                                            
  tin cậy                                            

  Dữ liệu cá Quyền của chủ thể dữ liệu; cấm mua bán  [Luật Bảo vệ dữ liệu cá nhân 2025 (91/2025/QH15)](https://chinhphu.vn/?pageid=27160&docid=214590&classid=1&typegroupid=3)
  nhân       dữ liệu cá nhân; mạng xã hội không được 
             yêu cầu giấy tờ định danh có ảnh/video  
             làm yếu tố xác thực. Hiệu lực           
             01/01/2026.                             

  Mật mã dân Điều kiện kinh doanh sản phẩm, dịch vụ  [Nghị định
  sự         mật mã dân sự và xuất nhập khẩu sản     58/2016/NĐ-CP](https://thuvienphapluat.vn/van-ban/Thuong-mai/Nghi-dinh-58-2016-ND-CP-kinh-doanh-san-pham-dich-vu-mat-ma-dan-su-xuat-nhap-khau-mat-ma-dan-su-2016-315422.aspx)
             phẩm mật mã dân sự (liên quan HSM, giải 
             pháp mã hoá, thiết bị VPN).             
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Quan hệ với 4 lớp năng lực còn lại

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

**Nguồn:** bảng "Khung tham chiếu phổ biến", slide 17 -- Chương 2
(2.pdf)

# App & Integration Platform

## Khái niệm

**App & Integration Platform (Nền tảng Ứng dụng và Tích hợp)** là lớp
năng lực trung gian trong kiến trúc hạ tầng CNTT doanh nghiệp, chịu
trách nhiệm xây dựng, triển khai, vận hành và tích hợp các ứng dụng cũng
như dịch vụ phần mềm. Lớp này cung cấp môi trường thực thi (runtime
environment), điều phối (orchestration) và kết nối giữa các hệ thống
nghiệp vụ nội bộ (ERP, CRM, Core Banking, Legacy Systems) với các dịch
vụ bên ngoài như Cloud Services, Partner APIs hoặc Third-party SaaS.

Trong khung tham chiếu hạ tầng CNTT, App & Integration Platform nằm
giữa:

- **Bên dưới:** Lớp (1) Compute & Connectivity cung cấp hạ tầng tính
  toán, lưu trữ và mạng; cùng lớp (3) Security + Identity cung cấp định
  danh, xác thực và chính sách bảo mật xuyên suốt.

- **Bên trên:** Lớp (5) Data Platform, nơi dữ liệu được lưu trữ, quản
  trị và phân tích.

Nhờ đó, lớp này đóng vai trò cầu nối giúp các hệ thống độc lập có thể
giao tiếp với nhau một cách chuẩn hóa, an toàn, linh hoạt và có khả năng
mở rộng, thay thế mô hình kết nối điểm-điểm (Point-to-Point) vốn khó bảo
trì.

Trong các hệ thống hiện đại, App & Integration Platform gắn liền với
kiến trúc **Cloud-Native**, **Container**, **Microservices** và
**Kubernetes**, cho phép tự động hóa việc triển khai, mở rộng quy mô và
quản lý vòng đời ứng dụng.

## Vai trò

Lớp năng lực App & Integration Platform đảm nhận 6 vai trò chiến lược
cốt lõi trong mô hình tổng thể hạ tầng CNTT doanh nghiệp.

### Cầu nối tích hợp & Xóa bỏ ốc đảo dữ liệu (Data Silos)

Lớp này chịu trách nhiệm kết nối các hệ thống ứng dụng riêng lẻ (như
ERP, CRM, Core Banking, các hệ thống legacy cũ) với nhau và mở rộng kết
nối tới đối tác/bên thứ ba thông qua API, Message Queue, Event Bus. Giải
pháp này thay thế hoàn toàn mô hình kết nối điểm-điểm (point-to-point)
phức tạp, chồng chéo và khó bảo trì; từ đó cho phép các hệ thống giao
tiếp, liên thông và chia sẻ dữ liệu tự động theo thời gian thực.

### Nền tảng phát triển & Tăng tốc đổi mới (Agility & Innovation)

Lớp này cung cấp một môi trường runtime chuẩn hóa dựa trên các công nghệ
hiện đại như Container, Kubernetes, Microservices và Serverless. Môi
trường này giúp rút ngắn đáng kể vòng đời phát triển phần mềm (SDLC),
giúp đội ngũ phát triển triển khai ứng dụng nhanh chóng, nhất quán và
chuyển đổi việc phát hành phần mềm từ các thao tác thủ công dễ lỗi thành
một quy trình tự động, có thể lặp lại ở quy mô lớn.

### Kiểm soát luồng giao tiếp & Chuẩn hóa điểm truy cập

Thông qua thành phần trung tâm là API Gateway, lớp này đóng vai trò là
\"cửa ngõ\" duy nhất kiểm soát toàn bộ lưu lượng truy cập (Traffic flow)
đi vào và đi ra. API Gateway thực thi việc xác thực quyền gọi API, quản
lý phân luồng, giới hạn tốc độ truy cập (Rate limiting/Throttling) để
bảo vệ các dịch vụ backend phía sau khỏi nguy cơ quá tải hoặc tấn công
mạng.

### Mở rộng linh hoạt & Tăng khả năng chịu lỗi (Scalability & Resilience)

Nhờ kiến trúc microservices kết hợp với cơ chế điều phối của Kubernetes,
lớp này cho phép hệ thống tự động mở rộng độc lập từng vi dịch vụ theo
chiều ngang (Horizontal Scaling) linh hoạt theo lượng tải thực tế. Việc
mở rộng hoặc nâng cấp một dịch vụ cụ thể diễn ra mịn màng mà không làm
gián đoạn hay ảnh hưởng đến toàn bộ hệ thống chung.

### Nền tảng thực thi phương pháp luận DevOps / SRE

Lớp này tạo ra môi trường kỹ thuật tiêu chuẩn để áp dụng các quy trình
phát triển và vận hành hiện đại như CI/CD, GitOps, quản lý phiên bản API
(Versioning) và khả năng quan sát ứng dụng (App Observability). Việc này
giúp biến đổi các chỉ số đo lường độ tin cậy (SLO/SLA) thành các chính
sách vận hành thực tế.

### Điểm thực thi chính sách bảo mật ứng dụng

Lớp này là nơi cụ thể hóa các nguyên tắc bảo mật và kiến trúc Zero Trust
ở tầng ứng dụng. Các nhiệm vụ bảo mật được thực thi trực tiếp tại đây
bao gồm: xác thực và phân quyền truy cập (AuthN/Z), bảo vệ lưu lượng
API, quản lý tập trung các chuỗi bí mật (Secrets management) và tự động
quét lỗ hổng bảo mật của container image trước khi đưa lên môi trường
vận hành.

## Các thành phần

### Phần cứng (Hardware - HW)

- **Nguyên lý kế thừa:** Lớp này không sở hữu hạ tầng vật lý riêng biệt
  mà \"tận dụng\" và kế thừa trực tiếp năng lực tính toán (Compute
  fabric, Virtual Machines, Cloud Instances) từ **Lớp (1) Compute &
  Connectivity**.

- **Đặc tính kỹ thuật:** Cấu hình phần cứng ở lớp (1) phục vụ cho
  Lớp (4) phải tối ưu hóa cho Container Runtime (tối ưu phân bổ CPU/RAM
  linh hoạt). Yêu cầu năng lực hỗ trợ **Horizontal Scaling** (mở rộng
  theo chiều ngang) để các cụm máy chủ tự động tăng/giảm số lượng node
  theo lượng tải thực tế, khác biệt so với mô hình chạy ứng dụng nguyên
  khối (Monolithic) cố định.

### 2. Phần mềm (Software - SW) --- Trọng tâm của lớp

Thành phần phần mềm trong Lớp (4) đóng vai trò là lõi vận hành và điều
phối:

- **Middleware / ESB (Enterprise Service Bus):** Tầng phần mềm trung
  gian đảm nhận nhiệm vụ chuyển đổi định dạng dữ liệu (Data
  transformation), định tuyến thông điệp và tích hợp các hệ thống cũ
  (Legacy systems) với các ứng dụng hiện đại mà không bắt buộc thay đổi
  cấu trúc mã nguồn của hệ thống gốc.

- **API Gateway:** Point-of-entry (điểm vào) duy nhất quản lý toàn bộ
  API. Theo tài liệu của AWS (Amazon API Gateway Documentation), API
  Gateway là dịch vụ được quản lý giúp nhà phát triển xuất bản, bảo mật,
  giám sát và vận hành API ở quy mô lớn. Thành phần này thực thi xác
  thực (Cognito/IAM/Custom Authorizer), định tuyến yêu cầu, quản lý môi
  trường (Dev/Staging/Prod) và áp dụng cơ chế giới hạn tần suất (Rate
  Limiting/Throttling) để chống quá tải cho dịch vụ phía sau.

- **Microservices & Container / Kubernetes (K8s):**

  - **Container:** Đóng gói mã nguồn ứng dụng cùng toàn bộ thư viện liên
    quan (dependencies) thành một đơn vị thực thi độc lập, nhất quán
    trên mọi môi trường.

  - **Kubernetes (K8s):** Nền tảng điều phối (orchestrator) tự động hóa
    quá trình đóng gói, triển khai, mở rộng và quản lý container. K8s
    nhóm các container thành các đơn vị logic gọi là **Pod** để quản lý
    tài nguyên và tự động phục hồi khi gặp sự cố (Self-healing).

- **Service Mesh (Thành phần nâng cao/Tùy chọn):** Lớp hạ tầng chuyên
  dụng (sử dụng các công nghệ như Istio, Linkerd) quản lý giao tiếp nội
  bộ giữa các microservices thông qua mô hình *Sidecar Proxy*. Service
  Mesh cung cấp khả năng quan sát traffic, cân bằng tải nâng cao và tự
  động mã hóa giao tiếp nội bộ bằng **mTLS (Mutual TLS)** mà không cần
  can thiệp vào mã nguồn ứng dụng.

- **Message Queue / Event Bus:** Cơ chế truyền nhận tin bất đồng bộ
  (Asynchronous messaging) sử dụng các công nghệ như Apache Kafka,
  RabbitMQ. Giúp triệt tiêu sự phụ thuộc trực tiếp (Loosely Coupled)
  giữa các microservices, tăng khả năng chịu lỗi và đảm bảo tính sẵn
  sàng cao khi có sự cố cục bộ.

### 3. Mạng (Network)

- **Ingress / Egress Control:** Quản lý và kiểm soát chặt chẽ luồng lưu
  lượng dữ liệu đi vào (Ingress) và đi ra (Egress) khỏi cụm ứng dụng/K8s
  cluster.

- **Routing nội bộ & Service Discovery:** Giải quyết thách thức địa chỉ
  IP thay đổi liên tục trong môi trường container (các Pod được tạo/xóa
  liên tục). Sử dụng cơ chế tự động phát hiện dịch vụ (Service
  Discovery - ví dụ: CoreDNS) để các microservices tự tìm thấy nhau
  thông qua tên miền nội bộ.

- **Load Balancing (LB):** Cân bằng tải ở cả Lớp 4 (Transport layer) và
  Lớp 7 (Application layer) nhằm phân bổ đều lượng truy cập đến các
  instance của dịch vụ.

- **API Traffic Control:** Điều phối băng thông, thực thi các thuật toán
  cắt giảm lưu lượng bất thường (Traffic Shifting, Throttling), bảo vệ
  hệ thống backend khỏi các cuộc tấn công từ chối dịch vụ (DDoS/DoS).

### 4. Quản trị (Governance / Ops)

- **CI/CD & GitOps:** Tự động hóa toàn bộ pipeline từ xây dựng (Build),
  kiểm thử (Test) đến triển khai (Deploy) phần mềm thông qua các công cụ
  như Jenkins, GitLab CI, ArgoCD. Phương pháp luận GitOps sử dụng Git
  làm nguồn sự thật (Single Source of Truth) để quản lý cấu hình và hạ
  tầng dưới dạng mã (IaC).

- **Release / Change Management & API Versioning:** Quản lý vòng đời
  phát hành và phiên bản API (v1, v2\...) nghiêm ngặt, đảm bảo tính
  tương thích ngược (Backward compatibility) để việc nâng cấp hệ thống
  không làm gián đoạn các ứng dụng đang khai thác API cũ.

- **SRE Practice (Site Reliability Engineering):** Áp dụng các chỉ số kỹ
  thuật để đo lường và duy trì độ tin cậy của ứng dụng: **SLA** (Service
  Level Agreement), **SLO** (Service Level Objective), **SLI** (Service
  Level Indicator) và quản lý Ngân sách rủi ro (Error Budgets).

- **App Observability (Khả năng quan sát ứng dụng):** Thu thập và phân
  tích toàn diện dữ liệu vận hành dựa trên 3 trụ cột cốt lõi (Telemetry
  Data):

  1.  *Metrics:* Đo lường chỉ số định lượng thời gian thực (Prometheus).

  2.  *Logs:* Ghi chép nhật ký sự kiện hệ thống (ELK Stack / Fluentd).

  3.  *Traces:* Truy vết hành trình của từng request xuyên qua các
      microservices (Jaeger / Zipkin).

### 5. Bảo mật (Security)

- **AuthN / AuthZ (Authentication & Authorization):** Chuẩn hóa việc xác
  thực và phân quyền người dùng cũng như dịch vụ dựa trên các tiêu chuẩn
  công nghiệp: **OIDC (OpenID Connect)**, **OAuth 2.0**, và **SAML
  2.0**.

- **Secrets Management:** Quản lý, mã hóa và phân phối tập trung các
  chuỗi thông tin nhạy cảm (API keys, database credentials, TLS
  certificates) bằng các giải pháp chuyên dụng như HashiCorp Vault hoặc
  AWS Secrets Manager, loại bỏ hoàn toàn việc lưu mật khẩu trực tiếp
  trong mã nguồn (Hardcoded secrets).

- **Runtime Security:** Giám sát, phát hiện và ngăn chặn các hành vi bất
  thường của ứng dụng và container ngay trong thời gian thực (Runtime)
  khi hệ thống đang vận hành.

- **API Security & WAF (Web Application Firewall):** Bảo vệ API và ứng
  dụng web khỏi các nguy cơ an ninh phổ biến (OWASP Top 10) như SQL
  Injection, Cross-Site Scripting (XSS), Broken Object Level
  Authorization (BOLA).

- **Container Image Scanning:** Tự động kiểm tra và quét lỗ hổng bảo mật
  (Vulnerabilities) trong các file đóng gói container image (sử dụng
  Trivy, Clair\...) trước khi cho phép đẩy lên kho lưu trữ (Registry) và
  triển khai lên môi trường Production.

## Đặc điểm kĩ thuật

**Các đặc điểm kỹ thuật về bảo mật:**

- Xác thực và phân quyền: Hỗ trợ OAuth 2.0, OpenID Connect (OIDC), SAML
  2.0, JWT và RBAC/ABAC.

- Quản lý bí mật (Secrets Management): Lưu trữ và cấp phát an toàn các
  khóa API, mật khẩu và chứng chỉ thông qua Vault hoặc dịch vụ KMS.

- Bảo mật API: API Gateway kết hợp WAF, Rate Limiting, IP Filtering,
  chống tấn công DDoS và kiểm tra nội dung đầu vào.

- Bảo mật Runtime: Kiểm soát container runtime, image scanning,
  admission control và chính sách bảo mật Kubernetes.

- Mã hóa: Hỗ trợ TLS/mTLS cho giao tiếp giữa các dịch vụ và mã hóa dữ
  liệu nhạy cảm.

- Kiểm toán: Ghi nhận nhật ký truy cập, thay đổi cấu hình và các hoạt
  động quản trị phục vụ điều tra và tuân thủ.

**Các đặc điểm kỹ thuật về vận hành:**

- Hỗ trợ triển khai liên tục (Continuous Deployment) và tích hợp liên
  tục (Continuous Integration).

- Quản lý vòng đời ứng dụng từ phát triển, kiểm thử, triển khai đến
  ngừng hoạt động.

- Theo dõi các chỉ số SLI/SLO, thời gian phản hồi, tỷ lệ lỗi và mức sử
  dụng tài nguyên.

- Hỗ trợ tự động khôi phục (Self-healing), rollback khi triển khai thất
  bại và cân bằng tải thông minh.

## Quan hệ với các lớp năng lực khác

Lớp **App & Integration Platform** là cầu nối giữa hạ tầng, dữ liệu và
các ứng dụng nghiệp vụ, cung cấp môi trường triển khai và tích hợp các
dịch vụ trong hệ thống.

- **Với Compute & Connectivity:** Sử dụng tài nguyên tính toán, lưu trữ
  và mạng để triển khai và vận hành ứng dụng.

- **Với Ops Platform:** Được giám sát, quản lý và tự động hóa triển khai
  thông qua các công cụ vận hành (CI/CD, monitoring, logging).

- **Với Security & Identity:** Áp dụng các cơ chế xác thực, phân quyền
  và bảo mật để bảo vệ ứng dụng và API.

- **Với Data Platform:** Khai thác, xử lý và trao đổi dữ liệu với các cơ
  sở dữ liệu, kho dữ liệu và hệ thống phân tích.

Nhờ liên kết với bốn lớp còn lại, **App & Integration Platform** đảm bảo
các ứng dụng được triển khai, tích hợp và vận hành hiệu quả, an toàn và
có khả năng mở rộng.

# Data Platform

## Khái niệm

Trong tổng thể kiến trúc hạ tầng công nghệ thông tin (CNTT) doanh
nghiệp, hạ tầng không chỉ dừng lại ở các thiết bị vật lý hay mạng kết
nối thô, mà là một hệ thống đa tầng kết hợp kỹ thuật, vận hành và quản
trị để đảm bảo các hệ thống số hoạt động ổn định, an toàn và tối ưu chi
phí. Trong mô hình hạ tầng tham chiếu chuẩn hóa gồm 5 lớp năng lực cốt
lõi, lớp **Data Platform** (Nền tảng dữ liệu) đóng vai trò là trung tâm
lưu trữ, xử lý, khai thác và quản trị toàn bộ tài sản dữ liệu của tổ
chức.

Data Platform là tập hợp các công nghệ phần cứng, phần mềm, luồng truyền
tải mạng, cơ chế kiểm soát vận hành và chính sách an toàn thông tin được
thiết kế để quản lý dữ liệu xuyên suốt vòng đời---từ khi khởi tạo, thu
thập, biến đổi, lưu trữ cho đến khi phân tích và tiêu hủy. Khác với các
ứng dụng nghiệp vụ đơn lẻ, Data Platform cung cấp năng lực nền tảng nhất
quán cho phép kết nối các hệ thống giao dịch (OLTP), hệ thống phân tích
(OLAP), báo cáo thông minh (BI) và các mô hình học máy hay trí tuệ nhân
tạo (AI/ML).

## Vai trò

Vai trò chiến lược của Data Platform thể hiện ở ba khía cạnh cốt lõi:

- **Xóa bỏ các vùng cô lập dữ liệu (Data Silos):** Hợp nhất dữ liệu từ
  nhiều nguồn ứng dụng khác nhau (ERP, CRM, LMS, IoT) về một môi trường
  quản lý tập trung hoặc phân tán có kiểm soát.

- **Đảm bảo tính tin cậy và chất lượng dữ liệu:** Cung cấp chuẩn mực về
  định dạng, quy trình làm sạch và kiểm soát nguồn gốc dữ liệu để đảm
  bảo mọi quyết định kinh doanh đều dựa trên thông tin chính xác.

- **Thúc đẩy giá trị kinh doanh từ dữ liệu:** Tạo tiền đề kỹ thuật vững
  chắc để triển khai phân tích thời gian thực (real-time analytics), tối
  ưu hóa vận hành và tuân thủ các quy định pháp lý khắt khe về dữ liệu.

## Các thành phần

### Hạ Tầng Phần Cứng (Hardware - HW)

Hạ tầng phần cứng của Data Platform kế thừa và tận dụng năng lực tính
toán và kết nối cơ bản từ **Lớp Compute & Connectivity**. Tuy nhiên, do
đặc thù xử lý khối lượng dữ liệu khổng lồ với tần suất truy xuất cao,
phần cứng dành cho Data Platform có những yêu cầu chuyên biệt:

- **Tối ưu hóa năng lực I/O (Input/Output Performance):** Hệ thống đòi
  hỏi các dòng máy chủ trang bị bộ vi xử lý nhiều nhân, dung lượng RAM
  lớn và hệ thống lưu trữ có chỉ số IOPS (Input/Output Operations Per
  Second) cực cao như ổ cứng NVMe SSD, hệ thống SAN/NAS băng thông rộng
  hoặc kiến trúc lưu trữ phân tán.

- **Khả năng co giãn (Scalability):** Dù triển khai theo mô hình
  On-premise hay Cloud (Compute/Storage Fabric), phần cứng phải hỗ trợ
  cả hai cơ chế mở rộng dọc (Scale-up - nâng cấp CPU/RAM) và mở rộng
  ngang (Scale-out - thêm nút vào cụm tính toán/lưu trữ) nhằm đáp ứng sự
  tăng trưởng dữ liệu không ngừng mà không làm gián đoạn dịch vụ.

### Lớp Phần Mềm Và Dịch Vụ (Software - SW)

Lớp phần mềm cấu thành Data Platform bao gồm các công nghệ quản trị, xử
lý và lưu trữ dữ liệu từ mức độ thô đến mức độ cấu trúc cao:

- **Hệ quản trị cơ sở dữ liệu (DBMS):** Cung cấp khả năng lưu trữ và
  truy vấn dữ liệu giao dịch hoặc phi cấu trúc (RDBMS, NoSQL, NewSQL).

- **Kho dữ liệu và Hồ dữ liệu (DW / Data Lake / Lakehouse):** Kiến trúc
  kết hợp giữa kho dữ liệu tối ưu cho truy vấn phân tích structured data
  (Data Warehouse) và hồ dữ liệu chứa dữ liệu thô/phi cấu trúc (Data
  Lake) theo mô hình Data Lakehouse hiện đại, giúp tối ưu hóa chi phí
  lưu trữ và hiệu năng phân tích.

- **Công cụ tích hợp dữ liệu (ETL/ELT & Streaming):** Thực hiện trích
  xuất, biến đổi và nạp dữ liệu theo lô (Batch Processing via ETL/ELT)
  hoặc xử lý dòng dữ liệu liên tục theo thời gian thực (Event Streaming
  via Kafka/Kinesis).

- **Danh mục dữ liệu & Nguồn gốc dữ liệu (Data Catalog / Lineage):** Cho
  phép tìm kiếm, phân loại và theo dõi luồng dịch chuyển dữ liệu từ điểm
  đầu đến điểm cuối trong toàn bộ kiến trúc.

- **Quản lý dữ liệu chủ & Tối ưu chất lượng dữ liệu (MDM & DQ
  Tooling):** Đảm bảo tính duy nhất, nhất quán của các thực thể dữ liệu
  quan trọng (khách hàng, sản phẩm) và tự động hóa quá trình kiểm tra,
  làm sạch dữ liệu.

### Mạng Và Hạ Tầng Truyền Dẫn (Network)

Mạng đóng vai trò là \"hệ tuần hoàn\" đảm bảo luồng di chuyển dữ liệu
giữa các hệ thống nguồn và Data Platform diễn ra thông suốt và an toàn:

- **Kết nối nguồn dữ liệu (Source Connectivity):** Thiết lập các đường
  truyền kết nối an toàn (VPC Peering, Direct Connect, VPN, API
  Gateways) để thu thập dữ liệu từ ứng dụng nội bộ, thiết bị ngoại biên
  hoặc các dịch vụ SaaS bên ngoài.

- **Truyền tải dữ liệu theo lô và dòng (Batch & Stream Movement):** Băng
  thông mạng phải được tính toán để xử lý các đợt chuyển dữ liệu dung
  lượng lớn (Batch Ingestion) trong khung giờ thấp điểm mà không làm
  nghẽn hệ thống, đồng thời đảm bảo độ trễ thấp (Low Latency) cho các
  luồng dữ liệu thời gian thực (Stream Ingestion).

- **Đồng bộ và nhân bản (Replication & Synchronization):** Hỗ trợ cơ chế
  Change Data Capture (CDC) để đồng bộ biến động dữ liệu tức thì từ các
  CSDL vận hành về nền tảng phân tích.

### Quản Trị Và Vận Hành Dữ Liệu (Governance / Ops)

Quản trị dữ liệu là yếu tố then chốt biến dữ liệu từ \"tài nguyên thô\"
thành \"tài sản chiến lược\" có thể kiểm soát được. Trụ cột này được
thiết kế dựa trên các tiêu chuẩn quốc tế như DAMA-DMBOK và TOGAF:

- **Quản trị dữ liệu (Data Governance & Stewardship):** Định ra khung
  chính sách, quy trình và phân công trách nhiệm rõ ràng (Data Stewards)
  đối với việc sở hữu, sử dụng và giám sát dữ liệu.

- **Chính sách lưu trữ và tiêu hủy (Data Retention Policies):** Quy định
  thời gian lưu trữ đối với từng loại dữ liệu nhằm tối ưu chi phí hạ
  tầng và tuân thủ các quy định pháp lý.

- **Quy tắc chất lượng & Chuẩn hóa siêu dữ liệu (DQ Rules & Metadata
  Standards):** Thiết lập các bộ tiêu chuẩn đánh giá độ chính xác, tính
  đầy đủ của dữ liệu và đồng bộ hóa từ điển dữ liệu (Business Glossary)
  trong toàn doanh nghiệp.

### Bảo Mật Và An Toàn Dữ Liệu (Security)

Security trong Data Platform không nằm riêng rẽ mà là một lớp bao trùm,
phối hợp chặt chẽ với **Lớp Security & Identity** để bảo vệ dữ liệu
trước các truy cập trái phép và nguy cơ rò rỉ:

- **Mã hóa dữ liệu (Encryption):** Áp dụng thuật toán mã hóa mạnh cho dữ
  liệu ở trạng thái nghỉ (At-rest - trên ổ đĩa, database) và dữ liệu
  đang truyền tải (In-transit - qua đường truyền mạng TLS/SSL).

- **Dịch vụ quản lý khóa (KMS):** Tích hợp hệ thống quản lý khóa mã hóa
  trung tâm để kiểm soát quyền khởi tạo, xoay vòng và thu hồi khóa an
  toàn.

- **Che giấu và Phân quyền truy cập chi tiết (Data Masking, Row/Column
  Security):** Sử dụng kỹ thuật làm mờ/mã hóa hóa dữ liệu nhạy cảm (PII)
  đối với môi trường thử nghiệm, kết hợp phân quyền truy cập theo từng
  hàng (Row-level) và từng cột (Column-level) dựa trên vai trò người
  dùng (RBAC/ABAC).

- **Phòng chống thất thoát & Ghi vết hoạt động (DLP & Data Access
  Audit):** Triển khai giải giải pháp ngăn chặn thất thoát dữ liệu và
  duy trì nhật ký truy cập (Audit logs) toàn diện nhằm phục vụ công tác
  truy vết và kiểm toán an ninh.

## Đặc điểm kĩ thuật

**Quản lý dữ liệu tập trung và hiệu quả:** Trước khi có Data platform,
nhiều doanh nghiệp gặp vấn đề "data silo", nghĩa là dữ liệu bị phân tán
theo phòng ban, gây khó khăn khi tổng hợp. Với nền tảng dữ liệu, tất cả
dữ liệu được gom về một hệ thống tập trung, giúp quản lý dữ liệu (data
management) hiệu quả, dễ truy xuất, và kiểm soát chất lượng.

**Hỗ trợ ra quyết định chính xác:** Dữ liệu tập trung và chuẩn hóa cho
phép trực quan hóa theo thời gian thực, giúp lãnh đạo ra quyết định dựa
trên dữ liệu (data-driven decision) thay vì cảm tính. Điều này đặc biệt
quan trọng trong các ngành như tài chính, bán lẻ, logistics, hay sản
xuất.

**Tăng hiệu quả vận hành và tiết kiệm chi phí:** Data platform giúp tự
động hóa nhiều quy trình thủ công: thu thập dữ liệu, chuẩn hóa dữ liệu,
lập báo cáo. Nhờ đó, doanh nghiệp tiết kiệm nhân lực, giảm lỗi, tăng tốc
độ xử lý và tối ưu chi phí vận hành.

**Nền tảng cho AI và Machine Learning (xu hướng hiện nay):** Một Data
platform hiện đại chính là cơ sở để triển khai AI/ML. Khi dữ liệu được
chuẩn hóa và tích hợp, doanh nghiệp có thể triển khai các mô hình dự
đoán, phân tích hành vi khách hàng, tối ưu marketing, hoặc dự đoán nhu
cầu sản xuất.

## Quan hệ với các lớp năng lực khác

Lớp năng lực Data Platform trong Khung tham chiếu kiến trúc hạ tầng CNTT
doanh nghiệp là nền tảng cốt lõi giúp tổ chức quản lý, bảo vệ và tối ưu
hóa giá trị của tài sản dữ liệu. Việc triển khai Data Platform đòi hỏi
sự đầu tư đồng bộ và cân bằng giữa 5 khía cạnh: trang bị phần cứng I/O
cao, lựa chọn phần mềm lưu trữ/xử lý linh hoạt, thiết lập hạ tầng mạng
kết nối thông suốt, duy trì kỷ luật quản trị dữ liệu nghiêm ngặt và bao
trùm bởi lớp bảo mật đa tầng. Việc tuân thủ khung tham chiếu này giúp
doanh nghiệp xây dựng một hạ tầng dữ liệu vững chắc, sẵn sàng đáp ứng
các yêu cầu phân tích cao cấp và trí tuệ nhân tạo trong tương lai.

Data Platform không hoạt động độc lập mà nằm trong một hệ sinh thái hạ
tầng phụ thuộc lẫn nhau. Nó nhận tài nguyên phần cứng từ **Compute &
Connectivity**, được vận hành thông qua các công cụ giám sát từ **Ops
Platform**, tuân thủ chính sách danh tính từ **Security & Identity**, và
cung cấp dữ liệu đầu vào/đầu ra cho các dịch vụ ứng dụng tại **App &
Integration Platform**.

Trong bối cảnh chuyển đổi số hiện đại, kiến trúc Data Platform đang tiến
hóa mạnh mẽ theo hai xu hướng chính:

- **Data Fabric:** Tự động hóa việc tích hợp, khám phá và quản trị dữ
  liệu bằng cách sử dụng phân tích metadata thông minh trên toàn bộ môi
  trường Hybrid Cloud.

- **Data Mesh:** Chuyển đổi từ mô hình dữ liệu tập trung sang mô hình
  phân tán theo miền nghiệp vụ (Domain-driven), coi dữ liệu như một sản
  phẩm (Data as a Product) nhưng vẫn duy trì sự quản trị nhất quán
  (Federated Computational Governance).
