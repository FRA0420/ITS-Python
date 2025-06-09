def convert(a:list[tuple])->dict:
    # mydict:dict={}
    # for chiave,valore in a:
    #     if chiave in mydict:
    #         mydict[chiave]+=valore
    #     else:
    #         mydict[chiave]=valore
    # return mydict
    
    
    dict_1:dict={}
    
    for element in a:

        chiave,valore=element[0],element[1]

        if chiave in dict_1:
            
            dict_1[chiave]+=valore

        else:

            dict_1[chiave]=valore

    return dict_1




lista:list[tuple]=[('a',1),('b',8)]
convert(lista)
print(convert(lista))