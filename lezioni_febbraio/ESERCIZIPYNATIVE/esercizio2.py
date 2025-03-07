somma=0
previous=0
for n in range(10):
    somma=previous+n
    previous=n
    print(f"current number {n} --> previous number {previous}  somma: {somma}")
