import time
from src.clock import get_current_time

class Belly:
    def __init__(self, clock_service = get_current_time):
        self._pepinos_comidos = 0
        self._tiempo_esperado = 0
        self._clock = clock_service # Dependency Inyection

    def comer(self, pepinos: int):
        self._pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas: int):
        self._tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self, stress_test = False):
        # El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
        if not stress_test and (self._pepinos_comidos < 0 or self._pepinos_comidos > 100):
            raise ValueError("Invalid number of cukes")
        if stress_test:
            time.sleep(self._pepinos_comidos / 1000)
        return self._tiempo_esperado >= 1.5 and self._pepinos_comidos > 10
    
    def pepinos_comidos(self):
        return self._pepinos_comidos
    
    def predict_growl(self):
        return self._tiempo_esperado >= 1.5 and self._pepinos_comidos > 10
    
    def remaining_cukes_avoiding_growl(self):
        if self._pepinos_comidos <= 10:
            return 10 - self._pepinos_comidos
        else:
            return -1
        
    def time_to_eat(self):
        return self._clock()