#!/usr/bin/env python3

"""
Faça um programa de terminal que exibe ao utilizador uma lista de quartos
disponiveis para arrendar e o preço de cada quarto. Esta informação está
disponivel em um ficheiro de texto separado por virgulas.

O programa pergunta ao utlizador o seu nome, qual o número do quarto que 
pretende reservar e o total de dias que deseja, no final exibe o valor
estimado a ser pago.

O programa deve também salvar esta operação em outro ficheiro contendo as 
reservas, de nome `reservas.txt`

ex:     
            Judce,1,5
            
Se outro utilizador tentar reservar o memso quarto, o programa deve exibir
uma mensagem informando que tal quarto já está reservado.

"""

import sys
import os
import logging

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Ficheiro `reservas.txt`não existente")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Ficheiro `quartos.txt`não existente")
    sys.exit(1)
    
    
print("Reserva Hotel Pythonic")
print("-" * 40)

    
print("Lista de quartos:")
for codigo, dados in quartos.items():
    nome = dados["nome"]
    preco = dados["preco"]
    disponivel = "⛔" if not dados['disponivel'] else "👍"
    #disponivel = dados['disponivel] and "👍" or "⛔" -> Esta é outra maneira de fazer
    # TODO: Substituir casa decimal por virgula
    print(f"{codigo} - {nome} - $ {preco:.2f} - {disponivel}")

if len(ocupados) == len(quartos):
    print("\nHotel Lotado ⛔\n")
    sys.exit()   
        
print("-" * 40)
nome = input("Nome do cliente: ").strip()
try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Opção de quarto inválida, escreva apenas digitos")
    sys.exit(1)
except KeyError:
    logging.error("O quarto número %d não existe", num_quarto)
    sys.exit(1)
    
try:
    dias = int(input("Quantos dias pretende ficar?: ").strip())
except ValueError:
    logging.error("Número inválido, escreva apenas digitos.")
    sys.exit(1)
    
nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")
    
print(f"\nBem vindo {nome}, está a reservar o quarto '{nome_quarto}' "
       f"que ficará a um total de {total}$")