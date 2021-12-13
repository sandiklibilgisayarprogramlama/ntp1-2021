from kisi import Kisi


class Ogrenci(Kisi):
    def __init__(self, tcno, ad, soyad, tel, yas,not_ortalama):
        super().__init__(tcno, ad, soyad, tel, yas)
        self.not_ortalama =not_ortalama
    
    def bilgileri_yazdir(self):
        super().bilgileri_yazdir()
        print(self.not_ortalama)
    