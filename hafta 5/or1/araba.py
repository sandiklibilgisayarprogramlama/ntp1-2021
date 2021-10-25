class Araba:

    def __init__(self,marka,model,silindir,renk):
        self.marka = marka
        self.model = model
        self.silindir = silindir
        self.renk = renk
    
    def ozellikleri_yazdir(self):
        print("özellikler")
        print("Araç rengi: "+self.renk)
        print("araç markası: "+self.marka)
        print("Araç modeli:"+ str(self.model))
        print("Araç silindir:"+self.silindir)
