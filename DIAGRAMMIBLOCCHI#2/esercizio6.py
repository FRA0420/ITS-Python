x:int=int(input("Inserisci un valore positivo: "))
somma= 0
if x < 0 or x % 1 !=0:
    print("Errore! Valore inserito non valido")
else:
    for n in range(10):
        n:int=int(input("Inserisci un numero: "))
        if x % 2 == 0:
            if n > (x/2):
                somma += n
        else:
            if n < x:
                somma += n
            
print(f"La somma finale è: {somma}")
            


