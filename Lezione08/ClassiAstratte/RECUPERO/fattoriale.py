def fattoriale(n:int)->int:
    # fact:int = 1
    # count:int=1
    # while count <= n:
    #     fact *= count
    #     count += 1 
    # return fact
    fact:int=1
    for i in range(n):
        fact *= n - i
    return fact

print(fattoriale(100))

