def add_one(intero:int):
    intero+=1
    return(intero)
number:int=int(input("Inserisci un numero: "))
print(add_one(number))
def add_one_to_list(num_list:list[int]):
    new_list:list[int]=[]
    for element in num_list:
        new_list.append(add_one(element))
    print(new_list)


myList:list[int]=[]
while True:
    number:int=int(input("Inserisci un numero, 0 per terminare: "))
    if number == 0:
        break
    else:
        myList.append(number)
add_one_to_list(myList)