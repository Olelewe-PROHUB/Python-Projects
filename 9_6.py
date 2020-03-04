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
        print(f"The name of the restaurant is {self.name}, and they offer {self.type} food. ")
 
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

#The next segment of this program builds upon the existing Restaurant Class
#A new class called IceCreamStand will build upon the previous class by 
#inheritance

class IceCreamStand(Restaurant):
    """
    A new class that inherits the restaurant class I created earlier. It will
    create an attribute called flavors, which will store a list of desired 
    flavors.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Cookies and Cream', 'Pumpkin Spice', 'Vanilla', 'Berry'        ]

    def display_flavors(self):
        """Shows the flavors that the ice cream store features"""
        print("The store has the following flavors: ")
        for k in self.flavors:
            print(k)

place = IceCreamStand('Baskin-Robbins','Ice Cream')

place.display_flavors()

