__author__ = 'User'

import os

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TASK 1: Setup the Database (Run once on a new machine)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Runs the Create DB Library to create the application database
os.system(r'python db\create_db.py')

# Insert initial records into the database
os.system(r'python db\insert_db.py')

# Select the records to show they are indeed there
os.system(r'python db\select_db.py')

print('\n\nFirst time startup for Creature Stablock Creator Complete!')