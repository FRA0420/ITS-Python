#calcola la misura del cateto c in un triangolo rettagolo 
a:float=float(input("Inserisci l'ipotenusa a: "))
b:float=float(input("Inbserisci un cateto b: "))
c=0
if a > b:
    c:float=((a**2)-(b**2))**0.5 #formula per trovare cateto c 
else:
    print("Errore") #no sottrazione negativa
print(f"Il cateto c misura: {c:.3f}")