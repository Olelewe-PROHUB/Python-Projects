#This program prints the statements in learning_python.txt

filename = 'learning_python.txt'

with open(filename) as file_object:
    statement = file_object.readlines()

for stat in statement:
    print(stat.rstrip())

print("\n")

with open(filename) as file_object1:
    for list in file_object1:
        print(list.rstrip())

print("\n")
words = ''
for wrd in statement:
    words += wrd

print(words)
