__author__ = 'User'


class Action:
    name = ''
    desc = ''
    attack = ''
    hit = ''

    # Default Constructor
    def __init__(self):
            pass

    def __init__(self, name, desc, attack, hit):
        self.name = name
        self.desc = desc
        self.attack = attack
        self.hit = hit