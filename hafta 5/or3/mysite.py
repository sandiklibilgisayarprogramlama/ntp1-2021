class Site:

    def __init__(self,blok_listesi,site_ismi):
        self.blok_listesi = blok_listesi
        self.site_ismi = site_ismi
    
    def aidatini_odemeyenleri_listele(self):
        for blok in self.blok_listesi:
            for daire in blok.daire_listesi:
                if not daire.aidat_odedimi:
                    print(str(daire.daireno) + " nolu daire ücretini ödememiş")
    
    def toplam_aidat_listele(self):
        alinan_aidatlar = 0
        for blok in self.blok_listesi:
            for daire in blok.daire_listesi:
                if daire.aidat_odedimi:
                    alinan_aidatlar = alinan_aidatlar+ daire.aidat_ucreti
        
        print("Gelen Aidat Ücreti")
        print(alinan_aidatlar)
    
    def site_toplam_daire_sayisi(self):
        daire_say=0
        for blok in self.blok_listesi:
            daire_say = daire_say + len(blok.daire_listesi)
        
        print(daire_say)
    
    def bloktaki_daire_sayisini_getir(self,blok):
        print(blok.blok_adi + " daire sayısı : "+str(len(blok.daire_listesi)))
    
    def cesitine_gore_daire_sayisi_getir(self,cesit):
        say =0
        for blok in self.blok_listesi:
            for daire in blok.daire_listesi:
                if daire.dairetip == cesit:
                    say = say+1
        
        print("sitedeki "+cesit+" tipindeki daire sayisi : "+str(say))