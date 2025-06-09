class Film:
    _titolo:str
    _durata:int
    def __init__(self,tit,dur):
        self.setTitolo(tit)
        self.setDurata(dur)

    def setTitolo(self,titolo:str):
        self._titolo=titolo

    def setDurata(self,durata:int):
        self._durata=durata

    def getTitolo(self):
        return self._titolo
    def getDurata(self):
        return self._durata
    
    def __str__(self):
        return f"{self.getTitolo()} e {self.getDurata()}"

class Sala:
    _numero:int
    _posti_totali:int
    _posti_pren:int
    def __init__(self,num:int,film:Film,posti_totali:int):
        self.setNumero(num)
        self.set_posti(posti_totali)
        self._posti_pren:int=0
        self.setFilm(film)
    
    def setNumero(self,numero:int):
        self._numero=numero

    def set_posti(self,posti:int):
        self._posti_totali=posti

    def setFilm(self,film:Film):
        self.film=film

    def numero(self):
        return self._numero
    def posti(self):
        return self._posti_pren

    def prenota_posti(self,num_posti):
        if num_posti <= 0:
            print("Devi prenotare almeno un posto")
        if self._posti_totali >= num_posti:
            self._posti_pren += num_posti
            return f"Prenotazione confermata: {num_posti} per {self.film.getTitolo()} in sala {self.numero()} numero dei posti: {self.posti_disponibili()}"
        else:
            return "Posti non disponibili"
    
    def posti_disponibili(self):
        return self._posti_totali - self._posti_pren
    
class Cinema:
    def __init__(self):
        self.sale:list[Sala]=[]
    
    def aggiungi_sala(self,sala:Sala):
        if sala not in self.sale:
            self.sale.append(sala)
        
                
            

    def prenota_film(self,titolo_film,num_posti):
        if self.sale:
            for sala in self.sale:
                if sala.film.getTitolo().lower() == titolo_film.lower():
                    return sala.prenota_posti(num_posti)
            return f"Film '{titolo_film}' non trovato"
        else:
            return "Nessuna sala disponibile nel cinema"

# Creazione film
film1 = Film("Inception", 148)
film2 = Film("Interstellar", 169)
print(film1)

# Creazione sale
sala1 = Sala(1, film1, 100)
sala2 = Sala(2, film2, 80)

# Configurazione cinema
cinema = Cinema()
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)



# # Mostra programmazione
# print("\n Programmazione:")
# cinema.mostra_programmazione()

# Cliente prenota
print("Prenotazioni:")
print(cinema.prenota_film("Inception", 4))
# print(cinema.prenota_film("Interstellar", 90))  # troppo
# print(cinema.prenota_film("Avatar", 2))         # film non esiste

# # Dopo prenotazioni
# print("\n Disponibilità aggiornata:")
# cinema.mostra_programmazione()