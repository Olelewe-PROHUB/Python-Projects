#This program will prompt a user for their favorite number
#Write the output to a in the JavaScript Object Notation format
#And export to a file.

#This segment of the program will read the file favornumb.json
#Import its value over and display the number
#That the user entered in favorite_number.py

import json

filename = 'favornumb.json'

try:
    with open(filename) as f:
        value = json.load(f)
        if value:
            print("Your previous entry has been recovered!")

except FileNotFoundError:
    print("No previous entry found.")
    number = input("What is your favorite number?: ")
    filename = 'favornumb.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
        print("Thank you for your submission!")

    with open(filename) as fa:
        value = json.load(fa)
        print(f"Your favorite number is {value}")

else:    
    print(f"Welcome! Your favorite number is {value}!")








