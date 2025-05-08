# 2. Trova tutte le email in un testo

# Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.
import re
def extract_emails(stringa:str):
    result:list[str] = re.findall(r'\S+@\S+', stringa)
    print(result)
    

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)

