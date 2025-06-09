from abc import ABC,abstractmethod

class Person(ABC):

    @abstractmethod
    def __init__(self,nome:str,cognome:str,cf:str):
        self.setName(nome)
        self.setCognome(cognome)

    def setName(self,name:str):
        self._nome=name
    def getName(self)->str:
        return self._nome

    def setCognome(self,cogn:str):
        self._cognome=cogn
    def getCognome(self)->str:
        return self._cognome
    
    

    
