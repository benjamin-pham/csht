**1. Hạ tầng tính toán & kết nối (Compute & Connectivity)**

\- Khái niệm: Là \"đất đai và nền móng\" của toàn bộ tòa nhà số trong
doanh nghiệp --- nơi mọi dữ liệu được xử lý, lưu trữ và luân chuyển. Đây
là lớp vật lý/hạ tầng cơ bản nhất trong 5 lớp năng lực CNTT: nếu ví hạ
tầng CNTT như một thành phố, thì lớp này chính là nền đất, hệ thống điện
-- nước và mạng lưới đường xá kết nối mọi khu vực với nhau.

\- Có nghĩa vụ cung cấp tài nguyên tính toán(Compute), lưu trữ(Storage)
và kết nối(Network), đảm bảo hệ thống hoạt động ổn định, sẵn sàng mở
rộng và hỗ trợ triển khai các dịch vụ số.

\- Có bao gồm thành phần: Data center / Cloud / Hybrid, Compute,
Storage, Network, SD-WAN, VPN.

+:--------------:+----------------+----------------+----------------+
| Nhóm           | Thành phần     | Chức năng      | Ví dụ          |
|                |                | chính          |                |
+----------------+----------------+----------------+----------------+
| Tính toán &    | Data Center /  | Nơi đặt hạ     | Server         |
| lưu trữ        | Cloud / Hybrid | tầng vật lý    | on-premise,    |
|                |                | hoặc thuê hạ   | AWS/Azure/GCP, |
|                |                | tầng ảo hóa    | mô hình lai    |
|                |                | trên nền tảng  | (hybrid cloud) |
|                |                | đám mây, hoặc  |                |
|                |                | kết hợp cả hai |                |
|                +----------------+----------------+----------------+
|                | Compute        | Cung cấp năng  | CPU, GPU, ,máy |
|                |                | lực xử lý để   | chủ ảo (VM),   |
|                |                | chạy ứng dụng  | container chạy |
|                |                | và xử lý dữ    | ứng dụng web   |
|                |                | liệu           |                |
|                +----------------+----------------+----------------+
|                | Storage        | Lưu trữ dữ     | Ổ cứng         |
|                |                | liệu có cấu    | SAN/NAS,       |
|                |                | trúc và phi    | Object Storage |
|                |                | cấu trúc       | (S3, Blob)     |
+----------------+----------------+----------------+----------------+
| Kết nối        | Network        | Hạ tầng mạng   | LAN, WAN,      |
|                |                | nội bộ và liên | switch, router |
|                |                | kết giữa các   |                |
|                |                | hệ thống       |                |
|                +----------------+----------------+----------------+
|                | SD-WAN         | Mạng diện rộng | Kết nối nhiều  |
|                |                | được định      | chi nhánh về   |
|                |                | nghĩa bằng     | trung tâm dữ   |
|                |                | phần mềm, tối  | liệu/cloud     |
|                |                | ưu định tuyến  |                |
|                |                | lưu lượng      |                |
|                +----------------+----------------+----------------+
|                | VPN            | Kết nối riêng  | Nhân viên làm  |
|                |                | ảo, mã hóa     | việc từ xa     |
|                |                | đường truyền   | truy cập hệ    |
|                |                | qua mạng công  | thống nội bộ   |
|                |                | cộng           |                |
+----------------+----------------+----------------+----------------+

1.2/Data center(Trung tâm dữ liệu)

-Khái niệm: Là nơi đặt các máy chủ (server), thiết bị lưu trữ dữ liệu và
thiết bị mạng để lưu trữ, xử lý và cung cấp dữ liệu, ứng dụng cho người
dùng và doanh nghiệp

-Nguồn tham khảo: [[Trung tâm dữ liệu -- Wikipedia tiếng
Việt]{.underline}](https://vi.wikipedia.org/wiki/Trung_t%C3%A2m_d%E1%BB%AF_li%E1%BB%87u#cite_note-5)

1.3/Cloud computing(Điện toán đám mây)

-Khái niệm: Là mô hình cung cấp các tài nguyên CNTT như máy chủ, lưu
trữ, cơ sở dữ liệu, mạng và phần mềm thông qua Internet. Người dùng có
thể sử dụng các tài nguyên này theo nhu cầu mà không cần tự đầu tư hoặc
quản lý hạ tầng vật lý.\
-Nguồn tham khảo: [[Điện toán đám mây -- Wikipedia tiếng
Việt]{.underline}](https://vi.wikipedia.org/wiki/%C4%90i%E1%BB%87n_to%C3%A1n_%C4%91%C3%A1m_m%C3%A2y)

1.4/Hybrid cloud(đám mây lai)

-Khái niệm: Là mô hình sử dụng đồng thời hạ tầng nội bộ của doanh nghiệp
và dịch vụ Cloud, cho phép doanh nghiệp linh hoạt lựa chọn nơi lưu trữ
dữ liệu và triển khai ứng dụng.

-Nguồn tham khảo: [[Cloud computing -
Wikipedia]{.underline}](https://en.wikipedia.org/wiki/Cloud_computing#Hybrid),
[[Hybrid cloud storage -
Wikipedia]{.underline}](https://en.wikipedia.org/wiki/Hybrid_cloud_storage)

1.5/Compute(Tài nguyên tính toán)

-Khái niệm: Là các tài nguyên phần cứng hoặc máy ảo cung cấp năng lực xử
lý cho hệ thống, giúp chạy các ứng dụng, dịch vụ và xử lý dữ liệu.

-Nguồn tham khảo: [[Máy ảo trong Azure - Azure Virtual Machines \|
Microsoft
Learn]{.underline}](https://learn.microsoft.com/en-us/azure/virtual-machines/)

1.6/Storage

-Khái niệm: Là các phương thức và thiết bị dùng để lưu trữ dữ liệu số.

Nguồn tham khảo: [[Computer data storage -
Wikipedia]{.underline}](https://en.wikipedia.org/wiki/Computer_data_storage)

1.7/Network

\- Khái niệm: Là hệ thống kết nối các thiết bị để trao đổi dữ liệu với
nhau.

\- Nguồn tham khảo: [[Computer network -
Wikipedia]{.underline}](https://en.wikipedia.org/wiki/Computer_network)

1.8/SD-WAN

\- Khái niệm: Là mạng diện rộng được điều khiển và định tuyến thông minh
bằng phần mềm tập trung.

\- Nguồn tham khảo: [[SD-WAN -
Wikipedia]{.underline}](https://en.wikipedia.org/wiki/SD-WAN)

1.9/VPN

\- Khái niệm: Là công nghệ tạo đường truyền riêng, được mã hóa qua hạ
tầng mạng công cộng.

\- Nguồn tham khảo: [[Virtual private network -
Wikipedia]{.underline}](https://en.wikipedia.org/wiki/Virtual_private_network)
