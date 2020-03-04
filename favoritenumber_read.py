#This program will read the file favornumb.json
#Import its value over and display the number
#That the user entered in favorite_number.py

import json

filename = 'favornumb.json'

with open(filename) as f:
    value = json.load(f)
    print(f"Welcome! Your favorite number is {value}!")
 
