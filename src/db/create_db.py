#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: create_db.py
# By: Daniel Lamothe
#
# Purpose: Drops any existing tables and rebuilds the database architecture. To be used to wipe the database.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sqlite3

db = sqlite3.connect('db\cst8333.db')
print("Opened database successfully.")

# Clears the old database records [@DL to be removed later]
db.execute('DROP TABLE CREATURE')
db.execute('DROP TABLE ATTRIBUTES')
db.execute('DROP TABLE SENSES')
db.execute('DROP TABLE ACTION_COLLECTION')
db.execute('DROP TABLE ACTIONS')
db.commit()

db.execute('''
  CREATE TABLE IF NOT EXISTS ATTRIBUTES (
      id INTEGER PRIMARY KEY,
      strength INTEGER,
      dexterity INTEGER,
      constitution INTEGER,
      intelligence INTEGER,
      wisdom INTEGER,
      charisma INTEGER
      )
''')
print("ATTRIBUTE table created successfully.")

db.execute('''
  CREATE TABLE IF NOT EXISTS SENSES (
      id INTEGER PRIMARY KEY,
      darkvision TEXT,
      tremorsense TEXT,
      blindsense TEXT
      )
''')
print("SENSE table created successfully.")

db.execute('''
  CREATE TABLE IF NOT EXISTS ACTIONS (
      id INTEGER PRIMARY KEY,
      name TEXT,
      description TEXT,
      attack TEXT,
      hit TEXT
      )
''')
print("ACTION table created successfully.")

# ACTIONCOLLECTION table
db.execute('''
  CREATE TABLE IF NOT EXISTS ACTION_COLLECTION (
      id INTEGER PRIMARY KEY,
      action_ref integer NOT NULL,
      FOREIGN KEY (action_ref) REFERENCES ACTIONS(id)
      )
''')
print("ACTION table created successfully.")

# comes last due to foreign key requirements
db.execute('''
  CREATE TABLE IF NOT EXISTS CREATURE (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      size TEXT NOT NULL,
      type TEXT,
      alignment TEXT,
      ac INTEGER,
      hp TEXT,
      speed TEXT,
      attribute_ref INTEGER NOT NULL,
      senses_ref INTEGER NOT NULL,
      languages TEXT,
      challenge_rating TEXT,
      action_collection_ref INTEGER NOT NULL,
      FOREIGN KEY (attribute_ref) REFERENCES ATTRIBUTES(id) ON DELETE CASCADE,
      FOREIGN KEY (senses_ref) REFERENCES SENSES(id) ON DELETE CASCADE,
      FOREIGN KEY (action_collection_ref) REFERENCES ACTION_COLLECTION(id) ON DELETE CASCADE
      )
''')
print("CREATURE table created successfully.")

db.commit()
print("Changes saved.")

db.close()