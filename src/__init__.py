#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: __init__.py
# By: Daniel Lamothe
#
# Purpose: Start-up file for the Fantasy Creature CRUD application. This script prompts the user for basic choices to
#           guide the progression of the application.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import Database
import CreateCreature
import Creature

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
    print('(4) Update an Existing Creature - BETA')
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
        menu_creature.export(menu_creature.to_dict(), False)

    elif selection == '3':
        CreateCreature.prompt_create().save(False)

    # Update functionality is in Beta, not guaranteed to work.
    elif selection == '4':
        u_creature = Creature.Creature('','','','','','','','','','','','',)
        u_creature.update(False)

    elif selection == '5':
        user_input = input('Name of Creature: ')
        Database.Database.delete(user_input, False)

    else:
        print('Unknown option selected. Please try again.')