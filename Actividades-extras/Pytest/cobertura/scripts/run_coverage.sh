#!/usr/bin/env bash
set -euo pipefail

PKG="mi_modulo"
MIN=80
OUTDIR="htmlcov"

echo "🔧 Ejecutando pytest bajo coverage..."
coverage run -m pytest -v

echo "📊 Resumen en consola (fallará si < ${MIN}%):"
coverage report -m --fail-under=${MIN}

echo "🌐 Generando informe HTML en ${OUTDIR}/ ..."
coverage html --directory=${OUTDIR}

echo "✅ Listo. Abre ${OUTDIR}/index.html para ver el reporte."
