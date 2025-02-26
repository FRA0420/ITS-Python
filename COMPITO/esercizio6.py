n1:int = int(input("Inserisci un numero: "))
n2:int = int(input("Inserisci un altro numero: "))

prodotto = 1

if n1 > n2:
    print('n1 è maggiore')
    for n in range(n2, n1 +1):
        prodotto *= n
else:
    for n in range(n1, n2 +1):
        prodotto *= n

print(f"Il prodotto finale è: {prodotto}")