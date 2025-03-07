numero_massimo:float=float(input("Inserisci un numero: "))
count:int=1
while True:
    n:float=float(input("Inserisci numero: "))
    if n > numero_massimo:
        numero_massimo = n
    count += 1
    if count == 4:
        break 
print(f"Il numero massimo tra quelli inseriti è: {numero_massimo}")