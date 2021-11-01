from daire import Daire
from blok import Blok
from mysite import Site

d1 = Daire("3+1",False,1)
d2 = Daire("4+1",True,2) # 120
d3 = Daire("3+1",False,3)
d4 = Daire("4+1",False,4)
d5 = Daire("3+1",True,5) # 100
d6 = Daire("3+1",True,6) # 100
d7 = Daire("kapici",True,0)

b1=Blok([d1,d2,d3,d7],"A Blok")
b2=Blok([d4,d5,d6],"B Blok")

s1 = Site([b1,b2],"Gülevler Sitesi")

#s1.aidatini_odemeyenleri_listele()

s1.toplam_aidat_listele()

#s1.site_toplam_daire_sayisi()

#s1.bloktaki_daire_sayisini_getir(b1)

s1.cesitine_gore_daire_sayisi_getir("kapici")