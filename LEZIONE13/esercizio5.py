def recursiveArmonic(n:int)->float:
    if n % 1 !=0 or n <= 0:
        print("Errore!")
        exit()
    if n == 1:
        return 1
    else:
        return round((1/n)*recursiveArmonic(n-1),6)
print(recursiveArmonic(6))
