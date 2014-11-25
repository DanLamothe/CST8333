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
import CreateCreature



print('\nTASK1 - Database successfully set up!\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TASK 2: UI
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

menu = {'0': "Exit", '1': "Create Creature", '2': "Export Creature"}

while True:
    options = menu.keys()

    print('\n\nWelcome to the Fantasy Creature Statblock Creator')
    print('Please enter a selection from the options below: ')
    print('-------------------------------------------------')
    print('(0) Exit')
    print('(1) View Creature Records')
    print('(2) Export Statblock')
    print('(3) Create a Creature')
    print('(4) Update an Existing Creature')
    print('(5) Delete an Existing Creature')
    selection = input("\nPlease Select your option:")

    if selection == '0':
        print('\nGoodbye!')
        exit()

    # Creates a Creature Object through Prompts, saves the completed Creature into the database
    elif selection == '1':
        Database.Database.print_all_creatures(False)

    elif selection == '2':
        user_input = input('Name of Creature: ')
        menu_creature = Database.Database.read(user_input, False)
        menu_creature.export(menu_creature.to_dict())

    elif selection == '3':
        CreateCreature.prompt_create().save(False)

    elif selection == '5':
        user_input = input('Name of Creature: ')
        Database.Database.delete(user_input, False)

    else:
        print('Unknown option selected. Please try again.')

