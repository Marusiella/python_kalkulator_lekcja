
from typing import Match


def jakas_tan(spliter, inx):
    odp = inx.split(spliter)
    if odp[0] == inx:
        return False
    else:
        return [float(odp[0]), float(odp[1])]


while True:
    inx = input("Podaj działanie: ")
    dodawanie = jakas_tan("+", inx)
    odejmowanie = jakas_tan("-", inx)
    mnozenie = jakas_tan("*", inx)
    dzielenie_dwu = jakas_tan(":", inx)
    dzielenie_ukos = jakas_tan("/", inx)
    if dodawanie != False:
        print("dodawanie")
        print(dodawanie[0]+dodawanie[1])
    if odejmowanie != False:
        print("odejmowanie")
        print(odejmowanie[0]-odejmowanie[1])
    if mnozenie != False:
        print("mnozenie")
        print(mnozenie[0]*mnozenie[1])
    if dzielenie_dwu != False:
        print("Dzielenie poprzez użycie :")
        print(dzielenie_dwu[0]/dzielenie_dwu[1])
    if dzielenie_ukos != False:
        print("Dzielenie poprzez użycie /")
        print(dzielenie_ukos[0]/dzielenie_ukos[1])
