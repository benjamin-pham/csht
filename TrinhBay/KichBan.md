# Kịch Bản Trình Bày — Đồ án & Thực hành Môn CSHT

**Tổng thời gian: 15 phút** | **31 slide** | **Nhóm 5 — Chuỗi Ways Station**

**Phân bổ:** Đồ án ~8 phút | Thực hành ~6 phút | Kết & Q/A ~1 phút

---

## Slide 1 — Trang bìa ⏱ ~15 giây

Kính chào cô và các bạn. Em là [TÊN], đại diện Nhóm 5, trình bày báo cáo Đồ án và Thực hành môn Cơ sở Hạ tầng Công nghệ Thông tin. Doanh nghiệp nhóm em chọn là chuỗi Ways Station.

---

## Slide 2 — Cấu trúc bài thuyết trình ⏱ ~20 giây

Bài trình bày gồm 2 phần. Phần 1 là Đồ án — đề xuất đầu tư hạ tầng CNTT (Công nghệ Thông tin) cho Ways Station. Phần 2 là Thực hành — ứng dụng AI (Artificial Intelligence — trí tuệ nhân tạo) dự báo lưu lượng khách. Hai phần song song trên cùng doanh nghiệp nhưng phạm vi đo lường tách biệt rõ ràng.

---

## Slide 3 — Tổng quan doanh nghiệp ⏱ ~40 giây

Ways Station là chuỗi giải trí tích hợp: Gym 24/7, Net, Bida, Cầu lông, Hub. Tăng trưởng rất nhanh — 22 lên 34 chi nhánh trong 2 năm.

Đặc biệt quan trọng: doanh thu tính theo block thời gian — khách quẹt thẻ vào, tính tiền từng giờ. Nếu hệ thống sập, không tính được tiền, mất doanh thu ngay lập tức.

Về pháp lý: 34 chi nhánh là 34 hộ kinh doanh cá thể riêng biệt, không có pháp nhân trung tâm, không có IT (Information Technology — bộ phận công nghệ thông tin) tại chỗ. Hạ tầng CNTT bị chia cắt hoàn toàn.

Điểm nhạy cảm: nhân viên đang phải chụp ảnh CCCD (Căn cước công dân), Face ID (nhận diện khuôn mặt) của khách rồi gửi qua Zalo cá nhân. Đây là rủi ro vi phạm Nghị định 13 rất nghiêm trọng.

---

## Slide 4 — Phần 1: Đồ án ⏱ ~15 giây

Bắt đầu Phần 1: Đồ án Môn học. Tên đề tài là Đề xuất đầu tư nền tảng tích hợp ứng dụng và nền tảng dữ liệu tập trung cho chuỗi Ways Station. Mục tiêu: giải quyết 3 vấn đề vừa nêu — đứt gãy tích hợp, mù dữ liệu, và rò rỉ dữ liệu cá nhân.

---

## Slide 5 — Bối cảnh & Điểm nghẽn ⏱ ~40 giây

Nhóm em xác định 4 điểm nghẽn chính.

**Thứ nhất — Nghẽn hạ tầng:** 34 chi nhánh dùng 8 phần mềm rời rạc, không có API (Application Programming Interface — giao diện lập trình ứng dụng) nào nối với nhau, 0% tích hợp tự động. Báo cáo quản trị trễ 24 đến 48 giờ.

**Thứ hai — Giới hạn vận hành:** toàn bộ giao tiếp qua 1 tổng đài, Zalo cá nhân và sổ giao ca giấy. Cách làm này đã đạt giới hạn ở mốc 34 chi nhánh.

**Thứ ba — Rủi ro bảo mật:** 100% ảnh CCCD, cà vẹt xe, Face ID của khách lưu trên điện thoại cá nhân nhân viên, không mã hóa.

**Thứ tư — Áp lực pháp lý:** vi phạm NĐ13 (Nghị định 13/2023/NĐ-CP) về bảo vệ dữ liệu cá nhân. Mức phạt có thể lên đến 5% tổng doanh thu.

---

## Slide 6 — Phạm vi đầu tư theo lớp năng lực ⏱ ~35 giây

Dự án đầu tư theo 3 lớp năng lực.

**Lớp 4** — Nền tảng ứng dụng: gồm API Gateway (cổng giao tiếp API), Kafka (hệ thống hàng đợi tin nhắn), Kubernetes (hệ thống quản lý container) trên Cloud (đám mây) và Edge (biên — tại chi nhánh). Mục đích: nối liền 8 phần mềm rời rạc.

**Lớp 5** — Nền tảng dữ liệu: gồm Data Lakehouse (kho dữ liệu tập trung), Airflow ETL (Extract-Transform-Load — trích xuất, chuyển đổi, nạp dữ liệu), CDC streaming (Change Data Capture — bắt sự kiện thay đổi dữ liệu thời gian thực). Mục đích: tập trung dữ liệu real-time, xóa mù dữ liệu.

**Lớp 3** — Chỉ 2 thành phần: Keycloak IAM/SSO (Identity and Access Management / Single Sign-On — quản lý định danh và đăng nhập một lần) và mã hóa PII (Personally Identifiable Information — thông tin định danh cá nhân). Mục đích: 1 định danh duy nhất, mã hóa 100% dữ liệu nhạy cảm, triệt tiêu rủi ro NĐ13.

Lớp 1 và 2 kế thừa hạ tầng sẵn có để tiết kiệm chi phí.

---

## Slide 7 — Đối tượng thụ hưởng ⏱ ~30 giây

Nền tảng phục vụ 5 nhóm đối tượng.

Ban Giám đốc — khoảng 5 đến 8 người — có báo cáo real-time (thời gian thực) thay vì trễ 48 giờ.

Quản lý chi nhánh — 34 người — có SSO (Single Sign-On) đăng nhập 1 lần cho mọi hệ thống.

Phòng ban HQ (Headquarters — trụ sở chính) gồm Nhân sự, Kho — khoảng 15 đến 20 người — giải phóng 2.500 giờ công đối soát thủ công mỗi năm.

Nhân viên tại chi nhánh — khoảng 250 đến 300 người — quan trọng nhất — hệ thống vẫn tính tiền được khi rớt mạng nhờ offline mode (chế độ ngoại tuyến).

Khách hàng — toàn bộ hội viên — có 1 định danh cho 5 dịch vụ và dữ liệu cá nhân được bảo mật.

---

## Slide 8 — Ma trận KPI nền tảng ⏱ ~40 giây

Nhóm em đặt 6 KPI (Key Performance Indicator — chỉ số đo lường hiệu suất) theo 3 vấn đề.

Giải quyết đứt gãy tích hợp — Lớp 4: Uptime (thời gian hoạt động) ≥ 99,99%, tức downtime (thời gian ngừng) không quá 4 phút/tháng. MTTR (Mean Time To Recovery — thời gian khôi phục trung bình) ≤ 30 phút — hệ thống phải tự phục hồi.

Giải quyết mù dữ liệu — Lớp 5: Data Freshness (độ tươi dữ liệu) ≤ 5 giây cho luồng CDC (Change Data Capture). Data Completeness (tính đầy đủ dữ liệu) ≥ 99,5%.

Giải quyết rò rỉ PII — Lớp 3: Encryption Coverage (tỷ lệ mã hóa) = 100%. RPO (Recovery Point Objective — mục tiêu điểm khôi phục) ≤ 15 phút.

Nghiệm thu thành công khi đạt 6/6 KPI tại Go-live (thời điểm vận hành chính thức), duy trì 5/6 sau 3 tháng.

---

## Slide 9 — Công thức KPI (1/2) ⏱ ~30 giây

3 công thức KPI đầu tiên.

**Uptime** theo chuẩn Google SRE (Site Reliability Engineering — kỹ thuật độ tin cậy hệ thống) — bằng Tổng thời gian trừ Downtime, chia cho Tổng thời gian. Target ≥ 99,99% nghĩa là downtime tối đa 4,32 phút mỗi tháng.

**MTTR** (Mean Time To Recovery) theo Atlassian ITSM (IT Service Management — quản lý dịch vụ CNTT) — bằng Tổng thời gian khắc phục sự cố chia cho Tổng số sự cố. Target ≤ 30 phút — hệ thống Kubernetes phải tự khởi tạo lại service lỗi trước khi ảnh hưởng diện rộng.

**Encryption Coverage** (tỷ lệ mã hóa) theo NIST (National Institute of Standards and Technology — Viện Tiêu chuẩn Công nghệ Hoa Kỳ) — bằng Số bản ghi được mã hóa chia cho Tổng số bản ghi nhạy cảm. Target = 100% — nếu hacker đánh cắp được database, dữ liệu cũng bị vô hiệu hóa.

---

## Slide 10 — Công thức KPI (2/2) ⏱ ~25 giây

2 KPI còn lại.

**Data Freshness** (độ tươi dữ liệu) theo ISO/IEC 25012 — bằng Thời điểm ghi nhận trên Cloud trừ Thời điểm giao dịch tại POS (Point of Sale — máy bán hàng). Target ≤ 5 giây — tức là khách quẹt thẻ tại chi nhánh, trong vòng 5 giây dữ liệu phải có mặt trên Data Lakehouse.

**Data Completeness** (tính đầy đủ dữ liệu) cũng theo ISO 25012 — bằng Số bản ghi trên Cloud chia cho Số bản ghi trên POS. Target ≥ 99,5% — đảm bảo không thất thoát dữ liệu, giảm sai lệch đối soát doanh thu từ 3,8% xuống dưới 0,5%.

---

## Slide 11 — Phương án kiến trúc Hybrid Cloud ⏱ ~1 phút 10 giây

Nhóm em đánh giá 3 kịch bản: On-Premise (tại chỗ), Cloud-Native (thuần đám mây), và Hybrid Cloud (đám mây lai).

On-Premise đạt 2/6 tiêu chí — giữ được offline và tuân thủ NĐ13, nhưng CAPEX (Capital Expenditure — chi phí đầu tư ban đầu) quá cao, không auto-scale (tự co giãn), không DR (Disaster Recovery — khôi phục thảm họa).

Cloud-Native đạt 4/6 — co giãn tốt, CAPEX thấp, nhưng **mất mạng là mất doanh thu ngay lập tức**, và PII đặt trên hạ tầng bên thứ ba vi phạm NĐ13.

**Hybrid Cloud đạt 6/6.** Xử lý tập trung tự co giãn trên Cloud. Edge Cluster K3s (cụm máy chủ biên chạy Kubernetes nhẹ) tại chi nhánh giữ offline mode — mất mạng vẫn tính tiền được, khi có mạng tự đồng bộ bù. Dữ liệu PII nhạy cảm giữ On-Premise tại HQ, mã hóa AES-256 (chuẩn mã hóa 256-bit), không rời khỏi máy chủ doanh nghiệp.

Tại sao Hybrid Cloud phù hợp riêng Ways Station? Vì 4 đặc điểm của doanh nghiệp này buộc phải chọn Hybrid:

- **Doanh thu tính theo giờ** — mất mạng vài phút là không tính được tiền, không trả được bàn, thiệt hại ngay lập tức. Nên phải có Edge xử lý offline. Cloud-Native bị loại ở đây.
- **34 hộ kinh doanh cá thể, không có IT tại chỗ** — không thể đặt cụm server đầy đủ tại 34 điểm. Chỉ chấp nhận thiết bị nhỏ, cấu hình từ xa, tự phục hồi. On-Premise bị loại ở đây.
- **Thu thập PII nhạy cảm cao** — ảnh CCCD, Face ID bắt buộc nằm dưới quyền kiểm soát trực tiếp của doanh nghiệp, không đặt trên hạ tầng bên thứ ba. Cloud-Native bị loại lần nữa.
- **Tăng trưởng nhanh, tải biến động mạnh** — cần auto-scaling (tự co giãn) và nhân bản chi nhánh mới trong vài giờ. On-Premise bị loại lần nữa.

Chỉ Hybrid Cloud thỏa đồng thời cả 4 điều kiện này.

---

## Slide 12 — CAPEX ⏱ ~30 giây

Tổng CAPEX (Capital Expenditure — chi phí đầu tư ban đầu): 1,309 tỷ VNĐ, chia 3 nhóm.

Phần cứng 565 triệu — gồm 36 Edge Server (máy chủ biên tại chi nhánh) và Rack Server tại HQ (trụ sở chính).

Dịch vụ triển khai 632 triệu — thiết kế, cài đặt, tích hợp, đào tạo.

Cloud giai đoạn dev (development — phát triển) 112 triệu trong 4 tháng.

Điểm đáng chú ý: bản quyền phần mềm = 0 đồng, toàn bộ dùng mã nguồn mở — open-source.

---

## Slide 13 — OPEX ⏱ ~25 giây

OPEX (Operational Expenditure — chi phí vận hành định kỳ) hàng năm: 1,123 tỷ VNĐ.

Hạ tầng Cloud chiếm lớn nhất: 703 triệu — gồm K8s Cluster (cụm Kubernetes), Managed PostgreSQL HA (cơ sở dữ liệu có tính sẵn sàng cao), Managed Kafka, GPU Instance (máy chủ GPU) và nâng băng thông 34 chi nhánh.

Nhân sự vận hành: 343 triệu — 1 DevOps/SRE (Development Operations / Site Reliability Engineer — kỹ sư vận hành) full-time, 1 Data Engineer part-time.

Bảo mật và bảo trì phần cứng: 77 triệu — gồm gia hạn Firewall NGFW (Next-Generation Firewall — tường lửa thế hệ mới), Pentest (kiểm thử xâm nhập) 2 lần/năm, bảo trì server.

---

## Slide 14 — TCO 3 năm ⏱ ~35 giây

TCO (Total Cost of Ownership — tổng chi phí sở hữu) 3 năm tổng cộng: 5,209 tỷ VNĐ. Tương đương chỉ 1,45% doanh thu chuỗi trong 3 năm — nằm trong biên độ đầu tư CNTT bình thường của ngành.

Lợi ích quy đổi ước tính gần 2 tỷ/năm. Trừ OPEX, dòng tiền ròng khoảng 832 triệu/năm. **Thời gian hoàn vốn — Payback Period: 1,7 năm — tức 21 tháng.**

Và chưa tính giá trị tránh được rủi ro phạt NĐ13 — mức phạt có thể lên đến 6 tỷ.

---

## Slide 15 — Tiêu chí nghiệm thu đồ án ⏱ ~30 giây

Nghiệm thu theo từng lớp.

Lớp 4: Uptime ≥ 99,99% và MTTR ≤ 30 phút. Offline test — ngắt mạng chi nhánh ≥ 4 giờ, POS vẫn tính tiền bình thường, tự đồng bộ 100% giao dịch khi có mạng trở lại. Load test — API Gateway chịu tải ≥ 2.000 CCU (Concurrent Users — người dùng đồng thời).

Lớp 5: Data Freshness ≤ 5 giây. Data Completeness ≥ 99,5%. Sai lệch đối soát doanh thu dưới 0,5%.

Lớp 3: Encryption Coverage = 100% — toàn bộ PII mã hóa AES-256 trên On-Premise. RPO ≤ 15 phút. Vượt qua Vulnerability Scan (quét lỗ hổng bảo mật) — 0 lỗ hổng Critical/High.

---

## Slide 16 — Phần 2: Thực hành ⏱ ~15 giây

Chuyển sang Phần 2: Thực hành Môn học. Tên đề tài là Ứng dụng mô hình học sâu — Deep Learning — và mô hình nền tảng chuỗi thời gian — Time-Series Foundation Models — để dự báo lưu lượng khách hàng đa chi nhánh cho chuỗi Ways Station. Đề tài này chạy song song với đồ án, cùng doanh nghiệp nhưng đo đối tượng khác — đo sản phẩm phần mềm AI thay vì đo nền tảng hạ tầng.

---

## Slide 17 — Bối cảnh & Điểm nghẽn vận hành ⏱ ~30 giây

Bài toán thực hành xuất phát từ vấn đề vận hành. Lưu lượng khách tại 34 chi nhánh biến động rất mạnh theo khung giờ. Nhưng việc xếp ca hiện tại hoàn toàn dựa vào cảm tính.

Hậu quả: giờ cao điểm thiếu người phục vụ, giờ thấp điểm dư thừa nhân sự. Gây lãng phí quỹ lương — OPEX — rất lớn.

Ở mốc 34 chi nhánh, cần có dữ liệu định lượng để tự động hóa quyết định.

---

## Slide 18 — Giải pháp AI dự báo ⏱ ~30 giây

Giải pháp: xây dựng hệ thống AI dự báo lưu lượng khách theo từng chi nhánh, từng khung giờ, trong 7 ngày tới.

Dữ liệu đầu vào tận dụng luồng dữ liệu đã làm sạch trên Cloud Data Lakehouse từ đồ án.

Đầu ra: Dashboard (bảng điều khiển) cho Quản lý chi nhánh duyệt lịch xếp ca. Hệ thống này đóng vai trò DSS (Decision Support System — hệ thống hỗ trợ ra quyết định). AI chỉ hỗ trợ, quyết định cuối cùng thuộc về con người.

---

## Slide 19 — Đối tượng thụ hưởng (Thực hành) ⏱ ~25 giây

Kết quả dự báo phục vụ 4 nhóm.

Phòng Điều phối — khoảng 5 đến 10 người — xếp ca linh hoạt, tối ưu chi phí nhân sự.

Quản lý chi nhánh — 34 người — nhận cảnh báo sớm để gọi thêm người, tránh quá tải.

Bộ phận Kho — khoảng 5 đến 10 người — định lượng được nhu cầu tiêu thụ để điều phối vật tư, cung ứng.

Marketing — khoảng 5 người — nhận diện chính xác khung giờ thấp điểm để chạy chiến dịch kích cầu.

Khách hàng hưởng lợi gián tiếp — trải nghiệm nhanh chóng, không phải chờ đợi lâu vào giờ cao điểm.

---

## Slide 20 — Các mô hình AI thực nghiệm ⏱ ~35 giây

Nguyên tắc quan trọng: nhóm em cam kết **ngưỡng chỉ số**, không cam kết thuật toán cụ thể. Thực nghiệm song song 4 mô hình.

**ARIMA** (Auto-Regressive Integrated Moving Average — mô hình tự hồi quy tích hợp trung bình trượt) — dùng làm baseline (mốc đối chứng).

**Prophet** — mô hình của Meta, rất mạnh trong việc xử lý tính chu kỳ, mùa vụ.

**LSTM / BiLSTM** (Long Short-Term Memory / Bidirectional LSTM — bộ nhớ dài-ngắn hạn hai chiều) — mạng nơ-ron hồi quy, xuất sắc trong việc học các mẫu dữ liệu phức tạp dài hạn.

**TSFM** (Time-Series Foundation Model — mô hình nền tảng chuỗi thời gian) — xu hướng AI mới nhất, năng lực tổng quát hóa cao.

Tiêu chí chọn: MAPE dưới 15%, Inference Latency (thời gian suy luận) ≤ 200ms, Delta MAPE ≤ 10% giữa các ngữ cảnh.

Nếu không mô hình nào đạt, phát hành chế độ beta, giữ Moving Average (trung bình trượt) 7 ngày làm fallback (phương án dự phòng).

---

## Slide 21 — KPI Nhóm A (Mô hình AI) ⏱ ~30 giây

KPI Nhóm A đo chất lượng mô hình AI.

**MAPE** (Mean Absolute Percentage Error — sai số phần trăm tuyệt đối trung bình): dưới 15% tại Pilot (thử nghiệm), siết xuống dưới 10% sau go-live 3 tháng.

**MAE** (Mean Absolute Error — sai số tuyệt đối trung bình): ≤ 3 khách/khung giờ — sai lệch thực tế không quá 3 người.

**Precision** (độ chính xác nhận diện cao điểm): ≥ 85% — khi báo giờ cao điểm, 85% phải đúng là cao điểm thật.

**Inference Latency** (thời gian suy luận mô hình): ≤ 200ms — trả kết quả tức thì.

---

## Slide 22 — Công thức KPI A (1/2) ⏱ ~25 giây

2 công thức đầu tiên đo chất lượng mô hình.

**MAPE** — Mean Absolute Percentage Error — bằng trung bình của giá trị tuyệt đối hiệu số giữa lượng khách thực tế (y) và dự báo (y-hat), chia cho lượng khách thực tế, nhân 100%. Nói đơn giản: mô hình sai bao nhiêu phần trăm so với thực tế. Target dưới 15%.

**MAE** — Mean Absolute Error — bằng trung bình giá trị tuyệt đối hiệu số giữa thực tế và dự báo. Đo sai lệch cụ thể bao nhiêu khách. Target ≤ 3 khách/khung giờ — tức AI nói 30 khách thì thực tế nằm trong khoảng 27 đến 33.

---

## Slide 23 — Công thức KPI A (2/2) ⏱ ~25 giây

2 công thức còn lại.

**Precision** — bằng TP (True Positive — dương tính thật) chia cho TP cộng FP (False Positive — dương tính giả). Nghĩa là: trong tất cả các lần mô hình báo "đây là giờ cao điểm", bao nhiêu lần đúng là cao điểm thật. Target ≥ 85% — hạn chế tối đa việc báo động giả khiến quản lý gọi thêm người không cần thiết.

**Inference Latency** (thời gian suy luận) — bằng Thời điểm trả kết quả trừ Thời điểm gửi request (yêu cầu). Đo tốc độ suy luận thuần của mô hình, không tính gateway. Target ≤ 200ms — đảm bảo Dashboard phản hồi tức thì khi quản lý truy vấn.

---

## Slide 24 — KPI Nhóm B (Vận hành phần mềm) ⏱ ~25 giây

KPI Nhóm B đo vận hành hệ thống phần mềm.

**Uptime API** (thời gian hoạt động của API): ≥ 99,9% — gián đoạn tối đa 43 phút/tháng.

**Batch Freshness** (độ tươi dữ liệu luồng batch — xử lý theo lô): ≤ 24 giờ — dữ liệu huấn luyện đồng bộ xong trước sáng.

**API Response Time P95** (thời gian phản hồi API ở phân vị 95): ≤ 500ms.

Lưu ý Nhóm B đo ứng dụng phần mềm, khác với KPI nền tảng hạ tầng ≥ 99,99% bên đồ án.

---

## Slide 25 — Công thức KPI B ⏱ ~30 giây

3 công thức KPI vận hành phần mềm.

**Uptime API** theo Google SRE — bằng Tổng thời gian trừ Downtime API, chia cho Tổng thời gian. Target ≥ 99,9% — gián đoạn tối đa 43 phút/tháng. Lưu ý đây là uptime ứng dụng, thấp hơn 1 bậc so với uptime nền tảng 99,99% bên đồ án vì tầng dịch vụ có thêm hao hụt.

**Batch Data Freshness** theo ISO 25012 — bằng Thời điểm hoàn thành ETL (Extract-Transform-Load) trừ Thời điểm khóa sổ cuối ngày. Target ≤ 24 giờ — dữ liệu huấn luyện phải đồng bộ xong trước sáng hôm sau.

**API Response Time P95** theo AWS Builders' Library — lấy percentile 95 (phân vị 95) của toàn bộ thời gian phản hồi. Target ≤ 500ms — 95% thao tác của quản lý trên Dashboard phải được phản hồi dưới nửa giây.

---

## Slide 26 — Kiến trúc Data Pipeline ⏱ ~40 giây

Luồng xử lý tự động — Data Pipeline (đường ống dữ liệu) — gồm 3 tầng.

**Tầng Dữ liệu:** 1 giờ sáng, Airflow (công cụ điều phối luồng công việc) tự động Extract (rút dữ liệu) từ POS 34 chi nhánh qua kênh mã hóa TLS (Transport Layer Security — bảo mật tầng truyền tải). Transform — làm sạch, khử trùng lặp, ẩn danh PII. Load — nạp vào kho dữ liệu PostgreSQL.

**Tầng Ứng dụng — AI Engine:** Train (huấn luyện) mô hình hàng tháng, lưu phiên bản vào MLflow (công cụ quản lý vòng đời mô hình AI). Batch Inference (suy luận theo lô) hàng đêm lúc 2 giờ sáng, xuất dự báo 7 ngày cho 34 chi nhánh.

**Tầng Trình bày — DSS:** Alert Service (dịch vụ cảnh báo) cảnh báo nếu dự báo vượt 1,5 lần trung bình. 8 giờ sáng, Quản lý chi nhánh gọi API xem dự báo và duyệt lịch phân ca. Con người chốt quyết định cuối cùng.

---

## Slide 27 — CAPEX Thực hành ⏱ ~25 giây

Tổng CAPEX xây dựng: 663 triệu trong 15 tuần.

Nhân công chiếm 594 triệu — đội 7 người gồm PM (Project Manager — quản lý dự án), Data Engineer (kỹ sư dữ liệu), ML Engineer (Machine Learning Engineer — kỹ sư học máy), Backend Developer (lập trình viên phía sau), SRE (Site Reliability Engineer), QA (Quality Assurance — kiểm thử chất lượng).

Hạ tầng dev 64 triệu — thuê VM (Virtual Machine — máy ảo), GPU training (GPU huấn luyện), PostgreSQL, S3 (Object Storage — lưu trữ đối tượng).

Bản quyền = 0 — toàn bộ open-source: Airflow, MLflow, FastAPI.

---

## Slide 28 — OPEX Thực hành ⏱ ~20 giây

OPEX hàng năm: 325,8 triệu.

Cloud server (máy chủ đám mây): 163 triệu — gồm K8s Cluster, PostgreSQL HA (High Availability — tính sẵn sàng cao), S3 Storage, DNS (Domain Name System).

Nhân sự Hypercare (hỗ trợ tăng cường sau go-live) part-time: 132 triệu.

Pentest (kiểm thử xâm nhập): 20 triệu — 2 lần/năm.

GPU tái huấn luyện mô hình AI: 9,6 triệu — chạy Spot Instance (máy ảo giá rẻ theo nhu cầu) 1 lần/tháng.

---

## Slide 29 — Tiêu chí nghiệm thu thực hành ⏱ ~30 giây

Nghiệm thu Nhóm A — mô hình AI:
- MAPE (sai số phần trăm) dưới 15% tại Pilot.
- MAE (sai số tuyệt đối) ≤ 3 khách/giờ.
- Precision (độ chính xác cảnh báo cao điểm) ≥ 85%.
- Inference Latency (thời gian suy luận) ≤ 200ms.

Nghiệm thu Nhóm B — vận hành:
- Uptime API ≥ 99,9%.
- API Response P95 ≤ 500ms.
- Batch Freshness ≤ 24 giờ.

Nghiệm thu hiệu quả nghiệp vụ: tự động hóa 100% quy trình tính toán nhân sự trực, tiết kiệm tối thiểu 15% OPEX nhờ cắt giảm lãng phí thừa nhân sự.

---

## Slide 30 — Cảm ơn ⏱ ~10 giây

Trên đây là toàn bộ báo cáo Đồ án và Thực hành của Nhóm 5. Cảm ơn cô và các bạn đã lắng nghe. Nhóm em sẵn sàng trả lời câu hỏi.

---

## Bảng tổng kết thời gian

| Phần | Slide | Thời gian |
|:---|:---:|---:|
| Mở đầu & Tổng quan | 1–3 | ~1 phút 15 giây |
| Đồ án | 4–15 | ~7 phút |
| Thực hành | 16–29 | ~6 phút 25 giây |
| Kết thúc | 30 | ~10 giây |
| **Tổng** | **30** | **~14 phút 50 giây** |

> Tổng thời gian hiện tại rất đẹp (dưới 15 phút). Nếu cần chạy nhanh hơn nữa: ở slide 11 (Hybrid Cloud) chỉ nói 2 trong 4 đặc điểm, hoặc ở slide 19 (đối tượng thụ hưởng thực hành) gộp 4 nhóm thành 2 câu.
