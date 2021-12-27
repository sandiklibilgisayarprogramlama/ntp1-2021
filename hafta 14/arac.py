class Arac:
    def __init__(self,marka,model,yakit_tipi,gunluk_tutar,km_basina_yakilan):
        self.marka=marka
        self.model = model
        self.yakit_tipi = yakit_tipi
        self.gunluk_tutar = gunluk_tutar
        self.km_basina_yakilan = km_basina_yakilan
    
    def yuz_km_yaktigi_yakit(self):
        print(100 * self.km_basina_yakilan," lt")