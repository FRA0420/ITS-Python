#esercizio 6.7


dict1: dict = { "first_name":"Giulia", "last_name":"La Venuta", "age": 26, "city": "Roma"}
dict13: dict = { "first_name":"Leo", "last_name":"Ciccio", "age": 27, "city": "Roma"}
dict14: dict = { "first_name":"Valerio", "last_name":"nerd", "age": 28, "city": "Roma"}

people: list = [dict1,dict13,dict14]
for i in people:
    if i == people[0]:
        for k,v in dict1.items():
            print(f"{k}: {v}")
    if i == people[1]:
        for k,v in dict13.items():
            print(f"{k}: {v}")
    if i == people[2]:
        for k,v in dict14.items():
            print(f"{k}: {v}")
