import tkinter as tk
from tkinter import messagebox

def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    course = var_course.get()
    
    if not name or not email or not phone:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return

    if "@" not in email:
        messagebox.showerror("Lỗi định dạng", "Email không hợp lệ! (Phải có ký tự @)")
        return

    result_label.config(text=f"Success: \nName: {name} \nEmail: {email} \nRegistered for {course}", fg="green")

def cap_nhat_gia(*args):
    khoa_hoc = var_course.get()
    if khoa_hoc == "Python Basic":
        gia = "500.000 VNĐ"
    elif khoa_hoc == "Web Development":
        gia = "700.000 VNĐ"
    elif khoa_hoc == "Data Science":
        gia = "600.000 VNĐ"
    else:
        gia = "0 VNĐ"
    lbl_gia_hien_tai.config(text=f"Giá tiền: {gia}")

window = tk.Tk()
window.title("Workshop Registration System")
window.geometry("450x550")

window.grid_columnconfigure(0, weight=1, uniform="group1")
window.grid_columnconfigure(1, weight=1, uniform="group1")

title_lbl = tk.Label(window, text="WORKSHOP REGISTRATION", font=("Arial", 16, "bold"))
title_lbl.grid(row=0, column=0, columnspan=2, pady=30)

tk.Label(window, text="Full Name:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(window, width=25)
entry_name.grid(row=1, column=1, sticky="w", padx=10, pady=5)

tk.Label(window, text="Email:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_email = tk.Entry(window, width=25)
entry_email.grid(row=2, column=1, sticky="w", padx=10, pady=5)

tk.Label(window, text="Phone Number:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_phone = tk.Entry(window, width=25)
entry_phone.grid(row=3, column=1, sticky="w", padx=10, pady=5)

tk.Label(window, text="Select Workshop:").grid(row=4, column=0, sticky="e", padx=10, pady=10)
var_course = tk.StringVar(value="Python Basic")
var_course.trace_add("write", cap_nhat_gia)
courses = ["Python Basic", "Web Development", "Data Science"]
dropdown = tk.OptionMenu(window, var_course, *courses)
dropdown.config(width=21)
dropdown.grid(row=4, column=1, sticky="w", padx=10, pady=10)

lbl_gia_hien_tai = tk.Label(window, text="Giá tiền: 500.000 VNĐ", font=("Arial", 11, "bold"), fg="red", width=25, anchor="center")
lbl_gia_hien_tai.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Results will appear here", fg="blue", justify="center", height=4)
result_label.grid(row=6, column=0, columnspan=2, pady=10)

btn_submit = tk.Button(window, text="Register Now", command=submit_data, bg="#28a745", fg="white", font=("Arial", 10, "bold"), width=20)
btn_submit.grid(row=7, column=0, columnspan=2, pady=20)

window.mainloop()