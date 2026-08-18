#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' dict_comprehension102.py

Create a dictionary using dictionary comprehension
Similar to list comprehension, but uses {}
eg.
list of tuple(fruit_name, quantity)
tuple_pairs = [('apple', 124), ('banana', 300), ('plum', 1.25)]
fruit_dict = {k: v for k, v in tuple_pairs}

also makes a true copy
fruit_dict2 = {k: v for k, v in fruit_dict.items()}

tested with VSCodium IDE on LinuxMint  vegaseat 19jul2026
'''

import pprint

# write a test file with unique words
names = '''\
Paul
Peter
Sally
Frank
Jim
Sandra
Quasimo
'''

fname = "names.txt"
# write the name string to a disc file (current folder)
with open(fname, 'w') as fout:
    fout.write(names)

# read the names back into a dictionary {name: initial}
with open(fname) as fin:
    name_dict = {name.strip():name[0] for name in fin}

pprint.pprint(name_dict)
''' result...
{'Frank': 'F',
 'Jim': 'J',
 'Paul': 'P',
 'Peter': 'P',
 'Quasimo': 'Q',
 'Sally': 'S',
 'Sandra': 'S'
'''

# testing ...
# search for a name in the name_dict (no result if not found)
name = 'Peter'
# Python3 uses in
if name in name_dict:
    print("--> {} found".format(name))

print('='*40)

# more ...
# write a csv (comma separated values) file
# with element_symbol, element_name, atomic_weight lines
element_test_csv = '''\
H,Hydrogen,1.008
He,Helium,4.002602
Li,Lithium,6.94
Be,Beryllium,9.0121831
B,Boron,10.81
C,Carbon,12.011'''

# save to a csv file for the fun of it
fname2 = "elements_test.csv"
with open(fname2, 'w') as fout:
    fout.write(element_test_csv)

# create a dictionary via for loop, split() to lists and empty {}
ee_dict = {}
for line in element_test_csv.split("\n"):
    #print(list(line.split(",")))
    e_list = list(line.split(","))
    #print(e_list)
    e_dict = {e_list[0]: (e_list[1], float(e_list[2]))}
    ee_dict.update(e_dict)

print("Via for loop:")
pprint.pprint(ee_dict)
'''
Via for loop:
{'B': ('Boron', 10.81),
 'Be': ('Beryllium', 9.0121831),
 'C': ('Carbon', 12.011),
 'H': ('Hydrogen', 1.008),
 'He': ('Helium', 4.002602),
 'Li': ('Lithium', 6.94)}
'''

print('='*40)

#print(element_test_csv.split("\n"))

# using dictionary comprehension
# note: split() gives a list
mydict = {line.split(",")[0]: (line.split(",")[1], float(line.split(",")[2])) \
for line in element_test_csv.split("\n")}

print("Via dictionary comprehension:")
pprint.pprint(mydict)
'''
Via dictionary comprehension:
{'B': ('Boron', 10.81),
 'Be': ('Beryllium', 9.0121831),
 'C': ('Carbon', 12.011),
 'H': ('Hydrogen', 1.008),
 'He': ('Helium', 4.002602),
 'Li': ('Lithium', 6.94)}
'''

print('='*40)

print("swapping keys and values:")
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"original = {original}")
print(f"swapped = {swapped}")
'''
swapping keys and values:
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {1: 'a', 2: 'b', 3: 'c'}
'''

print('='*40)

print("create dictionary from tuple pairs:")
pairs = [('apple', 2), ('banana', 3), ('cherry', 5)]
fruit_dict = {k: v for k, v in pairs}
print(f"tuple pairs = {pairs}")
print(f"fruit_dict = {fruit_dict}")
'''
create dictionary from tuple pairs:
tuple pairs = [('apple', 2), ('banana', 3), ('cherry', 5)]
fruit_dict = {'apple': 2, 'banana': 3, 'cherry': 5}
'''

print('='*40)

print("mapping characters to their ASCII codes:")
ascii_map = {char: ord(char) for char in 'abcd'}
print(f"char: ASCII = {ascii_map}")
'''
mapping characters to their ASCII codes:
char: ASCII = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
'''

print('='*40)

import json

json_string = '''
[
    {"id": 1, "name": "Alice", "score": 85},
    {"id": 2, "name": "Bob", "score": 92},
    {"id": 3, "name": "Charlie", "score": 78}
]
'''
print("convert JSON string to Python list of dicts:")
print(f"json string = {json_string}")
# Convert JSON string to Python list of dicts
data = json.loads(json_string)
for item in data:
    print(item)
'''
convert JSON string to Python list of dicts:
json string = 
[
    {"id": 1, "name": "Alice", "score": 85},
    {"id": 2, "name": "Bob", "score": 92},
    {"id": 3, "name": "Charlie", "score": 78}
]

{'id': 1, 'name': 'Alice', 'score': 85}
{'id': 2, 'name': 'Bob', 'score': 92}
{'id': 3, 'name': 'Charlie', 'score': 78}
'''

print('='*40)

print("create a dictionary of names and scores:")
name_score_dict = {entry["name"]: entry["score"] for entry in data}
print(name_score_dict)
'''
{'Alice': 85, 'Bob': 92, 'Charlie': 78}
'''

print("scores above 80:")
high_scores = {entry["name"]: entry["score"] for entry in data if entry["score"] >= 80}
print(f"{high_scores}")
'''
scores above 80:
{'Alice': 85, 'Bob': 92}
'''
