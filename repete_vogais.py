#!/usr/bin/env python3

"""
                Repete Vogais
    
Faça um programa que pede ao utilizador que escreva uma ou mais palavras e imprima
cada uma das palavras com as suas vogais duplicadas.

ex:
    python3 repete_vogais.py
    'Escreva uma palavra (ou enter para sair):' Python
    'Escreva uma palavra (ou enter para sair):' Judce
    'Escreva uma palavra (ou enter para sair):' Clau

    ->Pythoon
    ->Juudcee
    ->Claauu

"""

vogais = ['a','e','i','o','u']

guarda_palavras = []
while True:  
    palavra = input("Escreva uma palavra (ou ENTER para sair): ").strip()
    if not palavra: # Condição de parada
        break
    nova_palavra = ""
    for letra in palavra:
        # TODO: Remover acentuação usando fuções
       # if letra.lower() in vogais: #ou if letra.lower() in "aeiouãêéíá"
           # nova_palavra += letra * 2
        #else:
           # nova_palavra += letra
     
        nova_palavra += letra * 2 if letra.lower() in vogais else letra        
            
    guarda_palavras.append(nova_palavra)


print("\n",*guarda_palavras, sep="\n")  # Jeito mais simples
       
