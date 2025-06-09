class Prodotto:
    def __init__(self,nome:str,quantità:int):
        self.setNome(nome)
        self.setQuantità(quantità)
    
    def setNome(self,n:str):
        if n:
            self.n=n
        else:
            raise ValueError("Il campo nome non può essere vuoto")
    def getNome(self):
        return self.n
    
    def setQuantità(self,q:int):
        self.q=q
    def getQuantità(self):
        return self.q
    
class Magazzino:
    def __init__(self):
        self.box:dict[str,Prodotto]={}

    def aggiungi_prodotto(self,prodotto:Prodotto):
        name = prodotto.getNome()
        if name not in self.box:
            self.box[name]=prodotto
            return self.box
        else:
            quantità_corrente = self.box[name].getQuantità()
            nuova_quantità = quantità_corrente + prodotto.getQuantità()
            self.box[name].setQuantità(nuova_quantità)
            return self.box
    def cerca_prodotto(self,nome:str)->Prodotto|None:
        for nome_prodotto,prodotto in self.box.items():
            if nome_prodotto == nome:
                return prodotto
        print("Prodotto non trovato in magazzino")
        return None
        
    def verifica_disponibilità(self,nome:str)->str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto is None:
            return "Prodotto non disponibile"
        elif prodotto.getQuantità() > 0:
            return f"Il prodotto {nome} è disponibile in quantità: {prodotto.getQuantità()}"
        else:
            return f"Il prodotto {nome} è esaurito"


if __name__ == "__main__":
    # Creo il magazzino
    magazzino = Magazzino()

    # Creo prodotti
    p1 = Prodotto("Mouse", 10)
    p2 = Prodotto("Tastiera", 5)
    p3 = Prodotto("Monitor", 0)

    # Aggiungo i prodotti al magazzino
    magazzino.aggiungi_prodotto(p1)
    magazzino.aggiungi_prodotto(p2)
    magazzino.aggiungi_prodotto(p3)
    

    # Cerco un prodotto
    prodotto = magazzino.cerca_prodotto("Tastiera")
   

    # Verifico disponibilità
    print(magazzino.verifica_disponibilità("Mouse"))      # disponibile
    print(magazzino.verifica_disponibilità("Monitor"))    # esaurito
    print(magazzino.verifica_disponibilità("Stampante"))  # non trovato