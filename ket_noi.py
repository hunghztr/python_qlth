import pymysql
from tkinter import messagebox
class ket_noi:
    def __init__(self):
        self.ket_noi = pymysql.connect(host="localhost",user="root",password="141512",database="qlth")
        self.cursor = self.ket_noi.cursor()
    def thuc_thi(self,truy_van,tham_so=None):
        self.cursor.execute(truy_van,tham_so or ())
        self.ket_noi.commit()
        if self.cursor.rowcount == 0:
            messagebox.showinfo("thông báo","thực thi thất bại")

    def lay_du_lieu(self,truy_van,tham_so=None):
        self.cursor.execute(truy_van,tham_so or ())
        return self.cursor.fetchall()
    def ngat_ket_noi(self):
        self.cursor.close()
        self.ket_noi.close()