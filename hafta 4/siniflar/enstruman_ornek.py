"""
Enstruman adlı bir sınıf tanımlayınız.
içerisinde ornek niteliği olarak
ad
çalgı tipi # (vurmalı,üfürmeli,telli)
olsun.
davul, zurna, saz için örnek tanımlayınız.
içerisine parametre alan bir Çal fonksiyon tanımlayınız, 
fonksiyon parametre olarak nota gönderiniz. 
Ör : Saz do çaldı yazabilir.

sonra sazla do, sazla re,  zurna re çaldırın. 
"""

class Enstruman:
    def __init__(self,ad,calgi_tipi):
        self.ad = ad
        self.calgi_tipi = calgi_tipi
    
    def cal(self,nota):
        print(self.ad + " "+ nota+" çaldı")

davul = Enstruman("davul","vurmalı")
zurna = Enstruman("zurna","üflemeli")
saz = Enstruman("saz","telli")

saz.cal("do")
saz.cal("re")
zurna.cal("re")