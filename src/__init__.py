#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: __init__.py
# By: Daniel Lamothe
#
# Purpose: CST8333 Demo for Assignment 3. Creates and populates the database with a sample creature. Reads the database
#   and stores the values in a Dictionary object. Using the Dictionary object and the Template module, the script
#   substitutes values in the dictionary into the supplied HTML template. A new file is created depicting the creature
#   in statistical form.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'User'

import os
import sqlite3
from string import Template


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TASK 1: Setup the Database
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Runs the Create DB Library to create the application database
os.system(r'python db\create_db.py')

# Insert initial records into the database
os.system(r'python db\insert_db.py')

# Select the records to show they are indeed there
os.system(r'python db\select_db.py')

print('\nTASK1 - Database successfully set up!\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TASK 2: Retrieve the stats for the stored tunafish creature
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Open the template'
file_in = open(r'templates\BasicCreatureBlock.html', 'r')

# Read the statblock
src = Template(file_in.read())

# Create a Dictionary to hold all of the information to be written to the stat block [Replace with Creature.py]
print('TASK 2 - Retrieving data from the database...')

stats = {'name': '',
         'size': '',
         'type': '',
         'alignment': '',
         'ac': '',
         'hp': '',
         'speed': '',
         'str': '',
         'dex': '',
         'con': '',
         'int': '',
         'wis': '',
         'cha': '',
         'senses': '',
         'languages': '',
         'challenge': '',
         'attack': '',
         'attackDescription': '',
         'attackHit': '',
         'attackDamage': ''}

# Retrieve the database data from the ACTIONS Table
db = sqlite3.connect(r'db\cst8333.db')
cursor = db.execute("SELECT * from ACTIONS")

for row in cursor:
    stats.__setitem__('attack', row[1])
    stats.__setitem__('attackDescription', row[2])
    stats.__setitem__('attackHit', row[3])
    stats.__setitem__('attackDamage', row[4])

print("Read ACTIONS successfully.")
db.close()

# Retrieve the database data from the SENSES Table
db = sqlite3.connect(r'db\cst8333.db')
cursor = db.execute("SELECT * from SENSES")

for row in cursor:
    stats.__setitem__('senses', row[1])

print("Read SENSES successfully")
db.close()

# Retrieve the database data from the ATTRIBUTES Table
db = sqlite3.connect(r'db\cst8333.db')
cursor = db.execute("SELECT * from ATTRIBUTES")

for row in cursor:
    stats.__setitem__('str', row[1])
    stats.__setitem__('dex', row[2])
    stats.__setitem__('con', row[3])
    stats.__setitem__('int', row[4])
    stats.__setitem__('wis', row[5])
    stats.__setitem__('cha', row[6])

print("Read ATTRIBUTES successfully")
db.close()

# Retrieve the database data from the CREATURE Table
db = sqlite3.connect(r'db\cst8333.db')
cursor = db.execute("SELECT * from CREATURE")

for row in cursor:
    stats.__setitem__('name', row[1])
    stats.__setitem__('size', row[2])
    stats.__setitem__('type', row[3])
    stats.__setitem__('alignment', row[4])
    stats.__setitem__('ac', row[5])
    stats.__setitem__('hp', row[6])
    stats.__setitem__('speed', row[7])
    stats.__setitem__('languages', row[10])
    stats.__setitem__('challenge', row[11])

print("Read CREATURE successfully")
db.close()

print("TASK 2 - Complete")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TASK 3: Create a statblock representing the stored tunafish creature
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a destination file
file_name = str.format('{}StatBlock.html', stats.get('name'))
file_out = open(file_name, 'w')

# Make the substitutions
file_out.write(src.substitute(stats))

# Free resources by closing the destination file. Will be found in the src folder. Can open in browser.
file_out.close()
print('Dire Tunafish Created!')

# close the template
file_in.close()

