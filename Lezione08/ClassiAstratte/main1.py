from es1 import *

def main():
    c = Circle(5,3.14)
    r = Rectangle(4, 6)

    print("Cerchio:")
    print("Area:", c.area())
    print("Perimetro:", c.perimetro())

    print("\nRettangolo:")
    print("Area:", r.area())
    print("Perimetro:", r.perimetro())

if __name__ == "__main__":
    main()