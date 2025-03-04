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


def ql_tau(): open_file("../../QL_tau.py")


def sua_tau():
    id = id_entry.get()
    ten = taikhoan_entry.get()
    sotoa = matkhau_entry.get()

    if not id:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        cursor.execute("UPDATE tau SET ten = %s, so_toa = %s WHERE id = %s", (ten, sotoa, id)
                       )
        conn.commit()

        messagebox.showinfo("Thành công", "Sửa thành công!")
        ql_tau()

    except Exception as e:
        messagebox.showerror("Lỗi", f"không thể sửa: {e}")

root = tk.Tk()
root.title("Sửa Tàu")
root.geometry("400x300")

tk.Label(root, text="Sửa Tàu", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="ID:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
id_entry = tk.Entry(root, font=('Arial', 12))
id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Tên:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
taikhoan_entry = tk.Entry(root, font=('Arial', 12))
taikhoan_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Số toa:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
matkhau_entry = tk.Entry(root, font=('Arial', 12))
matkhau_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

btn_edit = tk.Button(root, text="Sửa", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=sua_tau)
btn_edit.grid(row=4, column=0, columnspan=2, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

root.mainloop()
