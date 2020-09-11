from random import randrange
body = 0
while body < 21:
    dalsi = input(str("chceš další?"))
    if dalsi == "ano" or dalsi == "Ano":
        karta = randrange(2, 11)
        body = body + karta
        print("tvůj součet je:", body)
    elif dalsi == "ne" or dalsi == "Ne":
        break
    else:
        print("zadan spatny vstup")

print("tvůj součet je:", body)

if body > 21:
    print("prohrál jsi")
