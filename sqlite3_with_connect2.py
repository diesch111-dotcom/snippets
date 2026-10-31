#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sqlite3_with_connect2.py

using the with statement to connect
also get column names

sqlite3.connect(database, timeout=5.0, isolation_level=None,
    detect_types=0, factory=100)
where...
timeout=5.0 --> allows multiple access for 5 seconds (for servers)
isolation_level=None -->  autocommit mode
detect_types=0 --> native types TEXT, INTEGER, FLOAT, BLOB and NULL
factory=100 --> statement cache to avoid SQL parsing overhead

vegaseat  31oct2026
'''

import sqlite3

# file "sqlite3_people.db" is in Linux directory: "/home/admin123"
# and has been previously created
# using 'with' manages the connection and commits automatically
with sqlite3.connect("sqlite3_people.db") as conn:
    cursor = conn.cursor()
    # Query data safely using parameterized queries
    cursor.execute("SELECT name, age FROM data WHERE age > ?", (25,))
    for name, age in cursor.fetchall():
        print(f"{name} is {age} years old.")

'''
Paul Park is 42 years old.
Nick Noble is 30 years old.
Mark Moses is 75 years old.
'''

print("="*32)

# reopen connection ...
conn = sqlite3.connect('sqlite3_people.db')
# with statement takes care of conn.commit() and conn.close()
with conn:
    # allows for named rows via their column names
    conn.row_factory = sqlite3.Row
    # establish the cursor, needed to execute the connected db
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    sf = "{} age {} is a {}"
    for row in rows:
        print(sf.format(row["name"], row["age"], row["occupation"]))

    print("="*32)
   
    # cursor.description returns a tuple of tuples containing column info
    # the first element of each tuple is the column name
    column_names = [description[0] for description in cur.description]
    print(column_names)

'''
John Jupiter age 15 is a Student
Paul Park age 42 is a Casino Dealer
Nick Noble age 30 is a Dentist
Mark Moses age 75 is a WM Greeter
================================
['name', 'age', 'occupation']
'''

