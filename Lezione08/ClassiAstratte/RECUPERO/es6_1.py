class ContactManager():

    def __init__(self):
        self.contacts:dict[str,list[str]]={}


    def create_contact(self,name:str,phone_numbers:list[str])->dict[str,list[str]]:
        
        if type(phone_numbers) != list:
            raise ValueError("Errore")

        if name in self.contacts:
            raise ValueError("Errore.Il contatto esiste già")
        else:
            self.contacts[name]=phone_numbers
            

        return {name:phone_numbers}
    

    def add_phone_number(self,contact_name:str,phone_number:str)->dict:
        
        if contact_name not in self.contacts:
            raise ValueError("Errore il contatto non esiste")
        else:
            if phone_number not in self.contacts[contact_name]:
                self.contacts[contact_name].append(phone_number)
    
            else:
                raise ValueError("Il telefono è già inserito")

        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self,contact_name:str,phone_number:str)->dict:
        new_dict:dict[str,list[str]]={}
        if contact_name not in self.contacts:
            raise ValueError("Errore il contatto non esiste")
        else:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                new_dict[contact_name]=self.contacts[contact_name]
            else:
                raise ValueError("Il telefono non esiste")
        return new_dict
    
    def update_phone_number(self,contact_name:str,old_phone_number:str,new_phone_number:str)->dict:
        new_dict:dict[str,list[str]]={}
        if contact_name not in self.contacts:
            raise ValueError("Errore il contatto non esiste")

        else:
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)
                new_dict[contact_name]=self.contacts[contact_name]
            else:
                raise ValueError("Il numero non è presente")

    def list_contacts(self)->list[str]:
        return list(self.contacts.keys())
    
    def list_phone_numbers(self,contact_name:str)->list:
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            raise ValueError("Il contatto non è presente")
        
    def search_contact_by_phone_number(self,phone_number:str)->dict:
        new_list:list=[]
        for chiave,telefono in self.contacts.items():
            if phone_number in telefono:
                new_list.append(chiave)
            else:
                raise ValueError("Nessun contatto trovato con questo numero di telefono")
            
        if not new_list:
            raise ValueError("Errore! La lista è vuota")
        
        return new_list


    def __str__(self)->str:
        return f"{self.contacts.keys()} e {self.contacts.values()}"
    

if __name__ == '__main__':

    rubrica:ContactManager=ContactManager()

    rubrica.create_contact(name="Chiara",phone_numbers=["3344778899"])
    print(rubrica.contacts)
    rubrica.create_contact(name="Leo",phone_numbers=["3344778899"])
    rubrica.create_contact(name="Giulia",phone_numbers=["3344778899"])
    rubrica.add_phone_number(contact_name="Chiara",phone_number="1122334455")
    rubrica.add_phone_number(contact_name="Leo",phone_number="1122334455")
    rubrica.add_phone_number(contact_name="Giulia",phone_number="1122334455")
    rubrica.add_phone_number(contact_name="Chiara",phone_number="9988776655")
    rubrica.add_phone_number(contact_name="Leo",phone_number="9988776655")
    rubrica.add_phone_number(contact_name="Giulia",phone_number="9988776655")


