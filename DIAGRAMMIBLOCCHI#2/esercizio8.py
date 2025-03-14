A:float=float(input("Inserisci un valore intero positivo: "))
B:float=float(input("Inserisci un altro valore intero positivo: "))
if A and B < 0 and A and B % 2 !=0:
    print("Errore condizioni non rispettate")
    exit()
else:
    somma = 0 
    count = A
    while count <= B:
        somma += count
        count +=1 
print(f"La somma è: {somma}")



