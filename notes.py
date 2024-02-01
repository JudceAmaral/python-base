#!/usr/bin/env python3
"""
Bloco de notas
    $ notes.py new "Minha Nota"
                    tag: tech
                    text: Anotação geral sobre a carreira de tecnologia
                    
    chamada:
        $notes.py read --tag=tech
...
...
    Vão existir dois subcomandos: new ou read

"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds} ")
    sys.exit()
    
if arguments[0] not in cmds:
    print(f"Invalid command `{arguments[0]}`")

while True:
     
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag? : ").strip().lower()
        #   Leitura das notas
        for line in open(filepath):
            title, tag, text = line.split("\t")
            #if tag.lower() == arguments[1].lower():
            if tag.lower() == arg_tag:
                print(f"Title: {title}\n")
                print(f"Text: {text}\n")
                print("-" * 30)
                print()
    
        
    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("Qual é o título? : ").strip().title()
        #   Escrita das notas
        #title = arguments[1]   # Havia um todo aqui
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
        # \t - tsv
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
            
    cont = input(f"Prentende continuar a {arguments[0]} notas? [N/y] : ").strip().lower()
    if cont != "y": 
        break