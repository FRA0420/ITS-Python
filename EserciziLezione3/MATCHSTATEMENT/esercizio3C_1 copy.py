voto:int = int(input("Che voto hai preso da 1 a 10? "))

match voto:
    case 10:
        print("Eccellente!")
    case 8|9:
        print("Molto buono!")
    case 6|7:
        print("Sufficiente")
    case 4|5:
        print("Insufficiente")
    case voto if voto <=3 and voto >=1:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")

        
