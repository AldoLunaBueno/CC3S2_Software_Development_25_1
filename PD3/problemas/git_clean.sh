#!/usr/bin/env bash
set -euo pipefail

# Activar depuración si se pasa --debug
if [[ "${1:-}" == "--debug" ]]; then
    set -x
    export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
    shift
fi

# Función: mostrar_ayuda
# Muestra el uso del script y las opciones disponibles
mostrar_ayuda() {
    cat <<EOF
Uso: $0 [--branches|--stashes|--backup|--report|--help|--debug]

Opciones:
  --branches   Limpiar ramas locales y remotas con patrón
  --stashes    Gestionar stashes de forma interactiva
  --backup     Crear backup filtrado del reflog
  --report     Generar informe JSON del repositorio
  --help       Mostrar esta ayuda
  --debug      Activar modo depuración
EOF
}

# Función: limpiar_ramas
# Limpia ramas locales y remotas según un patrón
limpiar_ramas() {
    read -rp "Ingresa el patrón de la rama (regex): " patron
    if [[ ! $patron =~ ^[[:alnum:]_/.-]+$ ]]; then
        echo "Patrón inválido."
        exit 1
    fi

    mapfile -t ramas_locales < <(git branch | sed 's/..//' | grep -E "$patron" || true)
    if [[ ${#ramas_locales[@]} -eq 0 ]]; then
        echo "No hay ramas locales que coincidan con '$patron'"
    else
        for rama in "${ramas_locales[@]}"; do
            read -rp "¿Eliminar rama local '$rama'? (s/n): " respuesta
            if [[ $respuesta =~ ^[sS]$ ]]; then
                git branch -D "$rama"
            fi
        done
    fi

    mapfile -t ramas_remotas < <(git branch -r | sed 's/ *origin\///' | grep -E "$patron" || true)
    if [[ ${#ramas_remotas[@]} -eq 0 ]]; then
        echo "No hay ramas remotas que coincidan con '$patron'"
    else
        for rama in "${ramas_remotas[@]}"; do
            read -rp "¿Eliminar rama remota 'origin/$rama'? (s/n): " respuesta
            if [[ $respuesta =~ ^[sS]$ ]]; then
                git push origin --delete "$rama"
            fi
        done
    fi
}

# Función: gestionar_stashes
# Lista stashes y permite aplicar o eliminar interactuando con el usuario
gestionar_stashes() {
    echo "Lista de stashes:"
    lista=$(git stash list | nl -w2 -s'. ')
    echo "$lista"

    read -rp "Introduce los índices de stashes a modificar (ej: 0 2 4): " linea
    read -ra indices <<< "$linea"

    for i in "${indices[@]}"; do
        if [[ ! $i =~ ^[0-9]+$ ]]; then
            echo "Índice inválido: $i"
            exit 1
        fi
    done

    for i in "${indices[@]}"; do
        read -rp "¿Aplicar stash@{$i} (a), eliminar (e), ambos (ae)? " accion
        if [[ $accion =~ a ]]; then
            git stash apply "stash@{$i}"
        fi
        if [[ $accion =~ e ]]; then
            git stash drop "stash@{$i}"
        fi
    done
}

# Función: backup_reflog
# Guarda entradas relevantes del reflog en un archivo
backup_reflog() {
    archivo="reflog_$(date +%Y%m%d_%H%M%S).log"
    git reflog | grep -E 'reset|merge' > "$archivo"
    echo "Backup del reflog guardado en $archivo"
}

# Función: informe_json
# Genera un informe en formato JSON con datos del repositorio
informe_json() {
    rama=$(git rev-parse --abbrev-ref HEAD)
    cantidad_stashes=$(git stash list | wc -l)
    tags=$(git tag | jq -R -s -c 'split("\n")[:-1]')
    submodulos=$(git submodule status | awk '{print $2}' | jq -R -s -c 'split("\n")[:-1]')
    archivo="informe_$(date +%Y%m%d).json"

    json=$(cat <<EOF
{
  "rama_actual": "$rama",
  "stashes": $cantidad_stashes,
  "tags": $tags,
  "submodulos": $submodulos
}
EOF
)
    echo "$json" > "$archivo"
    echo "Informe JSON generado en $archivo"
}

# Enrutamiento principal
case "${1:-}" in
    --help)
        mostrar_ayuda
        ;;
    --branches)
        limpiar_ramas
        ;;
    --stashes)
        gestionar_stashes
        ;;
    --backup)
        backup_reflog
        ;;
    --report)
        informe_json
        ;;
    *)
        mostrar_ayuda
        ;;
esac
