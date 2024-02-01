#!/usr/bin/env python3
import os
import sys

#EAFP - Easy to Ask Forgiveness than permission
#(É mais fácil pedir perdão do que permissão)



try:
    names = open("names.txt").readlines()
except FileNotFoundError as fnfe: # capturando a exception
    print(f"{str(fnfe)}.") # tratando a exception
    sys.exit(1)
else:
    print("Sucesso!!") # Executa apenas quando não há exception
finally:
    print("Execute isso sempre!") # Executa sempre, mesmo que ocorra exception
    
     