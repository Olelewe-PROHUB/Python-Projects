#This program will create a function that takes items of what a customer wants
#On a sandwich. The function will print all of the items requested in the order

def get_wich(*stuff):
    """This function will accept any number of items as input and print the         order in a list"""

    print("You wish to have the following items in your sandwich: ")
    for bil in stuff:
        print(f"- {bil}")

    print("\n")


get_wich('Ham')
get_wich('Turkey', 'Mayonaise', 'Rye')
get_wich('Jelly', 'Wheat')
        
