giorno:int=int(input("Inserisci un giorno: "))

mese:int=int(input("Inserisci un mese, espresso numericamente: "))

data:tuple=(giorno,mese)

if mese <= 12 and mese >0 and giorno > 0 and giorno <=31:

    match data:
        case (1,1):
            print(f"Il {giorno}\\{mese} è Capodanno!")
        case (14,2):
            print(f"Il {giorno}\\{mese} è San Valentino")
        case (2,6):
            print(f"Il {giorno}\\{mese} è la Festa della Repubblica")
        case (15,8):
            print(f"Il {giorno}\\{mese} è Ferragosto")
        case (31,10):
            print(f"Il {giorno}\\{mese} è Halloween")
        case (25,12):
            print(f"Il {giorno}\\{mese} è Natale")
        case _:
            print("Nessuna festività importante in questa data")

else:
    print("Data non valida")