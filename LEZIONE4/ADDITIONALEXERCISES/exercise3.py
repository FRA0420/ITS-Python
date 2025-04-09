
def print_numbers(myList:list[int]):
    for item in myList:
        print(item)
myList:list[int]=[]
while True:
    number:int=int(input("Inserisci un numero, 0 per terminare: "))
    if number == 0:
        break
    myList.append(number)
print_numbers(myList)
    
