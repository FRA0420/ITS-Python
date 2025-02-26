parole:list[str] = []

while True:

    parola:str = input("inserisci una parola (o 'fine' per terminare) " )
    if parola.lower() == "fine":
        break
    parole.append(parola)
    
    if parola[0] == parola[-1]:
        print(f"Il primo e l'ultimo carattere della parola {parola} sono uguali")
        
    
    
    
