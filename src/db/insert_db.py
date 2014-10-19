__author__ = 'User'

import sqlite3

db = sqlite3.connect('cst8333.db')
print("Opened database successfully.")

# Creates the Dire Tuna Fish creature
db.execute('''
  INSERT INTO ACTIONS (id, name, description, attack, hit)
    VALUES (1, "Slam", "Melee natural attack", "+7 to hit, reach 5ft., one target", "13 (2d8+4) bludgeoning damage" )
''')

db.execute('''
  INSERT INTO SENSES (id, darkvision)
    VALUES (1, "Darkvision 40ft.")
''')

db.execute('''
  INSERT INTO ATTRIBUTES (id, strength, dexterity, constitution, intelligence, wisdom, charisma)
    VALUES (1, 17, 14, 15, 5, 10, 5 )
''')

db.execute('''
  INSERT INTO CREATURE (id, name, size, type, alignment, ac, hp, speed, attribute_ref, senses_ref, languages, challenge_rating, actions_ref)
    VALUES (1, "Dire Tuna Fish", "Large", "beast", "true neutral", 12, "59 (7d10+21)", "70ft. (swim)", 1, 1, null, "2 (450xp)", 1)
''')

db.commit()
print("Changes saved.")