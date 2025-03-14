n:float=float(input("Inserisci un valore intero positivo: "))
if n < 0 and n % 2 != 0:
    print("Errore! Numero inserito non valido")
    exit()
else:
    conteggio:int=0
    for element in range(3):
        x:float=float(input("Inserisci un numero intero: "))
        if x % 2 != 0:
            print("Errore inserisci numero intero")
        else:
            if x % n == 0:
                conteggio += 1
print(f"Il risultato del conteggio è: {conteggio}")