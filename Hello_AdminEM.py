#This program will review entries for different User Accounts and Provide 
#Confirmation if those names are available.

CurrNames = ['Danny','Freddy','Amarachi','Ogemdi','Sara','Admin','Patty','Chukwuemeka']

NamesInput = ['Danny','Freddy','Dick','Amarachi','Ogemdi','Sara','Admin']

if len(CurrNames) == 0:
         print("No users have been entered. Please provide a Username")
else:
    for logs in CurrNames:
  
        if logs in NamesInput:
             print(f"The Username {logs}, has already been taken.\n")

        else:
             print(f"The Username {logs} is available.\n")

   

