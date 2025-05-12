#!/usr/bin/env bash
branch=$(git rev-parse --abbrev-ref HEAD)
# solo: feature/XYZ-123-descripcion o hotfix/XYZ-123
re='^(feature|hotfix)\/[A-Z]{2,5}-[0-9]+-[a-z0-9]+(-[a-z0-9]+)*$'
if [[ ! $branch =~ $re ]]; then
  echo "Nombre de rama inválido: $branch"
  echo "Formato correcto: feature/ABC-123-descripcion"
  exit 1
fi