class Arac:
    def __init__(self,renk,teker_sayisi,motor_gucu,koltuk_sayisi):
        self.renk = renk
        self.teker_sayisi = teker_sayisi
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
    
    def bilgilerini_yazdir(self):
        print(self.renk)
        print(self.teker_sayisi)
        print(self.motor_gucu)
        print(self.koltuk_sayisi)
