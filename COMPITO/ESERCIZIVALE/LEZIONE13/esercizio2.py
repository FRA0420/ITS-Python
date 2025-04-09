def compoundInterest(capitale:float,t:int,r=1.005)->float:
    # m = capitale * (1+r)**t
# t<= 0 perchè indica che il mese t = 0 è il mese in cui io ho investito, avrò quindi capitale = capitale
    if t <= 0:
        return round(capitale,2)
    if capitale == 0:
        return None
    else:
        return round((r*compoundInterest(capitale,t-1)),2)
print(compoundInterest(1000,6))