#!/usr/bin/env python3

""" For loop 
dados = {}

for line in open("blog.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()
    
print(dados)

"""

original = [1, 2, 3]

dobro = []
#Abordagem de programação imperativa
for n in original:
    dobro.append(n * 2)
print("Dobro Imperativo -> ",dobro)

#Abordagem Funcional seria:
#Usando "List Comprehension" (sempre irá geral uma lista)
#Se o objetivo for só dar um print na tela, ela não será uma boa abordagem
dobro = [n * 2 for n in original]
print("Dobro Funcional -> ",dobro)

#print(([n * 2 for n in original])) meu teste, funcionou