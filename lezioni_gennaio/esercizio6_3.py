#esercizio 6.3

glossary: dict = {"function": "boh", "collections": "più cose", "stringhe": "bla bla bla", "operators": "calcola"}
print(glossary)

for k,v in glossary.items():
    print(f"Il termine {k} ha come significato: \n{v}")