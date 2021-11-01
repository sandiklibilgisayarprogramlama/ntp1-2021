class Daire:

    def __init__(self,dairetip,aidat_odedimi,daireno):
        if dairetip == "kapici":
            self.aidat_ucreti = 0
        elif dairetip == "3+1":
            self.aidat_ucreti = 100
        else:
            self.aidat_ucreti = 120
        
        self.dairetip = dairetip
        self.aidat_odedimi = aidat_odedimi
        self.daireno = daireno