# Create a class called MathOperations to group together some basic arithmetic functionality. Inside this class, define two static methods:

#     add, which accepts two numeric parameters and returns their sum.

#     multiply, which also takes two numeric parameters and returns their product.

# Finally, write a small driver program to test the functionality of the add and multiply methods. This should involve calling both methods with sample inputs and printing the results to verify that they work correctly.

class MathOperations:

    @staticmethod
    def add(a:int|float,b:int|float):
        return a+b
    
    @staticmethod
    def multiply(a:int|float,b:int|float):
        return a*b
    
def main():
    # Test del metodo add
    sum_result = MathOperations.add(10, 5)
    print("Somma:", sum_result)

    # Test del metodo multiply
    product_result = MathOperations.multiply(10, 5)
    print("Prodotto:", product_result)

if __name__ == "__main__":
    main()
    
