**BÁO CÁO GIAI ĐOẠN 2 LẬP KẾ HOẠCH TRIỂN KHAI HẠ TẦNG CNTT WAYS STATION**

*“**Nâng cấp và chuyển đổi hạ tầng** CNTT sang **mô hình** Hybrid Cloud **nhằm tối ưu vận hành và mở rộng chuỗi không gian làm việc thông minh** WAYS STATION”*

| **Thông tin** | **Nội dung** |
| --- | --- |
| Đơn vị chủ quản | Công ty Cổ phần Công nghệ & Không gian làm việc WAYS STATION |
| Giai đoạn | Giai đoạn 2 – Lập kế hoạch triển khai hạ tầng CNTT |
| Thời gian dự kiến | 06 tháng – 10/2026 đến 03/2027 |
| Mô hình đề xuất | Hybrid Cloud |

# 1. TỔNG QUAN GIAI ĐOẠN 2

Giai đoạn 2 được xây dựng trên cơ sở khảo sát hiện trạng AS-IS, các vấn đề, mục tiêu KPI và phương án kiến trúc TO-BE đã xác định ở Giai đoạn 1. Trọng tâm của giai đoạn này là chuyển phương án Hybrid Cloud thành kế hoạch triển khai cụ thể, có yêu cầu kỹ thuật, danh mục đầu tư, chi phí, tiến độ, nhân sự và tiêu chí nghiệm thu.

Theo Giai đoạn 1, WAYS STATION hiện có 3 chi nhánh, mỗi chi nhánh phục vụ trung bình 150–200 khách hàng/ngày và 30 nhân viên vận hành. Hạ tầng hiện tại gồm Mini Server/NAS, Wi-Fi 5, 2 đường FTTH và các hệ thống Smart Lock, POS/Billing, CCTV. Hạ tầng có tình trạng quá tải và thiếu cơ chế dự phòng, giám sát, bảo mật và sao lưu tập trung.

# 2. BƯỚC 5 – CHUẨN HÓA YÊU CẦU KỸ THUẬT

## 2.1. Cơ sở xác định yêu cầu

- CPU/RAM tại chi nhánh có thể đạt 85–95% vào giờ cao điểm.

- Wi-Fi 5 có nguy cơ quá tải khi trên 80 khách hàng sử dụng đồng thời.

- Core Switch tồn tại điểm lỗi đơn lẻ (SPOF).

- Chưa có hệ thống Monitoring/Observability tập trung.

- Backup hiện thực hiện thủ công, RPO hiện tại 7 ngày và RTO 24–48 giờ.

- Chưa có IAM/SSO/MFA tập trung và chưa triển khai EDR.

- Dữ liệu đang phân tán tại SaaS POS, Smart Lock Controller local và NAS local.

## 2.2. KPI mục tiêu TO-BE

| **Tiêu chí** | **AS-IS** | **TO-BE** |
| --- | --- | --- |
| Uptime | 97,5% | ≥ 99,9% |
| RPO / RTO | 7 ngày / 24–48 giờ | RPO ≤ 1 giờ / RTO ≤ 2 giờ |
| Wi-Fi | 30–40 users/AP | ≥ 100 users/AP |
| Latency | > 120 ms | < 20 ms |
| EDR | 0% | 100% Endpoint |
| MFA | Chưa triển khai tập trung | 100% Admin |
| MTTD / MTTR | 45 phút / 4 giờ | < 15 phút / < 2 giờ |

## Định hướng trình bày: toàn bộ yêu cầu và giải pháp dưới đây được quy về bài toán vận hành, mở rộng và bảo vệ hạ tầng của WAYS STATION.

## 2.3. Yêu cầu nghiệp vụ

| **Mã** | **Yêu cầu nghiệp vụ** | **Mức độ** |
| --- | --- | --- |
| BR-01 | Khách hàng có thể đặt chỗ và thanh toán ổn định qua App/Web. | Cao |
| BR-02 | Hệ thống Smart Lock phải hoạt động liên tục. | Rất cao |
| BR-03 | Nhân viên sử dụng POS/Billing ổn định. | Rất cao |
| BR-04 | Khách hàng truy cập Wi-Fi tốc độ cao tại chi nhánh. | Cao |
| BR-05 | CCTV tiếp tục ghi nhận hình ảnh và log. | Cao |
| BR-06 | Quản trị viên giám sát tập trung các chi nhánh. | Cao |
| BR-07 | Có khả năng khôi phục dữ liệu khi xảy ra sự cố. | Rất cao |
| BR-08 | Có thể triển khai nhanh hạ tầng cho chi nhánh mới. | Cao |
| BR-09 | Dữ liệu khách hàng và giao dịch được bảo vệ. | Rất cao |
| BR-10 | Hệ thống có khả năng mở rộng từ 3 lên 8 chi nhánh. | Rất cao |

## 2.4. Yêu cầu hệ thống

Network: sử dụng 2 đường FTTH độc lập tại mỗi chi nhánh; SD-WAN Router; Firewall/UTM; VLAN phân tách Staff, Guest, POS, Smart Lock, CCTV và Management; Wi-Fi 6; quản lý AP tập trung.

Cloud: triển khai Core Application và Database trên AWS/Azure; sử dụng khả năng Auto Scaling, Backup và Disaster Recovery; thiết kế để mở rộng khi số lượng chi nhánh tăng.

Security: Central IAM, SSO, MFA cho tài khoản quản trị, EDR trên Endpoint, phân quyền theo vai trò, cập nhật bảo mật tập trung, Firewall và Network Segmentation.

Monitoring: giám sát CPU, RAM, Storage, Bandwidth, Packet Loss, Latency, Wi-Fi AP, Server, Database, Application, SD-WAN, Firewall và ISP.

# 3. BƯỚC 6 – THIẾT KẾ GIẢI PHÁP TO-BE VÀ BOM/BOQ

## 3.1. Kiến trúc tổng thể

Kiến trúc đề xuất sử dụng mô hình Hybrid Cloud. Tại mỗi chi nhánh, các thiết bị Edge, SD-WAN, Firewall, Switch và Wi-Fi 6 tạo lớp kết nối và bảo vệ; các hệ thống Core App, Database, API Gateway, IAM/SSO/MFA, EDR và Monitoring được quản lý tập trung trên nền tảng Cloud.

Luồng tổng quát: Internet/2 ISP → SD-WAN Router → Firewall → Core/Distribution Switch → Wi-Fi 6/POS/Smart Lock/CCTV → kết nối SD-WAN/VPN → AWS/Azure Cloud → Core App/Database/API Gateway/IAM/Monitoring.

## 3.2. Thiết kế theo 5 lớp

| **Lớp** | **Thành phần chính** |
| --- | --- |
| Lớp 1 – Compute & Connectivity | Cloud Compute, Managed Database, SD-WAN, Wi-Fi 6, Switch, Firewall, Dual-ISP |
| Lớp 2 – Platform & Operations | Monitoring, Central Logging, Backup, Disaster Recovery, Alerting |
| Lớp 3 – Security & Identity | IAM, SSO, MFA, EDR, Firewall, Network Segmentation |
| Lớp 4 – Application & Integration | WAYS STATION App, POS, Smart Lock, API Gateway, Cloud Integration |
| Lớp 5 – Data | Cloud Database, Cloud Storage, Backup Storage, Encryption, Data Classification |

## 3.3. BOM/BoQ thiết bị tại chi nhánh

| **STT** | **Hạng mục** | **SL** | **Đơn giá dự toán** | **Thành tiền** |
| --- | --- | --- | --- | --- |
| 1 | SD-WAN Router | 5 | 2khoảng 5 triệu | 12khoảng 5 triệu |
| 2 | Firewall/UTM | 5 | khoảng 20 triệu | 100 triệu |
| 3 | Wi-Fi 6 AP | 25 | khoảng 5 triệu | 12khoảng 5 triệu |
| 4 | Managed Switch | 10 | 1khoảng 5 triệu | 1khoảng 50 triệu |
| 5 | UPS | 5 | khoảng 8 triệu | 40 triệu |
| 6 | Rack + phụ kiện | 5 | khoảng 5 triệu | 2khoảng 5 triệu |
| 7 | Thiết bị/Module mạng dự phòng | 1 gói | 2khoảng 5 triệu | 2khoảng 5 triệu |

Tạm tính thiết bị: khoảng 590 triệu VNĐ.

## 3.4. BOM/BoQ Cloud và phần mềm

| **STT** | **Hạng mục** | **Dự toán năm đầu** |
| --- | --- | --- |
| 1 | Cloud Compute | khoảng 60 triệu |
| 2 | Managed Database | khoảng 50 triệu |
| 3 | Cloud Storage/Backup | khoảng 30 triệu |
| 4 | API Gateway và dịch vụ liên quan | khoảng 20 triệu |
| 5 | IAM/SSO/MFA | 2khoảng 5 triệu |
| 6 | EDR | khoảng 30 triệu |
| 7 | Monitoring/Logging | 2khoảng 5 triệu |

Tạm tính Cloud + License năm đầu: khoảng 240 triệu VNĐ.

## 3.5. Dịch vụ triển khai

| **Hạng mục** | **Chi phí dự kiến** |
| --- | --- |
| Khảo sát & thiết kế chi tiết | 1khoảng 5 triệu |
| Cấu hình Network/SD-WAN | 1khoảng 5 triệu |
| Cấu hình Cloud | khoảng 20 triệu |
| Migration dữ liệu | 1khoảng 5 triệu |
| Security configuration | khoảng 10 triệu |
| Testing & Go-live | khoảng 10 triệu |

Tạm tính dịch vụ: khoảng 85 triệu VNĐ.

# 4. BƯỚC 7 – DỰ TOÁN CHI PHÍ & PHÂN TÍCH CAPEX/OPEX/TCO

## 4.1. Tổng hợp dự toán

| **Khoản mục** | **Dự toán** |
| --- | --- |
| Thiết bị Edge/Network | ≈ 590 triệu VNĐ |
| Cloud + License năm đầu | ≈ 240 triệu VNĐ |
| Dịch vụ triển khai | ≈ 8khoảng 5 triệu VNĐ |
| Tổng theo BoQ minh họa | ≈ 91khoảng 5 triệu VNĐ |
| Ngân sách mục tiêu theo Giai đoạn 1 | ≈ 8khoảng 50 triệu VNĐ |

Các đơn giá trong bảng là dự toán phục vụ bài tập, chưa phải báo giá chính thức. Để bám ngân sách khoảng 850 triệu VNĐ của Giai đoạn 1, cần tối ưu BoQ, đàm phán license, mua thiết bị theo gói và ưu tiên các hạng mục thiết yếu.

## 4.2. CAPEX

CAPEX là các khoản đầu tư ban đầu như SD-WAN Router, Firewall, Wi-Fi 6 AP, Managed Switch, UPS, Rack và phụ kiện mạng. CAPEX dự kiến khoảng 500–600 triệu VNĐ tùy cấu hình và báo giá thực tế.

## 4.3. OPEX

OPEX gồm Cloud Compute, Database, Storage, Backup, Monitoring, EDR, IAM/SSO, Internet, License và hỗ trợ kỹ thuật. Giai đoạn 1 đặt mức OPEX Cloud khoảng 30–40 triệu VNĐ/tháng.

## 4.4. TCO minh họa 3 năm

| **Khoản mục** | **Năm 1** | **Năm 2** | **Năm 3** |
| --- | --- | --- | --- |
| CAPEX | 5khoảng 50 triệu | 0 | 0 |
| Cloud/License | 300 triệu | 4khoảng 20 triệu | 4khoảng 20 triệu |
| Bảo trì/vận hành | khoảng 30 triệu | 40 triệu | 40 triệu |
| Tổng | 880 triệu | 4khoảng 60 triệu | 4khoảng 60 triệu |

TCO minh họa 3 năm ≈ 1,8 tỷ VNĐ. Đây là mô hình tính phục vụ bài tập; khi đầu tư thực tế cần thay bằng báo giá và hợp đồng dịch vụ chính thức.

# 5. BƯỚC 8 – KẾ HOẠCH TRIỂN KHAI THEO GIAI ĐOẠN

## 5.1. WBS

- Khởi động dự án: thành lập đội dự án, xác định phạm vi, phê duyệt kế hoạch và phân công trách nhiệm.

- Khảo sát & thiết kế: khảo sát Network, Wi-Fi, Server/NAS, Smart Lock/POS/CCTV; thiết kế Network, Cloud và Security.

- Mua sắm: lập BoQ, lấy báo giá, so sánh nhà cung cấp, phê duyệt và đặt hàng.

- Triển khai: lắp đặt Network, SD-WAN, Wi-Fi 6, Firewall, Cloud, IAM/SSO/MFA, EDR và Monitoring.

- Migration: backup NAS, chuyển dữ liệu lên Cloud Storage, cấu hình Database, kiểm tra và đồng bộ.

- Testing: Load Test, Failover Test, Security Test, Backup/Restore Test và DR Test.

- Go-live: chuyển đổi hệ thống, theo dõi, xử lý lỗi và nghiệm thu.

## 5.2. Roadmap 6 tháng

| **Thời gian** | **Công việc chính** |
| --- | --- |
| 10/2026 | Khởi động + khảo sát + thiết kế chi tiết |
| 11/2026 | Hoàn thiện BoQ + mua sắm thiết bị |
| 12/2026 | Triển khai Cloud + Network Core |
| 01/2027 | Triển khai SD-WAN + Wi-Fi 6 tại chi nhánh |
| 02/2027 | Migration + Security + Monitoring + Testing |
| 03/2027 | Go-live + nghiệm thu + bàn giao |

## 5.3. Nguyên tắc chuyển đổi

Công tác thi công và cắt chuyển mạng tại chi nhánh chỉ thực hiện trong ca đêm 22:00–06:00. Quy trình chuyển đổi: Backup → Chuẩn bị → Cấu hình → Cut-over → Kiểm tra → Rollback nếu lỗi → Go-live. Không thực hiện chuyển đổi khi chưa có phương án rollback.

# 6. NHÂN SỰ, TỔ CHỨC VÀ CƠ CHẾ PHỐI HỢP

| **Vai trò** | **Trách nhiệm** |
| --- | --- |
| Project Sponsor | Phê duyệt ngân sách và định hướng |
| Project Manager | Quản lý tổng thể dự án |
| Network Engineer | Network, SD-WAN, Wi-Fi, Switch |
| Cloud Engineer | Cloud, Database, Backup |
| Security Engineer | Firewall, IAM, MFA, EDR |
| System Engineer | Server, Migration, Monitoring |
| IT Support | Hỗ trợ người dùng và chi nhánh |
| Vendor | Cung cấp thiết bị, license và hỗ trợ kỹ thuật |
| Đại diện chi nhánh | Phối hợp lịch thi công và kiểm thử |

## 6.1. Cơ chế phối hợp

- Hàng ngày: kiểm tra tiến độ, vấn đề phát sinh và trạng thái triển khai.

- Hàng tuần: họp Project Manager và các nhóm kỹ thuật; báo cáo tiến độ, rủi ro và ngân sách.

- Sự cố nghiêm trọng: IT Support → Team Leader → Project Manager → Technical Lead/Vendor.

# 7. QUẢN TRỊ RỦI RO

| **Rủi ro** | **Khả năng** | **Ảnh hưởng** | **Phương án xử lý** |
| --- | --- | --- | --- |
| ISP mất kết nối | TB | Cao | Dual ISP + SD-WAN Failover |
| Thiết bị lỗi | TB | Cao | Thiết bị dự phòng + bảo hành |
| Migration lỗi | TB | Rất cao | Backup + rollback |
| Cloud downtime | Thấp | Cao | Multi-AZ + Backup |
| Cấu hình Firewall sai | TB | Cao | Review + test trước Go-live |
| Mất dữ liệu | Thấp | Rất cao | Backup + DR |
| Nhân viên chưa quen hệ thống | TB | TB | Training + tài liệu hướng dẫn |
| Trễ thiết bị | TB | Cao | Đặt hàng sớm + nhà cung cấp thay thế |
| Vượt ngân sách | TB | Cao | Kiểm soát BoQ + Change Request |
| Không đạt hiệu năng Wi-Fi | TB | Cao | Wi-Fi survey + Load Test |

# 8. KẾ HOẠCH KIỂM THỬ

| **Loại kiểm thử** | **Cách thực hiện** | **Tiêu chí** |
| --- | --- | --- |
| Load Test | Kiểm thử hệ thống ở 150% tải dự kiến | Không lỗi nghiêm trọng, đạt hiệu năng |
| Failover Test | Ngắt ISP 1 và kiểm tra chuyển sang ISP 2 | Dịch vụ tiếp tục hoạt động |
| Backup/Restore | Backup → giả lập lỗi → Restore | RPO ≤ 1 giờ, RTO ≤ 2 giờ |
| Security Test | Kiểm tra Firewall, IAM, MFA, EDR | Đạt yêu cầu bảo mật |
| DR Test | Giả lập sự cố và khôi phục dịch vụ | Khôi phục trong RTO mục tiêu |

# 9. TIÊU CHÍ NGHIỆM THU

| **Tiêu chí** | **Mục tiêu** |
| --- | --- |
| Uptime | ≥ 99,9% |
| RPO | ≤ 1 giờ |
| RTO | ≤ 2 giờ |
| Wi-Fi | ≥ 100 users/AP |
| Latency | < 20 ms |
| EDR | 100% Endpoint |
| MFA | 100% Admin |
| MTTD | < 15 phút |
| MTTR | < 2 giờ |
| Load Test | Đạt 150% tải |
| Failover | Đạt |
| Backup/Restore | Đạt |
| Go-live | Không xảy ra unplanned downtime nghiêm trọng |

# 10. KẾT LUẬN GIAI ĐOẠN 2

Giai đoạn 2 chuyển các mục tiêu và phương án đã xác định ở Giai đoạn 1 thành kế hoạch triển khai có thể thực hiện, bao gồm yêu cầu nghiệp vụ, yêu cầu kỹ thuật, kiến trúc TO-BE, danh mục thiết bị, dự toán CAPEX/OPEX, TCO, WBS, Roadmap, nhân sự và phương án quản trị rủi ro.

Giải pháp Hybrid Cloud kết hợp SD-WAN, Wi-Fi 6, Cloud Database, Central IAM/SSO/MFA, EDR và Monitoring phù hợp với định hướng mở rộng của WAYS STATION. Kiến trúc được thiết kế để vừa giải quyết tình trạng quá tải hiện tại vừa tạo nền tảng mở rộng từ 3 lên 8 chi nhánh.

Mục tiêu cuối cùng của Giai đoạn 2 là tạo ra một kế hoạch đủ rõ để bước sang giai đoạn triển khai: xác định triển khai cái gì, ở đâu, cần thiết bị gì, ai thực hiện, thực hiện khi nào, chi phí bao nhiêu và nghiệm thu bằng tiêu chí nào.

# 11. GHI CHÚ ĐỒNG BỘ VỚI GIAI ĐOẠN 1

Giai đoạn 1 có hai cách gọi cho công cụ Monitoring: phần kiến trúc TO-BE đề cập Datadog, trong khi phần phạm vi thực hành đề cập Grafana Monitoring. Trong bản Giai đoạn 2 này, công cụ được ghi ở mức “Monitoring/Logging” để tránh tự ý thay đổi quyết định của Giai đoạn 1. Khi nộp bản chính thức, nên chốt một công cụ duy nhất để kiến trúc, BOM và chi phí thống nhất.

**Ghi chú về giá : **Các mức giá trong bảng chỉ nhằm minh họa quy mô ngân sách và nên hiểu là giá dự toán/khoảng giá, không phải báo giá chính thức. Giá thực tế có thể thay đổi theo model, cấu hình, số lượng, thời điểm, nhà cung cấp, thuế và chính sách chiết khấu. Khi triển khai thực tế sẽ lấy báo giá/quotation tại thời điểm mua.

Nguồn tham khảo cho phương án WAYS STATION: AWS Pricing Calculator và Microsoft Azure Pricing Calculator – dùng để tham khảo cách lập dự toán Cloud. Các KPI, BoQ, chi phí, tiến độ và tiêu chí nghiệm thu trong báo cáo là đề xuất phục vụ bài toán WAYS STATION, không phải báo giá hay yêu cầu bắt buộc của nhà cung cấp.

# LƯU Ý KHI TRÌNH BÀY – WAYS STATION

- Bài tập trung vào vấn đề thực tế của WAYS STATION: 3 chi nhánh, tải sử dụng tăng, thiếu dự phòng, giám sát, bảo mật và sao lưu tập trung.

- Hybrid Cloud, SD-WAN, Wi-Fi 6, IAM/SSO/MFA, EDR và Monitoring chỉ được trình bày như các thành phần của phương án WAYS STATION.

- KPI và chi phí là mục tiêu/ước tính của nhóm cho bài toán này; khi triển khai thực tế phải lấy báo giá và cấu hình thực tế.

- Nguồn tham khảo chỉ dùng để chứng minh cách tính chi phí Cloud và làm cơ sở kỹ thuật khi cần; không trình bày lan man về nhà cung cấp.

| Nội dung WAYS STATION | Nguồn tham khảo |
| --- | --- |
| Phần Hybrid Cloud / kiến trúc TO-BE | [1], [2], [3] |
| Phần Backup, DR, Failover, RPO/RTO | [1], [3] |
| Phần IAM, MFA, Security, EDR | [1], [3] |
| Phần Monitoring / Operational Excellence | [2], [3] |
| Phần dự toán Cloud | [4], [5] |

**TÀI LIỆU THAM KHẢO**

*Nguồn có thể tra cứu trực tiếp cho bài toán hạ tầng** CNTT WAYS STATION*

**[1] WAYS STATION – Website chính thức Mục đích : **Đối chiếu thông tin nhận diện, dịch vụ và hệ sinh thái WAYS STATION.

**Link tra cứu : [2] WAYS STATION – Danh sách địa chỉ và bảng giá Mục đích : **Đối chiếu hệ thống chi nhánh và thông tin hoạt động được công bố.

**Link tra cứu : [3] MaSoThue – Tra cứu hộ kinh doanh WAYS STATION Mục đích : **Tra cứu thông tin mã số thuế/địa chỉ thuế của đơn vị WAYS STATION cụ thể; cần ghi rõ chi nhánh/đơn vị khi trích dẫn.

**Link tra cứu : [4] Bizfly Cloud – Bảng giá dịch vụ Mục đích : **Tham khảo giá Cloud Server/VPS/Storage để lập dự toán Cloud tại Việt Nam; bảng giá của nhà cung cấp ghi rõ chưa bao gồm VAT.

**Link tra cứu : [5] Bizfly Cloud – Cloud VPS Mục đích : **Tham khảo cấu hình CPU, RAM, SSD và đơn giá VPS theo tháng.

**Link tra cứu : [6] Bizfly Cloud – Simple Storage Mục đích : **Tham khảo chi phí lưu trữ, truyền dữ liệu và phương án Cloud Storage/Backup.

**Link tra cứu : [7] Chính phủ Việt Nam – Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân Mục đích : **Cơ sở pháp lý tham khảo khi bài đề cập bảo vệ dữ liệu khách hàng, kiểm soát truy cập và an toàn dữ liệu.

**Link tra cứu : [8] Vietcombank – Tỷ giá ngoại tệ Mục đích : **Tham khảo tỷ giá khi cần quy đổi chi phí dịch vụ quốc tế từ USD sang VND; tỷ giá phụ thuộc thời điểm tra cứu.

**Link tra cứu : [9] Microsoft Learn – Azure Well-Architected Framework Mục đích : **Tham khảo Reliability, Security, Cost Optimization, Operational Excellence và Performance Efficiency cho kiến trúc Cloud.

**Link tra cứu : [10] Microsoft Learn – Azure Well-Architected Reliability Mục đích : **Tham khảo dự phòng, phục hồi, monitoring, reliability targets và kiểm thử khôi phục.

**Link tra cứu : [11] Microsoft Learn – Azure Well-Architected Security Mục đích : **Tham khảo bảo mật, kiểm soát truy cập, bảo vệ dữ liệu và Zero Trust.

**Link tra cứu : [12] Cisco – SD-WAN Configuration Guides Mục đích : **Tham khảo tài liệu kỹ thuật về SD-WAN và kết nối mạng WAN cho mô hình nhiều chi nhánh.

**Link tra cứu : **

# ĐỐI CHIẾU NGUỒN VỚI NỘI DUNG BÀI

| Nội dung trong bài WAYS STATION | Nguồn |
| --- | --- |
| Thông tin WAYS STATION, chi nhánh, dịch vụ | [1], [2], [3] |
| Chi phí Cloud/VPS/Storage | [4], [5], [6] |
| Bảo vệ dữ liệu khách hàng | [7] |
| Quy đổi chi phí quốc tế sang VND | [8] |
| Hybrid Cloud, Reliability, Backup/DR, Monitoring | [9], [10] |
| IAM/MFA, bảo mật và kiểm soát truy cập | [11] |
| SD-WAN và kết nối mạng chi nhánh | [12] |

