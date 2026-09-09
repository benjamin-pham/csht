# Kiến Trúc Hạ Tầng CNTT Doanh Nghiệp

## Khái Niệm và Vai Trò của Data Platform

Trong tổng thể kiến trúc hạ tầng công nghệ thông tin (CNTT) doanh
nghiệp, hạ tầng không chỉ dừng lại ở các thiết bị vật lý hay mạng kết
nối thô, mà là một hệ thống đa tầng kết hợp kỹ thuật, vận hành và quản
trị để đảm bảo các hệ thống số hoạt động ổn định, an toàn và tối ưu chi
phí \[1\]. Trong mô hình hạ tầng tham chiếu chuẩn hóa gồm 5 lớp năng lực
cốt lõi, lớp **Data Platform** (Nền tảng dữ liệu) đóng vai trò là trung
tâm lưu trữ, xử lý, khai thác và quản trị toàn bộ tài sản dữ liệu của tổ
chức \[1\].

Data Platform là tập hợp các công nghệ phần cứng, phần mềm, luồng truyền
tải mạng, cơ chế kiểm soát vận hành và chính sách an toàn thông tin được
thiết kế để quản lý dữ liệu xuyên suốt vòng đời---từ khi khởi tạo, thu
thập, biến đổi, lưu trữ cho đến khi phân tích và tiêu hủy \[1\]. Khác
với các ứng dụng nghiệp vụ đơn lẻ, Data Platform cung cấp năng lực nền
tảng nhất quán cho phép kết nối các hệ thống giao dịch (OLTP), hệ thống
phân tích (OLAP), báo cáo thông minh (BI) và các mô hình học máy hay trí
tuệ nhân tạo (AI/ML) \[3\].

Vai trò chiến lược của Data Platform thể hiện ở ba khía cạnh cốt lõi:

1.  **Xóa bỏ các vùng cô lập dữ liệu (Data Silos):** Hợp nhất dữ liệu từ
    nhiều nguồn ứng dụng khác nhau (ERP, CRM, LMS, IoT) về một môi
    trường quản lý tập trung hoặc phân tán có kiểm soát \[2\].

2.  **Đảm bảo tính tin cậy và chất lượng dữ liệu:** Cung cấp chuẩn mực
    về định dạng, quy trình làm sạch và kiểm soát nguồn gốc dữ liệu để
    đảm bảo mọi quyết định kinh doanh đều dựa trên thông tin chính xác
    \[2\].

3.  **Thúc đẩy giá trị kinh doanh từ dữ liệu:** Tạo tiền đề kỹ thuật
    vững chắc để triển khai phân tích thời gian thực (real-time
    analytics), tối ưu hóa vận hành và tuân thủ các quy định pháp lý
    khắt khe về dữ liệu \[2\].

## Tóm Tắt Đặc Điểm Kỹ Thuật Dựa Trên Khung Tham Chiếu Hạ Tầng

Khung tham chiếu hạ tầng CNTT doanh nghiệp phân tách lớp năng lực Data
Platform theo 5 trụ cột kỹ thuật và quản trị \[1\]. Bảng dưới đây tổng
hợp đầy đủ các thành phần chính được quy định trong khung tham chiếu:

+------------+-----------------+------------+-------------+--------------------+--------------+
| **Lớp Năng | **Phần Cứng     | **Phần Mềm | **Mạng      | **Quản Trị         | **Bảo Mật    |
| Lực**      | (HW)**          | (SW)**     | (Network)** | (Governance/Ops)** | (Security)** |
+------------+-----------------+------------+-------------+--------------------+--------------+
| **(5) Data | •               | • DBMS (Hệ | • Ingest /  | • Data governance  | • Encryption |
| Platform** | Storage/compute | quản trị   | Replication |                    | at-rest &    |
|            | mạnh IO         | CSDL)      |             | • Data stewardship | in-transit   |
|            |                 |            | • Batch /   |                    |              |
|            | • Tận dụng năng | • Data     | Stream      | • Data retention   | • Key        |
|            | lực nền tảng từ | Warehouse  | movement    | policies           | Management   |
|            | Lớp (1) Compute | / Lake /   |             |                    | Service      |
|            | & Connectivity  | Lakehouse  | • Kết nối   | • Data quality     | (KMS)        |
|            |                 |            | nguồn dữ    | rules              |              |
|            |                 | • ETL/ELT  | liệu đa     |                    | • Data       |
|            |                 | &          | dạng        | • Metadata         | masking      |
|            |                 | Streaming  |             | standards          |              |
|            |                 |            |             |                    | • Row/Column |
|            |                 | • Catalog  |             |                    | level        |
|            |                 | / Lineage  |             |                    | security     |
|            |                 |            |             |                    |              |
|            |                 | • Master   |             |                    | • Data Loss  |
|            |                 | Data       |             |                    | Prevention   |
|            |                 | Management |             |                    | (DLP)        |
|            |                 | (MDM)      |             |                    |              |
|            |                 |            |             |                    | • Audit truy |
|            |                 | • Data     |             |                    | cập dữ liệu  |
|            |                 | Quality    |             |                    |              |
|            |                 | (DQ)       |             |                    |              |
|            |                 | tooling    |             |                    |              |
+------------+-----------------+------------+-------------+--------------------+--------------+

## Phân Tích Chi Tiết Các Trụ Cột Kỹ Thuật Của Data Platform

### 1. Hạ Tầng Phần Cứng (Hardware - HW)

Hạ tầng phần cứng của Data Platform kế thừa và tận dụng năng lực tính
toán và kết nối cơ bản từ **Lớp (1) Compute & Connectivity** \[1\]. Tuy
nhiên, do đặc thù xử lý khối lượng dữ liệu khổng lồ với tần suất truy
xuất cao, phần cứng dành cho Data Platform có những yêu cầu chuyên biệt:

- **Tối ưu hóa năng lực I/O (Input/Output Performance):** Hệ thống đòi
  hỏi các dòng máy chủ trang bị bộ vi xử lý nhiều nhân, dung lượng RAM
  lớn và hệ thống lưu trữ có chỉ số IOPS (Input/Output Operations Per
  Second) cực cao như ổ cứng NVMe SSD, hệ thống SAN/NAS băng thông rộng
  hoặc kiến trúc lưu trữ phân tán \[1\].

- **Khả năng co giãn (Scalability):** Dù triển khai theo mô hình
  On-premise hay Cloud (Compute/Storage Fabric), phần cứng phải hỗ trợ
  cả hai cơ chế mở rộng dọc (Scale-up - nâng cấp CPU/RAM) và mở rộng
  ngang (Scale-out - thêm nút vào cụm tính toán/lưu trữ) nhằm đáp ứng sự
  tăng trưởng dữ liệu không ngừng mà không làm gián đoạn dịch vụ \[1\].

### 2. Lớp Phần Mềm Và Dịch Vụ (Software - SW)

Lớp phần mềm cấu thành Data Platform bao gồm các công nghệ quản trị, xử
lý và lưu trữ dữ liệu từ mức độ thô đến mức độ cấu trúc cao \[1\]:

- **Hệ quản trị cơ sở dữ liệu (DBMS):** Cung cấp khả năng lưu trữ và
  truy vấn dữ liệu giao dịch hoặc phi cấu trúc (RDBMS, NoSQL, NewSQL)
  \[1\].

- **Kho dữ liệu và Hồ dữ liệu (DW / Data Lake / Lakehouse):** Kiến trúc
  kết hợp giữa kho dữ liệu tối ưu cho truy vấn phân tích structured data
  (Data Warehouse) và hồ dữ liệu chứa dữ liệu thô/phi cấu trúc (Data
  Lake) theo mô hình Data Lakehouse hiện đại, giúp tối ưu hóa chi phí
  lưu trữ và hiệu năng phân tích \[1\].

- **Công cụ tích hợp dữ liệu (ETL/ELT & Streaming):** Thực hiện trích
  xuất, biến đổi và nạp dữ liệu theo lô (Batch Processing via ETL/ELT)
  hoặc xử lý dòng dữ liệu liên tục theo thời gian thực (Event Streaming
  via Kafka/Kinesis) \[1\].

- **Danh mục dữ liệu & Nguồn gốc dữ liệu (Data Catalog / Lineage):** Cho
  phép tìm kiếm, phân loại và theo dõi luồng dịch chuyển dữ liệu từ điểm
  đầu đến điểm cuối trong toàn bộ kiến trúc \[1\].

- **Quản lý dữ liệu chủ & Tối ưu chất lượng dữ liệu (MDM & DQ
  Tooling):** Đảm bảo tính duy nhất, nhất quán của các thực thể dữ liệu
  quan trọng (khách hàng, sản phẩm) và tự động hóa quá trình kiểm tra,
  làm sạch dữ liệu \[1\].

### 3. Mạng Và Hạ Tầng Truyền Dẫn (Network)

Mạng đóng vai trò là \"hệ tuần hoàn\" đảm bảo luồng di chuyển dữ liệu
giữa các hệ thống nguồn và Data Platform diễn ra thông suốt và an toàn
\[1\]:

- **Kết nối nguồn dữ liệu (Source Connectivity):** Thiết lập các đường
  truyền kết nối an toàn (VPC Peering, Direct Connect, VPN, API
  Gateways) để thu thập dữ liệu từ ứng dụng nội bộ, thiết bị ngoại biên
  hoặc các dịch vụ SaaS bên ngoài \[1\].

- **Truyền tải dữ liệu theo lô và dòng (Batch & Stream Movement):** Băng
  thông mạng phải được tính toán để xử lý các đợt chuyển dữ liệu dung
  lượng lớn (Batch Ingestion) trong khung giờ thấp điểm mà không làm
  nghẽn hệ thống, đồng thời đảm bảo độ trễ thấp (Low Latency) cho các
  luồng dữ liệu thời gian thực (Stream Ingestion) \[1\].

- **Đồng bộ và nhân bản (Replication & Synchronization):** Hỗ trợ cơ chế
  Change Data Capture (CDC) để đồng bộ biến động dữ liệu tức thì từ các
  CSDL vận hành về nền tảng phân tích \[1\].

### 4. Quản Trị Và Vận Hành Dữ Liệu (Governance / Ops)

Quản trị dữ liệu là yếu tố then chốt biến dữ liệu từ \"tài nguyên thô\"
thành \"tài sản chiến lược\" có thể kiểm soát được \[1\]. Trụ cột này
được thiết kế dựa trên các tiêu chuẩn quốc tế như DAMA-DMBOK và TOGAF
\[4\]:

- **Quản trị dữ liệu (Data Governance & Stewardship):** Định ra khung
  chính sách, quy trình và phân công trách nhiệm rõ ràng (Data Stewards)
  đối với việc sở hữu, sử dụng và giám sát dữ liệu \[1\].

- **Chính sách lưu trữ và tiêu hủy (Data Retention Policies):** Quy định
  thời gian lưu trữ đối với từng loại dữ liệu nhằm tối ưu chi phí hạ
  tầng và tuân thủ các quy định pháp lý \[1\].

- **Quy tắc chất lượng & Chuẩn hóa siêu dữ liệu (DQ Rules & Metadata
  Standards):** Thiết lập các bộ tiêu chuẩn đánh giá độ chính xác, tính
  đầy đủ của dữ liệu và đồng bộ hóa từ điển dữ liệu (Business Glossary)
  trong toàn doanh nghiệp \[1\].

### 5. Bảo Mật Và An Toàn Dữ Liệu (Security)

Security trong Data Platform không nằm riêng rẽ mà là một lớp bao trùm,
phối hợp chặt chẽ với **Lớp (3) Security & Identity** để bảo vệ dữ liệu
trước các truy cập trái phép và nguy cơ rò rỉ \[1\]:

- **Mã hóa dữ liệu (Encryption):** Áp dụng thuật toán mã hóa mạnh cho dữ
  liệu ở trạng thái nghỉ (At-rest - trên ổ đĩa, database) và dữ liệu
  đang truyền tải (In-transit - qua đường truyền mạng TLS/SSL) \[1\].

- **Dịch vụ quản lý khóa (KMS):** Tích hợp hệ thống quản lý khóa mã hóa
  trung tâm để kiểm soát quyền khởi tạo, xoay vòng và thu hồi khóa an
  toàn \[1\].

- **Che giấu và Phân quyền truy cập chi tiết (Data Masking, Row/Column
  Security):** Sử dụng kỹ thuật làm mờ/mã hóa hóa dữ liệu nhạy cảm (PII)
  đối với môi trường thử nghiệm, kết hợp phân quyền truy cập theo từng
  hàng (Row-level) và từng cột (Column-level) dựa trên vai trò người
  dùng (RBAC/ABAC) \[1\].

- **Phòng chống thất thoát & Ghi vết hoạt động (DLP & Data Access
  Audit):** Triển khai giải giải pháp ngăn chặn thất thoát dữ liệu và
  duy trì nhật ký truy cập (Audit logs) toàn diện nhằm phục vụ công tác
  truy vết và kiểm toán an ninh \[1\].

## Mối Tương Quan Kiến Trúc Và Xu Hướng Phát Triển

Data Platform không hoạt động độc lập mà nằm trong một hệ sinh thái hạ
tầng phụ thuộc lẫn nhau \[1\]. Nó nhận tài nguyên phần cứng từ **Compute
& Connectivity (1)**, được vận hành thông qua các công cụ giám sát từ
**Ops Platform (2)**, tuân thủ chính sách danh tính từ **Security &
Identity (3)**, và cung cấp dữ liệu đầu vào/đầu ra cho các dịch vụ ứng
dụng tại **App & Integration Platform (4)** \[1\].

Trong bối cảnh chuyển đổi số hiện đại, kiến trúc Data Platform đang tiến
hóa mạnh mẽ theo hai xu hướng chính \[5\]:

- **Data Fabric:** Tự động hóa việc tích hợp, khám phá và quản trị dữ
  liệu bằng cách sử dụng phân tích metadata thông minh trên toàn bộ môi
  trường Hybrid Cloud \[5\].

- **Data Mesh:** Chuyển đổi từ mô hình dữ liệu tập trung sang mô hình
  phân tán theo miền nghiệp vụ (Domain-driven), coi dữ liệu như một sản
  phẩm (Data as a Product) nhưng vẫn duy trì sự quản trị nhất quán
  (Federated Computational Governance) \[8\].

## Kết Luận

Lớp năng lực Data Platform trong Khung tham chiếu kiến trúc hạ tầng CNTT
doanh nghiệp là nền tảng cốt lõi giúp tổ chức quản lý, bảo vệ và tối ưu
hóa giá trị của tài sản dữ liệu \[1\]. Việc triển khai Data Platform đòi
hỏi sự đầu tư đồng bộ và cân bằng giữa 5 khía cạnh: trang bị phần cứng
I/O cao, lựa chọn phần mềm lưu trữ/xử lý linh hoạt, thiết lập hạ tầng
mạng kết nối thông suốt, duy trì kỷ luật quản trị dữ liệu nghiêm ngặt và
bao trùm bởi lớp bảo mật đa tầng \[1\]. Việc tuân thủ khung tham chiếu
này giúp doanh nghiệp xây dựng một hạ tầng dữ liệu vững chắc, sẵn sàng
đáp ứng các yêu cầu phân tích cao cấp và trí tuệ nhân tạo trong tương
lai \[2\].

#### Nguồn trích dẫn

1.  1\. Khung tham chiếu hạ tầng CNTT doanh nghiệp. (2.pdf).

2.  2\. SPD Technology. (n.d.). Data Management Framework: Shaping an
    Approach for Controlling Data.
    [[https://spd.tech/data/data-management-framework-shaping-an-approach-for-controlling-data/]{.underline}](https://spd.tech/data/data-management-framework-shaping-an-approach-for-controlling-data/)

3.  3\. Atlan. (n.d.). What is Data Architecture? Types, Components &
    Principles.
    [[https://atlan.com/what-is-data-architecture/]{.underline}](https://atlan.com/what-is-data-architecture/)

4.  4\. Dataforest. (2026). What Is Data Architecture? Types, Frameworks
    & Guide.
    [[https://dataforest.ai/blog/what-is-data-architecture]{.underline}](https://dataforest.ai/blog/what-is-data-architecture)

5.  5\. 8allocate. (n.d.). How to Develop an Effective Data Management
    Strategy.
    [[https://8allocate.com/blog/how-to-develop-an-effective-data-management-strategy/]{.underline}](https://8allocate.com/blog/how-to-develop-an-effective-data-management-strategy/)

6.  6\. CData Software. (n.d.). What is Data Architecture?.
    [[https://www.cdata.com/blog/what-is-data-architecture]{.underline}](https://www.cdata.com/blog/what-is-data-architecture)

7.  7\. Google Patents. (2023). US11818156B1 - Data lake-enabled
    security platform.
    [[https://patents.google.com/patent/US11818156B1/en]{.underline}](https://patents.google.com/patent/US11818156B1/en)

8.  8\. Scribd. (n.d.). Effective Data Architecture Design Guide.
    [[https://www.scribd.com/document/976917545/Unit-3-Designing-Good-Data-Architecture]{.underline}](https://www.scribd.com/document/976917545/Unit-3-Designing-Good-Data-Architecture)
