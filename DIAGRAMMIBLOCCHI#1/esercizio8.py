soglia:float=float(input("Inserisci un valore soglia: "))
count = 0
while count < 7:
    n:float=float(input("Inserisci un numero: "))
    if n > soglia:
        print(f"{n} è maggiore di {soglia}")
        count += 1 
    elif n == soglia:
        print(f"{n} è uguale a {soglia}")
    else:
        print(f"{n} non è maggiore di {soglia}")
        count += 1