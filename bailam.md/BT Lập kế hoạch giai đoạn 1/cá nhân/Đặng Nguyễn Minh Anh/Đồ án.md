# ĐỒ ÁN MÔN HỌC — LẬP KẾ HOẠCH GIAI ĐOẠN 1

## Đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho hệ sinh thái dịch vụ Ways Station

| | |
|---|---|
| **Đơn vị thụ hưởng** | Chuỗi Ways Station — 34 chi nhánh tại TP.HCM |
| **Lớp năng lực đầu tư** | Lớp 4 — Nền tảng ứng dụng & tích hợp; Lớp 5 — Nền tảng dữ liệu |
| **Lớp 1, 2, 3** | Kế thừa hạ tầng hiện có, không đầu tư mua sắm mới |
| **Thời gian triển khai** | 12 tháng |
| **Chu kỳ thiết kế** | 5 năm |
| **Nội dung giai đoạn 1** | Bước 1 — Khảo sát hiện trạng; Bước 2 — Vấn đề và rủi ro; Bước 3 — Mục tiêu và KPI; Bước 4 — Phương án kiến trúc |

**Nguồn dữ liệu.** Báo cáo sử dụng ba nhóm nguồn: (1) tài liệu nghiệp vụ nội bộ của 8 vị trí vận hành tại chi nhánh mà nhóm tiếp cận được — danh mục tại Phụ lục; (2) nguồn công khai chính chủ của doanh nghiệp gồm website, thông tin chi nhánh và cổng tuyển dụng; (3) nguồn đối chiếu về quy mô và pháp lý. Các chỉ số kỹ thuật định lượng về hiệu năng, sự cố, sao lưu và bảo mật là **số liệu giả lập có kiểm soát**, được xây dựng trên cơ sở quan sát quy trình thực tế và ngưỡng chuẩn ngành, do dữ liệu vận hành thực của doanh nghiệp thuộc diện bảo mật. Nhóm không tiếp cận được tài liệu quy trình của khối văn phòng, nên mô tả hoạt động nội bộ của Phòng Nhân sự, Phòng Điều phối và Bộ phận kho hàng là suy luận từ phạm vi trách nhiệm được công bố.

---

# BƯỚC 1 — KHẢO SÁT HIỆN TRẠNG HẠ TẦNG (AS-IS)

## 1.1. Phạm vi hoạt động của doanh nghiệp

Ways Station vận hành theo mô hình tổ hợp: mỗi chi nhánh gộp nhiều mảng dịch vụ trong cùng một địa điểm.

| # | Mảng dịch vụ | Đặc điểm vận hành |
|---|---|---|
| 1 | **NET** | Phòng máy kết hợp bếp phục vụ tại chỗ và quầy hàng hoá theo bảng giá niêm yết. Có nội quy phòng riêng, cho phép ghép ghế ngủ từ 21h đến 7h. |
| 2 | **BIDA** | Ba loại bàn: bàn lỗ dùng bộ 16 bi; bàn libre dùng bộ 3 bi trơn, duy trì nhiệt độ mặt bàn 37–39 °C; bàn 3C dùng bộ 3 bi có chấm, duy trì 41–43 °C. Tính giá theo khung giờ. Bia và khăn lạnh chỉ phục vụ tại mảng này. |
| 3 | **CẦU LÔNG** | Sân cho thuê, phục vụ trà đá theo định lượng chuẩn và 2 khăn lạnh mỗi bàn. |
| 4 | **GYM** | Check-in bằng nhận diện khuôn mặt, không dùng thẻ hội viên. Hoạt động 24/7, không giới hạn thời gian tập. Bán gói tập theo tháng, có chương trình mua 3 tháng tặng 1 tháng. |
| 5 | **HUB** | Không gian học tập và làm việc. Bán vé theo block 4 tiếng, không bán lẻ, không hoàn tiền. Có hàng bán, 13 loại đồ uống miễn phí và 7 loại thiết bị cho mượn. Có dịch vụ in ấn theo bảng giá. |
| — | **GIỮ XE** | Dịch vụ hỗ trợ đi kèm mọi chi nhánh, dùng thẻ xe, có quy trình xử lý mất thẻ theo ba tình huống giấy tờ. |

Bếp và quầy hàng hoá không phải một mảng dịch vụ độc lập mà là dịch vụ bán kèm nằm trong NET và BIDA, dùng chung một bảng giá niêm yết.

## 1.2. Cơ cấu tổ chức và kênh vận hành

Toàn bộ giao tiếp giữa 34 chi nhánh và hội sở đi qua một tổng đài duy nhất phân nhánh theo phím:

| Kênh | Đơn vị phụ trách | Nghiệp vụ |
|---|---|---|
| Tổng đài — phím 2 | **Phòng Nhân sự** | Tuyển dụng, đào tạo, ký quỹ, cấp phát đồng phục, ghi nhận công, tính lương, đổi vị trí/chi nhánh/ca làm, thôi việc |
| Tổng đài — phím 3 | **Phòng Điều phối** | Lịch làm việc, ca sau chưa tới, học việc, ca làm phát sinh, nghỉ phép, lấy vân tay, chấm công vào/ra |
| Tổng đài — phím 8 | **Bộ phận kho hàng** | Vấn đề kho (hết gas, hết vật tư); hỗ trợ đăng nhập phần mềm quản lý gym và cổng thanh toán ngân hàng |
| Email nhân sự | Phòng Nhân sự | Vấn đề cá nhân, phản ánh |
| Zalo | Quản lý chi nhánh | Nhận ảnh chụp biên bản, xử lý sự vụ tại chỗ |
| Cổng nhân sự nội bộ | Phòng Nhân sự | Hệ thống quản lý nhân sự, nhân viên tự truy cập |

Toàn bộ luồng giao tiếp này chạy trên kênh thoại và tin nhắn, không đi qua hệ thống. Ba hệ quả trực tiếp:

- Mọi yêu cầu hỗ trợ là một cuộc gọi, không sinh ra bản ghi có cấu trúc. Không đếm được, không phân loại được, không đo được thời gian xử lý.
- Không tồn tại hệ thống tiếp nhận yêu cầu. Không có cách truy vấn số sự cố phát sinh trong một kỳ.
- Phòng Điều phối xếp ca cho 34 chi nhánh với đầu vào là các cuộc gọi rời rạc thay vì dữ liệu nhu cầu.

## 1.3. Lớp 1 — Tính toán và kết nối

| Chỉ số | Hiện trạng |
|---|---|
| Máy chủ cục bộ | 1 máy/chi nhánh, tổng 34 máy |
| Mức sử dụng CPU giờ cao điểm | 85–92% |
| RAM | 8–16 GB, mức sử dụng khoảng 78% |
| Tuổi đời thiết bị trung bình | 4,2 năm |
| Tỉ lệ thiết bị hết hạn hỗ trợ | 41% (14/34 chi nhánh) |
| Đường truyền | 1 line/chi nhánh, 100–150 Mbps, không có line dự phòng |
| Kết nối trực tiếp giữa các chi nhánh | Không có |
| Điểm lỗi đơn | 100% chi nhánh |
| Thiết bị đầu cuối đặc thù | Đầu đọc nhận diện khuôn mặt tại gym; máy chấm công vân tay; thiết bị gia nhiệt bàn bida |

Ba ràng buộc thiết kế rút ra cho lớp 4 và lớp 5:

1. Nền tảng mới bắt buộc hoạt động theo mô hình ưu tiên ngoại tuyến tại điểm bán. Mất mạng vẫn phải bán được hàng và tính giờ, đồng bộ bù khi có mạng trở lại.
2. Doanh nghiệp đã có hai kênh sinh dữ liệu sinh trắc — nhận diện khuôn mặt tại gym và vân tay chấm công. Đây là nguồn dấu thời gian check-in chính xác, tự động, hiện chưa được khai thác cho mục đích phân tích.
3. Bàn bida yêu cầu duy trì nhiệt độ theo dải cụ thể, là ứng viên cho giám sát thiết bị ở giai đoạn sau nhưng nằm ngoài phạm vi kỳ này.

## 1.4. Lớp 2 — Vận hành

| Chỉ số | Hiện trạng |
|---|---|
| Hệ thống giám sát tập trung | 0/34 chi nhánh |
| Hệ thống tiếp nhận yêu cầu | Không có; sử dụng tổng đài thoại và Zalo |
| Thời gian trung bình phát hiện sự cố | 4–8 giờ |
| Thời gian trung bình khắc phục | 12–24 giờ |
| Số sự cố ghi nhận trong 6 tháng | 118 sự cố, trung bình 19,7 sự cố/tháng |
| Trong đó gây gián đoạn bán hàng | 22 sự cố, trung bình 3,5 giờ/sự cố |
| Thời gian gián đoạn bán hàng tích luỹ 6 tháng | 77 giờ |
| Cơ chế sao lưu | Thủ công, sao chép tay ra ổ cứng ngoài, không có lịch cố định |
| Tỉ lệ sao lưu thành công | 47% |
| Mục tiêu điểm khôi phục thực tế | Khoảng 24 giờ |
| Mục tiêu thời gian khôi phục thực tế | 4–8 giờ |
| Kế hoạch khôi phục thảm hoạ | Không có, chưa từng diễn tập |
| Bàn giao ca | Sổ giao ca giấy, ghi tay |
| Lưu trữ biên bản sự vụ | Biên bản giấy, bàn giao cho thu ngân, không được huỷ khi chưa có phép quản lý |

## 1.5. Lớp 3 — Bảo mật và định danh

| Chỉ số | Hiện trạng |
|---|---|
| Định danh dùng chung toàn hệ sinh thái | Không có. Hội viên gym không sử dụng được tại net, bida, cầu lông, HUB |
| Quy trình đăng ký hội viên gym | Khách điền phiếu giấy, nhân viên nhập tạo hội viên, sau đó lấy dữ liệu khuôn mặt |
| Xử lý giấy tờ khi khách mất thẻ xe | Chụp ảnh căn cước công dân, cà vẹt xe, biên bản, thân xe, biển số và hình ảnh khách, gửi qua Zalo cho quản lý |
| Tạm giữ giấy tờ khách | Giữ cà vẹt 24 giờ với giấy tờ không chính chủ; giữ xe 36 giờ với trường hợp không có giấy tờ |
| Tỉ lệ tài khoản có xác thực đa yếu tố | 0% |
| Mô hình tài khoản nhân viên | Dùng chung theo ca |
| Giải pháp bảo vệ điểm cuối | 0% |
| Nhật ký tập trung | Không có; nhật ký nằm rải rác trên từng máy, lưu tối đa 7 ngày |
| Lỗ hổng nghiêm trọng chưa vá | 23 lỗ hổng (quét mẫu 5 chi nhánh, suy rộng) |
| Tỉ lệ dữ liệu nhạy cảm được mã hoá | 0% |

Quy trình xử lý mất thẻ xe là quy trình được ban hành chính thức và yêu cầu nhân viên học thuộc. Quy trình này yêu cầu chụp ảnh căn cước công dân và cà vẹt xe của khách rồi gửi qua Zalo cá nhân. Hệ quả là ảnh giấy tờ tuỳ thân của khách hàng đang được lưu trên tài khoản nhắn tin cá nhân của nhân viên vận hành, không mã hoá, không kiểm soát truy cập, không có thời hạn xoá và không thu hồi được khi nhân viên nghỉ việc.

## 1.6. Lớp 4 — Ứng dụng và tích hợp

Danh sách hệ thống đang vận hành song song:

| # | Hệ thống hoặc kênh | Chức năng |
|---|---|---|
| 1 | Phần mềm quản lý phòng máy | Tính giờ, bán hàng tại net |
| 2 | Phần mềm quản lý bida | Tính giờ theo khung giờ và theo loại bàn |
| 3 | Phần mềm đặt sân cầu lông | Đặt sân, tính giờ |
| 4 | Phần mềm quản lý gym | Hội viên, gói tập, nhận diện khuôn mặt |
| 5 | Hệ thống vé HUB | Bán và quản lý vé 4 tiếng |
| 6 | Cổng thanh toán ngân hàng | Đối soát giao dịch chuyển khoản |
| 7 | Hệ thống quản lý nhân sự nội bộ | Công, lương, thông tin nhân viên |
| 8 | Máy chấm công vân tay | Ghi nhận vào ca và ra ca |
| 9 | Zalo | Gửi biên bản, ảnh giấy tờ, xử lý sự vụ |
| 10 | Tổng đài thoại phân nhánh | Toàn bộ yêu cầu hỗ trợ từ chi nhánh |
| 11 | Sổ giao ca giấy và biên bản giấy | Bàn giao ca, ghi nhận sự vụ |
| 12 | Excel | Tổng hợp báo cáo |

| Chỉ số | Hiện trạng |
|---|---|
| Số hệ thống phần mềm độc lập | 8 hệ thống, cộng 3 kênh thủ công |
| Cổng giao tiếp ứng dụng | Không có |
| Số luồng tích hợp tự động giữa các hệ thống | 0 |
| Tỉ lệ nghiệp vụ liên hệ thống xử lý thủ công | 100% |
| Mức độ ảo hoá và container hoá | 0% |
| Cơ chế tích hợp liên tục và triển khai liên tục | Không có; cập nhật phần mềm bằng cách sao chép tay tới từng chi nhánh |
| Thời gian đưa một chi nhánh mới vào hệ thống | 3–4 tuần |
| Nghiệp vụ đang chạy trên giấy hoặc Zalo | Bàn giao ca, biên bản sự vụ, biên bản mất thẻ xe, phiếu đăng ký hội viên, báo hết vật tư, xin ca phát sinh |

## 1.7. Lớp 5 — Dữ liệu

| Chỉ số | Hiện trạng |
|---|---|
| Số cơ sở dữ liệu độc lập | 34, mỗi chi nhánh một cơ sở dữ liệu |
| Kho dữ liệu tập trung | Không có |
| Quy trình thu thập và chuyển đổi dữ liệu tự động | Không có |
| Cách lập báo cáo ngày, tuần, tháng | Thủ công bằng Excel, dựa trên ảnh chụp và tin nhắn Zalo |
| Giờ công tổng hợp báo cáo | 2 nhân sự × 4 giờ/ngày × 26 ngày = 208 giờ/tháng, tương đương 2.496 giờ/năm |
| Độ trễ dữ liệu phục vụ ra quyết định | 24–48 giờ |
| Tỉ lệ sai lệch số liệu doanh thu khi đối soát | 3,8% |
| Quản trị danh mục hàng hoá | Bảng giá đã thống nhất giữa net, bida và HUB, có ngoại lệ theo mảng: bia chỉ bán tại bida, khăn lạnh miễn phí chỉ tại bida |
| Quy tắc tính giá món | Có công thức rõ ràng nhưng áp dụng bằng trí nhớ nhân viên tại quầy |
| Định mức nguyên vật liệu | Có định lượng chi tiết theo từng món và từng loại đồ uống |
| Đối chiếu định mức với tiêu hao thực tế | Không có hệ thống |
| Theo dõi hàng cho mượn tại HUB | 7 loại thiết bị, không có hệ thống ghi nhận mượn và trả |
| Theo dõi hàng miễn phí tại HUB | 13 loại đồ uống, không có hệ thống ghi nhận tiêu thụ |
| Chuẩn hoá danh mục dịch vụ giữa các chi nhánh | Chưa chuẩn hoá; cùng một dịch vụ được đặt tên khác nhau giữa các chi nhánh |
| Quản trị dữ liệu, danh mục dữ liệu, chất lượng dữ liệu | Không có |
| Khả năng truy vết nguồn gốc dữ liệu | Không có |

Doanh nghiệp đã có sẵn định mức nguyên vật liệu chuẩn hoá tới từng đơn vị nhỏ nhất. Tuy nhiên định mức này chỉ tồn tại dưới dạng tài liệu để nhân viên học thuộc, không được số hoá, nên không thể đối chiếu giữa lượng nguyên liệu lẽ ra phải tiêu hao theo định mức và lượng thực tế xuất kho. Doanh nghiệp có đủ cơ sở để kiểm soát hao hụt nhưng không có công cụ thực hiện việc kiểm soát đó.

## 1.8. Chỉ số tăng trưởng

| Chỉ số | 24 tháng trước | Hiện tại | Mức tăng |
|---|---|---|---|
| Số chi nhánh | 22 | 34 | +54,5% |
| Số mảng dịch vụ | 3 | 5, cộng dịch vụ giữ xe | +67% |
| Số hội viên | khoảng 12.000 | khoảng 41.000 | +242% |
| Giao dịch mỗi ngày toàn chuỗi | khoảng 2.900 | khoảng 6.800 | +134% |

Khối lượng dữ liệu và giao dịch tăng gấp hai đến ba lần trong khi năng lực xử lý dữ liệu không thay đổi. Khoảng cách này tiếp tục giãn ra theo tốc độ mở rộng chi nhánh.

## 1.9. Tổng hợp điểm nghẽn đã định lượng

| Mã | Điểm nghẽn | Số liệu | Lớp liên quan |
|---|---|---|---|
| P1 | Dữ liệu phân mảnh, không hợp nhất được | 34 cơ sở dữ liệu, 8 hệ thống, 0 luồng tích hợp | 4, 5 |
| P2 | Báo cáo thủ công tiêu tốn giờ công | 2.496 giờ/năm | 5 |
| P3 | Ra quyết định trên dữ liệu cũ | Độ trễ 24–48 giờ | 5 |
| P4 | Số liệu không đáng tin cậy | Sai lệch 3,8% khi đối soát | 5 |
| P5 | Yêu cầu hỗ trợ không sinh bản ghi | 100% qua thoại và Zalo | 4 |
| P6 | Nguy cơ mất dữ liệu | Sao lưu thành công 47%, điểm khôi phục 24 giờ, không có kế hoạch thảm hoạ | 2, 5 |
| P7 | Định danh rời rạc | Hội viên gym không dùng được tại 4 mảng còn lại | 4 |
| P8 | Mở rộng chậm | 3–4 tuần cho mỗi chi nhánh mới | 4 |
| P9 | Dữ liệu cá nhân lưu sai cách | Ảnh giấy tờ khách gửi qua Zalo theo quy trình chính thức | 3, 5 |
| P10 | Có định mức nhưng không kiểm soát được hao hụt | Định mức chi tiết, không số hoá, không đối chiếu được | 5 |
| P11 | Tài sản cho mượn không được theo dõi | 7 loại thiết bị tại HUB, không có hệ thống mượn trả | 5 |

## 1.10. Sơ đồ kiến trúc hiện trạng

```
   [Chi nhánh 1]      [Chi nhánh 2]   ...   [Chi nhánh 34]
        |                   |                     |
   1 server / 1 line   1 server / 1 line    1 server / 1 line
        (không có kết nối ngang giữa các chi nhánh)
        |
   ┌────┴──────────────────────────────────────────┐
   │  8 HỆ THỐNG RỜI RẠC, KHÔNG TRAO ĐỔI DỮ LIỆU:  │
   │   net · bida · cầu lông · gym · vé HUB ·      │
   │   nhân sự · chấm công vân tay ·               │
   │   cổng thanh toán ngân hàng                   │
   └────┬──────────────────────────────────────────┘
        |
   ┌────┴────────────────────────────────────┐
   │  3 KÊNH THỦ CÔNG BẮC CẦU GIỮA CHÚNG:    │
   │   · Tổng đài thoại (phím 2 / 3 / 8)     │
   │   · Zalo (biên bản, ảnh giấy tờ, sự vụ) │
   │   · Sổ giao ca giấy + biên bản giấy     │
   └────┬────────────────────────────────────┘
        |
        ▼
   [2 nhân sự tổng hợp Excel thủ công]
        208 giờ/tháng · sai lệch 3,8%
        |
        ▼
   [Hội sở: Nhân sự · Điều phối · Kho hàng]
        nhận số liệu trễ 24–48 giờ
```

Con người và tổng đài đang đóng vai trò lớp tích hợp của hệ thống.

---

# BƯỚC 2 — VẤN ĐỀ VÀ RỦI RO NẾU KHÔNG ĐẦU TƯ

## 2.1. Tác động vận hành

Yêu cầu hỗ trợ đi qua kênh thoại nên không sinh bản ghi; không có bản ghi nên không có giám sát; không có giám sát nên thời gian phát hiện sự cố kéo dài 4–8 giờ và thời gian khắc phục kéo dài 12–24 giờ. Mỗi sự cố chiếm gần trọn một ca kinh doanh trước khi được xử lý.

| Hệ quả | Cơ sở tính | Thiệt hại quy đổi mỗi năm |
|---|---|---|
| Gián đoạn bán hàng | 154 giờ/năm × doanh thu trung bình 1,2 triệu đồng/giờ/chi nhánh | Khoảng 185 triệu đồng |
| Giờ công tổng hợp báo cáo thủ công | 2.496 giờ/năm × 45.000 đồng/giờ | Khoảng 112 triệu đồng |
| Hao hụt nguyên liệu không kiểm soát được | 9% giá trị nguyên liệu tươi mỗi tháng | Khoảng 96 triệu đồng |
| Thất thoát thiết bị cho mượn tại HUB | Khoảng 4% số lượt mượn không thu hồi được | Khoảng 38 triệu đồng |
| Sai lệch số liệu khi đối soát | 3,8% doanh thu đối soát | Thất thoát cộng chi phí truy tìm nguyên nhân |

Toàn bộ các khoản trên tăng tuyến tính theo số chi nhánh. Với tốc độ mở rộng 54,5% trong 24 tháng, chi phí vận hành ẩn sẽ vượt 500 triệu đồng mỗi năm trong hai năm tới mà không tạo thêm bất kỳ năng lực mới nào.

## 2.2. Tác động tuân thủ và an ninh

| Vấn đề | Hiện trạng | Rủi ro nếu xảy ra |
|---|---|---|
| Ảnh giấy tờ tuỳ thân của khách lưu trên Zalo cá nhân của nhân viên | Theo quy trình xử lý mất thẻ xe đang ban hành | Không xác định được dữ liệu cá nhân đang nằm ở đâu; nhân viên nghỉ việc mang theo dữ liệu; không có cơ chế xoá; không đáp ứng được yêu cầu chứng minh khi bị thanh tra |
| Giấy tờ tuỳ thân được tạm giữ vật lý | Cà vẹt 24 giờ, xe 36 giờ | Không có sổ theo dõi điện tử, phát sinh tranh chấp khi mất mát, không truy được người giữ và thời điểm giữ |
| Biên bản giấy là bản gốc duy nhất | Không có bản sao số | Mất biên bản là mất toàn bộ chứng cứ |
| Dữ liệu sinh trắc học | Nhận diện khuôn mặt tại gym, vân tay chấm công | Đây là dữ liệu cá nhân nhạy cảm, yêu cầu mức bảo vệ cao hơn dữ liệu thông thường; hiện chưa có chính sách lưu trữ và bảo vệ rõ ràng |
| Không có nhật ký tập trung, nhật ký lưu tối đa 7 ngày | Nhật ký rải rác trên từng máy | Khi xảy ra rò rỉ, không chứng minh được phạm vi ảnh hưởng |
| Tài khoản dùng chung theo ca, không có xác thực đa yếu tố | 0% tài khoản được bảo vệ | Không quy trách nhiệm cá nhân khi phát sinh gian lận nội bộ |

Khung pháp lý cần đối chiếu gồm Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân và các quy định hiện hành về an toàn thông tin. Nghĩa vụ cốt lõi là doanh nghiệp phải trả lời được ba câu hỏi: dữ liệu cá nhân đang nằm ở đâu, ai được truy cập, lưu trong bao lâu. Với 34 ốc đảo dữ liệu cộng với ảnh giấy tờ nằm trên Zalo cá nhân của hàng trăm nhân viên vận hành, Ways Station hiện không trả lời được câu nào.

## 2.3. Tác động chiến lược

| Mục tiêu kinh doanh | Rào cản hạ tầng | Hệ quả |
|---|---|---|
| Mở thêm chi nhánh | 3–4 tuần để đưa một chi nhánh vào hệ thống | Hạ tầng ghìm tốc độ mở rộng, chi phí mở rộng tăng theo số chi nhánh |
| Bổ sung mảng dịch vụ mới | Phải tích hợp thủ công vào 8 hệ thống rời rạc | Thời gian đưa dịch vụ ra thị trường kéo dài |
| Hội viên xuyên dịch vụ, một tài khoản dùng chung cả 5 mảng | Gym có hội viên riêng theo khuôn mặt, HUB bán vé riêng, ba mảng còn lại tính tiền theo lượt | Không triển khai được, mất đòn bẩy giữ chân khách lớn nhất của mô hình tổ hợp |
| Bán chéo giữa các mảng trong cùng chi nhánh | Không nhận diện được khách gym có phải khách net hay không | Không đo được giá trị vòng đời khách hàng |
| Ứng dụng phân tích và dự báo | Không có kho dữ liệu, dữ liệu chưa chuẩn hoá | Không có dữ liệu đầu vào, mọi dự án phân tích về sau bị chặn từ đầu |

Mô hình kinh doanh của Ways Station là tổ hợp đa dịch vụ trong cùng một địa điểm, và giá trị cốt lõi của mô hình đó nằm ở việc một khách hàng sử dụng nhiều dịch vụ. Hạ tầng hiện tại không nhìn thấy được điều đó, vì mỗi mảng ghi nhận khách riêng và không nối được với nhau. Doanh nghiệp đang vận hành mô hình tổ hợp trên một hạ tầng chỉ hỗ trợ được mô hình đơn lẻ. Đây chính là khoảng cách mà đầu tư lớp 4 và lớp 5 lấp vào.

## 2.4. Bảng đăng ký rủi ro

| Mã | Rủi ro nếu không đầu tư | Khả năng | Ảnh hưởng | Mức | Chi phí ước tính | Biện pháp kiểm soát |
|---|---|---|---|---|---|---|
| R1 | Rò rỉ dữ liệu cá nhân từ ảnh giấy tờ lưu trên Zalo | Cao | Rất cao | Nghiêm trọng | Xử phạt cộng tổn thất thương hiệu | Định danh tập trung, số hoá và mã hoá biên bản (Lớp 4) |
| R2 | Mất dữ liệu giao dịch một ngày do sao lưu thất bại | Cao | Cao | Nghiêm trọng | 15–40 triệu đồng mỗi lần | Kho dữ liệu tập trung, sao lưu tự động (Lớp 5) |
| R3 | Gián đoạn bán hàng kéo dài do phát hiện sự cố chậm | Cao | Trung bình | Cao | Khoảng 185 triệu đồng/năm | Giám sát nền tảng mới, tự phục hồi (Lớp 4) |
| R4 | Quyết định sai do số liệu trễ và sai lệch | Cao | Cao | Cao | Doanh thu cơ hội | Thu thập dữ liệu tự động, độ trễ tối đa 15 phút (Lớp 5) |
| R5 | Chi phí vận hành tăng tuyến tính theo số chi nhánh | Rất cao | Trung bình | Cao | Khoảng 112 triệu đồng/năm và tăng dần | Tự động hoá toàn bộ báo cáo (Lớp 5) |
| R6 | Không triển khai được hội viên xuyên dịch vụ | Rất cao | Cao | Cao | Mất cơ hội chiến lược | Định danh tập trung (Lớp 4) |
| R7 | Hao hụt nguyên liệu và thất thoát thiết bị không phát hiện được | Cao | Trung bình | Cao | Khoảng 134 triệu đồng/năm | Quản trị dữ liệu, đối chiếu định mức (Lớp 5) |
| R8 | Onboard chi nhánh mới bị nghẽn | Cao | Trung bình | Trung bình | Chậm 3–4 tuần mỗi chi nhánh | Cổng giao tiếp ứng dụng, mẫu onboard chuẩn (Lớp 4) |

## 2.5. Đối chiếu chi phí đầu tư và thiệt hại tránh được

| Khoản mục | Giá trị |
|---|---|
| Thiệt hại định lượng được hiện nay | Khoảng 431 triệu đồng mỗi năm (185 triệu gián đoạn, 112 triệu giờ công, 96 triệu hao hụt nguyên liệu, 38 triệu thất thoát thiết bị) |
| Thiệt hại chưa định lượng được | Sai lệch số liệu, quyết định sai, rủi ro pháp lý về dữ liệu cá nhân, cơ hội chiến lược bị mất |
| Xu hướng nếu không đầu tư | Tăng tuyến tính theo số chi nhánh |

Dự toán đầu tư đầy đủ được xây dựng ở Bước 7 về chi phí đầu tư ban đầu, chi phí vận hành và tổng chi phí sở hữu.

---

# BƯỚC 3 — MỤC TIÊU VÀ KPI HẠ TẦNG

## 3.1. Mục tiêu tổng quát

Xây dựng nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung, biến 34 chi nhánh đang vận hành như 34 hệ thống độc lập thành một hệ thống thống nhất về giao tiếp, về định danh và về dữ liệu; thay thế ba kênh thủ công gồm tổng đài thoại, Zalo và sổ giấy bằng luồng dữ liệu có cấu trúc; qua đó cho phép Ways Station khai thác đúng giá trị của mô hình tổ hợp đa dịch vụ và mở rộng quy mô mà không tăng tuyến tính chi phí vận hành.

## 3.2. Mục tiêu cụ thể

### Lớp 4 — Nền tảng ứng dụng và tích hợp

| Mã | Mục tiêu | Điểm nghẽn xử lý |
|---|---|---|
| MT1 | Hợp nhất giao tiếp giữa 8 hệ thống hiện hữu thông qua cổng giao tiếp ứng dụng và hàng đợi thông điệp; số hoá ba kênh thủ công thành luồng dữ liệu có cấu trúc | P1, P5, P8 |
| MT2 | Đảm bảo nền tảng tích hợp đạt độ sẵn sàng và hiệu năng mức doanh nghiệp, tự phát hiện và tự phục hồi khi có lỗi thành phần | P5 |
| MT3 | Thiết lập định danh tập trung: một tài khoản khách hàng dùng chung cả năm mảng dịch vụ; tài khoản nhân viên định danh theo cá nhân; chấm dứt việc lưu ảnh giấy tờ khách trên kênh nhắn tin cá nhân | P7, P9 |
| MT4 | Rút ngắn thời gian đưa chi nhánh mới hoặc mảng dịch vụ mới vào hệ thống | P8 |

### Lớp 5 — Nền tảng dữ liệu

| Mã | Mục tiêu | Điểm nghẽn xử lý |
|---|---|---|
| MT5 | Xây dựng kho dữ liệu tập trung thu thập tự động dữ liệu giao dịch, vận hành và hội viên từ toàn bộ 34 chi nhánh và cả năm mảng dịch vụ | P1, P6 |
| MT6 | Giảm độ trễ dữ liệu phục vụ ra quyết định từ mức ngày xuống mức phút | P3 |
| MT7 | Tự động hoá toàn bộ báo cáo vận hành ngày, tuần, tháng, loại bỏ khâu tổng hợp Excel thủ công | P2 |
| MT8 | Thiết lập quản trị dữ liệu: số hoá bảng giá và định mức nguyên vật liệu để đối chiếu được hao hụt; số hoá theo dõi thiết bị cho mượn; chuẩn hoá danh mục dùng chung; truy vết được nguồn gốc số liệu | P4, P10, P11 |

Các chỉ số về khôi phục dữ liệu, giám sát và mã hoá được đưa vào bộ KPI phi chức năng của chính nền tảng lớp 4 và lớp 5, với phạm vi đo giới hạn trong nền tảng mới, không mở rộng ra hạ tầng lớp 1 đến lớp 3 vốn nằm ngoài phạm vi đầu tư.

## 3.3. Bảng KPI — Lớp 4

| Mã | Mục tiêu | Chỉ số | Hiện trạng | Cam kết | Thời điểm đo | Căn cứ nghiệm thu | Chịu trách nhiệm |
|---|---|---|---|---|---|---|---|
| KPI1.1 | MT1 | Số luồng tích hợp tự động giữa các hệ thống | 0 | Tối thiểu 12 luồng, phủ tối thiểu 6/8 hệ thống | Sau vận hành 3 tháng | Danh sách giao diện đã công bố trên cổng giao tiếp, kèm biên bản kiểm thử tích hợp | Trưởng nhóm kỹ thuật |
| KPI1.2 | MT1 | Tỉ lệ nghiệp vụ liên hệ thống còn đối chiếu thủ công | 100% | Tối đa 5% | Sau vận hành 3 tháng | Đối chiếu quy trình vận hành trước và sau | Chủ sở hữu ứng dụng |
| KPI1.3 | MT1 | Tỉ lệ biên bản sự vụ lập trên hệ thống thay vì giấy và Zalo | 0% | 100% | Sau vận hành 4 tháng | Truy vấn số biên bản điện tử trên tổng số sự vụ | Chủ sở hữu ứng dụng |
| KPI1.4 | MT1 | Tỉ lệ yêu cầu hỗ trợ sinh ra bản ghi có cấu trúc | 0% | Tối thiểu 90% | Sau vận hành 6 tháng | Nhật ký hệ thống tiếp nhận yêu cầu | Chủ sở hữu ứng dụng |
| KPI1.5 | MT1 | Tỉ lệ bàn giao ca thực hiện trên hệ thống thay vì sổ giấy | 0% | 100% | Sau vận hành 4 tháng | Truy vấn bản ghi bàn giao ca | Trưởng bộ phận vận hành |
| KPI2.1 | MT2 | Độ sẵn sàng của cổng giao tiếp ứng dụng và dịch vụ định danh | Không xác định | Tối thiểu 99,9% mỗi tháng | Hàng tháng từ tháng thứ 2 | Báo cáo độ sẵn sàng từ nhà cung cấp nền tảng và hệ thống giám sát nội bộ | Trưởng nhóm hạ tầng |
| KPI2.2 | MT2 | Thời gian phản hồi giao diện lập trình, phân vị 95 | Chưa có | Dưới 200 mili giây | Sau vận hành 1 tháng | Báo cáo hiệu năng từ cổng giao tiếp | Trưởng nhóm hạ tầng |
| KPI2.3 | MT2 | Thời gian tự phục hồi khi một thành phần nền tảng lỗi | 12–24 giờ | Dưới 15 phút, tự động | Diễn tập theo quý | Nhật ký nền tảng điều phối ghi nhận thời điểm khởi tạo lại thành phần lỗi | Trưởng nhóm hạ tầng |
| KPI2.4 | MT2 | Thời gian phát hiện sự cố trên nền tảng mới | 4–8 giờ | Dưới 5 phút | Sau vận hành 1 tháng | Hệ thống cảnh báo ghi nhận thời điểm phát cảnh báo | Trưởng nhóm hạ tầng |
| KPI3.1 | MT3 | Tỉ lệ khách hàng dùng một tài khoản cho tối thiểu hai mảng dịch vụ | 0% | Tối thiểu 60% hội viên hoạt động | Sau vận hành 6 tháng | Truy vấn hệ thống định danh | Chủ sở hữu ứng dụng |
| KPI3.2 | MT3 | Số mảng dịch vụ đã tích hợp vào định danh chung | 0/5 | 5/5 | Sau vận hành 6 tháng | Biên bản tích hợp từng mảng | Trưởng nhóm kỹ thuật |
| KPI3.3 | MT3 | Tỉ lệ tài khoản nhân viên định danh theo cá nhân | 0% | 100% | Sau vận hành 3 tháng | Rà soát danh sách tài khoản trên hệ thống định danh | Trưởng nhóm bảo mật |
| KPI3.4 | MT3 | Tỉ lệ tài khoản đặc quyền có xác thực đa yếu tố | 0% | 100% | Sau vận hành 3 tháng | Cấu hình chính sách và báo cáo tuân thủ | Trưởng nhóm bảo mật |
| KPI3.5 | MT3 | Tỉ lệ ảnh giấy tờ khách hàng lưu trên hệ thống có kiểm soát truy cập | 0% | 100% | Sau vận hành 4 tháng | Rà soát quy trình mất thẻ xe phiên bản mới và kiểm tra hệ thống lưu trữ | Trưởng nhóm bảo mật |
| KPI4.1 | MT4 | Thời gian đưa một chi nhánh mới vào hệ thống | 3–4 tuần | Tối đa 2 ngày làm việc | Chi nhánh mới đầu tiên sau vận hành | Biên bản onboard có mốc thời gian | Quản lý dự án |
| KPI4.2 | MT4 | Thời gian tích hợp một mảng dịch vụ mới | 3–4 tuần | Tối đa 5 ngày làm việc | Khi phát sinh | Biên bản tích hợp | Trưởng nhóm kỹ thuật |

## 3.4. Bảng KPI — Lớp 5

| Mã | Mục tiêu | Chỉ số | Hiện trạng | Cam kết | Thời điểm đo | Căn cứ nghiệm thu | Chịu trách nhiệm |
|---|---|---|---|---|---|---|---|
| KPI5.1 | MT5 | Số chi nhánh có dữ liệu chảy tự động về kho dữ liệu | 0/34 | 34/34 | Sau vận hành 6 tháng, triển khai cuốn chiếu | Bảng theo dõi trạng thái thu thập theo chi nhánh | Chủ sở hữu dữ liệu |
| KPI5.2 | MT5 | Số mảng dịch vụ có dữ liệu trong kho | 0/5 | 5/5 | Sau vận hành 6 tháng | Kiểm tra bảng dữ liệu theo mảng | Chủ sở hữu dữ liệu |
| KPI5.3 | MT5 | Tỉ lệ chạy thu thập dữ liệu thành công | Chưa có | Tối thiểu 99% mỗi tháng | Hàng tháng | Nhật ký điều phối luồng dữ liệu | Chủ sở hữu dữ liệu |
| KPI5.4 | MT5 | Mục tiêu điểm khôi phục của kho dữ liệu tập trung | Khoảng 24 giờ | Tối đa 15 phút | Diễn tập 6 tháng một lần | Biên bản diễn tập khôi phục | Chủ sở hữu dữ liệu |
| KPI5.5 | MT5 | Mục tiêu thời gian khôi phục của kho dữ liệu tập trung | 4–8 giờ | Tối đa 4 giờ | Diễn tập 6 tháng một lần | Biên bản diễn tập khôi phục | Chủ sở hữu dữ liệu |
| KPI6.1 | MT6 | Độ trễ dữ liệu doanh thu từ lúc phát sinh giao dịch tới lúc hiển thị | 24–48 giờ | Tối đa 15 phút | Sau vận hành 3 tháng, đo liên tục | Đối soát dấu thời gian giữa giao dịch tại chi nhánh và bản ghi trong kho dữ liệu | Chủ sở hữu dữ liệu |
| KPI6.2 | MT6 | Độ trễ dữ liệu tỉ lệ lấp đầy theo khung giờ | Không có | Tối đa 15 phút | Sau vận hành 3 tháng | Đối soát dấu thời gian | Chủ sở hữu dữ liệu |
| KPI7.1 | MT7 | Tỉ lệ báo cáo ngày, tuần, tháng được sinh tự động | 0% | 100% | Sau vận hành 6 tháng | Danh mục báo cáo và lịch chạy tự động | Chủ sở hữu dữ liệu |
| KPI7.2 | MT7 | Giờ công tổng hợp báo cáo thủ công | 208 giờ mỗi tháng | Tối đa 10 giờ mỗi tháng | Sau vận hành 6 tháng | Đối chiếu bảng chấm công trước và sau | Trưởng bộ phận vận hành |
| KPI8.1 | MT8 | Tỉ lệ danh mục hàng hoá và bảng giá được số hoá, dùng chung toàn chuỗi | Chưa số hoá | 100% | Sau vận hành 4 tháng | Đối chiếu danh mục hệ thống với bảng giá ban hành | Chủ sở hữu dữ liệu |
| KPI8.2 | MT8 | Tỉ lệ định mức nguyên vật liệu được số hoá và đối chiếu tự động với xuất kho thực tế | 0% | 100% các món có định mức | Sau vận hành 5 tháng | Báo cáo đối chiếu định mức và thực tế hàng tháng | Chủ sở hữu dữ liệu và Bộ phận kho hàng |
| KPI8.3 | MT8 | Tỉ lệ thiết bị cho mượn tại HUB có bản ghi mượn và trả trên hệ thống | 0% | 100%, đủ 7 loại | Sau vận hành 4 tháng | Truy vấn bản ghi mượn và trả | Chủ sở hữu dữ liệu |
| KPI8.4 | MT8 | Tỉ lệ sai lệch doanh thu khi đối soát | 3,8% | Tối đa 0,5% | Đối soát hàng tháng từ tháng thứ 3 | Biên bản đối soát doanh thu định kỳ | Kế toán chuỗi và Chủ sở hữu dữ liệu |
| KPI8.5 | MT8 | Tỉ lệ bảng dữ liệu cốt lõi có chủ sở hữu, mô tả và truy vết nguồn gốc | 0% | 100% | Sau vận hành 6 tháng | Rà soát danh mục dữ liệu | Chủ sở hữu dữ liệu |
| KPI8.6 | MT8 | Tỉ lệ dữ liệu cá nhân nhạy cảm được mã hoá khi lưu trữ và khi truyền tải trong nền tảng mới | 0% | 100% | Sau vận hành 3 tháng | Rà soát cấu hình mã hoá và biên bản kiểm tra | Trưởng nhóm bảo mật |

## 3.5. Ma trận truy vết

| Điểm nghẽn | Rủi ro | Mục tiêu | KPI đại diện | Lớp |
|---|---|---|---|---|
| P1 Dữ liệu phân mảnh | R2, R4 | MT1, MT5 | KPI1.1, KPI5.1 | 4, 5 |
| P2 Báo cáo thủ công | R5 | MT7 | KPI7.2 | 5 |
| P3 Dữ liệu trễ | R4 | MT6 | KPI6.1 | 5 |
| P4 Sai lệch số liệu | R4 | MT8 | KPI8.4 | 5 |
| P5 Yêu cầu hỗ trợ không sinh bản ghi | R3 | MT1, MT2 | KPI1.4, KPI2.4 | 4 |
| P6 Nguy cơ mất dữ liệu | R2 | MT5 | KPI5.4, KPI5.5 | 5 |
| P7 Định danh rời rạc | R6 | MT3 | KPI3.1, KPI3.2 | 4 |
| P8 Onboard chậm | R8 | MT4 | KPI4.1 | 4 |
| P9 Ảnh giấy tờ lưu trên Zalo | R1 | MT3 | KPI3.5 | 4 |
| P10 Không kiểm soát được hao hụt | R7 | MT8 | KPI8.2 | 5 |
| P11 Thiết bị cho mượn không theo dõi | R7 | MT8 | KPI8.3 | 5 |

Toàn bộ 11 điểm nghẽn đều có mục tiêu xử lý; toàn bộ 8 mục tiêu đều có KPI đo lường; không có mục tiêu nào nằm ngoài phạm vi lớp 4 và lớp 5 đã xác lập.

---

# BƯỚC 4 — PHƯƠNG ÁN KIẾN TRÚC MỤC TIÊU

## 4.1. Kịch bản A — Nâng cấp hạ tầng tại chỗ tập trung

Dựng một trung tâm dữ liệu quy mô nhỏ tại chi nhánh trung tâm, toàn bộ nền tảng lớp 4 và lớp 5 chạy trên phần cứng do doanh nghiệp sở hữu.

| Lớp | Thành phần |
|---|---|
| Tính toán và kết nối | Mua mới 4–6 máy chủ vật lý, thiết bị lưu trữ dùng chung, thiết bị chuyển mạch; thuê thêm đường truyền dành riêng tới chi nhánh trung tâm |
| Vận hành | Hệ thống giám sát tự triển khai, tự quản trị bản vá |
| Bảo mật và định danh | Hệ thống định danh tự vận hành, tự quản lý khoá mã hoá |
| Ứng dụng và tích hợp | Ảo hoá và cụm điều phối container tự dựng, cổng giao tiếp ứng dụng tự vận hành |
| Dữ liệu | Kho dữ liệu tự dựng trên phần cứng nội bộ |

Về khả năng sẵn sàng cao và khôi phục thảm hoạ, kịch bản này chỉ đạt mô hình chủ động — dự phòng trong cùng một địa điểm. Muốn có khả năng khôi phục thảm hoạ thực sự phải đầu tư địa điểm thứ hai, chi phí nhân đôi. Về khả năng mở rộng, mỗi lần mở rộng phải qua chu kỳ mua sắm phần cứng 6–10 tuần, không đạt được cam kết đưa chi nhánh mới vào hệ thống trong 2 ngày. Kịch bản này cũng mâu thuẫn với phạm vi đầu tư đã xác lập là không mua sắm phần cứng mới.

## 4.2. Kịch bản B — Kiến trúc lai

Lõi nền tảng gồm cổng giao tiếp ứng dụng, hệ thống định danh, hàng đợi thông điệp và kho dữ liệu đặt trên nền tảng đám mây. Tại mỗi chi nhánh chỉ cài một thành phần thu thập nhẹ chạy trên máy chủ sẵn có. Phần mềm bán hàng và tính giờ vẫn chạy cục bộ theo mô hình ưu tiên ngoại tuyến.

| Lớp | Thành phần |
|---|---|
| Tính toán và kết nối | Kế thừa nguyên trạng máy chủ và đường truyền chi nhánh; lõi thuê tài nguyên theo mức sử dụng |
| Vận hành | Giám sát tập trung cho lõi nền tảng; chi nhánh gửi tín hiệu tình trạng định kỳ |
| Bảo mật và định danh | Dịch vụ định danh quản trị sẵn với đăng nhập một lần và xác thực đa yếu tố; mã hoá khi lưu trữ và khi truyền tải |
| Ứng dụng và tích hợp | Cổng giao tiếp ứng dụng, hàng đợi thông điệp và container trên lõi; thành phần thu thập tại biên có bộ đệm cục bộ khi mất kết nối |
| Dữ liệu | Kho dữ liệu tập trung, thu thập theo lịch và theo sự kiện |

Kịch bản này đạt mô hình đa vùng ở lớp lõi, có sao lưu bất biến, đáp ứng mục tiêu điểm khôi phục 15 phút và thời gian khôi phục 4 giờ. Việc thêm một chi nhánh chỉ cần cài thành phần thu thập và khai báo cấu hình, không phụ thuộc chu kỳ mua sắm phần cứng.

Điểm quyết định là khả năng chịu ràng buộc mạng. Mỗi chi nhánh chỉ có một đường truyền không dự phòng, trong khi Ways Station kinh doanh dịch vụ tại chỗ với hình thức tính tiền theo giờ. Khi khách đang chơi net, đang thuê bàn bida hoặc đang tập gym, việc bán hàng và tính giờ không được phép dừng. Mô hình ưu tiên ngoại tuyến tại biên kết hợp đồng bộ bù về lõi đáp ứng đúng ràng buộc này.

## 4.3. Kịch bản C — Ưu tiên đám mây hoàn toàn

Toàn bộ nghiệp vụ, kể cả bán hàng và tính giờ tại quầy, chạy trực tiếp trên đám mây. Chi nhánh chỉ còn thiết bị đầu cuối truy cập.

| Lớp | Thành phần |
|---|---|
| Tính toán và kết nối | Bỏ máy chủ cục bộ; bắt buộc nâng cấp và bổ sung đường truyền dự phòng cho toàn bộ 34 chi nhánh |
| Vận hành, bảo mật, ứng dụng, dữ liệu | Chủ yếu sử dụng dịch vụ quản trị sẵn trên nền tảng đám mây |

Kịch bản này đạt mức sẵn sàng cao nhất ở lớp lõi trong ba kịch bản. Tuy nhiên rủi ro vận hành là mất kết nối đồng nghĩa với ngừng tính giờ, ngừng bán hàng và ngừng check-in tại gym. Với gym hoạt động 24/7 và mô hình tính tiền theo giờ ở cả net và bida, đây là rủi ro không chấp nhận được. Ngoài ra việc bắt buộc nâng cấp đường truyền toàn chuỗi làm phát sinh đầu tư vào lớp 1, mâu thuẫn với phạm vi đầu tư đã xác lập.

## 4.4. So sánh ba kịch bản

| Tiêu chí | A — Tại chỗ | B — Lai | C — Đám mây |
|---|---|---|---|
| Tuân thủ phạm vi đầu tư đã xác lập | Không, phải mua phần cứng | Có | Không, phải nâng cấp đường truyền |
| Mô hình chi phí | Đầu tư ban đầu rất cao | Đầu tư ban đầu thấp, vận hành vừa phải | Đầu tư ban đầu thấp, vận hành cao nhất |
| Chịu được mất kết nối tại chi nhánh | Có | Có | Không, ngừng bán hàng |
| Đạt độ sẵn sàng 99,9% | Khó, cần địa điểm thứ hai | Có | Có |
| Đạt điểm khôi phục 15 phút | Khó, cần đầu tư thêm | Có | Có |
| Đạt onboard chi nhánh trong 2 ngày | Không, phụ thuộc chu kỳ mua sắm | Có | Có |
| Yêu cầu đội ngũ vận hành nội bộ | Rất cao | Trung bình | Thấp |
| Thời gian tới vận hành chính thức | 14–18 tháng | 12 tháng | 10–12 tháng |
| Rủi ro chính | Chi phí và nhân lực | Quản trị ranh giới giữa biên và lõi | Phụ thuộc hoàn toàn vào đường truyền |

## 4.5. Chấm điểm có trọng số

| Tiêu chí | Trọng số | A | B | C |
|---|---|---|---|---|
| Phù hợp phạm vi đầu tư đã xác lập | 25% | 1 | 5 | 2 |
| Đáp ứng bộ KPI đã cam kết | 25% | 3 | 5 | 4 |
| Chịu lỗi đường truyền tại chi nhánh | 20% | 4 | 5 | 1 |
| Tổng chi phí sở hữu 5 năm | 15% | 2 | 4 | 3 |
| Phù hợp năng lực đội ngũ hiện tại | 15% | 2 | 4 | 5 |
| **Điểm quy đổi** | **100%** | **2,35** | **4,70** | **2,90** |

## 4.6. Phương án lựa chọn: Kịch bản B — Kiến trúc lai

Ba căn cứ lựa chọn:

1. Đây là kịch bản duy nhất giữ đúng phạm vi đầu tư đã xác lập. Toàn bộ ngân sách tập trung vào lớp 4 và lớp 5, các lớp 1 đến 3 giữ nguyên và chỉ kế thừa. Hai kịch bản còn lại đều làm phát sinh đầu tư ngoài phạm vi.
2. Đây là kịch bản duy nhất tương thích với ràng buộc vận hành thực tế: kinh doanh dịch vụ tại chỗ, tính tiền theo giờ, gym hoạt động 24/7, mỗi chi nhánh chỉ có một đường truyền không dự phòng.
3. Đây là kịch bản đáp ứng đủ bộ KPI đã cam kết ở Bước 3 trong khung thời gian 12 tháng.

## 4.7. Sơ đồ kiến trúc mục tiêu

```
   ┌──────────────── LÕI TẬP TRUNG ────────────────────────┐
   │                                                        │
   │  LỚP 4 — Nền tảng ứng dụng và tích hợp                 │
   │   · Cổng giao tiếp ứng dụng                            │
   │   · Hàng đợi thông điệp, đồng bộ bù khi mất kết nối    │
   │   · Định danh tập trung — 1 tài khoản cho 5 mảng       │
   │   · Tiếp nhận yêu cầu và biên bản sự vụ điện tử        │
   │     thay thế tổng đài thoại, Zalo và sổ giấy           │
   │   · Nền tảng container và điều phối, tự phục hồi       │
   │                                                        │
   │  LỚP 5 — Nền tảng dữ liệu                              │
   │   · Kho dữ liệu tập trung, 34 chi nhánh × 5 mảng       │
   │   · Thu thập dữ liệu tự động theo lịch và sự kiện      │
   │   · Danh mục hàng hoá và định mức nguyên vật liệu      │
   │     số hoá, đối chiếu với xuất kho thực tế             │
   │   · Theo dõi thiết bị cho mượn tại HUB                 │
   │   · Bảng điều khiển thời gian gần thực                 │
   └────────────────────────▲───────────────────────────────┘
                            │  đồng bộ tối đa 15 phút, có bù trễ
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   [Chi nhánh 1]       [Chi nhánh 2]  ...  [Chi nhánh 34]
   Thành phần thu thập tại biên, có bộ đệm cục bộ
        │
   net · bida · cầu lông · gym · HUB · giữ xe
   chạy cục bộ theo mô hình ưu tiên ngoại tuyến
   kế thừa phần cứng và đường truyền hiện có
```

So với kiến trúc hiện trạng, ba kênh thủ công gồm tổng đài thoại, Zalo và sổ giấy được thay thế bằng hai thành phần trong lõi là hệ thống tiếp nhận yêu cầu và hệ thống biên bản sự vụ điện tử. Con người không còn đóng vai trò lớp tích hợp giữa các hệ thống.

---

# PHỤ LỤC — DANH MỤC TÀI LIỆU NGHIỆP VỤ ĐÃ SỬ DỤNG

| # | Tài liệu | Nội dung khai thác |
|---|---|---|
| 1 | Nghiệp vụ vị trí Giữ xe | Quy trình xử lý mất thẻ theo ba tình huống giấy tờ; quy định chụp ảnh và gửi qua Zalo; quy định tạm giữ giấy tờ; sổ giao ca; bàn giao biên bản giấy |
| 2 | Nghiệp vụ vị trí Thu ngân Gym | Quy trình dẫn khách tham quan; quy trình tư vấn gói tập; phiếu đăng ký hội viên giấy; check-in bằng nhận diện khuôn mặt; bảng giá gói tập |
| 3 | Nghiệp vụ vị trí Phục vụ Gym | Nội quy phòng tập; quy trình vệ sinh; quy trình hỗ trợ thiết bị |
| 4 | Nghiệp vụ vị trí Phục vụ Cầu lông | Định lượng pha chế đồ uống; định mức khăn lạnh theo bàn |
| 5 | Nghiệp vụ vị trí Phục vụ Bida | Phân biệt ba loại bàn; dải nhiệt độ mặt bàn; nguyên tắc tính giá theo khung giờ |
| 6 | Nghiệp vụ vị trí Phục vụ Net | Công thức chế biến; định mức nguyên liệu theo món; bảng giá hàng hoá |
| 7 | Nghiệp vụ vị trí Thu ngân Net và HUB | Quy định phòng HUB; chính sách vé 4 tiếng; danh mục hàng bán, hàng miễn phí và hàng cho mượn; quy định an toàn bếp |
| 8 | Nghiệp vụ vị trí Thu ngân Net và Bida | Bảng giá; công thức tính giá món; nội quy phòng net và phòng bida; quy trình kiểm tra phòng |
| 9 | Bảng phân nhánh tổng đài hỗ trợ | Cơ cấu Phòng Nhân sự, Phòng Điều phối và Bộ phận kho hàng; hệ thống quản lý nhân sự nội bộ; phần mềm quản lý gym; cổng thanh toán ngân hàng |

Nguồn công khai chính chủ: website doanh nghiệp, trang dịch vụ không gian học tập và làm việc, thông tin chi nhánh, cổng tuyển dụng. Nguồn đối chiếu: tra cứu thông tin đăng ký kinh doanh và mã số thuế.
