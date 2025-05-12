import pytest

# Intentamos importar el módulo 'milib'
try:
    import milib
except ImportError:
    milib = None  # Si no se puede importar, se asigna None


# Este test está marcado para que **siempre se omita** (nunca se ejecuta)

@pytest.mark.skip("No corre esto!")
def test_fail():
    # Este test fallaría si se ejecutara
    assert False

# Este test **solo se ejecuta** si el módulo 'milib' está disponible

@pytest.mark.skipif(milib is None, reason="milib no está disponible")
def test_milib():
    # Verifica que la función fw() de milib devuelve 42
    assert milib.fw() == 42

# Este test se omite en tiempo de ejecución con una condición
def test_skip_at_runtime():
    if True:
        pytest.skip("Finalmente decidí no ejecutar este test")
    # Aquí iría la lógica del test si no se omitiera
