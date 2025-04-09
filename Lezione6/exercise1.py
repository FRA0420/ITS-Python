class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    

alice = Person("Alice W.",45)
bob = Person("Bob M.", 36)
print(bob.age)

if bob.age > alice.age:
    print(bob.name)
else:
    print(alice.name)

chiara = Person("Chiara M.",26)
leo = Person("Leo S.",27)
ric = Person("Ric M.",24)

people:list=[alice,bob,chiara,leo,ric]

youngest=people[0]



for element in people:
    if youngest.age > element.age:
        youngest=element
print(youngest.name)


    # if youngest > bob.age:
    #     youngest = bob.age
    #     youngest_name=bob.name
    # if youngest > chiara.age:
    #     youngest = chiara.age
    #     youngest_name=chiara.name
    # if youngest > leo.age:
    #     youngest = leo.age
    #     youngest_name=leo.name
    # if youngest > ric.age:
    #     youngest = ric.age 
    #     youngest_name=ric.name
    # else:
    #     youngest = alice.age
    #     youngest_name=alice.name





    