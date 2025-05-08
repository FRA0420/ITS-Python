def create_contact(nome:str,email:str=None,telefono:int=None)->dict:
    dizio={}
    if nome not in dizio:
        dizio["profile"]=nome
    if email not in dizio:
        dizio["email"]=email

    if telefono not in dizio:
        dizio["telefono"]=telefono
    return dizio

def update_contact(diz:dict, nome:str, email:str=None,telefono:int=None)->dict:
    if diz["profile"]==nome:
        for chiave,valore in diz.items():
            if diz["email"] == "" and email != None:
                diz["email"]=email
            if diz["email"] != "" and email != None:
                diz["email"] = email
            if  diz["telefono"] ==None and telefono != None:
                diz["telefono"]=telefono
            if diz["telefono"] !=None and telefono != None:
                diz["telefono"] = telefono
            if diz["telefono"] != None and telefono == None:
                continue
    return diz

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))

contact = create_contact("Laura Neri", email="laura.neri@domain.com")
print(create_contact("Laura Neri", email="laura.neri@domain.com"))
print(update_contact(contact, "Laura Neri", email="laura.new@domain.com", telefono=84736736))


