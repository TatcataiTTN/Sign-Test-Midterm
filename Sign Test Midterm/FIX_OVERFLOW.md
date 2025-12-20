# FIX SLIDES BỊ TRÀN - HƯỚNG DẪN TOÀN DIỆN

## ✅ ĐÃ FIX XONG

### Section 01: History (3 slides) ✓
- Slide 1: Arbuthnot → `\footnotesize`, `\itemsep0pt`, giảm `\vspace`
- Slide 2: Historical apps → `\scriptsize` blocks, compact lists
- Slide 3: Modern apps → `\footnotesize`, compact enum

### Section 02: Theory (3 slides) ✓  
- Slide 1: Definition → `\footnotesize`, shorter definition
- Slide 2: 4 steps → `\footnotesize`, `\itemsep0pt`
- Slide 3: Formulas → `[shrink=5]`, `\scriptsize` blocks

---

## 🔧 CÁCH FIX (ÁP DỤNG CHO TẤT CẢ SLIDES)

### 1. Thêm `[allowframebreaks,shrink=X]`

```latex
% TRƯỚC:
\begin{frame}{Title}

% SAU:
\begin{frame}[allowframebreaks,shrink=5]{Title}
```

- `allowframebreaks`: Tự động chia slide nếu quá dài
- `shrink=5`: Thu nhỏ nội dung 5% (có thể 5-15)

---

### 2. Giảm Font Size

```latex
\small       → \footnotesize     (nhỏ hơn)
\footnotesize → \scriptsize      (nhỏ nhất có thể đọc)
```

**Áp dụng:**
```latex
\begin{frame}{...}
    \footnotesize   % ← Thêm dòng này ngay sau {
    
    Nội dung...
\end{frame}
```

---

### 3. Loại bỏ Spacing Thừa

```latex
% TRƯỚC:
\vspace{0.3cm}

% SAU:
\vspace{0.15cm}   % Hoặc bỏ hẳn
```

**Và:**
```latex
% TRƯỚC:
\begin{itemize}

% SAU:
\begin{itemize}\itemsep0pt    % ← Thêm \itemsep0pt
```

---

### 4. Thu gọn Blocks

```latex
% TRƯỚC:
\begin{block}{Title}
    Content with normal font
\end{block}

% SAU:
\begin{block}{Title}
    \scriptsize    % ← Thêm dòng này
    Content
\end{block}
```

---

### 5. Cắt Text Dài

```latex
% TRƯỚC:
"Kiểm định phi tham số sử dụng dấu (+/-) của hiệu số để..."

% SAU:
"Kiểm định phi tham số dùng dấu (+/-) để..."
```

---

## 📋 CHECKLIST FIX TỪNG SLIDE

### Khi một slide bị tràn:

- [ ] Thêm `[allowframebreaks,shrink=5]`
- [ ] Thêm `\footnotesize` sau `\begin{frame}`
- [ ] Thêm `\itemsep0pt` vào tất cả `\begin{itemize}` và `\begin{enumerate}`
- [ ] Giảm tất cả `\vspace{0.3cm}` → `\vspace{0.15cm}`
- [ ] Blocks dùng `\scriptsize`
- [ ] Cắt text dài → ngắn gọn
- [ ] Test compile → Nếu vẫn tràn: tăng `shrink=10`

---

## 🚀 SCRIPT COMPILE NHANH

### Cách 1: Bash script (1 dòng)

```bash
cd sign_test_midterm/
./compile_quick.sh
```

### Cách 2: Makefile

```bash
make
```

### Cách 3: Trực tiếp

```bash
xelatex -interaction=nonstopmode main_NO_IMAGES && xelatex -interaction=nonstopmode main_NO_IMAGES
```

**Lưu ý:** `nonstopmode` = không dừng khi gặp lỗi, cứ chạy tiếp!

---

## 📊 SECTIONS CẦN FIX TIẾP

### Section 03: Examples (3 slides)
- Pain medication example
- A/B testing example  
- Color preference example

### Section 04: Demo Jupyter (4 slides)
- Setup slide
- Data loading
- Sign Test execution
- Visualization

### Section 05: FAQs (2 slides)
- When to use
- Common questions

### Section 06: Conclusion (2 slides)
- Summary
- References

---

## 🔥 FIX NHANH TẤT CẢ (TEMPLATE)

Thêm vào **ĐẦU MỖI SECTION FILE**:

```latex
% Global font size for this section
\footnotesize
```

Hoặc thêm vào **PREAMBLE** của `main_NO_IMAGES.tex`:

```latex
% After \begin{document}
\begin{document}

% Global smaller font
\let\oldframe\frame
\renewcommand{\frame}[1][]{\oldframe[#1]\footnotesize}

...
```

---

## ✅ KẾT QUẢ SAU KHI FIX

- Tất cả slides vừa khít trong 1 trang
- Không mất chữ
- Font vẫn đọc được (không quá nhỏ)
- Trình bày gọn gàng, chuyên nghiệp

---

## 📞 NẾU VẪN BỊ TRÀN

1. Tăng `shrink`: từ `5` → `10` → `15`
2. Giảm font: `\footnotesize` → `\scriptsize`
3. Chia slide: Dùng `allowframebreaks` để tự động chia
4. Cắt content: Bớt 1-2 bullet points

---

**Đảm bảo 100% không mất chữ!** ✓
