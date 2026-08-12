# CẨM NANG GIẢI NGỐ DỰ ÁN (THE ULTIMATE GUIDE)

---

## 1. Mục tiêu của dự án là gì?
Chúng ta có dữ liệu bán hàng lịch sử của một công ty thương mại điện tử (bán 4 sản phẩm chính: P1, P2, P3, P4).
**Nhiệm vụ:** Xây dựng một cỗ máy (Mô hình AI) để khi đưa vào một "Ngày trong tương lai" (ví dụ: Tết Dương lịch năm sau), máy sẽ tự động tính toán xem ngày hôm đó công ty sẽ thu về tổng cộng **bao nhiêu tiền (Total Sales)**. 

Bài toán này trong ngành gọi là **Time-Series Forecasting (Dự báo chuỗi thời gian)**.

---

## 2. Dữ liệu (Dataset) có gì?
File `statsfinal.csv` ban đầu có các thông tin cơ bản sau của 4600 ngày:
- **Date**: Ngày tháng.
- **Q-P1 đến Q-P4**: Số lượng bán ra của 4 sản phẩm.
- **S-P1 đến S-P4**: Số tiền thu về của 4 sản phẩm.

---

## 3. Điểm "Ăn Tiền" thứ 1: Tự code thuật toán (From Scratch)
Hầu hết sinh viên làm Machine Learning đều dùng câu lệnh `from sklearn.linear_model import LinearRegression`. 
Nhưng ở dự án này, chúng ta **CẤM** sử dụng `scikit-learn`.
Thay vào đó, tất cả các thuật toán AI đều được **tự lập trình bằng tay** dựa trên toán học ma trận của thư viện `numpy`. 
- **Linear Regression**: Dùng phương trình chuẩn (Normal Equation - Đạo hàm ma trận) để tìm ra công thức y = ax + b.
- **Decision Tree / Random Forest / Gradient Boosting**: Tự viết các hàm chia cắt dữ liệu (split), tính phương sai (variance) để tạo ra các nhánh cây quyết định.
> **Ý nghĩa:** Điều này chứng minh bạn hiểu cốt lõi toán học của AI, chứ không phải một "thợ gõ code" chỉ biết gọi hàm có sẵn.

---

## 4. Điểm "Ăn Tiền" thứ 2: Phát hiện và xử lý Data Leakage (Rò rỉ dữ liệu)
Đây là câu chuyện kịch tính nhất của dự án. 

**Vấn đề xảy ra:** Lúc đầu, khi đưa tất cả các cột dữ liệu vào mô hình, AI chạy ra kết quả đúng 100% (Sai số RMSE = 0.00). Sinh viên bình thường sẽ ăn mừng và đem nộp bài.

**Sự thật cay đắng:** Bị rò rỉ dữ liệu (Data Leakage). 
- Đề bài bắt dự báo Tổng doanh thu (`Total_Sales`).
- Dữ liệu lại chứa sẵn cột Doanh thu từng món (`S-P1`, `S-P2`...). Mô hình AI rất thông minh, nó tự phát hiện ra trò lừa: `Total_Sales = S-P1 + S-P2 + S-P3 + S-P4`. Nó chỉ làm phép toán cộng thay vì "Dự báo"!
- Hơn nữa, vì giá bán (Price) cố định, nên nếu để cột số lượng (`Q-P1`), mô hình lấy Số lượng x Giá = Doanh thu. Đều là ăn gian. Nếu muốn dùng được mô hình trong tương lai, chúng ta không thể "biết trước" tương lai bán được bao nhiêu cái rồi mới đi tính tiền được.

**Cách giải quyết của chúng ta:**
Mạnh tay **XÓA BỎ BẢN TÀNG** (Drop) tất cả các cột liên quan đến số lượng và tiền (Q và S). Chúng ta ép AI phải học bằng con đường chân chính: Chỉ dự báo dựa trên **THỜI GIAN** (Năm, Tháng, Ngày trong tuần, Quý, Có phải cuối tuần không).
> **Ý nghĩa:** Chỉ số RMSE (Sai số) tăng lên ~13,780. Nhưng đây là một mô hình THẬT, có thể triển khai vào kinh doanh để dự báo Tương Lai. Giảng viên chấm thi sẽ cho điểm tuyệt đối phần tư duy này.

---

## 5. Cuộc chiến giữa các mô hình (Model Selection)
Chúng ta đã cho 4 con AI lên võ đài chiến đấu (dự đoán thử trên 20% dữ liệu giấu kín):
1. **Linear Regression** (Hồi quy tuyến tính)
2. **Decision Tree** (Cây quyết định)
3. **Random Forest** (Rừng ngẫu nhiên)
4. **Gradient Boosting** (Tăng cường độ dốc)

**Kết quả:** 
Trong khi các mô hình Cây (Tree-based) rất mạnh ở dữ liệu dạng bảng phức tạp, nhưng đối với dữ liệu thuần **Thời Gian** (Tháng, Quý, Ngày), cây quyết định rất dễ học thuộc lòng (Overfitting) lịch của năm cũ và dự báo sai bét ở năm mới.
Do đó, **Linear Regression** đã giành chiến thắng (RMSE thấp nhất). Nó nắm bắt được chu kỳ (Trend) tuyến tính vô cùng tốt. Đơn giản mà hiệu quả (Ockham's Razor).

---

## 6. Đóng gói sản phẩm (Deployment)
Thay vì để code chạy lộn xộn trong file huấn luyện, chúng ta đã tách hẳn ra 1 file `src/predict.py`.
Chỉ cần bạn chạy file này, ném cho nó 1 ngày (VD: `"2024-12-25"`), nó sẽ:
1. Bóc tách ra ngày đó thuộc Tháng mấy, Thứ mấy, Quý mấy.
2. Chuẩn hóa các số liệu đó.
3. Đưa vào phương trình Linear Regression đã học xong.
4. Trả về kết quả: Giáng sinh năm 2024 công ty sẽ thu được ~50,768 USD.

---

## 7. Các Câu Hỏi Bảo Vệ Đồ Án Thường Gặp (Q&A)

**Q1: Tại sao lại chọn mô hình Hồi quy tuyến tính (Linear Regression) cho bài toán này thay vì các mô hình phức tạp hơn (như Deep Learning)?**
A: Trong bài toán này, các đặc trưng (features) chủ yếu là dữ liệu thời gian (Năm, Tháng, Ngày). Mô hình Linear Regression với tính chất đơn giản đã nắm bắt rất tốt xu hướng (trend) của thời gian mà không bị Overfitting (học thuộc lòng dữ liệu cũ) như các mô hình Cây quyết định sâu. Tiêu chí của chúng ta là "Occam's Razor" - mô hình đơn giản nhất mà hiệu quả nhất sẽ được ưu tiên. Thêm vào đó, việc tính toán ma trận trực tiếp rất nhanh và nhẹ.

**Q2: Hiện tượng Data Leakage (Rò rỉ dữ liệu) trong bài toán này cụ thể là gì và tại sao bạn phải loại bỏ các cột số lượng (Q-P) và doanh thu từng món (S-P)?**
A: Data Leakage xảy ra khi mô hình được học những thông tin mà thực tế ở tương lai nó không thể biết trước. Biến mục tiêu là Tổng doanh thu (`Total_Sales`), nếu chúng ta giữ lại các cột doanh thu từng món, mô hình chỉ đơn giản làm phép cộng (S-P1 + S-P2 + S-P3 + S-P4) và đạt sai số bằng 0. Nếu giữ lại cột số lượng (Q-P), mô hình sẽ lấy Số lượng x Giá để ra Doanh thu. Thực tế, khi dự báo cho tương lai (ví dụ ngày mai), chúng ta chưa thể biết ngày mai bán được bao nhiêu món. Do đó, phải loại bỏ hết để ép mô hình dự báo dựa trên chu kỳ thời gian.

**Q3: Tại sao lại phải chuẩn hóa dữ liệu (Standardization/Z-score) trước khi đưa vào mô hình Linear Regression?**
A: Trong phương trình chuẩn (Normal Equation) của Linear Regression, nếu các thang đo của các biến khác biệt quá lớn (ví dụ cột Năm là 2024, cột Tháng là 1-12, cột DayOfWeek là 0-6), ma trận có thể bị bất ổn định về mặt số học. Việc chuẩn hóa giúp các biến số được đưa về cùng một tỷ lệ, giúp thuật toán hội tụ chính xác hơn và đánh giá được đúng mức độ quan trọng (trọng số) của từng biến.

**Q4: Yếu tố mùa vụ (Seasonality) được mô hình xử lý như thế nào?**
A: Thay vì giữ nguyên cột Ngày (Date) dạng chuỗi (không thể tính toán), chúng tôi đã trích xuất (Feature Engineering) ra các biến số như: Tháng (Month), Quý (Quarter), Tuần trong năm (WeekOfYear), và Có phải cuối tuần không (IsWeekend). Những biến này trực tiếp cung cấp cho mô hình Linear Regression khả năng nhận diện chu kỳ mua sắm lặp lại theo lịch (ví dụ: mua sắm tăng cao vào cuối tuần hoặc cuối năm).

**Q5: Hạn chế của dự án này là gì và hướng phát triển tiếp theo?**
A: Hạn chế lớn nhất là mô hình Linear Regression hiện tại chỉ nắm bắt được xu hướng tuyến tính cơ bản, chưa giải quyết triệt để các tương tác phi tuyến tính phức tạp (ví dụ: ảnh hưởng chéo giữa các sự kiện lễ hội đặc biệt). Hướng phát triển là có thể thử nghiệm nghiệm các mô hình chuyên dụng cho chuỗi thời gian như ARIMA, Prophet, hoặc mạng LSTM (nếu lượng dữ liệu đủ lớn), cũng như bổ sung thêm dữ liệu ngoại cảnh (thời tiết, chiến dịch marketing) để tăng độ chính xác.

**Q6: So với yêu cầu gốc của đề bài (có nhắc đến Customer demographics, Marketing campaign, Reviews), tại sao mô hình này lại không có những biến đó?**
A: Đề bài yêu cầu lý tưởng nhất là có các dữ liệu về khách hàng (tuổi, giới tính) và marketing. Tuy nhiên, bộ dữ liệu `statsfinal.csv` mà chúng ta sử dụng là dạng **dữ liệu đã được tổng hợp theo ngày (Daily Aggregated Data)** chứ không phải dữ liệu giao dịch chi tiết (Transactional Data). Vì vậy, chúng ta không có thông tin khách hàng hay lượt đánh giá (reviews). Bù lại, chúng ta đã tận dụng triệt để các **đặc trưng thời gian (Seasonal trends)** để bù đắp sự thiếu hụt này và dự báo dựa trên chu kỳ ngày/tháng/năm, hoàn toàn đáp ứng được mục tiêu cốt lõi của bài toán là "Dự báo doanh thu" (Predicting Product Sales).

**Q7: Đề bài có gợi ý dùng ARIMA hoặc Prophet cho Time-Series, tại sao lại dùng Linear Regression, Decision Tree, Random Forest?**
A: Đề bài yêu cầu rõ ở Bước 3 (Model Selection) là: "Consider regression algorithms like linear regression, decision trees, random forests, or gradient boosting". Chúng ta đã bám sát và cài đặt thành công 100% CẢ 4 thuật toán này từ con số 0 (không dùng thư viện có sẵn). Việc dùng ARIMA hay Prophet chỉ nằm ở phần "Additional Considerations" (Cân nhắc thêm). Việc dùng Linear Regression trích xuất đặc trưng thời gian thực chất hoạt động rất hiệu quả và đáp ứng đúng, đủ trọng tâm Bước 3 của đề.

---
*Cẩm nang này là bí kíp độc quyền để bạn nắm trùm dự án. Chúc bạn thành công!*
