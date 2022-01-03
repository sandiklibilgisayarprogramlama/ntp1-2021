class Musteri:
    def __init__(self,ad,adres):
        self.ad = ad
        self.adres = adres
    
    def kredi_hesap(self):
        pass

class KurumsalMusteri(Musteri):
    def __init__(self, ad, adres,baglanti,kredioran,kredilimit):
        super().__init__(ad, adres)
        self.baglanti = baglanti
        self.kredioran = kredioran
        self.kredilimit = kredilimit
    
    def hatirlat(self):
        pass
    
    def faturalandir(self):
        pass

class BireyselMusteri(Musteri):
    def __init__(self, ad, adres,kkno):
        super().__init__(ad, adres)
        self.kkno = kkno

class Siparis:
    def __init__(self,tarih,hazirmi,adet,fiyat,musteri):
        self.tarih = tarih
        self.hazirmi=hazirmi
        self.adet = adet
        self.fiyat = fiyat
        self.musteri = musteri

    def tabloya_dok(self):
        print(self.musteri.ad+"-"+str(self.fiyat))

"""
ahmet adlı bireysel musteri 10000 lira tutarında 20 adet
harddisk alıyor. ekrana bu bilgileri yazdırın.
"""        

bm1 = BireyselMusteri("ahmet","istanbul","32141231233213")

siparis = Siparis("02.01.2022",True,20,10000,bm1)
siparis.tabloya_dok()

