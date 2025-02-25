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
        animal_type = "unknown"
'''dict_animale_categoria:dict = {'Animale': animal_type,'Habitat': habitat}
animale_in_acqua:list[str]=["balena", "delfino", "tartaruga", "coccodrillo", pesci]
animale_terra:list[str]=[mammiferi[:-2], rettili[:2]]
animale_aria:list[str]=[uccelli[:4]]
for element in categorie_habitat:
    if element == "acqua":
        match animal_type:
            case animal_type if animal_type in animale_in_acqua:
                print("")'''
habitat:str=input(f"Inserire un habitat dove vive l'animale {animal_type}: ").lower()
if habitat in categorie_habitat:
    if habitat == categorie_habitat[0]:
        match animal_type:
            case animal_type if animal_type in pesci:
                print(f"L'animale {animal_type} ")
            



else:
    print("Habitat non valido")





     
    




