class Ogrenci:
    def __init__(self,ad,soyad,tcno,tel):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tcno
        self.tel = tel
    
    def bilgileri_yazdir(self):
        print(self.ad)
        print(self.soyad)
        print(self.tcno)
        print(self.tel)