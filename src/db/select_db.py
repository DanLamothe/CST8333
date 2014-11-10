#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File Name: select_db.py
# By: Daniel Lamothe
#
# Purpose: Library that holds functions to check the status of tables.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'User'

import sqlite3


def select_creature():
    db = sqlite3.connect('db\cst8333.db')
    print("Opened database successfully.")

    cursor = db.execute("SELECT id, name, hp from CREATURE")

    for row in cursor:
        print("ID =", row[0])
        print("Name =", row[1])
        print("HP =", row[2])
        print("\n")

    print("Operation performed successfully.")
    db.close()


def select_attributes():
    db = sqlite3.connect('db\cst8333.db')
    print("Opened database successfully.")

    cursor = db.execute("SELECT * from ATTRIBUTES")

    for row in cursor:
        print("ID =", row[0])
        print("STR =", row[1])
        print("DEX =", row[2])
        print("CON =", row[3])
        print("INT =", row[4])
        print("WIS =", row[5])
        print("CHA =", row[6])
        print("\n")

    print("Operation performed successfully.")
    db.close()


def select_senses():
    db = sqlite3.connect('db\cst8333.db')
    print("Opened database successfully.")

    cursor = db.execute("SELECT * from SENSES")

    for row in cursor:
        print("ID =", row[0])
        print("Senses =", row[1])
        print("\n")

    print("Operation performed successfully.")
    db.close()


def select_actions():
    db = sqlite3.connect('db\cst8333.db')
    print("Opened database successfully.")

    cursor = db.execute("SELECT * from ACTIONS")

    for row in cursor:
        print("ID =", row[0])
        print("Name =", row[1])
        print("Description =", row[2])
        print("Attack =", row[3])
        print("\n")

    print("Operation performed successfully.")
    db.close()

select_actions()
select_attributes()
select_senses()
select_creature()