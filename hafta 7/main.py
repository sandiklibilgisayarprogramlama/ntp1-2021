from masa import Masa

masa1 = Masa(130,170,70,"mavi")
masa2 = Masa(120,80,70,"mavi")

masa1.bilgileri_yazdir()
masa2.bilgileri_yazdir()

# eni büyük olanı yazdıralım.

if masa1.en > masa2.en:
    print("masa1 daha büyük")
else:
    print("masa 2 daha büyük")

# rengi mavi olanı ekrana yazdıralım.

if masa1.renk == "mavi":
    print("masa 1 mavi")

if masa2.renk=="mavi":
    print("masa 2 mavi")

masa1.en_boydan_buyukmu()

