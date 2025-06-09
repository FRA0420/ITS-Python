import json 

PATH:str = "new.json"
mode="r"

with open(PATH,mode=mode) as file:
    config:dict = json.load(file)

    print(config)

    new_valore:str=config["chiave"]
    print(new_valore)