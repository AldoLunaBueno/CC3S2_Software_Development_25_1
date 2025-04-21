import pytest
from src.parsers import time_description_to_hours

@pytest.mark.parametrize("time_description, expected_time", [
    ("1 hora", 1.0),
    ("90 minutos", 1.5),
    ("1 hora y 30 minutos", 1.5),
    ("3600 segundos", 1.0),
    ("1 hora y 29 minutos y 61 segundos", 1.5003),
    ("1 hora y 30 minutos y 45 segundos", 1.5125),
    ("1 hora, 30 minutos y 45 segundos", 1.5125),
    ("media hora", 0.5),
    ("2 horas 15 minutos", 2.25),
    ("dos horas y treinta minutos", 2.5),
    ("3 horas 45 minutos 5 segundos", 3.7513),
    ("25 minutos y 10 segundos", 0.4194),
    ("45 segundos", 0.0125)
])
def test_convertir_tiempo_a_horas(time_description, expected_time):
    assert abs(time_description_to_hours(time_description) - expected_time) < 0.0001
