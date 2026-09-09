#### User: 26410325 Tìm hiểu về Ops Platform: Nếu ví hạ tầng CNTT như một nhà máy, thì Ops Platform chính là phòng điều khiển trung tâm --- theo dõi máy móc, sửa khi hỏng, đảm bảo sản xuất không gián đoạn, và tính xem tốn bao nhiêu tiền điện.

####  **- Monitoring / Observability**

- **Monitoring**: theo dõi các chỉ số (CPU, RAM, disk, network\...) để
  biết hệ thống có \"khỏe\" không, và cảnh báo (alert) khi có vấn đề.

- **Observability**: hiểu rộng hơn --- dựa vào 3 loại dữ liệu: *logs*
  (nhật ký), *metrics* (số liệu), *traces* (dấu vết request đi qua đâu)
  để biết **tại sao** hệ thống lỗi, không chỉ biết **là** nó lỗi.

#### Ví dụ công cụ: Prometheus, Grafana, Datadog, ELK Stack. ** - ITSM (IT Service Management)**

- Là cách tổ chức quản lý dịch vụ CNTT theo quy trình chuẩn (thường dựa
  trên framework ITIL).

- Gồm các quy trình quen thuộc: **Incident Management** (xử lý sự cố),
  **Problem Management** (tìm nguyên nhân gốc), **Change Management**
  (quản lý thay đổi), **Service Request** (yêu cầu dịch vụ).

- Công cụ tiêu biểu: ServiceNow, Jira Service Management.

#### **- CMDB (Configuration Management Database)**

- Là \"cuốn sổ tay\" ghi lại tất cả tài sản CNTT (server, ứng dụng,
  thiết bị mạng\...) gọi là **CI -- Configuration Item**, và mối quan hệ
  giữa chúng.

- Ví dụ: biết ứng dụng A chạy trên server B, server B kết nối switch C →
  khi server B hỏng, biết ngay ứng dụng nào bị ảnh hưởng.

- CMDB là \"trái tim dữ liệu\" để ITSM và Monitoring hoạt động hiệu quả
  hơn.

#### **- Patching (vá lỗi)**

- Là việc cập nhật bản vá (patch) cho OS, phần mềm, firmware để vá lỗ
  hổng bảo mật hoặc sửa bug.

- Cần có quy trình rõ ràng: test trước khi patch, có lịch bảo trì
  (maintenance window), rollback nếu lỗi.

- Không patch kịp = nguy cơ bị hack rất cao (nhiều vụ tấn công lớn là do
  lỗ hổng đã có bản vá nhưng chưa cập nhật).

#### **- Backup**

- Sao lưu dữ liệu định kỳ để phòng khi mất dữ liệu (do lỗi phần cứng,
  ransomware, thao tác sai\...).

- Nguyên tắc phổ biến: **3-2-1** --- 3 bản sao, 2 loại phương tiện lưu
  trữ khác nhau, 1 bản lưu ở nơi khác (offsite).

#### **- DR (Disaster Recovery)**

- Là kế hoạch khôi phục hệ thống khi xảy ra thảm họa lớn (cháy nổ
  datacenter, thiên tai, tấn công mạng diện rộng\...).\`

- Hai chỉ số quan trọng cần nhớ:

  - **RTO (Recovery Time Objective)**: khôi phục trong bao lâu?

  - **RPO (Recovery Point Objective)**: chấp nhận mất dữ liệu trong
    khoảng thời gian bao lâu?

- Backup là một phần của DR, nhưng DR rộng hơn --- còn gồm cả kế hoạch
  chuyển hệ thống sang site dự phòng.

#### **- Capacity (quản lý năng lực)**

- Dự đoán và đảm bảo hệ thống luôn đủ tài nguyên (CPU, RAM, băng thông,
  dung lượng lưu trữ\...) để đáp ứng nhu cầu hiện tại và tương lai.

- Tránh 2 thái cực: **thiếu tài nguyên** (hệ thống chậm/crash) và **dư
  thừa quá mức** (lãng phí tiền).

#### **- FinOps (Financial Operations)** 

- Là cách quản lý & tối ưu chi phí, đặc biệt phổ biến trong thời cloud
  --- vì cloud tính tiền theo mức sử dụng, rất dễ \"đốt tiền\" nếu không
  kiểm soát.

- FinOps giúp các bên (kỹ thuật, tài chính, kinh doanh) cùng nhìn vào
  chi phí hạ tầng, tối ưu (ví dụ: tắt máy ảo không dùng, mua gói cam kết
  dài hạn để rẻ hơn\...).

Một số link tài liệu tham khảo thêm để hiểu rõ về các khái niệm:\
[[Hạ tầng công nghệ thông tin
Wiki]{.underline}](https://vi.wikipedia.org/wiki/H%E1%BA%A1_t%E1%BA%A7ng_c%C3%B4ng_ngh%E1%BB%87_th%C3%B4ng_tin)\
[[https://fptcloud.com/ha-tang-cong-nghe-thong-tin-la-gi/]{.underline}](https://fptcloud.com/ha-tang-cong-nghe-thong-tin-la-gi/)

[[Wikipedia tiếng Việt -- Quản lý dịch vụ CNTT
(ITSM)]{.underline}](https://vi.wikipedia.org/wiki/Qu%E1%BA%A3n_l%C3%BD_d%E1%BB%8Bch_v%E1%BB%A5_c%C3%B4ng_ngh%E1%BB%87_th%C3%B4ng_tin)\
[[Viettel IDC -- RTO và RPO là
gì?]{.underline}](https://www.viettelidc.com.vn/tin-tuc/tim-hieu-ve-rto-va-rpo-2-khai-niem-can-nam-khi-trien-khai-backup)
