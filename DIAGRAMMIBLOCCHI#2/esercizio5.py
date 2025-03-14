n:int=int(input("Insersci un numero intero positivo: "))
if n < 0 or n % 1 !=0:
    print("Errore! Il numero inserito non è valido")
    exit()
else:
    somma = 0
    count = 1
    while count <= n:
        somma += count**2
        count += 1
    print(f"La somma dei quadrati del numero {n} è: {somma}")



