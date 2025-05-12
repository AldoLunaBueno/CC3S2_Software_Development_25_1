# Práctica Dirigida 3

## Previo

### Comando ls

¿Cómo obtener una lista que incluya todos los archivos, incluidos los ocultos, que sea legible por humanos, ordenado comenzando por el más reciente y con salida coloreada?

```txt
-rw-r--r--   1 user group 1.1M Jan 14 09:53 f1
drwxr-xr-x   5 user group  160 Jan 14 09:53 .
-rw-r--r--   1 user group  514 Jan 14 06:42 f2
```

Respuesta:

```bash
ls -laht --color
```

> La documentación se puede leer con ``man ls`` localmente.

## Bash

Los scripts de Bash siempre deben comenzar con `#!/usr/bin/env bash`

Para ejecutar un script de Bash en Linux se requiere habilitar la ejecución:

```bash
chmod +x script.sh
```

