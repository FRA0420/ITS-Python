def recursivePower(base:int,exponent:int) -> int:
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    if base and exponent == 0:
        return 1
    
    else:
        return int(base*recursivePower(base, exponent-1))
    
print(recursivePower(3,4))  

    
        