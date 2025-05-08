# 1. Verifica se una stringa è un numero intero

# Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), 
# False altrimenti.

import re


def is_integer(stringa:str)->bool:
    integer:str=re.fullmatch(r"-?\d+",stringa)
    if integer != None:
        return True
    else:
        return False
    
        
print(is_integer("blablabla"))
print(is_integer("12"))
print(is_integer("-12.4"))
