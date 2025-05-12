# stdout a archivo
ls -l > listado.txt

# stderr
grep f1 *.log 2> errores.log

# ambos
make &> build.log

# pipe
ps aux | grep sshd | awk '{print $2}'
# si quieramos redirigirlo a un archivo:
# ps aux | grep sshd | awk '{print $2}' > archivo.txt

# process substitution
diff <(sort file1) <(sort file2)
