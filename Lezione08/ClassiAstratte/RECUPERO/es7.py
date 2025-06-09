class ContactManager():
    
    def __init__(self):
        self.contacts:dict[str,list[str]]={}

    def create_contact(self,name:str,phone_numbers:list[str])->dict:

        new_dict:dict[str,list[str]]={}

        if name and phone_numbers:
            if name in self.contacts:
                raise ValueError("Il contatto esiste già")
            else:
                self.contacts[name]=phone_numbers
                new_dict[name]=phone_numbers
        else:
            raise ValueError("I due campi sono obbligatori")
        
        return new_dict
    
    def add_phone_number(self,name:str,phone_number:list[str])->dict:
        new_dict:dict[str,list[str]]={}
        if name in self.contacts:
            if phone_number not in self.contacts[name]:
                self.contacts[name].append(phone_number)
                new_dict[name]=self.contacts[name]
            else:
                raise ValueError("Il numero di telefono esiste già")
        else:
            raise ValueError("Il contatto non esiste")
        
        return new_dict

    def remove_phone_number(self,contact_name:str,phone_numer:str)->dict:
        new_dict={}
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste")
        if phone_numer not in self.contacts[contact_name]:
            raise ValueError("Il numero di telefono non è presente")
        self.contacts[contact_name].remove(phone_numer)
        new_dict[contact_name]=self.contacts[contact_name]


    def update_phone_number(self,contact_name:str,old_phone_number:str,new_phone_number:str)->dict:
        new_dict:dict={}
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste")
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Il numero di telefono non è presente")
        if new_phone_number in self.contacts[contact_name]:
            raise ValueError("Il numero di telefono esiste già")
        self.contacts[contact_name].remove(old_phone_number)
        self.contacts[contact_name].append(new_phone_number)
        
        return new_dict
    
    def list_contacts(self)->list:
        return list(self.contacts.keys())
    
    def list_phone_number(self,contact_name:str)->list:
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non è presente")
        return self.contacts[contact_name]
        
    def search_contact_by_phone_number(self,phone_number:str)->list:
        new_list=list()
        for name,telefono in self.contacts.items():
            if phone_number in telefono:
                new_list.append(name)

        return new_list
      
            



        

                