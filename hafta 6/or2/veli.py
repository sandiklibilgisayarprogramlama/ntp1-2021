from typing import List

from cocuk import Cocuk


class Veli:

    def __init__(self,ad,soyad ,cocuklar ):
        self.ad = ad
        self.soyad = soyad
        self.cocuklar = cocuklar
    
    def buyuk_olani_ekrana_yazdir(self):
        buyuk_cocuk = None
        for k in self.cocuklar:
            if buyuk_cocuk == None:
                buyuk_cocuk = k
            
            if buyuk_cocuk.yas < k.yas:
                buyuk_cocuk = k
        
        buyuk_cocuk.bilgileri_yazdir()