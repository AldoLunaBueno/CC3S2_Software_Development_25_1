#!/usr/bin/env bash
email="$1"
re='^([[:alnum:]_.+-]+)@([[:alnum:]-]+\.[[:alnum:].-]+)$'
if [[ $email =~ $re ]]; then
  echo "Email válido"
  echo "Usuario: ${BASH_REMATCH[1]}"  # primer grupo
  echo "Dominio: ${BASH_REMATCH[2]}" # segundo grupo
else
  echo "Email inválido"
fi

# METHACHARACTERS

# ^ (caret): Matches the start of a string.
# $ (dollar): Matches the end of a string.
# . (dot): Matches any single character except a newline character.
# [] (square brackets): Defines a character class, matching any one character within the brackets.
# {} (curly brackets): Specifies a specific quantity of characters to match.
# - (hyphen): Specifies a range of characters when used within square brackets.
# ? (question mark): Makes the preceding character optional, matching zero or one occurrence.
# * (asterisk): Matches zero or more occurrences of the preceding character.
# + (plus): Matches one or more occurrences of the preceding character.
# () (parentheses): Groups expressions together.
# | (pipe): Indicates an OR condition between two expressions.
# \ (backslash): Escapes a metacharacter, allowing it to be matched as a literal character.


# CLASS CHARACTERS -> [[:WORD:]]

# [:alnum:]
# Alphanumeric characters: [:alpha:] and [:digit:]; in the C locale and ASCII character encoding, this is the same as [0-9A-Za-z].

# [:alpha:]
# Alphabetic characters: [:lower:] and [:upper:]; in the C locale and ASCII character encoding, this is the same as [A-Za-z].

# [:blank:]
# Blank characters: space and tab.

# [:cntrl:]
# Control characters. In ASCII, these characters have octal codes 000 through 037, and 177 (DEL). In other character sets, these are the equivalent characters, if any.

# [:digit:]
# Digits: 0 1 2 3 4 5 6 7 8 9.

# [:graph:]
# Graphical characters: [:alnum:] and [:punct:].

# [:lower:]
# Lower-case letters; in the C locale and ASCII character encoding, this is a b c d e f g h i j k l m n o p q r s t u v w x y z.

# [:print:]
# Printable characters: [:alnum:], [:punct:], and space.

# [:punct:]
# Punctuation characters; in the C locale and ASCII character encoding, this is ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~.

# [:space:]
# Space characters: in the C locale, this is tab, newline, vertical tab, form feed, carriage return, and space. See Usage, for more discussion of matching newlines.

# [:upper:]
# Upper-case letters: in the C locale and ASCII character encoding, this is A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.

# [:xdigit:]
# Hexadecimal digits: 0 1 2 3 4 5 6 7 8 9 A B C D E F a b c d e f.