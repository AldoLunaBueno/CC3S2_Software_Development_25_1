from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    """Casos de prueba para la Pila"""

    def setUp(self) -> None:
        """Configuración antes de cada prueba."""
        self.stack = Stack()

    def tearDown(self) -> None:
        """Limpieza después de cada prueba."""
        self.stack = None

    def test_is_empty(self) -> None:
        """Prueba de si la pila está vacía."""
        stack = Stack()
        self.assertTrue(
            stack.is_empty(),
            "La pila recién creada debe estar vacía"
        )
        stack.push(5)
        self.assertFalse(
            stack.is_empty(),
            "Después de agregar un elemento, la pila no debe estar vacía"
        )
