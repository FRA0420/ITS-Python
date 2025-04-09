class Persona:
    def __init__(self,name:str,cognome:str,age:int):
        self.name=name
        self.cognome=cognome
        self.age=age
    def setName(self,name):
        self.name=name
    def setCognome(self,cognome):
        self.cognome=cognome
    def setAge(self,age):
        self.age=age
    def getName(self):
        return self.name
    def getCognome(self):
        return self.cognome
    def getAge(self):
        return self.age
    def __str__(self):
        return f"Ciao! Sono {self.name} {self.cognome}. Ho {self.age} anni"
chiara=Persona("Chiara","Macciocchi",26)
print(chiara) 
    
