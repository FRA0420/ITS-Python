animal:str=input("Inserisci un nome di un animale: ").lower()
mammiferi:list[str]=["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list[str]=["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list[str]=["aquila", "pappagallo", "gufo","falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list[str]=["squalo","trota","salmone","carpa"]
categorie_habitat:list[str]=["acqua", "aria", "terra"]
habitat:str=input("Inserire un habitat per il tuo animale: ").lower()
animal_type:str = ''
if habitat not in categorie_habitat:
    print("Habitat non valido")
match animal:
    case animal if animal in mammiferi:
        print(f"{animal} appartiene alla categoria dei Mammiferi!")
        animal_type = animal
    case animal if animal in rettili:
        print(f"{animal} appartiene alla categoria dei Rettili!")
        animal_type = animal
    case animal if animal in uccelli:
        print(f"{animal} appartiene alla categoria degli Uccelli!")
        animal_type = animal
    case animal if animal in pesci:
        print(f"{animal} appartiene alla categoria dei Pesci!")
        animal_type = animal
    case _:
        print(f"Mi dispiace non sono in grado di classificare {animal}")
        animal_type = animal

    
match habitat:
    case habitat if habitat in categorie_habitat and habitat == categorie_habitat[0]:
        match animal_type:
            case animal_type if animal_type in mammiferi and animal_type in mammiferi[0:5]:
                print(f"L'animale {animal_type} non può vivere in {categorie_habitat[0]}!")
            case animal_type if animal_type in mammiferi and animal_type in mammiferi[5:7]:
                print(f"L'animale {animal_type} può vivere in {categorie_habitat[0]}!")
            case animal_type if animal_type in pesci:
                print(f"L'animale {animal_type} può vivere in {categorie_habitat[0]}!")
            case animal_type if animal_type in uccelli[0:4]:
                print(f"L'animale {animal_type} non può vivere in {categorie_habitat[0]}!")
            case animal_type if animal_type in uccelli[6:8]:
                print(f"L'animale {animal_type} non può vivere in {categorie_habitat[0]}!")
            case animal_type if animal_type in uccelli[4:6]:
                print(f"L'animale {animal_type} non vive ma sta anche in {categorie_habitat[0]}!")
            case animal_type if animal_type in rettili[0:2]:
                print(f"L'animale {animal_type} non può vivere in {categorie_habitat[0]}!")
            case animal_type if animal_type in rettili[2:4]:
                print(f"L'animale {animal_type} può vivere anche in {categorie_habitat[0]}!")
            case _:
                print(f"Mi dispiace non so se {animal_type} vive nell'{categorie_habitat[0]}")
    case habitat if habitat in categorie_habitat and habitat == categorie_habitat[1]:
        match animal_type:
            case animal_type if animal_type in mammiferi:
                print(f"L'animale {animal_type} non può volare!")
            case animal_type if animal_type in rettili:
                print(f"L'animale {animal_type} non può volare!")
            case animal_type if animal_type in pesci:
                print(f"L'animale {animal_type} non può volare!")
            case animal_type if animal_type in uccelli[0:4]:
                print(f"L'animale {animal_type} vola, quindi vive in {categorie_habitat[1]}")
            case animal_type if animal_type in uccelli[4:6]:
                print(f"L'animale {animal_type} può volare ma male quindi non vive in {categorie_habitat[1]}")
            case animal_type if animal_type in uccelli[6:8]:
                print(f"L'animale {animal_type} non sa volare sigh, non vive in {categorie_habitat[1]}")
            case _:
                print(f"Mi dispiace non so se {animal_type} vive nell'{categorie_habitat[1]}")
    case habitat if habitat in categorie_habitat and habitat == categorie_habitat[2]:
        match animal_type:
            case animal_type if animal_type in mammiferi[0:5]:
                print(f"L'animale {animal_type} vive sulla {categorie_habitat[2]}!")
            case animal_type if animal_type in mammiferi[5:7]:
                print(f"L'animale {animal_type} non può vivere sulla {categorie_habitat[2]}!")
            case animal_type if animal_type in pesci:
                print(f"L'animale {animal_type} non può vivere sulla {categorie_habitat[2]}!")
            case animal_type if animal_type in uccelli[0:4]:
                print(f"L'animale {animal_type} di solito non vive sulla {categorie_habitat[0]}")
            case animal_type if animal_type in uccelli[4:6]:
                print(f"L'animale {animal_type} può vivere anche sulla {categorie_habitat[2]}!")
            case animal_type if animal_type in uccelli[6:8]:
                print(f"L'animale {animal_type} vive sulla {categorie_habitat[2]}!")
            case animal_type if animal_type in rettili[0:2]:
                print(f"L'animale {animal_type} vive sulla {categorie_habitat[2]}!")
            case animal_type if animal_type in rettili[2:4]:
                print(f"L'animale {animal_type} può vivere anche sulla {categorie_habitat[2]}!")
            case _:
                print(f"Mi dispiace non so se {animal_type} vive sulla {categorie_habitat[2]}")
    case _:
        print(f"Mi dispiace non ho informazione sull'habitat {habitat}")

            




            



                


            

            
        
        

            
            
                









     
    




