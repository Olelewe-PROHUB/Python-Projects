#The write_guest program prompts the user for a name.
#Once provided, the name is written to a text file called guest.txt

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input("What is your name? : ")
    file_object.write(f"{name}")


