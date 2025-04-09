import random 
from random import randint

txc:int=int(input("Inserisci un valore di tiro per colpire: "))
armatura:int=int(input("Inserisci un valore di classe armatura: "))

successi:int=0

for n in range(10000):
    tirato=(random.randint(1,20))+txc
    if tirato >= armatura:
        successi+=1
        
    else:
        continue
perc_successi:int=(successi/10000)*100
print(f"{perc_successi:.1f}%")



