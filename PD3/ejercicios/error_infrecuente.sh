#!/usr/bin/env bash

n=$(( RANDOM % 100 ))

if [[ n -eq 42 ]]; then
   echo "Algo esta pasando!"
   >&2 echo "El error fue por usar numero magicos"
   exit 1
fi

echo "Todo salio de acuerdo al plan"