posti_liberi=20
while True:
    opzione:str=input("Cosa vuoi fare? (prenota,libera,visualizza,esci) ")
    match opzione:
        case "prenota":
            if posti_liberi > 0:
                posti_liberi -= 1 
            else:
                print("Non ci sono più posti liberi")
                
        case "libera":
            if posti_liberi == 20:
                print("Non ci sono posti da liberare")
                
            else:
                posti_liberi += 1 
        case "visualizza":
            posti_occupati=20-posti_liberi
            print(f"I posti liberi sono: {posti_liberi} mentre i posti occupati sono: {posti_occupati}")
        case "esci":
            break
        case _:
            print("Inserisci un comando valido")
