#This program will create a class and several methods for the object Restaurant
#Two attributes will be stored restauraunt_name and cuisine_type
#Followed by the definition of two methods called describe_restauraunt and 
#open_restauraunt. 

#The modification to this program will add a new attribute with a starting value#Of zero. It will then draw an instance of this class. Another method will also be included detailing the number of customers that have been served. Another 
#Method will also be added to increment the number of customers that have been
#Served

class Restaurant:
    """Definition of a class to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
       """Initialize name and cuisine type attributes"""
       self.name = restaurant_name
       self.type = cuisine_type
       self.number_served = 0

    def describe_restaurant(self):
        """
        Method provides the name of the Restaurant and the type of Cuisine.
        """       
        print(f"The name of the restaurant is {self.name}, and they offer {self.        type} food.")
 
    def open_restaurant(self):
        """Creates a statement telling the user that the Restaurant is open"""
        print(f"{self.name} is open!")


    def set_number_served(self, numbers):
        """A method that sets the number of customers when called"""
        self.number_served = numbers        
        print(f"The Number of Customers served are: {self.number_served}")

    def increment_number_served(self, values):
        """This method increases the number of customers when called"""
        self.number_served = self.number_served + values
        return self.number_served

restaurant = Restaurant("Abuelito's", "Mexican")

print(f"{restaurant.name}")
print(f"{restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"{restaurant.number_served}")
restaurant.set_number_served(32)

incret = restaurant.increment_number_served(1)
print(f"The new number of customers served are: {incret}")
