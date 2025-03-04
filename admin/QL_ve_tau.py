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
            cursor.execute("SELECT * FROM ve_tau WHERE id LIKE %s OR gia_tien LIKE %s OR ten_toa LIKE %s OR ten_tau LIKE %s OR id_kh LIKE %s OR id_ghe_ngoi LIKE %s", (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"))
    else:
        cursor.execute("SELECT * FROM ve_tau")

    rows = cursor.fetchall()
    for row in rows:
        listbox.insert("", "end", values=(row['id'], row['gia_tien'], row['ten_toa'], row['ten_tau'], row['id_kh'], row['id_ghe_ngoi']))


def tim_kiem(listbox, search_entry):
    query = search_entry.get()
    hien_thi(listbox, query)


def them_lich_trinh(listbox):
    def save_new_seat():
        giatien = tinhtrang_entry.get()
        tentoa = idtoa_entry.get()
        tentau = idtoa_entry1.get()
        idgn = idtoa_entry3.get()


        if not giatien or not tentoa or not tentau  or not idgn:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute("INSERT INTO ve_tau (gia_tien, ten_toa, ten_tau,id_ghe_ngoi ) VALUES ( %s, %s,%s, %s)",(giatien, tentoa, tentau, idgn))
            conn.commit()
            messagebox.showinfo("Thành công", "Thêm thành công!")
            root.destroy()
            hien_thi(listbox)  # Refresh the list after adding the new seat
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể thêm: {e}")

    root = tk.Tk()
    root.title("Thêm vé tàu")
    root.geometry("400x350")

    tk.Label(root, text="Thêm vé tàu", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Giá tiền:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
    tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Tên toa:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry = tk.Entry(root, font=('Arial', 12))
    idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Tên tàu:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry1 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry1.grid(row=4, column=1, padx=10, pady=10, sticky="ew")


    tk.Label(root, text="ID ghế ngồi:", font=('Arial', 12)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry3 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry3.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    btn_save = tk.Button(root, text="Thêm", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=save_new_seat)
    btn_save.grid(row=7, column=0, columnspan=2, pady=20)

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
    gt = selected_data[1]
    tt = selected_data[2]
    tent = selected_data[3]
    idkh = selected_data[4]
    idgn = selected_data[5]

    def save_changes():
        giatien = tinhtrang_entry.get()
        tentoa = idtoa_entry.get()
        tentau = idtoa_entry1.get()
        id_kh = idtoa_entry2.get()
        id_gn = idtoa_entry3.get()

        if not giatien or not tentoa or not tentau or not id_gn :
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            cursor.execute(
                "UPDATE ve_tau SET gia_tien = %s, ten_toa = %s, ten_tau = %s, id_kh = %s, id_ghe_ngoi = %s WHERE id = %s",
                (giatien, tentoa, tentau, id_kh, id_gn, ID))

            conn.commit()
            messagebox.showinfo("Thành công", "Sửa thành công!")
            root.destroy()
            hien_thi(listbox)  # Refresh the list after editing the seat
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sửa: {e}")

    root = tk.Tk()
    root.title("Sửa vé tàu")
    root.geometry("400x330")

    tk.Label(root, text="Sửa vé tàu", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Giá tiền:", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tinhtrang_entry = tk.Entry(root, font=('Arial', 12))
    tinhtrang_entry.insert(0,gt)
    tinhtrang_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Tên toa:", font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry = tk.Entry(root, font=('Arial', 12))
    idtoa_entry.insert(0,tt)
    idtoa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="Tên tàu:", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry1 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry1.insert(0,tent)
    idtoa_entry1.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="ID kh:", font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry2 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry2.insert(0, idkh)
    idtoa_entry2.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(root, text="ID ghế ngồi:", font=('Arial', 12)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
    idtoa_entry3 = tk.Entry(root, font=('Arial', 12))
    idtoa_entry3.insert(0, idgn)
    idtoa_entry3.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    btn_save = tk.Button(root, text="Lưu thay đổi", width=15, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", command=save_changes)
    btn_save.grid(row=7, column=0, columnspan=2, pady=20)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    root.mainloop()


def xoa(listbox):
    selected_item = listbox.selection()

    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một ghế để xóa!")
        return

    selected_data = listbox.item(selected_item[0], "values")
    id_ghe = selected_data[0]

    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa vé với ID {id_ghe}?")
    if confirm:
        try:
            cursor.execute("DELETE FROM ve_tau WHERE id = %s", (id_ghe,))
            conn.commit()
            messagebox.showinfo("Thành công", "Xóa thành công!")
            hien_thi(listbox)  # Refresh the list after deleting the seat
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa: {e}")

# Main function to show the seat management interface
def show_ql_ve_tau(main_frame, show_home_func):
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="Quản lý vé tàu", font=('Arial', 14, 'bold')).pack(pady=10)

    search_frame = tk.Frame(main_frame)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Tìm kiếm:", font=('Arial', 12))
    search_label.grid(row=0, column=0, padx=5)

    search_entry = tk.Entry(search_frame, font=('Arial', 12), width=20)
    search_entry.grid(row=0, column=1, padx=5)

    search_button = tk.Button(search_frame, text="Tìm kiếm", font=('Arial', 12), bg="#4CAF50", fg="white", command=lambda: tim_kiem(listbox, search_entry))
    search_button.grid(row=0, column=2, padx=5)

    listbox = ttk.Treeview(main_frame, columns=("ID", "Giá tiền", "Tên toa", "Tên tàu", "ID kh", "ID ghế ngồi"), show="headings")
    for col in ("ID", "Giá tiền", "Tên toa", "Tên tàu", "ID kh", "ID ghế ngồi"):
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

