# 9-13. Dice: 
# Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Dice:

    def __init__(self,sides:int=6):
        self.sides=sides

    def roll_dice(self):
        print(randint(1,self.sides),end=" ")
        
dice1=Dice(6)


for i in range(10):
    dice1.roll_dice()

dice2=Dice(10)
dice3=Dice(20)
print("")
for i in range(10):
    dice2.roll_dice()
print("")
for i in range(20):
    dice3.roll_dice()

