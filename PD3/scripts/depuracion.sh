set -xe  # traza + salir al error
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
trap 'echo "Error en línea $LINENO"; exit 1' ERR