# 9-14. 
# Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. 
# Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. 
# Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.
# 1. Add a method called simulate_until_win(self, my_ticket) that:

#     Accepts a ticket (a list of 4 items).
#     Repeatedly draws random tickets using the draw_ticket() method.
#     Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
#     Returns the number of attempts and the winning ticket.

# 2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

# 3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

# 4. Print a message showing:

#     Your ticket
#     The winning ticket
#     How many attempts it took to win
import random

class LotteryMachine:
    def __init__(self,lista:list):
        try:
            len(lista) < 14
        except:
                self.lista=[1,2,3,4,5,6,7,10,34,77,"c","l","k","o","a"]
    
        else:
            self.lista=lista

    def drawing_ticket(self):
            vincenti=random.choices(self.lista, k=4)
            return vincenti
    def simulate_until_win(self,my_ticket:list):
        try:
            len(my_ticket) < 4
        except:
                self.my_ticket=["c","l",4,77]
                
        else:
            self.my_ticket=my_ticket
        draw_ticket=self.drawing_ticket()
        attempts=1
        while my_ticket != draw_ticket:
            draw_ticket=self.drawing_ticket()
            attempts+=1
        print(f"Congratulazioni! Dopo solo {attempts} volte hai vinto!")
            
             
             
    # def greet(self):
    #     print("Ogni biglietto che matcherà questi elementi vincerà un premio. \nGli elementi sono:", )

lista1=LotteryMachine([1,3,4,7,8,4,7,9,2,10,"a","b","c","u","i"])
print(lista1.drawing_ticket())      
# lista1.greet()
lista1.simulate_until_win([4,7,"c","u"])