# bir klasör içindeki ismi en uzun olan dosya ismini 
# yazdırın.

import os

def en_uzun_dosya_ismini_ekrana_yaz():
    dosya_listesi=os.listdir("ornek")
    yazilacak=""
    for d in dosya_listesi:
        if len(d) > len(yazilacak):
            yazilacak=d
    print(yazilacak)

en_uzun_dosya_ismini_ekrana_yaz()