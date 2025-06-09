# Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
# restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
# con i prezzi aumentati del 10% e arrotondati a due cifre decimali.

def products(mydict:dict[str,float])->dict:
    nuovo_dict:dict[str,int]={}
    for k,v in mydict.items():
        if v < 50:
            v1=round(v+(v*0.1),2)
            nuovo_dict[k]=v1
        else:
            continue
    return nuovo_dict

dizio:dict[str,int]={"acqua":34,"pane":22.5,"carne":51}
print(products(dizio))