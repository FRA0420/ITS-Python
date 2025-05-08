from media import Media

class Movie(Media):

    #attributi della superclass
    #self.title:str
    #self.year:int

#attributi della classe movie sono:
#self.durata:int

#inizializzare un oggetto della classe Movie
    def __init__(self,title:str,year:int,durata:int)->None:
        #inizializzare la superclasse richiamando il metodo init della superclasse Media
        super().__init__(title,year)

        self.setDurata(durata)

    #metodi setter
    def setDurata(self,durata:int)->None:
        if durata >= 0:
            self.durata=durata
        else:
            print("Errore")
    #metodi getter
    def getDurata(self)->int:
        return self.durata

    #concetto overriding->ovvero nella classe film Movie ridefinire il metodo __str__
    def __str__(self)->str:
        return f"{super.__str__()}\nDurata: {self.getDurata()}"
    


#da scrivere dentro un codice test.py
#film:Movie=Movie(....)
#isIstance(film1,Movie)->True
#isIstance(film,Media)->True

