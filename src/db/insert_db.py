__author__ = 'User'

import sqlite3

__name__ = "insert_db"


def create_tuna_fish():
    db = sqlite3.connect('db\cst8333.db')
    print("Opened database successfully.")

    # Creates the Dire Tuna Fish creature
    db.execute('''
      INSERT INTO ACTIONS (name, description, attack, hit)
        VALUES ("Slam", "Melee natural attack", "+7 to hit, reach 5ft., one target", "13 (2d8+4) bludgeoning damage" )
    ''')

    db.execute('''
      INSERT INTO ACTION_COLLECTION (action_ref)
        VALUES (1)
    ''')

    db.execute('''
      INSERT INTO SENSES (darkvision)
        VALUES ("Darkvision 40ft.")
    ''')
    db.execute('''
      INSERT INTO ATTRIBUTES (strength, dexterity, constitution, intelligence, wisdom, charisma)
        VALUES (17, 14, 15, 5, 10, 5 )
    ''')
    db.execute('''
      INSERT INTO CREATURE (name, size, type, alignment, ac, hp, speed, attribute_ref, senses_ref, languages, challenge_rating, action_collection_ref)
        VALUES ("Dire TunaFish", "Large", "beast", "true neutral", 12, "59 (7d10+21)", "70ft. (swim)", 1, 1, NULL, "2 (450xp)", 1)
    ''')
    db.commit()
    print("Changes saved.")
    db.close()


# Creates the Dire Tuna Fish creature
def create_creature(creature):
    db = sqlite3.connect('db\cst8333.db')
    print("Opened database successfully.")
    cursor = db.cursor()

    # Loops through the list of action dictionaries and persists them
    rowid_action_list = []
    for action in creature.actionSet:
        insert_action = str.format('''
            INSERT INTO ACTIONS (name, description, attack, hit)
            VALUES (?, ?, ?, ?, ?)
        ''', (action.name, action.description, action.attack, action.hit))
        cursor.execute(insert_action)
        rowid_action_list.append(cursor.lastrowid)

    # Loops and registers each action record to an action_collection
    for integer in rowid_action_list:
        insert_action_collection = str.format(format('''
        INSERT INTO ACTION_COLLECTION (action_ref)
        VALUES (?)
        ''', integer))
        cursor.execute(insert_action_collection)

    rowid_action_collection = cursor.lastrowid

    # Inserts records for Sense tablecreate_senses
    insert_senses = str.format('''
        INSERT INTO SENSES (darkvision, tremorsense, blindsense)
        VALUES (?, ?, ?)
    ''', (creature.senses.get('DarkVision'), creature.senses.get('TremorSense'), creature.senses.get('BlindSense')))
    db.execute(insert_senses)
    rowid_sense = cursor.lastrowid

    # Inserts records for Attributes table
    insert_attributes = str.format('''
        INSERT INTO ATTRIBUTES (strength, dexterity, constitution, intelligence, wisdom, charisma)
        VALUES (?, ?, ?, ?, ?, ?)
    ''',
                                   (creature.attributes.get('STR')),
                                   (creature.attributes.get('DEX')),
                                   (creature.attributes.get('CON')),
                                   (creature.attributes.get('INT')),
                                   (creature.attributes.get('WIS')),
                                   (creature.attributes.get('CHA'))
    )
    db.execute(insert_attributes)
    rowid_attributes = cursor.lastrowid

    # Inserts the creature object into the Creature table
    insert_creature = str.format('''
      INSERT INTO CREATURE (name, size, type, alignment, ac, hp, speed, attribute_ref, senses_ref, languages, challenge_rating, actions_ref)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (creature.name, creature.size, creature.type, creature.ac, creature.hp, creature.speed, rowid_attributes,
          rowid_sense, creature.languages, creature.challenge, rowid_action_collection))
    db.execute(insert_creature)

    db.commit()
    print("Changes saved.")

    db.close()

# Creates the basic dire tunafish as seen in Exercise 04
create_tuna_fish()
