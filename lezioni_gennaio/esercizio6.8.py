#esercizio 6.8

martin:dict = {"cat":"chiara"}
lucky:dict = {"cat":"mamma"}
willy:dict = {"cat":"vinci"}
pets:list = [martin,lucky,willy]
for i in pets:
    for k,v in i.items():
        print(k,v)