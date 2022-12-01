import pizzarendelo


def fajta_bekero():
    fajta = input("Milyen típusú pizzát szeretne? sa/go/so ")
    return fajta


def meret_bekero():
    meret = input("Mekkora pizzát szeretne? ki/no/na ")
    return meret


def feltet_bekero():
    feltet = input("Kér extra feltétet? igen/nem ")
    return feltet
