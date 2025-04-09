import random
from random import randint

danno_player:int=(2*random.randint(2,6))+3
txc_player:int=int(input("Inserisci un tuo txc: "))
CA_mostro:int=int(input("Inserisci la classe armatura del mostro: "))
PF_mostro:int=int(input("Inserisci i punti ferita del mostro: "))
turni:int=0
simulazione=3
while simulazione != 0:
    if random.randint(1,20)+txc_player >= CA_mostro:
        if PF_mostro > 0:
            PF_mostro -= danno_player
            turni+=1 
        else:
            simulazione-=1
            print(turni)

    else:
        turni+=1
        continue

