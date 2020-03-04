#This program will create several conditional statements
#And determine if they are True or False

watch = 'Garmin'

collection = ['Seiko','Casio','Breitling','Garmin']

for col in collection:
    if col == watch:
       print(f"This is a {col.title()}")
    else:
       print(col)


