#This program will create a class and several methods for the object Users
#Two attributes will be stored first_name and last_name
#Followed by the definition of two methods called describe_user and 
#greet_user. More will be explained below:

class User:
    """Definition of a class to model a User Profile."""

    def __init__(self, first_name, last_name, user_age, user_town):
       """Initialize name, age, and hometown attributes"""
       self.first = first_name
       self.last = last_name
       self.age = user_age
       self.town = user_town

    def describe_user(self):
        """
        Method provides the profile of the User including their name, age, and 
        hometown.
        """       
        print(f"First Name: {self.first}")
        print(f"Last Name: {self.last}")
        print(f"Age:       {self.age}")
        print(f"Hometown:  {self.town}")
 
    def greet_user(self):
        """Creates a personalized statement greeting the user."""
        print(f"Welcome {self.first} {self.last}, glad to see you back!")


#Creates a new class called Admin to indicate the administrative user
#Will display administrator privledges through the method show_privledges

class Admin(User):
    """Definition of the class Admin"""
    """Admin will inherit the properties of the parent class Admin"""

    def __init__(self, first_name, last_name, user_age, user_town):
        """
        Initialize the attributes of the parent class
        Creates an attribute called privleges that stores a string
        the displays the permissions of the Admin User.
        """
        super().__init__(first_name, last_name, user_age, user_town)
        self.privs_one = ["Can Add Post", "Can Delete Post", "Can Modify Accounts"]
             
    def display_priv(self):
        """Shows the permissions of the administrator"""
        print(f"Welcome {self.first} {self.last}")
        for k in self.privs_one :
            print(k)

permit = Admin('Gerald', 'Lavert', 25, 'Oregon') 

permit.display_priv()
     
