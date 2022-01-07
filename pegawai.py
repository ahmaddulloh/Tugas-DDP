import datetime

class pegawai :
    honor_per_jam = 30000

    def __init__(self,nama,jam_kerja):
        self.nama = nama
        self.jam_kerja = jam_kerja

    def honor (self):
        hasil = self.jam_kerja * pegawai.honor_per_jam
        return "Honor %s" % self.nama + "selama %s" % self.jam_kerja + " jam adalah %s" % hasil 

abdul = pegawai("abdul ", 6)
print(abdul.honor())