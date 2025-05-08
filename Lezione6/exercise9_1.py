# 9-1. Restaurant: Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, 
# and then call both methods.

class Restaurant:

    def __init__(self,restaurant_name:str,cuisine_type:str,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    def setnumber_served(self,number_served):
        self.number_served=number_served
    def incrementnumber_served(self,valore):
        self.number_served+=valore
        print(f"Il ristorante {self.restaurant_name} ha servito {self.number_served} clienti questa sera")
    def describe_restaurant(self):
        print(f"Il ristorante {self.restaurant_name} è un ristorante di {self.cuisine_type} e di solito serve {self.number_served} clienti")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

# ristorante=Restaurant("Bufalero","Carne")
# ristorante.describe_restaurant()
# ristorante.open_restaurant()

