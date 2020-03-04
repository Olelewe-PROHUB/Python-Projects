#This program will read the files cats.txt and dogs. txt
#Once the names are ingested, the names in the files are printed 

filename = 'cats.txt'

try:
    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

    print("\n")

except FileNotFoundError:
    pass

else:
    for line in lines:
        print(line.rstrip())

"""
    Second attempt of reading text files
"""

 
filename1 = 'dogs.txt'

try:
    with open(filename1) as file_object1:
        lines = file_object1.readlines()

except FileNotFoundError:
    pass

else:
    for line in lines:
        print(line.rstrip())

