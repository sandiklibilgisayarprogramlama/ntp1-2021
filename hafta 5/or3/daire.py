class Daire:

    def __init__(self,dairetip,aidat_odedimi,daireno):
        if dairetip == "3+1":
            self.aidat_ucreti = 100
        else:
            self.aidat_ucreti = 120
        
        self.dairetip = dairetip
        self.aidat_odedimi = aidat_odedimi
        self.daireno = daireno