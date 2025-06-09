# crea un file json usando i comandi touch, e nano. Leggete il file appena creato e stampate un valore

# crea un file json da python salvando un dizionario a vostra scelta

#crea un file json, usando touch e nano, che contiene codici fiscali come chiavi 
# e come valori dizionari che contengono nome, cognome ed età della
#persona (almeno 2) e poi modificate il json aggiungengo una persona. 

import json

PATH:str = "es2.json"
mode:str = "w"

with open(PATH,mode=mode) as file:  
    config:dict = {"Nome":"RPMGym","Versione":"Beta","Creator":"Valerion"}
    json.dump(config,file,indent=4)


