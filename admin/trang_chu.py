import tkinter as tk
from tkinter import Menu
import QL_ve_tau, QL_tau, QL_toa, QL_ctlt, QL_ttkh, QL_ghe_ngoi, QL_lich_trinh, QL_nguoi_dung

def show_home():
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text="Trang chủ Quản Lý", font=('Arial', 16, 'bold')).pack(pady=20)



def ql_tau(): QL_tau.show_ql_tau(main_frame, show_home)
def ql_toa(): QL_toa.show_ql_toa(main_frame, show_home)
def ql_ghe_ngoi(): QL_ghe_ngoi.show_ql_ghe_ngoi(main_frame, show_home)
def ql_nguoi_dung(): QL_nguoi_dung.show_ql_nguoi_dung(main_frame, show_home)
def ql_ttkh(): QL_ttkh.show_tt_kh(main_frame, show_home)
def ql_ve(): QL_ve_tau.show_ql_ve_tau(main_frame, show_home)
def ql_lich_trinh(): QL_lich_trinh.show_ql_lich_trinh(main_frame, show_home)
def ql_ctlt():QL_ctlt.show_ql_ctlt(main_frame, show_home)

root = tk.Tk()
root.title("Trang Chủ Quản Lý")
root.geometry("800x500")

# Tạo menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Tạo menu Quản lý
menu_quan_ly = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Quản Lý", menu=menu_quan_ly)
menu_quan_ly.add_command(label="Quản lý toa", command= ql_toa)
menu_quan_ly.add_command(label="Quản lý tàu" , command= ql_tau)
menu_quan_ly.add_command(label="Quản lý vé", command= ql_ve)
menu_quan_ly.add_command(label="Quản lý lịch trình", command= ql_lich_trinh)
menu_quan_ly.add_command(label="Quản lý người dùng", command= ql_nguoi_dung)
menu_quan_ly.add_command(label="Quản lý ghế ngồi", command= ql_ghe_ngoi)
menu_quan_ly.add_command(label="Quản lý chi tiết lịch trình", command= ql_ctlt)
menu_quan_ly.add_command(label="Quản lý thông tin khách hàng", command=ql_ttkh)

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)
show_home()
root.mainloop()