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

    if query:  # If there's a search query
        cursor.execute("SELECT * FROM lich_trinh WHERE id LIKE %s OR thoi_gian LIKE %s OR diem_don LIKE %s OR diem_den LIKE %s", (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"))
    else:
        cursor.execute("SELECT * FROM lich_trinh")

    rows = cursor.fetchall()
    for row in rows:
        listbox.insert("", "end", values=(row['id'], row['thoi_gian'], row['diem_don'], row['diem_den']))


def tim_kiem(listbox, search_entry):
    query = search_entry.get()
    hien_thi(listbox, query)


def them_lich_trinh(listbox):
    def save_new_seat():
        thoigian = tinhtrang_entry.get()
        diemdon = idtoa_entry.get()
        diemden = idtoa_entry1.get()


        if not thoigian or not diemdon or not diemden:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute("INSERT INTO lich_trinh (thoi_gian, diem_don, diem_den) VALUES (%s, %s, %s)",(thoigian, diemdon, diemden))
            conn.commit()
            messagebox.showinfo("Thành công", "Thêm thành công!")
            root.destroy()
            hien_thi(listbox)  # Refresh the list after adding the new seat
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể thêm: {e}")

    root = tk.Tk()
    root.title("Thêm lịch trình")
    root.geometry("400x300")

    tk.Label(root, text="Thêm lịch trình", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Thời gian:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
    tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Điểm đón:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry = tk.Entry(root, font=('Arial', 12))
    idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Điểm đến:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry1 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry1.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    btn_save = tk.Button(root, text="Thêm", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=save_new_seat)
    btn_save.grid(row=5, column=0, columnspan=2, pady=20)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    root.mainloop()

def sua(listbox):
    selected_item = listbox.selection()

    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một ghế để sửa!")
        return

    selected_data = listbox.item(selected_item[0], "values")
    ID = selected_data[0]
    thoigiaN = selected_data[1]
    diemdoN = selected_data[2]
    diemdeN = selected_data[3]

    def save_changes():
        thoigian = tinhtrang_entry.get()
        diemdon = idtoa_entry.get()
        diemden = idtoa_entry1.get()

        if not thoigian or not diemdon or not diemden:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute("UPDATE lich_trinh SET thoi_gian = %s, diem_don = %s, diem_den = %s WHERE id = %s",
                           (thoigian, diemdon, diemden, ID))
            conn.commit()
            messagebox.showinfo("Thành công", "Sửa thành công!")
            root.destroy()
            hien_thi(listbox)  # Refresh the list after editing the seat
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sửa: {e}")

    root = tk.Tk()
    root.title("Sửa lịch trình")
    root.geometry("400x300")

    tk.Label(root, text="Sửa lịch trình", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Thời gian:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
    tinhtrang_entry.insert(0, thoigiaN)  # Pre-fill with current value
    tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Điểm đón:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry = tk.Entry(root, font=('Arial', 12))
    idtoa_entry.insert(0, diemdoN)  # Pre-fill with current value
    idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Điểm điến:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry1 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry1.insert(0, diemdeN)  # Pre-fill with current value
    idtoa_entry1.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    btn_save = tk.Button(root, text="Lưu thay đổi", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=save_changes)
    btn_save.grid(row=5, column=0, columnspan=2, pady=20)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    root.mainloop()


def xoa(listbox):
    selected_item = listbox.selection()

    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một lịch trình để xóa!")
        return

    selected_data = listbox.item(selected_item[0], "values")
    id_ghe = selected_data[0]

    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa lịch trình với ID {id_ghe}?")
    if confirm:
        try:
            cursor.execute("DELETE FROM lich_trinh WHERE id = %s", (id_ghe,))
            conn.commit()
            messagebox.showinfo("Thành công", "Xóa thành công!")
            hien_thi(listbox)  # Refresh the list after deleting the seat
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa: {e}")

# Main function to show the seat management interface
def show_ql_lich_trinh(main_frame, show_home_func):
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="Quản lý lịch trình", font=('Arial', 14, 'bold')).pack(pady=10)

    search_frame = tk.Frame(main_frame)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Tìm kiếm:", font=('Arial', 12))
    search_label.grid(row=0, column=0, padx=5)

    search_entry = tk.Entry(search_frame, font=('Arial', 12), width=20)
    search_entry.grid(row=0, column=1, padx=5)

    search_button = tk.Button(search_frame, text="Tìm kiếm", font=('Arial', 12), bg="#4CAF50", fg="white", command=lambda: tim_kiem(listbox, search_entry))
    search_button.grid(row=0, column=2, padx=5)

    listbox = ttk.Treeview(main_frame, columns=("ID", "Thời gian", "Điểm đón", "Điểm đến"), show="headings")
    for col in ("ID", "Thời gian", "Điểm đón", "Điểm đến"):
        listbox.heading(col, text=col)
        listbox.column(col, width=100)
    listbox.pack(pady=10)

    btn_frame = tk.Frame(main_frame)
    btn_frame.pack()

    tk.Button(btn_frame, text="Thêm", width=10, bg="#4CAF50", fg="white", command=lambda: them_lich_trinh(listbox)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="Sửa", width=10, bg="#FFEB3B", fg="black", command=lambda: sua(listbox)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(btn_frame, text="Xóa", width=10, bg="#F44336", fg="white", command=lambda: xoa(listbox)).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(main_frame, text="Quay lại", width=30, command=show_home_func).pack(pady=10)

    hien_thi(listbox)

