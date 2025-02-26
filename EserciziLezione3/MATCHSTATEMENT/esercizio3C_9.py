x:int=int(input("Inserisci la coordinata del punto x: "))
y:int=int(input("Inserisci la coordinata del punto y: "))
tupla:tuple=(x,y)

match tupla:
    case (0,0):
        print("Il punto si trova nell'origine")
    case (x,0):
        print("Il punto si trova sull'asse delle X")
    case (0,y):
        print("Il punto si trova sull'asse Y")
    case tupla if x > 0 and y > 0:
        print("Il punto si trova nel primo quadrante")
    case tupla if x < 0 and y > 0:
        print("Il punto si trova nel secondo quadrante")
    case tupla if x < 0 and y < 0:
        print("Il punto si trova nel terzo quadrante")
    case tupla if x > 0 and y < 0:
        print("Il punto si trova nel quarto quadrante")
    

