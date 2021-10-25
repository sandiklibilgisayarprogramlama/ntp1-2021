import os

# baş harfe göre klasör içinde arama yapan fonksiyon
dosya_listesi = os.listdir("ornek")
print(dosya_listesi)

def bas_harfe_gore_arama(bas_harf):
    for d in dosya_listesi:
        if d[0] == bas_harf:
            print(d)

bas_harfe_gore_arama("n")
