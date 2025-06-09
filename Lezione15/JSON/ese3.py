import json

PATH:str = "es3.json"
mode:str = "w"
diz3:dict = {}

with open(PATH,mode="r" ,encoding="utf-8") as file:

    diz3 = json.load(file)

diz3["RMG666"]["età"]=25

with open(PATH,mode=mode, encoding="utf-8") as file:

        json.dump(diz3,file,indent=4)