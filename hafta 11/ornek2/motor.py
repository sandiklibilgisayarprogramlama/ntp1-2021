from arac import Arac

class Motor(Arac):
    def __init__(self, renk, teker_sayisi, motor_gucu, koltuk_sayisi,yaris_motorumu):
        super().__init__(renk, teker_sayisi, motor_gucu, koltuk_sayisi)
        self.yaris_motorumu = yaris_motorumu
    
    def bilgilerini_yazdir(self):
        print(self.yaris_motorumu)
        return super().bilgilerini_yazdir()