def city_country(n:str,c:str):
    return(f"\"{n.title()},{c.title()}\"")
print(city_country(n=input("Inserisci una città "), c=input("Inserisci il Paese associato ")))
print(city_country(n="Roma",c="Italia"))
print(city_country("Parigi","Francia"))

    

