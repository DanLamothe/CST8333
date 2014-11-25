#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: test\__init__.py
# By: Daniel Lamothe
#
# Purpose: Start-up file for testing the Fantasy Creature CRUD application. The developer uses this file to launch
#           test functions to simulate data entry.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import Creature
import Action
import Database


# Populates the database with a sample test record for testing, saves time.
def test_creature_create():
    attributes = {}
    senses = {}
    action_set = []

    #Create Attributes
    attributes.__setitem__('STR', 16)
    attributes.__setitem__('DEX', 15)
    attributes.__setitem__('CON', 18)
    attributes.__setitem__('INT', 22)
    attributes.__setitem__('WIS', 17)
    attributes.__setitem__('CHA', 13)

    #Create Senses
    senses.__setitem__('DarkVision', 'DarkVision 60ft.')
    senses.__setitem__('TremorSense', '')
    senses.__setitem__('BlindSense', '')

    myAction = Action.Action('Test_Action', 'Melee 5ft slash', '+5 to hit', '2d12 + 3 damage')
    action_set.append(myAction)

    #created_creature = Creat       (name, size, specification, alignment, ac, hp, speed, attributes, senses,
    #                                languages, challenge_rating, action_set)
    myCreature = Creature.Creature('Test', 'Small', 'Dragon', 'LG', 16, '100', '35 ft.', attributes, senses,
                                   'Draconic Common', '4', action_set)
    myCreature.save(True)


# Reads all database records and prints to console.
def test_creature_select():
    Database.Database.print_all_creatures(True)


# Tests delete functionality
def test_creature_delete():
    creature_name = input('Name of Creature to Delete:')
    Database.Database.delete(creature_name, True)


# Tests Read functionality
def test_creature_read():
    creature_name = input('Name of Creature to load into memory:')
    read_creature = Database.Database.read(creature_name, True)
    assert read_creature == isinstance(Creature.Creature)
    print(read_creature.name)
    return read_creature


# Tests export functionality
def test_creature_export():
    creature = test_creature_read()
    creature.export(creature.to_dict(), True)

# Creature Creation Test Code (Uncomment to test)
# test_creature_create()

# Creature SELECT Test Code (Uncomment to test)
#test_creature_select()

# Creature DELETE Test Code (Uncomment to test)
#test_creature_delete()
#test_creature_select()

# Creature Read Test Code (Uncomment to test)
#test_creature_select()
#test_creature_read()

# Creature Export Test Code (Uncomment to Test)
test_creature_select()
test_creature_export()
