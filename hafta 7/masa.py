"""
Masa adlı bir sınıf oluşturunuz. Masaya örnek değişkeni 
olarak 
en,boy,yükseklik,renk değerlerini ekleyiniz. 

içine  görevi ekrana bilgileri yazdirmak olan 
bilgilerini_yazdir metodu ekleyiniz.
ekleyiniz.

İki adet masa örneği oluşturunuz. 
ve bilgilerini_yazdir() metodunu çağırınız.
"""

class Masa:
    def __init__(self,en,boy,yukseklik,renk):
        self.en = en
        self.boy = boy
        self.yukseklik = yukseklik
        self.renk = renk
    
    def bilgileri_yazdir(self):
        print(self.en)
        print(self.boy)
        print(self.yukseklik)
        print(self.renk)

# en_boydan_buyukmu 
# büyükse evet
# değilse hayır yazsın:

    def en_boydan_buyukmu(self):
        if self.en > self.boy:
            print("evet")
        else:
            print("hayır")