#!/usr/bin/env python3

import logging

#nossa instancia 
log = logging.Logger("judce", logging.DEBUG)

#level

#usaremos um ch - console handler
ch = logging.StreamHandler() # como não especificamos, será o stde - standard error
ch.setLevel(logging.DEBUG)

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

log.debug("Mensagem pra o dev, sysadmin")
log.info("Mensagem geral para utilizadores")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral, ex: base de dados foi apagada")

print("-------------------")

try:
    1/0
except ZeroDivisionError as zde:
    log.error("Deu erro %s", str(zde))