l1:list[str] = ["Chiara", "Giulia", "Leo", 
                "Admin", "Valerio"]

username:str = (input("Quale è il tuo username? ")).lower()


for username in l1:
    if username == "Admin":
        print("Hello Admin, ...")
    
else: 
    print(f"Hello {username}")
    
    
