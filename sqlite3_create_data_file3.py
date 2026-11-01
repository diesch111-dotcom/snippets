#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sqlite3_create_data_file3.py

Commits raw data to the db file (data is persistent now)

vegaseat  30oct2026
'''

import sqlite3

header = 'name,wealth,age,source,nation'
bill_list = [
['Elon Musk', '$839.0 billion', '54', 'Tesla and SpaceX', 'USA'],
['Larry Page', '$257.0 billion', '52', 'part of Google', 'USA'],
['Sergey Brin', '$237.0 billion', '52', 'part of Google', 'USA'],
['Jeff Bezos', '$224.0 billion', '62', 'Amazon', 'USA'],
['Mark Zuckerberg', '$222.0 billion', '41', 'Meta Platforms', 'USA'],
['Larry Ellison', '$190.0 billion', '81', 'Oracle Corporation', 'USA'],
['Bernard Arnault', '$171.0 billion', '77', 'LVMH', 'FRANCE'],
['Jensen Huang', '$154.0 billion', '63', 'Nvidia', 'USA'],
['Warren Buffett', '$149.0 billion', '95', 'Berkshire Hathaway', 'USA'],
['Amancio Ortega', '$148.0 billion', '89', 'Indite', 'SPAIN']
]

# create/connect to a permanent database file
# file saved to directory: /home/admin123
conn = sqlite3.connect('Billionairs2026.db')
# with takes care of conn.commit() and conn.close()
with conn:
    # establish the cursor, needed to execute the connected db
    cur = conn.cursor()
    # do this or it will keep adding data to existing data file
    cur.execute("DROP TABLE IF EXISTS data")
    # query language in upper case is optional
    # create the table using header information
    cur.execute("""
    CREATE TABLE IF NOT EXISTS data
    (
    name TEXT,
    wealth TEXT, 
    age INT, 
    source TEXT,
    nation TEXT
    )
    """)
    # now load/insert the list of lists
    cur.executemany('INSERT INTO data VALUES (?,?,?,?,?)', bill_list)

