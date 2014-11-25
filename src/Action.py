#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: Action.py
# By: Daniel Lamothe
#
# Purpose: A simple object representing an Action a Creature can take. Used to house Action information.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Action:
    name = ''
    desc = ''
    attack = ''
    hit = ''

    # Default Constructor
    def __init__(self):
            pass

    # Constructor with provided parameters
    def __init__(self, name, desc, attack, hit):
        self.name = name
        self.desc = desc
        self.attack = attack
        self.hit = hit