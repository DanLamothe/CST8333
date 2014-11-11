__author__ = 'User'

'''
    Name: Creature.py
    By: Daniel Lamothe
    Last Modified: 2014-10-19

    Purpose: A Python class that representing a collection of information and statistics representing a creature in a
            fantasy RPG.
'''


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

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    __init__()