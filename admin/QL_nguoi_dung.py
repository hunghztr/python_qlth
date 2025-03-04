import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

# MySQL database connection
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='Tien123@',
                       db='qlth',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


def hien_thi(listbox, query=""):
    listbox.delete(*listbox.get_children())  # Delete old data in listbox

    if query:
        cursor.execute("SELECT * FROM nguoi_dung WHERE id LIKE %s OR tai_khoan LIKE %s OR mat_khau LIKE %s OR vai_tro LIKE %s", (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"))
    else:
        cursor.execute("SELECT * FROM nguoi_dung")

    rows = cursor.fetchall()
    for row in rows:
        listbox.insert("", "end", values=(row['id'], row['tai_khoan'], row['mat_khau'], row['vai_tro']))  # Insert data into Treeview


def tim_kiem(listbox, search_entry):
    query = search_entry.get()
    hien_thi(listbox, query)


def them_nguoi_dung(listbox):
    def save_new_user():
        tk = taikhoan_entry.get()
        mk = matkhau_entry.get()
        vt = vaitro_entry.get()

        if not tk or not mk or not vt:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute("INSERT INTO nguoi_dung (tai_khoan, mat_khau, vai_tro) VALUES (%s, %s, %s)", (tk, mk, vt))
            conn.commit()
            messagebox.showinfo("Thành công", "Thêm thành công!")
            root.destroy()
            hien_thi(listbox)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể thêm: {e}")

    root = tk.Toplevel()
    root.title("Thêm Người Dùng")
    root.geometry("450x350")
    root.resizable(False, False)

    # Dùng grid() toàn bộ
    tk.Label(root, text="Thêm Người Dùng", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Tài khoản:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    taikhoan_entry = tk.Entry(root, font=('Arial', 12))
    taikhoan_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Mật khẩu:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    matkhau_entry = tk.Entry(root, font=('Arial', 12), show="*")
    matkhau_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Vai trò:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    vaitro_entry = tk.Entry(root, font=('Arial', 12))
    vaitro_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    btn_save = tk.Button(root, text="Thêm", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=save_new_user)
    btn_save.grid(row=4, column=0, columnspan=2, pady=20)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)


def sua(listbox):
    selected_item = listbox.selection()

    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người để sửa!")
        return

    selected_data = listbox.item(selected_item[0], "values")
    id = selected_data[0]
    tko = selected_data[1]
    mk = selected_data[2]
    vt = selected_data[3]

    def save_changes():
        taik = tinhtrang_entry.get()
        matkhau = idtoa_entry.get()
        vait = idtoa_entry1.get()

        if not taik or not matkhau or not vait:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute("UPDATE nguoi_dung SET tai_khoan = %s, mat_khau = %s, vai_tro = %s WHERE id = %s",
                           (taik, matkhau, vait, id))
            conn.commit()
            messagebox.showinfo("Thành công", "Sửa thành công!")
            root.destroy()
            hien_thi(listbox)  # Refresh the list after editing the seat
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sửa: {e}")

    root = tk.Tk()
    root.title("Sửa Ghế Ngồi")
    root.geometry("400x300")

    tk.Label(root, text="Sửa Ghế Ngồi", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Tài khoản:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
    tinhtrang_entry.insert(0, tko)
    tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Mât khẩu:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry = tk.Entry(root, font=('Arial', 12))
    idtoa_entry.insert(0, mk)
    idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Vai trò:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry1 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry1.insert(0, vt)
    idtoa_entry1.grid(row=4, column=1, padx=10, pady=10, sticky="ew")


    btn_save = tk.Button(root, text="Lưu thay đổi", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=save_changes)
    btn_save.grid(row=5, column=0, columnspan=2, pady=20)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    root.mainloop()


def xoa(listbox):
    selected_item = listbox.selection()

    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người dùng để xóa!")
        return

    selected_data = listbox.item(selected_item[0], "values")
    id_user = selected_data[0]

    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa người dùng với ID {id_user}?")
    if confirm:
        try:
            cursor.execute("DELETE FROM nguoi_dung WHERE id = %s", (id_user,))
            conn.commit()
            messagebox.showinfo("Thành công", "Xóa thành công!")
            hien_thi(listbox)  # Refresh the list after deleting
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa: {e}")


def show_ql_nguoi_dung(main_frame, show_home_func):
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="Quản lý Người Dùng", font=('Arial', 14, 'bold')).pack(pady=10)

    search_frame = tk.Frame(main_frame)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Tìm kiếm:", font=('Arial', 12))
    search_label.grid(row=0, column=0, padx=5)

    search_entry = tk.Entry(search_frame, font=('Arial', 12), width=20)
    search_entry.grid(row=0, column=1, padx=5)

    search_button = tk.Button(search_frame, text="Tìm kiếm", font=('Arial', 12), bg="#4CAF50", fg="white",
                              command=lambda: tim_kiem(listbox, search_entry))
    search_button.grid(row=0, column=2, padx=5)

    listbox = ttk.Treeview(main_frame, columns=("ID", "Tài khoản", "Mật khẩu", "Vai trò"), show="headings")
    for col in ("ID", "Tài khoản", "Mật khẩu", "Vai trò"):
        listbox.heading(col, text=col)
        listbox.column(col, width=100)
    listbox.pack(pady=10)

    btn_frame = tk.Frame(main_frame)
    btn_frame.pack()

    tk.Button(btn_frame, text="Thêm", width=10, bg="#4CAF50", fg="white", command=lambda: them_nguoi_dung(listbox)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="Sửa", width=10, bg="#FFEB3B", fg="black", command=lambda: sua(listbox)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(btn_frame, text="Xóa", width=10, bg="#F44336", fg="white", command=lambda: xoa(listbox)).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(main_frame, text="Quay lại", width=30, command=show_home_func).pack(pady=10)

    hien_thi(listbox)