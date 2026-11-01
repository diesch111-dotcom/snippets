#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sqlite3_with_connect3.py

using the with statement to connect to
"Billionairs2026.db"

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
# header = 'name, wealth, age, source, nation'
# using 'with' manages the connection and commits automatically
with sqlite3.connect("Billionairs2026.db") as conn:
    cursor = conn.cursor()
    # Query data safely using parameterized queries
    cursor.execute("SELECT name, age, nation FROM data")
    for name, age, nation in cursor.fetchall():
        print(f"{name} is {age} years old, 'home' is in {nation}")

    print("="*52)

    # allows for named rows via their column names
    conn.row_factory = sqlite3.Row
    # establish the cursor, needed to execute the connected db
    cursor2 = conn.cursor()
    cursor2.execute("SELECT * FROM data")
    rows = cursor2.fetchall()
    sf = "{} has {}, 'owns' {}"
    for row in rows:
        print(sf.format(row["name"], row["wealth"], row["source"]))

'''
Elon Musk is 54 years old, 'home' is in USA
Larry Page is 52 years old, 'home' is in USA
Sergey Brin is 52 years old, 'home' is in USA
Jeff Bezos is 62 years old, 'home' is in USA
Mark Zuckerberg is 41 years old, 'home' is in USA
Larry Ellison is 81 years old, 'home' is in USA
Bernard Arnault is 77 years old, 'home' is in FRANCE
Jensen Huang is 63 years old, 'home' is in USA
Warren Buffett is 95 years old, 'home' is in USA
Amancio Ortega is 89 years old, 'home' is in SPAIN
====================================================
Elon Musk has $839.0 billion, 'owns' Tesla and SpaceX
Larry Page has $257.0 billion, 'owns' part of Google
Sergey Brin has $237.0 billion, 'owns' part of Google
Jeff Bezos has $224.0 billion, 'owns' Amazon
Mark Zuckerberg has $222.0 billion, 'owns' Meta Platforms
Larry Ellison has $190.0 billion, 'owns' Oracle Corporation
Bernard Arnault has $171.0 billion, 'owns' LVMH
Jensen Huang has $154.0 billion, 'owns' Nvidia
Warren Buffett has $149.0 billion, 'owns' Berkshire Hathaway
Amancio Ortega has $148.0 billion, 'owns' Indite
'''

