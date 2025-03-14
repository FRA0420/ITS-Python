somma:float=0
count:int=0
while True:
    n:float= float(input("Inserisci un numero: "))
    if n <=0:
        count+=1
    else:
        somma+=n
        count+=1
    if count == 5:
        break
print(f"La somma dei valori positivi inseriti è: {somma}")