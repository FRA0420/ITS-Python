def make_album(name:str,album:str,songs=None):
    albumDict:dict={}
    if songs == None:
         albumDict:dict[str,str]={"Nome":name.title(),"Album":album.title()}
    else:
        albumDict:dict[str,str,int]={"Nome":name.title(),"Album":album.title(),"Songs":songs}
    return albumDict

#albumDict:dict={}
while True:
    scelta=input("Vuoi inserire informazioni su un album? ")
    if scelta == "no":
        print("Non ho album su cui dare informazioni")
        break
    if scelta == "si":
        name:str=input("Inserisci un nome di un'artista ")
        album:str=input("Inserisci il nome di un suo album ")
        songs:str=input("Sai quante canzoni sono? ")
        if songs == "si":
            s:int=int(input("Quante canzoni sono? "))
            print(make_album(name,album,s))
            break
        if songs == "no":
            print(make_album(name,album))
            break
    
