
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


def ql(): open_file("../../QL_ctlt.py")

def sua():
    id_tau = id_entry.get()
    id_lich = taikhoan_entry.get()


    if not id_tau :
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        cursor.execute("update ghe_ngoi set id_tau = %s , id_lich = %s ", (id_tau, id_lich))
        conn.commit()

        messagebox.showinfo("Thành công", "Sửa thành công!")
        ql()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sửa : {e}")
root = tk.Tk()
root.title("Sửa Chi Tiết Lịch Trình")  # Tiêu đề cửa sổ
root.geometry("400x300")  # Kích thước cửa sổ

# Cải thiện label và entry
tk.Label(root, text="Sửa Chi Tiết Lịch Trình", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

# Label và Entry cho ID tàu
tk.Label(root, text="ID Tàu:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
id_entry = tk.Entry(root, font=('Arial', 12))
id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Label và Entry cho ID lịch
tk.Label(root, text="ID Lịch:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
taikhoan_entry = tk.Entry(root, font=('Arial', 12))
taikhoan_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Nút "Sửa"
btn_add = tk.Button(root, text="Sửa", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=sua)
btn_add.grid(row=3, column=0, columnspan=2, pady=20)

# Cải thiện tính năng mở rộng cột để ô nhập liệu có thể thay đổi kích thước
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

# Khởi chạy giao diện
root.mainloop()
