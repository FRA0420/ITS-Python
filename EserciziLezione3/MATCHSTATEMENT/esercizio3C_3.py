oggetti:list[str] = []
n = 0
while n <= 2:
    i:str = (input("Che oggetti vuoi inserire? "))
    oggetti.append(i)
    n+=1
print(oggetti)    

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("dispositivi elettronici")
    case _:
        print("categoria sconosciuta")