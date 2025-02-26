count:int = 4
numeri:list[int] = []

while count >= 0:
    n:int = int(input("Inserisci un numero: "))
    if n >= 1 and n <= 30:
        count -= 1
        numeri.append(n)
    else:
        print("Inserisci numero compreso tra 1 e 30")
    
print(f"\nI numeri da te inseriti sono: {numeri}\n")

for element in numeri:
    stringa:str = ''
    for a in range(1,element+1):
        stringa += '*'
    print(stringa)
