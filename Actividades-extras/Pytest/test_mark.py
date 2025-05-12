import pytest
# Esta prueba está marcada como 'dicttest'
# Permite filtrar su ejecución con la opción `-m dicttest`


@pytest.mark.dicttest
def test_lista_igual_a_si_misma():
    """Prueba que verifica que una lista es igual a sí misma."""
    lista = ['a', 'b']
    assert lista == lista

# Esta prueba no tiene marca específica
# Se puede ejecutar con `-m 'not dicttest'`


def test_fallo_forzado():
    """Prueba que falla intencionadamente."""
    assert False
