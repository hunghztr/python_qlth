import pymysql
import tkinter as tk
from tkinter import messagebox
import subprocess

conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='Tien123@',
                       db='qlth',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


def open_file(file_name):
    try:
        subprocess.run(["python", file_name])
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể mở file: {e}")


def ql_nguoi_dung(): open_file("../../QL_nguoi_dung.py")


def them_nguoi_dung():
    tk = taikhoan_entry.get()
    mk = matkhau_entry.get()
    vt = vaitro_entry.get()

    if not id or not tk or not mk or not vt:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        cursor.execute("insert into nguoi_dung (tai_khoan, mat_khau, vai_tro) values (%s, %s, %s)", (tk,mk,vt))
        conn.commit()

        messagebox.showinfo("Thành công", "Thêm thành công!")
        root.destroy()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm: {e}")

root = tk.Tk()
root.title("Thêm Người Dùng")
root.geometry("450x350")

tk.Label(root, text="Thêm Người Dùng", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Tài khoản:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
taikhoan_entry = tk.Entry(root, font=('Arial', 12))
taikhoan_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Mật khẩu:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
matkhau_entry = tk.Entry(root, font=('Arial', 12))
matkhau_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Vai trò:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
vaitro_entry = tk.Entry(root, font=('Arial', 12))
vaitro_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

btn_edit = tk.Button(root, text="Thêm", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=them_nguoi_dung)
btn_edit.grid(row=5, column=0, columnspan=2, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

root.mainloop()
