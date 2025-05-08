from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    #inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape('rettangolo')

    def draw(self)->None:
        print(f"\n{self.getShape()}\n")

        # per disegnare il rettangolo avrò bisogno di due cicli for annidati, uno esterno(i) che scorre la lista verticalmente
        # e uno interno(j) che la scorre orizzontalmente

        #ciclo for esterno
        for i in range(5):
            #ciclo for interno:
            for j in range(5*2):

                # lato a e lato d del rettangolo
                if i == 0 or i == (5-1):
                    print("*",end=" ")
                # lato b e lato c del rettangolo
                elif j == 0 or j == (10-1):
                    print("*",end=" ")
                #stampare gli spazi bianchi
                else:
                    print(" ",end=" ")
            
            print("\n",end="")