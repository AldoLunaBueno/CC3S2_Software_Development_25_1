# language: es

Característica: Comportamiento del Estómago
  @spanish
  Escenario: Comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir
  
  @spanish
  Escenario: Comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir
  
  @spanish
  Escenario: Comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir
  
  @spanish
  Escenario: Comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora, 29 minutos y 61 segundos"
    Entonces mi estómago debería gruñir
  
  @spanish
  Escenario: Comer una cantidad fraccionaria insuficiente de pepinos
    Dado que he comido 9.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir
  
  @spanish
  Escenario: Comer una cantidad fraccionaria suficiente de pepinos
    Dado que he comido 10.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir
  
  @english
  Escenario: Esperar usando horas en inglés y gruñir
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes and half second"
    Entonces mi estómago debería gruñir

  @english
  Escenario: Esperar usando horas en inglés y gruñir
    Dado que he comido 11 pepinos
    Cuando espero "one hour and fifty minutes"
    Entonces mi estómago debería gruñir