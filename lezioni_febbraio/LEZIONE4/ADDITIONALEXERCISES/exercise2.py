def check_lenght(stringa:str):
    print(len(stringa))
    if len(stringa) > 10:
        print(f"La stringa {stringa} è lunga più di 10 caratteri")
    elif len(stringa) == 10:
        print(f"La stringa {stringa} è lunga 10 caratteri")
    else:
        print(f"La stringa {stringa} è lunga meno di 10 caratteri")
check_lenght(input("Inserisci una stringa: "))


