cities:dict[str]={
    "Roma":{
        "Monument": "Colosseo", 
        "Abitanti": 6000000, 
        "Paese": "Italia"
        },
    "Londra": {
        "Monument": "LondonEye", 
        "Abitanti": 30000000, 
        "Paese": "Inghilterra"
        }, 
    "Edimburgo": {
        "Monumet":"Castello", 
        "Abitanti": 10000000, 
        "Paese": "Scozia"}
                }
for k,v in cities.items():
    print(f"{k.title()}:")
    for keys, values in v.items():
        print(f"{keys.title()} ---> {values}")

    
        




