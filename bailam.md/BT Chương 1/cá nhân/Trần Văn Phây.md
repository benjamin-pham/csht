1.  **Data warehouse ([[Nguồn tham
    khảo]{.underline}](https://izisolution.vn/data-warehouse-la-gi-dac-diem-thanh-phan-va-vai-tro-doi-voi-he-thong-bi/))**

    a.  Khái niệm

        - [Data warehouse (kho dữ liệu) là hệ thống lưu trữ tập trung,
          có nhiệm vụ tập hợp và hợp nhất dữ liệu từ nhiều nguồn khác
          nhau (ví dụ như phần mềm bán hàng, kế toán, CRM,..). Thay vì
          lưu riêng ở từng hệ thống khác nhau, dữ liệu được lưu tập
          trung về 1 hệ thống nhằm mục đích phân tích dữ liệu, xây dựng
          báo cáo]{.mark}

    b.  Vai trò

        - [Lưu trữ dữ liệu tập trung, tạo ra 1 góc nhìn thống nhất về dữ
          liệu giúp doanh nghiệp hiểu rõ hơn về hoạt động của họ]{.mark}

        - [Giúp tối ưu hóa việc phân tích, báo cáo và hỗ trợ doanh
          nghiệp ra quyết định chính xác]{.mark}

        - [Lưu trữ toàn bộ dữ liệu lịch sử hỗ trợ doanh nghiệp phân tích
          sự thay đổi của dữ liệu , từ đó hiểu rõ hơn về xu hướng, biến
          động của doanh nghiệp]{.mark}

2.  **[Data lakehouse ([[Nguồn tham
    khảo]{.underline}](https://www.elcom.com.vn/data-lakehouse-la-gi-su-khac-biet-so-voi-data-warehouse-va-data-lake-1732525678))]{.mark}**

    a.  [Khái niệm]{.mark}

        - [Là sự kết hợp giữa Data lake (lưu trữ được mọi loại dữ liệu)
          và data warehouse, cho phép sử dụng **giải pháp lưu trữ với
          chi phí thấp để lưu trữ lượng lớn dữ liệu thô**, đồng thời
          cung cấp chức năng quản lý và tổ chức dữ liệu]{.mark}

    b.  [Vai trò]{.mark}

        - [Cho phép lưu trữ khối lượng lớn dữ liệu trên nền tảng đám mây
          với chi phí thấp, đồng thời không cần duy trì đồng thời cả
          Data Warehouse và Data Lake, **giảm chi phí vận hành**]{.mark}

        - [Tất cả dữ liệu được tập trung trong một kho duy nhất, cho
          phép kết nối trực tiếp với các công cụ mà không cần phải trích
          xuất hoặc chuẩn bị dữ liệu để đưa vào kho dữ liệu]{.mark}

3.  **[ETL/ELT ([[Nguồn tham
    khảo]{.underline}](https://viblo.asia/p/etl-va-elt-nhung-su-khac-biet-can-phai-biet-Ljy5VQGVlra))]{.mark}**

    a.  [Khái niệm]{.mark}

        - [ETL: Là viết tắt của **Extract, Transform, Load.** Đây là 1
          quá trình **Trích xuất** dữ liệu từ các hệ thống nguồn sau đó
          sẽ thực hiện quá trình **Chuyển đổi** dữ liệu (tính toán, nối
          chuỗi v.v. ) trước khi **Tải** dữ liệu vào hệ thống lưu trữ
          (Data warehouse/lakehouse). Hệ thống nguồn -\> Transform
          engine -\> DWH]{.mark}

        - [ELT: Là viết tắt của **Extract, Load, Transform.** Khác với
          **ETL, ELT** thực hiện chuyển đổi dữ liệu trực tiếp tại data
          warehouse]{.mark}

    b.  [Vai trò]{.mark}

        - [Chuẩn hoá và làm sạch dữ liệu]{.mark}

4.  [**MDM** ([**[Nguồn tham
    khảo]{.underline}**](https://fpt-is.com/goc-nhin-so/master-data-management-la-gi/))]{.mark}

    a.  [Khái niệm]{.mark}

        - [Là viết tắt của **Master Data Management** (Quản lý dữ liệu
          chủ). Là phương pháp quản lý dữ liệu tập trung vào việc duy
          trì, bảo vệ và quản lý data cốt lõi (Master Data) của 1 tổ
          chức (Khách hàng, Sản phẩm, Nhà cung cấp,..)]{.mark}

    b.  [Vai trò]{.mark}

        - [Giảm công sức khi kiểm tra, sửa chữa dữ liệu, từ đó giảm chi
          phí liên quan đến quản lý dữ liệu]{.mark}

        - [Giảm nguy cơ sai sót do thông tin lỗi thời, không đồng
          nhất]{.mark}

5.  **[Data Governance ([[Nguồn tham
    khảo]{.underline}](https://vnptai.io/vi/blog/detail/data-governance-la-gi))]{.mark}**

    a.  [Khái niệm]{.mark}

        - [Là một hệ thống nguyên tắc, quy trình và chính sách nhằm đảm
          bảo dữ liệu luôn được đạt tiêu chuẩn về chất lượng, bảo mật và
          khả năng truy cập]{.mark}

    b.  [Vai trò]{.mark}

        - [Dữ liệu được tổ chức và kiểm soát tốt giúp doanh nghiệp dễ
          dàng phân tích và đưa ra quyết định chính xác]{.mark}

        - [Phân quyền truy cập rõ ràng giúp các bộ phận trong doanh
          nghiệp khai thác dữ liệu linh hoạt hơn]{.mark}

        - [Hạn chế dữ liệu dư thừa giúp tiết kiệm chi phí quản lý và vận
          hành]{.mark}

6.  **[Data quality ([[Nguồn tham
    khảo]{.underline}](https://www.sap.com/resources/what-is-data-quality))]{.mark}**

    a.  [Khái niệm]{.mark}

        - [Là mức độ phù hợp và độ tin cậy của dữ liệu đối với mục đích
          sử dụng]{.mark}

    b.  [Vai trò]{.mark}

        - [Cung cấp nền tảng cho trí tuệ nhân tạo và học máy]{.mark}

        - [Giảm chi phí vận hành bằng cách loại bỏ việc làm lại và những
          điểm không hiệu quả]{.mark}

        - [Nâng cao sự hài lòng của khách hàng thông qua những trải
          nghiệm nhất quán và đáng tin cậy]{.mark}

7.  **[Data Catalog ([[Nguồn tham
    khảo]{.underline}](https://indaacademy.vn/dwh/data-catalog-la-gi-loi-ich-cua-data-catalog-doi-voi-doanh-nghiep/))]{.mark}**

    a.  [Khái niệm]{.mark}

        - [Là một tập hợp và sử dụng MetaData -- siêu dữ liệu, tóm tắt
          dữ liệu và tổng hợp để tạo kho thông tin và công cụ tìm
          kiếm]{.mark}

    b.  [Vai trò]{.mark}

        - [Giúp người dùng dễ dàng hiểu và sử dụng dữ liệu, từ đó giúp
          tiết kiệm thời gian]{.mark}

        - [Giúp AI và học máy, Data Catalog có thể tự động gắn thẻ và
          suy luận ngữ nghĩa]{.mark}

        - [Giúp doanh nghiệp kiểm soát quyền truy cập dữ liệu, bảo vệ
          quyền riêng tư]{.mark}
