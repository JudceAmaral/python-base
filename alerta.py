#!/usr/bin/env python3

"""
        Alarme de temperatura
        
Faça um script que pergunte ao utilizador qual a temperatura atual
o indice de humidade do ar, será exibida uma mensagem de alerta 
dependendo das condições seguintes:

    temp maior que 45: ALERTA!!! Perigo de calor extremo
    tem vezes 3 for maior ou igual a humidade: ALERTA!!! Perigo de calor húmido
    temp entre 10 e 30: Normal
    temp < 0: ALERTA: Frio extremo

"""
import sys
import logging

log = logging.Logger("Alerta")


info = {
    "temperatura": None,
    "humidade": None
}
while True:
    # condicao de parada
    # o dicionário está completamente preenchido
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break # para o while
    
    for key in info.keys():     # ["temperatura", "humidade"]
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, insira os números", key)
            break # para o for
        
       
temp, humidade = info.values() # unpacking [30, 90]
print(temp, humidade) 
if temp > 45:
    print("ALERTA!!! 🔥 Perigo Calor extremo")
elif temp > 30 and temp * 3 >= humidade:
    print("ALERTA!!! 🔥❄️ perigo de calor húmido")
elif temp >= 10 and temp <= 30:
    print("Temperatura Normal 👌")
elif temp >= 0 and temp <= 10:
    print("Frio ⛄")
elif temp < 0:
    print("ALERTA!!! ❄️⛄ Frio extremo.")