import pytest
from app.math import sumar, dividir

@pytest.mark.unit
def test_sumar_numeros():
    assert sumar(2, 3) == 5

@pytest.mark.unit
def test_dividir_numeros():
    assert dividir(10, 2) == 5.0
