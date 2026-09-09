1.  Ops Platform là gì?

Ops Platform là gì là mô hình vận hành tập trung vào việc xây dựng quản
trị và vận hành nền tảng kỹ thuật nội bộ nhằm cung cấp các năng lực hạ
tầng CI CD bảo mật quan sát và triển khai dưới dạng dịch vụ tự phục vụ
cho các đội phát triển

2.  Vai trò của Ops Platform?

Đảm bảo tính sẵn sàng, hiệu suất và độ tin cậy của toàn bộ hệ thống.
Giảm tải công việc thủ công thông qua tự động hóa. Cung cấp bức tranh
toàn cảnh cho đội ngũ IT, giúp nhanh chóng tìm ra và xử lý nguyên nhân
gốc rễ khi có sự cố.

3.  Khung tham chiếu

    a.  Phần cứng (Hardware)

> Tận dụng phần cứng đang rãnh để có thể chạy những tool hoặc agent để
> tự động kiểm tra, phân tích log, để gửi cảnh báo tới quản trị viên.

b.  Phần mềm (Software)

    i.  Monitoring/observability: Sử dụng những công cụ phần mềm để hiển
        thị những chỉ số hoặc ghi lại những lịch sử thay đổi và ai đã
        thay đổi.

    ii. ITSM:

> ITSM đề cập đến tập hợp các chính sách, quy trình và thủ tục được sử
> dụng để quản lý các dịch vụ CNTT trong suốt vòng đời của chúng. Không
> giống như các mô hình hỗ trợ CNTT truyền thống tập trung vào việc khắc
> phục sự cố một cách phản ứng, ITSM có cách tiếp cận chủ động bằng cách
> tối ưu hóa việc cung cấp dịch vụ, tự động hóa quy trình làm việc và
> nâng cao trải nghiệm người dùng.\
> Nguồn:
> https://vn.linkedin.com/pulse/what-itsm-why-its-essential-modern-enterprises-easyvista-arkzf?tl=vi

iii. CMDB:

> CMDB là một kho lưu trữ tập trung đóng vai trò là xương sống của ITSM
> trong ServiceNow. Nó lưu trữ thông tin về các mục cấu hình (CI) và các
> mối quan hệ, cho phép các tổ chức duy trì cái nhìn toàn diện về môi
> trường CNTT của họ. CI có thể bao gồm phần cứng, phần mềm, mạng, cơ sở
> vật chất, nhân sự và tài liệu, tất cả đều rất quan trọng để cung cấp
> dịch vụ CNTT một cách hiệu quả.
>
> Nguồn:
> https://vn.linkedin.com/pulse/understanding-configuration-management-database-cmdb-lopez-vargas-srnwe?tl=vi

iv. FinOps:

> FinOps là sự kết hợp của Finace và DevOps nhấn mạnh sự giao tiếp và
> hợp tác giữa các nhóm kinh doanh và kỹ thuật.
>
> FinOps mang lại sự thay đổi mục tiêu tài chính trong các giá trị công
> nghệ như Cloud, SaaS, PaaS, Licensing, Data Centers, Data Cloud
> Platforms,\... FinOps cho phép bộ phận kỹ thuật và kinh cân bằng giữa
> tốc độ, chi phí và chất lượng và quyết định đầu tư.
>
> Nguồn: <https://www.finops.org/introduction/what-is-finops/>

v.  IaC/automation:

> IaC (Infrastructure as Code) tự động hóa quy trình hoặc công việc bằng
> code thay vì thực hiện thủ công tối ưu hóa quy trình làm việc.
>
> Tham khảo: Teraform <https://developer.hashicorp.com/terraform>

c.  Mạng (Network)

> Đảm bảo luồng dữ liệu vận hành được truyền tải an toàn, xuyên suốt mà
> không làm ảnh hưởng đến băng thông mạng của ứng dụng thực tế.
>
> Management Plane/Out-of-band management: Tách biệt luồng dữ liệu quản
> trị khỏi luồng dữ liệu người dùng.
>
> Pipeline dữ liệu lớn: Sử dụng các công cụ như Kafka, Fluentd, Logstash
> để trung chuyển hàng triệu dòng logs từ các server về hệ thống giám
> sát mà không làm nghẽn mạng nội bộ.

d.  Quản trị (Governance/Ops)

> Incident/Change/Problem: Các quy trình xử lý sự cố, quản lý thay đổi
> hệ thống và xử lý các vấn đề theo khung ITIL.
>
> SLO/SLA: Cam kết chất lượng dịch vụ và mục tiêu dịch vụ (chuẩn SRE).
>
> DR drills, capacity planning: Diễn tập phục hồi thảm họa định kỳ, lên
> kế hoạch khi nào cần mua thêm những phần cứng lưu trữ.
>
> Chuẩn vận hành: Chuẩn hóa tài liệu quy tắc vận hành cho kỹ thuật.
>
> Tham khảo: https://sre.google/books/,
> https://www.atlassian.com/itsm/itil

e.  Bảo mật (Security)

> Audit/log integrity: Đảm bảo log hệ thống và log thao tác không thể bị
> xóa hay chỉnh sửa, nhằm mục đích điều tra sau sự cố.
>
> Kiểm soát quyền admin (PAM - Privileged Access Management): Không dùng
> chung tài khoản root/admin, cung cấp tài khoản tạm thời có quyền vừa
> đủ và giới hạn thời gian sử dụng tài khoản.
>
> Quy trình vá lỗi & Cảnh báo an ninh vận hành: Cập nhật các bản vá cho
> hệ điều hành/phần mềm vận hành. Kết nối với hệ thống bảo mật để đưa ra
> cảnh báo nếu có hành vi vận hành bất thường.
