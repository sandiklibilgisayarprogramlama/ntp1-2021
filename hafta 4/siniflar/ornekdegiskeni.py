class Araba:
    #sinif niteliği
    #ad=""
    # siniftan örnek oluşturulurken çalıştırılacak ilk metod
    def __init__(self,marka,model,renk):
        print("init çalıştı")
        # ornek niteliklerimiz
        self.marka = marka
        self.model = model
        self.renk = renk
    
    def bilgileri_yazdir(self):
        print(self.marka)
        print(self.model)
        print(self.renk)
    
    def yas_getir(self):
        return 2021-int(self.model)

ornek1 = Araba("mercedes","2018","beyaz")
ornek1.bilgileri_yazdir()
print("yaş bilgisi")
print(ornek1.yas_getir())

#print(dir(Araba))
ornek2 = Araba("ford",2019,"beyaz")
print(ornek2.marka)
print(ornek2.model)
print(ornek2.renk)

# hata verir, parametreler eksik
#ornek3 = Araba()