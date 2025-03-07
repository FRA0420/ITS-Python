def make_album(name:str,album:str,songs=None):
    albumDict:dict={}
    if songs == None:
         albumDict:dict[str,str]={"Nome":name,"Album":album}
    else:
        albumDict:dict[str,str,int]={"Nome":name,"Album":album,"Songs":songs}
    return albumDict
    
    
print(make_album("Achille Lauro","Ragazzi Madre"))
print(make_album("Tedua","Divina Commedia", 8))
        