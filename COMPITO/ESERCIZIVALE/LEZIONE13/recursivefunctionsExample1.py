def sum(n:int) -> int:
    somma:int=0
    if n <0:
        print("Errore numero negativo")
        return None
    else:
        while n >=0:
            somma += n
            n -= 1
        return int(somma)  #return sum as int
print(sum(5))
print(sum(-5))
