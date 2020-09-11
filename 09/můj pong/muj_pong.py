import pyglet
from pyglet import gl
from pyglet.window import key
import random

# Velikost okna (v pixelech)
SIRKA = 900
VYSKA = 600

VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 200  # v pixelech za sekundu
RYCHLOST_PALKY = RYCHLOST * 1.5  # taky v pixelech za sekundu

DELKA_PULICI_CARKY = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXTU = 30

pozice_palek = [VYSKA // 2, VYSKA // 2]  # vertikalni pozice dvou palek
pozice_mice = [0, 0]  # x, y souradnice micku -- nastavene v reset()
rychlost_mice = [0, 0]  # x, y slozky rychlosti micku -- nastavene v reset()
stisknute_klavesy = set()  # sada stisknutych klaves
skore = [0, 0]  # skore dvou hracu

#definovani pozice micku a udeleni rychlosti
def reset():
    #pozice
    pozice_mice[0] = SIRKA // 2 #x
    pozice_mice[1] = VYSKA // 2 #y
    #rychlost
    if random.randint(0, 1):
        rychlost_mice[0] = RYCHLOST
    else:
        rychlost_mice[0] = -RYCHLOST #x
    rychlost_mice[1] = random.uniform(-1, 1) * RYCHLOST #y

#spusteni hry
reset()


def nakresli_obdelnik(x1, y1, x2, y2):
    """Nakresli obdelnik na dane souradnice

    Nazorny diagram::

         y2 - +-----+
              |/////|
         y1 - +-----+
              :     :
             x1    x2
    """
    # Tady pouzijeme volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # ukonci kresleni trojuhelniku

def vykresli():
    """Vykresli stav hry"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna (vybarvi na cerno)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bilou
    #micek#
    nakresli_obdelnik(
        pozice_mice[0] - VELIKOST_MICE // 2,
        pozice_mice[1] - VELIKOST_MICE // 2,
        pozice_mice[0] + VELIKOST_MICE // 2,
        pozice_mice[1] + VELIKOST_MICE // 2,
        )
    #palky
    nakresli_obdelnik(
        0,
        pozice_palek[0] - DELKA_PALKY // 2,
        TLOUSTKA_PALKY,
        pozice_palek[0] + DELKA_PALKY // 2
        )
    nakresli_obdelnik(
        SIRKA - TLOUSTKA_PALKY,
        pozice_palek[1] - DELKA_PALKY // 2,
        SIRKA,
        pozice_palek[1] + DELKA_PALKY // 2
        )
    #půlící čára
    for x in range(DELKA_PULICI_CARKY // 2, VYSKA, DELKA_PULICI_CARKY * 2):
        nakresli_obdelnik(
            (SIRKA // 2) - 1,
            x,
            (SIRKA // 2) + 1,
            x + DELKA_PULICI_CARKY
    )
    #skore
    nakresli_text(
        str(skore[0]),
        ODSAZENI_TEXTU,
        VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
        'left'
    )
    nakresli_text(
        str(skore[1]),
        SIRKA - ODSAZENI_TEXTU,
        VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
        'right'
    )
"""Nakresli dany text na danou pozici

    Argument ``pozice_x`` muze byt "left" nebo "right", udava na kterou stranu
    bude text zarovnany
    """
def nakresli_text(text, x, y, pozice_x):
    """Nakresli dany text na danou pozici

    Argument ``pozice_x`` muze byt "left" nebo "right", udava na kterou stranu
    bude text zarovnany
    """
    napis = pyglet.text.Label(
        text,
        font_size=VELIKOST_FONTU,
        x=x, y=y, anchor_x=pozice_x
    )
    napis.draw()

def stisk_klavesy(symbol,modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add(('nahoru', 0))
    if symbol == key.S:
        stisknute_klavesy.add(('dolu', 0))
    if symbol == key.UP:
        stisknute_klavesy.add(('nahoru', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add(('dolu', 1))

def pusteni_klavesy(symbol,modifikatory):
    if symbol == key.W:
            stisknute_klavesy.discard(('nahoru', 0))
    if symbol == key.S:
            stisknute_klavesy.discard(('dolu', 0))
    if symbol == key.UP:
            stisknute_klavesy.discard(('nahoru', 1))
    if symbol == key.DOWN:
            stisknute_klavesy.discard(('dolu', 1))

def obnov_stav(dt):
#aktualizace pozice palky
    for cislo_palky in (0, 1):

        if ("nahoru", cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] += dt * RYCHLOST_PALKY
        if ("dolu", cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] -= dt * RYCHLOST_PALKY
#osetreni vyjeti palky z obrazovky
        #dolni zarazka
        if pozice_palek[cislo_palky] < DELKA_PALKY // 2:
                pozice_palek[cislo_palky] = DELKA_PALKY // 2
        #horni zarazka
        if pozice_palek[cislo_palky] > VYSKA - (DELKA_PALKY // 2):
            pozice_palek[cislo_palky] = VYSKA - (DELKA_PALKY // 2)
    #pohyb micku
    pozice_mice[0] += rychlost_mice[0] * dt
    pozice_mice[1] += rychlost_mice[1] * dt

    # Odraz micku od sten
    if pozice_mice[1] < VELIKOST_MICE // 2:
        rychlost_mice[1] = abs(rychlost_mice[1])
    if pozice_mice[1] > VYSKA - VELIKOST_MICE // 2:
        rychlost_mice[1] = -abs(rychlost_mice[0])
#odrazeni vlevo
    if pozice_mice[0] < TLOUSTKA_PALKY + VELIKOST_MICE // 2:
        if (pozice_mice[1] < (pozice_palek[0] + DELKA_PALKY // 2)) and (pozice_mice[1] > (pozice_palek[0] - DELKA_PALKY // 2)):
            rychlost_mice[0] = abs(rychlost_mice[0])
        else:
            skore[1] += 1
            reset()
#odrazeni vpravo
    if pozice_mice[0] > (SIRKA - (TLOUSTKA_PALKY + VELIKOST_MICE // 2)):
        if (pozice_mice[1] < (pozice_palek[1] + DELKA_PALKY // 2)) and (pozice_mice[1] > (pozice_palek[1] - DELKA_PALKY // 2)):
            rychlost_mice[0] = -abs(rychlost_mice[0])
        else:
            skore[0] += 1
            reset()

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
    on_key_press=stisk_klavesy,
    on_key_release=pusteni_klavesy
)
pyglet.clock.schedule(obnov_stav)
pyglet.app.run()  # vse je nastaveno, at zacne hra
