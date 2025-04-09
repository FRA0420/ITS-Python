def check_each(myList:list[int]):
    for item in myList:
        if item > 5:
            print(f"{item} è maggiore di 5!")
        elif item == 5:
            print(f"{item} è 5!")
        else:
            print(f"{item} è minore di 5")


myList:list[int]=[]
while True:
    number:int=int(input("Inserisci un numero, 0 per terminare: "))
    if number == 0:
        break
    myList.append(number)
check_each(myList)
