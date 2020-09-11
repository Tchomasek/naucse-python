from random import randrange

def vyhodnot(pole):
    "Vyhodnotí stav pole."
    if 'xxx' in pole:
        return("x")
    elif 'ooo' in pole:
        return("o")
    elif '-' not in pole:
        return("!")
    else:
        return '-'

def tah(pole, pozice, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici."
    return pole[:pozice] + symbol + pole[pozice + 1:]

def tah_hrace(herni_pole):
    "Ptá se hráče na kterou pozici chce hrát a vrací herní pole se zaznamenaným tahem"
    while True:
        try:
            cislo_pozice = int(input("Na kterou pozici chceš hrát? "))
        except ValueError:
            print("to není číslo")
        else:
            if cislo_pozice >= 0 and cislo_pozice < len(herni_pole) and herni_pole[cislo_pozice] == "-":
                return tah(herni_pole, cislo_pozice, "x")
            else:
                print("Špatná pozice, zkus to znovu. ")


def tah_pocitace(herni_pole):
    "Vrátí herní pole se zaznamenaným tahem počítače. "
    while True:
        cislo_pozice = randrange(len(herni_pole))
        if herni_pole[cislo_pozice] == "-":
            return tah(herni_pole, cislo_pozice, "o")

def piskvorky1d():
    "Vygeneruje prázdné pole a střídá tah hráče a počítače. "
    pole = "-" * 20
    while True:
        print(pole)
        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != '-':
            break
        pole = tah_pocitace(pole)
        if vyhodnot(pole) != '-':
            break

    print(pole)
    if vyhodnot(pole) == '!':
        print('Remíza!')
    elif vyhodnot(pole) == 'x':
        print('Vyhrála jsi!')
    elif vyhodnot(pole) == 'o':
        print('Vyhrál počítač!')
