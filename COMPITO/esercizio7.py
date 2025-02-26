a:list[int] = [2,3,4,5]
b:list[int] = [10,11,15,16]
c:list[int] = []
somma = 0
if len(a) == len(b):
    
    for first_element in a:
        for second_element in b:
            somma = first_element+second_element
            c.append(somma)    
print(f"\na: {a}, \nb: {b}, \nc: {c}")