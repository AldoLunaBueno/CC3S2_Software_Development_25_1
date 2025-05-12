#!/usr/bash/env bash

# Aritmética
a=7; b=3
echo "$a + $b = $((a + b))"
echo "$a ** $b = $((a ** b))"

# Substituciones de comandos
fecha=$(date +%Y-%m-%d)
archivos=$(ls | wc -l)

echo "Hoy: $fecha, Archivos: $archivos"

# Otras
VAR=""
echo "${VAR:-default}" # default si VAR es vacío
txt="archivo.tar.gz"
echo "${txt%.tar.gz}"  # el % quita sufijo