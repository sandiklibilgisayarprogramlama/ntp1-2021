class Cocuk:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

        self.bilgileri_yazdir()

    # bilgileri yazdır metodu
    def bilgileri_yazdir(self):
        print("ad:",self.ad)
        print("soyad:",self.soyad)
        print("yas:",str(self.yas))