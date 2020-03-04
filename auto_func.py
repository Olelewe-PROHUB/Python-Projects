#This program creates a function  requesting information on the car
#Make and Model  by default are entered, followed by three or more other details 

def build_profile(make, model, **auto_info):
    """Build a dictionary containing everything we know about a car."""
    auto_info['car_make'] = make
    auto_info['car_model'] = model
    return auto_info


