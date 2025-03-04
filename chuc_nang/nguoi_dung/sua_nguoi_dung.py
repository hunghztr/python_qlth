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


def sua_nguoi_dung():
    id = id_entry.get()
    tk = taikhoan_entry.get()
    mk = matkhau_entry.get()
    vt = vaitro_entry.get()

    if not id:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        cursor.execute("UPDATE nguoi_dung SET tai_khoan = %s, mat_khau = %s, vai_tro = %s WHERE id = %s",
                       (tk, mk, vt, id))
        conn.commit()

        messagebox.showinfo("Thành công", "Sửa thành công!")
        ql_nguoi_dung()

    except Exception as e:
        messagebox.showerror("Lỗi", f"không thể sửa: {e}")

root = tk.Tk()
root.title("Sửa Người Dùng")
root.geometry("400x350")

tk.Label(root, text="Sửa Người Dùng", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="ID:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
id_entry = tk.Entry(root, font=('Arial', 12))
id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Tài khoản:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
taikhoan_entry = tk.Entry(root, font=('Arial', 12))
taikhoan_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Mật khẩu:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
matkhau_entry = tk.Entry(root, font=('Arial', 12))
matkhau_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Vai trò:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
vaitro_entry = tk.Entry(root, font=('Arial', 12))
vaitro_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

btn_edit = tk.Button(root, text="Sửa", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=sua_nguoi_dung)
btn_edit.grid(row=5, column=0, columnspan=2, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

root.mainloop()
