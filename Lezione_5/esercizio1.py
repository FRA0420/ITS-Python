# Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.

# La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.
# print(somma_elementi([1,1,1],[1,1,1]))

	

# [2, 2, 2]

# def somma_elementi(lista1:list[int], lista2:list[int])->list[int]:
#     lista3=lista1.copy()
#     for element in range(len(lista2)):
#         lista3[element]+=lista2[element]
        
#     return lista3
# print(somma_elementi([1,1,1],[1,1,1]))



# Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, 
# dove n è la lunghezza della lista. Tuttavia, alcuni numeri potrebbero mancare: 
# la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.

# Il tuo compito è individuare i numeri mancanti.

# Scrivi una funzione che, data in input una lista, 
# restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.
# print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

	

# [5, 6]

# def find_disappeared_numbers(lista:list[int])->list[int]:
#     n = len(lista)

#     lista3=[]
#     for i in range(1,n+1):
#         if i not in lista:
#             lista3.append(i)
#     return lista3

#rint(find_disappeared_numbers([4,3,2,7,8,2,3,1,]))
        

        
        

# print(find_disappeared_numbers([1,4,3,5]))

# Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

#     tutti i numeri pari vengano prima di tutti i numeri dispari;

#     l’ordine relativo tra pari e dispari va mantenuto;

#     l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

# print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

	

# [6, 8, 4, 3, 1, 7]

# def even_odd_pattern(lista:list[int]):
#     lista_pari=[]
#     lista_dispari=[]
#     lista2=lista.copy()

#     for element in lista2:
#         if element % 2 ==0:
#             lista_pari.append(element)
#         else:
#             lista_dispari.append(element)
#     lista_pari.extend(lista_dispari)
#     return lista_pari
# print(even_odd_pattern([3,6,1,8,4,7]))
    
# Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.

# Un fattore primo di n è un numero primo che divide esattamente n (cioè senza resto), 
# e la cui moltiplicazione in sequenza restituisce n. Un numero può avere lo stesso fattore primo più volte.
# Cosa sono i fattori primi?

# I fattori primi di un numero sono numeri primi che, moltiplicati tra loro, 
# danno come risultato proprio quel numero.

# 🔹 Esempio:
# Il numero 60 si può scomporre in: 2 × 2 × 3 × 5 → cioè: 2² × 3 × 5

# 🔎 Suggerimento:
# Prova a pensare a come potresti "smontare" un numero dividendolo più volte, 
# iniziando dal numero primo più piccolo possibile. Cosa succede ogni volta che la divisione ha resto 0? 
# E cosa potresti fare quando non lo è più?

# print(prime_factors(4))
# [2, 2]
# print(prime_factors(60))
# [2, 2, 3, 5]

# def prime_factors(numero:int)->int:
#     fattori = []
#     div = 2
#     while numero > 1:
#         if numero % div ==0:
#             print(div)
#             numero //= div
#             print(numero)
#             fattori.append(div)
#         else:
#             div += 1


#     return fattori
    



# Nel gioco del Blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. 
# Ogni carta ha un valore compreso tra 2 e 11 inclusi.

#     Il valore numerico delle carte (da 2 a 10) è equivalente al loro valore nominale.
#     Le figure (Jack, Regina, Re) non sono incluse in questo esercizio e vengono ignorate.
#     L'Asso (valore 11) può valere 1 o 11, a seconda di quale sia più favorevole al giocatore:
#         Se la somma della mano supera 21, e c'è almeno un asso valutato 11, quell'asso 
#         deve essere considerato 1 per evitare il "bust" (superare 21).

# Scrivi una funzione che prende in input una lista di interi rappresentanti i valori delle carte 
# e restituisce il valore totale della mano secondo le regole del Blackjack.

# print(blackjack_hand_total([2, 3, 5]))
# 10
# print(blackjack_hand_total([11, 5, 5]))
# 21

# def blackjack_hand_total(cards:list[int]):
#     somma = 0
#     for i in cards:
#         somma+=i
#         if somma > 21:
#             if 11 or 1 in cards:
#                 somma -= 10
        
            
#     return somma
# print(blackjack_hand_total([2,3,5]))
# print(blackjack_hand_total([11, 5, 5]))
# print(blackjack_hand_total([11,1,10]))

floors:list=[1,4]

numeri= [i for i in range(floors[0],floors[-1] +1)]
print(numeri)

            





