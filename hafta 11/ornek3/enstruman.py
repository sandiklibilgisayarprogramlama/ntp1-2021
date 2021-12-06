class Enstruman:
    def __init__(self,ad,nota,calgi_tipi):
        self.ad = ad
        self.nota = nota
        self.calgi_tipi = calgi_tipi

    def Cal(self):
        print("Çalgı : "+self.ad)
        print("Çalgı Tipi : "+self.calgi_tipi.tipadi)
        print("Nota : "+self.nota)