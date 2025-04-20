import pytest
from src.belly import Belly

def test_pepinos_fraccionarios_gruñir():
    belly = Belly()
    belly.comer(10.5)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True
    
def test_pepinos_fraccionarios_no_gruñir():
    belly = Belly()
    belly.comer(9.5)
    belly.esperar(2)
    assert belly.esta_gruñendo() == False
    
def test_pepinos_negativos_error():
    belly = Belly()
    belly.comer(-20)
    belly.esperar(2)
    with pytest.raises(ValueError):
        belly.esta_gruñendo()