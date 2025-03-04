from BTL_PY.ket_noi import ket_noi

kn = ket_noi()
sql = "insert into chi_tiet_lich_trinh values(%s,%s)"
# sql = "delete from chi_tiet_lich_trinh where id_tau = 2"
tham_so = (2,1)
kn.thuc_thi(sql,tham_so)