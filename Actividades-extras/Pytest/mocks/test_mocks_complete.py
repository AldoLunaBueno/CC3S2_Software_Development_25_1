# test_mock_complete.py
"""
Demostración unificada de técnicas de unittest.mock:

1.  Mock "vacío" con atributos y métodos creados dinámicamente.
2.  side_effect para introducir lógica dentro del mock.
3.  Validación de llamadas con assert_called_*.
4.  mock.patch como gestor de contexto y como decorador.
5.  Tests de integración que emulan distintos escenarios
    usando requests.get sin tocar la red.

Ejecuta:
    pytest -q test_mock_complete.py
"""

from unittest import mock
import os
import pytest
import requests

# 1.  Lógica a validar (código de producción "DUT")



class WhereIsPythonError(Exception):  # mismo nombre que en el ejemplo
    pass


def is_python_still_a_programming_language() -> bool:
    """
    Devuelve True si la home page de python.org contiene la frase
    "Python is a programming language".  Ante cualquier situación
    inesperada lanza WhereIsPythonError.
    """
    import requests  # import local para facilitar el parcheo

    try:
        r = requests.get("http://python.org")
    except IOError:
        # simulamos ‘red rota’: dejamos que el flujo
        # continúe hasta el raise final
        pass
    else:
        if r.status_code == 200:
            return "Python is a programming language" in r.content
    raise WhereIsPythonError("Something bad happened")


# 2.  Utilidades auxiliares para las pruebas


def get_fake_get(status_code: int, content: str):
    """
    Devuelve una función que imita requests.get.
    Esa función a su vez retorna un mock con atributos
    status_code y content pre-configurados.
    """

    # Creamos un mock "respuesta HTTP"
    fake_response = mock.Mock()
    fake_response.status_code = status_code
    fake_response.content = content

    def fake_get(url: str):
        # ¡ignora la URL por completo!
        return fake_response

    return fake_get


def raise_get(url: str):
    """Simula fallo de red al llamar a requests.get."""
    raise IOError(f"Unable to fetch url {url}")

# 3.  Tests unitarios independientes (atributos, métodos, efectos)

def test_dynamic_attribute_and_method(capsys):
    m = mock.Mock()
    # 3.1 Atributo asignado en tiempo de ejecución
    m.some_attribute = "hello world"
    assert m.some_attribute == "hello world"

    # 3.2 Método que siempre devuelve 42
    m.some_method.return_value = 42
    assert m.some_method() == 42
    assert m.some_method("with", "arguments") == 42

    # 3.3 Método con efecto secundario (imprime y devuelve 43)
    def print_hello():
        print("hello world!")  # side effect
        return 43

    m.some_side_effect_method.side_effect = print_hello
    assert m.some_side_effect_method() == 43

    captured = capsys.readouterr()
    assert "hello world!" in captured.out

    # 3.4 El método se invocó exactamente una vez
    m.some_side_effect_method.assert_called_once_with()

def test_validate_calls_success():
    m = mock.Mock()
    m.some_method("f1", "b1")
    # Coincide → no lanza excepción
    m.some_method.assert_called_once_with("f1", "b1")
    # Con mock.ANY podemos ignorar un parámetro
    m.some_method.assert_called_once_with("f1", mock.ANY)


def test_validate_calls_failure():
    m = mock.Mock()
    m.some_method("f1", "b1")
    with pytest.raises(AssertionError):
        m.some_method.assert_called_once_with("f1", "baz")


# 4.  Ejemplos de patch como gestor de contexto


def test_patch_os_unlink_context_manager():
    # Simulamos que os.unlink siempre lanza IOError
    def fake_unlink(path):
        raise IOError("Testing!")

    with mock.patch("os.unlink", fake_unlink):
        with pytest.raises(IOError):
            os.unlink("dummy.txt")

    # Fuera del with, la función original está restaurada
    fd, tmp = None, None
    try:
        # Creamos y luego borramos un archivo real para comprob1
        fd, tmp = os.open("tempfile.txt", os.O_CREAT), "tempfile.txt"
    finally:
        if fd is not None:
            os.close(fd)
        os.unlink(tmp)  # no debería lanzar


# 5.  Tests completos usando patch como decorador


@mock.patch(
    "requests.get",
    get_fake_get(200, "Python is a programming language for sure"),
)
def test_python_is():
    assert is_python_still_a_programming_language() is True


@mock.patch(
    "requests.get",
    get_fake_get(200, "Python is no more a programming language"),
)
def test_python_is_not():
    assert is_python_still_a_programming_language() is False


@mock.patch("requests.get", get_fake_get(404, "Whatever"))
def test_bad_status_code():
    with pytest.raises(WhereIsPythonError):
        is_python_still_a_programming_language()


@mock.patch("requests.get", raise_get)
def test_ioerror():
    with pytest.raises(WhereIsPythonError):
        is_python_still_a_programming_language()

# tests extra para pytest + unittest.mock

import requests

# 6. Parametrización + monkeypatch

@pytest.mark.parametrize(
    "status_code, content, expectation",
    [
        (200, "Python is a programming language", True),
        (200, "PYTHON *was* a programming language", False),
        (404, "Whatever", pytest.raises(WhereIsPythonError)),
    ],
)
def test_parametrize_monkeypatch(
    monkeypatch, status_code, content, expectation
):
    """Misma lógica, pero variando datos con @parametrize."""

    def fake_get(url):
        return mock.Mock(status_code=status_code, content=content)

    # Monkeypatch reemplaza *en caliente* sin decoradores
    monkeypatch.setattr(requests, "get", fake_get)

    if isinstance(expectation, bool):
        assert is_python_still_a_programming_language() is expectation
    else:
        with expectation:
            is_python_still_a_programming_language()


# 7. patch.object – parcheo de un método concreto de un módulo

def test_patch_object_on_os_path():
    with mock.patch.object(os.path, "isfile", return_value=True) as isfile_mock:
        assert os.path.isfile("dummy.txt")  # siempre True
        isfile_mock.assert_called_once_with("dummy.txt")
    # Fuera del with la función original vuelve a estar intacta
    assert os.path.isfile(__file__)

# 8. patch.dict / monkeypatch.setenv – variables de entorno

def test_patch_dict_env():
    with mock.patch.dict(os.environ, {"API_KEY": "TEST123"}, clear=False):
        assert os.getenv("API_KEY") == "TEST123"
    # Restituido
    assert os.getenv("API_KEY") != "TEST123"

def test_monkeypatch_setenv(monkeypatch):
    monkeypatch.setenv("FEATURE_FLAG", "on")
    assert os.getenv("FEATURE_FLAG") == "on"

# 9. Especificar interfaz con autospec / create_autospec

class Service:
    def do_something(self, x):
        ...

def test_autospec_restricts_attributes():
    srv_mock = mock.create_autospec(Service)
    srv_mock.do_something.return_value = 99
    assert srv_mock.do_something(5) == 99
    # Llamar a método inexistente provoca AttributeError
    with pytest.raises(AttributeError):
        srv_mock.unexpected()

# 10. call_args_list y conteo de invocaciones

def test_call_args_inspection():
    processor = mock.Mock()
    for i in range(3):
        processor.process(i)
    assert processor.process.call_count == 3
    # Recuperamos los argumentos usados en todas las llamadas
    seen = [call.args[0] for call in processor.process.call_args_list]
    assert seen == [0, 1, 2]

# 11. Ejemplos de marcas xfail / skip

@pytest.mark.xfail(reason="Demostración de prueba esperadamente fallida")
def test_xfail_demo():
    # Esta aserción es falsa, pytest la marcará como XFAIL (no como error)
    assert 1 == 0

@pytest.mark.skipif(os.name != "posix", reason="Solo relevante en sistemas POSIX")
def test_skip_demo():
    # El separador de rutas es '/' en POSIX
    assert os.sep == "/"

