import time

class Belly:
    def __init__(self):
        self._pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        self._pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self, stress_test = False):
        # El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
        if (not stress_test and (self._pepinos_comidos < 0 or self._pepinos_comidos > 100)):
            raise ValueError
        if stress_test:
            time.sleep(self._pepinos_comidos / 1000)
        return self.tiempo_esperado >= 1.5 and self._pepinos_comidos > 10
    
    def pepinos_comidos(self):
        return self._pepinos_comidos