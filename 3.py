import tkinter as tk

def hien_ket_qua():
    # Lấy dữ liệu từ Entry (Yêu cầu 2)
    ten = entry_ho_ten.get()
    email = entry_email.get()
    
    # Cập nhật vào Label hiển thị kết quả (Yêu cầu 1)
    lbl_ket_qua.config(text=f"Đã đăng ký: {ten} - {email}")

root = tk.Tk()
root.title("Workshop Registration System")

# Khu vực nhập liệu
entry_ho_ten = tk.Entry(root)
entry_ho_ten.grid(row=0, column=0)

entry_email = tk.Entry(root)
entry_email.grid(row=1, column=0)

# Nút bấm để kích hoạt hiển thị
btn_submit = tk.Button(root, text="Đăng ký", command=hien_ket_qua)
btn_submit.grid(row=2, column=0)

# Khu vực hiển thị kết quả quan trọng nhất
lbl_ket_qua = tk.Label(root, text="", fg="red") 
lbl_ket_qua.grid(row=3, column=0)

root.mainloop()