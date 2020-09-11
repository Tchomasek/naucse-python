import piskvorky

def test_tah_na_prazdne_pole():
    pole = piskvorky.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('o') == 1
    assert pole.count('-') == 19
