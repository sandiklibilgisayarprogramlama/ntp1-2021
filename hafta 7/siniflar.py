class Monitor:

    def __init__(self,inc,renk):
        self.inc = inc
        self.renk = renk

class Klavye:

    def __init__(self,renk,tur):
        self.renk = renk
        self.tur = tur

class Fare:

    def __init__(self,optikmi,renk):
        self.optikmi = optikmi
        self.renk = renk

class Kasa:

    def __init__(self,en,boy):
        self.en = en
        self.boy = boy

class Kamera:
    def __init__(self,mpixel,renk):
        self.mpixel = mpixel
        self.renk = renk

class Bilgisayar:
    def __init__(self,kasa,fare,monitor,klavye,kamera):
        self.kasa = kasa
        self.fare = fare
        self.monitor = monitor
        self.klavye = klavye
        self.kamera = kamera

    def monitor_inc_yazdir(self):
        print(self.monitor.inc)
    
    def klavye_tur_yazdir(self):
        print(self.klavye.tur)

    # klavye ve farenin renkleri aynı ise
    # uyumlu değilse uyumsuz yazdıralım.

    def renk_control(self):
        if self.klavye.renk == self.fare.renk:
            print("renkler aynı")
        else:
            print("renkler aynı değil")
    
