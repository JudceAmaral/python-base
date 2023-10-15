#!/usr/bin/env python3
""" Hello World multilanguage

According to default language of the  system, the program should 
show the equivalent language 

Usage: get LANG variable previously configured

Execution: python3 thistime.py

"""
#Metadados
__version__ = "0.0.1"
__author__ = "Judce Amaral"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_PT":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"



print(msg) 
