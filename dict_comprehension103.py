
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' dict_comprehension103.py

Create a dictionary using dictionary comprehension
Similar to list comprehension, but uses {}
eg.
list of tuple(fruit_name, quantity)
tuple_pairs = [('apple', 124), ('banana', 300), ('plum', 1.25)]
fruit_dict = {k: v for k, v in tuple_pairs}

also makes a true copy
fruit_dict2 = {k: v for k, v in fruit_dict.items()}

slicing uses [start:<end:step]
'start' defaults to 0, 'end' to len(sequence), 'step' to 1

tested with VSCodium IDE on LinuxMint  vegaseat 19jul2026
'''

# write a test file with unique words
names = '''\
Paul
Peter
Sally
Frank
John
Jimmy John
Sandra
Quasimo'''

name_list = names.splitlines()
print(name_list)
'''
['Paul', 'Peter', 'Sally', 'Frank', 'John', 'Jimmy John', 'Sandra', 'Quasimo']
'''

for name in name_list:
    print(name)
'''
Paul
Peter
Sally
Frank
John
Jimmy John
Sandra
Quasimo
'''

# make key the first +  last character + length of name to aid collision avoidance
name_dict = {name[:1] + name[-1:] + str(len(name)): name for name in name_list}
print(name_dict)
'''
{'Pl4': 'Paul', 'Pr5': 'Peter', 'Sy5': 'Sally', 'Fk5': 'Frank', 'Jn4': 'John', 
'Jn10': 'Jimmy John', 'Sa6': 'Sandra', 'Qo7': 'Quasimo'}
'''

# using a list of tuple(fruit_name, quantity) pairs
tuple_pairs = [('apple', 124), ('banana', 300), ('plum', 125)]
fruit_dict = {k: v for k, v in tuple_pairs}
print("using a list of tuple pairs:")
print(fruit_dict)
'''
using a list of tuple pairs:
{'apple': 124, 'banana': 300, 'plum': 125}
'''

print("make a true copy:")
fruit_dict2 = {k: v for k, v in fruit_dict.items()}
print(fruit_dict2)
'''
make a true copy:
{'apple': 124, 'banana': 300, 'plum': 125}
'''

# will change the original fruit_dict
# add anouther fruit
fruit_dict['pear'] = 56
print(fruit_dict)
'''
{'apple': 124, 'banana': 300, 'plum': 125, 'pear': 56}
'''

# a safe way to add
# 'plum' already exists, so no effect
fruit_dict.setdefault('plum', 10)
# 'orange' is new so it is added
fruit_dict.setdefault('orange', 10)
print(fruit_dict)
'''
{'apple': 124, 'banana': 300, 'plum': 125, 'pear': 56, 'orange': 10}
'''

# remove a specific fruit
fruit_dict.pop('banana')
print(fruit_dict)
'''
{'apple': 124, 'plum': 125, 'pear': 56, 'orange': 10}
'''
