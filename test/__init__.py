__author__ = 'User'


import Creature
import Action
import sqlite3
import Database


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
    myCreature.save(1)


def test_creature_select():
    db = sqlite3.connect('..\src\db\cst8333.db')
    print("Opened database successfully.")
    cursor = db.execute("SELECT * from CREATURE")
    for row in cursor:
        print(row)
    print("Operation performed successfully.")
    db.close()


def test_creature_delete():
    creature_name = input('Name of Creature to Delete:')
    Database.Database.delete(creature_name, 1)
# Creature Creation Test Code (Uncomment to test)
# test_creature_create()

# Creature SELECT Test Code (Uncomment to test)
test_creature_select()

# Creature DELETE Test Code
test_creature_delete()
test_creature_select()
