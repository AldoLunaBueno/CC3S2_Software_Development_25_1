#!/usr/bin/env bash
msg_file=$1
# tipo(scope)!?: descripción de al menos 10 caracteres
re='^(feat|fix|docs|style|refactor|perf|test|chore)(\([a-z0-9_-]+\))?(!)?: .{10,}$'
if ! grep -Eq "$re" "$msg_file"; then
  echo "Mensaje de commit no cumple conventional commits"
  echo "Ej: fix(parser): manejar comillas dobles correctamente"
  exit 1
fi