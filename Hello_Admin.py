#This program will review entries for different User Accounts and Provide 
#Greetings to those Users that are valid

Logins = []

ValidLog = ['Danny','Freddy','Dick','Amarachi','Ogemdi','Sara','Admin']

for logs in Logins:
    if logs == []:
         print("No users have been entered. Please provide a Username")

    elif logs == 'Admin' and logs in ValidLog:
         print("Welcome System Administrator! Would you like an Activity Report         ?\n")

    elif logs in ValidLog:
         print(f"Welcome {logs.upper()}! Please press ENTER to continue.\n")

    else:
         print(f"{logs.upper()} is not a valid Username. Please try again.\n") 


