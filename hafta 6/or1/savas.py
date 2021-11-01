class Savas:

    def __init__(self,ulke1,ulke2):
        self.ulke1 = ulke1
        self.ulke2 = ulke2
    
    def savastir(self):
        
        while True:
            for k in range(len(self.ulke1.birlik_listesi)):
                u1_insan=self.ulke1.birlik_listesi[k]
                u2_insan=self.ulke2.birlik_listesi[k]

                if u1_insan.grup == "okcu":
                    u2_insan.can = u2_insan.can-u1_insan.vg_okcu
                elif u1_insan.grup == "asker":
                    u2_insan.can = u2_insan.can-u1_insan.vg_asker
                elif u1_insan.grup == "sovalye":
                    u2_insan.can = u2_insan.can-u1_insan.vg_sovalye
                
                if u2_insan.grup == "okcu":
                    u1_insan.can = u1_insan.can-u2_insan.vg_okcu
                elif u2_insan.grup == "asker":
                    u1_insan.can = u1_insan.can-u2_insan.vg_asker
                elif u2_insan.grup == "sovalye":
                    u1_insan.can = u1_insan.can-u2_insan.vg_sovalye
            
            u1_can = 0
            u2_can = 0

            for u in self.ulke1.birlik_listesi:
                u1_can = u1_can + u.can

            for u in self.ulke2.birlik_listesi:
                u2_can = u2_can + u.can

            print("ülke 1 can : " + str(u1_can))
            print("ülke 2 can : " + str(u2_can))
            if u1_can <= 0:
                print("savaşı ",self.ulke2.ulke_adi+" kazandı")
                break

            if u2_can <= 0:
                print("savaşı ",self.ulke1.ulke_adi+" kazandı")
                break

        toplam_asker_sayisi = 8    
        for k in range(len(self.ulke1.birlik_listesi)):
            u1_insan=self.ulke1.birlik_listesi[k]
            u2_insan=self.ulke2.birlik_listesi[k]

            if u1_insan.can<= 0:
                toplam_asker_sayisi=toplam_asker_sayisi-1
            
            if u2_insan.can<= 0:
                toplam_asker_sayisi=toplam_asker_sayisi-1
        
        print("kalan asker sayı :", str(toplam_asker_sayisi))
            