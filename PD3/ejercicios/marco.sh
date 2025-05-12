marco() {
    export MARCO_DIR="$PWD"
}

polo() {
    if [[ -z "$MARCO_DIR" ]]; then
        echo "No has ejecutado 'marco' aún."
    else
        cd "$MARCO_DIR" || echo "Error al cambiar de directorio"
    fi
}