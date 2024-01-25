#!/usr/bin/env python3

import logging

logging.debug("Mensagem pra o dev, sysadmin")
logging.info("Mensagem geral para utilizadores")
logging.warning("Aviso que não causa erro")
logging.error("Erro que afeta uma única execução")
logging.critical("Erro geral, ex: base de dados foi apagada")

print("-------------------")

try:
    1/0
except ZeroDivisionError as zde:
    logging.error("Deu erro %s", str(zde))