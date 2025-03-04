import tkinter as tk
from tkinter import ttk, messagebox
from BTL_PY.ket_noi import ket_noi


class QuanLyKhach:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(self.parent)
        self.frame.pack(expand=1, fill="both")

        ttk.Label(self.frame, text="Danh sách Khách Hàng", font=("Arial", 14)).pack(pady=10)

        # Tạo ô tìm kiếm
        khuon_tim_kiem = ttk.Frame(self.frame)
        khuon_tim_kiem.pack()
        self.tim = ttk.Entry(khuon_tim_kiem, width=30)
        self.tim.pack(side=tk.LEFT)
        ttk.Button(khuon_tim_kiem, text="Tìm kiếm", command=self.tim_kiem).pack(side=tk.LEFT, padx=10)

        # Tạo bảng TreeView
        self.customer_tree = ttk.Treeview(self.frame, columns=("ID", "Tên", "SĐT"), show='headings')
        self.customer_tree.column("ID", anchor="center", width=50)
        self.customer_tree.column("Tên", anchor="center", width=150)
        self.customer_tree.column("SĐT", anchor="center", width=100)
        self.customer_tree.heading("ID", text="ID")
        self.customer_tree.heading("Tên", text="Tên Khách Hàng")
        self.customer_tree.heading("SĐT", text="Số Điện Thoại")
        self.customer_tree.pack(pady=10, padx=50, fill=tk.BOTH, expand=True)
        self.load_customers()

        # Tạo các nút chức năng
        khuon = ttk.Frame(self.frame)
        khuon.pack(pady=5)
        ttk.Button(khuon, text="Thêm Khách Hàng", command=self.open_add_customer_form, width=20).pack(side=tk.LEFT, pady=10)
        ttk.Button(khuon, text="Sửa Khách Hàng", command=self.open_update_customer_form, width=20).pack(side=tk.LEFT, pady=10)
        ttk.Button(khuon, text="Xóa Khách Hàng", command=self.open_delete_customer_form, width=20).pack(side=tk.LEFT, padx=10)

    def load_customers(self, tham_so=None):
        for row in self.customer_tree.get_children():
            self.customer_tree.delete(row)
        kn = ket_noi()
        if tham_so is None:
            customers = kn.lay_du_lieu("SELECT * FROM ttkh")
        else:
            customers = kn.lay_du_lieu("SELECT * FROM ttkh WHERE ten LIKE %s", tham_so)
        for customer in customers:
            self.customer_tree.insert("", tk.END, values=customer)
        kn.ngat_ket_noi()

    def add_customer(self):
        ten = self.new_customer_name.get()
        sdt = self.new_customer_phone.get()
        if not ten or not sdt:
            messagebox.showinfo("Thông báo", "Vui lòng nhập đủ thông tin")
        else:
            sql = "INSERT INTO ttkh (ten, sdt) VALUES (%s, %s)"
            tham_so = (ten, sdt)
            kn = ket_noi()
            kn.thuc_thi(sql, tham_so)
            kn.ngat_ket_noi()
            self.add_window.destroy()
            self.load_customers()

    def open_add_customer_form(self):
        self.add_window = tk.Toplevel(self.parent)
        self.add_window.title("Thêm Khách Hàng")
        self.add_window.geometry("300x200")

        ttk.Label(self.add_window, text="Tên Khách Hàng:").pack(pady=5)
        self.new_customer_name = ttk.Entry(self.add_window)
        self.new_customer_name.pack()

        ttk.Label(self.add_window, text="Số Điện Thoại:").pack(pady=5)
        self.new_customer_phone = ttk.Entry(self.add_window)
        self.new_customer_phone.pack()

        ttk.Button(self.add_window, text="Lưu", command=self.add_customer).pack(pady=10)

    def update_customer(self):
        id = self.new_customer_id.get()
        ten = self.new_customer_name.get()
        sdt = self.new_customer_phone.get()
        if not id or not ten or not sdt:
            messagebox.showinfo("Thông báo", "Vui lòng nhập đủ thông tin")
        else:
            kn = ket_noi()
            sql = "UPDATE ttkh SET ten = %s, sdt = %s WHERE id = %s"
            tham_so = (ten, sdt, id)
            kn.thuc_thi(sql, tham_so)
            kn.ngat_ket_noi()
            self.update_window.destroy()
            self.load_customers()

    def open_update_customer_form(self):
        self.update_window = tk.Toplevel(self.parent)
        self.update_window.title("Cập nhật Khách Hàng")
        self.update_window.geometry("300x200")

        ttk.Label(self.update_window, text="ID:").pack(pady=5)
        self.new_customer_id = ttk.Entry(self.update_window)
        self.new_customer_id.pack()

        ttk.Label(self.update_window, text="Tên Khách Hàng:").pack(pady=5)
        self.new_customer_name = ttk.Entry(self.update_window)
        self.new_customer_name.pack()

        ttk.Label(self.update_window, text="Số Điện Thoại:").pack(pady=5)
        self.new_customer_phone = ttk.Entry(self.update_window)
        self.new_customer_phone.pack()

        ttk.Button(self.update_window, text="Lưu", command=self.update_customer).pack(pady=10)

    def delete_customer(self):
        id = self.new_customer_id.get()
        kn = ket_noi()
        sql = "DELETE FROM ttkh WHERE id = %s"
        tham_so = (id,)
        kn.thuc_thi(sql, tham_so)
        kn.ngat_ket_noi()
        self.delete_window.destroy()
        self.load_customers()

    def open_delete_customer_form(self):
        self.delete_window = tk.Toplevel(self.parent)
        self.delete_window.title("Xóa Khách Hàng")
        self.delete_window.geometry("300x200")

        ttk.Label(self.delete_window, text="ID:").pack(pady=5)
        self.new_customer_id = ttk.Entry(self.delete_window)
        self.new_customer_id.pack()

        ttk.Button(self.delete_window, text="Xóa", command=self.delete_customer).pack(pady=10)

    def tim_kiem(self):
        ten = self.tim.get()
        tham_so = (f"%{ten}%",)
        self.load_customers(tham_so)
