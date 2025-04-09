def make_shirt(s:str="l",t:str="I love Python"):
    print(f"Maglietta taglia {s}, testo \"{t}\"")
make_shirt()
make_shirt("m")
make_shirt(s=input("Che taglia è la maglietta? "), t=input("Che messaggio ci mettiamo sopra? "))