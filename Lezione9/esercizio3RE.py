# Scrivi una funzione mask_numbers(text) che sostituisce tutte le sequenze di cifre con ###.
import re

def mask_numbers(text:str):
    result:str=re.sub(r'\d+',"###",text)
    print(result)

test = "Il codice è 12345 e la data è 2025."
mask_numbers(test)  # "Il codice è ### e la data è ###."