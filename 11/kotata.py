class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def __str__(self):
        print("kotatko jmenem {}".format(self.jmeno))
    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))
    def snez(self, jidlo):
        print("{}: mnau mnau, {} mi chutna".format(self.jmeno, jidlo))


mourek = Kotatko("Mourek")
#mourek.jmeno = "Mourek"
mourek.snez("ryba")

micka = Kotatko("Micka")
#micka.jmeno = "Micka"

mourek.zamnoukej()
micka.zamnoukej()

mourek.__str__()
