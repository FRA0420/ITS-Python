soldi:int = int(input("Quanti soldi hai da spendere? "))
if soldi > 0:
    barrette_disponibili:int = soldi
    buoni_sconto:int = barrette_disponibili
    barrette_bonus:int = buoni_sconto //6
    buoni_sconto_restanti:int = barrette_disponibili % 6
    totale_barrette:int = barrette_disponibili + barrette_bonus
else:
    print("errore")
    exit()

print(f"Puoi acquistare {barrette_disponibili} barrette e ricevere {barrette_bonus} barrette bonus.")
print(f"In totale avrai {totale_barrette} barrette. Inoltre, ti avanzano {buoni_sconto_restanti} buoni sconto")
