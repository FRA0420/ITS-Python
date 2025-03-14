count=0
pari = 0
dispari = 0
while count <= 9:
    n:int=int(input("Inserisci un numero intero: "))
    if n % 1 !=0:
        print("Errore inserisci un numero intero")
    else:
        if n % 2 == 0:
            pari += 1
            count +=1
        else:
            dispari +=1
            count +=1
print(f"Il numero di numeri pari inseriti è {pari} mentre i dispari sono {dispari}")

        