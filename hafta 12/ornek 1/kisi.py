class Kisi:
    def __init__(self,tcno,ad,soyad,tel,yas):
        self.tcno = tcno
        self.ad = ad
        self.soyad = soyad
        self.tel = tel
        self.yas = yas
    
    def bilgileri_yazdir(self):
        print(self.ad)
        print(self.soyad)
        print(self.tcno)
        print(self.tel)
        print(self.yas)