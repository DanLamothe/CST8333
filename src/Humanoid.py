import Creature


class Humanoid(Creature):

    def __init__(self):
        has_opposable_thumbs = True

    def more_defense(self):
        if self.Creature.ac < 10:
            self.Creature.ac += 3