numero:float = float(input("Inserisci un numero: "))
somma = 0 
count = 0 
numero_max = numero
numero_min = numero
if numero < 0:
     exit()
if numero.is_integer():
     somma += numero
     count += 1

while True:
    numero:float = float(input("Inserisci un numero: "))
    media = 0

    if numero < 0:
        break

    if numero.is_integer():
        count += 1 
        somma += numero
        
         
    if numero > numero_max:
        numero_max = numero
    if numero < numero_min:
            numero_min = numero

    
media = somma/count
print(f"La media dei numeri interi è {media}")
print(f"Il numero maggiore è {numero_max}, il numero minore è {numero_min}")
    

    