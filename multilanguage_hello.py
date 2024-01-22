#!/usr/bin/env python3
"""Hello World Multilinguas.

De acordo a lingua selecionada no ambiente, o programa exibe a mensagem de "Olá, Mundo!" correspondente ao idioma

Ou informe atraves do CLI 
"""

__version__ = "0.1.2"
__author__ = "Judce Amaral"

import os
import sys

#print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    #TODO Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip() #O último strip() serve para retirar o espaço em branco de uma frase
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:") #Para o caso de apagarmos a variavek de ambiente LANG

current_language = current_language[:5]

msg = {
    "C.UTF": "Hellooo, World!",
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "pt_PT": "Olá, Mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))
