lista_n:list[int]=[]
dizionario_n:dict[int]={}  #mi servirà per la frequenza
while True:
    n:int=int(input("Inserisci un numero (0 per terminare): "))
    if n == 0:
        break
    else:
        lista_n.append(n)
        if n not in dizionario_n.keys():
            dizionario_n[n]= 1
        else:
            dizionario_n[n]+=1
lista_dispari:list[float]=[]
lista_pari:list[float]=[]
somma_pari:float=0
somma_dispari:float=0
media_dispari:float=0
for element in lista_n:
    if element % 2 ==0:
        lista_pari.append(element)
        somma_pari += element
    else:
        lista_dispari.append(element)
for disparo in lista_dispari:
    somma_dispari+= disparo
    media_dispari= somma_dispari/len(lista_dispari)
#adesso la frequenza
freq_max:int= 0
chiavi_max:list[int] =[]
chiave_max:int = 0
for frequenza in dizionario_n.keys():
    if dizionario_n[frequenza] > freq_max:
        freq_max= dizionario_n[frequenza]
        chiavi_max=[]
        chiavi_max.append(frequenza)
    elif dizionario_n[frequenza] == freq_max:
        chiavi_max.append(frequenza)
chiave_frequente=chiavi_max
print(f"la somma dei numeri pari è: {somma_pari}")
print(f"la media dei numeri dispari è: {media_dispari}")
print("Il o i numero/i con la frequenza più alta è o sono:" , *chiavi_max , (freq_max , "volte"))    #non sono riuscita a stampare l'output finale senza le [] della lista :(







