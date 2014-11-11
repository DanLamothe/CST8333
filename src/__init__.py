#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: __init__.py
# By: Daniel Lamothe
#
# Purpose: CST8333 Demo for Assignment 04. Creates and populates the database with a sample creature. Reads the database
#   and stores the values in a Creature object. Manipulation of dictionary objects and the Template module, the script
#   substitutes values in the dictionary into the supplied HTML template. A new file is created depicting the creature
#   in statistical form.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'User'

import os
import Database

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
# TASK 2: Retrieve the stats for the stored Dire TunaFish creature
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

my_creature = Database.Database.read('Dire TunaFish')
my_creature.export(my_creature.to_dict())

