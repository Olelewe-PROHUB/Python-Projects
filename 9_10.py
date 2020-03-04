#Imports all the classes from the module PermissionsModule
#Will create an instance of Admin and call the function show_privleges
#To show that everything is working correctly

import PermissionsModule
"""This imports the PermissionsModule"""

#Here we will make an instance of the class Admin, followed by a call
#Of the method show_privleges

special = PermissionsModule.Admin('Paul', 'Barnhart', 25, 'Masonville')

special.priv.display_priv()
