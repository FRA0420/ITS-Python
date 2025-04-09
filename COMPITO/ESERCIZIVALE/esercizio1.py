while True:
    numero:int=int(input("Inserisci un numero: "))
    if numero % 1 != 0:
        print("Errore inserisci un numero intero")
    else:
        break
asterisco:str=""
for n in range(numero):
    asterisco+="*"
    print(asterisco)

    
