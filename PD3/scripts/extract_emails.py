#!/usr/bin/env python3
import re, sys
texto=sys.stdin.read() # Para finalizar lectura: Enter, Ctrl+D
pat=re.compile(r'([A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+)')
for email in set(pat.findall(texto)):
    print(email)

# Posible uso:
# cat logs.txt | python3 extract_emails.py