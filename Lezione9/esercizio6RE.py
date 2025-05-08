# Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

import re

def check_product_code(code):
    valido=re.fullmatch(r'PROD-[0-9]{4}-[A-Z]{2}',code)
    if valido:
        return True
    else:
        return False
    
print(check_product_code("PROD-9876-ZX"))  # True
print(check_product_code("PROD-99-ZX"))