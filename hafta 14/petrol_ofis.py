class PetrolOfisi:
    def __init__(self,yakit_tutar,yakit_odeme):
        self.yakit_tutar = yakit_tutar
        self.yakit_odeme = yakit_odeme

    def yakit_tutari_getir(self):
        print(self.yakit_tutar," ₺")