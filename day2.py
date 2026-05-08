import tkinter as tk
from tkinter import messagebox

def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    course = var_course.get()
    
    if name and email and phone:
        result_label.config(text=f"Success: \nName:  {name} \nEmail : {email} \nRegistered for {course}")
    if "@" not in email:
        messagebox.showerror("Lỗi định dạng", "Email không hợp lệ! (Phải có ký tự @)")
        return
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

window = tk.Tk()
window.title("Workshop Registration System")
window.geometry("400x450")

title_lbl = tk.Label(window, text="WORKSHOP REGISTRATION", font=("Arial", 16, "bold"))
title_lbl.grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(window, text="Full Name:").grid(row=1, column=0, sticky="w", padx=20)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1, pady=5, padx=20)

tk.Label(window, text="Email:").grid(row=2, column=0, sticky="w", padx=20)
entry_email = tk.Entry(window)
entry_email.grid(row=2, column=1, pady=5, padx=20)

tk.Label(window, text="Phone Number:").grid(row=3, column=0, sticky="w", padx=20)
entry_phone = tk.Entry(window)
entry_phone.grid(row=3, column=1, pady=5, padx=20)

tk.Label(window, text="Select Workshop:").grid(row=4, column=0, sticky="w", padx=20, pady=10)
var_course = tk.StringVar(value="Python Basic")
courses = ["Python Basic", "Web Development", "Data Science"]
dropdown = tk.OptionMenu(window, var_course, *courses)
dropdown.grid(row=4, column=1, sticky="ew", padx=20)

result_label = tk.Label(window, text="Results will appear here", fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=20)

btn_submit = tk.Button(window, text="Register Now", command=submit_data, bg="green", fg="white")
btn_submit.grid(row=6, column=0, columnspan=2, pady=10, ipadx=50)

window.mainloop()