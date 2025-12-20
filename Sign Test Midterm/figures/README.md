# HƯỚNG DẪN TẠO HÌNH ẢNH CHO BÀI THUYẾT TRÌNH SIGN TEST

Tổng số ảnh cần tạo: **12 ảnh**

---

## 1. LỊCH SỬ & ĐỘNG LỰC (3 ảnh)

### arbuthnot_timeline.png
- **Loại:** Timeline infographic
- **Nội dung:**
  * Trục thời gian ngang 1629-1710 (82 năm)
  * Portrait nhỏ của John Arbuthnot ở góc trên bên trái
  * Line chart: Tỷ lệ Nam/Nữ qua các năm (luôn > 1.0)
  * Đường ngang đỏ ở y=1.0 (equal ratio)
  * Highlight: "82/82 năm Nam > Nữ"
  * Text: P = (1/2)^82 ≈ 10^-25
- **Công cụ:** Canva / PowerPoint / Python matplotlib
- **Kích thước:** 1200x800 px
- **Màu:** Xanh dương (nam), hồng (nữ), nền trắng, grid xám nhạt

**Code Python mẫu:**
```python
import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1629, 1711)
ratio = 1.02 + 0.05 * np.random.rand(len(years))  # All > 1

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(years, ratio, 'b-', linewidth=2, label='Male/Female ratio')
ax.axhline(1.0, color='red', linestyle='--', linewidth=2, label='Equal ratio')
ax.fill_between(years, 1.0, ratio, alpha=0.3, color='blue')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Male/Female Birth Ratio', fontsize=14)
ax.set_title("Arbuthnot's Study: 82 Years of Male > Female Births", fontsize=16, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('arbuthnot_timeline.png', dpi=300, bbox_inches='tight')
```

---

### historical_applications.png
- **Loại:** Infographic 3 cột
- **Nội dung:**
  * **Cột 1 (Y học):**
    - Icon: Ống nghiệm hoặc viên thuốc
    - Text: "James Lind (1747)"
    - Subtitle: "Scurvy Treatment"
    - Mini description: "12 sailors, 6 methods"
  * **Cột 2 (Tâm lý học):**
    - Icon: Bộ bài Zener cards
    - Text: "J.B. Rhine (1930s)"
    - Subtitle: "ESP Experiments"
    - Mini description: "Đoán bài đúng/sai"
  * **Cột 3 (Kinh tế):**
    - Icon: Biểu đồ chứng khoán
    - Text: "Stock Analysis (1960s)"
    - Subtitle: "Market Prediction"
    - Mini description: "Tăng/giảm so baseline"
- **Công cụ:** Canva (template "Timeline" hoặc "Infographic")
- **Kích thước:** 1400x600 px
- **Màu:** Mỗi cột một màu khác nhau (xanh lá, cam, xanh dương)

**Hướng dẫn Canva:**
1. Truy cập canva.com
2. Search "Infographic" hoặc "Timeline"
3. Chọn template 3 cột
4. Thay đổi text và icon theo mô tả
5. Download PNG (high quality)

---

### modern_applications.png
- **Loại:** 4 icons với labels ngang hàng
- **Nội dung:**
  * **Icon 1:** Hai màn hình (A/B) - "A/B Testing"
  * **Icon 2:** Ống nghiệm - "Clinical Trials"
  * **Icon 3:** Người dùng + sao rating - "User Studies"
  * **Icon 4:** Bánh răng + checkmark - "Quality Control"
- **Công cụ:** Flaticon.com + PowerPoint
- **Kích thước:** 1000x400 px
- **Layout:** 4 icons ngang hàng, mỗi icon 150x150px, label dưới

**Nguồn icons miễn phí:**
- flaticon.com
- icons8.com
- fontawesome.com

---

## 2. LÝ THUYẾT (3 ảnh)

### sign_test_types.png
- **Loại:** Diagram so sánh 2 loại
- **Nội dung:**
  * Chia đôi: Trái (One-sample), Phải (Paired)
  * **One-sample:**
    - Công thức: X_i - M_0
    - Ví dụ: "Median = 70?"
    - Icon: Một phân phối
  * **Paired:**
    - Công thức: X_i - Y_i
    - Ví dụ: "Trước - Sau"
    - Icon: Hai phân phối kết nối
- **Công cụ:** PowerPoint hoặc Draw.io
- **Kích thước:** 1000x600 px

---

### flowchart_4steps.png
- **Loại:** Flowchart dọc
- **Nội dung:**
  ```
  [Box 1: Tính hiệu số]
  d_i = X_i - Y_i
         ↓
  [Box 2: Xác định dấu]
  +, -, hoặc 0
         ↓
  [Box 3: Đếm S⁺]
  Số dấu dương
         ↓
  [Box 4: So sánh Binomial]
  S⁺ ~ Bin(n, 0.5)
  ```
- **Style:** 
  - Boxes màu xanh gradient
  - Mũi tên đậm màu đen
  - Font rõ ràng (Arial/Helvetica)
  - Số thứ tự (1,2,3,4) ở góc trên boxes
- **Công cụ:** Draw.io / Lucidchart / TikZ
- **Kích thước:** 800x1000 px

**Link Draw.io template:**
https://app.diagrams.net (chọn "Flowchart" template)

---

### formula_illustration.png
- **Loại:** Diagram công thức với ví dụ
- **Nội dung:**
  * **Trên:** 
    - H₀ và H₁ trong boxes
    - S⁺ ~ Binomial(n, 0.5)
  * **Giữa:**
    - Công thức p-value (two-tailed)
  * **Dưới:**
    - Ví dụ cụ thể: n=12, S⁺=9
    - Tính p-value = 0.0327
    - Kết luận: Bác bỏ H₀
- **Công cụ:** PowerPoint hoặc LaTeX (tikz)
- **Kích thước:** 1000x600 px

---

## 3. VÍ DỤ (2 ảnh)

### ab_testing_comparison.png
- **Loại:** Side-by-side comparison
- **Nội dung:**
  * **Bên trái:** Mock screenshot Interface A (simple)
  * **Bên phải:** Mock screenshot Interface B (better design)
  * **Giữa:** Mũi tên hoặc "VS"
  * **Dưới:** Bar chart
    - 11 thanh xanh (thích B)
    - 3 thanh đỏ (thích A)
    - Label: "11/15 prefer B"
- **Công cụ:** PowerPoint + mock screenshots từ Figma
- **Kích thước:** 1400x700 px

---

### color_preference.png
- **Loại:** Bar chart đơn giản
- **Nội dung:**
  * 2 bars:
    - Bar 1 (Xanh): Height = 14, label "Prefer Blue"
    - Bar 2 (Đỏ): Height = 6, label "Prefer Red"
  * Y-axis: "Number of People" (0-20)
  * Title: "Color Preference (n=20)"
- **Công cụ:** Excel hoặc Python matplotlib
- **Kích thước:** 1000x600 px

**Code Python:**
```python
import matplotlib.pyplot as plt

categories = ['Prefer Blue', 'Prefer Red']
values = [14, 6]
colors = ['blue', 'red']

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(categories, values, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
ax.set_ylabel('Number of People', fontsize=14)
ax.set_title('Color Preference Study (n=20)', fontsize=16, fontweight='bold')
ax.set_ylim(0, 20)
for i, v in enumerate(values):
    ax.text(i, v + 0.5, str(v), ha='center', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('color_preference.png', dpi=300, bbox_inches='tight')
```

---

## 4. DEMO JUPYTER (4 ảnh - CHỤP TỪ NOTEBOOK THẬT)

### jupyter_cell1_output.png
- **Cách tạo:**
  1. Chạy notebook thật (sign_test_demo.ipynb)
  2. Chụp màn hình Cell 1 output (DataFrame head)
  3. Crop gọn gàng, chỉ giữ output table
- **Kích thước:** 1200x600 px
- **Note:** PHẢI có syntax highlighting

---

### jupyter_output_table.png
- **Cách tạo:**
  1. Chạy Cell 2 (bảng với cột Dấu)
  2. Chụp output table
  3. Nếu có thể, dùng `df.style` để highlight:
     - Dấu + màu xanh
     - Dấu - màu đỏ
- **Kích thước:** 1200x500 px

**Code styling (optional):**
```python
styled_df = df_filtered.style.applymap(
    lambda x: 'color: green' if x == '+' else 'color: red', 
    subset=['Dau']
)
styled_df
```

---

### jupyter_output_stats.png
- **Cách tạo:**
  1. Chạy Cell 3 (print statistics)
  2. Chụp text output
  3. Crop sao cho rõ ràng
- **Kích thước:** 800x300 px
- **Nội dung mẫu:**
  ```
  Số dấu +: 9/11
  P-value: 0.0327
  BÁC BỎ H0 (p=0.0327 < 0.05)
  => CÓ BẰNG CHỨNG: Thuốc có hiệu quả!
  ```

---

### jupyter_plots.png
- **Cách tạo:**
  1. Chạy Cell 4 (matplotlib plots)
  2. Chụp figure với 2 subplots
  3. Đảm bảo rõ nét, màu sắc đẹp
- **Kích thước:** 1400x700 px
- **Note:** 2 plots phải nằm ngang (1 row, 2 cols)

---

## 5. KẾT LUẬN (1 ảnh)

### qr_code_github.png
- **Cách tạo:**
  1. Truy cập https://www.qr-code-generator.com
  2. Nhập link GitHub repo
  3. Download PNG
- **Kích thước:** 500x500 px
- **Màu:** Đen trắng (standard)

**Link mẫu:** https://github.com/yourusername/sign-test-demo

---

## CÔNG CỤ KHUYẾN NGHỊ

### Online (Miễn phí, Dễ dùng)
1. **Canva.com** - Infographics, timelines
2. **Draw.io** - Flowcharts, diagrams
3. **Flaticon.com** - Icons miễn phí
4. **QR Code Generator** - QR codes

### Desktop (Nhanh)
1. **PowerPoint/Keynote** - Slides, diagrams
2. **Excel** - Charts, tables
3. **Screenshot tools** - Chụp màn hình

### Python (Professional, Reproducible)
1. **matplotlib** - Charts, plots
2. **seaborn** - Statistical visualizations
3. **PIL/Pillow** - Image processing

---

## CHECKLIST HOÀN THÀNH

- [ ] arbuthnot_timeline.png
- [ ] historical_applications.png
- [ ] modern_applications.png
- [ ] sign_test_types.png
- [ ] flowchart_4steps.png
- [ ] formula_illustration.png
- [ ] ab_testing_comparison.png
- [ ] color_preference.png
- [ ] jupyter_cell1_output.png
- [ ] jupyter_output_table.png
- [ ] jupyter_output_stats.png
- [ ] jupyter_plots.png
- [ ] qr_code_github.png

**Tổng: 13 ảnh**

---

## LƯU Ý QUAN TRỌNG

1. **Độ phân giải:** Tất cả ảnh nên ≥300 DPI để trình chiếu rõ nét
2. **Format:** PNG (không nên dùng JPG cho diagrams/text)
3. **Màu sắc:** Nhất quán với theme HUST (đỏ, xanh dương, xanh lá)
4. **Font:** Rõ ràng, dễ đọc (Arial, Helvetica, hoặc Roboto)
5. **Backup:** Lưu file nguồn (.pptx, .ai, .py) để edit sau

---

## TIMELINE ƯỚC TÍNH

- **Lịch sử & Động lực:** 1-2 giờ (3 ảnh)
- **Lý thuyết:** 1-2 giờ (3 ảnh)
- **Ví dụ:** 30 phút - 1 giờ (2 ảnh)
- **Demo Jupyter:** 1 giờ (chạy notebook + chụp 4 ảnh)
- **QR code:** 5 phút

**Tổng:** 4-6 giờ (nếu làm từ đầu)

---

**Good luck! 🎨📊**
