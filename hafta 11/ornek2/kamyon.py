from arac import Arac

class Kamyon(Arac):
    def __init__(self, renk, teker_sayisi, motor_gucu, koltuk_sayisi,yukseklik):
        super().__init__(renk, teker_sayisi, motor_gucu, koltuk_sayisi)
        self.yukseklik = yukseklik
    
    def bilgilerini_yazdir(self):
        print(self.yukseklik)
        return super().bilgilerini_yazdir()
