class Araba:
    # static değişken
    marka=10
    teker=4

    def __init__(self,model):
        self.model = model
        # örnek değişkeni
    
    @classmethod
    def modeli_ekrana_yazdir(cls,birset):
        print(birset)

    @staticmethod
    def merhaba_yaz():
        print("merhaba")
    
"""
@classmethod
@staticmethod
"""

Araba.modeli_ekrana_yazdir(10)
Araba.merhaba_yaz()