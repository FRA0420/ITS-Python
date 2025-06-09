# 2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
# classifichi i numeri in liste separate per numeri positivi e negativi.

def conv_dict(a:list[float])->dict:
    # mydict:dict[list]={}
    # lista_positivo:list=[]
    # lista_negativo:list=[]
    # for element in a:
    #     if element >= 0:
    #         lista_positivo.append(element)
    #     else:
    #         lista_negativo.append(element)

    # mydict["positivi"]=lista_positivo
    # mydict["negativi"]=lista_negativo
    # return mydict

    dict1:dict[str,list]={"positivi":[],"negativi":[]}
    for element in a:
        if element >= 0:
            dict1["positivi"].append(element)
        else:
            dict1["negativi"].append(element)
    return dict1

b:list[int]=[1,4,-17,8,-90,13,-24]
print(conv_dict(b))

    



        