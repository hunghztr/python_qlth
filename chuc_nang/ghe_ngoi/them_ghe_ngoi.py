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


def ql_ghe_ngoi(): open_file("../../QL_ghe_ngoi.py")


def them_ghe_ngoi():
    tinh_trang = tinhtrang_entry.get()
    id_toa = idtoa_entry.get()

    if not id or not tinh_trang or not id_toa:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        cursor.execute("insert into ghe_ngoi (tinh_trang, id_toa) values (%s, %s)", (tinh_trang, id_toa))
        conn.commit()

        messagebox.showinfo("Thành công", "Thêmthành công!")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm: {e}")


root = tk.Tk()
root.title("Thêm Ghế Ngồi")
root.geometry("400x300")

tk.Label(root, text="Thêm Ghế Ngồi", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Tình Trạng:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="ID Toa:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
idtoa_entry = tk.Entry(root, font=('Arial', 12))
idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

btn_edit = tk.Button(root, text="Thêm", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=them_ghe_ngoi)
btn_edit.grid(row=4, column=0, columnspan=2, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

root.mainloop()
