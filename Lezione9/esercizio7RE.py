# Scrivi una funzione is_valid_name(name) che controlla se la stringa inizia con una lettera maiuscola seguita da almeno due lettere minuscole.

# Esempio:

# is_valid_name("Marco")    # True
# is_valid_name("marco")    # False
# is_valid_name("Ma")       # False

import re

def is_valid_name(name):
    valido=re.fullmatch(r'[A-Z]{1}[a-z]{2,}',name)
    if valido:
        return True
    else:
        return False
    
print(is_valid_name("Marco"))    # True
print(is_valid_name("marco"))    # False
print(is_valid_name("Ma"))
