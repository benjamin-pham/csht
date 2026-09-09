**1. Mục đích và phạm vi**

Giai đoạn 1 tập trung mô tả bức tranh công nghệ hiện tại của Ways
Station, xác định những điểm gây ảnh hưởng trực tiếp đến hoạt động kinh
doanh và xây dựng một định hướng hạ tầng có khả năng đáp ứng quá trình
mở rộng chuỗi. Phạm vi xem xét bao gồm hệ thống tại cơ sở, kết nối mạng,
vận hành CNTT, bảo mật, ứng dụng và dữ liệu.

Thay vì chỉ thay thế thiết bị, kế hoạch ưu tiên chuẩn hóa cách vận hành,
giảm phụ thuộc vào xử lý thủ công và tạo nền tảng để dữ liệu từ các cơ
sở có thể được khai thác tập trung.

**2. Giai đoạn A – Chụp lại bức tranh hiện trạng**

Qua khảo sát giả định, hạ tầng có đặc điểm phân tán: mỗi cơ sở tương đối
độc lập, trong khi dữ liệu quản trị cần được tổng hợp về trung tâm. Điều
này tạo ra khoảng cách giữa hoạt động tại quầy và nhu cầu ra quyết định
của cấp quản lý.

**2.1. Hạ tầng thiết bị và đường truyền**

> Thiết bị tại cơ sở chủ yếu phục vụ POS, quản lý dịch vụ và các tác vụ
> văn phòng; cấu hình giữa các cơ sở chưa đồng nhất.
>
> Một số thiết bị mạng chưa hỗ trợ tốt việc phân tách vùng truy cập,
> khiến mạng nghiệp vụ và mạng dành cho khách có thể dùng chung hạ tầng.
>
> Kết nối Internet phụ thuộc vào từng cơ sở; phương án dự phòng chưa
> được chuẩn hóa.
>
> Khi thiết bị mạng hoặc đường truyền chính gặp lỗi, khả năng chuyển
> sang phương án dự phòng còn hạn chế.

**2.2. Quy trình hỗ trợ và giám sát**

> Sự cố thường được phản ánh từ nhân viên tại cơ sở thay vì phát hiện
> qua hệ thống cảnh báo chủ động.
>
> Nhật ký hệ thống nằm ở nhiều máy khác nhau, gây khó khăn cho việc truy
> vết nguyên nhân.
>
> Việc cập nhật phần mềm và cấu hình thiết bị chưa có một quy trình tự
> động thống nhất.
>
> Thời gian xử lý phụ thuộc nhiều vào khả năng hỗ trợ từ xa hoặc việc
> nhân sự kỹ thuật phải đến trực tiếp.

**2.3. An toàn thông tin và tài khoản**

> Tài khoản sử dụng cho các ứng dụng nghiệp vụ có nguy cơ bị phân tán
> giữa nhiều hệ thống.
>
> Chưa có cơ chế quản lý quyền tập trung theo vai trò; việc cấp và thu
> hồi tài khoản dễ phụ thuộc vào thao tác thủ công.
>
> Dữ liệu quan trọng cần được phân loại rõ hơn để xác định loại nào được
> lưu tại cơ sở, loại nào phải đưa về hệ thống trung tâm.
>
> Việc ghi nhận nhật ký truy cập chưa đủ tập trung để hỗ trợ kiểm tra
> khi có sự cố.

**2.4. Ứng dụng và kết nối giữa các hệ thống**

> Các phần mềm nghiệp vụ có thể hoạt động tốt ở từng chức năng riêng
> nhưng việc trao đổi dữ liệu giữa chúng còn hạn chế.
>
> Một số báo cáo cần tổng hợp bằng bảng tính sau khi dữ liệu được xuất
> từ nhiều nguồn.
>
> Thiếu một lớp tích hợp trung gian khiến việc mở thêm ứng dụng mới có
> thể phát sinh nhiều kết nối riêng lẻ.
>
> Thời gian cấu hình một cơ sở mới phụ thuộc vào nhiều bước thủ công.

**2.5. Dữ liệu và báo cáo quản trị**

> Dữ liệu giao dịch, khách hàng, vận hành và doanh thu có thể nằm ở các
> nguồn khác nhau.
>
> Nhân viên phải kiểm tra, đối chiếu hoặc nhập lại một phần thông tin
> trước khi lập báo cáo.
>
> Báo cáo quản trị chưa đạt mức gần thời gian thực, nên phản ứng với
> biến động trong ngày còn chậm.
>
> Chưa có kho dữ liệu thống nhất để phân tích xu hướng sử dụng dịch vụ
> giữa các nhóm khách hàng.

**2.6. Bộ chỉ số nền dùng cho bài toán**

| **Chỉ số** | **Mức giả định hiện tại** | **Ý nghĩa** |
|:--:|----|----|
| Sự cố CNTT tại cơ sở | Khoảng 1–3 vụ/cơ sở/tháng | Phản ánh độ ổn định của hạ tầng |
| Thời gian phát hiện | Khoảng 2–6 giờ | Độ chủ động của hệ thống giám sát |
| Thời gian xử lý | Khoảng 6–18 giờ | Khả năng khôi phục dịch vụ |
| Sao lưu tự động | Khoảng 20% | Mức độ bảo vệ dữ liệu |
| Độ trễ báo cáo | Khoảng 12–36 giờ | Khả năng ra quyết định theo ngày |
| Triển khai cơ sở mới | 2–5 ngày | Mức độ chuẩn hóa và tự động hóa |

**3. Giai đoạn B – Xác định điểm nghẽn và lý do cần thay đổi**

Vấn đề cốt lõi không nằm ở một thiết bị riêng lẻ mà ở cách các thành
phần đang vận hành thiếu tính tập trung và thiếu cơ chế dự phòng. Nếu
giữ nguyên mô hình, khi số lượng cơ sở tăng lên, khối lượng hỗ trợ, đối
soát dữ liệu và quản lý tài khoản cũng tăng theo.

**3.1. Bốn nhóm vấn đề ưu tiên**

| **Nhóm** | **Biểu hiện** | **Hệ quả** | **Mức ưu tiên** |
|:--:|----|----|----|
| Độ ổn định | Phụ thuộc đường truyền và thiết bị đơn lẻ | Dịch vụ tại cơ sở có thể gián đoạn | Rất cao |
| Dữ liệu | Nhiều nguồn và báo cáo thủ công | Chậm đối soát, khó nhìn toàn chuỗi | Cao |
| Bảo mật | Quản lý tài khoản và log chưa tập trung | Khó kiểm soát truy cập | Rất cao |
| Mở rộng | Cấu hình cơ sở còn nhiều bước thủ công | Tăng chi phí khi mở rộng | Cao |

**3.2. Tác động nếu chưa xử lý**

> Hoạt động tại quầy có thể bị ảnh hưởng khi kết nối tới hệ thống trung
> tâm không ổn định.
>
> Ban quản lý phải chờ tổng hợp dữ liệu trước khi đánh giá doanh thu,
> hiệu suất dịch vụ hoặc nhu cầu tồn kho.
>
> Khi số lượng cơ sở tăng, nhân sự CNTT phải xử lý nhiều cấu hình tương
> tự nhau bằng tay.
>
> Tài khoản và dữ liệu phân tán làm tăng diện tích rủi ro khi xảy ra sự
> cố bảo mật.
>
> Chi phí duy trì hệ thống cũ tăng dần nhưng không tạo thêm nhiều giá
> trị cho hoạt động kinh doanh.

**3.3. Ma trận rủi ro**

| **Rủi ro** | **Khả năng** | **Ảnh hưởng** | **Cách giảm thiểu** |
|:--:|----|----|----|
| Mất kết nối tại cơ sở | Cao | Cao | Thiết kế Offline-first và đường truyền dự phòng |
| Mất hoặc sai lệch dữ liệu | Trung bình | Rất cao | Backup tự động, kiểm tra tính toàn vẹn và phân quyền |
| Tài khoản bị lộ | Trung bình | Cao | SSO, MFA, RBAC và nhật ký tập trung |
| Triển khai chậm | Cao | Trung bình | Chuẩn hóa cấu hình, IaC và bộ cài đặt mẫu |
| Báo cáo không kịp thời | Cao | Cao | Xây dựng pipeline dữ liệu tập trung |

**4. Giai đoạn C – Mục tiêu cần đạt sau chuyển đổi**

Mục tiêu được đặt theo hướng đo được và có thể kiểm tra sau khi triển
khai. Các chỉ tiêu dưới đây là mục tiêu đề xuất cho bài tập, cần được
hiệu chỉnh sau khi có số liệu thực tế.

| **KPI** | **Mốc hiện tại (giả định)** | **Mục tiêu đề xuất** | **Cách kiểm tra** |
|:--:|----|----|----|
| Availability dịch vụ lõi | Chưa có baseline ổn định | ≥ 99,9% | Theo dõi monitoring hàng tháng |
| MTTD | 2–6 giờ | \< 10 phút | Đối chiếu alert và ticket |
| MTTR | 6–18 giờ | \< 60 phút cho lỗi thông thường | Timestamp của incident |
| RPO | ≤ 24 giờ | ≤ 30 phút | Kiểm tra bản sao lưu |
| Độ trễ dữ liệu | 12–36 giờ | \< 15 phút | Đối chiếu timestamp nguồn/đích |
| Triển khai cơ sở | 2–5 ngày | \< 1 ngày | Đo thời gian từ cấu hình đến nghiệm thu |
| Bao phủ MFA | Chưa đồng nhất | 100% tài khoản quản trị | Báo cáo IAM |

**4.1. Nguyên tắc thiết kế mục tiêu**

> Hoạt động kinh doanh tại cơ sở không nên phụ thuộc hoàn toàn vào
> Internet.
>
> Một tài khoản cần có danh tính thống nhất và quyền hạn rõ ràng.
>
> Dữ liệu nên được thu thập một lần, sau đó tái sử dụng cho nhiều báo
> cáo.
>
> Hạ tầng mới phải có khả năng mở rộng mà không cần thay đổi toàn bộ
> kiến trúc.
>
> Mọi thành phần quan trọng phải có cơ chế giám sát, sao lưu và khôi
> phục.

**5. Giai đoạn D – Các phương án kiến trúc đề xuất**

Ba phương án được xây dựng theo ba mức độ tập trung khác nhau. Việc lựa
chọn không chỉ dựa vào chi phí mà còn dựa vào khả năng duy trì hoạt động
tại cơ sở, mức độ kiểm soát dữ liệu và năng lực vận hành của đội ngũ
CNTT.

**5.1. Phương án A – Trung tâm dữ liệu tập trung**

> Đưa phần lớn máy chủ và cơ sở dữ liệu vào một trung tâm dữ liệu chuyên
> dụng.
>
> Các cơ sở kết nối về trung tâm qua VPN/SD-WAN.
>
> Đầu tư hệ thống máy chủ, lưu trữ, firewall và sao lưu tập trung.
>
> Phù hợp khi doanh nghiệp muốn kiểm soát tài sản CNTT chặt chẽ.
>
> Điểm hạn chế: vốn đầu tư ban đầu cao và việc mở rộng phụ thuộc vào
> năng lực phần cứng.

**5.2. Phương án B – Mô hình lai Edge + Cloud**

> Giữ một lớp xử lý tối thiểu tại cơ sở để POS và các nghiệp vụ thiết
> yếu vẫn chạy khi mất Internet.
>
> Đồng bộ dữ liệu về Cloud khi kết nối được khôi phục.
>
> Đưa API, dịch vụ tích hợp, kho dữ liệu và dashboard lên Cloud.
>
> Dùng IAM/SSO, MFA và phân quyền theo vai trò cho các ứng dụng.
>
> Áp dụng monitoring tập trung, backup tự động và cơ chế cảnh báo sự cố.
>
> Đây là phương án cân bằng giữa tính liên tục tại cơ sở và khả năng mở
> rộng.

**5.3. Phương án C – Cloud tập trung**

> Phần lớn ứng dụng và dữ liệu được chuyển lên Cloud.
>
> Thiết bị tại cơ sở chủ yếu đóng vai trò đầu cuối truy cập dịch vụ.
>
> Triển khai và mở rộng nhanh, giảm phần cứng phải quản lý tại từng cơ
> sở.
>
> Hạn chế lớn nhất là mức độ phụ thuộc vào chất lượng Internet tại cơ
> sở.
>
> Cần bổ sung phương án cache/offline nếu chọn mô hình này cho nghiệp vụ
> quan trọng.

**5.4. So sánh ba hướng triển khai**

| **Tiêu chí** | **A. Trung tâm tập trung** | **B. Edge + Cloud** | **C. Cloud tập trung** |
|:--:|----|----|----|
| Chi phí ban đầu | Cao | Trung bình | Thấp–trung bình |
| Khả năng mở rộng | Trung bình | Cao | Rất cao |
| Chạy khi mất Internet | Tốt nếu có hệ thống tại cơ sở | Rất tốt | Hạn chế |
| Quản lý tập trung | Tốt | Rất tốt | Rất tốt |
| Độ phức tạp | Trung bình | Cao | Trung bình |
| Phù hợp với chuỗi nhiều cơ sở | Khá | Rất phù hợp | Phù hợp nếu mạng ổn định |

**6. Phương án được đề xuất**

Phương án B – Edge + Cloud được lựa chọn cho giai đoạn tiếp theo. Lý do
chính là mô hình này giải quyết được hai yêu cầu có khả năng mâu thuẫn:
cơ sở vẫn phải phục vụ khách hàng khi mạng gặp lỗi, trong khi ban quản
lý cần dữ liệu tập trung để điều hành toàn chuỗi.

**6.1. Sơ đồ logic ở mức khái niệm**

**\[Cơ sở\] → \[Edge/POS + Cache\] → \[VPN/SD-WAN\] → \[API &
Integration\] → \[Cloud Platform\]\
↓\
\[Data Warehouse/Lakehouse\]\
↓\
\[BI / Dashboard quản trị\]**

**6.2. Lộ trình triển khai sơ bộ**

| **Giai đoạn** | **Thời lượng dự kiến** | **Công việc chính** | **Kết quả** |
|:--:|----|----|----|
| Chuẩn hóa | 2–3 tuần | Kiểm kê thiết bị, mạng, tài khoản và dữ liệu | Bộ baseline thống nhất |
| Thử nghiệm | 3–4 tuần | Pilot tại một số cơ sở đại diện | Đánh giá mô hình Edge + Cloud |
| Mở rộng | 6–10 tuần | Triển khai theo nhóm cơ sở | Hạ tầng được chuẩn hóa |
| Tối ưu | 3–4 tuần | Tinh chỉnh monitoring, backup, dashboard | Bộ KPI vận hành |

**7. Kết luận giai đoạn 1**

Kết quả của giai đoạn 1 là xác định được hiện trạng, các điểm nghẽn
chính, bộ KPI mục tiêu và ba hướng kiến trúc có thể triển khai. Trọng
tâm của kế hoạch không phải thay mới toàn bộ hạ tầng trong một lần, mà
là từng bước chuẩn hóa mạng, danh tính, dữ liệu và khả năng giám sát.
