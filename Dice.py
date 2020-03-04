#This program will create a class with an attribute called sides which has 
#A default value of 6. The method roll_die prints a random number between
#1 and the number of sides the die has. After this program has successfully
#Worked, we will make a 10-sided and 20-sided die.

"""Imports the Python Module random and the class radint"""
from random import randint

class Die:
    """Initializes the Class Die"""
    
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        """Creates the method roll_die"""
        i = 0
        while i <= 10:
            k = randint(1, self.sides)
            print(f"{k}")
            i+=1

rolly = Die(6)
rolly.roll_die()

print("\n")

rolly1 = Die(10)
rolly1.roll_die()

print("\n")

rolly2 = Die(20)
rolly2.roll_die()



        
