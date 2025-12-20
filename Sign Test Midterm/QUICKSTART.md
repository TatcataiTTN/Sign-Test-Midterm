# HƯỚNG DẪN NHANH - BẮT ĐẦU NGAY!

## 🚀 3 BƯỚC ĐỂ BẮT ĐẦU

### BƯỚC 1: KIỂM TRA FILE (2 phút)

```bash
cd sign_test_midterm/

# Xem cấu trúc
ls -la

# Bạn sẽ thấy:
# - main_NO_IMAGES.tex       (file chính - version KHÔNG ẢNH)
# - sections/                (6 file section)
# - figures/                 (thư mục cho ảnh + README hướng dẫn)
# - notebooks/               (Jupyter notebook + data)
# - README.md                (hướng dẫn đầy đủ)
```

---

### BƯỚC 2: COMPILE SLIDES NGAY (5 phút)

#### Trên macOS:

```bash
# Cài XeLaTeX nếu chưa có (chỉ lần đầu)
brew install --cask mactex

# Compile slides (chạy 2 lần)
xelatex main_NO_IMAGES.tex
xelatex main_NO_IMAGES.tex

# Mở PDF
open main_NO_IMAGES.pdf
```

#### Trên Windows:
1. Tải MiKTeX: https://miktex.org/download
2. Cài đặt
3. Mở Command Prompt:
   ```cmd
   xelatex main_NO_IMAGES.tex
   xelatex main_NO_IMAGES.tex
   ```

#### Hoặc dùng Overleaf (KHUYẾN NGHỊ cho người mới):
1. Tải toàn bộ folder lên Overleaf.com
2. Menu → Settings → Compiler: chọn **XeLaTeX**
3. Nhấn **Recompile**
4. Tải PDF về

**LƯU Ý:** PHẢI dùng XeLaTeX (KHÔNG phải pdfLaTeX) vì có tiếng Việt!

---

### BƯỚC 3: CHẠY JUPYTER NOTEBOOK (10 phút)

```bash
cd notebooks/

# Cài đặt packages nếu chưa có
pip install jupyter numpy pandas scipy matplotlib seaborn

# Khởi động Jupyter
jupyter notebook

# Browser sẽ mở tự động
# → Chọn: sign_test_demo.ipynb
# → Nhấn "Run All" hoặc Shift+Enter từng cell
```

**Kết quả:** Bạn sẽ thấy:
- Bảng dữ liệu
- Kết quả kiểm định (p-value = 0.0327)
- 2 plots đẹp
- So sánh với t-test

**QUAN TRỌNG:** Chụp screenshots từ notebook để làm ảnh cho slides!

---

## 📝 CHECKLIST LÀM VIỆC THEO THỨ TỰ

### NGÀY 1-2: Làm quen (2-3 giờ)
- [ ] Đọc README.md đầy đủ
- [ ] Compile main_NO_IMAGES.pdf
- [ ] Chạy notebook, hiểu từng bước
- [ ] Đọc qua 6 file section

### NGÀY 3-5: Tạo ảnh (4-6 giờ)
- [ ] Đọc figures/README.md
- [ ] Tạo 9 ảnh đầu tiên (lịch sử, lý thuyết, ví dụ)
- [ ] Chụp 4 ảnh từ notebook
- [ ] Tạo QR code GitHub

**Tools:**
- Canva.com (infographics)
- Draw.io (flowcharts)
- Python matplotlib (charts)

### NGÀY 6: Hoàn thiện slides (2 giờ)
- [ ] Copy main_NO_IMAGES.tex → main.tex
- [ ] Thay placeholders bằng `\includegraphics`
- [ ] Compile main.pdf (version có ảnh)
- [ ] Kiểm tra tất cả ảnh hiển thị OK

### NGÀY 7-8: Luyện tập (4 giờ)
- [ ] Đọc qua slides 3 lần
- [ ] Luyện demo notebook
- [ ] Đo thời gian (17±2 phút)
- [ ] Chia phần trình bày cho nhóm
- [ ] Test máy chiếu

---

## 🆘 XỬ LÝ SỰ CỐ NHANH

### LaTeX không compile?
```bash
# Kiểm tra compiler
xelatex --version

# Nếu lỗi, dùng Overleaf (100% work)
```

### Jupyter không chạy?
```bash
# Kiểm tra packages
pip list | grep -E 'numpy|pandas|scipy'

# Cài lại
pip install --upgrade numpy pandas scipy matplotlib
```

### Không biết tạo ảnh?
1. **Plan A:** Dùng Canva (dễ nhất)
2. **Plan B:** Dùng PowerPoint
3. **Plan C:** Nhờ bạn giỏi design

---

## 📞 LIÊN HỆ HỖ TRỢ

**Trương Tuấn Nghĩa:** nghia.tt251196m@sis.hust.edu.vn

---

## 🎯 MỤC TIÊU CUỐI CÙNG

1. **File PDF slides** (main.pdf) với đầy đủ ảnh
2. **Jupyter notebook** chạy được, có screenshots
3. **Luyện tập** đủ 3 lần, thời gian 17±2 phút
4. **Tự tin** trình bày và trả lời Q&A

---

**BẮT ĐẦU NGAY! CHÚC BẠN THÀNH CÔNG! 🚀**
