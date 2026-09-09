\(2\) Ops Platform

**I.Khái niệm:** Ops Platform (Operations Platform) là nền tảng vận hành
CNTT, gồm tập hợp các công cụ, quy trình và dịch vụ giúp doanh nghiệp
giám sát toàn bộ hạ tầng, quản lý cấu hình, quản lý tài sản CNTT, quản
lý sự cố, quản lý thay đổi, sao lưu và khôi phục, tự động hóa vận
hành,đảm bảo SLA và tính sẵn sàng của hệ thống

**II.Vai trò:** Không tạo ra chức năng kinh doanh mới mà đảm bảo hệ
thống luôn vận hành đúng gồm:

[[https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/servicemanagement.html]{.underline}](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/servicemanagement.html)

[[https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.operationalExcellence.en.html]{.underline}](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.operationalExcellence.en.html)

  ------------------- ------------------------------------------------
  Vãi trò             Ý nghĩa
  Giám sát hệ thống   Theo dõi CPU, RAM, Disk, Network, Database\...
  Phát hiện sự cố     Cảnh báo ngay khi có lỗi
  Quản lý cấu hinh    Biết chính xác server nào đang chạy gì
  Quản lý thay đổi    Tránh việc cập nhật gây lỗi toàn hệ thống
  Sao lưu dữ liệu     Phục hồi khi mất dữ liệu
  Tự động hóa         Giảm thao tác thủ công
  Đo SLA              Đảm bảo dịch vụ hoạt động đúng cam kết
  ------------------- ------------------------------------------------

**III.Đặc điểm:**

  --------------- --------------------------------------
  Thành phần      Chức năng
  Monitoring      Giám sát hệ thống
  Observability   Quan sát toàn bộ trạng thái hệ thống
  ITSM            Quản lý dịch vụ CNTT
  CMDB            Quản lý cấu hình
  Patching        Cập nhật bản vá
  Backup/DR       Sao lưu và khôi phục
  IaC             Quản lý hạ tầng bằng mã
  Automation      Tự động hóa
  FinOps          Quản lý chi phí Cloud
  --------------- --------------------------------------

**1.Monitoring** là quá trình: thu thập số liệu, theo dõi trạng thái,
phát hiện lỗi

Ví dụ: CPU, RAM, Disk, Network, Database, Web Server

Công cụ phổ biến: Prometheus, Zabbix, Nagios, Azure Monitor, Amazon
CloudWatch

**2.Observability** cao hơn Monitoring không chỉ biết "Server đang lỗi"
mà còn biết "vì sao lỗi".

Sử dụng: Metrics, Logs, Traces để xác định nguyên nhân gốc (root cause)

**3.ITSM (IT Service Management)** là tập hợp các quy trình chuẩn để:
Incident Management, Change Management, Problem Management, Service
Request, Asset Management

Giúp: Chuẩn hóa quy trình, giảm lỗi, nâng chất lượng dịch vụ

**4.CMDB (Configuration Management Database)** cơ sở dữ liệu lưu thông
tin về: Server, Switch, Router, Database, Application, VM, Service, và
lưu mối quan hệ giữa các thành phần

**Ví dụ:** Website -\> Application Server -\> Database -\> Storage (nếu
lỗi sẽ biết ngay Website bị ảnh hưởng)

**5.Patching** là quá trình: Cập nhật bản vá, vá lỗ hổng, sửa bug

**Ví dụ:** Window Update, Linux Security Patch, Firmware Switch

**6.Backup / DR:** Sao lưu dữ liệu, còn **Disaster Recovery (DR):** phục
hồi hệ thống khi xảy ra cháy data center, ransomware, mất điện, hỏng ổ
cứng

**7.IaC (Infrastructure as Code)** quản lý hạ tầng bằng mã dùng:
Terraform, ansible, AWS cloudFormation, bicep giúp triển khai nhanh, ít
sai sót, dễ tái sử dụng

**8.Automation** tự động hóa: Backup, restart service, deploy, scaling,
patch với mục tiêu giảm tác thủ công

**9.FinOps** quản trị chi phí cloud theo dõi dịch vụ nào tốn tiền, phòng
ban nào dùng nhiều, tối ưu tài nguyên

Ví dụ: một VM chỉ dùng 5% CPU nên giảm cấu hình để tiết kiệm chi phí

**IV.Ops Platform trong kiến trúc hạ tầng (theo khung tham chiếu)**

Hardware -\> Software -\> Network -\> Ops Platform -\> Security

không thay thế các lớp khác nó điều phối việc vận hành của:
Hardware,Software, Network và phối hợp chặt chẽ với lớp security để duy
trì hệ thống an toàn và ổn định

**VI.Với thực tế (**Với Website thương mại điện tử**)**

Với quy trình vận hành Ops Platform áp dụng:

1.Monitoring phát hiện CPU tăng 95%.

2.Observability phân tích log và trace để xác định nguyên nhân.

3.ITSM tự động tạo ticket Incident.

4.CMDB xác định server và các dịch vụ liên quan.

5.Automation tự khởi động thêm máy chủ nếu được cấu hình.

6.Nếu cần cập nhật, Change Management kiểm soát việc triển khai.

7.Backup/DR sẵn sàng khôi phục nếu xảy ra sự cố nghiêm trọng.
