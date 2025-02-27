#esercizio 6.8

martin:dict = {"cat":"chiara"}
lucky:dict = {"cat":"mamma"}
willy:dict = {"cat":"vinci"}
pets:list = [martin,lucky,willy]
for i in pets:
    if i == pets[0]:
        for k,v in martin.items():
            print(f"Il {k} Martin è di {v}")
    if i == pets[1]:
        for k,v in lucky.items():
            print(f"Il {k} Lucky appartiene a {v}")
    if i == pets[2]:
        for k,v in willy.items():
            print(f"Il {k} Willy appartiene a {v}")