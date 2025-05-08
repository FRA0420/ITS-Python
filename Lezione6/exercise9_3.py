# 9-3. Users: Make a class called User. 
# Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self,first_name:str,last_name:str,login_attempts:int,**kwargs):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts
        self.kwargs=kwargs
        print(kwargs)
    
    def describe_user(self):
        print(f"{self.first_name}:{self.last_name}")
        for k,v in self.kwargs.items():
            print(f"{k}:{v}")
    
    def greet_user(self):
        print(f"Ciao User {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"Hai effettuato l'accesso {self.login_attempts} volte")
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"Gli accessi sono stati resettati. Hai effettuato l'accesso {self.login_attempts} volte")



if __name__ == "__main__":

    chiara=User("Chiara","Macciocchi",età=26,laurea="Economia")
    chiara.describe_user()
    chiara.greet_user()