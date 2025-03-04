import tkinter as tk
from tkinter import messagebox
import subprocess

from BTL_PY.ket_noi import ket_noi


def run_python_script():
    try:
        subprocess.run(["python", "admin/trang_chu.py"])
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể mở file: {e}")
def run_python_script_nv():
    try:
        subprocess.run(["python", "qlth/main.py"])
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể mở file: {e}")

login_window = tk.Tk()
login_window.title("Đăng Nhập")
login_window.geometry("300x200")

label_email = tk.Label(login_window, text="Tài khoản:", font=('Arial', 12))
label_email.pack(pady=5)
entry_email = tk.Entry(login_window, font=('Arial', 12))
entry_email.pack(pady=5)

label_password = tk.Label(login_window, text="Mật khẩu:", font=('Arial', 12))
label_password.pack(pady=5)
entry_password = tk.Entry(login_window, show="*", font=('Arial', 12))
entry_password.pack(pady=5)

def login_action():
    email = entry_email.get()
    password = entry_password.get()

    kn = ket_noi()
    sql = "select vai_tro from nguoi_dung where tai_khoan = %s and mat_khau = %s"
    tham_so = (email, password)
    nd = kn.lay_du_lieu(sql,tham_so)
    if nd != ():
        ad = ('ad',)
        if nd[0] == ad:
            run_python_script()
        nv = ('nv',)
        if nd[0] == nv:
            run_python_script_nv()
    elif nd == () :
        messagebox.showinfo("thông báo","vui lòng nhập thông tin chính xác")
login_button = tk.Button(login_window, text="Đăng Nhập", command=login_action, width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white")
login_button.pack(pady=20)



login_window.mainloop()
