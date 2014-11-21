__author__ = 'User'

import Action

my_dict = {}
my_dict.__setitem__('name', '')
my_dict.__setitem__('size', '')
my_dict.__setitem__('specification', '')
my_dict.__setitem__('alignment', '')
my_dict.__setitem__('ac', 0)
my_dict.__setitem__('hp', '')
my_dict.__setitem__('speed', '')
my_dict.__setitem__('attribute_str', 0)
my_dict.__setitem__('attribute_dex', 0)
my_dict.__setitem__('attribute_con', 0)
my_dict.__setitem__('attribute_int', 0)
my_dict.__setitem__('attribute_wis', 0)
my_dict.__setitem__('attribute_cha', 0)
my_dict.__setitem__('senses', {'DarkVision': '', 'TremorSense': '', 'BlindSense': ''})
my_dict.__setitem__('languages', '')
my_dict.__setitem__('challenge_rating', '')
my_dict.__setitem__('action_set', []) #list of actions...

print('You will be prompted for values representing a creature. Press X to exit at any time')
selection = ''
while selection != 'x':
    for item in my_dict:
        selection = input('Name:')
        my_dict.__setitem__('name', selection)

        selection = input('Size:')
        my_dict.__setitem__('size', selection)

        selection = input('Specification:')
        my_dict.__setitem__('specification', selection)

        selection = input('Alignment:')
        my_dict.__setitem__('alignment', selection)

        selection = input('Armor Class (int):')
        my_dict.__setitem__('ac', selection)

        selection = input('Hit Points:')
        my_dict.__setitem__('hp', selection)

        selection = input('Speed (feet):')
        my_dict.__setitem__('speed', selection)

        selection = input('Strength (Int)')
        my_dict.__setitem__('attribute_str', selection)

        selection = input('Dexterity (Int)')
        my_dict.__setitem__('attribute_dex', selection)

        selection = input('Constitution (Int)')
        my_dict.__setitem__('attribute_con', selection)

        selection = input('Intelligence (Int)')
        my_dict.__setitem__('attribute_int', selection)

        selection = input('Wisdom (Wis)')
        my_dict.__setitem__('attribute_wis', selection)

        selection = input('Charisma (Int)')
        my_dict.__setitem__('attribute_cha', selection)

        selection = input('Senses: DarkVision?')
        my_dict.__setitem__('senses'['DarkVision'], selection)

        selection = input('Senses: TremorSense?')
        my_dict.__setitem__('senses'['TremorSense'], selection)

        selection = input('Senses: BlindSense?')
        my_dict.__setitem__('senses'['BlindSense'], selection)

        selection = input('Languages:')
        my_dict.__setitem__('languages', selection)

        selection = input('Challenge Rating:')
        my_dict.__setitem__('challenge_rating', selection)

        # Build an Action
        action_name = ''
        action_desc = ''
        action_attack = ''
        action_hit = ''

        selection = input('Action Name:')
        action_name = selection

        selection = input('Action Descriptor:')
        action_desc = selection

        selection = input('Attack Modifier to Hit:')
        action_attack = selection

        selection = input('Attack Damage:')
        action_hit = selection

        creature_action = Action(action_name, action_desc, action_attack, action_hit)
        my_dict.__setitem__('action_set', [].append(creature_action))