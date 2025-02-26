#per fare questo esercizio ho usato la matematica spero vada bene :)
targets:list[float] = [3.14, 3.141, 3.1415, 3.14159] #gli obiettivi a cui il programma deve arrivare
moltiplicatori:list[float]=[100,1000,10000,100000]  #(obiettivo*100)= 314 oppure (obiettivo*1000)=3141 ecc...ecc...


for n in range(4):  #perché prendo in considerazione i 4 casi dati dall'esercizio
    print(f'Fase {n}')
    numero = 4
    termini = 0
    while True:
        termini+= 1
        numero += (4/(2*termini+1))*((-1)**termini)     #in questo modo scorro la serie infinita e con -1elevatoaiterazioni cambio il segno da + a - e viceversa
        
        if int(numero*moltiplicatori[n])==int(targets[n]*moltiplicatori[n]):       #quando l'intero del numero uscito fuori dalla serie infinita moltiplicato
                                                                                    #per 100 è uguale all'intero corrispondente nella lista targets per il moltiplicatore
                                                                                    #allora avrò il mio output
            print(f"Ci ho messo {termini} termini per trovare {targets[n]}")
            break
  

