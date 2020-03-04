#This program will store the names of different pets in different dictionaries
#Once the dictionaries are create, a loop will execute and print all the 
#Information defined about them

Pet1 = {'Pet Type': 'Iguana', 'Color': 'Green', 'Owner Name': 'Cyrus'}
Pet2 = {'Pet Type': 'Dog', 'Color': 'Golden', 'Owner Name': 'Heather'}
Pet3 = {'Pet Type': 'Rabbit', 'Color': 'White', 'Owner Name': 'Pablo'}
Pet4 = {'Pet Type': 'Mouse', 'Color': 'Brown', 'Owner Name': 'Beatrice'}

Pets = [Pet1, Pet2, Pet3, Pet4]

Type = ""
Color = ""
Name = ""

for animals in Pets:
    
    Type = animals['Pet Type'] 
    Color = animals['Color']
    Name = animals['Owner Name']

    print(f"The Pet is a {Type}, it has a {Color} color, and the owner's name is {Name}")







