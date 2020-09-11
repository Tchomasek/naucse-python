class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def snez(self, jidlo):
        print("({} na {} chvíli fascinovaně kouká)".format(self.jmeno, jidlo))
        super().snez(jidlo)
    def udelej_zvuk(self):
        print("{}: Mňau!".format(self.jmeno))

class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print("{}: Haf!".format(self.jmeno))

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)

standa = Hadatko('Stanislav')
micka = Kotatko('Micka')
azorek = Stenatko('Azorek')

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.udelej_zvuk()
    zviratko.snez('flákota')
