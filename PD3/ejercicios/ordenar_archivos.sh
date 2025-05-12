#!/usr/bin/env bash

# 1. Encontrar el archivo más recientemente modificado en un directorio.
# 2. Listar todos los archivos por orden de recencia.

echo $(find . -type f -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d ' ' -f 2-)

 # ¿Qué hace el pipe compuesto?
 # 1. Encuentra recursivamente todos los archivos en el directorio actual (.) y los formatea con una marca de tiempo absoluta, su nombre y salto de línea al final.
 # 2. ordenar según la representación numérica de una cadena (-n) y revertir el orden normal (-r).
 # 3. Obtiene la primera línea (-n 1)
 # 4. Divide la cadena según el delimitador ' ' y toma solo la segunda parte (el nombre del archivo).
