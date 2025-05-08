def rimuovi_elementi(lista:list[int],dizio:dict[int])->list:
    lista_elementi=lista.copy()
    rimasti=0
    for k,v in dizio.items():
        rimasti = v
        while k in lista_elementi and rimasti > 0:
            lista_elementi.remove(k)
            rimasti-=1
    return lista_elementi

print(rimuovi_elementi([1,2,3,2,4],{2:2}))
print(rimuovi_elementi([],{2:1}))