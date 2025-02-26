frase:str=input("frase: ")
lunghezza=len(frase)
match frase:
    case frase if frase[-1] == "?" and lunghezza %2 == 0:
        print("Si")
    case frase if frase[-1] == "?" and lunghezza % 2 != 0:
        print("No")
    case frase if frase[-1] == "!":
        print("Wow!")
    case _:
        print(f"Tu dici \"{frase}\"")
    
