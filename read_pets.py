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
    print("File could not be found in the given directory")
    print("\n")


filename1 = 'dogs.txt'

try:
    with open(filename1) as file_object1:
        lines = file_object1.readlines()

    for line in lines:
        print(line.rstrip())

except FileNotFoundError:
    print("File could not be found in the given directory")

