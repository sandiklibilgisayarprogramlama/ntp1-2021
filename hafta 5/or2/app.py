from kisi import Kisi

kisi1 = Kisi("ahmEt","uzun ",12,"E")
kisi2 = Kisi("Leyla"," uZun",23,"K")

kisi1.bilgilerini_yazdir()
kisi2.bilgilerini_yazdir()
print(kisi1.dogum_yili_getir())
print(kisi2.dogum_yili_getir())

print(kisi1.ad_soyad_getir())
print(kisi2.ad_soyad_getir())