# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 
    
    print("Sequenza a):")
    for n in range(1,7+1):
        print(n)

    print("Sequenza b):")
    for n in range(3,28,5):
        print(n)



    print("Sequenza c):")
    for n in range(20,-16,-6):
        print(n)
    

    print("Sequenza d):")
    for n in range(19,59,8):
        print(n)
    

