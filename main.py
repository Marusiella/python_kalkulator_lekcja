
from typing import Match


def jakas_tan(spliter, inx):
    odp = inx.split(spliter)
    if odp[0] == inx:
        return False
    else:
        return [float(odp[0]), float(odp[1])]


work = []
while True:
    inx = input("Podaj działanie: ")
    dodawanie = jakas_tan("+", inx)
    odejmowanie = jakas_tan("-", inx)
    mnozenie = jakas_tan("*", inx)
    dzielenie = jakas_tan(":", inx)
    if dodawanie != False:
        print("dodawanie")
        print(dodawanie[0]+dodawanie[1])
    if odejmowanie != False:
        print("odejmowanie")
        print(odejmowanie[0]-odejmowanie[1])
    if mnozenie != False:
        print("mnozenie")
        print(mnozenie[0]*mnozenie[1])
    if dzielenie != False:  
        print("dzielenie")
        print(dzielenie[0]/dzielenie[1])

