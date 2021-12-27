import araba,motor
class Filo:
    def __init__(self,firma_adi,araclar,petrol_ofisleri) -> None:
        self.firma_adi = firma_adi
        self.araclar = araclar
        self.petrol_ofisleri = petrol_ofisleri
    
    def motor_sayisi_getir(self):
        sayi = 0
        for arac in self.araclar:
            if type(arac) == motor.Motor:
                sayi=sayi+1
        print(self.firma_adi," içindeki motor sayısı: ",sayi)

    def araba_sayisini_getir(self):
        sayi = 0
        for arac in self.araclar:
            if type(arac) == araba.Araba:
                sayi=sayi+1
        print(self.firma_adi," içindeki araba sayısı: ",sayi)
    
    def tuketilen_toplam_yakit(self):
        toplam=0
        for pet in self.petrol_ofisleri:
            toplam = toplam + pet.yakit_tutar
        
        print(self.firma_adi,
        " kiralanan araçların toplam yakit tutarı(haftalik): ",toplam)