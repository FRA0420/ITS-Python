# Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, 
# con lettere maiuscole e numeri.

# Esempio:

# text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
# find_codes(text)  # ['AB12CD34', '12345678']
import re

def find_codes(text):
    lista:list=re.findall(r'\b\w{8}\b',text)
    print(lista)

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678']
