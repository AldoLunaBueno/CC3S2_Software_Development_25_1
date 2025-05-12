import pytest
from app.math import dividir

@pytest.mark.bdd
def test_usuario_divide_correctamente():
    """Simula que un usuario divide números correctamente."""
    resultado = dividir(100, 4)
    assert resultado == 25.0
