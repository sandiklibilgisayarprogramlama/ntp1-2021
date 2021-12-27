from arac import Arac
class Motor(Arac):
    def __init__(self, marka, model, yakit_tipi, gunluk_tutar, km_basina_yakilan,sepetli_mi,teker_sayisi):
        super().__init__(marka, model, yakit_tipi, gunluk_tutar, km_basina_yakilan)
        self.sepetli_mi = sepetli_mi
        self.teker_say = teker_sayisi