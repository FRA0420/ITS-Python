from abc import ABC,abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(a,b):
        pass
    
    @abstractmethod
    def perimetro(a,b):
        pass


#perimetro= (a+b)*2
#area= a*b

#perimetro=2pigreco*r
#area=r^2*pigreco

class Rectangle(Shape):

    def area(self,a:int,b:int)->None:
        if a > 0 and b > 0:
            return a*b
        raise ValueError("i valori devono essere positivi")
    
    def perimetro(self,a:int,b:int)->None:
        if a > 0 and b > 0:
            return (a+b)*2
        raise ValueError("i valori devono essere positivi")
    
class Circle(Shape):

    def area(self,a:int,b:float)->None:
        if a > 0 and b == 3.14:
            return (a*a)*b
        raise ValueError("i valori devono essere positivi")
    
    def perimetro(self,a:int,b:int)->None:
        if a > 0 and b == 3.14:
            return (b*2)*a
        raise ValueError("i valori devono essere positivi")