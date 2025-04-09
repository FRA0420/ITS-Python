class Animal:
    def __init__(self,name:str,legs:int)->None:
        self.name=name
        self.legs=legs
    def printInfo(self):
        print(f"Animale:{self.name.title()}\nLegs:{self.legs}")
    def setLegs(self,legs:int):
        self.legs=legs
    def getLegs(self):
        return self.legs
gatto=Animal("cat",4)
print(gatto.name)
gatto.printInfo()
cane=Animal("cane",4)
print(cane.name)
cane.legs=8
print(f"Il cane ha: {cane.legs} zampe")
gatto.setLegs(6)
print(gatto.legs)
print(cane.getLegs())
print(gatto.getLegs())
cane.printInfo()

   
    
    
