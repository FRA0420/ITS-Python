'''l =[1,2,9,10]
x = l.pop()
print(x)
print(l)
l.remove(2)
print(l)'''

l = [1,5,9,10,16,98,"a"]

'''for i in range(len(l)-1, -1,-1):
    print("Sto rimuovendo l'elemento all'indice" , i)
    l.remove(l[i])'''

while len(l) > 0:
    x = l.pop()
    print("Ho rimosso" , x)

