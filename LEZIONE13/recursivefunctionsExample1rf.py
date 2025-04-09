def recursiveSum(n:int)-> int:
    if n < 0:
        print("Errore numero negativo")
        return 0
    elif n == 0:
        return 0
    else:
        return int(n + recursiveSum(n-1))

print(recursiveSum(5))