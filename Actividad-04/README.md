# Introducción a Git

## Conceptos básicos de Git

Uso el comando git config para configurar mi nombre de usuario y correo para acceder a todos mis repositorios (modo global). También sirve para listar las variables de configuración, con git config --list

![](2025-04-02-07-47-07.png)

> Si no hago esto, Git no podrá guardar ningún cambio porque cada cambio (commit) se asocia a la identidad de quien realiza el cambio.
>
> ![](2025-04-02-08-19-44.png)

### Operaciones básicas

#### git init

Al inicializar el nuevo repositorio, se genera un directorio .git que se puede explorar en Windows activando la vista de elementos ocultos:

![](2025-04-02-07-57-17.png)

> Hay que evitar crear un repositorio dentro de otro repositorio, porque git da problemas.

#### git status

Creo un nuevo archivo llamado README.md. Mi archivo recién creado no está guardado en el historial, por lo que figura como untracked:

![](2025-04-02-08-07-58.png)

#### git add

Con este comando decido hasta qué punto rastrear mis cambios para luego guardarlos en el historial.

![](2025-04-02-08-13-05.png)

#### git commit

Pero aún no he guardado nada. Este comando sirve para guardar los cambios rastreados por git add en forma de un commit:

![](2025-04-02-08-21-00.png)

#### git log

Con este comando puedo ver el historial de commits y algunos detalles como el autor.

![](2025-04-02-08-31-53.png)

> Este comando me permitió darme cuenta de que había escrito mal mi correo en la configuración. Para arreglarlo usé git commit --amend (solo se puede para el último commit y si no ha sido pusheado a un repositorio remoto):
>
> ![](2025-04-02-08-31-26.png)

Pregunta: ¿Cuál es la salida del siguiente comando?

`git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'`

```
*        5a1d078 46 minutes ago ("AldoLunaBueno") Initial commit with README.md
```

![](2025-04-02-09-25-46.png)

## Ejercicios

### Ejercicio 1

La primera línea del mismo documento es distinta en ambas ramas, y esto crea un conflicto cuando usamos git merge, el cual hay que resolver vanualmente.

![](2025-04-02-16-09-45.png)

![](2025-04-02-16-13-38.png)

![](2025-04-02-16-20-03.png)

### Ejercicio 2

![](2025-04-02-16-27-29.png)

Para salir presionamos q.

Ahora vamoa a añadir un cambio a nuestro código que no deberíamos haber hecho.

![](2025-04-02-16-36-03.png)

Si el cambio es tan sencillo como agregar una línea, podríamos revertirlo simplemente borrando esa línea y haciendo un nuevo commit, pero ¿qué tal si el cambio erróneo es más complejo? La mejor solución es usar el comando `git revert HEAD`.

![](2025-04-02-16-35-41.png)

Como vemos, el commit erróneo que hicimos no desapareció, pero en el HEAD volvemos a tener la versión antes del cambio erróneo.

![](2025-04-02-17-14-40.png)

Para ver el git rebase en acción, simulamos commits que añaden en pasos una funcionalidad.

![](2025-04-02-17-36-47.png)

Queremos resumir estos pasos en un solo commit que refleje el cambio completo introducido por la funcionalidad. Por eso luego de usar git rebase solo usamos el mensaje del primer commit para que represente a todos (el primero con pick y los demás con squash o simplemente s).

![](2025-04-02-17-38-32.png)

![](2025-04-02-17-39-38.png)

> Un comando git rebase mal ejecutado cambia el HEAD hacia el primer commit de los que iban a ser resumidos en uno solo.

![](2025-04-02-17-25-56.png)

### Ejercicio 3

Creamos una nueva rama bugfix/rollback-feature desde el commit correspondiente a la creación del archivo main.py. 

![](2025-04-02-19-10-22.png)

Intentamos hacer un merge entre esta rama y el HEAD, pero ocurre un conflicto debido a que en ambas se toca la misma pieza de código: la versión del HEAD tiene un desarrollo que no tiene la nueva rama, y esta nueva rama tiene la solución a un bug que no se llegó a resolver en HEAD. Por esta razón, el merge debe ser realizado manualmente.

![](2025-04-02-19-18-47.png)

![](2025-04-02-19-21-37.png)

### Ejercicio 4

![](2025-04-06-17-18-42.png)

![](2025-04-06-17-21-52.png)

### Ejercicio 5

Primero clonamos el repositorio que llamamos repo_ej5_25_1. Está vacío. Esto es un problema, porque para crear una nueva rama se necesita un commit desde la cual esta cuelgue. Por eso creamos previamente el archivo que modificaremos después, collaboration.py, y guardamos este cambio como un nuevo commit.

![](2025-04-06-20-34-02.png)

Ahora que se pudo crear la nueva rama feature/team-feature, que está ligada al último commit, hacemos un checkout para hacer cambios sobre esta.

![](2025-04-06-18-35-52.png)

Cuando vamos a subir los cambios al repositorio remoto con git push, se presenta el siguiente problema:

![](2025-04-06-18-32-10.png)

Esto no sucedería si el comando fuera ejecutado desde un entorno que se puede conectar al navegador, ya que desde ahí crearía un enlace para que al abrirlo me permita autenticarme en el sitio web mismo. Aquí, en WSL, tengo que copiar y pegar el token de acceso en la terminal.

![](2025-04-06-18-32-48.png)

Y también hay que configurar el token para otorgar acceso a los repositorios.

![](2025-04-06-18-33-04.png)

Una vez subidos los cambios podemos ver en el repositorio remoto que solo hay una rama. ¿Por qué no aparece la rama main? Esto es porque solo hemos subido los cambios de la nueva rama, no de la rama main.

![](2025-04-06-18-41-39.png)

Pero para hacer el pull request de la nueva rama a la rama main necesitamos que aparezcan ambas en el repositorio remoto de GitHub, así que hacemos también git push origin main:

![](2025-04-06-18-45-36.png)

Aquí se puede ver el mismo archivo collaboration.py en su última actualización en ambas ramas en GitHub:

![](2025-04-06-18-47-29.png)

Para hacer el pull request seleccionamos las ramas apropiadas siguiendo la dirección de la flecha y, si dice *Able to merge*, podemos hacer el pull request.

![](2025-04-06-18-53-53.png)

Aquí añadimos un título (por defecto es el título del commit contenido en el pull request) y explicamos el pull request como si fuera la descripción de un commit.

![](2025-04-06-18-58-07.png)

Una vez hecho el PR, otros colaboradores o el autor pueden comentar, revisar y añadir actualizaciones al PR.

![](2025-04-06-19-04-09.png)

![](2025-04-06-19-05-18.png)

![](2025-04-06-19-05-52.png)