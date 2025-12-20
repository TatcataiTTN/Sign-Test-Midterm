# HƯỚNG DẪN SETUP THEME HUST

## 📋 CÁC FILE THEME CẦN THIẾT

Để slides hoạt động đúng với theme HUST, bạn cần **copy 5 files theme** từ folder bài cũ (AMR seminar) sang folder này:

### Danh sách 5 files:

1. `beamerthemehust.sty` (11 KB) - Theme chính
2. `beamercolorthemehust.sty` (3 KB) - Màu sắc
3. `beamerfontthemehust.sty` (320 bytes) - Font chữ
4. `beamerinnerthemehust.sty` (6 KB) - Inner theme
5. `beamerouterthemehust.sty` (4 KB) - Outer theme

### Folder res/ (background images):

Bạn cũng cần copy cả folder `res/` với các file background:
- bg-43-1.png, bg-43-2.png, ..., bg-43-5.png (aspect ratio 4:3)
- bg-169-1.png, bg-169-2.png, bg-169-3.png (aspect ratio 16:9)
- Cả .svg và .png versions

---

## 🚀 CÁCH SETUP NHANH

### Option 1: Copy thủ công (KHUYẾN NGHỊ)

```bash
# Bước 1: Di chuyển đến folder bài cũ (AMR seminar)
cd /path/to/your/kpneumoniae_amr_seminar/

# Bước 2: Copy 5 files theme sang folder Sign Test
cp beamer*.sty /path/to/sign_test_midterm/

# Bước 3: Copy folder res/
cp -r res/ /path/to/sign_test_midterm/

# Bước 4: Verify
cd /path/to/sign_test_midterm/
ls -la beamer*.sty
ls -la res/
```

### Option 2: Copy trong Finder (macOS)

1. Mở 2 cửa sổ Finder:
   - Cửa sổ 1: Folder bài cũ (AMR seminar)
   - Cửa sổ 2: Folder `sign_test_midterm/`

2. Copy 5 files `.sty`:
   - Chọn tất cả files `beamer*.sty`
   - Drag & drop vào folder `sign_test_midterm/`

3. Copy folder `res/`:
   - Drag & drop folder `res/` vào `sign_test_midterm/`

---

## ✅ KIỂM TRA SAU KHI COPY

Cấu trúc folder `sign_test_midterm/` phải như sau:

```
sign_test_midterm/
│
├── beamerthemehust.sty              ← Theme chính
├── beamercolorthemehust.sty         ← Màu sắc
├── beamerfontthemehust.sty          ← Font
├── beamerinnerthemehust.sty         ← Inner theme
├── beamerouterthemehust.sty         ← Outer theme
│
├── res/                             ← Background images
│   ├── bg-169-1.png
│   ├── bg-169-1.svg
│   ├── bg-169-2.png
│   ├── bg-169-2.svg
│   ├── bg-169-3.png
│   ├── bg-169-3.svg
│   ├── bg-43-1.png
│   ├── bg-43-1.svg
│   └── ... (các files bg khác)
│
├── main_NO_IMAGES.tex               ← File chính (đã update dùng theme HUST)
├── sections/
├── figures/
├── notebooks/
└── ...
```

---

## 🔧 COMPILE VỚI THEME HUST

Sau khi copy xong, compile như bình thường:

```bash
cd sign_test_midterm/

# Compile với XeLaTeX (QUAN TRỌNG!)
xelatex main_NO_IMAGES.tex
xelatex main_NO_IMAGES.tex  # Chạy 2 lần

# Xem kết quả
open main_NO_IMAGES.pdf
```

**LƯU Ý:** 
- PHẢI dùng **XeLaTeX** (không phải pdfLaTeX)
- Nếu gặp lỗi, check xem đã copy đủ 5 files `.sty` chưa

---

## 🎨 THEME HUST ĐÃ ĐƯỢC APPLY

File `main_NO_IMAGES.tex` đã được cập nhật với:

```latex
% Load HUST theme
\usetheme{hust}
\definecolor{hustgreen}{RGB}{34,139,34}
```

Và title frame:
```latex
\begin{frame}[noframenumbering,Title]
    \maketitle
\end{frame}
```

---

## 🆘 XỬ LÝ LỖI

### Lỗi: "File `beamerthemehust.sty' not found"

**Nguyên nhân:** Chưa copy files theme vào folder

**Giải pháp:**
1. Check lại đã copy đủ 5 files `.sty` chưa
2. Đảm bảo files ở cùng folder với `main_NO_IMAGES.tex`

### Lỗi: "File `res/bg-169-1.png' not found"

**Nguyên nhân:** Chưa copy folder `res/`

**Giải pháp:**
1. Copy cả folder `res/` từ bài cũ
2. Đảm bảo folder `res/` ở cùng level với `main_NO_IMAGES.tex`

### Lỗi: Font chữ không đẹp

**Nguyên nhân:** Dùng pdfLaTeX thay vì XeLaTeX

**Giải pháp:**
1. PHẢI compile với **XeLaTeX**
2. Nếu dùng Overleaf: Menu → Settings → Compiler: XeLaTeX

---

## 📞 HỖ TRỢ

Nếu gặp vấn đề khi setup theme:

1. Check lại đã copy đủ 5 files `.sty` + folder `res/` chưa
2. Verify cấu trúc folder đúng như trên
3. Compile với XeLaTeX (KHÔNG phải pdfLaTeX)
4. Liên hệ: nghia.tt251196m@sis.hust.edu.vn

---

**CHECKLIST:**
- [ ] Copy 5 files `beamer*.sty`
- [ ] Copy folder `res/`
- [ ] Verify cấu trúc folder
- [ ] Compile với XeLaTeX
- [ ] Xem PDF - theme HUST đã xuất hiện!

---

**Chúc bạn thành công! 🎨**
