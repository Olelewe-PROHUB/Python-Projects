#This program prints the statements in learning_python.txt

filename = 'learning_python.txt'

with open(filename) as file_object:
    statement = file_object.readlines() 

oscar = ''

for stat in statement:
    oscar += stat
    oscar = oscar.replace('Python', 'C')

print(oscar.rstrip())
        

