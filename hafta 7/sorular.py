#Parametre olarak bir kelime listesi alan ve bu liste içindeki tüm
#elemanları büyük harfe çeviren ve bu listeyi ekrana yazan fonksiyonu tanımla
#yınız.

"""
ahmet
list("ahmet") => 'a','h','m','e','t'
"""

liste = ["ahmet","mehmet","ayşe"]

def buyuk_harfe_cevir(kelime_liste):
    for eleman in kelime_liste:
        i_liste = []
        for k,e in enumerate(eleman):
            if e == "i":
                i_liste.append(k)
        
        buyuk_eleman=eleman.upper()
        #buyuk_eleman = buyuk_eleman.replace("I","İ")
        liste_eleman=list(buyuk_eleman)
        for i in i_liste:
             liste_eleman[i]= 'İ'
        print("".join(liste_eleman))

def buyuk_harfe_cevir_replace(kelime_liste):
    for eleman in kelime_liste:        
        buyuk_eleman=eleman.upper()
        buyuk_eleman = buyuk_eleman.replace("I","İ")
        print(buyuk_eleman)

buyuk_harfe_cevir(liste)
# INCI
buyuk_harfe_cevir(["inci","Cumhur","Naci"])


"""
{
    "anahtar":deger
}
"""
def sozlukleri_birleştir(sozluk1,sozluk2):
    for a,d in sozluk2.items():
        sozluk1[a] = d
    
    return sozluk1
