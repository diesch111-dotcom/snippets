#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sqlite3_load_list_of_lists_create_file.py

Important if you make changes to the database
Commits current data to the db file (data is persistent now)
If the file given in connect() does not exist, it will be created
conn.commit()
# done
conn.close()

"with conn" takes care of this

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import sqlite3

# list of [name, age, occupation] lists
mylists = [
['John Jupiter', 15, 'Student'   ],
['Paul Park', 42, 'Casino Dealer'],
['Nick Noble', 30, 'Dentist'     ],
['Mark Moses', 75, 'WM Greeter'  ],
['Stew Pitt', 23, 'Male Rolemodel']
]

# create/connect to a permanent database file
conn = sqlite3.connect('data3.db')

# with takes care of conn.commit() and conn.close()
with conn:
    # establish the cursor, needed to execute the connected db
    cur = conn.cursor()
    # do this or it will keep adding data to existing data file
    cur.execute("DROP TABLE IF EXISTS data")
    # query language in upper case is optional
    # create the table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS data
    (name TEXT, age INT, occupation TEXT)
    ''')
    try:
        # now load/insert the list of lists
        cur.executemany('INSERT INTO data VALUES (?,?,?)', mylists)
    except:
        pass
