from kisi import Kisi

class Hoca(Kisi):
    def __init__(self, ad, soyad, tcno, tel,danisman_ogrenciler):
        super().__init__(ad, soyad, tcno, tel)
        self.danisman_ogrencileri = danisman_ogrenciler