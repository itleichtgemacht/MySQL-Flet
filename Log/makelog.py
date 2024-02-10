import logging
# ### AH
# https://codegree.de/python-logging/
#
# logging stellt mehrere Funktionen bereit, um Meldungen auszugeben. 
# Diese unterscheiden sich nach ihrem Level. Standardmäßig gibt es die Level:
#     - debug
#     - info
#     - warning 
#     - error
#     - critical
#
# Beispiele:
#   logging.info(f'teile {dividend} durch {divisor}')
#   logging.debug('debug')
#   logging.info('info')
#   logging.warning('warning')
#   logging.error('error')
#   logging.critical('critical')
#
# Standardmäßig werden nur die Nachrichten von warning, error und critical ausgegeben wurden.
#
# logging.basicConfig(level=logging.DEBUG)
# DEBUG:root:debug
# INFO:root:info
# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical
# ###

logging.basicConfig(
    filename='Log\\debug.log', 
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%d.%m.%y %H:%M:%S',
    level=logging.DEBUG,
)


