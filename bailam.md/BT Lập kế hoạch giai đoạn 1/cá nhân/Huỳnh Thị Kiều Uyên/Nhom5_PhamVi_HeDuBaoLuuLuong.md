**BÁO CÁO BÀI TẬP**

**XÁC ĐỊNH PHẠM VI ĐẦU TƯ NĂNG LỰC CNTT**

*Đề tài: Xây dựng năng lực dự báo lưu lượng khách theo khung giờ cho hệ
thống Ways Station*

# Bước 0 --- Chuẩn bị đầu vào

**Tài liệu khảo sát đã thu thập**

- Khảo sát tổng quan doanh nghiệp: lịch sử phát triển, quy mô, phạm vi
  hoạt động, cơ cấu tổ chức.

- Sản phẩm Bước 0 đã nộp trước đó: phạm vi đầu tư Lớp (4) App &
  Integration Platform và Lớp (5) Data Platform.

- Khung tham chiếu Lớp năng lực hạ tầng CNTT (IT Capability Layers
  Model).

- Cổng thông tin dịch vụ chính thức: waysstation.vn, diachi.ways.vn
  (danh sách chi nhánh, quy định đặt giờ, bảng giá).

- Phản hồi vận hành thực tế từ khách hàng trên Google Maps và
  Trustindex.

- Bản mẫu giao diện (mockup) màn hình dự báo dành cho Phòng Điều phối.

**Hiện trạng dữ liệu (AS-IS)**

- Mức độ số hóa không đồng đều giữa các mảng dịch vụ: Gym có hệ thống
  nhận diện khuôn mặt, Gaming có phần mềm quản lý; Billiards, Cầu lông
  và Hub vẫn ghi nhận thủ công.

- Số liệu công suất sử dụng (bàn / máy / sân / chỗ ngồi) được đếm tay
  theo khung giờ chẵn, độ phân giải 2 giờ, lưu rời rạc trên Excel và
  Google Drive theo từng ca và từng chi nhánh.

- Chưa có kho dữ liệu tập trung; chưa có lịch sử lưu lượng ở dạng chuẩn
  hóa dùng được cho phân tích.

- Toàn bộ báo cáo hiện có chỉ mô tả những gì đã xảy ra; chưa có bất kỳ
  năng lực dự báo nào.

- Việc xếp ca, nhập hàng và lên chương trình khuyến mãi đang dựa vào
  kinh nghiệm cá nhân của quản lý chi nhánh.

**Kết luận đầu vào**

Đề tài này kế thừa hai lớp năng lực đã xác định. Năng lực dự báo là phần
mở rộng tự nhiên của Lớp (5) Data Platform: chuyển hệ thống từ chỗ báo
cáo quá khứ sang chỗ ước lượng được tương lai. Đề tài không đề xuất đầu
tư hạ tầng tính toán hay lưu trữ mới.

# Bước 1 --- Tên đề tài và thông tin chung

  --------------------------------------------------------------------
  **Hạng mục**      **Nội dung**
  ----------------- --------------------------------------------------
  Tên đề tài        Xây dựng năng lực dự báo lưu lượng khách theo
                    khung giờ phục vụ điều phối nhân sự, dự trữ hàng
                    hóa và hoạt động marketing tại hệ thống Ways
                    Station

  Lớp năng lực      Mở rộng Lớp (5) Data Platform; sử dụng dữ liệu do
                    Lớp (4) App & Integration Platform cung cấp

  Đơn vị chủ trì    Bộ phận Dữ liệu & Phân tích

  Đơn vị thụ hưởng  Phòng Điều phối, Bộ phận Marketing, Bộ phận Cung
                    ứng, Quản lý khu vực và chi nhánh

  Thời lượng        06 tháng, triển khai sau khi Lớp (4) hoàn tất giai
                    đoạn thí điểm

  Điều kiện tiên    Đường ống dữ liệu của Lớp (5) đã vận hành ổn định;
  quyết             check-in được ghi nhận ở dạng số tại các chi nhánh
                    thí điểm

  Sản phẩm bàn giao Đường ống dự báo tự động; màn hình dự báo cho
                    Phòng Điều phối; bộ tài liệu vận hành và chuyển
                    giao
  --------------------------------------------------------------------

# Bước 2 --- Bối cảnh và lý do chọn đề tài (Business Case)

**Bối cảnh**

Ways Station vận hành hơn 30 chi nhánh tại TP.HCM, mở cửa 24/7 xuyên lễ,
mỗi chi nhánh có một tổ hợp dịch vụ khác nhau. Chuỗi mở rộng nhanh: từ
22 lên hơn 34 chi nhánh trong chưa đầy hai năm. Nhóm khách hàng chủ lực
là sinh viên và giới trẻ, khiến nhu cầu biến động mạnh theo lịch học,
mùa thi, kỳ nghỉ và các dịp lễ hội.

**Ba nhóm vấn đề đang tồn tại**

- Tác động vận hành: nhân sự được xếp theo cảm tính nên thừa người ở
  khung giờ vắng và thiếu người ở khung giờ cao điểm; hàng hóa nhập theo
  kinh nghiệm nên thường xuyên thiếu hàng đúng lúc đông khách. Cả hai
  đều làm giảm chất lượng chăm sóc khách hàng và tăng chi phí.

- Tác động trong các dịp đặc biệt: lễ, hội, kỳ nghỉ dài và mùa thi làm
  nhu cầu biến động rất mạnh, và biến động này ngược chiều nhau giữa các
  mảng dịch vụ. Không có công cụ nào giúp lượng hóa trước mức độ biến
  động, nên các dịp lẽ ra là cơ hội doanh thu lại trở thành thời điểm
  rủi ro vận hành.

- Tác động chiến lược: mỗi chi nhánh mới khai trương đều không có căn cứ
  nào để xếp ca và nhập hàng trong hai đến ba tháng đầu, trong khi đây
  chính là giai đoạn quyết định ấn tượng ban đầu của khách hàng. Tốc độ
  mở chi nhánh càng nhanh thì thiệt hại tích lũy càng lớn.

**Vì sao phải đầu tư ngay lúc này**

Lớp (4) và Lớp (5) đang trong lộ trình triển khai và sẽ tạo ra dòng dữ
liệu chuẩn hóa đầu tiên của doanh nghiệp. Nếu năng lực dự báo được thiết
kế đồng thời, các yêu cầu về độ phân giải thời gian, trường dữ liệu và
quy tắc chất lượng sẽ được đưa vào ngay từ khâu thiết kế đường ống. Nếu
để sau, doanh nghiệp sẽ phải sửa lại đường ống và chờ thêm nhiều tháng
tích lũy dữ liệu, làm chậm toàn bộ lợi ích.

**Rủi ro nếu không đầu tư**

  ---------------------------------------------------------------------
  **Rủi ro**            **Ảnh hưởng**            **Biện pháp của đề
                                                 tài**
  --------------------- ------------------------ ----------------------
  Xếp ca sai nhu cầu    Chi phí nhân sự lãng phí Cung cấp mức dự báo
                        ở giờ vắng; khách chờ    theo từng khung giờ
                        lâu và trải nghiệm kém ở cho từng chi nhánh và
                        giờ cao điểm             dịch vụ

  Thiếu hàng vào dịp    Mất doanh thu trực tiếp; Cung cấp cận trên của
  cao điểm              khách chuyển sang đối    dự báo làm căn cứ đặt
                        thủ                      mức tồn kho

  Khuyến mãi sai khung  Giảm giá vào giờ vốn đã  Xác định khung giờ
  giờ                   đông, không kéo thêm     vắng có độ tin cậy cao
                        khách vào giờ vắng       để nhắm mục tiêu

  Chi nhánh mới vận     Ấn tượng ban đầu kém,    Dự báo tham chiếu từ
  hành mò mẫm           kéo dài thời gian hòa    nhóm chi nhánh tương
                        vốn                      đồng ngay từ ngày khai
                                                 trương

  Dữ liệu tiếp tục phân Không thể phân tích,     Chuẩn hóa dữ liệu lưu
  mảnh                  không thể mở rộng, phụ   lượng thành một nguồn
                        thuộc cá nhân            dùng chung
  ---------------------------------------------------------------------

# Bước 3 --- Mục tiêu, KPI và tiêu chí thành công

**Mục tiêu tổng quát**

Xây dựng năng lực dự báo lưu lượng khách theo khung giờ cho từng chi
nhánh và từng mảng dịch vụ trong tối thiểu 7 ngày tới, có tính đến các
dịp lễ, hội, kỳ nghỉ dài và ngày đặc biệt, để Phòng Điều phối, Marketing
và Cung ứng chủ động ra quyết định thay vì xử lý bị động.

**Hệ thống KPI ba tầng**

KPI được tách làm ba tầng vì chúng thuộc ba phạm vi trách nhiệm khác
nhau. Tầng nền tảng là điều kiện cần của tầng mô hình; tầng mô hình là
điều kiện cần của tầng nghiệp vụ. Đầu tư hạ tầng tác động trực tiếp lên
tầng nền tảng.

  ----------------------------------------------------------------------
  **Tầng**   **Chỉ số**               **Hiện        **Mục      **Thời
                                      trạng**       tiêu**     điểm đo**
  ---------- ------------------------ ------------- ---------- ---------
  Nền tảng   Tỷ lệ chi nhánh ghi nhận Không đồng    100%       Sau
             check-in ở dạng số       đều, chưa                go-live 3
                                      thống kê                 tháng

  Nền tảng   Tỷ lệ ca làm việc có dữ  Chưa đo được  ≥ 98%      Sau
             liệu đầy đủ                                       go-live 3
                                                               tháng

  Nền tảng   Tỷ lệ lượt chạy đường    Chưa có đường ≥ 99%      Sau
             ống thành công           ống                      go-live 1
                                                               tháng

  Nền tảng   Độ trễ dữ liệu đầu vào   Thủ công,     ≤ 24 giờ   Sau
             của mô hình              không xác                go-live 1
                                      định                     tháng

  Mô hình    Sai số dự báo trên các   Không có dự   ≤ 15%      Sau
             khung giờ hoạt động      báo                      go-live 6
             chính                                             tháng

  Mô hình    Tầm dự báo               Không có      ≥ 7 ngày   Sau
                                                               go-live 3
                                                               tháng

  Mô hình    Độ phủ thực tế của       Không có      85% -- 95% Sau
             khoảng dự báo 90%                                 go-live 6
                                                               tháng

  Mô hình    Thời gian có dự báo cho  Không có      ≤ 24 giờ   Sau
             chi nhánh mới                          từ khai    go-live 6
                                                    trương     tháng

  Nghiệp vụ  Tỷ lệ ca được xếp dựa    0%            ≥ 70%      Sau
             trên dự báo                                       go-live 6
                                                               tháng

  Nghiệp vụ  Tỷ lệ đề xuất nhân sự    Không áp dụng ≥ 60%      Sau
             được Phòng Điều phối                              go-live 6
             chấp nhận                                         tháng

  Nghiệp vụ  Số lần thiếu hàng ở      Chưa thống kê Giảm 50%   Sau
             khung giờ cao điểm                                go-live 6
                                                               tháng
  ----------------------------------------------------------------------

**Tiêu chí thành công tổng thể**

Đề tài được coi là thành công khi Phòng Điều phối sử dụng kết quả dự báo
như một đầu vào thường xuyên của quy trình xếp ca hằng tuần, và khi cả
ba bộ phận thụ hưởng cùng khai thác một nguồn dự báo duy nhất thay vì tự
ước lượng riêng lẻ.

# Bước 4 --- Đối tượng, phạm vi và giả định / ràng buộc

**Đối tượng phục vụ**

  ---------------------------------------------------------------------
  **Đối tượng**    **Nhu cầu**                   **Giá trị nhận được**
  ---------------- ----------------------------- ----------------------
  Phòng Điều phối  Biết trước khung giờ nào đông Mức dự báo và số nhân
                   để bố trí đủ người            sự đề xuất theo từng
                                                 khung giờ, kèm quyền
                                                 chấp nhận hoặc điều
                                                 chỉnh

  Bộ phận Cung ứng Nhập đủ hàng, không thiếu vào Cận trên của dự báo
                   giờ cao điểm                  làm căn cứ đặt mức tồn
                                                 kho theo mức phục vụ
                                                 mong muốn

  Bộ phận          Nhắm khuyến mãi vào đúng      Danh sách khung giờ dự
  Marketing        khung giờ vắng                báo thấp với độ tin
                                                 cậy cao

  Quản lý khu vực  Chủ động chuẩn bị cho dịp lễ  Cảnh báo sớm các khung
  / chi nhánh      và kỳ nghỉ                    giờ vượt ngưỡng phục
                                                 vụ hiện tại
  ---------------------------------------------------------------------

**Trong phạm vi**

- Dự báo số lượt khách theo khung giờ cho từng chi nhánh và từng mảng
  dịch vụ, tầm dự báo tối thiểu 7 ngày.

- Xử lý ảnh hưởng của ngày lễ, ngày hội, kỳ nghỉ dài, mùa thi và các
  ngày đặc biệt theo cả lịch dương và lịch âm.

- Dự báo tham chiếu cho chi nhánh mới chưa có dữ liệu lịch sử.

- Kết quả dự báo dạng khoảng, kèm nhãn độ tin cậy cho từng khung giờ.

- Đề xuất số nhân sự cho mỗi khung giờ; quyết định cuối cùng thuộc về
  con người.

- Màn hình dự báo dành cho Phòng Điều phối và cơ chế ghi nhận phản hồi
  chấp nhận hoặc điều chỉnh.

- Quy tắc kiểm soát chất lượng dữ liệu đầu vào và ba luồng xử lý ngoại
  lệ.

**Ngoài phạm vi**

- Tự động sinh và tự động áp dụng lịch làm việc cho từng nhân viên.

- Phân tích hành vi từng khách hàng cá nhân và thiết kế gói combo.

- Dự báo doanh thu, chi phí hoặc các chỉ số tài chính.

- Xử lý dữ liệu hình ảnh hoặc video từ hệ thống camera.

- Đầu tư máy chủ, thiết bị lưu trữ và hạ tầng mạng --- thuộc phạm vi lớp
  năng lực khác.

- Thay thế các phần mềm quản lý nghiệp vụ hiện hữu của từng mảng dịch
  vụ.

**Giả định**

- Hạ tầng tính toán và lưu trữ được kế thừa từ Lớp (1) hoặc thuê ngoài,
  không nằm trong dự toán của đề tài.

- Lớp (4) hoàn thành giai đoạn thí điểm đúng tiến độ và cung cấp được
  luồng sự kiện check-in chuẩn hóa.

- Doanh nghiệp đồng ý số hóa việc ghi nhận check-in tại các mảng dịch vụ
  hiện còn đếm tay.

- Lịch lễ, lịch thi và lịch nghỉ của các trường đại học trọng điểm trong
  khu vực được cập nhật trước tối thiểu 30 ngày.

- Danh mục chi nhánh, dịch vụ và sức chứa được chuẩn hóa và duy trì bởi
  Lớp (5).

**Ràng buộc**

- Dữ liệu hiện tại có độ phân giải 2 giờ. Giai đoạn đầu, hệ thống dự báo
  theo đúng độ phân giải này; chỉ nâng lên mức chi tiết hơn sau khi việc
  số hóa check-in hoàn tất.

- Trong giai đoạn nghiên cứu và trình bày học thuật, nhóm không sử dụng
  dữ liệu kinh doanh thật của doanh nghiệp. Việc kiểm chứng sử dụng bộ
  dữ liệu mô phỏng có cấu trúc mùa vụ tương đương; các KPI về sai số chỉ
  được xác nhận chính thức trong giai đoạn thí điểm với dữ liệu thật.

- Số lượng bàn, máy, sân và chỗ ngồi tại mỗi chi nhánh là hữu hạn, nên
  lưu lượng thực tế bị chặn trần ở khung giờ cao điểm. Kết quả dự báo
  phải được diễn giải cùng với sức chứa.

- Các sự kiện bất thường không báo trước không thể dự báo được. Hệ thống
  chỉ gắn nhãn độ tin cậy thấp và nhường quyết định cho người điều phối.

- Chi nhánh mở mới liên tục, nên hệ thống phải hoạt động được ngay cả
  khi một phần chuỗi chưa có lịch sử.

- Dữ liệu cá nhân của khách hàng phải được che hoặc mã hóa theo quy định
  phân quyền của Lớp (5).

# Nhánh kỹ thuật dự kiến áp dụng

Đề tài xác định nhánh kỹ thuật, không chốt sản phẩm hay thuật toán cụ
thể. Mỗi nhánh dưới đây là một họ giải pháp gồm nhiều lựa chọn tương
đương về mặt kiến trúc; nếu một lựa chọn không đạt yêu cầu khi thử
nghiệm, có thể thay bằng lựa chọn khác trong cùng nhánh mà không phải
thiết kế lại hệ thống. Cột cuối nêu tiêu chí để chọn giải pháp trong
nhánh, phục vụ bước chuẩn hóa yêu cầu kỹ thuật và chấm thầu.

**Nhóm A --- Nhánh mô hình dự báo**

+-------------------+-----------------------+-----------------------+
| **Nhánh kỹ        | **Vai trò trong hệ    | **Tiêu chí chọn giải  |
| thuật**           | thống**               | pháp trong nhánh**    |
+===================+=======================+=======================+
| Time Series       | Sinh dự báo cho chi   | Độ dài cửa sổ ngữ     |
| Foundation Model  | nhánh mới chưa có dữ  | cảnh; khả năng nhận   |
|                   | liệu lịch sử, không   | biến ngoại sinh; giấy |
| (Mô hình nền tảng | cần huấn luyện riêng  | phép sử dụng thương   |
| chuỗi thời gian)  |                       | mại; chi phí suy luận |
+-------------------+-----------------------+-----------------------+
| Gradient Boosting | Mô hình chủ lực cho   | Hỗ trợ hàm mất mát    |
| Decision Trees    | chi nhánh đã có lịch  | phân vị; tốc độ huấn  |
|                   | sử; tiếp nhận trực    | luyện lại hằng ngày;  |
| (Cây quyết định   | tiếp biến lễ, hội, kỳ | khả năng giải thích   |
| tăng cường)       | nghỉ, mùa thi         | mức đóng góp của từng |
|                   |                       | biến                  |
+-------------------+-----------------------+-----------------------+
| Classical         | Mốc đối chiếu bắt     | Hỗ trợ đa chu kỳ mùa  |
| Statistical Time  | buộc để chứng minh mô | vụ (ngày và tuần);    |
| Series            | hình chính thực sự    | chi phí khớp lại mô   |
|                   | tốt hơn               | hình trên quy mô hàng |
| (Thống kê chuỗi   |                       | trăm chuỗi            |
| thời gian cổ      |                       |                       |
| điển)             |                       |                       |
+-------------------+-----------------------+-----------------------+
| Structural /      | Mốc đối chiếu thứ     | Khả năng khai báo     |
| Decomposition     | hai; diễn giải ảnh    | lịch lễ tùy biến gồm  |
| Models            | hưởng của từng dịp lễ | cả lịch âm; mức độ dễ |
|                   | cho người dùng nghiệp | đọc của kết quả phân  |
| (Mô hình phân rã  | vụ                    | rã                    |
| có thành phần     |                       |                       |
| ngày lễ)          |                       |                       |
+-------------------+-----------------------+-----------------------+
| Hierarchical      | Bảo đảm tổng dự báo   | Phương pháp điều hòa  |
| Forecasting &     | theo chi nhánh khớp   | được hỗ trợ; khả năng |
| Reconciliation    | với dự báo theo khu   | xử lý cấu trúc phân   |
|                   | vực và toàn chuỗi     | cấp không đều         |
| (Dự báo phân cấp  |                       |                       |
| và điều hòa)      |                       |                       |
+-------------------+-----------------------+-----------------------+
| Probabilistic /   | Cách đặt bài toán     | Số phân vị xuất được  |
| Quantile          | chung: xuất khoảng    | đồng thời; tính đơn   |
| Forecasting       | thay vì một con số    | điệu của các phân vị  |
|                   | duy nhất              |                       |
| (Dự báo xác suất  |                       |                       |
| theo phân vị)     |                       |                       |
+-------------------+-----------------------+-----------------------+
| Conformal         | Bảo đảm khoảng tin    | Hỗ trợ dữ liệu chuỗi  |
| Prediction        | cậy hiển thị phản ánh | thời gian; khả năng   |
|                   | đúng xác suất thực tế | hiệu chuẩn riêng theo |
| (Hiệu chuẩn       |                       | từng dịch vụ          |
| khoảng dự báo)    |                       |                       |
+-------------------+-----------------------+-----------------------+
| Anomaly & Outlier | Kiểm soát chất lượng  | Phân biệt được ca     |
| Detection         | dữ liệu đầu vào; sinh | vắng khách thật với   |
|                   | nhãn độ tin cậy thấp  | ca không ghi nhận; độ |
| (Phát hiện bất    |                       | trễ phát hiện         |
| thường)           |                       |                       |
+-------------------+-----------------------+-----------------------+

**Nhóm B --- Nhánh hạ tầng vận hành mô hình**

+-------------------+-----------------------+-----------------------+
| **Nhánh kỹ        | **Vai trò trong hệ    | **Tiêu chí chọn giải  |
| thuật**           | thống**               | pháp trong nhánh**    |
+===================+=======================+=======================+
| Feature Store &   | Quản lý tập trung các | Bảo đảm cùng một định |
| Calendar          | biến lịch: lễ dương,  | nghĩa biến giữa lúc   |
| Engineering       | lễ âm, mùa thi, kỳ    | huấn luyện và lúc dự  |
|                   | nghỉ, sự kiện chi     | báo; hỗ trợ truy vấn  |
| (Kho đặc trưng và | nhánh                 | theo thời điểm        |
| đặc trưng lịch)   |                       |                       |
+-------------------+-----------------------+-----------------------+
| Workflow          | Chạy đường ống dự báo | Cơ chế cảnh báo khi   |
| Orchestration     | theo lịch hằng ngày;  | thất bại; khả năng    |
|                   | xử lý phụ thuộc và    | chạy lại một phần;    |
| (Điều phối luồng  | chạy lại khi lỗi      | tích hợp với hệ giám  |
| công việc)        |                       | sát của Lớp (4)       |
+-------------------+-----------------------+-----------------------+
| MLOps & Model     | Lưu vết phiên bản mô  | Khả năng tái lập kết  |
| Registry          | hình, theo dõi sai số | quả; so sánh giữa các |
|                   | theo thời gian, phát  | phiên bản; quy trình  |
| (Quản lý vòng đời | hiện suy giảm chất    | phê duyệt trước khi   |
| và phiên bản mô   | lượng                 | đưa vào vận hành      |
| hình)             |                       |                       |
+-------------------+-----------------------+-----------------------+
| Data Quality &    | Chặn dữ liệu lỗi      | Khả năng khai báo quy |
| Validation        | trước khi vào mô      | tắc bằng cấu hình;    |
|                   | hình; kích hoạt luồng | báo cáo vi phạm theo  |
| (Kiểm định chất   | ngoại lệ              | chi nhánh             |
| lượng dữ liệu)    |                       |                       |
+-------------------+-----------------------+-----------------------+
| BI &              | Màn hình dự báo cho   | Hỗ trợ phân quyền     |
| Visualization     | Phòng Điều phối; ghi  | theo dòng và cột; tốc |
| Layer             | nhận phản hồi chấp    | độ tải; khả năng      |
|                   | nhận hoặc điều chỉnh  | nhúng vào ứng dụng    |
| (Trực quan hóa và |                       | nội bộ                |
| giao diện người   |                       |                       |
| dùng)             |                       |                       |
+-------------------+-----------------------+-----------------------+

# Ứng dụng thực tiễn khi hệ thống vận hành

Mục này mô tả những việc doanh nghiệp làm được sau khi có năng lực dự
báo, và làm bằng cách nào. Đây là căn cứ để lượng hóa lợi ích đầu tư.

  ----------------------------------------------------------------------
  **Ứng dụng**    **Bộ phận** **Cách sử dụng kết quả **Kết quả kỳ vọng**
                              dự báo**               
  --------------- ----------- ---------------------- -------------------
  Xếp ca theo nhu Phòng Điều  Lấy mức dự báo trung   Giảm giờ công thừa
  cầu thực        phối        vị của từng khung giờ, ở khung giờ vắng;
                              quy đổi ra số nhân sự  rút ngắn thời gian
                              theo tỷ lệ phục vụ của khách phải chờ ở
                              từng dịch vụ           khung giờ cao điểm

  Đặt mức tồn kho Cung ứng    Dùng cận trên của      Giảm số lần hết
  theo mức phục               khoảng dự báo làm mức  hàng vào giờ cao
  vụ                          đặt hàng cho nước, đồ  điểm mà không làm
                              ăn nhẹ, khăn và vật tư tăng tồn kho tồn
                              tiêu hao               đọng

  Khuyến mãi nhắm Marketing   Lọc các khung giờ có   Kéo khách vào giờ
  khung giờ vắng              cận trên của dự báo    thấp điểm thay vì
                              vẫn thấp hơn ngưỡng,   giảm giá ở giờ vốn
                              tức chắc chắn vắng, để đã đông
                              chạy giá ưu đãi        

  Cảnh báo vượt   Quản lý khu So mức dự báo với số   Chủ động điều động
  sức chứa        vực         bàn, máy, sân và chỗ   nhân sự hoặc hướng
                              ngồi hiện có của chi   khách sang chi
                              nhánh                  nhánh lân cận trước
                                                     khi quá tải

  Kế hoạch dịp lễ Ban điều    Xem dự báo cho tầm 14  Chuẩn bị nhân sự,
  và mùa thi      hành        ngày bao trùm dịp lễ,  hàng hóa và chương
                              hội, kỳ nghỉ dài và    trình trước tối
                              mùa thi của các trường thiểu hai tuần thay
                              lân cận                vì xử lý bị động

  Vận hành chi    Phòng Điều  Dùng dự báo tham chiếu Rút ngắn giai đoạn
  nhánh mới       phối        từ nhóm chi nhánh      vận hành mò mẫm từ
                              tương đồng ngay từ     vài tháng xuống còn
                              ngày khai trương       vài tuần

  Xếp lịch bảo    Kỹ thuật    Chọn khung giờ có dự   Bảo trì không làm
  trì thiết bị                báo thấp nhất trong    mất doanh thu giờ
                              tuần để bảo trì máy,   cao điểm
                              sân và thiết bị        

  Điều chỉnh giờ  Ban điều    Xem phân bố lưu lượng  Cắt bớt giờ vận
  mở của từng     hành        theo khung giờ của     hành gần như không
  dịch vụ                     từng mảng dịch vụ tại  có khách ở một số
                              từng chi nhánh         mảng, giảm chi phí
                                                     điện và nhân sự

  Kế hoạch tuyển  Nhân sự     Tổng hợp dự báo theo   Tuyển và đào tạo
  dụng thời vụ                tháng để ước lượng nhu trước mùa cao điểm
                              cầu nhân sự bán thời   thay vì tuyển gấp
                              gian theo mùa          khi đã quá tải

  Căn cứ mở chi   Ban Giám    Đối chiếu mô hình lưu  Chọn địa điểm và tổ
  nhánh mới       đốc         lượng giữa các khu vực hợp dịch vụ cho chi
                              và tổ hợp dịch vụ đang nhánh tiếp theo dựa
                              vận hành               trên số liệu
  ----------------------------------------------------------------------

# Điều kiện nghiệm thu chức năng

Tám hạng mục dưới đây là điều kiện thiết yếu để nghiệm thu chức năng dự
báo, kiểm chứng trên môi trường thật tại các chi nhánh thí điểm, có biên
bản xác nhận của đại diện Phòng Điều phối. Các hạng mục về độ chính xác
chỉ được đánh giá sau khi hạng mục 1 và 2 đã đạt, vì chất lượng dữ liệu
đầu vào là điều kiện cần của chất lượng dự báo.

  -------------------------------------------------------------------------
  **STT**   **Hạng mục**  **Ngưỡng đạt (định lượng)**  **Cách kiểm chứng**
  --------- ------------- ---------------------------- --------------------
  1         Độ đầy đủ dữ  Tỷ lệ ô thời gian có dữ liệu Đối chiếu báo cáo
            liệu đầu vào  ≥ 98% trên 30 ngày liên      chất lượng dữ liệu
                          tiếp; không chi nhánh nào có với sổ ca thủ công
                          tỷ lệ khuyết vượt 5%         trên mẫu 10 ca ngẫu
                                                       nhiên

  2         Sinh dự báo   Kết quả sẵn sàng trước 06:00 Nhật ký chạy đường
            đúng hạn và   trong 30/30 ngày; tỷ lệ chạy ống 30 ngày, đối
            đủ phạm vi    thành công ≥ 99%; 100% cặp   chiếu số bản ghi với
                          chi nhánh -- dịch vụ có đủ   danh mục chi nhánh
                          84 ô cho 7 ngày              

  3         Độ chính xác  Sai số tương đối ≤ 15% trên  Báo cáo so sánh dự
            dự báo        các ô có lưu lượng trung vị  báo với số thực tế,
                          từ 5 lượt trở lên; ≤ 10% khi tách riêng từng chi
                          tổng hợp ở mức ngày -- chi   nhánh
                          nhánh; đo liên tiếp 8 tuần   

  4         Vượt phương   Sai số thấp hơn phương án    Báo cáo so sánh có
            án đối chiếu  lặp lại tuần trước ít nhất   kiểm định trên toàn
                          20% tương đối, khác biệt có  bộ chuỗi và toàn bộ
                          ý nghĩa thống kê ở mức 5%    tuần đánh giá

  5         Hiệu chuẩn    Độ phủ thực tế của khoảng    Đếm tỷ lệ giá trị
            khoảng dự báo 90% nằm trong 85% -- 95%     thực rơi trong
                          (không quá hẹp và không quá  khoảng đã công bố,
                          rộng)                        đo trên 8 tuần

  6         Xử lý dịp lễ  Trong ít nhất 1 dịp lễ và 1  Báo cáo riêng cho
            và kỳ nghỉ    kỳ nghỉ dài, sai số không    từng dịp, đối chiếu
                          vượt quá 2 lần sai số ngày   cùng kỳ năm trước
                          thường                       nếu có dữ liệu

  7         Chi nhánh mới Có dự báo tham chiếu trong ≤ Thử nghiệm trên ít
                          24 giờ kể từ ngày khai       nhất 1 chi nhánh mới
                          trương; sai số ≤ 25% trong   thực tế
                          14 ngày đầu                  

  8         Mức chấp nhận Tỷ lệ đề xuất nhân sự được   Thống kê từ nhật ký
            của người     chấp nhận không sửa ≥ 60%    thao tác trên giao
            dùng          trong 4 tuần liên tiếp; ≥    diện
                          70% số ca trong tuần được    
                          xếp có tham chiếu dự báo     
  -------------------------------------------------------------------------

Các hạng mục nghiệm thu chung --- hiệu năng giao diện, phân quyền theo
vai trò, khả năng phục hồi sau sự cố và bộ tài liệu chuyển giao --- tuân
theo quy trình nghiệm thu đã quy định cho Lớp (4) và Lớp (5), không nhắc
lại trong bảng này.
