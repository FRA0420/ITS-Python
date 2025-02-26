animal:str=input("Inserisci un nome di un animale: ").lower()
mammiferi:list[str]=["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list[str]=["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list[str]=["aquila", "pappagallo", "gufo","falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list[str]=["squalo","trota","salmone","carpa"]
categorie_habitat:list[str]=["acqua", "aria", "terra"]
habitat:str=input("Inserire un habitat per il tuo animale: ").lower()
animal_type:str = ''
if habitat not in categorie_habitat:
    print(f"Non sono riuscito a classificare {habitat} come habitat per {animal}")
    exit()
match animal:
    case animal if animal in mammiferi:
        print(f"{animal} appartiene alla categoria dei Mammiferi!")
        animal_type = "mammifero"
    case animal if animal in rettili:
        print(f"{animal} appartiene alla categoria dei Rettili!")
        animal_type = "rettile"
    case animal if animal in uccelli:
        print(f"{animal} appartiene alla categoria degli Uccelli!")
        animal_type = "uccello"
    case animal if animal in pesci:
        print(f"{animal} appartiene alla categoria dei Pesci!")
        animal_type = "pesce"
    case _:
        print(f"Mi dispiace non sono in grado di classificare {animal}")
        animal_type = "unknown"


mydict:dict={"Animale": animal , "Categoria_animale": animal_type , "Habitat": habitat}

match mydict:
    case {"Animale": animal, "Categoria_animale": "pesce", "Habitat": "acqua"}:
        print(f"{animal} vive in {habitat}")
    case {"Animale": "delfino"|"balena", "Categoria_animale": "mammifero", "Habitat": "acqua"}:
        print(f"{animal} vive in {habitat}")
    case {"Animale": "tartaruga"|"coccodrillo", "Categoria_animale": "rettile", "Habitat": "acqua"}:
        print(f"{animal} può vivere anche in {habitat}")
    case {"Animale": "cigno"|"anatra", "Categoria_animale": "uccello", "Habitat": "acqua"}:
        print(f"{animal} si può trovare anche in {habitat}")
    case {"Animale": "tartaruga"|"coccodrillo", "Categoria_animale": "rettile", "Habitat": "terra"}:
        print(f"{animal} può vivere anche sulla {habitat}")
    case {"Animale": "anatra"|"cigno", "Categoria_animale": "uccello", "Habitat": "terra"}:
        print(f"{animal} vive sulla {habitat}")
    case {"Animale": "balena"|"delfino", "Categoria_animale": "mammifero", "Habitat": "terra"|"aria"}:
        print(f"{animal} non può vivere nell'habitat {habitat}")
    case {"Animale": animal, "Categoria_animale": "mammifero"|"pesce"|"rettile", "Habitat": "aria"}:
        print(f"{animal} non può vivere in {habitat}")
    case {"Animale": animal , "Categoria_animale": "mammifero"|"rettile", "Habitat": "terra"}:
        print(f"{animal} vive sulla {habitat}")
    case {"Animale": "tacchino"|"gallina" , "Categoria_animale": "uccello", "Habitat": "aria"}:
        print(f"{animal} non può vivere in {habitat}")
    case {"Animale": "anatra"|"cigno" , "Categoria_animale": "uccello", "Habitat": "aria"}:
        print(f"{animal} vola poco, il suo habitat non è l'{habitat}")
    case {"Animale": animal, "Categoria_animale": "uccello", "Habitat": "aria"}:
        print(f"{animal} vive in  {habitat}")
    case {"Animale": animal , "Categoria_animale": "unknown", "Habitat": habitat}:
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}")
    case {"Animale": animal , "Categoria_animale": "uccello"|"mammifero", "Habitat": "acqua"}:
        print(f"{animal} non può vivere in {habitat}")
    case _:
        print(f"Non sono riuscito a trovare un'habitat per {animal}")



    








