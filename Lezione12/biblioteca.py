
# Sistema di Gestione Biblioteca
# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
# Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, 
# restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. 
# Il libro deve essere inizialmente disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#     Metodi della classe:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. 
#     Restituisce un messaggio di conferma.

#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. 
#     Restituisce un messaggio di stato.

#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. 
#     Restituisce un messaggio di stato.

#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
#     Se non ci sono libri disponibili, restituisce un messaggio di errore.

# Codice Driver

#     Aggiungi libri alla biblioteca.
#     Presta e restituisci libri, gestendo anche casi limite (già prestato, doppia restituzione, libro inesistente).
#     Mostra i libri disponibili in ogni fase.
#     Visualizza lo stato finale di ogni libro.
class Libro:
    def __init__(self,titolo:str,autore:str):
        self.titolo=titolo
        self.autore=autore
        self.stato_prestito=False

class Biblioteca:
    
    def __init__(self):
        self.libri:list[Libro]=[]
    
    def aggiungi_libro(self,libro:Libro):
        if libro not in self.libri:
            self.libri.append(libro)
            return f"Il libro {libro.titolo} è stato aggiunto alla libreria."
    
    def presta_libro(self,titolo:Libro):
        for libro in self.libri:
            if libro.titolo == titolo:
                if libro.stato_prestito == False:
                    return f"Il libro {libro.titolo} attualmente non è disponibile"
                else:
                    libro.stato_prestito = True
                    return f"Il libro {libro.titolo} è disponibile per il prestito"
            else:
                return f"Il libro {libro.titolo} non è presente in biblioteca"
    def restituisci_libro(self,titolo:Libro):
        for libro in self.libri:
            if libro.titolo == titolo:
                if libro.stato_prestito == True:
                    libro.stato_prestito = False
                    return f"Libro {libro.titolo} è stato restituito"
                else:
                    return f"Libro {libro.titolo} non è stato preso in prestito"
            else:
                return f"Il libro {libro.titolo} non è presente in biblioteca"
    
    def mostra_libri_disponibili(self):
        disponibili=[]
        for libro in self.libri:
            if libro.stato_prestito == True:
                disponibili.append(libro)
            else:
                continue
        if disponibili == []:
            return "Errore non ci sono libri disponibili"
        else:
            return disponibili

        
                
                    
                
    
