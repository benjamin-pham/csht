## **Dịch vụ số & Chuyển đổi (Digital Product & Delivery Agility)**

1.  **Khái niệm:** Tập hợp các chỉ số đánh giá tốc độ, hiệu năng và chất
    lượng của quy trình phát triển/bàn giao sản phẩm phần mềm (thường
    dựa trên tiêu chuẩn DORA).

2.  **Vai trò:** Giúp đội ngũ kỹ thuật đưa tính năng mới ra thị trường
    nhanh nhất (Time-to-market) nhưng vẫn đảm bảo độ tin cậy, ít lỗi.

3.  **Cách thức đo lường:**

### **3.1. Deployment Frequency (Tần suất triển khai)**

**Mục đích:\
Đánh giá mức độ thường xuyên doanh nghiệp triển khai thành công phiên
bản mới lên môi trường Production.**

**Cách tính:\
Tổng số lần triển khai (Deployment) thành công lên môi trường Production
trong kỳ báo cáo.**

**Đơn vị tính:\
Lần/tuần hoặc lần/tháng.**

**Nguồn dữ liệu:**

- **Jenkins**

- **GitLab CI/CD**

- **Azure DevOps**

- **GitHub Actions**

- **ArgoCD, Spinnaker (nếu có)**

**Tần suất đo:**

- **Hàng tuần**

- **Hàng tháng**

### **3.2. Lead Time for Changes (Thời gian triển khai thay đổi)**

**Mục đích:\
Đo lường thời gian cần thiết để một thay đổi trong mã nguồn được đưa vào
vận hành ổn định trên môi trường Production.**

**Cách tính:**

> **Lead Time = Thời điểm Production ổn định − Thời điểm Commit/Merge
> Code**

**Đơn vị tính:\
Giờ hoặc ngày.**

**Nguồn dữ liệu:**

- **Git**

- **GitLab**

- **GitHub**

- **Azure DevOps**

- **Jira**

**Tần suất đo:**

- **Hàng tháng**

### **3.3. Change Failure Rate (Tỷ lệ lỗi do thay đổi)**

**Mục đích:\
Đánh giá tỷ lệ các lần triển khai gây ra lỗi hoặc sự cố trên môi trường
Production.**

**Cách tính:**

> **Change Failure Rate (%) = (Số lần triển khai gây lỗi / Tổng số lần
> triển khai) × 100%**

**Trong đó, triển khai gây lỗi bao gồm:**

- **Rollback phiên bản.**

- **Phát sinh Incident sau triển khai.**

- **Phải triển khai Hotfix.**

- **Gây gián đoạn hoặc suy giảm chất lượng dịch vụ.**

**Đơn vị tính:\
Phần trăm (%).**

**Nguồn dữ liệu:**

- **Jira Service Management**

- **ServiceNow**

- **Grafana**

- **Prometheus**

- **Azure Monitor**

- **Nhật ký vận hành (Operation Log)**

**Tần suất đo:**

- **Hàng tháng**

### **3.4. Mean Time to Recovery (MTTR)**

**Mục đích:\
Đánh giá khả năng khôi phục dịch vụ sau khi xảy ra sự cố.**

**Cách tính:**

> **MTTR = Tổng thời gian khắc phục các sự cố / Tổng số sự cố**

**Đơn vị tính:\
Phút hoặc giờ.**

**Nguồn dữ liệu:**

- **ServiceNow**

- **Jira Service Management**

- **Prometheus**

- **Grafana**

- **Zabbix**

- **Hệ thống giám sát vận hành**

**Tần suất đo:**

- **Hàng tháng**

**https://docs.gitlab.com/user/analytics/dora_metrics**

[[KPI & Strategy Software for Smarter Performance \|
Intrafocus]{.underline}](https://www.intrafocus.com/)

[[The KPI dashboard - Seeing the big picture \|
Intrafocus]{.underline}](https://www.intrafocus.com/blog/kpi-dashboard-seeing-the-big-picture/)
