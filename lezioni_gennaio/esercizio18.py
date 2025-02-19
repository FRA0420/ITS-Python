mylist= [1,2,3,44,5,7,90]
somma = 0 
media = 0

for n in mylist:
    if n % 2 == 0:
        somma += n
        media = somma/n
print(f"la somma è:{somma}")
print(f"la media è:{media}")
    
        
