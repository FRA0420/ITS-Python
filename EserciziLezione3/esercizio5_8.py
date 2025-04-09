l1:list[str] = ["Chiara", "Giulia", "Leo", 
                "Admin", "Valerio"]

username:str = (input("Quale è il tuo username? ")).title()

match username:
    case username if username in l1 and username == l1[3]:
        print("Hello Admin, would u like to see a status report?")
    case _:
        print(f"Hello {username} thank u for logging in again")
    
    
