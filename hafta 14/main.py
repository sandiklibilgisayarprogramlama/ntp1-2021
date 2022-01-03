from araba import Araba
from motor import Motor
from filo import Filo
from petrol_ofis import PetrolOfisi
from yakit import Yakit

benzinli = Yakit("Benzin")
tuplu = Yakit("Tüp")

fiat_araba=Araba("Fiat",2021,benzinli,400,4,4,100)
fiat_araba2=Araba("Fiat",2020,tuplu,400,4,4,100)

honda_motor=Motor("Honda",2014,benzinli,100,2,True,3)

pet1=PetrolOfisi(5000,"haftalik")
pet2=PetrolOfisi(10000,"haftalik")

filo=Filo("Sandikli Rent-a-car",[fiat_araba,fiat_araba2,honda_motor],[pet1,pet2])

pet1.yakit_tutari_getir()
pet2.yakit_tutari_getir()
honda_motor.yuz_km_yaktigi_yakit()
fiat_araba.yuz_km_yaktigi_yakit()

filo.motor_sayisi_getir()
filo.araba_sayisini_getir()
filo.tuketilen_toplam_yakit()