#This program will create a class and several methods for the object Users
#Two attributes will be stored first_name and last_name
#Followed by the definition of two methods called describe_user and 
#greet_user. More will be explained below:

#Two additional methods will be added. The first will record the number of login
#Attempts made by the User. The second method will reset the number of login
#Atttempts back to zero




class User:
    """Definition of a class to model a User Profile."""

    def __init__(self, first_name, last_name, user_age, user_town):
       """Initialize name, age, and hometown attributes"""
       self.first = first_name
       self.last = last_name
       self.age = user_age
       self.town = user_town
       self.login_attempts = 0

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

    def increment_login_attempt(self, attempt):
        """Increments the number of login attempts"""
        self.login_attempts += attempt
        print(f"Current number of login attempts {self.login_attempts}")

    def reset_login_attempts(self):
        """Resets the number of login attempts to zero"""
        self.login_attempts = 0         
        print(f"The number of login attempts have been reset to {self.login_attempts}")
       
user1 = User('Rachel', 'Dwyer', 27, 'Leadville')
user1.describe_user()
user1.greet_user()

print("\n")

user2 = User('Harold', 'Garner', 15, 'Buckingham')
user2.describe_user()
user2.greet_user()

print("\n")

user3 = User('Ikenna', 'Olelewe', 27, 'Oakland')
user3.describe_user()
user3.greet_user()

print("\n")

user4 = User('Barry', 'Weiss', 57, 'Los Angeles')
user4.describe_user()
user4.greet_user()

user4.increment_login_attempt(15)
user4.reset_login_attempts()

     
