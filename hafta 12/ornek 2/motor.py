from arac import Arac
class Motor(Arac):
    def __init__(self, marka, model, max_hiz, teker_sayisi, surucu,elektrikli_mi):
        super().__init__(marka, model, max_hiz, teker_sayisi, surucu)
        self.elektrikli_mi = elektrikli_mi