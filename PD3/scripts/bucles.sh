#!usr/bin/env bash

# bucles

# for clásico
for (( i=1; i<=3; i++ )); do
    echo "Iter $i";
done

# for-in
for file in *.sh; do
    echo "Script: ${file%.sh}";
done

# while
count=3
while (( count>0 )); do
    echo "$count";
    (( count-- ));
done

# until
echo "Crea un archivo resultado.txt para que el programa termine"
until [[ -f resultado.txt ]]; do 
    sleep 1;
done
echo "resultado.txt listo"