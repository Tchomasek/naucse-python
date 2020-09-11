class Kocka:
    def __init__(self):         # Init funkce nemusi brat jako parametr
        self.pocet_zivotu = 9   # pocet zivotu, ten je pokazde 9.

    def zamnoukej(self):
        print("Mnau, mnau, mnauuu!")

    def je_ziva(self):
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if not self.je_ziva():
            print("Nemuzes zabit uz mrtvou kocku!")
        else:
            self.pocet_zivotu -= 1

    def snez(self, jidlo):
        if not self.je_ziva():
            print("Je zbytecne krmit mrtvou kocku!")
            return
        if jidlo == "ryba" and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("Kocka spapala rybu a obnovil se ji jeden zivot.")
        else:
            print("Kocka se krmi.")
