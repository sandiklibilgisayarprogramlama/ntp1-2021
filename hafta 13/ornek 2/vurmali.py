from enstruman import Enstruman
class Vurmali(Enstruman):
    def __init__(self, enstruman_adi, malzeme,elektronik_mi):
        super().__init__(enstruman_adi, malzeme)
        self.elektronik_mi = elektronik_mi
    
    def cal(self):
        #return super().cal()
        if self.elektronik_mi:
            print("Elektronik ",self.enstruman_ad," çaldı")
        else:
            print("Düz ", self.enstruman_ad," Çaldı.")