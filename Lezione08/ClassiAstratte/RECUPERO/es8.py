class Movie():
    
    def __init__(self,movie_id:str,title:str,director:str)->None:
        self.movie_id=movie_id
        self.title=title
        self.director=director
        self.is_rented=False

    def rent(self)->None:
        if self.is_rented == False:
            self.is_rented = True
        else:
            print(f"Il film {self.title} è già stato noleggiato")

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film {self.title} non è stato noleggiato da questo cliente")
    

class Customer():

    def __init__(self,customer_id:str,name:str):
        self.customer_id=customer_id
        self.name=name
        self.rented_movies:list[Movie]=[]


    # def rent_movie(self,movie:Movie)->None:
# SBAGLIATO
    #     if movie not in self.rented_movies:
    #         self.rented_movies.append(movie)
    #     else:
    #         print(f"Il film {movie.title} è già noleggiato")

    def return_movie(self,movie:Movie)->None:

        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente")

    
class VideoRentalStore:

    def __init__(self):
        self.movies:dict[str,Movie]={}
        self.customers:dict[str,Customer]={}

    def add_movie(self,movie_id:str,title:str,director:str)->None:
        if movie_id in self.movies:
            print(f"Il film con ID: {movie_id} esiste già")
        else:
            self.movies[movie_id]=Movie(movie_id,title,director)
    #chiedere come fare a vedere se effettivamente si è aggiunto quel film che ho detto io [esce oggetto strano nell'output]
    def register_customer(self,customer_id:str,name:str)->None:
        if customer_id in self.customers:
            print(f"Il cliente con ID: {customer_id} è già registrato")
        else:
            self.customers[customer_id]=Customer(customer_id,name)

    def rent_movie(self,customer_id:str,movie_id:str)->None:
        if customer_id not in self.customers and movie_id not in self.movies:
            print("Errore film o cliente non trovati")
        else:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)

    def return_movie(self,customer_id:str,movie_id:str)->None:
        if customer_id not in self.customers and movie_id not in self.movies:
            print("Errore cliente o film non trovato")
        else:
            customer = self.customers[customer_id] #la variabile customer sarà il valore della chiave customer_id in self.customers
            movie = self.movies[movie_id]
            customer.return_movie(movie)

    def get_rented_movies(self,customer_id:str)->list[Movie]:
        if customer_id not in self.customers:
            print("cliente non trovato")
            return []
        else:
            customer = self.customers[customer_id]
            return customer.rented_movies
        




    

m:Movie=Movie("aaa","Ciao","Bello")
v:VideoRentalStore=VideoRentalStore()
v.add_movie("aaa","Ciao","Bello")