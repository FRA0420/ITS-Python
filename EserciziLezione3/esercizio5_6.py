age: int = int(input("Quale è la tua età? "))

'''if age <= 2:
    print("Sei un bambino!")

elif age > 2 and age < 4:
    print("Sei un todd!")

elif'''

match age:

    case age if age <= 2:
        print("Sei un bambino!")
    case age if age > 2 and age < 4:
        print("Sei un todd!")
    case age if age >= 4 and age < 13:
        print("Sei un ragazzino")
    case age if age >=13 and age < 20:
        print("sei un teenager")
    case age if age >= 20 and age < 65:
        print("Sei un adulto :(")
    case age if age >65:
        print("Sei vecchio,Robert")
