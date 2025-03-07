def sum(a:int,b:int):
    somma:int=0
    for i in range(a,b+1):
        somma+=i
    return somma

print(f"La somma dei numeri da 1 a 10 è: {sum(1,10)}")
print(f"La somma dei numeri da 20 a 37 è: {sum(20,37)}")
print(f"La somma dei numeri da 35 a 49 è: {sum(35,49)}")