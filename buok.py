from ket_noi import ket_noi

class ThemChuyenDi:
    def __init__(self):
        self.kn = ket_noi()
    def dong(self):
        self.kn.ngat_ket_noi()
    def them_lich_trinh(self):
        sql = "insert into lich_trinh (thoi_gian,diem_don,diem_den) values(%s,%s,%s)"
        tham_so = ("6h","Hà Nội","Hải Phòng")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("6h","Hà Tây","Hải Dương")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("6h","Vĩnh Phúc","Quảng Ninh")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("12h","Tuyên Quang","Hà Nội")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("12h","Hà Giang","Hải Phòng")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("18h","Ninh Bình","Hà Nội")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("18h","Hà Tĩnh","Bắc Giang")
        self.kn.thuc_thi(sql,tham_so)
    def them_tau(self):
        sql = "insert into tau (ten,so_toa) values(%s,%s)"
        tham_so = ("A01","3")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("A02","3")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("A03","3")
        self.kn.thuc_thi(sql,tham_so)

    def them_ctlt(self):
        sql = "insert into chi_tiet_lich_trinh values(%s,%s)"
        tham_so = ("1","1")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("1","2")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("2","1")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("2","3")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("3","4")
        self.kn.thuc_thi(sql,tham_so)
    def them_toa(self):
        sql = "insert into toa (ten,tong_ghe,so_ghe_trong,id_tau) values(%s,%s,%s,%s)"
        tham_so = ("A01-1","10","10","1")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("A01-2","10","10","1")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("A02-1","10","10","2")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("A03-2","10","10","3")
        self.kn.thuc_thi(sql,tham_so)
    def them_ghe(self):
        sql = "insert into ghe_ngoi (tinh_trang,id_toa) values(%s,%s)"
        tham_so = ("trống","1")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("trống","1")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("trống","2")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("trống","2")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("trống","3")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("trống","4")
        self.kn.thuc_thi(sql,tham_so)
    def them_ve(self):
        sql = "insert into ve_tau (gia_tien,ten_toa,ten_tau,id_ghe_ngoi) values(%s,%s,%s,%s)"
        tham_so = ("100000","A01-1","A01","1")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("150000","A01-1","A01","2")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("200000","A01-2","A01","3")
        self.kn.thuc_thi(sql,tham_so)
        tham_so = ("150000","A02-1","A02","5")
        self.kn.thuc_thi(sql,tham_so)

them = ThemChuyenDi()
them.them_lich_trinh()
them.them_tau()
them.them_ctlt()
them.them_toa()
them.them_ghe()
them.them_ve()