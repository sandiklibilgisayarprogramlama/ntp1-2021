from enstruman import Enstruman
class Telli(Enstruman):
    def __init__(self, enstruman_adi, malzeme,tel_sayisi):
        super().__init__(enstruman_adi, malzeme)
        self.tel_sayisi = tel_sayisi