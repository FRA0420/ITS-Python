l1:list[str] = ["Chiara", "Giulia", "Leo", 
                "Admin", "Valerio"]

username:str = (input("Quale è il tuo username? ")).lower()

if username in l1:
    for i in l1:
        if username == "Admin":
            print("Hello Admin, ...")
        else: 
            print("...")
else:
    print(f"{username} not found")
