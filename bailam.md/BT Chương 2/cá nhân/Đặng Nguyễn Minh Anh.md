LỚP NĂNG LỰC (1): COMPUTE & CONNECTIVITY

*(Hạ tầng tính toán và kết nối)*

# **I. Khái niệm**

Compute & Connectivity là lớp năng lực nền tảng nhất trong 5 lớp năng
lực của kiến trúc hạ tầng CNTT doanh nghiệp. Đây là lớp cung cấp tài
nguyên tính toán thô (compute), khả năng lưu trữ (storage) và khả năng
kết nối (connectivity) --- những thành phần vật lý và nền tảng vận hành
cơ bản mà mọi lớp năng lực khác (Ops Platform, Security, App &
Integration, Data Platform) đều phải dựa vào để hoạt động.

Có thể hiểu đơn giản: nếu ví hạ tầng CNTT của một doanh nghiệp như một
thành phố, thì lớp Compute & Connectivity chính là nền đất, hệ thống
điện và mạng lưới đường xá của thành phố đó --- mọi công trình (ứng
dụng, dữ liệu, dịch vụ) đều phải được xây dựng trên nền tảng này.

Lớp này bao gồm hai mảng lớn:

> • **Compute (tính toán):** năng lực xử lý (CPU, RAM) và lưu trữ dữ
> liệu (storage) để chạy hệ điều hành, phần mềm ảo hóa và ứng dụng.
>
> • **Connectivity (kết nối):** khả năng các thiết bị, hệ thống nói
> chuyện được với nhau, cả trong nội bộ (LAN) lẫn giữa các địa điểm khác
> nhau (WAN, Internet, cloud).

Về mô hình triển khai, lớp năng lực này có thể được hiện thực theo ba
hướng: On-premise (doanh nghiệp tự đầu tư và sở hữu phần cứng tại trung
tâm dữ liệu riêng), Cloud (thuê tài nguyên compute/storage/network từ
nhà cung cấp dịch vụ đám mây theo mô hình trả tiền theo nhu cầu), hoặc
Hybrid (kết hợp cả hai). Theo định nghĩa chuẩn hóa của Viện Tiêu chuẩn
và Công nghệ Hoa Kỳ (NIST), điện toán đám mây là mô hình cho phép truy
cập mạng thuận tiện, theo yêu cầu, tới một tập hợp tài nguyên tính toán
có thể cấu hình (mạng, máy chủ, lưu trữ, ứng dụng) và có thể được cấp
phát/thu hồi nhanh chóng với sự can thiệp quản lý tối thiểu \[1\].

# **II. Vai trò**

Lớp Compute & Connectivity đóng 4 vai trò chính trong toàn bộ kiến trúc
hạ tầng CNTT:

## **1. Cung cấp năng lực xử lý nền tảng**

Đây là nơi mọi ứng dụng nghiệp vụ (ERP, CRM, phần mềm kế toán, website,
app di động\...) được chạy. Nếu lớp này yếu (thiếu CPU/RAM, ổ cứng
chậm), toàn bộ hệ thống phía trên sẽ bị nghẽn, chậm, dễ lỗi --- bất kể
phần mềm nghiệp vụ có được thiết kế tốt đến đâu.

## **2. Đảm bảo khả năng lưu trữ và truy xuất dữ liệu**

Thông qua các hệ thống storage (SAN/NAS), lớp này lưu trữ toàn bộ dữ
liệu vận hành của doanh nghiệp và cung cấp tốc độ truy xuất phù hợp với
nhu cầu sử dụng.

## **3. Kết nối các thành phần trong hệ thống với nhau**

Không có mạng, máy chủ và storage tồn tại độc lập, không thể phối hợp.
Mạng là \"hệ tuần hoàn\" giúp người dùng ↔ ứng dụng ↔ dữ liệu ↔ dịch vụ
bên ngoài giao tiếp được với nhau.

## **4. Là nền tảng để các lớp năng lực khác vận hành**

Lớp Ops Platform cần compute để chạy công cụ giám sát; lớp Security cần
hạ tầng để triển khai tường lửa, IAM; lớp App & Data Platform đều chạy
trên compute/storage của lớp (1). Nói cách khác, đây là lớp \"nền vật
lý\" mà tất cả các lớp còn lại đều phụ thuộc vào.

# **III. Đặc điểm kỹ thuật**

Theo khung tham chiếu 5 lớp năng lực, lớp Compute & Connectivity được mô
tả theo 5 khía cạnh: Phần cứng, Phần mềm, Mạng, Quản trị/Vận hành, và
Bảo mật.

## **3.1. Phần cứng (Hardware)**

> • **Máy chủ (Server) / PC:** thiết bị tính toán chính, chạy hệ điều
> hành và ứng dụng. Trong mô hình on-premise truyền thống, doanh nghiệp
> sở hữu và quản lý toàn bộ máy chủ vật lý đặt tại trung tâm dữ liệu
> (data center) của mình.
>
> • **Storage (SAN/NAS):** hệ thống lưu trữ dữ liệu chuyên dụng, tách
> biệt khỏi máy chủ để dễ mở rộng dung lượng mà không phải nâng cấp toàn
> bộ server.
>
> • **Thiết bị mạng:** switch, router, firewall --- kết nối các máy chủ,
> storage và người dùng với nhau.
>
> • **Thiết bị người dùng cuối (endpoint):** máy tính, laptop của nhân
> viên.
>
> • **Tương đương trên cloud:** thay vì sở hữu phần cứng vật lý, doanh
> nghiệp thuê \"compute/storage fabric\" --- hạ tầng phần cứng thực do
> nhà cung cấp cloud (AWS, Microsoft Azure, Google Cloud) sở hữu và vận
> hành, doanh nghiệp chỉ thuê dùng.

## **3.2. Phần mềm (Software)**

> • **Hệ điều hành nền (OS):** Linux, Windows Server --- lớp phần mềm
> đầu tiên chạy trực tiếp trên phần cứng.
>
> • **Ảo hóa (Hypervisor):** phần mềm cho phép nhiều máy ảo (VM) cùng
> chạy trên một máy chủ vật lý, giúp tối ưu hiệu suất sử dụng phần cứng.
> Có hai loại chính:
>
> • **-- Type 1 (bare-metal):** cài đặt trực tiếp lên phần cứng, không
> cần hệ điều hành trung gian, hiệu năng cao, dùng phổ biến trong doanh
> nghiệp và trung tâm dữ liệu. Ví dụ: VMware ESXi/vSphere, Microsoft
> Hyper-V, KVM \[2\]\[3\].
>
> • **-- Type 2 (hosted):** cài đặt trên một hệ điều hành có sẵn (như
> một ứng dụng thông thường), phù hợp cho máy trạm cá nhân, môi trường
> thử nghiệm. Ví dụ: VMware Workstation, Oracle VirtualBox \[3\].
>
> • **SDN/Storage software:** phần mềm định nghĩa mạng (Software-Defined
> Networking) và phần mềm quản trị lưu trữ, cho phép cấu hình
> mạng/storage linh hoạt bằng phần mềm thay vì phải can thiệp vật lý vào
> thiết bị.

## **3.3. Mạng (Network)**

> • **LAN/WAN/Internet:** kết nối nội bộ (LAN) và kết nối diện rộng giữa
> các chi nhánh hoặc ra Internet (WAN).
>
> • **VPC/VNet (trên cloud):** mạng riêng ảo --- mô phỏng một mạng LAN
> riêng biệt cho doanh nghiệp ngay trên hạ tầng chia sẻ của nhà cung cấp
> cloud.
>
> • **SD-WAN:** kiến trúc mạng diện rộng được điều khiển bằng phần mềm,
> cho phép doanh nghiệp kết hợp nhiều loại đường truyền (MPLS, băng
> thông rộng, 4G/5G) và tự động chọn đường truyền tối ưu dựa trên tình
> trạng thực tế của từng kết nối, thay vì phụ thuộc hoàn toàn vào một
> đường truyền cố định \[4\]\[5\]. Đây là điểm khác biệt so với mô hình
> mạng WAN truyền thống vốn phụ thuộc nhiều vào đường MPLS đắt tiền.
>
> • **VPN:** công nghệ tạo đường hầm kết nối bảo mật, mã hóa dữ liệu
> truyền qua Internet --- thường dùng để kết nối nhân viên làm việc từ
> xa hoặc kết nối giữa các chi nhánh mà không cần kéo đường truyền
> riêng.
>
> • **DNS, Load Balancer (LB):** DNS phân giải tên miền thành địa chỉ
> IP; LB cơ bản phân phối tải request đến nhiều máy chủ để tránh quá tải
> một điểm duy nhất.

## **3.4. Quản trị/Vận hành (Governance/Ops)**

> • **Chuẩn cấu hình:** quy định thống nhất về cách cấu hình máy chủ,
> mạng để dễ quản lý và giảm rủi ro cấu hình sai.
>
> • **Inventory/Asset management:** quản lý danh mục tài sản phần cứng
> --- biết chính xác đang có bao nhiêu server, thiết bị mạng, đang vận
> hành ra sao.
>
> • **Capacity baseline:** thiết lập ngưỡng năng lực cơ sở (CPU, RAM,
> dung lượng lưu trữ hiện có) làm căn cứ để lập kế hoạch mở rộng khi nhu
> cầu tăng.

## **3.5. Bảo mật (Security)**

> • **Hardening:** củng cố cấu hình hệ thống/thiết bị theo hướng an toàn
> hơn, loại bỏ dịch vụ/cổng không cần thiết.
>
> • **Segmentation nền:** phân đoạn mạng để giới hạn phạm vi ảnh hưởng
> nếu một phần hệ thống bị tấn công.
>
> • **Firewall baseline:** thiết lập tường lửa ở mức cơ bản để kiểm soát
> lưu lượng ra/vào.
>
> • **TLS/VPN:** mã hóa dữ liệu truyền tải để chống nghe lén, đánh cắp
> thông tin trên đường truyền.
>
> • **Firmware/patch nền:** cập nhật bản vá cho firmware của thiết bị
> phần cứng và hệ điều hành nền để vá các lỗ hổng bảo mật đã biết.

# **IV. Mối quan hệ với các mô hình triển khai**

Việc đầu tư lớp Compute & Connectivity có thể thực hiện theo 3 mô hình:

  ------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Mô hình**   **Đặc điểm với lớp Compute & Connectivity**
  On-premise    Doanh nghiệp tự mua, tự sở hữu server/storage/thiết bị mạng, đặt tại data center riêng. Kiểm soát cao, nhưng chi phí đầu tư ban đầu (CapEx) lớn, mở rộng chậm hơn vì phải mua thêm thiết bị.
  Cloud         Thuê compute/storage/network dưới dạng dịch vụ (thường là mô hình IaaS -- Infrastructure as a Service). Mở rộng nhanh, linh hoạt, trả tiền theo mức sử dụng, nhưng phụ thuộc vào nhà cung cấp và cần kiểm soát chi phí chặt chẽ để tránh phát sinh ngoài dự kiến.
  Hybrid        Kết hợp: một phần hạ tầng tính toán/kết nối quan trọng giữ tại chỗ (on-prem), phần còn lại (ví dụ backup, mở rộng theo mùa vụ) đẩy lên cloud, kết nối với nhau qua VPN/SD-WAN.
  ------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **V. Xu hướng công nghệ mới (mục bổ sung)**

> • Chuyển dịch từ IaaS truyền thống sang mô hình serverless/compute co
> giãn tự động: giảm gánh nặng quản lý hạ tầng, tài nguyên tự động co
> giãn theo tải thực tế.
>
> • SD-WAN kết hợp SASE (Secure Access Service Edge): xu hướng hội tụ
> giữa mạng diện rộng và bảo mật thành một nền tảng thống nhất, được dự
> báo sẽ trở thành lựa chọn chủ đạo khi doanh nghiệp mở rộng sử dụng
> cloud và làm việc từ xa \[6\].
>
> • Container hóa thay thế một phần vai trò của máy ảo truyền thống:
> giúp tận dụng tài nguyên compute hiệu quả hơn so với ảo hóa toàn bộ hệ
> điều hành.

# **VI. Tài liệu tham khảo**

\[1\] Mell, P. & Grance, T. (2011). *The NIST Definition of Cloud
Computing*, NIST Special Publication 800-145, National Institute of
Standards and Technology.
[[https://doi.org/10.6028/NIST.SP.800-145]{.underline}](https://doi.org/10.6028/NIST.SP.800-145)

\[2\] IBM. *What Are Hypervisors?* IBM Think.
[[https://www.ibm.com/think/topics/hypervisors]{.underline}](https://www.ibm.com/think/topics/hypervisors)

\[3\] AWS. *Type 1 vs Type 2 Hypervisors -- Difference Between
Hypervisor Types.*
[[https://aws.amazon.com/compare/the-difference-between-type-1-and-type-2-hypervisors/]{.underline}](https://aws.amazon.com/compare/the-difference-between-type-1-and-type-2-hypervisors/)

\[4\] Cisco. *What Is SD-WAN? Software-Defined WAN.*
[[https://www.cisco.com/site/us/en/learn/topics/networking/what-is-sd-wan.html]{.underline}](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-sd-wan.html)

\[5\] Wikipedia. *SD-WAN.*
[[https://en.wikipedia.org/wiki/SD-WAN]{.underline}](https://en.wikipedia.org/wiki/SD-WAN)

\[6\] Palo Alto Networks. *What Is SD-WAN? Software-Defined Wide Area
Network.*
[[https://www.paloaltonetworks.com/cyberpedia/what-is-sd-wan]{.underline}](https://www.paloaltonetworks.com/cyberpedia/what-is-sd-wan)

\[7\] NetApp. *What is block storage? / What is object storage?*
[[https://www.netapp.com/data-storage/what-is-block-storage/]{.underline}](https://www.netapp.com/data-storage/what-is-block-storage/)
