corso:str=input("Ciao! Digita il nome del corso: ").title()
posti_liberi:int=100
while True:
    opzione:str=input("Cosa vuoi fare? (iscrivi,annulla,visualizza,elimina): ")
    match opzione:
        case "iscrivi":
            if posti_liberi > 0:
                posti_liberi -= 1 
        case "annulla":
            if posti_liberi < 100:
                posti_liberi += 1
        case "visualizza":
            print(f"I posti liberi nel corso {corso} sono: {posti_liberi}")
            print(f"I posti occupati nel corso {corso} sono: {100-posti_liberi}")
        case "elimina":
            print(f"Corso {corso} eliminato")
            posti_liberi = 100
            corso:str=input("Ciao! Digita il nome del corso: ").title()
        case "esci":
            break
        case _:
            print("Inserisci un'opzione valida")