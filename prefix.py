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
import logging
from logging import handlers

# BOILERPLATE -> Código repetitivo toda esta configuração de logging
# TODO: usar função
# TODO: usa lib (loguru)

#log_level = os.getenv("LOG_LEVEL", "WARNING").upper() 

#nossa instancia 
log = logging.Logger(__name__, logging.ERROR)



fh = handlers.RotatingFileHandler(
    "relatory_prefix.log", 
    maxBytes=300, # 10**6
    backupCount=10,
    )
fh.setLevel(logging.ERROR)


fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)


fh.setFormatter(fmt)

log.addHandler(fh)





operacoes = {
    "sum",
    "sub",
    "mul",
    "div",
}

#print(f"{sys.argv=}")
while True:
    arguments = sys.argv[1:]
    #   Validação
    if not arguments:
        op = input("Operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [op, n1, n2]
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("Ex: `sum 5 5`")
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

    try:
        n1, n2 = validated_nums
    except ValueError as ve:
        print(str(ve))
        sys.exit(1)
        
        
    #   TODO: Usar dict de funcoes
    if op == "sum":
        result = n1 + n2
    elif op == "sub":
        result = n1 - n2
    elif op == "mul":
        result = n1 * n2
    elif op == "div":
        result = n1 / n2
        
    print(f"O resultado é {result}")
    
    path = os.curdir
    filepath = os.path.join(path, "prefix.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'Anonymous')



    try:
        with open(filepath, "a") as file_:
            file_.write(f"{op},{n1},{n2} = {result}  | by: {user} at {timestamp}\n")
    except PermissionError as pe:
        # TODO: Logging
        log.error("Falha por: %s", pe)
        sys.exit(1)
    
    if input("Pressione ENTER para efetuar outra operação\n OU pressione qualquer outra tecla para sair: "):
       break