# Scrivi una funzione find_dates(text) 
# che trova tutte le date in formato italiano (dd/mm/yyyy) in un testo.
import re

def find_dates(text):
    date:list[str]=re.findall(r'((?:0[1-9]|1[0-9]|2[0-9]|3[0-1])/(?:0[1-9]|1[0-2])/(?:\d{4}))',text)
    print(date)

test = "Le date importanti sono 09/04/2025 e 15/08/2023 e 17/12/2023"
find_dates(test)  # ['09/04/2025', '15/08/2023']
