#!/usr/bin/python3

classlist=[]

userclass=""

while (userclass != "Done"):
    userclass = input("What classes do you like (Type 'Done' when done)?")
    if (userclass == "Done"):
        break
    else:
      classlist.append(userclass)

print("You like the following classes:",classlist)

