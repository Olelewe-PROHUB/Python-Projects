#This program will take the input of a City and its resepective Country
#The return value will be a formatted string followed by a print statement

def get_city(city, country):
    """Return the City and Country"""
    place = f"{city}, {country}"
    return place

#Prints the location 
th1 = get_city('Havannah', 'Cuba')
th2 = get_city('Santiago', 'Chile')
th3 = get_city('Cape Town','South Africa')

print(th1)
print(th2)
print(th3)


