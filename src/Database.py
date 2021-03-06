# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: Database.py
# By: Daniel Lamothe
#
# Purpose: Data Access layer for the application. Recevieves references to a Creature object to persist/update, or the
#           name of an existing database record for deletion. Can also read records from the database.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sqlite3
import Creature


class Database:
    # These Module Variables are used to differentiate between testing and production db access
    project_db_location = 'db\cst8333.db'
    test_db_location = '..\src\db\cst8333.db'

    # Default Constructor
    def __init__(self):
        pass

    # Function handles simple exceptions for debug purposes
    def handle_exception(e):
        print(e)
        pass

    # Reads and prints all records in the database.
    @staticmethod
    def print_all_creatures(is_test):
        if is_test:
            db = sqlite3.connect('..\src\db\cst8333.db')
        else:
            db = sqlite3.connect('db\cst8333.db')
        print("Opened database successfully.")
        cursor = db.execute("SELECT * FROM CREATURE")
        for row in cursor:
            print(row)
        db.close()

    # Provided a reference to a Creature object, persists it in the database.
    @staticmethod
    def save(creature, is_test):
        try:
            if is_test:
                db = sqlite3.connect('..\src\db\cst8333.db')
            else:
                db = sqlite3.connect('db\cst8333.db')
            print("Opened database successfully.")
            cursor = db.cursor()

            # Loops through the list of action dictionaries and persists them
            rowid_action_list = []
            for action in creature.actionSet:
                cursor.execute('INSERT INTO ACTIONS (name, description, attack, hit) VALUES (?, ?, ?, ?)',
                               (action.name, action.desc, action.attack, action.hit))
                rowid_action_list.append(cursor.lastrowid)

            # Loops and registers each action record to an action_collection
            for integer in rowid_action_list:
                cursor.execute('INSERT INTO ACTION_COLLECTION (action_ref) VALUES (?)', (integer,))
            rowid_action_collection = cursor.lastrowid

            # Inserts records for Sense tablecreate_senses
            db.execute('INSERT INTO SENSES (darkvision, tremorsense, blindsense) VALUES (?, ?, ?)',
                       (creature.senses.get('DarkVision'), creature.senses.get('TremorSense'),
                        creature.senses.get('BlindSense')))
            rowid_sense = cursor.lastrowid

            # Inserts records for Attributes table
            db.execute('''INSERT INTO ATTRIBUTES (strength, dexterity, constitution, intelligence, wisdom, charisma)
                VALUES(?, ?, ?, ?, ?, ?)''',
                       (creature.attributes.get('STR'),
                        creature.attributes.get('DEX'),
                        creature.attributes.get('CON'),
                        creature.attributes.get('INT'),
                        creature.attributes.get('WIS'),
                        creature.attributes.get('CHA')))
            rowid_attributes = cursor.lastrowid

            # Inserts the creature object into the Creature table
            db.execute('''
              INSERT INTO CREATURE (name, size, type, alignment, ac, hp, speed, attribute_ref, senses_ref, languages,
              challenge_rating, action_collection_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''', (creature.name, creature.size, creature.type, creature.alignment, creature.ac, creature.hp,
                    creature.speed, rowid_attributes, rowid_sense, creature.languages, creature.challenge,
                    rowid_action_collection))
            db.commit()
            print("Changes saved.")

        except Exception as e:
            print(e)
            print(e.l)
            db.rollback()
        finally:
            db.close()

    # Provided a reference to a Creature object and the original record's name, updates the exiting record
    @staticmethod
    def update(creature, original_name, is_test):
        try:
            if is_test:
                db = sqlite3.connect('..\src\db\cst8333.db')
            else:
                db = sqlite3.connect('db\cst8333.db')
            print("Opened database successfully.")
            cursor = db.cursor()

            # Retrieve Foreign Keys
            cursor.execute('SELECT action_collection_ref FROM CREATURE WHERE CREATURE.name = ?', (original_name,))
            u_action_collection_ref = cursor.fetchone()

            cursor.execute('SELECT action_ref FROM ACTION_COLLECTION WHERE id = ?', (u_action_collection_ref,))
            u_action_ref = cursor.fetchone()

            cursor.execute('SELECT senses_ref FROM CREATURE WHERE CREATURE.name = ?', (original_name,))
            u_senses_ref = cursor.fetchone()

            cursor.execute('SELECT attribute_ref FROM CREATURE WHERE CREATURE.name = ?', (original_name,))
            u_attribute_ref = cursor.fetchone()

            # Update Creature Table
            cursor.execute(
                '''UPDATE CREATURE SET name = ?, size = ?, type = ?, alignment = ?, ac = ?, hp = ?, speed = ?, languages = ?, challenge_rating = ? WHERE CREATURE.name = ?''',
                (creature.name, creature.size, creature.type,
                 creature.alignment, creature.ac, creature.hp, creature.speed,
                 creature.languages, creature.challenge, original_name))

            # Update Senses Table
            cursor.execute('''UPDATE SENSES SET darkvision = ?, tremorsense = ?, blindsense = ? WHERE id = ?''', (
                creature.senses.get('DarkVision'), creature.senses.get('TremorSense'),
                creature.senses.get('BlindSense'),
                u_senses_ref))

            # Update Attribute Table
            cursor.execute(
                '''UPDATE ATTRIBUTES SET strength = ?, dexterity = ?, constitution = ?, intelligence = ?, wisdom = ?, charisma = ? WHERE id = ?''',
                (
                    creature.get('STR'), creature.get('DEX'), creature.get('CON'), creature.get('INT'),
                    creature.get('WIS'),
                    creature.get('CHA'), u_attribute_ref))

            # Update Action Table
            cursor.execute(
                '''UPDATE ACTIONS SET name = ?, description = ?, attack = ?, hit = ? WHERE id = ?''', (
                creature.actionSet[0].name, creature.actionSet[0].desc, creature.actionSet[0].attack,
                creature.actionSet[0].hit, u_action_ref)
            )

            db.commit()
            print("Changes saved.")

        except Exception as e:
            print('***The Following Exception Occurred: ')
            print(e)
            db.rollback()
        finally:
            db.close()

    # Provided a name of an existing creature record, deletes the record.
    @staticmethod
    def delete(creature_name, is_test):
        try:
            if is_test:
                db = sqlite3.connect('..\src\db\cst8333.db')
            else:
                db = sqlite3.connect('db\cst8333.db')
            print("Opened database successfully.")

            cursor = db.cursor()

            # Turns on Foreign Key Constraint for cascade delete
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('DELETE FROM CREATURE WHERE CREATURE.name = ?', (creature_name,))
            db.commit()
            print("Changes saved.")

        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()

    # Provided the name of an existing creature record, restores the creature from the database into memory
    @staticmethod
    def read(creature_name, is_test):
        try:
            if is_test:
                db = sqlite3.connect('..\src\db\cst8333.db')
            else:
                db = sqlite3.connect('db\cst8333.db')
            print("Opened database successfully.")
            cursor = db.cursor()
            print('*** Cursor set')

            cursor.execute('SELECT * FROM CREATURE WHERE name = ?', (creature_name,))
            print('***Execute SELECT')

            # from the Creature Table, *** Might throw an error if more than 1 creature_name is selected...
            for row in cursor:
                print(row)
                name = row[1]
                size = row[2]
                specification = row[3]
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
            cursor.execute('SELECT * FROM ATTRIBUTES WHERE ATTRIBUTES.ID = ?', (attribute_ref,))
            attributes = {}
            for row in cursor:
                print(row)
                attributes.__setitem__('STR', str(row[1]))
                attributes.__setitem__('DEX', str(row[2]))
                attributes.__setitem__('CON', str(row[3]))
                attributes.__setitem__('INT', str(row[4]))
                attributes.__setitem__('WIS', str(row[5]))
                attributes.__setitem__('CHA', str(row[6]))

            # from the Senses Table
            cursor.execute('SELECT * FROM SENSES WHERE SENSES.ID = ?', (senses_ref,))
            senses = {}
            for row in cursor:
                print(row)
                senses.__setitem__('DarkVision', row[1])
                senses.__setitem__('TremorSense', row[2])
                senses.__setitem__('BlindSense', row[3])
                print(senses.get('TremorSense'))

            # from the Action Collection Table
            cursor.execute('SELECT * FROM ACTION_COLLECTION WHERE ACTION_COLLECTION.ID = ?', (action_collection_ref,))

            action_collection = []
            for row in cursor:
                print(row)
                action_collection.append(row[1])

            # Retrieving the actions
            action_set = []
            for fk in action_collection:
                cursor.execute('SELECT * FROM ACTIONS WHERE ACTIONS.ID = ?', (str(fk),))

                action = {}
                for row in cursor:
                    print(row)
                    action.__setitem__('Name', row[1])
                    action.__setitem__('Description', row[2])
                    action.__setitem__('Attack', row[3])
                    action.__setitem__('Hit', row[4])

                # Add the Dictionary to the List ¯\_(ツ)_/¯
                action_set.append(action)
            this_creature = Creature.Creature(name, size, specification, alignment, ac, hp, speed, attributes,
                                              senses, languages, challenge_rating, action_set)
        except Exception as e:
            print('*** The Following Exception Occurred:')
            print(e)
            db.rollback()
        finally:
            db.close()

        return this_creature