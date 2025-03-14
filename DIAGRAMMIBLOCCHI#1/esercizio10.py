reddito:float=float(input("Inserisci il tuo reddito familiare, espresso in EUR: "))
media:float=float(input("Inserisci la tua media dei voti: "))

if reddito < 0 and media < 0:
    print("Inserisci dei valori positivi")
    exit()
if reddito < 20000 and media > 27:
    print("Borsa di studio approvata")
else:
    print("Borsa di studio rifiutata. (Motivo: reddito o media insufficiente)")

