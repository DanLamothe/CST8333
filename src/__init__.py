#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: __init__.py
# By: Daniel Lamothe
#
# Purpose: CST8333 Demo for Assignment 04. Creates and populates the database with a sample creature. Reads the database
#   and stores the values in a Creature object. Manipulation of dictionary objects and the Template module, the script
#   substitutes values in the dictionary into the supplied HTML template. A new file is created depicting the creature
#   in statistical form.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'User'

import os
import Database
import Creature

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TASK 1: Setup the Database
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Runs the Create DB Library to create the application database
os.system(r'python db\create_db.py')

# Insert initial records into the database
os.system(r'python db\insert_db.py')

# Select the records to show they are indeed there
# os.system(r'python db\select_db.py')

print('\nTASK1 - Database successfully set up!\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TASK 2: UI
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

menu = {'0': "Exit", '1': "Create Creature", '2': "Export Creature"}

while True:
    options = menu.keys()

    print('Welcome to the Fantasy Creature Statblock Creator')
    print('Please enter a selection from the options below: ')
    print('-------------------------------------------------')
    print('(0) Exit')
    print('(1) Create')
    print('(2) Export Statblock')
    selection = input("\nPlease Select:")

    if selection == '0':
        print('\nGoodbye!')
        exit()

    elif selection == '1':
        pass

    elif selection == '2':
        menu_creature = Database.Database.read('Dire TunaFish')
        menu_creature.export(menu_creature.to_dict())

    else:
        print('Unknown option selected. Please try again.')

