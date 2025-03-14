età:int=int(input("Inserisci la tua età: "))
if età >= 18 and età <= 65:
    print("Puoi partecipare all'attività")
else:
    if età < 18:
        print("Non hai raggiunto l'età minima per la partecipazione")
    if età > 65:
        print("Hai superato l'età massima consentita per l'attività")
