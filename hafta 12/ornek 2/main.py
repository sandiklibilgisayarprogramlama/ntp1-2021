"""
Surucu isimli bir sınıf tanımlayınız. İçerisine 
ad,soyad,beceri_puan ornek değişkenlerini ekleyiniz.

Arac isimli bir sınıf tanımlayınız. 
İçerisine marka,model,max_hız,teker_sayisi,surucu(Surucu tipindee)
 ornek değişkenlerini ekleyiniz. 

Araç sınıfına km ve beceri_puanı parametre olarak alan ve ekrana 
gidilecek süreyi yazan fonksiyonu tanımlayınız.
sure=gidilecek_km /(max_hız*beceri_puan)

Arac sınıfından miras alan Motor ve Araba sınıflarını oluşturunuz.

Araba araçtan farklı olarak renk ve motorda araçtan farklı olarak
elektriklimi parametrelerini alsın.

Main sınıfında örnekleri oluşturunuz.
"""

from araba import Araba
from motor import Motor
from surucu import Surucu

surucu1 = Surucu("Veysi","uzun",0.8)
surucu2 = Surucu("Gökay","kısa",0.5)

motor1=Motor("Uğur",2020,120,2,surucu2,False)
araba1 = Araba("Şahin",2003,100,4,surucu1,"beyaz")

araba1.gidilecek_sure_hesapla(200)
motor1.gidilecek_sure_hesapla(200)