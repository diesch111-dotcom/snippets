#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sqlite3_create_data_file2.py

Commits raw data to the db file (data is persistent now)

vegaseat  30oct2026
'''

import sqlite3

# list of [name, age, occupation] lists
mylists = [
['John Jupiter', 15, 'Student'   ],
['Paul Park', 42, 'Casino Dealer'],
['Nick Noble', 30, 'Dentist'     ],
['Mark Moses', 75, 'WM Greeter'  ]
]
# create/connect to a permanent database file
# file saved to directory: /home/admin123
conn = sqlite3.connect('sqlite3_people.db')
# with takes care of conn.commit() and conn.close()
with conn:
    # establish the cursor, needed to execute the connected db
    cur = conn.cursor()
    # do this or it will keep adding data to existing data file
    cur.execute("DROP TABLE IF EXISTS data")
    # query language in upper case is optional
    # create the table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS data
    (name TEXT, age INT, occupation TEXT)
    """)
    # now load/insert the list of lists
    cur.executemany('INSERT INTO data VALUES (?,?,?)', mylists)

