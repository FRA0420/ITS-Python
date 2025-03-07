def check_value(num:int):
    if num > 5:
        print(f"{num} è maggiore di 5!")
    elif num < 5:
        print(f"{num} è minore di 5!")
    else:
        print(f"{num} è 5!")

check_value(int(input("Inserisci un numero: ")))