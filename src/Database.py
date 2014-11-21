__author__ = 'User'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: Database.py
# By: Daniel Lamothe
#
# Purpose: CST8333 Demo for Assignment 04. Creates a database object which will handle the connection to the sqlite3
# database file and all data manipulations for a current session. Ensures any resources are closed when task is done.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sqlite3
import Creature


class Database:

    # Default Constructor
    def __init__(self):
        pass

    def handle_exception(e):
        print(e)
        pass

    @staticmethod
    def save(creature):
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
    def delete(creature):
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

    @staticmethod
    def read(creature_name):
        try:
            db = sqlite3.connect('db\cst8333.db')
            print("Opened database successfully.")
            cursor = db.cursor()

            var = str.format('''
                SELECT FROM CREATURE WHERE CREATURE.name = ?
            ''', creature_name)
            cursor.execute(var)

            # from the Creature Table
            for row in cursor:
                name = row[1]
                size = row[2]
                type = row[3]
                alignment = row[4]
                ac = row[5]
                hp = row[6]
                speed = row[7]
                attribute_ref = row[8]
                senses_ref = row[9]
                languages = row[10]
                challenge_rating = row[11]
                action_collection_ref = row[12]

            # from the Attributes Table
            var = str.format('''
                SELECT FROM ATTRIBUTES WHERE ATTRIBUTES.ID = ?
            ''', attribute_ref)
            cursor.execute(var)

            attributes = {}
            for row in cursor:
                attributes.__setitem__('STR', row[1])
                attributes.__setitem__('DEX', row[2])
                attributes.__setitem__('CON', row[3])
                attributes.__setitem__('INT', row[4])
                attributes.__setitem__('WIS', row[5])
                attributes.__setitem__('CHA', row[6])

            # from the Senses Table
            var = str.format('''
                SELECT FROM SENSES WHERE SENSES.ID = ?
            ''', senses_ref)
            cursor.execute(var)

            senses = {}
            for row in cursor:
                senses.__setitem__('DarkVision', row[1])
                senses.__setitem__('TremorSense', row[2])
                senses.__setitem__('BlindSense', row[3])

            # from the Action Collection Table
            var = str.format('''
                SELECT FROM ACTION_COLLECTION WHERE ACTION_COLLECTION.ID = ?
            ''', action_collection_ref)
            cursor.execute(var)

            action_collection = []
            for row in cursor:
                action_collection.append(row[int])

            # Retrieving the actions
            action_set = []
            for fk in action_collection:
                var = str.format('''
                    SELECT FROM ACTIONS WHERE ACTIONS.ID = ?
                ''', fk)
                cursor.execute(var)

                action = {}
                for row in cursor:
                    action.__setitem__('Name', row[1])
                    action.__setitem__('Description', row[2])
                    action.__setitem__('Attack', row[3])
                    action.__setitem__('Hit', row[4])

                # Add the Dictionary to the List ¯\_(ツ)_/¯
                action_set.append(action)
            my_creature = Creature.Creature(name, size, type, alignment, ac, hp, speed, attributes, senses, languages,
                                   challenge_rating, action_set)
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()

        return my_creature