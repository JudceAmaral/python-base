#!/usr/bin/env python3
"""Hello World Multilinguas.

De acordo a lingua selecionada no ambiente, o programa exibe a mensagem de "Olá, Mundo!" correspondente ao idioma

Ou informe atraves do CLI 
"""

__version__ = "0.1.2"
__author__ = "Judce Amaral"

import os
import sys
import logging


# BOILERPLATE -> Código repetitivo toda esta configuração de logging
# TODO: usar função
# TODO: usa lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper() 

#nossa instancia 
log = logging.Logger("judce", log_level)

#level

#usaremos um ch - console handler
ch = logging.StreamHandler() # como não especificamos, será o stde - standard error
ch.setLevel(log_level)

#Formatação
#define a forma que será apresentada a nossa mensagem, ou seja, os parametros que a
#mesma utilizará

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

ch.setFormatter(fmt)

#destino

log.addHandler(ch)









#print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as ve:
        log.error(
            "You writed: %s, You must use `=`, try --key=value: %s", arg, str(ve)
        )
        sys.exit(1)
    
    key = key.lstrip("-").strip() #O último strip() serve para retirar o espaço em branco de uma frase
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
#print(f"{current_language=}") era para fazer DEBUG
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

"""
#O dicionario já é uma estrutura de dados que permite tratar determinados
#comportamentos inesperados, sem que seja necessário reportar erro

É basicamente um try com valor default

message = msg.get(current_language, msg["en_US"])

"""

#EAFP
try:
    message = msg[current_language]
except KeyError as ke:
    print(f"[ERROR]: {str(ke)} is a invalid value, try: {list(msg.keys())} instead")
    sys.exit(1)
print(message * int(arguments["count"]))
