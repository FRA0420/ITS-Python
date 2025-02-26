stringa:str = input("Inserisci una frase o parola ")
count:str = "" 
for i in range(len(stringa)-1,-1,-1):
    count += stringa[i]
print(f"{count}")

