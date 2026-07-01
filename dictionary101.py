#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" dictionary101.py

A Python dictionary is an unordered, mutable, and indexed collection 
of data. Unlike lists that store elements as single items, dictionaries 
store data in key:value pairs.

Keys must be unique and immutable (like strings, numbers, or tuples). 
You cannot have duplicate keys.

Values can be of any data type (lists, strings, integers, or even 
other dictionaries) and can be changed or duplicated.

Don't use keyword 'dict' for a variable name, might want to use 'dic2'

add another key:value pair with dict2[key2] = value2
d.items()    return a list of (key, val) tuple pairs
d.keys()     return a list of d's keys
d.values()   return a list of d's values
d.len()      size/length of dictionary d

d.max() returns maximum of key 'z' before 'a'
d,min() returns minimum of key

d.get(k, defaultval) return d[k] if found, else defaultval
d.setdefault(k[,defaultval]) d[k] if k in d, else defaultval
  (also setting it)
defaultval can be a simple message string like "not found"
k in d     True if d has key k, else False avoids error messages

these actions alter the dictionary!
d.pop(k[, default]) removes key k and returns the corresponding
  value. If key is not found, default is returned if given,
  otherwise KeyError is raised
d.popitem()  remove and return an arbitrary (key, value) pair
  from d
del d(k)  removes item having key k from dictionary d
d.clear()	Removes all elements from the dictionary

d1.update(d2)  for k, v in d2.items(): d1[k] = v
  adds d2 to d1 (if d1 is empty, you made a copy of d2)
  same as dict.update(d1, d2) d1 altered

note:
Python3.7+ dictionaries show ordered.

take a look at dns program  'NamedTuple101.py'

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""

import pprint

# Creating a dictionary of user data
user = {
    "name": "Tom",
    "age": 35,
    "city": "Rome",
    "skills": ["C++", "Food"]
}
print("size =", len(user))
print(user)

'''
size = 4
{'name': 'Tom', 'age': 35, 'city': 'Rome', 'skills': ['C++', 'Food']}
'''

# Using square brackets
print(user["name"])  # Tom

# Using the .get() method
print(user.get("age"))    # 35
print(user.get("city"))   # Rome
# supply a fallback value if the key is not found
print(user.get("IQ", "Not Found"))  # Not Found

print("="*40)

# Updating an existing key
user["age"] = 31 
# Adding a new key-value pair
user["email"] = "tom7@doit.com"

print("dictionary 'user' after add and change")
print("size =", len(user))
# pprint prints one key:value pair per line
# and keys in alphabetical order ...
pprint.pprint(user)

'''
dictionary 'user' after add and change
size = 5
{'age': 31,
 'city': 'Rome',
 'email': 'tom7@doit.com',
 'name': 'Tom',
 'skills': ['C++', 'Food']}
'''

print("="*40)

print("list all the keys:")
print(user.keys())
print("list all the values:")
print(user.values())
print("list all the pairs:")
print(user.items())
# only the key max/min are returned
print('Maximum Key', max(user))
print('Minimum Key', min(user))

'''
list all the keys:
dict_keys(['name', 'age', 'city', 'skills', 'email'])
list all the values:
dict_values(['Tom', 31, 'Rome', ['C++', 'Food'], 'tom7@doit.com'])
list all the pairs:
dict_items([('name', 'Tom'), ('age', 31), ('city', 'Rome'), 
            ('skills', ['C++', 'Food']), ('email', 'tom7@doit.com')])
Maximum Key skills
Minimum Key age
'''

print("="*40)

# these actions alter the dictionary!
# Removes a specific key and returns its value
age = user.pop("age") 
# Removes the last inserted key-value pair
last_item = user.popitem() 
# Deletes an item entirely using the 'del' keyword
del user["city"]

print("dictionary after pop and del")
print("size =", len(user))
print(user)

'''
dictionary after pop and del
size = 2
{'name': 'Tom', 'skills': ['C++', 'Food']}
'''

print("="*40)

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

print("="*40)

# create dictionaries
empty_dict = {}

print("create a dictionary from (key, value) tuples or lists")
list2 = [["salt", 1.22], ["sugar", 2.45], ["milk", 3.69]]
list3 = [["caviar", 34.97], ["wine", 22.99], ["lox", 13.23]]
food_dict = dict(list2 + list3)
pprint.pprint(food_dict)

# create a new dictionary containing only fooditems costing more than $10
# use a dictionary comprehenion instead of a for loop
exp_food_dict = {food: cost for food, cost in food_dict.items() if cost > 10}
print(exp_food_dict)

print("="*40)

# unpack the (food, cost) tuples
for food, cost in food_dict.items():
    print(f"{food} costs ${cost}")

print("="*40)

# print a selected item
print("just one selected key")
print('sugar costs ${sugar:4.2f}'.format(**food_dict))

# if you use a single asterisk (*) on a dictionary, Python will only 
# unpack its keys, completely ignoring the values.

print("="*40)

prices = {'pizza': 12.99, 'soda': 1.99, 'salad': 7.99}

for order, price in prices.items():
    print(f"Our {order} costs ${price}")

'''
Our pizza costs $12.99
Our soda costs $1.99
Our salad costs $7.99
'''

print("="*40)

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 5, 'c': 3, 'd': 4}
print(dict1)
print(dict2)
# If the dictionaries share the same keys, the dictionary placed last 
# will overwrite the earlier values
print("merge 2 dictionaries")
# Merge dict1 and dict2 into a new dictionary, dict1 and dict2 untouched
merged_dict = {**dict1, **dict2}
print(merged_dict)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("="*40)

print(dict1)
print(dict2)
print("dict.update(dict1, dict2), only dict1 changes")
dict.update(dict1, dict2)
print(dict1)
print(dict2)


