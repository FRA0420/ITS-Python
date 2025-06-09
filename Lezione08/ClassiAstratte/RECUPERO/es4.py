# Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
# soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
# è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
# oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.
from typing import Any

def verify(x,y,z)->str:
    
    if x and (y or z):
        return "azione permessa"
    else:
        return "azione negata"

print(verify(True,False,False))
print(verify(True,True,True))