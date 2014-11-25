#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: Setup.py
# By: Daniel Lamothe
#
# Purpose: A Python module which can be run as a script to generate a new sqlite3 database. This step should be optional
#           but is provided in the event the user wants a quick wipe to teh database file. The insert script is
#           commented out by default for this reason. Remove the comment to insert a sample 'Dire TunaFish' creature
#           into the database.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import os
import Database

# Runs the Create DB Library to create the application database
os.system(r'python db\create_db.py')

# Insert initial records into the database (Dire TunaFish Example)
# os.system(r'python db\insert_db.py')

# Select the records to show they are indeed there
Database.Database.print_all_creatures(False)

print('\n\nFirst time startup for Creature Stablock Creator Complete!')