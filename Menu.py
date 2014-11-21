__author__ = 'User'


menu = {'0': "Exit", '1': "Create Creature", '2': "Export Creature"}

while True:
    options = menu.keys()
    menu.sort()
    for entry in options:
        print(entry, menu[entry])
    selection = input("\nPlease Select:")
    if selection == '0':
        print('\nGoodbye!')
        exit()
    elif selection == '1':
        pass
    elif selection == '2':
        my_creature = Database.Database.read('Dire TunaFish')
        my_creature.export(my_creature.to_dict())
    else:
        print('Unknown option selected. Please try again.')
