numero_max:float=float(input("Inserisci un numero: "))
for n in range(3):
    n:float=float(input("Inserisci un numero: "))
    if n > numero_max:
        numero_max=n
print(f"Il numero maggiore è: {numero_max}")