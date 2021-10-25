# -*- coding: UTF-8 -*-
"""
print("merhaba","dünya")

print('Fırat', 'Özgül','1980', 'Adana',end="\n",sep="=")
sayi1= int(input("sayı 1 giriniz"))
sayi2 = int(input("sayi 2 giriniz"))

def topla(s1,s2):
    print(s1+s2)

def bol(s1,s2):
    print(s1/s2)

def fark(s1,s2):
    print(s1-s2)

def carp(s1,s2):
    print(s1*s2)

topla(sayi1,sayi2)
carp(13,10)
fark(12,9)
bol(14,2)
bol(15,5)
carp(12,3)
"""
# parametre olarak sayi listesi alan ve bu listenin
# elemanlarının toplamını ekrana yazan fonksiyonu
# yazınız.
"""
Ödev 
İçinde farklı tiplerde veri bulunan bir listeniz olsun
liste = [12,3,4,"ali",["veli",12],["ayşe",3],2,"selim"]
1. bu liste içindeki sayıların toplamını ekrana yazdıran
fonksiyonu yazınız.
2. bu liste içindeki str ifadelerini araya boşluk koyarak
ekrana yazan fonksiyonu yazınız.
3. bu liste içindeki liste sayısını ekrana yazan fonksiyonu yazınız.
(Yukarıda tanımlı fonksiyonlar parametre olarak hangi liste gönderilirse
gönderilsin sonuçları doğru göstermelidir!)
"""
"""
def listenin_elemanlarini_topla(bir_liste):
    toplam=0
    for i in bir_liste:
        toplam=toplam+i
    print("toplam : "+str(toplam))

listenin_elemanlarini_topla([12,32,45,67,23,78])


def gonderilen_verileri_goster(**gonderilenler):
    for anahtar,deger in gonderilenler.items():
        print("kişinin "+anahtar," :",deger)

kisi={"ad":"sülayman","soyad":"uzun","yas":34}
gonderilen_verileri_goster(**kisi)
"""

def ogrenci_bilgi_yazdir(ad,soyad,tcno,ulke="TÜRKİYE",evlimi=False):
    print(ad)
    print(soyad)
    print(tcno)
    print(ulke)
    print(evlimi)


ogrenci_bilgi_yazdir("ahmet","uzun","43423425455")
ogrenci_bilgi_yazdir("veli","kısa","434324234234",evlimi=True)
ogrenci_bilgi_yazdir("michael","scoldfield","d3423425252",ulke="US")

# Global ve local değişkenler
#adiniz global
#deger ve yazılacak local
"""
adiniz="veli"

def ekrana_yaz(yazilacak):
    deger="ekrana yazılanacak fonksiyonu ile yazildi"
    print(yazilacak)
    print(deger)
    deger
    print(adiniz)
"""

# x^2+34y-19 problemini hesaplayan fonksiyonu yazınız.
# return ile fonksiyondan geriye dönüş alınır.
def hesapla(x,y):
    sonuc = x**2+34*y-19
    return sonuc

sonuc = hesapla(1,2)

sonuc = sonuc+1
print(sonuc)


print(round(12.6))

print(int(12.999999999999))

#print(help(int))

# girilen bir sayının ikili sayı sistemine çevrilmesini sağlayan fonksiyonu
# yazınız.

import math

print(math.floor(12.2)) # alta yuvarlar
print(math.ceil(12.2)) # üste yuvarlar

# parametre olarak girilen ad soyadı çıktı formatı olarak adın sadece ilk
# harfi büyük soyadın ise hepsi büyük hale çeviren fonksiyonu yazınız.
# ahmet uzun -> Ahmet UZUN

