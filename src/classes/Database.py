__author__ = 'User'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: Database.py
# By: Daniel Lamothe
#
# Purpose: CST8333 Demo for Assignment 4. Creates a database object which will handle the connection to the sqlite3
# database file and all data manipulations for a current session. Ensures any resources are closed when task is done.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sqlite3


class Database:
    # Data Members
        # Connection Variable
        # Cursor Variable

    # Default Constructor
    def __init__(self):
        pass

    def handle_exception(e):
        print(e)
        pass

    @staticmethod
    def save(self, creature):
        try:
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
              INSERT INTO CREATURE (name, size, type, alignment, ac, hp, speed, attribute_ref, senses_ref, languages,
                challenge_rating, actions_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (creature.name, creature.size, creature.type, creature.ac, creature.hp, creature.speed,
                  rowid_attributes, rowid_sense, creature.languages, creature.challenge, rowid_action_collection))
            db.execute(insert_creature)

            db.commit()
            print("Changes saved.")

        except Exception as e:
            print(e)
            db.rollback()
        else:
            print("Unknown Error... Exiting")
            db.rollback()
        finally:
            db.close()

    def update(self, creature):
        pass

    @staticmethod
    def delete(self, creature):
        try:
            db = sqlite3.connect('db\cst8333.db')
            print("Opened database successfully.")

            cursor = db.cursor()

            # Turns on Foreign Key Constraint for cascade delete
            cursor.execute('PRAGMA foreign_keys = ON;')

            var = str.format('''
                DELETE FROM CREATURE WHERE CREATURE.name = ?
            ''', creature.name)

            cursor.execute(var)
            db.commit()
            print("Changes saved.")

        except Exception as e:
            print(e)
            db.rollback()
        else:
            print("Unknown Error... Exiting")
            db.rollback()
        finally:
            db.close()

