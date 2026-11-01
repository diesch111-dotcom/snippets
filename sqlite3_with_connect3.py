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
    sf = "{} has {}, 'owns shares of' {}"
    for row in rows:
        print(sf.format(row["name"], row["wealth"], row["source"]))

'''

'''

