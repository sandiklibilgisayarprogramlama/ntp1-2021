from arac import Arac
class Araba(Arac):
    def __init__(self, marka, model, max_hiz, teker_sayisi, surucu,renk):
        super().__init__(marka, model, max_hiz, teker_sayisi, surucu)
        self.renk = renk