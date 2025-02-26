
lanci_totali=1
n_t=0
n_c=0
n=""   #per salvare t o c
while lanci_totali <= 8:
    n:str=input(f"Lancio {lanci_totali}: ").lower()
    match n:
        case "t":
            n_t+=1
        case "c":
            n_c+=1
    lanci_totali+=1
percentuale_t=(n_t/8)*100
percentuale_c=(n_c/8)*100
print(f"\nTotale \"testa\": {n_t}\nPercentuale \"testa\": {percentuale_t:.2f}%")
print(f"Totale \"croce\": {n_c}\nPercentuale \"croce\": {percentuale_c:.2f}%")



        


