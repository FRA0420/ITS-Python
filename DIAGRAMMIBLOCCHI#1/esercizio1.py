a:int=int(input("Inserisci l'ipotenusa a: "))
b:int=int(input("Inbserisci un cateto b: "))
c=0
if a > b:
    c=((a**2)-(b**2))**0.5
else:
    print("Errore")
print(f"Il cateto c misura: {c:.3f}")