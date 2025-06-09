import json

# PATH: str = "config.json"
# mode: str = "r"

# with open(PATH, mode=mode) as file:

#     config:dict = json.load(file)

#     print(config)

#     nome_applicazione:str = config["chiave"]

#     print(nome_applicazione)

########################################################################################################

# PATH: str = "config_1.json"
# mode: str = "w"

# with open(PATH,mode=mode) as file:
#     nuovo_diz:dict = {"nome":"2048","versione":"1.2.3.4","OS":"Android 16.1.0"}
#     json.dump(nuovo_diz,file,indent=4)


#####################################################################################


PATH: str = "config.json"
mode: str = "w"
config:dict = {}

with open(PATH, mode="r") as file:  
    
    config = json.load(file)

config["chiave"] = 33

with open(PATH, mode=mode) as file:
#questo mode=mode sta per mode="w"
    

    json.dump(config,file, indent=4)