#This program will create a class and several methods for the object Restaurant
#Two attributes will be stored restauraunt_name and cuisine_type
#Followed by the definition of two methods called describe_restauraunt and 
#open_restauraunt. More will be explained below:

class Restaurant:
    """Definition of a class to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
       """Initialize name and cuisine type attributes"""
       self.name = restaurant_name
       self.type = cuisine_type

    def describe_restaurant(self):
        """
        Method provides the name of the Restaurant and the type of Cuisine.
        """       
        print(f"The name of the restaurant is {self.name}, and they offer {self.        type} food.")
 
    def open_restaurant(self):
        """Creates a statement telling the user that the Restaurant is open"""
        print(f"{self.name} is open!")

restaurant = Restaurant("Abuelito's", "Mexican")

print(f"{restaurant.name}")
print(f"{restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
     
