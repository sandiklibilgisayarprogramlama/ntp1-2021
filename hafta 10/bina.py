class Bina:
    @staticmethod
    def kat_sayisi_getir():
        return 4
    
    @staticmethod
    def daire_sayisi_getir():
        return 16
    
    def __init__(self,daireler):
        self.daireler = daireler

    def oturanlari_yazdir(self):
        for daire in self.daireler:
            print(daire.oturankisi)