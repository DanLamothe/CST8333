__author__ = 'User'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: Creature.py
# By: Daniel Lamothe
#
# Purpose: A Python class that representing a collection of information and statistics representing a creature in a
#          fantasy RPG.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import Database
from string import Template
import Action


class Creature:
    # Data Members
    name = ''
    size = ''
    type = ''
    alignment = ''
    ac = 10
    hp = ''
    speed = ''
    attributes = {'STR': 10,
                  'DEX': 10,
                  'CON': 10,
                  'INT': 10,
                  'WIS': 10,
                  'CHA': 10}
    senses = {'DarkVision': '', 'TremorSense': '', 'BlindSense': ''}
    languages = ''
    challenge = ''
    actionSet = []
    action = {'Name': '', 'Description': '', 'Attack': '', 'Hit': ''}

    # Default Constructor
    def __init__(self):
        pass

    def __init__(self, name, size, type, alignment, ac, hp, speed, attributes, senses, languages, challenge, actionSet):
        self.name = name
        self.size = size
        self.type = type
        self.alignment = alignment
        self.ac = ac
        self.hp = hp
        self.speed = speed
        self.attributes = attributes

        self.senses = senses
        self.languages = languages
        self.challenge = challenge
        self.actionSet = actionSet

        # need Action (Created Elsewhere, already attached in actionSet)

    def save(self, is_test):
        if is_test:
            Database.Database.save(self, True)
        else:
            Database.Database.save(self, False)

    def update(self, is_test):
        user_choice = input('\nAlter Creature MetaData? (Y/N)')
        original_name = self.name
        if user_choice == 'Y' or 'y':
            self.name = input('Name: ')
            self.size = input('Size: ')
            self.type = input('Specifications ')
            self.alignment = input('Alignment: ')
            self.ac = input('Armor Class (int): ')
            self.hp = input('Hit Points: ')
            self.speed = input('Speed(s): ')
            self.languages = input('Known Language(s): ')
            self.challenge = input('Challenge Rating: ')

        user_choice = input('\nAlter Creature Attribute Scores? (Y/N)')
        if user_choice == 'Y' or 'y':
            self.attributes.__setitem__('STR', int(input('Strength (int): ')))
            self.attributes.__setitem__('DEX', int(input('Dexterity (int): ')))
            self.attributes.__setitem__('CON', int(input('Constitution (int): ')))
            self.attributes.__setitem__('INT', int(input('Intelligence (int): ')))
            self.attributes.__setitem__('WIS', int(input('Wisdom (int): ')))
            self.attributes.__setitem__('CHA', int(input('Charisma (int): ')))

        user_choice = input('\nAlter Creature Senses? (Y/N)')
        if user_choice == 'Y' or 'y':
            self.senses.__setitem__('DarkVision', input('DarkVision (Nullable): '))
            self.senses.__setitem__('BlindSense', input('BlindSense (Nullable): '))
            self.senses.__setitem__('TremorSense', input('TremorSense (Nullable): '))

        user_choice = input('\nAlter Creature Action? (Y/N)')
        if user_choice == 'Y' or 'y':
            a_name = input('Action Name: ')
            a_desc = input('Action Description: ')
            a_attack = input('Modifiers to Hit: ')
            a_hit = input('Damage on Hit: ')
            self.actionSet[0] = Action.Action(a_name, a_desc, a_attack, a_hit)

        print('Attempting Update...')
        Database.Database.update(self, original_name, is_test)

    def delete(self, is_test):
        if is_test:
            Database.Database.delete(self.name, True)
        else:
            Database.Database.delete(self.name, False)

    def to_dict(self):
        my_dict = {}
        my_dict.__setitem__('name', self.name)
        my_dict.__setitem__('type', self.type)
        my_dict.__setitem__('size', self.size)
        my_dict.__setitem__('alignment', self.alignment)
        my_dict.__setitem__('ac', self.ac)
        my_dict.__setitem__('hp', self.hp)
        my_dict.__setitem__('speed', self.speed)
        my_dict.__setitem__('str', self.attributes.get('STR'))
        my_dict.__setitem__('dex', self.attributes.get('DEX'))
        my_dict.__setitem__('con', self.attributes.get('CON'))
        my_dict.__setitem__('int', self.attributes.get('INT'))
        my_dict.__setitem__('wis', self.attributes.get('WIS'))
        my_dict.__setitem__('cha', self.attributes.get('CHA'))
        my_dict.__setitem__('senses', self.senses)
        my_dict.__setitem__('languages', self.languages)
        my_dict.__setitem__('challenge', self.challenge)

        # Only handles 1 attack atm.
        my_dict.__setitem__('attack', self.actionSet[0]['Name'])
        my_dict.__setitem__('attackDescription', self.actionSet[0]['Description'])
        my_dict.__setitem__('attackHit', self.actionSet[0]['Attack'])
        my_dict.__setitem__('attackDamage', self.actionSet[0]['Hit'])

        return my_dict

    def to_string(self):
        print(str(self))

    @staticmethod
    def export(my_dict, is_test):
        try:
            # Open the template'
            if is_test:
                file_in = open(r'..\src\templates\BasicCreatureBlock.html', 'r')
            else:
                file_in = open(r'templates\BasicCreatureBlock.html', 'r')

            # Read the statblock
            src = Template(file_in.read())

            # Create a destination file
            file_name = str.format('{}_StatBlock.html', my_dict.get('name').strip())
            file_out = open(file_name, 'w')

            # Make the substitutions
            file_out.write(src.substitute(my_dict))
        except Exception as e:
            print(e)
        finally:
            # Free resources by closing the destination file. Will be found in the src folder. Can open in browser.
            file_out.close()
            print('{}_StatBlock.html created!', my_dict.get('name').strip())
            # close the template
            file_in.close()
