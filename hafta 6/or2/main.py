
from cocuk import Cocuk
from veli import Veli


cocuk1=Cocuk("ahmet","uzun",12)
cocuk2 = Cocuk("ayşe","kısa",10)
cocuk3 = Cocuk("hüseyin","kuş",34)
veli=Veli("Ali","uzun",[cocuk1,cocuk2,cocuk3])

# velinin ilk çocuğunun bilgisi
#veli.cocuklar[0].bilgileri_yazdir()
veli.buyuk_olani_ekrana_yazdir()