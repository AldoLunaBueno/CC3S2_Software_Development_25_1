# i=0
# while (( $? == 0 )); do
#    (( i++ ));
#    bash "./error_infrecuente.sh";
# done

# echo "Ejecuciones hasta el fallo: $i"

executable="./error_infrecuente.sh"
stdout_file="salida.txt"
stderr_file="error.txt"
i=0
status=0
while (( status == 0 )); do
    (( i++ ))
    bash "$executable" >"$stdout_file" 2>"$stderr_file";
    status=$?
done

echo "Fallo de la ejecución número $i"
echo "--- Salida estándar ---"
cat "$stdout_file"
echo "--- Salida de error ---"
cat "$stderr_file"
