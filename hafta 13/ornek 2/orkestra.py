class Orkestra:
    def __init__(self,enstrumanlar):
        self.enstrumanlar = enstrumanlar
    
    def hepsiniCal(self):
        for enstruman in self.enstrumanlar:
            enstruman.cal()