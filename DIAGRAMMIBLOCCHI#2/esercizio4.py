tutor_disponibili:int=2
lista_attesa:int=0
while True:
    studente:str=input("Chi sei? ")
    if tutor_disponibili > 0:
        tutor_disponibili -= 1 
    else:
        lista_attesa +=1
    if lista_attesa == 2 and tutor_disponibili == 0:
        break

  