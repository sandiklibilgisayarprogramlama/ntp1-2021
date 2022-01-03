"""parametre olarak bir kelime listesi alan ve 
indisi tek sayı olan elemanların tüm harflerini büyük yazdıran
indisi çift sayı olanların sadece ilk harfini büyük 
yazdıran fonksiyonu yazınız.
"""

kelime_listesi = ["lorem","ipsum","deneme","örnek"]

def soru(kelime_listesi):
    for ind in range(len(kelime_listesi)): # 0,1,2,3
        if ind % 2 == 0:
            print(str(kelime_listesi[ind]).capitalize())
        else:
            print(str(kelime_listesi[ind]).upper())

soru(kelime_listesi)

ss = {"ömer":[40,60],"veysi":[50,30],"fatih":[50,20]}
# yukarıdaki listede final notları
# buna göre bu öğrencilerin geçip geçmediğini ekrana yazdıran
# fonksiyonu yazınız. ort = vize*0.4+final*0.6

def gecme_durumunu_yazdir(not_sozluk):
    for anahtar,deger in not_sozluk.items():
        not_ort = deger[0]*0.4 + deger[1]*0.6
        gecme_durum=""
        if not_ort>=60:
            gecme_durum = "geçti"
        else:
            gecme_durum="kaldı"
        print(anahtar+" : "+gecme_durum)
        print(not_ort)

gecme_durumunu_yazdir(ss)