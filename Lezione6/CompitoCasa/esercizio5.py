def filtra_e_mappa(dizio:dict)->dict:
    nuovo_dizio={}
    nuovo_prezzo=0
    for prodotto,prezzo in dizio.items():
        if prezzo > 20:
            nuovo_prezzo=(prezzo-(prezzo*0.10))
            if prodotto not in nuovo_dizio:
                nuovo_dizio[prodotto]=nuovo_prezzo
        else:
            continue
    return nuovo_dizio

print(filtra_e_mappa({"Gomma":50.0,"Matita":1.0}))

