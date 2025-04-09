def recursiveFactorial(n:int)-> int:
    if n < 0:
        print("Errore")
    if n == 0 or n == 1:
        return 1
    else:
        return int(n*recursiveFactorial(n-1))
    
print(recursiveFactorial(8))
