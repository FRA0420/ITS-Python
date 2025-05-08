def trova_chiave_per_valore(dizio:dict,valore):
    
    for k in dizio.keys():
        if dizio[k] == valore:
            return k
        else:
            continue
    if valore not in dizio:
        return None
print(trova_chiave_per_valore({'a':100,'b':200,'c':300},200))
