#This program creates a function that accepts two characters
#A city name and a country name are provided

def getplace(city_name, country, population=''):
    """Define the location within a country"""
    
    if population:
        location = f"{city_name}, {country} - population {population}"
    else:
        location = f"{city_name}, {country}"
    return location.title()


