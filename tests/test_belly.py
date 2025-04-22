import pytest
from src.belly import Belly
from pytest_mock import mocker, MockerFixture

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
        
def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True
    
def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos() == 15
    
def test_stress_esta_gruñendo():
    belly = Belly()
    belly.comer(1000)
    try:
        belly.esta_gruñendo(stress_test=True)
    except Exception:
        assert False, "El método esta_gruñendo() no se puede usar en modo de prueba"
        
def test_belly_predict_growl():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.predict_growl() == True

def test_time_to_eat_calls_clock_once_mock(mocker: MockerFixture):
    fake_clock = mocker.Mock(return_value=10000)
    belly = Belly(clock_service=fake_clock)
    belly.time_to_eat()
    fake_clock.assert_called_once()
    
def test_time_to_eat_returns_value_stub(mocker: MockerFixture):
    fake_clock = mocker.Mock(return_value=10000)
    belly = Belly(clock_service=fake_clock)
    assert belly.time_to_eat() == 10000