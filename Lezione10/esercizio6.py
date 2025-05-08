from math import sqrt

def hypotenuse(c1:float,c2:float):
    ipo:float=1
    c1a=c1*c1
    c2a=c2*c2
    ipo=sqrt(c1a+c2a)
    return ipo 

print(hypotenuse(3.0, 4.0))
