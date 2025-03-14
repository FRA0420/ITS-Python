while True:
    n:int=int(input("Inserisci un numero intero positivo: "))
    if n % 1 == 0 and n > 0:
        break
    else:
        print("Errore inserisci un numero intero positivo")
fattoriale = 1
count=1
while count <= n:
        fattoriale *= count
        count += 1 

print(f"Il fattoriale di {n} è {fattoriale}")