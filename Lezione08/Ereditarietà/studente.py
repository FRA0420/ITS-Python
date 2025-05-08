from persona import Persona   #superclasse o classe padre

class Studente(Persona):
    def __init__(self):
        self.getAge()

#l'ereditarietà ci consente di definire una classe generale
#e partendo da quella posso costruire classi
#più articolate x aggiungere info in più
#classe studente sottoclasse della classe Persona 

