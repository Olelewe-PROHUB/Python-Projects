#This program will create a dictionary, and within each dictionary entry there
#Are favorite places that people want to go to

PP = {'Raul': ['Mexico', 'Bhutan', 'Australia'], 'Timothy': ['Iceland', 'Norway','Panama'], 'Kiersten': ['Argentina', 'Azores', 'South Africa']}

#This create the variables used to store the dictionary names


#This will create a variable to store the locations




#A "for-loop" will be used to cycle through the names. The loop will be followed 
#By a nested loop used to print the desired location of each individual

for names, locations in PP.items():

    
    print(f"{names} would like to go to the following places:")
   
    for places in locations:
        print(f"{places}\n")













