#This program will create a function that accepts inputs for the following:
#A T-Shirt size and a message that should be on the T-Shirt

def make_shirt(shirt_size = 'L', shirt_message = 'I love Python'):
    """Display details on the shirt."""
    print(f"Your shirt size is: {shirt_size}")
    print(f"The message you want displayed is: {shirt_message.title()}")

make_shirt(shirt_size = 'L')
make_shirt(shirt_size = 'M')
make_shirt(shirt_message = 'Make Py not war')


