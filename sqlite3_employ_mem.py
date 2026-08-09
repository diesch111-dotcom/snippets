#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sqlite3_employ_mem.py

Experimenting with a Python sqlite3 database of employees
Use memory for temporary testing

sqlite3.connect()
conn.cursor()
cur.execute()
cur.executemany()
cur.close()


tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import sqlite3

# for temporary testing you can use memory only
conn = sqlite3.connect(":memory:")

cur = conn.cursor()

# query language in upper case is optional eye candy
cur.execute('''CREATE TABLE employees(
number INTEGER PRIMARY KEY AUTOINCREMENT,
first TEXT,
last TEXT,
age INTEGER,
weight REAL)
''')

# a list of (first, last, age, weight) tuples
data_list = [
('Heidi', 'Kalumpa', 36, 127.3),
('Frank', 'Maruco', 27, 234),
('Larry', 'Pestraus', 19, 315),
('Serge', 'Romanowski', 59, 147),
('Carolus', 'Arm', 44, 102.5),
('Monika', 'Sargnagel', 21, 175),
('Hans', 'Solo', 37, 167.8),
('Mother', 'Therasa', 81, 93.2)
]

# insert all data_list lines at once ...
cur.executemany("INSERT INTO employees(first, last, age, weight) \
    VALUES (?, ?, ?, ?)", data_list )

# testing ...
cur.execute('SELECT * FROM employees')
print("fetch all data rows (raw data):")
for r in cur.fetchall():
    print(r)
print('-'*42)

cur.execute('SELECT * FROM employees ORDER BY last')
print("fetch all data rows (sorted by last name):")
for r in cur.fetchall():
    print(r)
print('-'*42)

cur.execute('SELECT * FROM employees WHERE age>50')
print("fetch all data rows where age is above 50:")
for r in cur.fetchall():
    print(r)
print('-'*42)

cur.execute('SELECT * FROM employees WHERE number=3')
print("fetch the data row of employee number 3:")
for r in cur.fetchall():
    print(r)
print('-'*42)

# finally ...
cur.close()

''' result...
fetch all data rows (raw data):
(1, 'Heidi', 'Kalumpa', 36, 127.3)
(2, 'Frank', 'Maruco', 27, 234.0)
(3, 'Larry', 'Pestraus', 19, 315.0)
(4, 'Serge', 'Romanowski', 59, 147.0)
(5, 'Carolus', 'Arm', 44, 102.5)
(6, 'Monika', 'Sargnagel', 21, 175.0)
(7, 'Hans', 'Solo', 37, 167.8)
(8, 'Mother', 'Therasa', 81, 93.2)
------------------------------------------
fetch all data rows (sorted by last name):
(5, 'Carolus', 'Arm', 44, 102.5)
(1, 'Heidi', 'Kalumpa', 36, 127.3)
(2, 'Frank', 'Maruco', 27, 234.0)
(3, 'Larry', 'Pestraus', 19, 315.0)
(4, 'Serge', 'Romanowski', 59, 147.0)
(6, 'Monika', 'Sargnagel', 21, 175.0)
(7, 'Hans', 'Solo', 37, 167.8)
(8, 'Mother', 'Therasa', 81, 93.2)
------------------------------------------
fetch all data rows where age is above 50:
(4, 'Serge', 'Romanowski', 59, 147.0)
(8, 'Mother', 'Therasa', 81, 93.2)
------------------------------------------
fetch the data row of employee number 3:
(3, 'Larry', 'Pestraus', 19, 315.0)
------------------------------------------
'''
