from my_project.calculator import Calcolatrice
import pytest
@pytest.fixture
def calculation():
    #creates a fresh istance of Calculator before each test
    return Calcolatrice(10,5)


def test_addition(calculation):
    # calculation: Calcolatrice = Calcolatrice(10,5)
    assert calculation.addition() == 13, 'the sum is wrong'

def test_subtraction(calculation):
    # calculation:Calcolatrice = Calcolatrice(10,5)
    assert calculation.substraction() == 5, 'the subtraction is wrong'

def test_multiplication(calculation):
    # calculation:Calcolatrice = Calcolatrice(10,5)
    assert calculation.multiplication() == 50 ,'the multiplication is wrong'

def test_division(calculation):
    # calculation:Calcolatrice = Calcolatrice(10,5)
    assert calculation.division() == 2.00 , 'the quotient is wrong'
