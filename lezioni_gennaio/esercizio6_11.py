roma:dict={"country":"italia", "population": 6000000 , "zona":"centro"}
napoli:dict= {"country":"italia", "population": 800000 , "zona": "sud"}
firenze:dict={"country":"italia", "population": 800000 , "zona": "nord"}

cities:dict={roma:"bella", napoli:"caotica" , firenze: "top"}

for i in cities:
    print(f"{i.title()}: ")
    for k,v in cities[i].items():
        print(f"{k.title()}-->{v}")
              