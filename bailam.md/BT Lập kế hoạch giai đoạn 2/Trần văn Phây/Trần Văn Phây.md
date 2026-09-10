**THUYẾT MINH ĐỀ TÀI XÂY DỰNG HỆ THỐNG PHẦN MỀM — GIAI ĐOẠN 2**

*Xây dựng nền tảng tích hợp và kho dữ liệu vận hành hợp nhất cho hệ
thống thể thao – giải trí Ways Station*

*Nội dung: Yêu cầu nghiệp vụ và hệ thống · Thiết kế giải pháp TO-BE và
kiến trúc · Kế hoạch triển khai (WBS) · Nhân sự và tổ chức · Dự toán chi
phí*

*Quy ước: \[n\] = nguồn kiểm chứng được · (giả định) = số do nhóm ước
tính, có nêu cơ sở tính*

**Mốc xuất phát mang từ giai đoạn 1.** Báo cáo doanh thu toàn hệ thống
hiện trễ **T+~30 ngày** (giả định); **~306 giờ** lao động thủ công mỗi
tuần dùng để hợp nhất số liệu (giả định); mức trưởng thành số **1,6/5**.
Toàn bộ yêu cầu và thiết kế dưới đây nhằm đưa ba con số này về T+1 ngày,
dưới 20 giờ/tuần và ≥ 3,0/5.

**5. YÊU CẦU NGHIỆP VỤ VÀ YÊU CẦU HỆ THỐNG**

**5.1. Yêu cầu nghiệp vụ (mức BRD)**

| **Mã** | **Nghiệp vụ** | **Tác nhân** | **Luồng chính** | **Ngoại lệ** | **Vào / Ra** |
|----|----|----|----|----|----|
| UC-01 | Ghi nhận giao dịch tại quầy | Thu ngân | Mở bàn/máy → tính giờ → thu tiền → hệ thống sinh mã và ghi nhận | Mất kết nối: ghi tạm, tự đẩy lại khi có mạng | Vào: dịch vụ, thời lượng, phương thức thanh toán. Ra: giao dịch ĐÃ GHI |
| UC-02 | Xác nhận chốt ca | Trưởng ca | Hệ thống tính sẵn số của ca → trưởng ca đối chiếu tiền thực → xác nhận | Lệch \> 2%: bắt buộc ghi lý do, chuyển quản lý khu vực phê duyệt | Vào: xác nhận của trưởng ca. Ra: ca ĐÃ XÁC NHẬN |
| UC-03 | Hợp nhất và phát hành báo cáo T+1 | Hệ thống (tự động), Ban điều hành | Gom giao dịch đã xác nhận → gộp theo chi nhánh × dịch vụ × pháp nhân | Còn ca chưa xác nhận: vẫn phát hành, ghi rõ phần thiếu và cảnh báo | Vào: giao dịch đã xác nhận. Ra: báo cáo hợp nhất T+1 |
| UC-04 | Hợp nhất danh tính khách hàng | Khách hàng, Hệ thống | Nhận số điện thoại → chuẩn hoá E.164 → tìm hồ sơ → nối hoặc tạo mới | Nhiều hồ sơ cũ cùng số: gộp và giữ lịch sử; không chắc chắn thì chờ xác nhận tay | Vào: số điện thoại từ 3 kênh. Ra: một hồ sơ duy nhất |

*Bảng 5.1. Bốn nghiệp vụ cốt lõi trong phạm vi đề tài*

**5.2. Yêu cầu chức năng theo module**

| **Module** | **Yêu cầu chức năng** |
|----|----|
| **M1** Tích hợp dữ liệu | FR-01 kết nối 4 nguồn (app gym, đặt sân, nhận diện khuôn mặt, phần mềm quầy) · FR-02 đồng bộ theo lịch có nhật ký và cảnh báo khi thất bại · FR-03 đẩy lại tự động khi nguồn tạm mất kết nối |
| **M2** Chốt ca | FR-04 tính sẵn số liệu ca từ giao dịch đã ghi · FR-05 màn hình xác nhận cho trưởng ca · FR-06 chặn xác nhận khi lệch \> 2% nếu chưa ghi lý do · FR-07 chuyển phê duyệt lên quản lý khu vực |
| **M3** Báo cáo hợp nhất | FR-08 gộp doanh thu theo chi nhánh × dịch vụ × pháp nhân · FR-09 phát hành báo cáo T+1 tự động · FR-10 xuất sổ theo từng hộ kinh doanh từ cùng một nguồn · FR-11 đánh dấu phần dữ liệu còn thiếu |
| **M4** Định danh và khách hàng | FR-12 định danh dùng chung theo chuẩn OIDC · FR-13 chuẩn hoá số điện thoại E.164 làm khoá · FR-14 gộp hồ sơ trùng, giữ lịch sử · FR-15 đối soát thanh toán theo mã đơn hàng do hệ thống sinh |
| **M5** Quản trị và phân quyền | FR-16 quản lý tài khoản theo vòng đời · FR-17 phân quyền theo vai trò (RBAC) · FR-18 nhật ký truy vết mọi thay đổi dữ liệu · FR-19 danh mục dữ liệu cá nhân và thời hạn lưu trữ |

*Bảng 5.2. Mười chín yêu cầu chức năng, nhóm theo năm module*

**5.3. Yêu cầu phi chức năng**

| **Nhóm** | **Yêu cầu** | **Ngưỡng đo được** |
|----|----|----|
| Hiệu năng | Thời gian phản hồi và số phiên đồng thời | API ≤ 500 ms ở phân vị 95; ≥ 60 phiên đồng thời; dựng báo cáo ngày ≤ 5 phút |
| Sẵn sàng | Uptime, sao lưu, khôi phục | Uptime **≥ 99,5%**; sao lưu theo nguyên tắc 3-2-1; **RPO ≤ 4 giờ, RTO ≤ 8 giờ**, diễn tập 2 lần/năm |
| Bảo mật | Xác thực, phân quyền, nhật ký, mã hoá | MFA cho tài khoản đặc quyền; RBAC theo least privilege và separation of duties; nhật ký ≥ 12 tháng, chống sửa/xoá; TLS 1.2+ và mã hoá at-rest |
| Mở rộng | Thêm chi nhánh không phát sinh lao động thủ công | Tới 60 chi nhánh mà không tăng giờ nhập liệu; thêm 1 chi nhánh chỉ là thêm 1 nguồn dữ liệu |
| Tuân thủ | Dữ liệu cá nhân theo Nghị định 13/2023 \[23\] | **100%** dữ liệu sinh trắc học có căn cứ pháp lý và thời hạn lưu trữ được công bố; **không sao chép** dữ liệu sinh trắc học ra khỏi hệ thống nhà cung cấp |
| Vận hành | Phát hiện và xử lý sự cố | **MTTD ≤ 15 phút**; quy trình sự cố 6 bước, phân mức P1–P4; phản hồi P1 ≤ 30 phút |

*Bảng 5.3. Yêu cầu phi chức năng — mỗi yêu cầu có ngưỡng kiểm thử được*

**5.4. Ma trận phân quyền**

Ma trận xây theo ba nguyên tắc: quyền tối thiểu cần thiết, chỉ truy cập
phần thông tin cần cho công việc, và tách nhiệm vụ để không ai nắm toàn
bộ một quy trình quan trọng. Ký hiệu: **X** toàn quyền · **S** sửa ·
**T** tạo · **X.** chỉ xem · **–** không có quyền.

| **Vai trò** | **Giao dịch** | **Chốt ca** | **Báo cáo hợp nhất** | **Hồ sơ khách hàng** | **Danh mục & dữ liệu chủ** | **Tài khoản & quyền** |
|----|----|----|----|----|----|----|
| Thu ngân | T | – | – | X. | – | – |
| Trưởng ca | X. | S (ca của mình) | X. (chi nhánh mình) | X. | – | – |
| Quản lý khu vực | X. | S (phê duyệt lệch) | X. (cụm chi nhánh) | X. | – | – |
| Kế toán hộ kinh doanh | X. | – | X. (pháp nhân mình) | – | – | – |
| Ban điều hành | X. | – | X. (toàn hệ thống) | X. | X. | – |
| Đầu mối CNTT | – | – | X. | – | S | X |

*Bảng 5.4. Ma trận vai trò → quyền. Điểm tách nhiệm vụ quan trọng nhất:
đầu mối CNTT quản trị tài khoản nhưng không sửa được giao dịch, người
làm nghiệp vụ không tự cấp được quyền cho mình*

**6. THIẾT KẾ GIẢI PHÁP (TO-BE) VÀ KIẾN TRÚC TỔNG THỂ**

**6.1. Quy trình TO-BE**

Quy trình TO-BE đã trình bày ở mục 5 của thuyết minh giai đoạn 1 (Hình
5.1 và Bảng 5.1), không lặp lại ở đây. Điểm chi phối toàn bộ thiết kế
dưới đây: bốn khâu thủ công được thay bằng đồng bộ tự động, con người
chỉ giữ **một điểm kiểm soát duy nhất** — trưởng ca xác nhận ca, với
ngưỡng lệch 2% bắt buộc ghi lý do.

**6.2. Kiến trúc hệ thống theo ba lớp**

<img
src="bailam.md/BT Lập kế hoạch giai đoạn 2/media_Phay/media/image1.png"
style="width:4.72441in;height:1.48092in" />

*Hình 6.1. Kiến trúc ba lớp — các nền tảng thuê ngoài giữ nguyên, phần
xây mới nằm ở lớp ứng dụng và lớp dữ liệu*

Lớp trình diễn không xây mới ứng dụng nào cho khách hàng — app hội viên
và web đặt sân giữ nguyên, chỉ thêm màn hình xác nhận ca và trang báo
cáo. Toàn bộ phần xây mới nằm ở lớp ứng dụng, với điểm thiết kế quan
trọng nhất là **cổng API làm điểm vào duy nhất**: năng lực thanh toán và
định danh chỉ xây một lần rồi dùng lại cho mọi kênh, khắc phục đúng điểm
nghẽn B5 của giai đoạn 1. Lớp dữ liệu tách dữ liệu vận hành khỏi dữ liệu
chủ, vì hai loại có chu kỳ thay đổi và chủ sở hữu khác nhau.

**6.3. Tích hợp hệ thống**

| **Hệ thống** | **Giao thức** | **Chiều** | **Tần suất** | **Dữ liệu đồng bộ** |
|----|----|----|----|----|
| Ứng dụng gym (thuê ngoài) | REST qua cổng API | Đọc từ nhà cung cấp | Mỗi 1 giờ | Hồ sơ hội viên, gói tập, nhật ký ra vào. **Không lấy dữ liệu sinh trắc học** |
| Hệ thống đặt sân | REST | Hai chiều | Thời gian thực khi có đơn | Đơn đặt sân, trạng thái thanh toán, mã đơn hàng do hệ thống sinh |
| Phần mềm quầy thu ngân | REST, hoặc tệp CSV nếu không có API | Đọc từ quầy | Cuối mỗi ca và mỗi 15 phút | Giao dịch gaming, billiards, bán tại quầy |
| Nhận diện khuôn mặt | REST | Đọc | Mỗi 1 giờ | Chỉ nhật ký ra vào (thời điểm, mã hội viên); không lấy ảnh hay đặc trưng khuôn mặt |
| Cổng thanh toán / ngân hàng | REST + webhook | Hai chiều | Thời gian thực | Kết quả thanh toán, đối soát theo mã đơn hàng |

*Bảng 6.1. Năm điểm tích hợp. Dự phòng bằng tệp CSV cho phần mềm quầy là
bắt buộc, vì chưa rõ nhà cung cấp có mở API hay không*

**6.4. Thiết kế dữ liệu**

<img
src="bailam.md/BT Lập kế hoạch giai đoạn 2/media_Phay/media/image2.png"
style="width:5.11811in;height:1.23383in" />

*Hình 6.2. Mô hình dữ liệu mức khái niệm — bảng dữ kiện trung tâm là
GIAO DỊCH, vây quanh là các thực thể danh mục*

| **Đối tượng** | **Quy tắc mã hoá và định danh** |
|----|----|
| Chi nhánh | Mã dạng \`CN-\<quận\>-\<số thứ tự\>\`; là **dữ liệu chủ** — mọi hệ thống tham chiếu về đây thay vì tự giữ danh sách riêng, khắc phục tình trạng bốn nguồn công bố bốn con số quy mô khác nhau |
| Khách hàng | **Số điện thoại chuẩn E.164** làm khoá — dữ liệu duy nhất mà cả ba kênh hiện tại đều thu thập |
| Giao dịch | Mã do hệ thống sinh, không do người dùng nhập — khắc phục điểm nghẽn B3 |
| Ca làm việc | Mã \`\<mã chi nhánh\>-\<ngày\>-\<số ca\>\`; gắn trưởng ca xác nhận và trạng thái |
| Pháp nhân | Mã theo mã số thuế hộ kinh doanh \[3\]; mỗi chi nhánh thuộc đúng một pháp nhân, để xuất sổ riêng từ cùng một nguồn |

*Bảng 6.2. Quy tắc chuẩn hoá danh mục và khoá định danh*

**7. KẾ HOẠCH TRIỂN KHAI (WBS) VÀ TIẾN ĐỘ**

| **Pha** | **Công việc chính** | **Sản phẩm bàn giao** | **Thời lượng** | **Chịu trách nhiệm** | **Tiêu chí hoàn thành** |
|----|----|----|----|----|----|
| **1. Khảo sát & phân tích** | Phỏng vấn hiện trạng, kiểm chứng 4 giả định ở Phụ lục A GĐ1, chốt phạm vi | BRD, SRS, danh mục tài sản CNTT | 3 tuần | BA (đối tác) + key user | Ký duyệt SRS; 4 giả định có số thật |
| **2. Thiết kế** | Kiến trúc 3 lớp, lược đồ dữ liệu, ma trận phân quyền, tích hợp | HLD, LLD, ma trận phân quyền được phê duyệt | 3 tuần | Tech lead (đối tác) | Đầu mối CNTT và Ban điều hành ký HLD |
| **3. Phát triển** | M1 và M3 kho dữ liệu, M2 chốt ca, M4 cổng API và định danh, M5 quản trị | Mã nguồn, môi trường kiểm thử, tài liệu triển khai | 10 tuần | Dev (đối tác) | Đủ 19 yêu cầu chức năng; qua kiểm thử nội bộ |
| **4. Kiểm thử** | SIT, kiểm thử tải 60 phiên, UAT với trưởng ca và kế toán | Bộ test case, biên bản SIT và UAT | 3 tuần | QA (đối tác) + key user | Ký nghiệm thu UAT; đạt ngưỡng NFR Bảng 5.3 |
| **5. Triển khai** | Thí điểm **1 chi nhánh đủ 4 dịch vụ**, chạy song song cách cũ, rồi rollout theo cụm | Hệ thống vận hành thật, kế hoạch rollout theo cụm | 4 tuần | PM (đối tác) + quản lý khu vực | Thí điểm 2 tuần không lệch số so với cách cũ; rollout đủ 38+ chi nhánh |
| **6. Vận hành & bảo trì** | Hypercare, bàn giao tài liệu vận hành 6 phần, đào tạo theo vai trò | Bộ tài liệu vận hành, biên bản bàn giao, báo cáo KPI | 3 tuần (rồi chuyển sang bảo trì) | Đối tác vận hành + đầu mối CNTT | Đạt K1, K2 tại T+3 tháng; MTTD ≤ 15 phút |

*Bảng 7.1. Sáu pha, tổng 26 tuần ≈ 6 tháng — khớp đúng khung thời gian
đã chốt ở giai đoạn 1*

**Ánh xạ về roadmap của đồ án.** Sáu pha ở đây chia theo vòng đời phát
triển phần mềm; năm pha Foundation – Core – Migration – Security uplift
– Optimize ở Bước 8 của đồ án chia theo năng lực hạ tầng. Cùng phủ 6
tháng: pha 1–2 ứng Foundation, pha 3 phủ Core và Migration, pha 4–5 phủ
Security uplift, pha 6 ứng Optimize.

**Vì sao bắt buộc chạy song song ở pha 5.** Các chi nhánh hoạt động 24
giờ nên không có cửa sổ dừng hệ thống. Trong 2 tuần thí điểm, chi nhánh
vẫn chốt ca theo cách cũ song song với hệ thống mới, và tiêu chí chuyển
giai đoạn là **hai con số phải khớp nhau** — đây cũng là cách duy nhất
kiểm chứng được rằng dữ liệu mới đáng tin trước khi bỏ cách làm cũ.

**8. NHÂN SỰ, TỔ CHỨC DỰ ÁN VÀ CƠ CHẾ PHỐI HỢP**

**8.1. Cơ cấu tổ chức dự án**

| **Vai trò** | **Thuộc bên** | **Số lượng** | **Mức tham gia** |
|----|----|----|----|
| Sponsor (chủ đầu tư) | Ways Station — Ban điều hành | 1 | Duyệt ngân sách, quyết định chuyển pha |
| Ban chỉ đạo (Steering) | Ways Station + đối tác | 3–4 | Họp tháng, xử lý việc vượt thẩm quyền PM |
| Quản lý dự án (PM) | Đối tác | 1 | Toàn thời gian trong 6 tháng |
| Phân tích nghiệp vụ (BA) | Đối tác | 1 | Toàn thời gian pha 1–2; bán thời gian pha 4 |
| Kiến trúc / Tech lead | Đối tác | 1 | Toàn thời gian pha 2–3 |
| Lập trình viên · Kiểm thử (QA) | Đối tác | 2 + 1 | Dev toàn thời gian pha 3; QA toàn thời gian pha 4 |
| An toàn thông tin · Vận hành | Đơn vị đánh giá độc lập; đối tác vận hành | 1 + 1 | ATTT theo đợt (rà soát thiết kế, đánh giá trước go-live); Ops từ pha 5 |
| **Đầu mối CNTT** | **Ways Station** | **1** | **Cần bố trí mới — hiện chưa có trong cơ cấu**; đối tác kỹ thuật thường trực của bên triển khai |
| Key user | Ways Station | 4–6 | Trưởng ca, quản lý khu vực, kế toán, nhân viên nhập liệu — pha 1, 4, 5 |

*Bảng 8.1. Phần lớn nhân lực đến từ đối tác — hệ quả trực tiếp của việc
doanh nghiệp không có phòng công nghệ thông tin*

**8.2. Ma trận RACI**

Ký hiệu: **R** thực hiện · **A** chịu trách nhiệm cuối · **C** được hỏi
ý kiến · **I** được thông báo.

| **Đầu việc** | **Sponsor** | **PM** | **BA** | **Tech lead** | **Đầu mối CNTT** | **Key user** |
|----|----|----|----|----|----|----|
| Chốt yêu cầu (SRS) | A | C | R | C | C | C |
| Duyệt thiết kế (HLD) | A | C | C | R | C | I |
| Đàm phán truy xuất dữ liệu với nhà cung cấp app gym | A | R | C | C | C | I |
| Chuyển đổi và làm sạch dữ liệu | I | A | C | R | C | C |
| Ký nghiệm thu UAT | A | C | C | I | C | R |
| Quyết định go-live | A | R | I | C | C | C |
| Nhận bàn giao tài liệu vận hành | I | C | I | C | A/R | I |

*Bảng 8.2. RACI cho bảy đầu việc lớn. Việc đàm phán với nhà cung cấp app
gym được đưa vào RACI vì đây là rủi ro R2 — điều kiện tiên quyết của
năng lực N2*

**8.3. Cơ chế làm việc**

> • **Họp và quản lý thay đổi.** Họp tiến độ hằng tuần (PM, đầu mối
> CNTT, trưởng nhóm kỹ thuật), họp Ban chỉ đạo hằng tháng, họp bất
> thường khi có sự cố P1 hoặc điểm kiểm soát chuyển pha không đạt. Mọi
> thay đổi phạm vi phải qua phiếu yêu cầu thay đổi có đánh giá ảnh hưởng
> tiến độ và chi phí; vượt 5% giá trị hợp đồng thì Sponsor duyệt — đây
> là hàng rào chống phình phạm vi.
>
> • **Sự cố, leo thang, theo dõi rủi ro.** Theo quy trình 6 bước và phân
> mức P1–P4: P1 phản hồi trong 30 phút và leo thang trực tiếp tới PM
> cùng đầu mối CNTT, P2 trong 2 giờ, P3 trong 1 ngày làm việc, P4 trong
> 3 ngày làm việc; mọi sự cố phải có bước tổng kết nguyên nhân và biện
> pháp phòng ngừa tái diễn. Vấn đề và rủi ro dùng một sổ theo dõi chung,
> rà soát trong họp tuần; tám rủi ro R1–R8 của giai đoạn 1 vào sổ ngay
> từ ngày đầu, mỗi rủi ro có người theo dõi.

**9. DỰ TOÁN CHI PHÍ VÀ PHƯƠNG ÁN TÀI CHÍNH**

Dự toán dưới đây dùng chung một bộ đơn giá với Bước 7 của đồ án, chỉ
tách theo sáu nhóm chi phí của thuyết minh đề tài thay vì theo nhóm hạng
mục đầu tư. Tổng giá trị vì vậy phải khớp: CAPEX 555 triệu và OPEX
thường xuyên 251,4 triệu mỗi năm.

| **Nhóm chi phí** | **Khoản mục** | **Cách tính** | **CAPEX** | **OPEX/năm** |
|----|----|----|----|----|
| **1. Phần mềm** | Cổng API, định danh, CSDL, giám sát, báo cáo — bản nguồn mở | 0 đồng; nếu chọn Power BI Pro: 14 USD/người/tháng × 10 người \[25\], tỷ giá **26.200 đ/USD** \[27\] | 0 | 0 (hoặc ~44 nếu dùng Power BI) |
| **2. Phát triển** | Nhân công triển khai C1–C7 | **11 man-month** × **45 triệu** (giả định) | **495,0** | – |
| **3. Hạ tầng** | Máy chủ ảo, lưu trữ sao lưu, cân bằng tải, tên miền, SSL | 2,84 triệu/tháng × 12, đơn giá công khai \[19\]\[21\] | 0 | **34,1** |
| **4. Bảo mật & tuân thủ** | Đánh giá ATTT trước go-live và định kỳ hằng năm | 60 triệu/lần (giả định — không ai công bố giá \[24\]) | **60,0** | **60,0** từ năm 2 |
| **5. Đào tạo & chuyển giao** | Đào tạo theo vai trò, bàn giao tài liệu vận hành 6 phần | Trong C7 (0,5 man-month); bổ sung từ năm 2 | trong 495,0 | ~15,0 từ năm 2 |
| **6. Vận hành** | Hỗ trợ, bảo trì sau bàn giao; đầu mối CNTT nội bộ | 15% × 495 = 74,3; đầu mối CNTT 286 × **50%** = 143,0 | 0 | **217,3** |
|  | **Tổng** |  | **555,0** | **251,4** (năm 1) |

*Bảng 9.1. Dự toán theo sáu nhóm chi phí (triệu đồng)*

**Dự phòng.** Cộng **10%** trên tổng dự toán, trong khoảng 5–15% hướng
dẫn cho phép. Chọn mức giữa vì hai khoản trọng yếu còn bất định cao:
đánh giá an toàn thông tin chưa có giá niêm yết, nhân công chưa có báo
giá thật.

**Phương án tài chính và kết luận.** Tổng chi phí sở hữu 3 năm khoảng
**1.715 triệu đồng**, 5 năm khoảng **2.480 triệu đồng** (chi tiết ở Bước
7 của đồ án). Cần nói rõ để tránh kỳ vọng sai: nếu chỉ tính phần tiết
kiệm thành tiền mặt — 96 triệu mỗi năm từ việc không còn cần vị trí nhân
viên nhập liệu — thì đề tài **không hoàn vốn trong 5 năm**. Điểm hoàn
vốn khoảng **năm thứ 4** chỉ đạt được khi tính cả giá trị giờ lao động
của trưởng ca được thu hồi (~371,5 triệu mỗi năm) và phần lợi ích tăng
theo số chi nhánh. Vì vậy cơ sở để phê duyệt đề tài là **giảm rủi ro
pháp lý về dữ liệu cá nhân và tạo năng lực mở rộng chuỗi**, không phải
tiết kiệm chi phí trong ngắn hạn.

**Cách chi.** Chia thanh toán theo bốn mốc nghiệm thu của Bảng 7.1 —
duyệt SRS, duyệt HLD, ký UAT, hoàn thành rollout — thay vì trả trước, để
mỗi lần chi gắn với một sản phẩm bàn giao kiểm chứng được; khoản đánh
giá an toàn thông tin ký với đơn vị độc lập, không dùng chính đối tác
triển khai.

**DANH MỤC NGUỒN**

**\[3\]** [<u>mã số thuế các hộ kinh doanh Ways
Station</u>](https://masothue.com) · **\[19\]** [<u>bảng giá Bizfly
Cloud VPS</u>](https://bizflycloud.vn/cloud-vps) · **\[21\]** [<u>chi
phí Bizfly Simple
Storage</u>](https://docs.bizflycloud.vn/simple_storage/resources/storage-subscription/)
· **\[23\]** [<u>Nghị định
13/2023/NĐ-CP</u>](https://vanban.chinhphu.vn) · **\[24\]** [<u>dịch vụ
đánh giá ATTT
Viettel</u>](https://giaiphapdoanhnghiepviettel.vn/dich-vu-kiem-tra-danh-gia-an-toan-thong-tin-mang-penetration-testing)
· **\[25\]** [<u>bảng giá Power BI
2026</u>](https://costbench.com/software/business-intelligence/power-bi/)
· **\[26\]** [<u>chi phí outsourcing phần mềm Việt Nam
2026</u>](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/)
· **\[27\]** [<u>tỷ giá Vietcombank
09/09/2026</u>](https://webgia.com/ty-gia/vietcombank/) · **\[28\]**
[<u>Chương 6 — Quản trị hệ thống và vận hành hạ tầng
(UIT)</u>](https://www.uit.edu.vn)
