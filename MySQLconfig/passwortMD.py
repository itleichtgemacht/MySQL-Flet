# ### AH
# Text (Passwort) verschlüsseln mit Benutzereingabe
# ---
# py-Package:  [shell] pipenv install pybase64 
# Hilfe unter: https://www.pythonhelp.org/tutorials/how-to-install-base64/
# ###

import base64

message = 'Tester12345#'
message = input('Welcher Text soll verschlüsselt werden? ')

print('Folgender Text wird verschlüsselt: ', message)
message_bytes = message.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf-8')

print('Passwort wurde verschlüsselt: ', base64_message)

decoded_bytes = base64.b64decode(base64_bytes)
decoded_message = decoded_bytes.decode('utf-8')

print('Passwort wurde wieder entschlüsselt: ', decoded_message)


