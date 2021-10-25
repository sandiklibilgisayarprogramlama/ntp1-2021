from orneksinif import Ogrenci,Ogretmen

ogrenci1 = Ogrenci()
ogrenci1.adi="Veli"
ogrenci1.soyadi="uzun"
ogrenci1.tc_no="34433434322"
ogrenci1.telefon="5069322233"
ogrenci1.yas=12

ogrenci2 = Ogrenci()
ogrenci2.adi="ahmet"
ogrenci2.soyadi="kısa"
ogrenci2.tc_no="423424234344"
ogrenci2.telefon="543121312312"
ogrenci2.yas=17

print(ogrenci1.adi)
print(ogrenci2.tc_no)

# içinde ad,soyad,tcno,adres,anadal
#bilgilerinin yer aldığı öğretmen sınıfı
#oluşturunuz. Bu sınıftan iki 
#örnek üretiniz.
Ogretmen.ad="mehmet"

ogretmen1 = Ogretmen()
ogretmen1.ad="asd"
ogretmen1.soyad="da"
ogretmen1.tcno="423525365454"
ogretmen1.adres="afyon"
ogretmen1.anadal="matematik"

ogretmen2 = Ogretmen()
ogretmen2.soyad="da"
ogretmen2.tcno="423525365454"
ogretmen2.adres="afyon"
ogretmen2.anadal="matematik"

print(ogretmen1.ad)
print(ogretmen2.ad)