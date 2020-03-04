#This program will create a class called Employee
#The class will take a first name, last name, and annual salary
#Each of these parameters will be stored as attrbiutes
#Also included will be a method called give_raise that adds $5,000
#To the annual salary, but also accepts a different raise amount

class Employee:
    """
        Will store attributes of an employee
        Including first name, last name, and
        annual salary
    """

    def __init__(self, first_name, last_name, salary):
        """Stores the attributes of the employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, new_raise=''):
        """Increases the salary of the employee"""
        bonus = 5000
        if new_raise:
            bonus = new_raise
            new_amount = self.salary + bonus
        else:
            new_amount = self.salary + bonus
        return new_amount






            
        
    
 
