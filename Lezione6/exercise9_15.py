# 9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

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

from exercise9_14 import LotteryMachine

