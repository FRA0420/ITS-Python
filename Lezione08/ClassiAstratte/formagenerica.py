from abc import ABC,abstractmethod
#abc=abstractBaseClass
class FormaGenerica(ABC):

    @abstractmethod
    def draw(self)->None:
        pass

        
    def setShape(self, shape:str)->None:
        if shape:
            self.shape = shape
        else:
            print("Errore, il valore shape non può essere una stringa vuota")

    def getShape(self)->str:
        return self.shape

