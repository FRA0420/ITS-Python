def ricerca_binaria(lista:list[int],n:int)->bool:
    inizio=0
    fine=len(lista)-1

    while inizio <= fine:
        centro = (inizio+fine) // 2

        if lista[centro] == n:
            return True
        
        elif lista[centro] < n:
            inizio = centro +1
            
        else:
            fine = centro -1
    
    return False

        

print(ricerca_binaria([1,2,3,5,7],5))
