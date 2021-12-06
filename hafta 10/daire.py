"""
Bina 
katsayisi = 4
dairesayisi = 16

Daire adında bir sınıf oluşturunuz. içine 
bulundugukat, kapino,oturankisi örnek değişkenlerini oluşturunuz.
Ayrıca içine kiracimi sınıf değişkenini oluşturunuz.
Daire içine malik_durumunu_yazdir classmethodunu yazınız.

Bina isimli bir sınıf oluşturunuz
bu sınıf içine katsayisi static metodunu ve dairesayisi static
metodunu oluşturunuz.
Bina içine daireler örnek değişkenini oluşturup yukarıdaki Daire
sınıfından ürettiğiniz örnekleri bu sınıfa parametre veriniz.

"""

class Daire:
    kiracimi=False

    def __init__(self,bulundugukat,kapino,oturankisi):
        self.bulundugukat = bulundugukat
        self.kapino = kapino
        self.oturankisi=oturankisi
    
    @classmethod
    def malik_durumunu_yazdir(cls):
        print(cls.kiracimi)
