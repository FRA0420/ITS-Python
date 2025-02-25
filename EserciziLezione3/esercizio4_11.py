pizza_list:list = ["zucchine", "margherita", "diavola"]

friend_pizzas = pizza_list.copy()
pizza_list.append("capricciosa")
friend_pizzas[2]= "bufala"

print("My favourite pizzas are: ")
for i in pizza_list:
    print(i)

print("\nMy friends's favourite pizzas are: ")
for j in friend_pizzas:
    print(j)


