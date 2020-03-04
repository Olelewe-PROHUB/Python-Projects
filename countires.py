#This program generates a statement about the location of a city
#The default value is Denver, United States

def cities(city_name = 'Denver', country_name = 'United States'):
    """Display information about a city."""
    print(f"{city_name.title()} is in {country_name.title()}\n")

cities()
cities(city_name = 'Los Angeles')
cities(city_name = 'Reykjavik', country_name = 'Iceland')
cities(city_name = 'Budapest', country_name = 'Hungary')
