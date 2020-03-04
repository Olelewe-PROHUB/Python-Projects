#This program will prompt a user for their favorite number 
#Write the output to a in the JavaScript Object Notation format
#And export to a file.

import json

number = input("What is your favorite number?: ")

filename = 'favornumb.json'
with open(filename, 'w') as f:
    json.dump(number, f)
    print("Thank you for your submission!")


