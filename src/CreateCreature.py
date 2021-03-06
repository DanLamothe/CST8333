#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: CreateCreature.py
# By: Daniel Lamothe
#
# Purpose: Called by the __init__.py module, this module holds the prompt_create() function which prompts the user for
#           information to create a a Creature object. Returns a reference to an instantiated Creature.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import Action
import Creature


def prompt_create():
    selection = ''
    attributes = {}
    senses = {}
    action_set = []

    #Create Attributes dictionary
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

    my_action = Action.Action('Test_Action', 'Melee 5ft slash', '+5 to hit', '2d12 + 3 damage')
    action_set.append(my_action)

    created_creature = Creature.Creature('Test', 'Small', 'Dragon', 'LG', 16, '100', '35 ft,', attributes, senses,
                                   'Draconic Common', '4', action_set)
    print('You will be prompted for values representing a creature. Press X to exit at any time')
    # allows quitting early
    while selection != 'x':
            selection = input('Name:')
            name = selection

            selection = input('Size:')
            size = selection

            selection = input('Specification:')
            specification = selection

            selection = input('Alignment:')
            alignment = selection

            selection = input('Armor Class (int):')
            ac = selection

            selection = input('Hit Points:')
            hp = selection

            selection = input('Speed (feet):')
            speed = selection

            selection = input('Strength (Int)')
            attributes.__setitem__('STR', selection)

            selection = input('Dexterity (Int)')
            attributes.__setitem__('DEX', selection)

            selection = input('Constitution (Int)')
            attributes.__setitem__('CON', selection)

            selection = input('Intelligence (Int)')
            attributes.__setitem__('INT', selection)

            selection = input('Wisdom (Wis)')
            attributes.__setitem__('WIS', selection)

            selection = input('Charisma (Int)')
            attributes.__setitem__('CHA', selection)

            selection = input('Senses: DarkVision?')
            senses.__setitem__('DarkVision', selection)

            selection = input('Senses: TremorSense?')
            senses.__setitem__('TremorSense', selection)

            selection = input('Senses: BlindSense?')
            senses.__setitem__('BlindSense', selection)

            selection = input('Languages:')
            languages = selection

            selection = input('Challenge Rating:')
            challenge_rating = selection

            # Build an Action
            selection = input('Action Name:')
            action_name = selection

            selection = input('Action Descriptor:')
            action_desc = selection

            selection = input('Attack Modifier to Hit:')
            action_attack = selection

            selection = input('Attack Damage:')
            action_hit = selection

            creature_action = Action.Action(action_name, action_desc, action_attack, action_hit)
            assert isinstance(creature_action, Action.Action)

            # Assign Creature Action
            action_set.append(creature_action)

            # Create the Creature
            created_creature = Creature.Creature(name, size, specification, alignment, ac, hp, speed, attributes, senses, languages, challenge_rating, action_set)

            assert isinstance(created_creature, Creature.Creature)
            selection = 'x'
    try:
        return created_creature
    except Exception as e:
        print('Creature Creation stopped before completion.')
        print(e)