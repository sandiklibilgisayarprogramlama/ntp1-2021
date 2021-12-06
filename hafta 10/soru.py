from daire import Daire
from bina import Bina

daire1 = Daire(1,3,"Ahmet")
daire2 = Daire(2,6,"Veli")

bina = Bina([daire1,daire2])

print(Bina.daire_sayisi_getir())
print(Bina.kat_sayisi_getir())
bina.oturanlari_yazdir()