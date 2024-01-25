#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE -> Código repetitivo toda esta configuração de logging
# TODO: usar função
# TODO: usa lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper() 

#nossa instancia 
log = logging.Logger("judce", log_level)

#level

#usaremos um ch - console handler
#ch = logging.StreamHandler() # como não especificamos, será o stde - standard error
                             # console/terminal/stderr
                             
#ch.setLevel(log_level)

fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=300, # 10**6
    backupCount=10,
    )
fh.setLevel(log_level)
#Formatação
#define a forma que será apresentada a nossa mensagem, ou seja, os parametros que a
#mesma utilizará

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

#ch.setFormatter(fmt)
fh.setFormatter(fmt)

#destino

#log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Mensagem pra o dev, sysadmin")
log.info("Mensagem geral para utilizadores")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral, ex: base de dados foi apagada")

print("-------------------")
"""
try:
    1/0
except ZeroDivisionError as zde:
    log.error("Deu erro %s", str(zde))