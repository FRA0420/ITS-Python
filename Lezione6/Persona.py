class Persona:
    #costruttore
    def __init__(self,name:str,lastname:str,age:int) -> None:
        self.name=name
        self.lastname=lastname
        self.age=age

    def __str__(self) -> str:

        return f"Nome:{self.name}\nCognome:{self.lastname}\nEtà:{self.age}"

Chiara = Persona("Chiara","Cognome",26)
print(Chiara)
