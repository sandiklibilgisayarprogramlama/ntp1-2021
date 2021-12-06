from calgitip import CalgiTip
from davul import Davul
from zurna import Zurna
from flut import Flut

vurmalı = CalgiTip(0,"Vurmalı")
uflemeli = CalgiTip(1,"Üflemeli")

davul1=Davul("Davul","Do",vurmalı)
zurna1=Zurna("Zurna","Mi",uflemeli)

davul1.Cal()
zurna1.Cal()