# Sistema di Gestione Catalogo Film 

# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
# rimuovere e cercare film di un particolare regista. 
# Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

# Classe:
# - MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

#     Metodi della classe:
#     - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
#     Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

#     - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
#     Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#     - list_directors(): Elenca tutti i registi presenti nel catalogo.

#     - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
#     Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore 
#     se nessun film contiene la parola cercata nel titolo.


class MovieCatalog:

#attributi della classe MovieCatalog
#self.catalog:dict[str,list[str]]

#init ci permette di inizializzare degli oggetti della classe MovieCatalog
    def __init__(self)->None:
        self.setCatalog()

    #metodi getter
    
    #metodo che ritorna il valore dell'attributo self.catalog
    def getCatalog(self)->dict[str,list[str]]:
        return self.catalog

    #metodi setter

    #metodo che consente di inizializzare l'attributo self.catalog
    def setCatalog(self)->None:
        self.catalog:dict[str,list[str]]={}

    #metodo stringer per visualizzare i dettagli del catalogo
    def __str__(self)->str:
        string:str="Catalogo:"
        if self.catalog:
            for key,values in self.catalog.items():
                temp_string:str="\n" + str(key)+": "+ str(values)
                string= string + temp_string

        return string
    
    #medodi della classe MovieCatalog

    #metodo che aggiunge una lista di film di uno specifico regista al catalogo
    def add_movies(self,director_name:str,movies:list[str])->None:
        #check se il regista non è valido
        if not director_name:
            print("Il regista non è valido")
        #check se la lista non è valida
        elif not movies:
            print("La lista dei film non può essere vuota")
        #se i dati sono balidi
        else:

            #se il regista è presente nel catalogo
            if director_name in self.catalog:

                #aggiungere la lista movies al catalogo
                for movie in movies:
                    #controllare che se il film movie sia stato già aggiunto al catalogo
                    #director_name è la chiave del dizionario che rappresenza il nome di un regista
                    #a questa chiave corrisponde una lista di film ovvero i film prodotti dal regista in questione
                    #self.catalog[director_name]? -> è il valore associato alla chiave director_name 
                    #ovvero è la lista di tutti i film prodotti dal regista
                    if movie in self.catalog[director_name]:
                        print(f"Il film {movie} è già presente nel catalogo")
                    
                    #se il film non è presente
                    else:

                        #aggiungere il film al catalogo
                        self.catalog[director_name].append(movie)
            #se il regista non è presente nel catalogo
            else:
                #creare un nuovo recordo
                self.catalog[director_name]=movies
    
    #metodo che rimuove un film dalla lista dei film prodotti da un regista
    def remove_movie(self,director_name:str,movie:str)->None:
        #check se il regista non è valido
        if not director_name:
            print("Il regista non è valido")
        #check se la lista non è valida
        elif not movie:
            print("Il film non è valido")
        #se i dati sono validi
        else:

            #vedo se il regista è presente nel catalogo
            #se è presente, faccio un check se il film è nella lista dei film prodotti dal regista in questione
            if director_name in self.catalog and movie in self.catalog[director_name]:
                self.catalog[director_name].remove(movie)
            
            #verifico se la lista dei film è vuota
            if not self.catalog[director_name]:
                #rimuovere il recordo
                del self.catalog[director_name]
    
    #metodo che ritorna una lista contenente i nomi di tutti i registi del catalogo
    def list_directors(self)->list[str]|str:
        #controllare se il dizionario self.catalog
        if self.catalog:
            return list(self.catalog.keys())
               
        #se il dizionario è vuoto
        else:
            return "Non ci sono registi nel catalogo perchè il catalogo è vuoto"
        
    #metodo che dato il nome del regista, restituisce tutti i film da esso prodotti
    def get_movies_by_director(self,director_name:str)->list[str]|str:
        if not director_name:
            print("Il regista non è valido")
        else:
            
            #controllo se il regista è nel catalogo
            if director_name in self.catalog:
                return self.catalog[director_name]
            #se il regista non è nel catalogo
            else:
                return f"Il regista {director_name} non è nel catalogo"
            
    def search_movies_by_title(self, title:str)->dict[str,list[str]]:
        title = title.lower()
        risultati= {}
        for director,films in self.catalog.items():
            trovati = []
            for film in films:
                if title in film.lower():
                    trovati.append(film)

            if trovati:
                risultati[director] = trovati
            if not risultati:
                return f"Nessun film trovato contentente la parola '{title}'"
        
            return risultati
        
    # Test MovieCatalog
catalog = MovieCatalog()

print(catalog.add_movies("Christopher Nolan", ["Inception", "Interstellar"]))
print(catalog.add_movies("Quentin Tarantino", ["Pulp Fiction", "Django Unchained"]))
print(catalog.add_movies("Christopher Nolan", ["Tenet", "Inception"]))  # evita duplicati

print(catalog.remove_movie("Quentin Tarantino", "Pulp Fiction"))
print(catalog.remove_movie("Quentin Tarantino", "Django Unchained"))  # rimuove tutto

print(catalog.list_directors())
print(catalog.get_movies_by_director("Christopher Nolan"))

print(catalog.search_movies_by_title("in"))  # trova "Inception" e "Interstellar"


