class Persona:
    
    def __init__(self,name:str,cognome:str,age:int):
        self.setName(name)
        self.setCognome(cognome)
        self.setAge(age)
    
    def setName(self,name):
        if name:
            self.name=name
        else:
            print("Errore il valore nome non può essere vuoto")
    
    def setCognome(self,cognome):
        if cognome:
            self.cognome=cognome
        else:
            print("Errore il valore cognome non può essere vuoto")
    
    def setAge(self,age):
        if age < 0 or age > 130:
            self.age=0
        else:
            self.age = age
    
    def getName(self):
        return self.name
    
    def getCognome(self):
        return self.cognome
    
    def getAge(self):
        return self.age
    
    def __str__(self):
        return f"\nCiao! Sono {self.name} {self.cognome}. Ho {self.age} anni\n"
    
    def speak(self):
        print(f"\nHello! My name is {self.getName()}\n")

# chiara=Persona("Chiara","Macciocchi",26)
# print(chiara) 
    
