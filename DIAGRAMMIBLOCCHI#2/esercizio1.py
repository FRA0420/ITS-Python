max_posti:int=int(input("Inserisci quanti posti massimi ha il parcheggio: "))
posti_liberi:int=max_posti

while True:
    opzione:str=input("Cosa vuoi fare? (ingresso,uscita,stato,esci): ")
    match opzione:
        case "ingresso":
            if posti_liberi > 0:
                posti_liberi -= 1 
            else:
                print("Non ci sono posti liberi")                
        case "uscita":
            if posti_liberi <= max_posti:
                posti_liberi += 1
            else:
                print("Non ci sono posti da liberare") 
        case "stato":
            print(f"I posti liberi sono: {posti_liberi}")
            print(f"I posti occupati sono: {max_posti-posti_liberi}")
        case "esci":
            break
        case _:
            print("Inserisci un comando valido")
