''' Data una stringa contenente solo i caratteri
 '(' e '(' restituire true se le parentesi sono bilanciate
 e False altrimenti.
 Ad esempio: 
 
 bilanciate di ("((())))") --> True
 
 bilanciate ("())")--> False
 
 bilanciate ("()()()")--> True
 
 bilanciate ("))((")--> False
 
 bilanciate ("(()())")--> True'''

d:dict = {"k": 2 , "a": 34 , "true": 12}

print("I valori del dizionario sono: ")

for value in d.values():
    print (f"- {value}")
