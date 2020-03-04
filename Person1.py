#This program will create information about an individual I know.

PersonD = {'FName': 'Kelechi', 'LName': 'Olelewe', 'Age': 25, 'City': 'Moorpark'}

PersonD2 = {'FName': 'Ginikachi', 'LName': 'Olelewe', 'Age': 23, 'City': 'Moorpark'}

PersonD3 = {'FName': 'Uchechukwu', 'LName': 'Olelewe', 'Age': 16, 'City': 'Moorpark'}

Nam1 = ""
Name2 = ""
Age1 = ""
City1 = ""

People = [PersonD, PersonD2, PersonD3];

for folks in People:
    
    Nam1 = folks['FName']
    Name2 = folks['LName']
    Age1 = folks['Age']
    City1 = folks['City'] 
    
    print(f"Here's Information about my brother: His name is {Nam1} {Name2},he is approximately {Age1} years old, and he lives in the city of {City1}.")

