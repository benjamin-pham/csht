# NGHIÊN CỨU KIẾN TRÚC HẠ TẦNG CNTT

## LỚP NĂNG LỰC (4): APP & INTEGRATION PLATFORM

![](media/image1.png){width="7.097222222222222in"
height="3.125e-2in"}![](media/image1.png){width="7.086805555555555in"
height="0.9270833333333334in"}

## TỔNG QUAN VỀ APP & INTEGRATION PLATFORM![](media/image1.png){width="5.2083333333333336e-2in" height="0.28125in"}

### Khái niệm (Concept)

> **App & Integration Platform** (Nền tảng Ứng dụng & Tích hợp) là lớp
> năng lực trung gian then chốt trong hạ tầng CNTT doanh nghiệp hiện
> đại. Lớp này cung cấp môi trường thực thi (runtime environment), khả
> năng điều phối (orchestration), kết nối và truyền nhận dữ liệu đồng
> bộ/bất đồng bộ giữa các ứng dụng nghiệp vụ nội bộ (như Core Banking,
> ERP, CRM, Legacy systems) cũng như với các hệ thống sinh thái bên
> ngoài (Partner APIs, Cloud Services, Third-party SaaS).

### Vai trò chiến lược trong Doanh nghiệp (Strategic Role)

- **Xóa bỏ ốc đảo dữ liệu (Data Silos):** Cho phép các hệ thống ứng dụng
  riêng lẻ giao tiếp, liên thông và chia sẻ dữ liệu tự động theo thời
  gian thực.

- **Tăng tốc độ phát triển & Đổi mới (Agility & Innovation):** Cung cấp
  môi trường chuẩn hóa (Container/Kubernetes, Microservices, Serverless)
  giúp rút ngắn vòng đời phát triển phần mềm (SDLC) và ra mắt sản phẩm
  nhanh chóng.

- **Chuẩn hóa điểm truy cập & Quản lý lưu lượng:** Tối ưu hóa việc điều
  phối lưu lượng truy cập (Traffic flow), bảo vệ ứng dụng phía sau và
  mang lại trải nghiệm người dùng liền mạch.

- **Khả năng mở rộng linh hoạt (Scalability & Resilience):** Cho phép mở
  rộng độc lập từng vi dịch vụ (Microservice) theo chiều ngang
  (Horizontal Scaling) mà không làm gián đoạn toàn bộ hệ thống.

## BẢNG PHÂN TÍCH 5 TRỤ CỘT KỸ THUẬT![](media/image1.png){width="5.2083333333333336e-2in" height="0.28125in"}

> Dựa trên Khung tham chiếu hạ tầng CNTT doanh nghiệp (Slide 17), lớp
> năng lực App & Integration Platform bao gồm 5 trụ cột thành phần với
> các đặc điểm kỹ thuật cụ thể sau:

+-----------+------------------+--------------------------------------+
| > **LỚP   | > **THÀNH        | > **ĐẶC ĐIỂM KỸ THUẬT VÀ CHỨC NĂNG   |
| > NĂNG    | > PHẦN/CÔNG      | > CHÍNH**                            |
| > LỰC**   | > NGHỆ**         |                                      |
+-----------+------------------+--------------------------------------+
| > **Phần  | > Compute nền    | > Tận dụng và kế thừa năng lực tính  |
| > cứng    | > (kế thừa Lớp   | > toán (Compute fabric, Virtual      |
| > (HW)**  | > 1)             | > Machines, Cloud Instances) từ Lớp  |
|           |                  | > (1) Compute & Connectivity để cấp  |
|           |                  | > phát tài nguyên thực thi ứng dụng. |
+-----------+------------------+--------------------------------------+
| > **Phần  | - Middleware /   | - **Middleware/ESB:** Chuyển đổi dữ  |
| > mềm     |   ESB            |   liệu, tích hợp hệ thống cũ (Legacy |
| > (SW)**  |                  |   systems).                          |
|           | - API Gateway    |                                      |
|           |                  | - **API Gateway:** Điểm truy cập duy |
|           | - Microservices  |   nhất quản lý, định tuyến và giới   |
|           |   &              |   hạn tần suất (Rate Limiting).      |
|           |   Container/K8s  |                                      |
|           |                  | - **Container/K8s:** Đóng gói ứng    |
|           | - Service Mesh   |   dụng dạng Docker và                |
|           |   (tùy chọn)     |                                      |
+-----------+------------------+--------------------------------------+
|           |                  |                                      |
+-----------+------------------+--------------------------------------+

+----------------+------------------+--------------------------------------+
|                | - Message Queue  | > điều phối bằng Kubernetes.         |
|                |   / Event Bus    |                                      |
|                |                  | - **Service Mesh:** Quản lý giao     |
|                |                  |   tiếp nội bộ giữa các microservices |
|                |                  |   (e.g., Istio, Linkerd).            |
|                |                  |                                      |
|                |                  | - **Message Queue/Event Bus:** Xử lý |
|                |                  |   truyền tin bất đồng bộ (e.g.,      |
|                |                  |   Kafka, RabbitMQ).                  |
+----------------+------------------+--------------------------------------+
| > **Mạng       | - Ingress /      | - Kiểm soát và bảo vệ lưu lượng truy |
| > (Network)**  |   Egress         |   cập đi vào (Ingress) và đi ra      |
|                |                  |   (Egress).                          |
|                | - Routing nội bộ |                                      |
|                |                  | - Định tuyến nội bộ và tự động phát  |
|                | - Service        |   hiện dịch vụ (Service Discovery -  |
|                |   Discovery      |   e.g., CoreDNS).                    |
|                |                  |                                      |
|                | - Load Balancer  | - Cân bằng tải L4/L7 nhằm phân bổ    |
|                |   (LB)           |   đều lưu lượng.                     |
|                |                  |                                      |
|                | - API Traffic    | - Điều phối và kiểm soát băng thông  |
|                |   Control        |   API (Throttling, Traffic           |
|                |                  |   Shifting).                         |
+----------------+------------------+--------------------------------------+
| > **Quản trị   | - CI/CD &        | - Tự động hóa quy trình đóng gói,    |
| > (Ops/ Gov)** |   Versioning     |   kiểm thử và tích hợp/ triển khai   |
|                |                  |   liên tục (GitOps, Jenkins,         |
|                | - Release /      |   ArgoCD).                           |
|                |   Change Mgmt    |                                      |
|                |                  | - Quan sát ứng dụng toàn diện qua 3  |
|                | - SRE Practice   |   trụ cột: Metrics (Prometheus),     |
|                |                  |   Logs (ELK/Fluentd), Traces         |
|                | - App            |   (Jaeger/Zipkin).                   |
|                |   Observability  |                                      |
|                |                  | - Áp dụng thực hành SRE (Service     |
|                |                  |   Level Objectives, Error Budgets).  |
+----------------+------------------+--------------------------------------+
| > **Bảo mật    | - AuthN / AuthZ  | - Xác thực và phân quyền chuẩn hóa   |
| > (Security)** |   (OIDC / SAML)  |   (OpenID Connect, OAuth2, SAML      |
|                |                  |   2.0).                              |
|                | - Secrets        |                                      |
|                |   Management     | - Quản lý tập trung các chuỗi bí mật |
|                |                  |   và khóa mã hóa (HashiCorp Vault,   |
|                | - Runtime        |   AWS Secrets Manager).              |
|                |   Security       |                                      |
|                |                  | - Lọc và ngăn chặn các đợt tấn công  |
|                | - API Security / |   ứng dụng mạng (WAF).               |
|                |   WAF            |                                      |
|                |                  | - Quét lỗ hổng bảo mật của Container |
|                | - Image Scanning |   Images trước khi đưa lên môi       |
|                |                  |   trường sản xuất (Trivy, Clair).    |
+----------------+------------------+--------------------------------------+

## ĐẶC ĐIỂM KỸ THUẬT TIÊN TIẾN & TIÊU CHUẨN NGÀNH![](media/image1.png){width="5.2083333333333336e-2in" height="0.28125in"}

### Kiến trúc Hướng sự kiện (Event-Driven Architecture - EDA) & Microservices

> Hệ thống hiện đại chuyển dịch mạnh mẽ từ kiến trúc khối (Monolithic)
> sang Microservices kết hợp EDA. Việc giao tiếp bất đồng bộ qua Message
> Queue/Event Bus (Kafka, RabbitMQ) giúp giảm độ gắn kết (Loosely
> Coupled), tăng khả năng chịu lỗi và đảm bảo tính sẵn sàng cao khi một
> vài thành phần gặp sự cố.

### Quản lý Vòng đời API (Full Lifecycle API Management)

> Áp dụng nguyên tắc **API-First**. API Gateway không chỉ đóng vai trò
> định tuyến mà còn bảo vệ hệ thống bằng các cơ chế Rate Limiting, IP
> Filtering, OAuth2 Validation và mã hóa dữ liệu trên đường truyền
> (TLS/mTLS).

### Mô hình Vận hành Cloud-Native & Observability

> Sử dụng phương pháp luận **GitOps** để quản lý cấu hình và triển khai
> ứng dụng dưới dạng mã (IaC). Giám sát nâng cao (Observability) giúp
> đội ngũ vận hành phát hiện sớm sự bất thường (Anomaly Detection) và
> rút ngắn thời gian khắc phục sự cố (MTTR).

## TÀI LIỆU THAM KHẢO(OFFICIAL SOURCES)![](media/image1.png){width="5.2083333333333336e-2in" height="0.28125in"}

![](media/image1.png){width="7.086805555555555in"
height="2.7916666666666665in"}
