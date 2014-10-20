'''
    Creates the database if it doesn't already exist.
    By: Daniel Lamothe
    Last Modified: 2014-10-19
'''

__author__ = 'User'


import sqlite3

db = sqlite3.connect('cst8333.db')
print("Opened database successfully.")

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
      action_ref integer NOT NULL
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
      FOREIGN KEY (attribute_ref) REFERENCES ATTRIBUTES(id),
      FOREIGN KEY (senses_ref) REFERENCES SENSES(id),
      FOREIGN KEY (action_collection_ref) REFERENCES ACTION_COLLECTION(id)
      )
''')
print("CREATURE table created successfully.")

db.commit()
print("Changes saved.")

db.close()