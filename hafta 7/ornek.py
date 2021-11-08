from siniflar import *

ornek1 = Kasa(40,50)
ornek2 = Klavye("beyaz","Q")
ornek3 = Monitor(21,"siyah")
ornek4 = Fare(True,"beyaz")
ornek6 = Kamera(48,"yeşil")

ornek5 = Bilgisayar(ornek1,ornek4,ornek3,ornek2,ornek6)

ornek5.monitor_inc_yazdir()
ornek5.klavye_tur_yazdir()

ornek5.renk_control()