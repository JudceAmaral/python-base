#!/usr/bin/env python3


import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do ficheiro de emails\n")
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]
    
path = os.curdir
filepath = os.path.join(path, filename)   # email.txt
templatepath = os.path.join(path, templatename)  # email_tmpl.txt

clientes = []
for line in open(filepath):
    name, email = line.split(",")
    #TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        %{
            "nome": name,
            "produto": "caneta",
            "texto": "Escreve mto bem",
            "link": "http//canetas.com",
            "quantidade": 1,
            "preco": 50.5,
            "email": email,
        }
    )
    print("-" * 50)