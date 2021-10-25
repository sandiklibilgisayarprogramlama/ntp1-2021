"""Kisi sınıfı oluşturunuz ve kişide olabilecek özellikleri yazınız.
 (Yaş, kilo,boy,ad,soyad)
"""

class Kisi:

# "sÜleymaN" -> süleyman -> Süleyman
    def __init__(self,ad,soyad,yas,cinsiyet):
        self.ad = ad.lower().capitalize().strip()
        self.soyad = soyad.upper().strip()
        self.yas = yas
        self.cinsiyet = cinsiyet
    
    def bilgilerini_yazdir(self):
        print("ad : "+str(self.ad))
        print("soyad : "+self.soyad)
        print("cinsiyet : "+self.cinsiyet)
        print("yas : "+str(self.yas))
        print("------------------------")

    def dogum_yili_getir(self):
        return 2021 - self.yas
    
    def ad_soyad_getir(self):
        return self.ad +" "+ self.soyad