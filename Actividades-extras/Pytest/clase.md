# Clase

## unittest vs pytest

Paralelismo:

- pytest tiene paralelismo, con xdist.
- unittest requiere multiprocessing porque no tiene paralelismo.

Gracias al paralelismo se puede reducir el tiempo de ejecución de grandes baterías de pruebas.

## makefile

pacman -Syu
pacman -D

### Con varios tarjet

- make: ejecuta solo el primer objetivo
- make test: ejecuta todos los objetivos
  
Se puede hacer esto:

make test build clean: se ejecutan los objetivos de forma paralela

make -j build test clean: inicializa simultáneamente los comandos en distintos hilos de la CPU (si la compu lo permite)

make all

## monkey patching

cambiar de entornos os.environ, kubernetes