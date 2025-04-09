import random
#definisco una funzione per calcolare la mossa della tartaruga dove la variabile tarta sarà la posizione nella lista percorso
def tarta_step(tarta):
    tarta_mossa= random.randint(1,10)
    match tarta_mossa:
        case 1|2|3|4|5:
            tarta+=1              #se fa da 1 a 5 avanza di una posizione
            return(tarta)
        case 6|7:                 #se fa 6 o 7 va indientro di sei ma con il controllo non puà andare più indietro della prima posizione
            tarta-=6
            if tarta < 0:
                return tarta == 0
            else:
                return(tarta)
        case 8|9|10:
            tarta +=1
            return(tarta)

#definisco la funzione per la mossa di lepre facendo le stesse cose che nella funzione tarta_step
def lepre_step(lepre):
    lepre_mossa=random.randint(1,10)
    match lepre_mossa:
        case 1|2:
            return(lepre)
        case 3|4:
            lepre += 9
            return(lepre)
        case 5:
            lepre -= 12
            if lepre < 0:
                return lepre == 0
            else:
                return(lepre)
        case 6|7|8:
            lepre += 1
            return(lepre) 
        case 9|10:
            lepre -= 2
            if lepre < 0:
                return lepre == 0
            else:
                return(lepre)
    
    

#questa funzione mi serve per stampare il percorso man mano che vado avanti con le iterazioni nel ciclo fuori da questa funzione
def printPosition(lista:list[str]):
    percorso = ''          #in questo modo non stampo la lista ma la stringa tratteggiata continua
    for element in lista:
        percorso += element
    print(percorso) 

tempo = 0       #per vedere quanto dura la gara 
noWinner = True         #finchè non c'è nessun vincitore

lista_posizioni:list=[]
for i in range(70):
    lista_posizioni.append('_')

tarta = 0         #posizione iniziale di tartaruga e lepre
lepre = 0

while noWinner:
    for i in range(70):         
        lista_posizioni[i]="_"      #tutte le posizioni sono _

    tarta = tarta_step(tarta)       #chiamando le funzioni nel ciclo aggiornerò ad ogni iterazione la loro posizione
    lepre = lepre_step(lepre)

    if (tarta < 69) and (lepre < 69):       #finchè non arrivano a 69 -> 0-69 -> 70 quadrati
        lista_posizioni[tarta]="T"      #la posizione di tarta nella lista è rappresentata dalla lettera T
        if tarta != lepre:
            lista_posizioni[lepre]="L"       #la posizione di lepre nella lista è rappresentata dalla lettera L 
        else:
            lista_posizioni[lepre]="OUCH!!!"  #quando si incontrano nello stesso quadrato tartaruga da un morso a lepre
        printPosition(lista_posizioni)

    elif tarta >= 69:
        noWinner = False                #si interrompe il ciclo while 
        print("Ha vinto la tartaruga!")
    else:
        noWinner = False
        print("Ha vinto la lepre")

    tempo +=1 
print(f"La gara è durata {tempo} secondi")
        





        






