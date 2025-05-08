def calcola_stipendio(ore_lavorate: int) -> float:
    stipendio = 0 
    ore_extra = 0
    if ore_lavorate <= 40:
        stipendio = ore_lavorate*10
    else:
        ore_extra = 40 - ore_lavorate
        moltiplico=abs(ore_extra)
        stipendio = (40*10) + (moltiplico*15)
    
    return stipendio 

print(calcola_stipendio(40))

print(calcola_stipendio(30))
print(calcola_stipendio(45))
print(calcola_stipendio(60))
print(calcola_stipendio(0))