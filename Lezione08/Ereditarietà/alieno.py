class Alieno:
    #di un alieno ci interessa sapere la galassia di appartenenza
    def __init__(self,galaxy:str):
        self.setGalaxy(galaxy)

    def setGalaxy(self,galaxy:str):
        if galaxy:
            self.galaxy=galaxy
        else:
            print("Errore galaxy non può essere una stringa vuota")
    
    def getGalaxy(self)->str:
        return self.galaxy
    
    def speak(self)->None:
        print("hxshxoscosw")

    def __str__(self)->str:
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}"
    
