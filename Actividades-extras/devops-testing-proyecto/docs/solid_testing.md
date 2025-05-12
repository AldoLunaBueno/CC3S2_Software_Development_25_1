# Principios SOLID en Testing DevOps

Este documento proporciona un desarrollo extenso en español sobre la manera de aplicar SRP, OCP, LSP, ISP y DIP en suites de pruebas automatizadas.

## Ejemplos de cada principio en la suit de pruebas

### SRP

En _test_user_repo.py_ la prueba _test_add_and_get_user_ verifica una única responsabilidad: que un usuario se puede agregar y luego recuperar correctamente.

No mezcla otros comportamientos (como errores, validaciones, etc.), por lo que cumple bien con SRP.

### OCP

En _test_payment_service.py_ observamos una prueba parametrizada. Cuando parametrizamos una prueba, logramos dos cosas:

1. Evitamos tener que modificar o replicar mal la misma lógica en otro método
2. Facilitamos la incorporación de nuevos casos de prueba, de forma que solo tenemos que añadir los datos del estos nuevos casos.

El primer punto mantiene la prueba cerrada a modificación; mientras que el segundo punto abre la prueba a ser extendida. Al darse las dos propiedades a la vez, podemos decir efectivamente que parametrizar las pruebas implica aplicar el principio OCP.

### LSP

a

### ISP

a

### DIP

a

## Términos

El camino feliz