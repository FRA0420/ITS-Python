somma = 0 
contatore_voti=0
while True:
    domanda:str=input("Vuoi inserire un voto? (si o no): ").upper()
    if domanda == "SI":
        voto:int=int(input("Inserisci un voto positivo: "))
        if voto < 0 or voto > 30:
            print("Errore! Inserisci un voto valido")
        else:
            somma += voto
            contatore_voti +=1
    if domanda == "NO":
        break
print(somma)
print(contatore_voti)
if somma > 0 and contatore_voti > 0:
    media_voti=somma/contatore_voti
    print(f"La media dei voti inseriti è: {media_voti}")
else:
    print("Non posso calcolare la media perchè non hai inserito voti")
