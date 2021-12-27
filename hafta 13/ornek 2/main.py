from telli import Telli
from uflemeli import Uflemeli
from vurmali import Vurmali
from orkestra import Orkestra

saz=Telli("Saz","ceviz",7)
flut=Uflemeli("Flüt","plastik",10)
davul=Vurmali("davul","odun",False)
ud=Telli("Ud","meşe",6)

orkestra1=Orkestra([saz,flut,davul,ud])
orkestra1.hepsiniCal()