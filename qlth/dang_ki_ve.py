import tkinter as tk
from tkinter import ttk, messagebox
from BTL_PY.ket_noi import ket_noi


class QuanLyVe:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(self.parent)
        self.frame.pack(expand=1, fill="both")

        ttk.Label(self.frame, text="Quản lý Vé", font=("Arial", 14)).pack(pady=10)
        # Tạo ô tìm kiếm
        khuon_tim_kiem = ttk.Frame(self.frame)
        khuon_tim_kiem.pack()
        kn = ket_noi()
        sql_don = "select diem_don from lich_trinh"
        lt_don = kn.lay_du_lieu(sql_don)
        sql_den = "select diem_den from lich_trinh"
        lt_den = kn.lay_du_lieu(sql_den)
        ttk.Label(khuon_tim_kiem,text="chọn điểm đón").pack(side=tk.LEFT)
        self.cb_diem_don = ttk.Combobox(khuon_tim_kiem,state="readonly")
        self.cb_diem_don.pack(side=tk.LEFT,padx=10)
        ttk.Label(khuon_tim_kiem,text="chọn điểm đến").pack(side=tk.LEFT)
        self.cb_diem_den = ttk.Combobox(khuon_tim_kiem,state="readonly")
        self.cb_diem_den.pack(side=tk.LEFT)
        self.cb_diem_don["values"] = [row[0] for row in lt_don]
        self.cb_diem_den["values"] = [row[0] for row in lt_den]
        ttk.Button(khuon_tim_kiem, text="Tìm kiếm", command=self.tim_chuyen_tau).pack(side=tk.LEFT, padx=10)

        # Tạo bảng TreeView
        self.ticket_tree = ttk.Treeview(self.frame, columns=("ID", "Giá tiền", "Tên toa","Tên tàu","Id khách","Ghế ngồi"), show='headings')
        self.ticket_tree.column("ID", anchor="center", width=50)
        self.ticket_tree.column("Giá tiền", anchor="center", width=50)
        self.ticket_tree.column("Tên toa", anchor="center", width=50)
        self.ticket_tree.column("Tên tàu", anchor="center", width=50)
        self.ticket_tree.column("Id khách", anchor="center", width=50)
        self.ticket_tree.column("Ghế ngồi", anchor="center", width=50)
        self.ticket_tree.heading("ID", text="ID")
        self.ticket_tree.heading("Giá tiền", text="Giá tiền")
        self.ticket_tree.heading("Tên toa", text="Tên toa")
        self.ticket_tree.heading("Tên tàu", text="Tên tàu")
        self.ticket_tree.heading("Id khách", text="Id khách")
        self.ticket_tree.heading("Ghế ngồi", text="Ghế ngồi")
        self.ticket_tree.pack(pady=10, padx=50, fill=tk.BOTH, expand=True)
        self.load_tickets()

        # Tạo các nút chức năng
        khuon = ttk.Frame(self.frame)
        khuon.pack(pady=5)
        ttk.Button(khuon, text="Đặt Vé", command=self.open_add_ticket_form, width=20).pack(side=tk.LEFT, pady=10)
        ttk.Button(khuon, text="Hủy Vé", command=self.open_delete_ticket_form, width=20).pack(side=tk.LEFT, padx=10)
        kn.ngat_ket_noi()

    def tim_chuyen_tau(self):
        for child in self.ticket_tree.get_children():
            self.ticket_tree.delete(child)
        don = self.cb_diem_don.get()
        den = self.cb_diem_den.get()
        kn = ket_noi()
        sql = "select id from lich_trinh where diem_don = %s and diem_den = %s"
        tham_so = (don,den)
        lt = kn.lay_du_lieu(sql,tham_so)
        id_lt = [row[0] for row in lt]
        if id_lt is not None:
            sql_lay_id_tau = "select id_tau from chi_tiet_lich_trinh where id_lich = %s"
            tham_so = (id_lt[0],)
            tau = kn.lay_du_lieu(sql_lay_id_tau,tham_so)
            if tau is not None:
                for row in tau:
                    sql_lay_toa = "select id from toa where id_tau = %s"
                    tham_so = (row[0],)
                    toa = kn.lay_du_lieu(sql_lay_toa,tham_so)
                    if toa is not None:
                        for row_toa in toa:
                            sql_lay_id_ghe = "select id from ghe_ngoi where id_toa = %s and tinh_trang = %s"
                            tham_so = (row_toa[0],"trống")
                            ghe = kn.lay_du_lieu(sql_lay_id_ghe,tham_so)
                            if ghe is not None:
                                for row_ghe in ghe:
                                    sql_lay_ve = "select * from ve_tau where id_ghe_ngoi = %s"
                                    tham_so = (row_ghe[0],)
                                    ve = kn.lay_du_lieu(sql_lay_ve,tham_so)

                                    for i in ve:
                                        self.ticket_tree.insert("",tk.END,values=i)


        kn.ngat_ket_noi()

    def load_tickets(self, tham_so=None):
        for row in self.ticket_tree.get_children():
            self.ticket_tree.delete(row)
        kn = ket_noi()
        tickets = kn.lay_du_lieu("SELECT ve_tau.id,"
                                     "ve_tau.gia_tien,"
                                     "ve_tau.ten_toa,"
                                     "ve_tau.ten_tau,"
                                     "ve_tau.id_kh,ghe_ngoi.tinh_trang"
                                     " FROM ve_tau , ghe_ngoi where ve_tau.id_ghe_ngoi = ghe_ngoi.id")
        for ticket in tickets:
            self.ticket_tree.insert("", tk.END, values=ticket)
        kn.ngat_ket_noi()

    def add_ticket(self):
        id_kh = self.customer_id_entry.get()
        id_ve = self.ticket_entry.get()
        kn = ket_noi()
        sql = "update ve_tau set id_kh = %s where id = %s"
        tham_so = (id_kh,id_ve)
        kn.thuc_thi(sql,tham_so)
        sql_lay_id_ghe = "select id_ghe_ngoi from ve_tau where id = %s"
        tham_so = (id_ve,)
        ghe = kn.lay_du_lieu(sql_lay_id_ghe,tham_so)
        if ghe is not None:
            sql_update_ghe = "update ghe_ngoi set tinh_trang = %s where id = %s"
            tham_so = ("không trống",ghe[0])
            kn.thuc_thi(sql_update_ghe,tham_so)
            sql_lay_id_toa = "select id_toa from ghe_ngoi where id = %s"
            tham_so = (ghe[0],)
            toa = kn.lay_du_lieu(sql_lay_id_toa,tham_so)
            if toa is not None:
                sql_update_toa = "update toa set so_ghe_trong = so_ghe_trong - 1 where id = %s"
                tham_so = (toa[0])
                kn.thuc_thi(sql_update_toa,tham_so)
            messagebox.showinfo("thông báo", "đặt vé cho khách thành công")
        kn.ngat_ket_noi()
        self.add_window.destroy()
        self.load_tickets()
    def open_add_ticket_form(self):
        """ Mở form đặt vé """
        self.add_window = tk.Toplevel(self.parent)
        self.add_window.title("Đặt Vé")
        self.add_window.geometry("300x200")

        ttk.Label(self.add_window, text="Id Khách Hàng:").pack(pady=5)
        self.customer_id_entry = ttk.Entry(self.add_window)
        self.customer_id_entry.pack()

        ttk.Label(self.add_window, text="Mã vé:").pack(pady=5)
        self.ticket_entry = ttk.Entry(self.add_window)
        self.ticket_entry.pack()

        ttk.Button(self.add_window, text="Xác nhận", command=self.add_ticket).pack(pady=10)

    def delete_ticket(self):
        id = self.ticket_id_entry.get()
        kn = ket_noi()
        sql = "update ve_tau set id_kh = NULL where id = %s"
        tham_so = (id,)
        kn.thuc_thi(sql,tham_so)
        sql_lay_id_ve = "select id_ghe_ngoi from ve_tau where id = %s"
        tham_so = (id,)
        ghe = kn.lay_du_lieu(sql_lay_id_ve,tham_so)
        sql_update_tinh_trang = "update ghe_ngoi set tinh_trang = %s where id = %s"
        tham_so = ("trống",ghe[0])
        kn.thuc_thi(sql_update_tinh_trang,tham_so)
        kn.ngat_ket_noi()
        self.delete_window.destroy()
        self.load_tickets()
    def open_delete_ticket_form(self):
        """ Mở form hủy vé """
        self.delete_window = tk.Toplevel(self.parent)
        self.delete_window.title("Hủy Vé")
        self.delete_window.geometry("300x200")

        ttk.Label(self.delete_window, text="ID Vé:").pack(pady=5)
        self.ticket_id_entry = ttk.Entry(self.delete_window)
        self.ticket_id_entry.pack()

        ttk.Button(self.delete_window, text="Xóa", command=self.delete_ticket).pack(pady=10)
