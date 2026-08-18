#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' dict_methods102.py

A look at Python dictionary object methods

d.items()    return a list of (key, val) tuple pairs
d.keys()     return a list of d's keys
d.values()   return a list of d's values

d.max() returns maximum of key 'z' before 'a'
d,min() returns minimum of key

d.get(k, defaultval) return d[k] if found, else defaultval
d.setdefault(k[,defaultval]) d[k] if k in d, else defaultval
  (also setting it)
defaultval can be a simple message string like "not found"

d.pop(k[, default]) removes key k and returns the corresponding
  value. If key is not found, default is returned if given,
  otherwise KeyError is raised
d.popitem()  remove and return an arbitrary (key, value) pair
  from d
d1.update(d2)  for k, v in d2.items(): d1[k] = v
  adds d2 to d1 
  if d1 is empty, you made a true copy of d2
  same as dict.update(d1, d2)

note:
In Python3.7+ dictionaries are ordered.
In Python3.6  dictionaries are unordered.

see ...
https://pynative.com/python-dictionaries/#h-summary-of-dictionary-operation
https://www.w3schools.com/python/python_reference.asp
https://www.w3schools.com/python/python_ref_dictionary.asp

tested with VSCodium IDE on LinuxMint  VegasEat 17aug2026
'''

import pprint
import pickle
import json

# get a list of the dictionary methods
# excluding the "dunder" (__) ones
mydict = dict()
print("dictionary object methods:")
for item in dir(mydict):
    if not item.startswith('_'):
        print(item)

'''
dictionary object methods:
clear
copy
fromkeys
get
items
keys
pop
popitem
setdefault
update
values
'''

# more info on individual dictionary methods ...
print('-'*15)

help(dict.popitem)
#help(dict.fromkeys)
help(dict.setdefault)
help(dict.get)

'''
Help on method_descriptor:

popitem(...)
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    does change D, one less item
    2-tuple; but raise KeyError if D is empty.

setdefault(...)
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    eg. D.get('He', "not found")
'''

print('create a dictionary dict()'.center(40, '-'))

# using dict()
# convert list of tuples to dictionary
print(dict([('a', 1),('b', 2)]))  # {'a': 1, 'b': 2}

# convert tuple of tuples to dictionary
print(dict((('a', 1),('b', 2))))  # {'a': 1, 'b': 2}

# convert list of lists to dictionary
print(dict([['a', 1],['b', 2]]))  # {'a': 1, 'b': 2}

print('-'*25)

numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
# zip the two lists, zip() is a generator
numlet = zip(numbers, letters)
print(numlet)

# convert the zip object to a list
print(list(numlet))
# refresh the zip() generator
numlet = zip(numbers, letters)

# convert the zip object to a dictionary
print(dict(numlet))
'''
<zip object at 0x000002066FC30080>
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
'''
print('-'*25)
alpha_str = "ABCDEFG"
print('interesting way via enumerate():')
ord_letter = dict(enumerate(alpha_str, 65))
# swap dictionary key:value pairs with a dictionary comprehension
letter_ord = {v: k for k, v in ord_letter.items()}
print(ord_letter)
print(letter_ord)
'''
interesting way via enumerate():
{65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G'}
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71}
'''
print('-'*25)
# now test some of the dictionary methods ...
# dict(element_symbol: (element_name, atomic_weight))
symbols = {
'B': ('Boron', 10.81),
 'Be': ('Beryllium', 9.0121831),
 'C': ('Carbon', 12.011),
 'H': ('Hydrogen', 1.008),
 'He': ('Helium', 4.002602),
 'Li': ('Lithium', 6.94)}
# items() are key, value lines
for item in symbols.items():
    print(item)
'''
{'B': ('Boron', 10.81),
 'Be': ('Beryllium', 9.0121831),
 'C': ('Carbon', 12.011),
 'H': ('Hydrogen', 1.008),
 'He': ('Helium', 4.002602),
 'Li': ('Lithium', 6.94)}
'''
print('-'*25)
# unpack key, value
for key, value in symbols.items():
    print('{} = {}'.format(key, value[0]))
'''
B = Boron
Be = Beryllium
C = Carbon
H = Hydrogen
He = Helium
Li = Lithium
'''
print('-'*25)
dict_people = {
"Mia Certs": 123,
"Stew Pitt": 543,
"Ben Dover": 998
}
print(dict_people)
'''
{'Mia Certs': 123, 'Stew Pitt': 543, 'Ben Dover': 998}
'''
# sorts the keys
print(sorted(dict_people))
'''
['Ben Dover', 'Mia Certs', 'Stew Pitt']
'''

print('get() setdefault()'.center(40, '-'))

# simply use dic[key], gives KeyError: if key not found
if 'He' in symbols:
    print(symbols['He'])  # ('Helium', 4.002602)

# avoid KeyError:
print(symbols.get('He', "not found"))  # ('Helium', 4.002602)
print(symbols.get('Xe', "not found"))  # not found
print(symbols.setdefault('He', "not found"))  # ('Helium', 4.002602)
print('-'*25)
# assume this is a string read from a file
# showing name=score data on each line
data_str = '''\
Bob=7
Bob=4
Bob=3
Sue=2
Sue=9
Sue=5
Jeff=1
Jeff=10'''

# convert to a name: score_list dictionary
# mutliple values for a given key go into a list
data_dict = {}
for line in data_str.split():
    name, score = line.split('=')
    # [] indicates that scores go into a list
    data_dict.setdefault(name, []).append(int(score))

print(data_dict)
print('Second score for Sue = {}'.format(data_dict['Sue'][1]))
'''
{'Bob': [7, 4, 3], 'Sue': [2, 9, 5], 'Jeff': [1, 10]}
Second score for Sue = 9
'''

# may be a more readable code
# using a defaultdict() from module collections
import collections
# mutliple values for a given key go into a list
ddict = collections.defaultdict(list)
for line in data_str.split():
    # unpack
    name, score = line.split('=')
    ddict[name].append(int(score))
    
print(ddict)
print(dict(ddict))
'''
defaultdict(<class 'list'>, {'Bob': [7, 4, 3], 'Sue': [2, 9, 5], 'Jeff': [1, 10]})
{'Bob': [7, 4, 3], 'Sue': [2, 9, 5], 'Jeff': [1, 10]}
'''

def invert_dict(d):
    """
    swap key:value dictionary pairs and take care of collisions
    """
    t = {}
    for k, v in d.items():
        t.setdefault(v, []).append(k)
    return t

# a state:senator test dictionary
state_senator = {
'Arizona': 'Flake',
'Colorado': 'Udall',
'New Mexico': 'Udall',
'California': 'Boxer',
'Iowa': 'Harkin',
'New York': 'Schumer'
}

pprint.pprint(state_senator)
print('-'*20)

senator_state = invert_dict(state_senator)

pprint.pprint(senator_state)
'''
{'Boxer': ['California'],
 'Flake': ['Arizona'],
 'Harkin': ['Iowa'],
 'Schumer': ['New York'],
 'Udall': ['Colorado', 'New Mexico']}
'''

print('copy()'.center(40, '-'))

# make a shallow copy of the symbols dictionary
new = symbols.copy()
print(new.keys())        # dict_keys(['B', 'Be', 'C', 'H', 'He', 'Li'])
print(type(new.keys()))  # <class 'dict_keys'>
print(list(new.keys()))  # ['B', 'Be', 'C', 'H', 'He', 'Li']

print('pop() popitem()'.center(40, '-'))

# remove key (plus value) from dictionary
new.pop('He', "not found")
print(new.keys())  # dict_keys(['B', 'Be', 'C', 'H', 'Li'])

print(new.pop('He', "not found"))  # not found --> He has been removed before

print("dictionary before dic.popitem():")
print(new)
print("the popped item:")
# remove last key,value pair (last in key hashorder)
print(new.popitem())
print("dictionary after dic.popitem():")
print(new)
'''
dictionary before dic.popitem():
{'B': ('Boron', 10.81), 'Be': ('Beryllium', 9.0121831), 
 'C': ('Carbon', 12.011), 'H': ('Hydrogen', 1.008), 'Li': ('Lithium', 6.94)}
the popped item:
('Li', ('Lithium', 6.94))
dictionary after dic.popitem():
{'B': ('Boron', 10.81), 'Be': ('Beryllium', 9.0121831), 
 'C': ('Carbon', 12.011), 'H': ('Hydrogen', 1.008)}
'''

print('keys(), values(), items(), fromkeys()'.center(60, '-'))

print(new.popitem())
print(new)
print(new.keys())
print(new.values())
print(new.items())
# convert to list to allow indexing
print(list(new.items())[2][1][0])
'''
('H', ('Hydrogen', 1.008))
{'B': ('Boron', 10.81), 'Be': ('Beryllium', 9.0121831), 'C': ('Carbon', 12.011)}
dict_keys(['B', 'Be', 'C'])
dict_values([('Boron', 10.81), ('Beryllium', 9.0121831), ('Carbon', 12.011)])
dict_items([('B', ('Boron', 10.81)), ('Be', ('Beryllium', 9.0121831)), 
            ('C', ('Carbon', 12.011))])
Carbon
'''

# this little trick removes dublicate items from a list
# doing this via a set would upset the order
old_list = [1, 2, 3, 1, 5, 4, 6, 3, 7, 4, 3, 2]
print(old_list)
new_list = list(dict.fromkeys(old_list).keys())
print(new_list)
'''
[1, 2, 3, 1, 5, 4, 6, 3, 7, 4, 3, 2]
[1, 2, 3, 5, 4, 6, 7]
'''

people: list[str] = ['Bob', 'Doris', 'Tony']
users: dict = dict.fromkeys(people)
print(users)
'''
{'Bob': None, 'Doris': None, 'Tony': None}
'''
# give a value other than None
users2: dict = dict.fromkeys(people, 'unknown')
print(users2)
'''
{'Bob': 'unknown', 'Doris': 'unknown', 'Tony': 'unknown'}
'''

print('update()'.center(40, '-'))

# another way to make a copy
new2 = {}
new2.update(symbols)
print(new2.keys())  # dict_keys(['B', 'Be', 'C', 'H', 'He', 'Li'])

# add another dictionary
new3 = {
'N': ('Nitrogen', 14.007),
'O': ('Oxygen', 15.999)
}
new2.update(new3)
print(new2.keys())  # dict_keys(['B', 'Be', 'C', 'H', 'He', 'Li', 'N', 'O'])
print('-'*25)
pprint.pprint(new2)
'''
{'B': ('Boron', 10.81),
 'Be': ('Beryllium', 9.0121831),
 'C': ('Carbon', 12.011),
 'H': ('Hydrogen', 1.008),
 'He': ('Helium', 4.002602),
 'Li': ('Lithium', 6.94),
 'N': ('Nitrogen', 14.007),
 'O': ('Oxygen', 15.999)}
'''

print('<>'*20)

def merge_dicts(dict1, dict2):
    result = {}
    d1_keys = set(dict1.keys())
    d2_keys = set(dict2.keys())
    # take care of values in dict1 and dict2 whose keys are not shared
    ns_keys = d1_keys ^ d2_keys
    result.update([(k,[v]) for (k,v) in dict1.items() if k in ns_keys])
    result.update([(k,[v]) for (k,v) in dict2.items() if k in ns_keys])
    # take care of values in dict1 and dict2 whose keys are shared
    # they are put into a list of values
    for k in d1_keys & d2_keys:
        result[k] = [dict1[k], dict2[k]]
    #print(result, type(result))
    return result

dict1 = {'name': 'Faith', 'age': 35}
dict2 = {'name': 'Frank', 'city': 'Boston'}
dict3 = merge_dicts(dict1, dict2)
print(dict3)
'''
{'age': [35], 'city': ['Boston'], 'name': ['Faith', 'Frank']}
'''

# key names would clash so the last value prevails
dict1.update(dict2)
print(dict1)
'''
{'name': 'Frank', 'age': 35, 'city': 'Boston'}

'''

# a different merge/update
dict4 = {**dict1, **dict2}
print(dict4)
'''
{'name': 'Frank', 'age': 35, 'city': 'Boston'}
'''

print('dictionary comprehension'.center(40, '-'))

# using dictionary comprehension to form a new dictionary
# a copy of dictionary new (what's left)
new4 = {key: val for key, val in new.items()}
print(new4)
'''
{'B': ('Boron', 10.81), 'Be': ('Beryllium', 9.0121831), 'C': ('Carbon', 12.011)}
'''

print('max(), min()'.center(40, '-'))

dict7 = {1:'aaa', 2:'bbb', 3:'AAA', 4:'fff'}
print(dict7)
# only the key max/min are returned
print('Maximum Key', max(dict7))  # 3
print('Minimum Key', min(dict7))  # 1

print('pickle json pprint'.center(40, '-'))

# see also python module shelve

# create the test dictionary
before_d = {}
before_d["Eurythmics"] = "Greatest Hits"
before_d["Queen"] = "Opera Night"
before_d["Maxl Graf"] = "Oktoberfest"

fname = "dict_music1.pkl"
# pickle dump the dictionary to a file
with open(fname, "wb") as fout:
    pickle.dump(before_d, fout)

# pickle load the dictionary back in from the file
with open(fname, "rb") as fin:
    after_d = pickle.load(fin)

# check if dump and load matches
pprint.pprint(before_d)
'''
{'Eurythmics': 'Greatest Hits',
 'Maxl Graf': 'Oktoberfest',
 'Queen': 'Opera Night'}
'''

pprint.pprint(after_d)
'''
{'Eurythmics': 'Greatest Hits',
 'Maxl Graf': 'Oktoberfest',
 'Queen': 'Opera Night'}
'''

# Python module json can be used to dump and load dictionay objects
# json --> JavaScript Object Notation

pfolio_dict = {
'GOOG': ('Google', 200, 549.85), 'YHOO': ('Yahoo', 900, 16.81),
'AAPL': ('Apple', 400, 188.0), "MSFT": ('Microsoft', 300, 26.5)
}

fname = "portfolio.jsn"
# dump the dictionary object to file
# you can look at the .jsn file with an editor
with open(fname, "w") as fout:
    json.dump(pfolio_dict, fout)

# read/load the dictionary object back from file
with open(fname) as fin:
    pfolio_dict2 = json.load(fin)

# testing ...
print(type(pfolio_dict2))
print('-'*20)
print(pfolio_dict2)
'''
<class 'dict'>
--------------------
{'AAPL': ['Apple', 400, 188.0], 'MSFT': ['Microsoft', 300, 26.5], ... }
'''

# "pretty print" format the dictionary with json.dumps()
s = json.dumps(pfolio_dict2, sort_keys=True, indent=2)
print(type(s))
print('-'*20)
print(s)
''' result note effect on ' ...
<class 'str'>
--------------------
{
  "AAPL": [
    "Apple",
    400,
    188.0
  ],
  "GOOG": [
    "Google",
    200,
    549.85
  ],
  "MSFT": [
    "Microsoft",
    300,
    26.5
  ],
  "YHOO": [
    "Yahoo",
    900,
    16.81
  ]
}
'''

# extra: list of tuples and dictionary apps
import operator
player_score = [('frank', 88), ('jerry', 68), ('albert', 99)]

# score is at tuple index 1
index1 = operator.itemgetter(1)
# list of (name, score) tuples
player_score.sort(key=index1, reverse=True)
print('via key=operator.itemgetter(1) -->  score at tuple index=1')
print(player_score)
print(dict(player_score))
'''
via key=operator.itemgetter(1) --> score at tuple index=1
[('albert', 99), ('frank', 88), ('jerry', 68)]
{'albert': 99, 'frank': 88, 'jerry': 68}
'''

# operator.setitem(a, b, c)
# set the value of a at index b to c
# eg. set 'jerry' to 'jerky'
operator.setitem(player_score, 2, ('jerky', 55))
print(player_score)  # [('albert', 99), ('frank', 88), ('jerky', 55)]
score_dict = dict(player_score)

# convert a dictionary to a list of tuples
player_score2 = [(player, score) for player, score in score_dict.items()]
print(player_score2)
'''
[('albert', 99), ('frank', 88), ('jerky', 55)]
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

