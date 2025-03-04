import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

# MySQL connection
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='141512',
                       db='qlth',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

def hien_thi(listbox, query=""):
    listbox.delete(*listbox.get_children())

    if query:
        cursor.execute("SELECT * FROM ttkh WHERE id LIKE %s OR ten LIKE %s OR sdt LIKE %s", (f"%{query}%", f"%{query}%", f"%{query}%"))
    else:
        cursor.execute("SELECT * FROM ttkh")

    rows = cursor.fetchall()
    for row in rows:
        listbox.insert("", "end", values=(row['id'], row['ten'], row['sdt']))

def tim_kiem(listbox, search_entry):
    query = search_entry.get()
    hien_thi(listbox, query)

def them_khach_hang(listbox):
    def save_new_passenger():
        ten = tinhtrang_entry.get()
        sdt = idtoa_entry.get()

        if not ten or not sdt:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute("INSERT INTO ttkh (ten, sdt) VALUES (%s, %s)", (ten, sdt))
            conn.commit()
            messagebox.showinfo("Thành công", "Thêm thành công!")
            root.destroy()
            hien_thi(listbox)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể thêm: {e}")

    root = tk.Tk()
    root.title("Thêm Khách Hàng")
    root.geometry("400x300")

    tk.Label(root, text="Tên:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
    tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="SĐT:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry = tk.Entry(root, font=('Arial', 12))
    idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    btn_save = tk.Button(root, text="Thêm", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white",
                         command=save_new_passenger)
    btn_save.grid(row=4, column=0, columnspan=2, pady=20)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)


def sua(listbox):
    selected_item = listbox.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn khách hàng để sửa!")
        return

    selected_data = listbox.item(selected_item[0], "values")
    id_kh = selected_data[0]
    ten = selected_data[1]
    sdt = selected_data[2]

    def save_changes():
        new_ten = tinhtrang_entry.get()
        new_sdt = idtoa_entry.get()

        if not new_ten or not new_sdt:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute("UPDATE ttkh SET ten = %s, sdt = %s WHERE id = %s", (new_ten, new_sdt, id_kh))
            conn.commit()
            messagebox.showinfo("Thành công", "Sửa thành công!")
            root.destroy()
            hien_thi(listbox)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sửa: {e}")

    root = tk.Tk()
    root.title("Sửa Khách Hàng")
    root.geometry("400x300")

    tk.Label(root, text="Tên:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
    tinhtrang_entry.insert(0, ten)
    tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="SĐT:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry = tk.Entry(root, font=('Arial', 12))
    idtoa_entry.insert(0, sdt)
    idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    btn_save = tk.Button(root, text="Thêm", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white",
                         command=save_changes)
    btn_save.grid(row=4, column=0, columnspan=2, pady=20)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.mainloop()


def xoa(listbox):
    selected_item = listbox.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn khách hàng để xóa!")
        return

    selected_data = listbox.item(selected_item[0], "values")
    id_kh = selected_data[0]

    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa khách hàng với ID {id_kh}?")
    if confirm:
        try:
            cursor.execute("DELETE FROM ttkh WHERE id = %s", (id_kh,))
            conn.commit()
            messagebox.showinfo("Thành công", "Xóa thành công!")
            hien_thi(listbox)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa: {e}")


def show_tt_kh(main_frame,show_home_func):
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="Quản lý Khách Hàng", font=('Arial', 14, 'bold')).pack(pady=10)

    search_frame = tk.Frame(main_frame)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Tìm kiếm:", font=('Arial', 12))
    search_label.grid(row=0, column=0, padx=5)

    search_entry = tk.Entry(search_frame, font=('Arial', 12), width=20)
    search_entry.grid(row=0, column=1, padx=5)

    search_button = tk.Button(search_frame, text="Tìm kiếm", font=('Arial', 12), bg="#4CAF50", fg="white",
                              command=lambda: tim_kiem(listbox, search_entry))
    search_button.grid(row=0, column=2, padx=5)

    listbox = ttk.Treeview(main_frame, columns=("ID", "Tên", "SĐT"), show="headings")
    for col in ("ID", "Tên", "SĐT"):
        listbox.heading(col, text=col)
        listbox.column(col, width=150)
    listbox.pack(pady=10)

    btn_frame = tk.Frame(main_frame)
    btn_frame.pack()

    tk.Button(btn_frame, text="Thêm", width=10, bg="#4CAF50", fg="white", command=lambda: them_khach_hang(listbox)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="Sửa", width=10, bg="#FFEB3B", fg="black", command=lambda: sua(listbox)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(btn_frame, text="Xóa", width=10, bg="#F44336", fg="white", command=lambda: xoa(listbox)).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(main_frame, text="Quay lại", width=30, command=show_home_func).pack(pady=10)

    hien_thi(listbox)
