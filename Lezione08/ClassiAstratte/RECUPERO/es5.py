# Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
# dato valore intero definito threshold.
from typing import Union

def multiply(a:list[Union[int,float]],threshold:int=50)->int:
    prodotto=1
    for element in a:
        if type(element)==int:
            if element < threshold:
                prodotto*=element
            else:
                continue

    return prodotto



