# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
# using a different number of arguments each time.

def ingredients(*args) -> None:
    panino:list[str]=[]
    for n in args:
        panino.append(n)
    print("Il sandwich è fatto con:", *panino)

ingredients("lattuga","salame","mozzarella")
ingredients("formaggio","salame","salsa","lattuga")
