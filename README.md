# PD2: Script Interactivo

## Preguntas

**Pregunta 1.** ¿Qué diferencias observas en el historial del repositorio después de restaurar un commit mediante reflog?

El comando `git reflog` es la prueba de que **git no borra nada**. No muestra el historial de commits (para eso tenemos ``git log``), sino que muestra un registro privado de movimientos del HEAD del repo, por lo tanto puede regresar a un estado anterior del repositorio en el que el perdido commit figuraba y así restaurarlo. El historial refleja ese movimiento como un nuevo cambio de HEAD, manteniendo los anteriores. Es decir, solo crea un nuevo punto de referencia.

**Pregunta 2.** ¿Cuáles son las ventajas y desventajas de utilizar submódulos en comparación con subtrees?

Tanto submódulos como subtrees permiten incluir un repo (externo) dentro de otro (el nuestro). Si queremos que el repo externo que incluimos esté bien aislado de nuestro repo, entonces lo incluimos como submódulo. Si el aislamiento no es problema, usamos subtrees, pero hay que tener en cuenta que todo el historial de ese repo externo se mezclará con el historial de nuestro repo, y es más difícil actualizar cambios en el repo externo.

**Pregunta 3.** ¿Cómo impacta la creación y gestión de hooks en el flujo de trabajo y la calidad del código?

Los hooks validan nuestros cambios automáticamente al hacer commit o push, por ejemplo. El impacto de esta validación automática es que aumenta la calidad del código, evita errores y estandariza practicas de desarrollo, además de la obvia aceleración del trabajo.

**Pregunta 4.** ¿De qué manera el uso de git bisect puede acelerar la localización de un error introducido recientemente?

El comando `git bisect` permite localizar el el commit exacto en donde se introdujo un error mediante búsqueda binaria. Si el desarrollador (o pruebas automatizadas) puede determinar si un commit introduce el error o no, entonces se puede valer del coomando `git bisect` para ir marcando los commits como libres de error (good) o como commits con error (bad). El algoritmo de búsqueda binaria integrado en `git bisect` usa esta retroalimentación del desarrollador para buscar de la manera más eficiente haciendo checkout automático a commits intermedios hasta encontrar el primer commit en donde se introduce el error. Personalmente, opino que si se usa manualmente, su utilidad se ve cuando hay que buscar en un espacio de 10 commits a más. Con menos commits, uno puede hasta adivinar dónde se introdujo el error. Sin embargo, su uso automático en combinación con pruebas automatizadas que determinen automáticamente si el commit tiene error lo vuelve un comando muy poderoso.

**Pregunta 5.** ¿Qué desafíos podrías enfrentar al administrar ramas y stashes en un proyecto con múltiples colaboradores?

El gran desafío es que los colaboradores, ya sea por olvido o descuido, pueden incumplir alguna regla de la política de ramas. Somos humanos, podemos equivocarnos. Y estas equivocaciones generan conflictos, por ejemplo, al fusionar ramas. Podemos tener ramas con nombres que no son consistentes. Inluso se puede correr el riesgo de sobreescribir o eliminar ramas importantes sin revisión. Con respecto a los stashes, como solo se guardan localmente, es difícil que otro colaborador borre tus stashes, salvo que se trabaje a través de un mismo servidor compartido y accediendo con el mismo usuario. Lo que si puede pasar es que por descuido los stashes no se limpien (quizás se delegaron a un hook mal hecho) y se vayan acumulando los stashes de todos.

## 