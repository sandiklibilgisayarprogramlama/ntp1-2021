from arac import Arac

class Araba(Arac):
    def __init__(self, marka, model, yakit_tipi, gunluk_tutar, km_basina_yakilan,kapi_sayisi,bagaj_hacmi):
        super().__init__(marka, model, yakit_tipi, gunluk_tutar, km_basina_yakilan)
        self.kapi_sayisi = kapi_sayisi
        self.bagaj_hacmi = bagaj_hacmi
