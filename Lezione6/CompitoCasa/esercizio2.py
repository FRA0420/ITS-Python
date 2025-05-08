def somma_condizionale(lista:list[int])->int:
    lista_numeri=lista.copy()
    lista_somma=[]
    somma=0

    for numero in lista_numeri:
        if numero % 2 == 0 and numero % 3 == 0:
            lista_somma.append(numero)
    for numeri in lista_somma:
        somma+=numeri
    return somma
    

print(somma_condizionale([1,2,3,6,12]))
print(somma_condizionale([5,7,11]))