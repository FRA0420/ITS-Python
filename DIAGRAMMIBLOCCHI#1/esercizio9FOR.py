#9. Classifica delle vendite

#Progetta un algoritmo che forniti dall'utente 20 totali di vendita 
#e i nomi dei venditori, trova i due nomi dei venditori 
#con il totale più alto e il totale più basso 
#delle vendite.

nome:str=input("Inserisci un nome di un venditore: ")
vendita:float=float(input("Inserisci una vendita: "))

max_nome:str=nome
min_nome:str=nome
max_vendita:float=vendita
min_vendita:float=vendita
for count in range(18):
    new_nome:str=input("Inserisci il nome di un altro venditore: ")
    new_vendita:float=float(input("Inserisci un'altra vendita: "))
    if new_vendita > max_vendita:
        max_nome=new_nome
        max_vendita=new_vendita
    elif new_vendita < min_vendita:
        min_vendita=new_vendita
        min_nome=new_nome
print(f"Il venditore migliore è {max_nome.title()} con una vendita di {max_vendita}!!")
print(f"Il venditore peggiore è {min_nome.title()} con una vendita di {min_vendita}")

    
