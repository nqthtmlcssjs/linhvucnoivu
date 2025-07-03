from PyPDF2 import PdfMerger
import os

# Xác định đường dẫn hiện tại
print("📂 Thư mục hiện tại:", os.getcwd())

# Tên chính xác của file cần gộp
file1 = "22_so_y_te.pdf"
file2 = "22a_so_y_te_phu_luc.pdf"

# Kiểm tra tồn tại
if not os.path.exists(file1) or not os.path.exists(file2):
    print("⚠️ Không tìm thấy 1 trong 2 file PDF!")
else:
    merger = PdfMerger()
    merger.append(file1)
    merger.append(file2)
    merger.write("22_so_y_te_full.pdf")
    merger.close()
    print("✅ Đã tạo file gộp: 22_so_y_te_full.pdf")
