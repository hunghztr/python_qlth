import tkinter as tk
from tkinter import ttk
from quan_li_khach import QuanLyKhach
from dang_ki_ve import QuanLyVe
class TrainTicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Bán Vé Tàu Hỏa")
        self.root.geometry("800x500")

        self.tab_control = ttk.Notebook(root)
        self.customer_tab = ttk.Frame(self.tab_control)
        self.ticket_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.customer_tab, text="Quản lý Khách Hàng")
        self.tab_control.add(self.ticket_tab, text="Đặt Vé")
        self.tab_control.pack(expand=1, fill="both")

        self.customer_manager = QuanLyKhach(self.customer_tab)
        self.ticket_manager = QuanLyVe(self.ticket_tab)

root = tk.Tk()
app = TrainTicketApp(root)
root.mainloop()
