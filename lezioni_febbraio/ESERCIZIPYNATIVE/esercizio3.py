stringa:str=input("Inserisci una stringa: ")
if stringa != 0:
    len=len(stringa)
    for i in range(0,len-1,2):
        print(f"All'indice paro {i} c'è il carattere: {stringa[i]}")

               
