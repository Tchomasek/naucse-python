pole = 20*"-"

def vyhodnot(pole):
    if 'xxx' in pole:
        return("x")
    elif 'ooo' in pole:
        return("o")
    elif '-' not in pole:
        return("!")
    else:
        return '-'

def tah(pole, cislo_policka, symbol):
    if symbol <= 0 or symbol > 19:
        print()
