#!/usr/bin/env python3
"""Hello World Multilinguas.

De acordo a lingua selecionada no ambiente, o programa exibe a mensagem de "Olá, Mundo!" correspondente ao idioma

"""

__version__ = "0.1.0"
__author__ = "Judce Amaral"

import os

current_language = os.getenv("LANG", "C.UTF")[:5]



#ordem complexidade O(n)
"""
if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde"

"""

msg = {
    "C.UTF": "Hellooo, World!",
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "pt_PT": "Olá, Mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
