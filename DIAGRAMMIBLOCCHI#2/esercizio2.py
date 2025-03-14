veicoli_ns:int=int(input("Inserisci il numero di veicoli che transita nella direzione Nord-Sud: "))
veicoli_eo:int=int(input("Inserisci il numero di veicoli che transita nella direzione Est-Ovest: "))
soglia:int=70
if veicoli_ns and veicoli_eo > soglia:
    time_ns=50
    time_eo=50
else:
    if veicoli_ns > 70:
        time_ns = 60
        time_eo = 40
    elif veicoli_eo > 70:
        time_eo = 60
        time_ns = 40
if veicoli_ns < 70 and veicoli_eo < 70:
    time_ns = (veicoli_ns/(veicoli_ns + veicoli_eo))*100
    time_eo = (veicoli_eo/(veicoli_eo + veicoli_ns))*100

print(f"Il tempo assegnato al semaforo verde della direzione Nord-Sud è: {time_ns}%")
print(f"Il tempo assegnato al semaforo verde della direzione Est-Ovest è: {time_eo}%")

