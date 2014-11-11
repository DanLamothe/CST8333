__author__ = 'User'

'''
    Name: Creature.py
    By: Daniel Lamothe
    Last Modified: 2014-10-19

    Purpose: A Python class that representing a collection of information and statistics representing a creature in a
            fantasy RPG.
'''
import Database
from string import Template

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
        self.senses = '{0}, {1}, {2}'.format(senses['DarkVision'], senses['TremorSense'], senses['BlindSense'])
        self.languages = languages
        self.challenge = challenge
        self.actionSet = actionSet

    def save(self):
        Database.Database.save(self)

    def update(self):
        pass

    def delete(self):
        Database.Database.delete(self)

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
        my_dict.__setitem__('challenge', self.name)

        # Only handles 1 attack atm.
        my_dict.__setitem__('attack', self.name)
        my_dict.__setitem__('attackDescription', self.name)
        my_dict.__setitem__('attackHit', self.name)
        my_dict.__setitem__('attackDamage', self.name)

        return my_dict

    @staticmethod
    def export(my_dict):
        try:
            # Open the template'
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
