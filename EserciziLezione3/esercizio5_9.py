l1:list[str] = ["Chiara", "Giulia", "Leo", 
                "Admin", "Valerio"]
'''if l1 != []:
    username:str = (input("Quale è il tuo username? ")).title()

    match username:
        case username if username in l1 and username == l1[3]:
            print("Hello Admin, would u like to see a status report?")
        case _:
            print(f"Hello {username} thank u for logging in again")
else:
    print("We need to find some users!")'''

for n in range(len(l1)):
    l1.pop(0)
username:str = (input("Quale è il tuo username? ")).title()

if l1 == []:
    print("We need to find some users!")

else:

    match username:
        case username if username in l1 and username == l1[3]:
            print("Hello Admin, would u like to see a status report?")
        case _:
            print(f"Hello {username} thank u for logging in again")


