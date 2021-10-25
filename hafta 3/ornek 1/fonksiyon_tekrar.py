# -*- coding: UTF-8 -*-

'''
İçinde farklı tiplerde veri bulunan bir listeniz olsun
liste = [12,3,4,"ali",["veli",12],["ayşe",3],2,"selim"]
1. bu liste içindeki sayıların toplamını ekrana yazdıran
fonksiyonu yazınız.
2. bu liste içindeki str ifadelerini araya boşluk koyarak
ekrana yazan fonksiyonu yazınız.
3. bu liste içindeki liste sayısını ekrana yazan fonksiyonu yazınız.
(Yukarıda tanımlı fonksiyonlar parametre olarak hangi liste gönderilirse
gönderilsin sonuçları doğru göstermelidir!)'''

liste = [12,3,4,"ali",["veli",12],["ayşe",3],2,"selim"]
def liste_icindeki_sayilari_topla(liste):
    toplam = 0
    for eleman in liste:
        if  "int" in str(type(eleman)):
            toplam = eleman+toplam
        elif "list" in str(type(eleman)):
            for k in eleman:
                if "int" in str(type(k)):
                    toplam = toplam+k

    print(toplam)

#liste_icindeki_sayilari_topla(liste)

def ekrana_merhaba_yaz():
    print("merhaba")

OKUL_ISMI = "Sandıklı MYO"
# girilen bir sayının ikili sayı sistemine çevrilmesini sağlayan fonksiyonu
# yazınız.
# 9 8 4 2 
# 1 
# "00001001"
#print(bin(9))