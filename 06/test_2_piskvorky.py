import pytest

import piskvorky

def test_tah_chyba():
    with pytest.raises(ValueError):
        piskvorky.tah_pocitace('oxoxoxoxoxoxoxoxoxox')
