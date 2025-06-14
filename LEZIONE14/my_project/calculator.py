class Calcolatrice:

    def __init__(self, a:int,b:int)->None:
        self.a=a
        self.b=b
    
    def addition(self)->int:
        return int(self.a+self.b)
    
    def substraction(self)->int:
        return int(self.a-self.b)
    
    def multiplication(self)->int:
        return int(self.a * self.b)
    
    def division(self)->float|None:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return round(self.a/self.b)
    