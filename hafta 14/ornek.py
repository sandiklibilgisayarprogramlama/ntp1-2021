class Sofor:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
    
class Araba:
    def __init__(self,marka,model,surucu):
        self.marka = marka
        self.model = model
        self.surucu = surucu


# main
sofor=Sofor("ahmet","uzun")
araba=Araba("mercedes",2021,sofor)