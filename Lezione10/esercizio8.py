# Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi 
# (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta 
# (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

# Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, o
# vvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

# Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, 
# entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare 
# la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, 
# entrambi contenuti entro un ciclo dell'orologio di 12 ore.

# Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

def seconds_since_noon(ore:int,minuti:int,secondi:int):
    limit12 = 0
    cont_ore= 0
    cont_minuti=minuti
    cont_secondi= secondi
    while ore > limit12:
        cont_ore += 1 
        ore -= 1
    for n in range(cont_ore):
        cont_minuti+=60
    for e in range(cont_minuti):
        cont_secondi+=60

    return cont_secondi

def time_difference(ore1:int,minuti1:int,secondi1:int,ore2:int,minuti2:int,secondi2:int):
    risultato1=seconds_since_noon(ore1,minuti1,secondi1)
    risultato2=seconds_since_noon(ore2,minuti2,secondi2)
    
    return abs(risultato1-risultato2)



# print(seconds_since_noon(3,15,30))
# print(seconds_since_noon(1,0,0))
print(time_difference(0, 0, 0, 12, 0, 0))
# print(seconds_since_noon(0,0,0))
# print(seconds_since_noon(12,0,0))