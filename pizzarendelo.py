"""
Pizzarendelő alkalmazás

A felhasználótól addig kérje be a rendeléseket, amíg a @ jelet nem ütjük le!
Minden rendelés során a  program kérje be, hogy:
1. sajtos, gombás, vagy sonkás pizzát kér-e?
2. mekkora a pizza mérete:
        kicsi   -  ára az ár 90%-a
        normál  - ára az ár 100%-a
        nagy    – ára az ár 110%-a

3.  kér e feltétet.

Alapárak:
A plusz feltét 50 Ft.
Normál sajtos pizza alapára 1000 Ft
Normál gombás pizza alapára 1100 Ft
Normál sonkás pizza alapára 1200 Ft


Tároljuk a felvett rendeléseket megfelelő listákba!  tipus, meret, feltet
Végezzük el minden rendelés esetében az ár kiszámítását is! esetleg ezt is tárolhatjuk egy listában! ar

A rendelések felvétele után készítsünk statisztikát!
1. Melyik típusú (név alapján)  pizzából hány darab fogyott?
2. Melyik pizzából fogyott a legtöbb?
3. Mekkora volt a bevétel?
4. Hányszor kértek extra feltétet?
5. A kicsi, nagy , vagy a közepes pizzából rendeltek-e többet?
6. … ami még eszetekbe jut.
"""

"""
pizzarendelo():

1 rendelés: 
be: sajtos
be: normál
be: nem kér feltétet
be: kér-e még? -> rendelés itt végződik

sok rendelés
adatszerkezet: 3db lista:
tipus=[]
meret=[]
feltet=[]
ar=[] -> indexek alapján árszámoló függvénynek átadjuk az értékeket
a listáknak globálisnak kell lennie

függvények:

rendelesfelvetel():
a listákat feltöltjük adatokkal


arszamitas():


rendeleskiiras():


statisztika1(): 2, 3 4 stb....


ne legyenek kódismétlések, azokat ki kell szervezni függvénybe
"""

pizza_fajtak = []
pizza_meretek = []
pizza_feltetek = []
pizza_arak = []
i = 0
ar = 0
import pizza_fuggvenyek
while True:
    rendeles = input("Kíván pizzarendelést leadni? igen/nem ")
    if rendeles == "nem":
        break
    pizza_fajtak.append(pizza_fuggvenyek.fajta_bekero())
    if pizza_fajtak[i] == "sa":
        ar = 1000
    elif pizza_fajtak[i] == "go":
        ar = 1100
    elif pizza_fajtak[i] == "so":
        ar = 1200
    pizza_meretek.append(pizza_fuggvenyek.meret_bekero())
    if pizza_meretek[i] == "ki":
        ar = ar * 0.9
    elif pizza_meretek[i] == "no":
        ar = ar * 1
    elif pizza_meretek[i] == "na":
        ar = ar * 1.1
    pizza_feltetek.append(pizza_fuggvenyek.feltet_bekero())
    if pizza_feltetek[i] == "igen":
        ar += 50
    pizza_arak.append(ar)
    i += 1
print(pizza_arak)
print(pizza_fajtak)
print(pizza_meretek)
print(pizza_feltetek)


