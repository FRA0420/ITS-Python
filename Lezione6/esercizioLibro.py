class Libro:

    def __init__(self):
        self.titolo:str=""
        self.autore:str=""
        self.genere:list[str]=[]

    def set_autore(self,nome_autore:str):
        self.autore=nome_autore
    
    def set_titolo(self,titolo_libro:str):
        self.titolo=titolo_libro

    def set_genere(self,lista_genere:list[str]):
        self.genere=lista_genere

    def get_autore(self)-> str:
        return self.autore
    
    def get_titolo(self)-> str:
        return self.titolo
    
    def get_genere(self)->list[str]:
        return self.genere
    
class Biblioteca:

    def __init__(self):
        self.libri:list[Libro]=[]

    def set_libro(self,libro:Libro):   
        self.libri.append(libro)

    def get_libri_titolo(self):
        for item in self.libri:
            print(item.get_titolo())
        
collezione:Biblioteca=Biblioteca()



piccolo_principe:Libro=Libro()
piccolo_principe.set_titolo("Piccolo Principe")
piccolo_principe.set_autore("AutorePiccoloPrincipe")
piccolo_principe.set_genere("Narrativa")


fm:Libro=Libro()
fm.set_titolo("Le avventure di Federico March")
fm.set_autore("Federico March")
fm.set_genere(["comico","avventura"])

collezione.set_libro(piccolo_principe)
collezione.set_libro(fm)

collezione.get_libri_titolo()

print("<----------->")

libro3:Libro=Libro()
libro3.set_titolo("Harry Potter")
libro3.set_autore("JK Rowling")
libro3.set_genere(["Fantasy"])

collezione.set_libro(libro3)
collezione.get_libri_titolo()



        
