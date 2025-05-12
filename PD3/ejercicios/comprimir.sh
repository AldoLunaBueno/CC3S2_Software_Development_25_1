#!/usr/bin/env bash
# comprimir.sh

# Recorre el árbol de directorios con find
# y busca todos los archivos html para comprimirlos.

# Info útil:
# Comando rápido para comprimir todo en el directorio actual:
# ls | xargs tar -cf etc.tar
# xargs es necesario porque tar no lee la salida estándar de ls
# xargs antes de un comando le pasa la stdout redirigida como argumentos

find . -type f -name '*.html' -print0 | xargs -0 tar -cf archivos_comprimidos.tar
# -print0 y -0 se usan casi siempre cooperativamente 
# para separar en caracteres nulos

# Usar una variable como intermediario:
# mapfile -d '' archivos < <(find . -type f -name '*.html' -print0)
# tar -cf archivos_comprimidos.tar "${archivos[@]}"
