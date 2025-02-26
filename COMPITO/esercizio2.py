
testo: str = input("Inserisci una frase a tua scelta: ")

conteggio_spazi = 0
for spazio in testo:
    if spazio == ' ':
        conteggio_spazi += 1 
    else:
        continue
print(f"Il numero di spazi in \"{testo}\" è" , conteggio_spazi)