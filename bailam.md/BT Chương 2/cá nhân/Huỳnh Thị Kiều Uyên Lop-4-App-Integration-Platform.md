**LỚP NĂNG LỰC (4): APP & INTEGRATION PLATFORM**

*(Nền tảng ứng dụng & tích hợp)*

*Thuyết trình trong khung tham chiếu phổ biến 5 lớp năng lực hạ tầng
CNTT*

------------------------------------------------------------------------

**1. Khái niệm**

App & Integration Platform là lớp năng lực chịu trách nhiệm xây dựng,
triển khai, vận hành và kết nối các ứng dụng/dịch vụ phần mềm trong
doanh nghiệp --- từ ứng dụng nội bộ (backend, portal) đến các dịch vụ mở
ra bên ngoài qua API.

Đây là lớp \"trung gian\" nằm giữa:

- Bên dưới: lớp (1) Compute & Connectivity (hạ tầng máy chủ/mạng nền) và
  lớp (3) Security + Identity (định danh, chính sách bảo mật xuyên
  suốt);

- Bên trên: lớp (5) Data Platform (nơi dữ liệu được lưu trữ, xử lý).

Nói cách khác, đây là lớp giúp các thành phần phần mềm rời rạc
(microservices, hệ thống cũ, dịch vụ bên thứ ba) \"nói chuyện\" được với
nhau một cách có kiểm soát, có khả năng mở rộng và có thể vận hành ổn
định ở quy mô lớn.

Về mặt kỹ thuật, lớp này gắn liền với khái niệm container orchestration:
theo tài liệu chính thức của dự án Kubernetes (CNCF), đây là nền tảng mã
nguồn mở giúp tự động hoá việc triển khai, mở rộng quy mô và quản lý các
ứng dụng đóng gói dưới dạng container --- chính là \"bộ khung vận hành\"
cho các microservices trong lớp App & Integration Platform.

**2. Vai trò trong khung tham chiếu tổng thể**

  ------------------------------------------------------------------
  **Vai trò**        **Diễn giải**
  ------------------ -----------------------------------------------
  Cầu nối tích hợp   Kết nối các hệ thống nội bộ (ERP, CRM, hệ thống
                     legacy) với nhau và với đối tác/bên thứ ba
                     thông qua API, message queue, event bus ---
                     thay vì kết nối điểm-điểm (point-to-point) gây
                     rối và khó bảo trì.

  Nền tảng phát      Cung cấp môi trường chuẩn hoá (container, K8s)
  triển & vận hành   để đội phát triển triển khai ứng dụng nhanh,
  ứng dụng           nhất quán, có thể mở rộng theo tải.

  Kiểm soát luồng    API Gateway đóng vai trò \"cửa ngõ\" duy nhất
  giao tiếp          kiểm soát ai được gọi API nào, giới hạn tốc độ
                     (rate limiting/throttling), định tuyến yêu cầu
                     tới đúng dịch vụ backend.

  Nền tảng cho       Là nơi áp dụng CI/CD, versioning, observability
  DevOps/SRE         --- biến việc phát hành phần mềm từ thủ công
                     thành quy trình tự động, lặp lại được.

  Điểm thực thi      Xác thực/phân quyền (AuthN/Z), bảo vệ API, quét
  chính sách bảo mật lỗ hổng image container --- là nơi các nguyên
  ứng dụng           tắc Zero Trust được áp dụng cụ thể ở tầng ứng
                     dụng.
  ------------------------------------------------------------------

**Vị trí trong chuỗi giá trị:** nếu lớp (1)-(2) là \"nền móng vận hành\"
và lớp (3) là \"lớp bao trùm an ninh\", thì lớp (4) chính là nơi giá trị
nghiệp vụ được hiện thực hoá thành phần mềm chạy được, trước khi dữ liệu
được đẩy xuống lớp (5) để lưu trữ và phân tích.

**3. Đặc điểm kỹ thuật theo 5 khía cạnh**

**3.1. Phần cứng (HW)**

- Về bản chất, lớp App & Integration Platform không có hạ tầng vật lý
  riêng mà \"tận dụng\" (kế thừa) lớp Compute nền (server/PC, cloud
  compute) từ lớp (1).

- Yêu cầu đặc thù: cấu hình compute cần hỗ trợ tốt container runtime
  (CPU, RAM linh hoạt theo tải), có thể co giãn theo chiều ngang
  (horizontal scaling) --- khác với ứng dụng nguyên khối (monolithic)
  chạy cố định trên một máy chủ.

**3.2. Phần mềm (SW) --- trọng tâm của lớp**

  ---------------------------------------------------------------------
  **Thành phần**  **Khái niệm**           **Vai trò kỹ thuật**
  --------------- ----------------------- -----------------------------
  Middleware /    Tầng phần mềm trung     Chuyển đổi định dạng dữ liệu,
  ESB (Enterprise gian giúp các ứng dụng  định tuyến thông điệp giữa hệ
  Service Bus)    khác nhau giao tiếp mà  thống cũ và mới
                  không cần biết chi tiết 
                  kỹ thuật của nhau       

  API Gateway     Điểm vào duy nhất quản  Theo tài liệu AWS, API
                  lý, giám sát và bảo mật Gateway là dịch vụ được quản
                  các lời gọi API         lý giúp nhà phát triển xuất
                                          bản, giám sát, bảo mật và vận
                                          hành API ở quy mô lớn; hỗ trợ
                                          định tuyến, xác thực
                                          (Cognito/IAM/Lambda
                                          authorizer), quản lý nhiều
                                          phiên bản/giai đoạn triển
                                          khai (dev/staging/prod), và
                                          giới hạn tốc độ để bảo vệ
                                          backend khỏi quá tải

  Microservices   Kiến trúc chia ứng dụng Cho phép phát triển, triển
                  lớn thành nhiều dịch vụ khai, mở rộng từng dịch vụ
                  nhỏ, độc lập, giao tiếp độc lập thay vì cả hệ thống
                  qua API                 nguyên khối

  Container /     Container đóng gói ứng  Theo Kubernetes.io, K8s tự
  Kubernetes      dụng + dependency thành động hoá việc triển khai, mở
  (K8s)           đơn vị chạy độc lập;    rộng và quản lý ứng dụng
                  K8s là nền tảng điều    container hoá; tổ chức
                  phối container          container thành các đơn vị
                                          logic (pod) để dễ quản lý và
                                          khám phá dịch vụ

  Service mesh    Lớp hạ tầng riêng quản  Cung cấp định tuyến thông
  (tuỳ chọn)      lý giao tiếp giữa các   minh, cân bằng tải, mã hoá
                  microservices (thường   giao tiếp nội bộ (mTLS), quan
                  qua sidecar proxy)      sát traffic giữa các service
                                          mà không cần sửa code ứng
                                          dụng

  Message queue / Cơ chế giao tiếp bất    Giảm phụ thuộc trực tiếp giữa
  Event bus       đồng bộ giữa các dịch   các service, tăng khả năng
                  vụ (Kafka,              chịu lỗi và mở rộng
                  RabbitMQ\...)           
  ---------------------------------------------------------------------

**3.3. Mạng (Network)**

- Ingress/Egress control: kiểm soát luồng traffic đi vào/đi ra hệ thống
  ứng dụng.

- Routing nội bộ & service discovery: các microservices cần cơ chế \"tự
  tìm nhau\" khi địa chỉ IP thay đổi liên tục (đặc biệt trong K8s, pod
  có thể được tạo/huỷ và đổi IP bất kỳ lúc nào).

- Load balancing (LB): phân phối tải giữa nhiều instance của cùng một
  service.

- API traffic control: giới hạn tốc độ, cắt giảm traffic bất thường, bảo
  vệ backend khỏi tấn công từ chối dịch vụ.

**3.4. Quản trị (Governance/Ops)**

- CI/CD (Continuous Integration/Continuous Deployment): tự động hoá
  build -- test -- triển khai, giảm rủi ro lỗi do thao tác thủ công.

- Release/Change management & Versioning API: quản lý phiên bản API (v1,
  v2\...) để không phá vỡ ứng dụng đang dùng phiên bản cũ khi nâng cấp.

- SRE practice (Site Reliability Engineering): áp dụng chỉ số đo lường
  độ tin cậy (SLO/SLA) cho từng dịch vụ.

- App observability: giám sát log, metric, trace ở mức ứng dụng để phát
  hiện sớm sự cố.

**3.5. Bảo mật (Security)**

- AuthN/Z (OIDC/SAML): xác thực và phân quyền truy cập ở mức API/dịch
  vụ.

- Secrets management: quản lý an toàn các thông tin nhạy cảm (mật khẩu,
  token, khoá API) mà ứng dụng cần dùng.

- Runtime security: giám sát và bảo vệ ứng dụng khi đang chạy (phát hiện
  hành vi bất thường trong container).

- API security/WAF: bảo vệ API khỏi các cuộc tấn công (SQL injection,
  broken access control\...).

- Image scanning: quét lỗ hổng bảo mật trong container image trước khi
  triển khai.

> *Liên hệ với nguyên tắc Zero Trust (NIST SP 800-207, SP 800-204, SP
> 800-228): NIST định nghĩa Zero Trust Architecture là tập hợp các
> nguyên tắc an ninh mạng không mặc định tin tưởng bất kỳ thực thể nào
> dựa trên vị trí mạng --- xác thực và phân quyền phải được thực hiện
> linh hoạt, nghiêm ngặt trước mỗi lần truy cập. Do các microservices
> giao tiếp lỏng lẻo (loosely coupled) và không còn khái niệm \"biên
> giới mạng\" rõ ràng, NIST SP 800-204 yêu cầu mỗi microservice phải
> được xác thực trước khi được tin tưởng, đồng thời chính sách bảo mật
> phải vừa được định nghĩa tập trung vừa được thực thi nhất quán ở mọi
> nơi. NIST SP 800-228 (2025) mở rộng nguyên tắc này riêng cho API, yêu
> cầu áp dụng kiểm soát ở toàn bộ vòng đời API (thiết kế -- phát triển
> -- triển khai -- vận hành -- gỡ bỏ), và nhấn mạnh rằng mọi lời gọi API
> --- kể cả API \"nội bộ\" giữa các microservice trong cùng cụm
> Kubernetes --- đều phải được coi là không đáng tin cậy cho đến khi
> được xác thực/phân quyền. Đây chính là cơ sở lý luận cho các đặc điểm
> bảo mật (AuthN/Z, API security, runtime security) của lớp App &
> Integration Platform.*

**4. Tóm tắt / Ghi chú trình bày**

- Lớp (4) là lớp \"lắp ráp và kết nối\" --- biến hạ tầng nền (lớp 1-2)
  và nguyên tắc an ninh (lớp 3) thành các ứng dụng/dịch vụ chạy được,
  đồng thời chuẩn bị dữ liệu để đưa xuống lớp (5).

- Từ khoá cốt lõi cần nhớ: API Gateway -- Microservices -- Container/K8s
  -- CI/CD -- Zero Trust API security.

- Khi trình bày, nên minh hoạ bằng sơ đồ luồng: Client → API Gateway →
  Service mesh/Microservices (chạy trên K8s) → Message queue → Data
  Platform, có lớp Security + Identity (3) bao trùm toàn bộ luồng này.

**5. Tài liệu tham khảo (nguồn chính thống)**

- Kubernetes.io (CNCF) --- Tài liệu chính thức về Kubernetes:
  kubernetes.io/docs/home/ và kubernetes.io/docs/concepts/overview/

- Amazon Web Services --- Amazon API Gateway Documentation:
  docs.aws.amazon.com/apigateway/

- NIST Special Publication 800-207 --- Zero Trust Architecture
  (nist.gov)

- NIST Special Publication 800-204 --- Security Strategies for
  Microservices-based Application Systems

- NIST Special Publication 800-228 (2025) --- Guidelines for API
  Protection

- NIST --- A Zero Trust Architecture Model for Access Control in
  Cloud-Native Applications in Multi-Location Environments:
  nist.gov/publications/zero-trust-architecture-model-access-control-cloud-native-applications-multi-location

- Red Hat --- What is Kubernetes?:
  redhat.com/en/topics/containers/what-is-kubernetes

> *Lưu ý: nhóm nên trích dẫn trực tiếp các trang chính thức của
> Kubernetes.io, AWS Docs và NIST (nist.gov) trong slide/báo cáo để đảm
> bảo tính chính thống theo yêu cầu của đề bài.*
