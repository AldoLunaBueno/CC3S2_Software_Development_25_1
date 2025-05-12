import pytest
from app.math import sumar, dividir

@pytest.mark.integration
def test_suma_y_division():
    total = sumar(10, 20)    # 30
    resultado = dividir(total, 5)
    assert resultado == 6.0
