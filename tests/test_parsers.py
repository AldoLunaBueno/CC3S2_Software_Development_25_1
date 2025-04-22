import pytest
from src.parsers import time_descr_to_h


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
    assert abs(time_descr_to_h(time_description) - expected_time) < 0.0001


@pytest.mark.parametrize("time_description, expected_time", [
    ("1 hour", 1.0),
    ("90 minutes", 1.5),
    ("1 hours and 30 minutes", 1.5),
    ("3600 seconds", 1.0),
    ("1 hours and 29 minutes and 61 seconds", 1.5003),
    ("1 hours y 30 minutes and 45 seconds", 1.5125),
    ("1 hours, 30 minutes and 45 seconds", 1.5125),
    ("half hour", 0.5),
    ("2 hours 15 minutes", 2.25),
    ("45 minutes 5 seconds and 3 hours", 3.751388)
])
def test_convertir_tiempo_a_horas_en_ingles(time_description, expected_time):
    diff = time_descr_to_h(time_description, "english") - expected_time
    assert abs(diff) < 0.0001


@pytest.mark.parametrize("time_description", ["horas", "minutos"])
def test_invalid_description_spanish(time_description):
    with pytest.raises(ValueError):
        time_descr_to_h(time_description)


@pytest.mark.parametrize("time_description", ["hours", "minutes"])
def test_invalid_description_english(time_description):
    with pytest.raises(ValueError):
        time_descr_to_h(time_description, "english")


def test_unkown_language():
    with pytest.raises(ValueError):
        time_descr_to_h("une heure", language="unkown")
