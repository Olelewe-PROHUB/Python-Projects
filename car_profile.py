#This program creates a car profile by requesting information on the car
#Make and Model  by default are entered, followed by three or more other details 

def build_profile(make, model, **auto_info):
    """Build a dictionary containing everything we know about a car."""
    auto_info['car_make'] = make
    auto_info['car_model'] = model
    return build_profile

auto_profile = build_profile('Mazda', 'CX-5', color = 'Black', type = 'SUV', crossover = 'Yes')

print(auto_profile)
