#     User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
#     Privileges: holds a list of privileges and a method show_privileges() to display them.
#     Admin: stores a User instance and a Privileges instance as attributes.

class User:
    def __init__(self,first_name,last_name,username,email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email


    def describe_user(self):
        print(f"{self.first_name}:{self.last_name}, username:{self.username}, email:{self.email}")
    
    def greet_user(self):
        print(f"Ciao {self.username}!")

class Privileges:
    def __init__(self,lista:list=None):
        if lista is None:
            lista = []
        self.lista=lista
    def show_privileges(self):
        if self.lista:
            print("I privilegi sono:", *self.lista, sep=",")
        else:
            print("Nessun privilegio assegnato")

class Admin:
    def __init__(self,user:User,privilege:Privileges):
        self.user=user
        self.privilege=privilege
    def describe_admin(self):
        return self.user.describe_user()
    def show_admin_privileges(self):
        return self.privilege.show_privileges()
    