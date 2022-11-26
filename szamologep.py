def osszeadas():
    # adatbekérés
    szam1 = float(input("Az első szám: "))
    szam2 = float(input("Az második szám: "))
    osszeg = szam1 + szam2
    # kiírás
    print(f"{szam1} + {szam2} = {osszeg}")
    print("-" * 20)


def kivonas():
    # adatbekérés
    szam1 = float(input("Az első szám: "))
    szam2 = float(input("Az második szám: "))
    osszeg = szam1 - szam2
    # kiírás
    print(f"{szam1} - {szam2} = {osszeg}")
    print("-" * 20)


def szamologep():
    # adatbekérés
    #lokális változó
    print("-" * 20)
    szam1 = float(adatbekeres("Adj meg egy számot!"))
    print("-" * 20)
    muvjel = adatbekeres("Add meg a műveleti jelet!")
    print("-" * 20)
    szam2 = float(adatbekeres("Adj meg még egy számot!"))
    print("-" * 20)
    # számolas
    szoveg = ""
    eredmeny = 0
    if muvjel == "+":
        eredmeny = szam1 + szam2
    elif muvjel == "-":
        eredmeny = szam1 - szam2
    elif muvjel == "/":
        eredmeny = szam1 / szam2
    elif muvjel == "*":
        eredmeny = szam1 * szam2
    else:
        szoveg = "nem értelmezhető a művelet"
    kiiras(szam1, szam2, muvjel, eredmeny, szoveg)




def adatbekeres(szoveg):
    print("-" * 20)
    muvjel = (input(szoveg))
    return muvjel   # visszatérési érték


def kiiras(szam1, szam2, muvjel, eredmeny, szoveg):
    # kiírás
    print("-" * 20)
    if szoveg == "":
        print(f"{szam1}{muvjel}{szam2}={eredmeny}")
    else:
        print(szoveg)
    print("-" * 20)