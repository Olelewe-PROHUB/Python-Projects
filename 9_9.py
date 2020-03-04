#Program imports a module with the class Restaurant - File 9_4.py and 
#Makes an instance/function call within the Restaurant Class

from RestaurantModule import Restaurant
"""We are importing the Restaurant Class from the module Restaurant Module"""

#Here we will create an instance of the Restaurant Module and call a method

example = Restaurant('Baskin Robbins', 'Ice Cream')

example.open_restaurant()

example1 = Restaurant('Togos', 'Sandwiches')

example1.describe_restaurant()


