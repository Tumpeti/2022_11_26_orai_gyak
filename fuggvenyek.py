szam = 2
def fv1():
    global szam
    szam1 = 3
    print(f"fv1 {szam1}")
    # print(f"fv1 {szam2}")
    print(f"fv1 {szam}") # ezt itt nem tudja még
    szam = 12 # itt határozzuk meg később
    print(f"fv1 {szam}")
    return szam1


def fv2():
    global szam
    szam2 = 4
    szam1 = fv1()
    print(f"fv2 {szam1}")
    print(f"fv1 {szam2}")
    print(f"fv1 {szam}")