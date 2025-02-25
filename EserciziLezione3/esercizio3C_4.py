animal:str=input("Inserisci un nome di un animale: ").lower()
mammiferi:list[str]=["cane", "gatto", "cavallo", "elefante", "leone"]
rettili:list[str]=["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list[str]=["aquila", "pappagallo", "gufo","falco"]
pesci:list[str]=["squalo","trota","salmone","carpa"]

match animal:
    case animal if animal in mammiferi:
        print(f"{animal} appartiene alla categoria dei Mammiferi!")
    case animal if animal in rettili:
        print(f"{animal} appartiene alla categoria dei Rettili!")
    case animal if animal in uccelli:
        print(f"{animal} appartiene alla categoria degli Uccelli!")
    case animal if animal in pesci:
        print(f"{animal} appartiene alla categoria dei Pesci!")
    case _:
        print(f"Mi dispiace non sono in grado di classificare {animal}")

