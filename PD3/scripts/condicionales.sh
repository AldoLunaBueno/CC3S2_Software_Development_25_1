#!/usr/bin/env bash

# Determina si el argumento es un palabra de longitud par o impar
# Si no hay argumento, error
# Ejemplo de argumento: txt

# if
num=$1
if [[ -z $num ]]; then
    echo "Pasa un número"
    exit 1
elif (( ${#num} % 2 == 0 )); then
    echo "$num es de longitud par"
else
    echo "$num es de longitud impar"
fi

# case
ext="$1"
case "$ext" in
    txt) echo "Texto" ;;
    sh) echo "Shell" ;;
    py) echo "Python" ;;
    *) echo "Desconocido" ;;
esac


# Resumen de las expresiones condicionales en Bash

# -a file
# True if file exists.

# -b file
# True if file exists and is a block special file.

# -c file
# True if file exists and is a character special file.

# -d file
# True if file exists and is a directory.

# -e file
# True if file exists.

# -f file
# True if file exists and is a regular file.

# -g file
# True if file exists and its set-group-id bit is set.

# -h file
# True if file exists and is a symbolic link.

# -k file
# True if file exists and its "sticky" bit is set.

# -p file
# True if file exists and is a named pipe (FIFO).

# -r file
# True if file exists and is readable.

# -s file
# True if file exists and has a size greater than zero.

# -t fd
# True if file descriptor fd is open and refers to a terminal.

# -u file
# True if file exists and its set-user-id bit is set.

# -w file
# True if file exists and is writable.

# -x file
# True if file exists and is executable.

# -G file
# True if file exists and is owned by the effective group id.

# -L file
# True if file exists and is a symbolic link.

# -N file
# True if file exists and has been modified since it was last read.

# -O file
# True if file exists and is owned by the effective user id.

# -S file
# True if file exists and is a socket.

# file1 -ef file2
# True if file1 and file2 refer to the same device and inode numbers.

# file1 -nt file2
# True if file1 is newer (according to modification date) than file2, or if file1 exists and file2 does not.

# file1 -ot file2
# True if file1 is older than file2, or if file2 exists and file1 does not.

# -o optname
# True if the shell option optname is enabled. The list of options appears in the description of the -o option to the set builtin (see The Set Builtin).

# -v varname
# True if the shell variable varname is set (has been assigned a value).

# -R varname
# True if the shell variable varname is set and is a name reference.

# -z string
# True if the length of string is zero.

# -n string
# string
# True if the length of string is non-zero.

# string1 == string2
# string1 = string2
# True if the strings are equal. When used with the [[ command, this performs pattern matching as described above (see Conditional Constructs).

# ‘=’ should be used with the test command for POSIX conformance.

# string1 != string2
# True if the strings are not equal.

# string1 < string2
# True if string1 sorts before string2 lexicographically.

# string1 > string2
# True if string1 sorts after string2 lexicographically.

# arg1 OP arg2
# OP is one of ‘-eq’, ‘-ne’, ‘-lt’, ‘-le’, ‘-gt’, or ‘-ge’. These arithmetic binary operators return true if arg1 is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to arg2, respectively. Arg1 and arg2 may be positive or negative integers. When used with the [[ command, Arg1 and Arg2 are evaluated as arithmetic expressions (see Shell Arithmetic).