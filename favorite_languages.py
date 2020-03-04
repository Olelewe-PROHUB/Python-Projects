#This program will provide a list of people that have conducted a poll
#If an individual has not completed a poll, they will be notified. If they have
#Taken the poll, they will be thanked for thier participation

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

Names = ['jen', 'sarah', 'nathaniel', 'edward', 'jacoby', 'lazar', 'phil']

for r in favorite_languages.keys():
   
    if r in Names:
        print(f"Thank You for participating in our poll {r.title()}!\n")

    else: 
        print(f"{r.title()}, you have not completed our poll")

