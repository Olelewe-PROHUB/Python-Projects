#This program writes the output of a program to a file

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning is large datasets.\n")
    file_object.write("I love creating apps that can run in a brwoser.\n")
