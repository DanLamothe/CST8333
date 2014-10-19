__author__ = 'User'

import sqlite3

db = sqlite3.connect('cst8333.db')
print("Opened database successfully.")

cursor = db.execute("SELECT id, name, hp from CREATURE")

for row in cursor:
    print("ID =", row[0])
    print("Name =", row[1])
    print("HP =", row[2])
    print("\n")

print("Operation performed successfully.")