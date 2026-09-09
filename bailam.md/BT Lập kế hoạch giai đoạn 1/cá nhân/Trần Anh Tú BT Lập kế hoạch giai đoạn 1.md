# **PHẦN I: QUY HOẠCH VÀ NÂNG CẤP HẠ TẦNG KỸ THUẬT (WAYS STATION)**

## 1. Tổng quan hiện trạng hạ tầng (AS-IS)

Chuỗi Ways Station quy mô 34-38 chi nhánh tại TP.HCM (vận hành 24/7 với
các dịch vụ Gaming, Bida, Gym, Cầu lông, Hub) hiện hoạt động dưới mô
hình các Hộ kinh doanh cá thể độc lập. Mô hình này tối ưu về thủ tục
hành chính nhưng gây ra sự phân tán về dữ liệu và hạ tầng CNTT. Bảng
dưới đây tóm tắt hiện trạng theo 5 lớp hạ tầng kỹ thuật:

  --------------- ------------------ -------------------------------------
  **Lớp hạ tầng** **Thiết bị & Phần  **Hiện trạng & Chỉ số định lượng**
                  mềm**              

  **1. Compute &  POS thu ngân,      Mạng WAN liên cơ sở: 0%. 100% sử dụng
     Network**    server tính tiền   Internet phổ thông không dự phòng.
                  nội bộ, modem FTTH Không có server trung tâm; \>60%
                  dân dụng.          thiết bị đã hết hạn bảo hành. Uptime
                                     toàn hệ thống \~95.0%.

   **2. Ops (Vận  Máy chấm công vân  Giám sát tự động: 0%. MTTD 4-8h, MTTR
      hành)**     tay, Google        12-24h. Sao lưu thủ công (\<30% tuân
                  Sheets, nhóm chat  thủ), chưa có giải pháp khắc phục
                  tác nghiệp.        thảm họa (DR).

  **3. Security & Thiết bị Face ID   Áp dụng SSO/MFA: 0%. Dữ liệu sinh
    Identity**    Gym độc lập, tài   trắc học Face ID lưu cục bộ chưa mã
                  khoản hệ thống net hóa, thiếu cơ chế Audit Log nhật ký
                  riêng lẻ.          truy cập.

    **4. App &    Web HR nội bộ, app Thiếu API Gateway trung gian. Tỷ lệ
   Integration**  Gym đóng gói, EDC  đóng gói Container (Docker) và triển
                  thanh toán độc     khai tự động (CI/CD) đạt 0%. Đối soát
                  lập.               dữ liệu thực hiện thủ công.

     **5. Data    Báo cáo ca xuất    Tập trung hóa dữ liệu: 0%. Chưa có
    Platform**    file Excel, lưu    Kho dữ liệu (Data Warehouse) và đường
                  rải rác Google     truyền ETL. Độ trễ tổng hợp báo cáo
                  Drive.             toàn chuỗi mất 24-48 giờ.
  --------------- ------------------ -------------------------------------

## 2. Phân tích rủi ro vận hành & Pháp lý

Việc duy trì hạ tầng phân tán hiện tại tiềm ẩn các rủi ro trọng yếu đối
với hoạt động kinh doanh và tính tuân thủ pháp luật của doanh nghiệp:

  --------- ------------------ --------- --------- -------------- ---------------
   **STT**  **Rủi ro trọng     **Xác     **Tác     **Thiệt hại    **Giải pháp
            yếu**              suất**    động**    ước tính       kiểm soát Kỹ
                                                   (VNĐ/năm)**    thuật**

      1     Rò rỉ dữ liệu sinh Trung     Rất       600 triệu - 2  Mã hóa dữ liệu
            trắc học Face ID;  bình      nghiêm    tỷ (Phạt hành  chuẩn AES-256
            Vi phạm Nghị định            trọng     chính, bồi     (Lớp 3), kích
            13/2023/NĐ-CP.                         thường, tổn    hoạt Audit Log,
                                                   hại thương     hoàn thiện đánh
                                                   hiệu).         giá tác động
                                                                  DPIA.

      2     Sự cố thiết bị POS Cao       Nghiêm    300 triệu -    Triển khai
            cục bộ gây thất              trọng     550 triệu (Mất Message Queue
            thoát dữ liệu giao                     dữ liệu doanh  (Lớp 4) đồng bộ
            dịch.                                  thu, chi phí   hóa giao dịch
                                                   đối soát).     thời gian thực
                                                                  lên Cloud.

      3     Thất thoát hàng    Rất cao   Trung     350 triệu -    Tự động hóa bán
            tồn kho & dịch vụ            bình      700 triệu      hàng (Lớp 4),
            do quản lý thủ                         (Thất thoát    tập trung dữ
            công.                                  F&B và giờ     liệu đối soát
                                                   dịch vụ).      tại Data
                                                                  Warehouse (Lớp
                                                                  5).

      4     Chậm tiến độ mở    Cao       Nghiêm    200 triệu -    Chuẩn hóa API
            rộng điểm bán mới            trọng     450 triệu (Chi Gateway, đồng
            do đóng gói hạ                         phí nhân công, bộ cấu hình
            tầng thủ công.                         lãng phí mặt   phần mềm từ xa.
                                                   bằng cơ sở).   
  --------- ------------------ --------- --------- -------------- ---------------

## 3. Mục tiêu chiến lược & Bảng KPI (TO-BE)

**Mục tiêu tổng quát:** Thiết lập kiến trúc tích hợp phần mềm trung gian
(Lớp 4) và Kho dữ liệu tập trung trên Cloud (Lớp 5), tuân thủ quy định
bảo mật dữ liệu cá nhân, tối ưu hóa chi phí bằng cách kế thừa hạ tầng
thiết bị hiện hữu.

  ----------- --------------- ------------ -------------- ---------------------
    **Hạng    **Chỉ số KPI**  **Hiện tại   **Mục tiêu     **Phương pháp đánh
     mục**                    (AS-IS)**    (TO-BE)**      giá**

    **Độ ổn   Tỷ lệ Uptime    \~95.0%      ≥ 99.9%        Giám sát tự động qua
    định**    toàn hệ thống                (Downtime \<   Prometheus/Grafana.
                                           8.7h/năm)      

  **Khôi phục RPO (Mất dữ     12 - 24 giờ\ \< 15 phút     Kiểm thử kịch bản
    sự cố**   liệu tối đa)\   \> 24 giờ    (Giao dịch),   gián đoạn định kỳ 6
              RTO (Thời gian               \< 1h (Báo     tháng/lần.
              gián đoạn)                   cáo)\          
                                           \< 2 giờ (Hệ   
                                           thống POS      
                                           chính)         

  **Tốc độ xử API Latency     Chưa định    \< 150 ms\     Kiểm thử tải trọng
     lý**     (p95)\          lượng\       \< 5 phút      k6/JMeter (500
              Độ trễ đồng bộ  24 - 48 giờ                 req/s).
              Data Warehouse                              

  **Bảo mật** Tỷ lệ mã hóa dữ 0%\          100% (At-rest  Đánh giá an ninh độc
              liệu nhạy cảm\  \< 10%       & In-transit)\ lập (Pentest).
              Tỷ lệ ghi nhận               100% (Lưu trữ  
              Audit Log                    tối thiểu 12   
                                           tháng)         

  **Vận hành  Chỉ số MTTD     4 - 8 giờ\   \< 15 phút\    Hệ thống ITSM Ticket
     IT**     (Phát hiện      12 - 24 giờ  \< 2 giờ (Sự   tracking.
              lỗi)\                        cố phần mềm)   
              Chỉ số MTTR                                 
              (Khắc phục lỗi)                             
  ----------- --------------- ------------ -------------- ---------------------

## 4. Phân tích & Lựa chọn phương án kiến trúc

So sánh 3 mô hình kiến trúc hạ tầng để xác định phương án tối ưu cho
chuỗi Ways Station:

  ------------- ------------------ -------------------- ------------------
   **Tiêu chí   **1. On-Premises** **2. Hybrid Platform **3. Pure Cloud**
   đánh giá**                      (Đề xuất)**          

   **Tận dụng   Trung bình (Yêu    Tối ưu (Duy trì toàn Thấp (Bắt buộc
  thiết bị hiện cầu thay thế       bộ POS, PC và hạ     nâng cấp kênh thuê
      hữu**     Router WAN tại các tầng mạng hiện có).  riêng
                điểm).                                  Leased-line).

   **Tích hợp   Khá (Phát sinh chi Rất tốt (Sử dụng     Rất tốt (Yêu cầu
  ứng dụng (Lớp phí bảo trì và cấu Cloud API Gateway,   tái cấu trúc toàn
      4)**      hình thủ công).    cân bằng tải tự      bộ mã nguồn phần
                                   động).               mềm).

   **Tập trung  Thấp (Hạn chế về   Rất tốt (Cloud Data  Rất tốt (Chi phí
  dữ liệu (Lớp  khả năng mở rộng   Warehouse linh hoạt, truy vấn dữ liệu
      5)**      dung lượng lưu     tối ưu cho           biến động lớn).
                trữ).              AI/Analytics).       

   **Tính sẵn   Thấp (Tốn chi phí  Cao (Vận hành        Phụ thuộc tuyệt
    sàng & Dự   xây dựng Trung tâm Offline cục bộ khi   đối vào đường
     phòng**    dữ liệu dự phòng   mất kết nối; Cloud   truyền Internet
                thứ 2).            tự động DR).         tại điểm bán.

   **Tuân thủ   Trung bình (Thiếu  Tối ưu (Tích hợp     Phức tạp (Rủi ro
    Nghị định   công cụ kiểm toán  IAM, mã hóa dữ liệu  pháp lý chuyển dữ
      13**      và mã hóa tự       sinh trắc học chuẩn  liệu xuyên biên
                động).             hóa).                giới).

  **Mô hình chi CAPEX rất cao,     CAPEX thấp, OPEX tối CAPEX thấp, OPEX
      phí**     OPEX vận hành cao. ưu theo mức độ sử    hạ tầng & đường
                                   dụng                 truyền cao.
                                   (Pay-as-you-go).     

   **Thời gian  6 - 9 tháng        3 - 4 tháng (Triển   5 - 7 tháng
  triển khai**                     khai cuốn chiếu)     
  ------------- ------------------ -------------------- ------------------

## Lý do lựa chọn Phương án 2 (Hybrid Platform):

- **Đảm bảo tính liên tục vận hành (Business Continuity):** Cho phép các
  điểm bán xử lý giao dịch offline khi gặp sự cố mạng Internet, sau đó
  tự động đồng bộ về Cloud qua Message Queue.

- **Tối ưu hóa CAPEX/OPEX:** Tận dụng 100% thiết bị phần cứng hiện có
  tại 34+ chi nhánh; chỉ chi trả chi phí điện toán đám mây cho các tác
  vụ tập trung (API Gateway, Data Warehouse, AI Training/Inference).

- **Khả năng mở rộng (Scalability):** Đặt nền tảng cho việc tích hợp các
  mô hình phân tích nâng cao và AI điều phối vận hành toàn chuỗi.

# **PHẦN II: ỨNG DỤNG AI DỰ BÁO LƯỢNG KHÁCH ĐIỀU PHỐI NHÂN SỰ**

## 1. Bối cảnh & Thách thức nghiệp vụ (Business Case)

**Hiện trạng điều phối nhân sự (AS-IS):**

- Lập kế hoạch ca làm việc dựa trên kinh nghiệm định tính của Quản lý
  chi nhánh.

- Gửi bảng đăng ký thủ công qua Google Sheets đến Phòng Điều phối Vận
  hành.

- Tỷ lệ hoán đổi ca và điều chỉnh giờ chót cao do biến động tải không dự
  báo trước.

**Tác động tài chính & Vận hành:**

- **Lãng phí chi phí nhân công:** Thừa 10-14 giờ công/chi nhánh/tuần
  trong khung giờ thấp điểm. Dẫn đến lãng phí 200-320 triệu VNĐ/năm trên
  toàn hệ thống.

- **Suy giảm chất lượng dịch vụ:** Khung giờ cao điểm thiếu hụt nhân lực
  làm tăng thời gian chờ của khách hàng (\>15 phút), giảm 8%-12% doanh
  thu F&B và dịch vụ bổ trợ.

- **Tỷ lệ nhân sự thời vụ khẩn cấp cao:** 25%-30% tổng số ca trực phải
  huy động nhân sự thời vụ chi phí cao, làm giảm tính ổn định trong chất
  lượng dịch vụ.

## 2. Giải pháp kỹ thuật AI & Xử lý bài toán Cold-Start

- **Đề xuất công nghệ:** Áp dụng Mô hình Nền tảng Chuỗi thời gian (Time
  Series Foundation Model - TSFM) tiên tiến như **Google TimesFM** hoặc
  **Amazon Chronos**.

- **Ưu thế kỹ thuật vượt trội:**

- **Khả năng suy luận Zero-shot:** Các mô hình truyền thống (ARIMA,
  XGBoost) yêu cầu dữ liệu lịch sử tối thiểu 3-6 tháng tại điểm bán.
  TSFM được huấn luyện tiền diện rộng trên hàng tỷ chuỗi thời gian, cho
  phép dự báo ngay lập tức đối với chi nhánh mới khai trương.

- **Xử lý bài toán Khởi động lạnh (Cold-Start):** Giải quyết triệt để
  bài toán thiếu dữ liệu tại các cơ sở mới mở bằng cách kết hợp tri thức
  tổng quát của mô hình nền tảng với các biến ngoại cảnh (vị trí, quy
  mô, ngày lễ, lịch thi học sinh/sinh viên).

- **Tích hợp biến đa chiều (Covariates):** Tự động cập nhật các yếu tố
  chu kỳ (giờ/ngày/tuần), sự kiện khuyến mãi, giải đấu Esport, và lịch
  hoạt động khu vực lân cận.

## 3. Mục tiêu & Hệ thống KPI đo lường thành công

**Mục tiêu SMART:** Xây dựng hệ thống dự báo lưu lượng khách theo khung
giờ (tầm nhìn 7-14 ngày) với độ chính xác MAPE \< 15% cho các cơ sở ổn
định và \< 25% cho cơ sở mới; giảm ≥ 40% chi phí huy động nhân sự thời
vụ khẩn cấp sau 3 tháng vận hành.

  ---------- -------------- ------------- ------------- ------------------ -----------
    **Nhóm   **Chỉ số đo    **Hiện tại    **Mục tiêu    **Phương pháp kiểm **Trách
    KPI**    lường**        (AS-IS)**     (TO-BE)**     tra**              nhiệm**

  **Mô hình  Sai số dự báo  Chưa định     \< 15% (Toàn  Đối soát dữ liệu   Lead Data
     AI**    (MAPE)\        lượng\        chuỗi), \<    thực tế hằng       Scientist /
             Tầm nhìn dự    0 ngày\       20% (Cao      tuần.\             ML Engineer
             báo\           N/A\          điểm)\        Kiểm tra Dashboard / Data
             Thời gian xử   24 - 48h (Thủ 7 - 14 ngày   hiển thị.\         Engineer
             lý (Latency)\  công)         (Chi tiết     Log giám sát hệ    
             Tần suất Batch               theo giờ)\    thống.\            
             job                          \< 3s/chi     Workflow Airflow   
                                          nhánh, \< 2   pipeline.          
                                          phút/toàn                        
                                          chuỗi\                           
                                          Tự động hằng                     
                                          ngày (Trước                      
                                          04:00 AM)                        

  **Vận hành Tỷ lệ ca thuê  25% - 30%\    \< 10% tổng   Báo cáo HR hằng    Trưởng
    & Kinh   khẩn cấp\      15% - 20%\    số ca\        tháng.\            phòng Điều
   doanh**   Lãng phí giờ   6 - 8h/chi    \< 5% tổng    Dữ liệu chấm công  phối /
             công (Thấp     nhánh/tuần\   giờ làm việc\ tự động.\          Trưởng
             điểm)\         \~75%         \< 1.5h/chi   Khảo sát Quản lý   phòng HR /
             Thời gian lập                nhánh/tuần\   chi nhánh.\        COO
             lịch tuần\                   ≥ 95% khách   Đánh giá CSAT &    
             SLA phục vụ                  phục vụ \< 5  Time-to-service.   
             khách hàng                   phút                             
  ---------- -------------- ------------- ------------- ------------------ -----------

## 4. Phạm vi triển khai dự án (Scope of Work)

**Phạm vi thực hiện (In-scope):**

- Xây dựng Pipeline tự động trích xuất dữ liệu giao dịch/lượt khách theo
  giờ từ 5 mảng dịch vụ (Gaming, Gym, Bida, Cầu lông, Hub) qua API Lớp 4
  về Data Warehouse Lớp 5.

- Thu thập và tiền xử lý dữ liệu biến ngoại cảnh (Lịch lễ tết, lịch thi
  đấu, sự kiện khu vực, chương trình khuyến mãi).

- Huấn luyện, tinh chỉnh (Fine-tuning) và triển khai mô hình TSFM
  (TimesFM/Chronos) phục vụ dự báo lưu lượng khách.

- Phát triển thuật toán quy đổi tự động từ \"Lượng khách dự báo\" sang
  \"Định mức nhân sự cần thiết\" theo từng vị trí (Thu ngân, Pha chế, Kỹ
  thuật, Phục vụ, Bảo vệ).

- Xây dựng Dashboard quản trị điều phối nhân sự và tích hợp đầu ra với
  phần mềm Quản lý Nhân sự (HRM).

**Ngoài phạm vi thực hiện (Out-of-scope):**

- Tự động phân công đích danh nhân sự cụ thể vào ca (Quyền quyết định
  thuộc về Quản lý chi nhánh).

- Tính toán lương, thưởng, phúc lợi hoặc quản lý đơn từ nghỉ phép.

- Sử dụng dữ liệu nhận diện hình ảnh/Camera AI đếm người tại điểm bán
  (Đảm bảo tuân thủ tính riêng tư và tuân thủ NĐ 13).

- Đầu tư thêm hạ tầng phần cứng Server/GPU cục bộ tại các điểm bán.

## 5. Giả định & Ràng buộc kỹ thuật

- **Ràng buộc phụ thuộc:** Dự án AI phụ thuộc hoàn toàn vào tiến độ hoàn
  thành Kho dữ liệu (Data Warehouse Lớp 5) từ Dự án Hạ tầng.

- **Tuân thủ pháp lý:** Dữ liệu đầu vào mô hình AI là con số thống kê đã
  ẩn danh hóa 100%, tuyệt đối không sử dụng thông tin định danh cá nhân
  (PII) hay dữ liệu sinh trắc học.

- **Tối ưu chi phí hạ tầng:** Tận dụng cơ chế Batch Processing chạy tự
  động vào khung giờ thấp điểm (03:00 - 04:00 AM) trên Serverless Cloud
  để tối ưu chi phí tài nguyên máy tính.
