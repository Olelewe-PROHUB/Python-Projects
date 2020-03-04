#The Lottery Program creates a list of 10 Letters and 5 Numbers from a list
#And randomly selects four numbers or letters from the list.
#A message will print saying that if the contestant posesses a matching 
#Combination, that they will win the prize

"""Need to import the choice method from the random module"""
from random import choice

class Lotto:

    def __init__(self):
        """Initialize the Lotto Attributes"""
        self.lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'F', 'G']
        self.combon = []
        self.combol = []
    
        """
        The method winnter, is used to determine the correct tickect combo
        If the choice is a string, it is assigned to self.combon
        If the choice is a number, it is assigned to self.combol
        Whoever fills up to a length of 5 firsts, becomes the winning
        Combination that is displayed
        """

    def winner(self):
        i = 0
        j = 0
        while i < 5 and j < 5:
            k = choice(self.lists)

            if k in range(1,10):
                self.combon.append(k)
                i+=1     
         
            if k in ['A', 'B', 'C', 'F', 'G']:
                self.combol.append(k)
                j+=1

            if i == 4 or j == 4:
                break

        if len(self.combon) == 4:
            print("To win you must have following number combination: ")
            for q in self.combon:
                print(f"{q}")

        elif len(self.combol) == 4:
            print("To win you must have following letter combination: ")
            for r in self.combol:
                print(f"{r}")

        else:
            print("No winning Combination has been determined")

prize = Lotto()
prize.winner()
    
