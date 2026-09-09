1 khái niệm

**Compute & Connectivity** là tập hợp các thành phần tài nguyên vật lý
(hoặc tài nguyên ảo hóa tương đương trên đám mây) cùng hệ điều hành/mạng
cơ bản, cung cấp năng lực **xử lý dữ liệu (Compute)**, **lưu trữ
(Storage)** và **truyền tải dữ liệu (Connectivity)** giữa các hệ thống.

- **Về phía Compute:** Bao gồm máy chủ (Server), máy trạm/thiết bị đầu
  cuối (Endpoint), hệ thống lưu trữ (SAN/NAS/Object Storage), cùng hệ
  điều hành nền (Linux/Windows Server) và trình quản lý ảo hóa
  (Hypervisor).

- **Về phía Connectivity:** Bao gồm hạ tầng mạng vật lý/ảo hóa (Switch,
  Router, Firewall, VPC/VNET), các dịch vụ định danh & định tuyến cơ bản
  (DNS, Load Balancer, VPN, SD-WAN) nhằm kết nối các tiến trình tính
  toán với nhau và tới người dùng cuối.

2 vai trò

Mặc dù không trực tiếp cung cấp logic nghiệp vụ cho người dùng cuối,
Compute & Connectivity đóng giữ các vai trò sống còn trong kiến trúc IT:

- **Trụ cột vận hành (Infrastructure Foundation):** Là \"mặt đất\" để
  dựng nên toàn bộ hệ thống. Nếu lớp (1) không ổn định hoặc gặp sự cố,
  tất cả các lớp phía trên (API, Database, IAM, App) đều dừng hoạt động.

- **Đảm bảo hiệu năng & khả năng mở rộng (Performance & Scalability):**
  Định hình giới hạn chịu tải, tốc độ xử lý I/O và băng thông mạng. Lớp
  này quyết định khả năng mở rộng ngang (Horizontal Scaling) hoặc mở
  rộng dọc (Vertical Scaling) của toàn bộ hệ thống.

- **Tạo dựng ranh giới an toàn ban đầu (Infrastructure Security
  Baseline):** Thực hiện phân vùng mạng (Network Segmentation), gia cố
  thiết bị (Hardening), cấu hình TLS/VPN và Patching cấp độ Firmware/OS
  để bảo vệ tài nguyên ngay từ cấp độ phần cứng và đường truyền.

- **Tối ưu hóa chi phí phần cứng (TCO & Capacity Baseline):** Giúp doanh
  nghiệp định lượng được mức độ tiêu thụ tài nguyên (CPU, RAM, Disk,
  Bandwidth), từ đó lập kế hoạch năng lực (Capacity Planning) và tối ưu
  hóa chi phí đầu tư hạ tầng (CapEx/OpEx).

3 đặc điểm kĩ thuật

- 

4 các mô hình triển khai

> · **On-premise:** Doanh nghiệp tự đầu tư, sở hữu và vận hành phần cứng
> tại Trung tâm dữ liệu (Data Center) riêng.
>
> · **Cloud:** Thuê tài nguyên tính toán, lưu trữ và mạng từ các nhà
> cung cấp đám mây (AWS, Azure, GCP\...) theo mô hình trả tiền theo nhu
> cầu. Theo chuẩn hóa của **NIST (Viện Tiêu chuẩn và Công nghệ Hoa
> Kỳ)**, điện toán đám mây là mô hình cho phép truy cập mạng thuận tiện,
> theo yêu cầu, tới một tập hợp tài nguyên tính toán có thể cấu hình
> (mạng, máy chủ, lưu trữ, ứng dụng) và có thể cấp phát/thu hồi nhanh
> chóng.
>
> · **Hybrid:** Mô hình kết hợp linh hoạt giữa On-premise và Cloud.
