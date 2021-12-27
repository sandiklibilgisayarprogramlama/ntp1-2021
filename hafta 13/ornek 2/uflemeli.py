from enstruman import Enstruman

class Uflemeli(Enstruman):
    def __init__(self, enstruman_adi, malzeme,nota_say):
        super().__init__(enstruman_adi, malzeme)
        self.nota_say = nota_say
    
    def cal(self):
        #return super().cal()
        print("Nota sayısı ",self.nota_say," olan ",
        self.enstruman_ad," adlı çaldı çaldı.")