#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sqlite3_process_read_data_file2.py

read a database file and process it with query language commands

sqlite3.connect(database, timeout=5.0, isolation_level=None,
    detect_types=0, factory=100)
where...
timeout=5.0 --> allows multiple access for 5 seconds (for servers)
isolation_level=None -->  autocommit mode
detect_types=0 --> native types TEXT, INTEGER, FLOAT, BLOB and NULL
factory=100 --> statement cache to avoid SQL parsing overhead

basic flow ...
once you have a connection
you can create a cursor object and
call its execute() method to perform SQL commands

vegaseat  30oct2026
'''

import sqlite3

# connect to a permanent database file you have created before
# file located in directory: /home/admin123
conn = sqlite3.connect('sqlite3_people.db')
# establish the cursor, needed to execute the connected db
cur = conn.cursor()

# show number of rows
nrow = next(cur.execute('''SELECT COUNT(*) FROM data'''))
print(nrow)
'''
(4,)
'''

print('-'*35)

# search by name
# query language in upper case is optional
sname = cur.execute('''SELECT * FROM data WHERE name="Paul Park"''').fetchall()
print(sname)
# unpack list tuple
name, age, occupation = sname[0]
print(name)
'''
[('Paul Park', 42, 'Casino Dealer')]
Paul Park
'''

print('-'*35)

# test non-existing name
tname = cur.execute('''select * from data where name="Ziggy"''').fetchall()
print(tname)
'''
[]
'''

print('-'*35)

# search by age
sage = cur.execute('''select * from data where age="75"''').fetchall()
print(sage)
'''
[('Mark Moses', 75, 'WM Greeter')]
'''

print('-'*35)

# search by occupation
socc = cur.execute('''select * from data where occupation="Dentist"''').fetchall()
print(socc)
# unpack list tuple
name, age, occupation = socc[0]
print("{} is a {}".format(name, occupation))
'''
[('Nick Noble', 30, 'Dentist')]
Nick Noble is a Dentist
'''

# done
conn.close()

print('-'*35)

# reopen connection ...
conn = sqlite3.connect('sqlite3_people.db')
# takes care of conn.commit() and conn.close()
with conn:
    # allows for named rows via their column names
    conn.row_factory = sqlite3.Row
    # establish the cursor, needed to execute the connected db
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    sf = "{} age {} is a {}"
    for row in rows:
        print (sf.format(row["name"], row["age"], row["occupation"]))

'''
John Jupiter age 15 is a Student
Paul Park age 42 is a Casino Dealer
Nick Noble age 30 is a Dentist
Mark Moses age 75 is a WM Greeter
'''
