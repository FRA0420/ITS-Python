class Media:
    
    #attributi della classe Media:
    #self.title:str
    #self.year:int

    #inizializzare __init__ i metodi setter e getter
    def __init__(self,title:str,year:int)->None:
        self.set_title(title)
        self.set_year(year)
    
    #metodi setter

    def set_title(self,title:str)->None:
        if title:
            self.title=title
        else:
            print("Errore")
    
    def set_year(self,year:int)->None:
        if year > 1900:
            self.year=year
        else:
            print("Errore")
    
    #metodi getter
    def get_title(self)->str:
        return self.title
    def get_year(self)->int:
        return self.year
    
    def __str__(self)->str:
        return f"Titolo: {self.get_title()}\nAnno di uscita: {self.get_year()}"
    
