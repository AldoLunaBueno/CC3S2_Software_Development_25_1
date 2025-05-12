# tests/test_my_module.py

import pytest
from mi_modulo import add, subtract

@pytest.mark.parametrize("a,b,exp", [
    (1,  2,  3),
    (0,  0,  0),
    (-1, 1,  0),
])
def test_add(a, b, exp):
    assert add(a, b) == exp

def test_subtract():
    assert subtract(10, 4) == 6
