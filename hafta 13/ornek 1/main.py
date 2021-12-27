from myo import MYO
from fakulte import Fakulte
from rektorluk import Rektorluk
from yok import YOK

myo1=MYO("Sandıklı Myo","Saldikli",150,15)
myo2=MYO("Suhut Myo","Suhut",50,5)

fakulte1=Fakulte("Mühendislik Fakültesi",400,"merkez")

rektorluk1=Rektorluk("AKÜ",[myo1,myo2],[fakulte1])

yok = YOK([rektorluk1])

print(yok.rektorlukler[0].myolar[1].ad)