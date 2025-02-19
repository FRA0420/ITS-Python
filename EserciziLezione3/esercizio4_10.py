animals:list = ["lion", "cat", "tiger"]
pizza_list:list = ["zucchine", "margherita", "diavola"]
l2 = animals + pizza_list

print("I primi 3 elementi sono " , l2[0:3])
for x in l2[:3]:
    print("\t" , x)


m = len(l2)//2 
l_metà = l2[m:m+3]

print("Gli elementi in mezzo sono " , l_metà)

print("Gli ultimi 3 elementi sono" , l2[-3:])
