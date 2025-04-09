def sumInRange(a:int,b:int)-> int:
    #la mia condizione è che b sia più grande di a 
    if a > b:
        #per scambiarli aggiungo una variabile temporanea
        temp:int=a
        #scambio i valori 
        a = b
        b = temp  #mi ospita il valore originale di a perchè lo perdo mettendolo come b
    #devo fare la somma
    somma:int=0
    while b>=a:
        somma += b
        b -= 1 
    return int(somma)
print(sumInRange(5,10))
print(sumInRange(10,5))


