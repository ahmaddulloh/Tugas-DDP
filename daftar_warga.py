import datetime
class Orang:
    lingkungan  = "RT 2/30 Kelurahan Majujaya"
    def __init__(self, nama, tgl_lahir):
        self.nama_lengkap = nama
        strTanggal = tgl_lahir
        arrTanggal = strTanggal.split("-")
        self.tgl_lahir = datetime.datetime(int(arrTanggal[2]), int(arrTanggal[1]), int(arrTanggal[0])).strftime("%A, %d %B %Y")
    def tulis_deskripsi(self):
        return self.nama_lengkap + "lahir pada tanggal %s" % self.tgl_lahir

orang1 = Orang("Ahmad", "20-03-1987")
orang2 = Orang("Bayu", "12-05-1988")

daftar_warga = (orang1,orang2)
print(Orang.lingkungan)
for i in daftar_warga:
    print(i.tulis_deskripsi())