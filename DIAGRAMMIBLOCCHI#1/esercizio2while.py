max_numero:float=float(input("Inserisci un numero: "))
count:int=1
while count < 4:
    n:float=float(input("Inserisci un numero: "))
    if n > max_numero:
        max_numero=n
        count+=1
    else:
        count+=1
print(f"Il numero massimo inserito è: {max_numero}")
