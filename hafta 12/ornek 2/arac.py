class Arac:
    def __init__(self,marka,model,max_hiz,teker_sayisi,surucu):
        self.marka = marka
        self.model = model
        self.max_hiz=max_hiz
        self.teker_sayisi = teker_sayisi
        self.surucu = surucu
    
    def gidilecek_sure_hesapla(self,km):
        sure= km / \
        (self.max_hiz*self.surucu.beceri_puan)
        print(sure)
