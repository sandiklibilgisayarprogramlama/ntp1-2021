# -*- coding: UTF-8 -*-

# dışarıdaki bir python sayfasının içindeki fonksiyon 3
# ve değişkenleri dahil etmek için 
# import dosya_ismi kullanılır.
# 1. çağırma yolu
"""
import fonksiyon_tekrar

fonksiyon_tekrar.ekrana_merhaba_yaz()

print(fonksiyon_tekrar.OKUL_ISMI)
"""
# 2. çağırma yolu
# as den sonra kısaltma
"""
import fonksiyon_tekrar as ft

ft.liste_icindeki_sayilari_topla()
ft.OKUL_ISMI
"""
# 3. çağırma yolu
"""
from fonksiyon_tekrar import OKUL_ISMI,liste_icindeki_sayilari_topla

print(OKUL_ISMI)
"""
# 4. yol
from fonksiyon_tekrar import *
print(OKUL_ISMI)
liste_icindeki_sayilari_topla([12,3])

