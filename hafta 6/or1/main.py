from insan import Insan
from savas import Savas
from ulke import Ulke

sovalye1 = Insan("şovalye 1",2,6,3,"sovalye")
sovalye2 = Insan("şovalye 2",2,5,1,"sovalye")

okcu1 = Insan("okcu 1",4,2,5,"okcu")
okcu2 = Insan("okcu 2",8,2,3,"okcu")
okcu3 = Insan("okcu 3",4,2,3,"okcu")

sovalye3 = Insan("şovalye 3",5,6,3,"sovalye")
sovalye4 = Insan("şovalye 4",9,6,3,"sovalye")

asker1 = Insan("asker 1",3,4,2,"asker")

ingiltere=Ulke("ingiltere",[sovalye4,okcu2,sovalye3,asker1])

almanya=Ulke("almanya",[okcu3,sovalye1,sovalye2,okcu1])

savas = Savas(almanya,ingiltere)
savas.savastir()