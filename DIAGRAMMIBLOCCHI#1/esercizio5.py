#numero primo
n:int=int(input("Inserisci un numero: "))
primo = True
if n % 1 !=0 or n <= 0:
    print("Errore! Il numero non è intero o positivo")
    exit()
if n == 1 or n == 2:
    print(f"{n} è un numero primo!")
    exit()
div = 2 
while True:
    if div == n:
        primo = True
        break
    elif n % div == 0:
            primo = False
            break
    
    else:
        div += 1

'''while True:
    if div <= (n**0.5):
        if n % div == 0:
            primo = True
            break
        else:
            div += 1 
    else:
        primo = False
        break'''

if primo == True:
    print(f"{n} è un numero primo")
else:
    print(f"{n} non è un numero primo")

