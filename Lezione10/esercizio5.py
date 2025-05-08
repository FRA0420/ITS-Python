def integerPower(base:int,espo:int):
    potenza=1
    # if base == int and (espo == int and espo != 0):
    for n in range(espo):
        potenza*= base            
    return potenza
	
print(integerPower(3, 4))