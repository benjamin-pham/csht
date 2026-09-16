# Giải Thích Các Thuật Ngữ Kỹ Thuật & Nghiệp Vụ Trong Báo Cáo Thực Hành
*(Đính kèm theo tài liệu: ThucHanh_Final_v2.md)*

Dưới đây là danh sách giải thích chi tiết các thuật ngữ chuyên môn và công thức tính toán được sử dụng trong bài thực hành ứng dụng AI dự báo lưu lượng khách hàng.

## 1. Giải thích các thuật ngữ chuyên môn

### 1.1. Nhóm Trí tuệ Nhân tạo (AI) & Học máy (Machine Learning)
*   **Time-Series Foundation Models (TSFM):** Mô hình nền tảng cho chuỗi thời gian. Đây là các mô hình AI lớn được huấn luyện sẵn trên khối lượng dữ liệu khổng lồ, chuyên dùng để nhận diện quy luật và dự báo các dữ liệu mang tính thời gian (ví dụ: lượng khách thay đổi theo giờ).
*   **Deep Learning (Học sâu):** Một tập hợp các thuật toán học máy dựa trên mạng nơ-ron nhân tạo nhiều lớp, có khả năng học các biểu diễn dữ liệu phức tạp.
*   **LSTM / BiLSTM, Prophet, ARIMA:** Tên của các thuật toán dự báo chuỗi thời gian phổ biến từ truyền thống đến hiện đại mà nhóm sẽ thực nghiệm để chọn ra phương pháp tốt nhất.
*   **Batch Inference (Suy luận hàng loạt):** Việc chạy mô hình AI để dự đoán kết quả cho một lượng lớn dữ liệu cùng một lúc (thường chạy theo lịch, ví dụ: 2 giờ sáng hàng ngày) thay vì dự báo từng lượt một.
*   **Data Drift:** Hiện tượng dịch chuyển dữ liệu. Xảy ra khi hành vi của khách hàng trong thực tế thay đổi đột ngột (ví dụ do thời tiết, thay đổi thị hiếu) khiến mô hình AI vốn đang dự báo đúng trở nên thiếu chính xác và cần được huấn luyện lại (tái huấn luyện).
*   **Model Registry:** Nơi lưu trữ, quản lý và theo dõi các phiên bản khác nhau của mô hình AI (nhóm sử dụng công cụ MLflow).

### 1.2. Nhóm Dữ liệu & Pipeline (Data Engineering)
*   **Data Pipeline:** Đường ống dữ liệu. Hệ thống tự động di chuyển dữ liệu từ nguồn (máy POS) qua các bước làm sạch, xử lý và đẩy vào kho dữ liệu.
*   **ETL / ELT (Extract, Transform, Load):** Quy trình trích xuất (lấy dữ liệu từ máy POS), chuyển đổi (làm sạch, ẩn danh, chuẩn hóa) và nạp dữ liệu (vào kho lưu trữ).
*   **Data Warehouse (Kho dữ liệu):** Nơi lưu trữ tập trung khối lượng lớn dữ liệu đã qua xử lý để phục vụ cho báo cáo và huấn luyện AI.
*   **DAG (Directed Acyclic Graph):** Đồ thị có hướng không chu trình. Trong hệ thống Apache Airflow, DAG đại diện cho một luồng công việc tự động (workflow) quy định thứ tự chạy của các tác vụ xử lý dữ liệu.

### 1.3. Nhóm Phần mềm & Vận hành (Software & DevOps)
*   **API (Application Programming Interface):** Giao diện lập trình ứng dụng. Phương thức để phần mềm dự báo AI gửi dữ liệu kết quả về cho hệ thống hiển thị (Dashboard) của Quản lý chi nhánh.
*   **RESTful API:** Một tiêu chuẩn thiết kế kiến trúc API phổ biến dùng trên nền tảng Web.
*   **Webhook:** Cơ chế cho phép hệ thống tự động đẩy thông tin/cảnh báo (push) sang ứng dụng khác (ví dụ: Slack, Email) ngay khi có sự kiện quan trọng (phát hiện giờ cao điểm).
*   **Cronjob:** Công cụ lập lịch chạy các tác vụ lặp đi lặp lại một cách tự động (ví dụ: chạy luồng rút dữ liệu vào 01:00 sáng mỗi ngày).
*   **CCU (Concurrent Users):** Số lượng người dùng kết nối hoặc truy cập đồng thời vào hệ thống API (Đồ án kiểm thử ở mức 500 CCU).
*   **Hypercare:** Giai đoạn "chăm sóc đặc biệt" ngay sau khi hệ thống chính thức ra mắt (Go-live). Đội ngũ IT sẽ túc trực, theo dõi sát sao để sửa lỗi lập tức nếu có.

### 1.4. Nhóm Quản lý dự án & Nghiệp vụ
*   **DSS (Decision Support System):** Hệ thống hỗ trợ ra quyết định. Đề tài xây dựng hệ thống AI này không thay con người quyết định mà chỉ cung cấp số liệu dự báo để Quản lý chi nhánh dễ dàng quyết định phân bổ nhân sự (xếp ca).
*   **SLA (Service Level Agreement):** Cam kết mức độ dịch vụ. Các chỉ số mà đội ngũ IT cam kết hệ thống phải đạt được (ví dụ: hệ thống không được sập quá 43,2 phút/tháng).
*   **CAPEX / OPEX / TCO:** CAPEX là chi phí đầu tư ban đầu; OPEX là chi phí vận hành định kỳ hàng năm; TCO là Tổng chi phí sở hữu dự án trong một khoảng thời gian (như 3 năm).

---

## 2. Giải Thích Các Công Thức Tính Toán & KPI

### 2.1. Nhóm chỉ số đánh giá Mô hình AI (Nhóm A)

**1. A.1 – MAPE (Mean Absolute Percentage Error)**
*   *Công thức:* $\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%$
*   *Giải thích:*
    *   $y_i$: Lượng khách thực tế.
    *   $\hat{y}_i$: Lượng khách mô hình AI dự báo.
    *   $n$: Số lượng mẫu dự báo.
*   *Ý nghĩa:* Tỷ lệ sai số phần trăm tuyệt đối trung bình. Phản ánh trung bình mô hình dự báo sai lệch bao nhiêu phần trăm so với thực tế. Đồ án yêu cầu MAPE < 15% khi thử nghiệm và < 10% khi vận hành thực tế (sai số càng nhỏ càng tốt).

**2. A.2 – MAE (Mean Absolute Error)**
*   *Công thức:* $\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$
*   *Ý nghĩa:* Sai lệch số lượng khách cụ thể trung bình. Đồ án đặt mức MAE $\le 3$, nghĩa là trung bình mô hình dự báo lệch so với thực tế không quá 3 khách mỗi giờ, giúp quản lý tin tưởng để xếp ca.

**3. A.3 – Precision (Độ chuẩn xác nhận diện Giờ cao điểm)**
*   *Công thức:* $\text{Precision} = \frac{TP}{TP + FP}$
*   *Giải thích:* 
    *   $TP$ (True Positive): Số lần cảnh báo giờ cao điểm ĐÚNG.
    *   $FP$ (False Positive): Số lần cảnh báo giờ cao điểm SAI (Báo động giả).
*   *Ý nghĩa:* Đồ án yêu cầu Precision $\ge 85\%$, tức là trong 100 lần hệ thống báo động "Sắp có giờ cao điểm", ít nhất 85 lần là đúng sự thật, tránh báo động giả làm lãng phí nhân sự.

**4. A.5 – Độ ổn định đa ngữ cảnh (Δ MAPE)**
*   *Công thức:* $\Delta = \max(\text{MAPE}_j) - \min(\text{MAPE}_j)$
*   *Ý nghĩa:* Chênh lệch mức sai số giữa chi nhánh hoạt động tốt nhất và tệ nhất. Đảm bảo mô hình AI dự báo đều đặn trên tất cả các dịch vụ (Gym, Gaming, Hub) thay vì chỉ giỏi ở một dịch vụ (Đòi hỏi độ chênh lệch $\le 10\%$).

### 2.2. Nhóm chỉ số Phần mềm & Vận hành (Nhóm B)

**5. B.1 – API Response Time P95 (Độ trễ API)**
*   *Ý nghĩa:* P95 $\le 500$ ms nghĩa là 95% số lượng truy vấn/yêu cầu lấy dữ liệu dự báo từ Quản lý chi nhánh phải được hệ thống trả về kết quả trong thời gian nhỏ hơn hoặc bằng 500 mili-giây (0,5 giây).

**6. B.3 – Uptime (Tính sẵn sàng của dịch vụ)**
*   *Công thức:* $\text{Uptime} = \frac{\text{Total Time} - \text{Downtime}}{\text{Total Time}} \times 100\%$
*   *Ý nghĩa:* Đảm bảo phần mềm không bị sập hay mất kết nối. Đạt mức $\ge 99,9\%$ tương đương thời gian sập tối đa cho phép là 43,2 phút mỗi tháng.

**7. B.4 – Data Completeness (Tính toàn vẹn dữ liệu)**
*   *Công thức:* $\frac{\text{Số bản ghi nạp thành công}}{\text{Tổng số bản ghi gốc tại POS}} \times 100\%$
*   *Ý nghĩa:* Đảm bảo không mất mát dữ liệu khi chuyển từ máy tính tiền (POS) lên kho dữ liệu (Yêu cầu $\ge 99,5\%$).

**8. B.5 – Batch Data Freshness (Độ trễ đồng bộ)**
*   *Công thức:* $\Delta t = t_{\text{Data Warehouse}} - t_{\text{POS}} \le 24\ \text{h}$
*   *Ý nghĩa:* Dữ liệu của ngày hôm qua phải được cập nhật hoàn tất lên kho dữ liệu đám mây trong vòng 24 giờ để có số liệu huấn luyện mô hình cho ngày hôm nay.

**9. B.6 – Error Rate (Tỷ lệ lỗi hệ thống)**
*   *Công thức:* $\frac{\text{Số phản hồi lỗi từ máy chủ (HTTP 5xx)}}{\text{Tổng số request}} \times 100\%$
*   *Ý nghĩa:* Khi người dùng gọi API, tỷ lệ trả về lỗi sập máy chủ phải nhỏ hơn 0,1%.

**10. B.7 – MTTD (Mean Time To Detect - Thời gian phát hiện sự cố)**
*   *Ý nghĩa:* Bất kỳ khi nào hệ thống hỏng hóc hoặc luồng dữ liệu bị lỗi, các công cụ giám sát phải tự động phát hiện và cảnh báo cho kỹ sư (Alert) trong thời gian trung bình $\le 15$ phút, nhanh hơn rất nhiều so với việc chờ nhân viên gọi báo lỗi.

