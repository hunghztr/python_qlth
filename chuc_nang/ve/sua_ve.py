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


def ql(): open_file("../../QL_toa.py")


def sua():
    id = id_entry.get()
    giatien = taikhoan_entry.get()
    tentoa = matkhau_entry.get()
    tentau = tao_entry.get()
    kh = khachhang_entry.get()
    ghe = ghe_entry.get()

    if not id:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        cursor.execute("update ve_tau set gia_tien = %s , ten_toa = %s, ten_tau = %s, id_kh = %s, id_ghe_ngoi = %s where id = %s",(giatien,tentoa,tentoa,kh,ghe,id,))
        conn.commit()

        messagebox.showinfo("Thành công", "Sửa thành công!")
        ql()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sửa: {e}")


root = tk.Tk()
root.title("Sửa Vé")
root.geometry("400x400")

tk.Label(root, text="Sửa Vé", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="ID:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
id_entry = tk.Entry(root, font=('Arial', 12))
id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Giá tiền:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
taikhoan_entry = tk.Entry(root, font=('Arial', 12))
taikhoan_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Tên toa:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
matkhau_entry = tk.Entry(root, font=('Arial', 12))
matkhau_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Tên tàu:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
tao_entry = tk.Entry(root, font=('Arial', 12))
tao_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="ID khách hàng:", font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
khachhang_entry = tk.Entry(root, font=('Arial', 12))
khachhang_entry.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="ID ghế ngồi:", font=('Arial', 12)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
ghe_entry = tk.Entry(root, font=('Arial', 12))
ghe_entry.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

btn_edit = tk.Button(root, text="Sửa", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=sua)
btn_edit.grid(row=7, column=0, columnspan=2, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

root.mainloop()
