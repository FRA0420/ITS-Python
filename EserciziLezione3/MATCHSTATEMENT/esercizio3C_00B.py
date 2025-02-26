name:str = input("Quale è il tuo nome? ").lower()

genere:str = input("quale è il tuo genere? m,f o ns? ").lower()

match genere:
    case "m":
        print(f"Nome: {name} \nGenere: {genere}")
    case "f":
        print(f"Nome: {name} \nGenere: {genere}")
    case "ns":
        print(f"Nome: {name} \nGenere: {genere}")
    case _:
        print("ERRORE! SPECIFICARE GENERE")
