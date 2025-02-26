person:dict={"Nome": None , "Ruolo": None, "Età": None}
person["Nome"]=input("Inserisci il tuo nome: ").title()
person["Ruolo"]=input("Inserisci il tuo ruolo: ").title()
person["Età"]=int(input("Inserisci la tua età: "))

if person['Età'] <18:
    print("Attenzione! Utente minorenne. Accesso limitato! Alcune funzionalità sono bloccate")
else:
    match person:
        case {"Nome": name, "Ruolo": "Admin", "Età": età}:
            print(f"Benvenuto Admin {person['Nome']}! Hai accesso completo a tutte le funzionalità")
        case {"Nome": name, "Ruolo": "Moderatore", "Età": età}:
            print(f"Benvenuto {person['Nome']}, puoi gestire i contenuti ma non modificare le impostazioni")
        case {"Nome": name, "Ruolo": "Ospite", "Età": età}:
            print(f"Benvenuto ospite {person['Nome']}, hai accesso ristretto alle funzionalità! Solo visualizzazione dei contenuti")
        case _:
            print("Attenzione ruolo non riconosciuto")
