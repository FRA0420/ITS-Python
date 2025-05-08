def aggrega_voti(voti:list[dict])->dict:
    nuovo_dict={}
    lista_voti=voti.copy()
    for element in lista_voti:
        nome = element["nome"]
        voto = element["voto"]
        if nome not in nuovo_dict:
            nuovo_dict[nome]=[]
        nuovo_dict[nome].append(voto)
    return nuovo_dict

