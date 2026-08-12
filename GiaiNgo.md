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

**Q8: Sự khác biệt giữa Parameters (Tham số) và Hyperparameters (Siêu tham số) trong Machine Learning là gì?**
A: Parameters là các giá trị mà mô hình tự học được từ dữ liệu trong quá trình huấn luyện (ví dụ: các trọng số W và hệ số bias b trong phương trình Linear Regression). Ngược lại, Hyperparameters là các giá trị do người dùng thiết lập trước khi huấn luyện để điều khiển quá trình học (ví dụ: Learning Rate (tốc độ học) trong Gradient Descent, số lượng cây trong Random Forest, độ sâu tối đa của Decision Tree).

**Q9: Overfitting (Quá khớp) và Underfitting (Chưa khớp) là gì? Làm sao để nhận biết chúng?**
A: **Overfitting** là hiện tượng mô hình "học thuộc lòng" dữ liệu huấn luyện (Training set), bao gồm cả nhiễu, nhưng dự đoán rất kém trên dữ liệu mới (Test set). Nhận biết: Lỗi trên tập Train rất thấp, nhưng lỗi trên tập Test rất cao. **Underfitting** là khi mô hình quá đơn giản, không đủ khả năng học được quy luật của dữ liệu. Nhận biết: Lỗi cao trên cả tập Train và tập Test.

**Q10: Tại sao chúng ta cần chia dữ liệu thành tập Train (Huấn luyện) và tập Test (Kiểm tra)?**
A: Việc chia dữ liệu giúp đánh giá khách quan khả năng tổng quát hóa (generalization) của mô hình trên dữ liệu nó chưa từng thấy. Nếu dùng toàn bộ dữ liệu để huấn luyện và đánh giá trên chính dữ liệu đó, chúng ta sẽ không biết liệu mô hình thực sự đã "hiểu" quy luật hay chỉ đơn giản là "học thuộc lòng" (Overfitting).

**Q11: Các độ đo MSE, RMSE, MAE, và R-squared (R2) khác nhau như thế nào khi đánh giá mô hình Hồi quy?**
A: **MAE (Mean Absolute Error)** đo trung bình sai số tuyệt đối, dễ hiểu và ít bị ảnh hưởng bởi nhiễu (outliers). **MSE (Mean Squared Error)** bình phương sai số, "phạt" nặng các dự đoán có sai lệch lớn. **RMSE (Root Mean Squared Error)** là căn bậc hai của MSE, đưa sai số về cùng đơn vị đo với biến mục tiêu. **R2-Score** đo lường tỷ lệ phương sai của biến mục tiêu được giải thích bởi mô hình, có giá trị thường từ 0 đến 1, càng gần 1 mô hình càng tốt.

**Q12: Cây quyết định (Decision Tree) trong bài toán này có dễ bị Overfitting không? Làm sao để khắc phục?**
A: Có, Decision Tree rất dễ bị Overfitting vì thuật toán có xu hướng chia nhỏ dữ liệu cho đến khi mỗi lá (leaf) chứa rất ít điểm dữ liệu, nghĩa là nó cố gắng học thuộc lòng luôn cả nhiễu. Để khắc phục, chúng ta có thể áp dụng cắt tỉa (pruning) bằng cách giới hạn độ sâu tối đa của cây (`max_depth`), hoặc quy định số lượng mẫu tối thiểu để tiếp tục chia nhánh. Sử dụng Random Forest cũng là một cách giải quyết triệt để vấn đề này.

**Q13: Tại sao Gradient Boosting lại thường cho kết quả khác biệt so với Random Forest dù cả hai đều là phương pháp Ensemble (Kết hợp nhiều cây)?**
A: **Random Forest** xây dựng nhiều cây quyết định một cách độc lập và song song, sau đó lấy trung bình dự đoán (đối với hồi quy). Mục đích chính là giảm phương sai (variance) để chống Overfitting.
Ngược lại, **Gradient Boosting** xây dựng các cây một cách tuần tự (sequential). Cây sau sẽ tập trung vào việc sửa chữa những sai sót (residual errors) của cây trước đó. Do đó, Gradient Boosting thường đạt độ chính xác cao hơn nhưng cũng dễ bị Overfitting hơn và tốn nhiều thời gian huấn luyện hơn nếu không tinh chỉnh kỹ các hyperparameter.

**Q14: Làm thế nào để kết luận mô hình nào trong 4 mô hình (Linear, Tree, Forest, Boosting) là phù hợp nhất cho dự án dự báo doanh thu này?**
A: Quyết định dựa trên việc so sánh các độ đo đánh giá (RMSE, R2-Score) tính toán trên tập Test. Mô hình phù hợp nhất là mô hình có **R2-Score cao nhất** (giải thích được nhiều nhất sự biến thiên của doanh thu) và **RMSE thấp nhất** (sai số dự báo trung bình nhỏ nhất), ĐỒNG THỜI không có sự chênh lệch quá lớn về hiệu suất giữa tập Train và tập Test (để đảm bảo không bị Overfitting). Trong thực tế, các mô hình Ensemble (như Random Forest hay Gradient Boosting) thường cho kết quả tốt hơn mô hình tuyến tính đơn giản khi dữ liệu có nhiều mối quan hệ phi tuyến tính.

### CÁC CÂU HỎI THEO 3 TIÊU CHÍ ĐÁNH GIÁ LAB

**PHẦN 1: DEFINE PROBLEM (Xác định bài toán)**
**Q15: Bài toán này thuộc nhóm học máy nào (Supervised, Unsupervised, hay Reinforcement)? Tại sao?**
A: Đây là bài toán **Học có giám sát (Supervised Learning)**, cụ thể là bài toán **Hồi quy (Regression)**. Lý do là vì dữ liệu đầu vào đã có sẵn nhãn (label) hoặc giá trị mục tiêu (target) cần dự đoán, đó là Tổng doanh thu (`Total_Sales`), mang giá trị số thực liên tục.

**Q16: Đầu vào (Input - X) và Đầu ra (Output - y) của bài toán này là gì?**
A: 
- **Đầu vào (X):** Các đặc trưng được trích xuất từ thời gian (Năm, Tháng, Quý, Ngày trong tuần, Có phải cuối tuần không...).
- **Đầu ra (y):** Biến mục tiêu cần dự báo là Tổng doanh thu (`Total_Sales`) của ngày tương ứng.

**PHẦN 2: DATA UNDERSTANDING (Hiểu và Xử lý dữ liệu)**
**Q17: Tại bước EDA (Exploratory Data Analysis - Khám phá dữ liệu), bạn rút ra được insight quan trọng nào ảnh hưởng đến việc chọn đặc trưng?**
A: Thông qua quá trình trực quan hóa (EDA), chúng tôi nhận thấy `Total_Sales` có tính chu kỳ (seasonality) và xu hướng (trend) biến động rõ rệt theo thời gian (ví dụ: doanh thu tăng vọt vào cuối tuần). Insight này là lý do chính để chúng tôi thực hiện Feature Engineering, biến cột ngày tháng dạng chuỗi thành các cột đặc trưng số (`DayOfWeek`, `Month`, `IsWeekend`) để thuật toán có thể học được.

**Q18: Khái niệm Data Leakage đã được thể hiện và xử lý như thế nào trong bài toán này?**
A: Trong bộ dữ liệu gốc, tổng doanh thu của từng món (S-P1, S-P2,...) khi cộng lại sẽ đúng bằng `Total_Sales`. Nếu giữ các cột này làm đầu vào (Input), mô hình sẽ "học lỏm" (leakage) tương lai vì trong thực tế, bạn không thể biết doanh thu từng món của ngày mai trước khi biết tổng doanh thu ngày mai. Do đó, chúng tôi phải loại bỏ (drop) toàn bộ các cột S-P và Q-P, ép mô hình dự báo hoàn toàn dựa trên lịch thời gian.

**PHẦN 3: MODELING (Mô hình hóa)**
**Q19: Baseline model (mô hình cơ sở) của dự án này là gì và tại sao lại cần nó?**
A: Baseline model trong dự án này là **Linear Regression**. Việc sử dụng mô hình tuyến tính đơn giản làm mốc (baseline) giúp chúng ta có thước đo chuẩn. Khi huấn luyện các mô hình phức tạp hơn (như Random Forest, Gradient Boosting), nếu chúng không mang lại chỉ số RMSE hoặc R2 tốt hơn đáng kể so với Baseline, ta sẽ giữ lại Baseline theo nguyên tắc Occam's Razor (ưu tiên mô hình đơn giản, tính toán nhẹ và dễ giải thích).

**Q20: Quá trình chuẩn hóa dữ liệu (Data Scaling) có tác động giống nhau lên tất cả các mô hình trong lab này không?**
A: **Không.** Quá trình chuẩn hóa (dùng `StandardScaler`) cực kỳ quan trọng và bắt buộc đối với **Linear Regression** vì thuật toán này dùng phương trình đại số/gradient descent, sự chênh lệch thang đo (Năm 2024 vs Tháng 1-12) sẽ gây mất ổn định ma trận. Ngược lại, các thuật toán Tree-based như **Decision Tree, Random Forest, Gradient Boosting** chia cắt không gian dữ liệu bằng cách tìm các điểm ngưỡng (threshold splits), do đó chúng hoàn toàn không bị ảnh hưởng bởi thang đo dữ liệu, chuẩn hóa hay không kết quả vẫn không đổi.

**PHẦN 4: ĐÁNH GIÁ VÀ CẢI TIẾN (Evaluation & Improvement)**
**Q21: Tại sao chúng ta không dùng K-Fold Cross Validation ngẫu nhiên trong dự án này?**
A: Với dữ liệu mang tính chuỗi thời gian (Time Series) như dự báo doanh thu, thứ tự thời gian là cốt lõi (sự kiện hôm nay ảnh hưởng đến ngày mai). K-Fold Cross Validation thông thường sẽ xáo trộn (shuffle) dữ liệu một cách ngẫu nhiên. Điều này làm phá vỡ tính liên tục của thời gian, dẫn đến sai lầm cực kỳ nghiêm trọng là dùng dữ liệu tương lai để huấn luyện và dự đoán quá khứ (Look-ahead bias). Nếu muốn dùng Cross Validation, ta bắt buộc phải dùng kỹ thuật **Time Series Split** (cuộn tiến dần theo thời gian).

**Q22: Việc tạo thêm đặc trưng như `IsWeekend` có thực sự cần thiết khi mô hình Cây có thể tự học từ `DayOfWeek` không?**
A: Rất cần thiết. Dù lý thuyết là Decision Tree có thể tự tìm ra quy luật từ biến `DayOfWeek` (ví dụ, nó tự nhận ra nhánh > 4 là cuối tuần), việc "mớm" sẵn cho nó một biến nhị phân 0/1 (`IsWeekend`) giúp thuật toán cắt nhánh (split) nhanh và trực tiếp hơn rất nhiều. Điều này làm giảm số lượng câu hỏi mà cây phải hỏi, giúp cây nông hơn (giảm độ sâu), từ đó tăng tốc độ học và hạn chế Overfitting.

**Q23: Trong quá trình làm Lab, làm sao bạn phát hiện ra mô hình đang bị Underfitting?**
A: Mô hình bị **Underfitting (chưa khớp)** khi nó quá đơn giản và không nắm bắt được quy luật của dữ liệu. Chúng tôi nhận biết điều này nếu cả chỉ số lỗi trên tập Train (Train RMSE) và tập Test (Test RMSE) đều rất lớn, đồng thời R2-Score ở cả 2 tập đều thấp (thậm chí gần 0). Ví dụ, nếu chúng ta không làm Feature Engineering mà chỉ truyền mỗi biến `Year` vào mô hình Linear Regression, mô hình chắc chắn sẽ bị Underfitting vì dữ liệu quá nghèo nàn.

---
*Cẩm nang này là bí kíp độc quyền để bạn nắm trùm dự án. Chúc bạn thành công!*
