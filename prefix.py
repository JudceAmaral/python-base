#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operacao] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefix.py sum 5 2
7

$ prefix.py mul 10 5
50

.
.
.
etc

Nova versão:
Os resultados das operações serão salvos em `prefix.log`

"""

__version__ = "0.1.0"

import os
import sys
from datetime import datetime
arguments = sys.argv[1:]

operacoes = {
    "sum",
    "sub",
    "mul",
    "div",
}

#print(f"{sys.argv=}")
    
#   TODO: Exceptions
if not arguments:
    op = input("Operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [op, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválido")
    print("EX: `sum 5 5")
    sys.exit(1)
    
op, *nums = arguments

#valid_op = operacoes
if op not in operacoes:
    print("Operação inválida")
    print(f"Escolha entre: {operacoes}")
    sys.exit(2)
    
validated_nums = []
for num in nums:
    # TODO: Repetição while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido `{num}`")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
    
n1, n2 = validated_nums

#   TODO: Usar dict de funcoes
if op == "sum":
    result = n1 + n2
elif op == "sub":
    result = n1 - n2
elif op == "mul":
    result = n1 * n2
elif op == "div":
    result = n1 / n2
    
path = os.curdir
filepath = os.path.join(path, "prefix.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'Anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{op},{n1},{n2} = {result}  | by: {user} at {timestamp}\n")
    
print(f"O resultado é {result}")