#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sort_assisting.py

Explore various ways to assist sorting

key=helper_function
key=len
key=int
key=float
key=lambda
key=operator.itemgetter()
Schwartzian transform algorithm

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import operator
import pprint

print('sorting numeric strings'.center(65, '-'))

print('sort as string values:')
a = ['77', '123', '18']
a.sort()
print(a)
print('sort as integer values:')
a.sort(key=int)
print(a)
b = ['77.9', '123.01', '18.7']
print('sort as string values:')
print(sorted(b)) 
print('sort as float values:')
print(sorted(b, key=float))

'''
sort as string values:
['123', '18', '77']
sort as integer values:
['18', '77', '123']
sort as string values:
['123.01', '18.7', '77.9']
sort as float values:
['18.7', '77.9', '123.01']
'''

print('helper sort (name, score) by score'.center(65, '-'))

def sort_score(tup):
    """
    a typical helper function
    tup is each tuple in the list to be sorted
    (item at index 1 of each tuple is the score)
    """
    return tup[1]

player_score = [('frank', 88), ('jerry', 68), ('albert', 99)]
# use helper function
player_score.sort(key=sort_score, reverse=True)
print('via helper function:')
print(player_score)

print('-'*50)

# somewhat simpler using anonymous function lambda ...
player_score = [('frank', 88), ('jerry', 68), ('albert', 99)]
player_score.sort(key=lambda tup: tup[1], reverse=True)
print('via lambda:')
print(player_score)

print('-'*50)

# index 1 is the score
index1 = operator.itemgetter(1)
player_score = [('frank', 88), ('jerry', 68), ('albert', 99)]
player_score.sort(key=index1, reverse=True)
print('via key=operator.itemgetter()')
print(player_score)

'''
via helper function:
[('albert', 99), ('frank', 88), ('jerry', 68)]
--------------------------------------------------
via lambda:
[('albert', 99), ('frank', 88), ('jerry', 68)]
--------------------------------------------------
via key=operator.itemgetter()
[('albert', 99), ('frank', 88), ('jerry', 68)]
'''

print('sort by last list item via itemgetter(-1)'.center(65, '-'))

# sort a list of lists by last item
data = [ "Dr. Heidi Karin Hirsch",
         "Miss Arlene Auerbach",
         "Mr. and Mrs. Larry Zoom",
         "Mr. Frank Paul Lummer",
         "Vice President Colter" ]
# convert data into list of lists
data_as_lists = [line.split() for line in data]
print('unsorted data lines:')
for each_item in data_as_lists:
	print(' '.join(each_item))
print('-'*35)
# -1 implies last item
data_as_lists.sort(key=operator.itemgetter(-1))
print('sorted by last item in each data line:')
for each_item in data_as_lists :
   print(" ".join(each_item))
   
'''
unsorted data lines:
Dr. Heidi Karin Hirsch
Miss Arlene Auerbach
Mr. and Mrs. Larry Zoom
Mr. Frank Paul Lummer
Vice President Colter
-----------------------------------
sorted by last item in each data line:
Miss Arlene Auerbach
Vice President Colter
Dr. Heidi Karin Hirsch
Mr. Frank Paul Lummer
Mr. and Mrs. Larry Zoom
'''

print('sort two_character cards by first and last char'.center(65, '-'))

cards = ['3S', 'KD','5S', 'TC','2D','3D']
print('unsorted:')
print(cards)
print('sorted by first character in each card:')
print(sorted(cards))
print('sorted by second character (index=1) in each card')
print(sorted(cards, key=operator.itemgetter(1)))

'''
unsorted:
['3S', 'KD', '5S', 'TC', '2D', '3D']
sorted by first character in each card:
['2D', '3D', '3S', '5S', 'KD', 'TC']
sorted by second character (index=1) in each card
['TC', 'KD', '2D', '3D', '3S', '5S']
'''

print('sort complex combination of lists/tuples'.center(65, '-'))

# sort a more complex combination of lists/tuples:
mylist = [
(1, ['a', '3.1', 'ad']),
(2, ['b', '4.0', 'bd']),
(3, ['c', '2.5', 'cd']),
]
print(mylist)
print('sort by item at index [1][1] of each tuple:')
newlist = sorted(mylist, key=lambda tup: tup[1][1])
print(newlist)

'''
[(3, ['c', '2.5', 'cd']), (1, ['a', '3.1', 'ad']), (2, ['b', '4.0', 'bd'])]
sort by item at index [1][1] of each tuple:
[(3, ['c', '2.5', 'cd']), (1, ['a', '3.1', 'ad']), (2, ['b', '4.0', 'bd'])]
'''

print('sorting via Schwartzian transform algorithm'.center(65, '-'))

print('temporarily put a copy of indexed item in front')
templist = [(x[1][1], x) for x in mylist]
print(templist)
templist.sort()
print('templist after sort():')
print(templist)
# remove temporary front item after sorting
newlist2 = [val for (temp, val) in templist]
print('rebuilt normal list:')
print(newlist2)

'''
temporarily put a copy of indexed item in front
[('3.1', (1, ['a', '3.1', 'ad'])), ('4.0', (2, ['b', '4.0', 'bd'])), ('2.5', (3, ['c', '2.5', 'cd']))]
templist after sort():
[('2.5', (3, ['c', '2.5', 'cd'])), ('3.1', (1, ['a', '3.1', 'ad'])), ('4.0', (2, ['b', '4.0', 'bd']))]
rebuilt normal list:
[(3, ['c', '2.5', 'cd']), (1, ['a', '3.1', 'ad']), (2, ['b', '4.0', 'bd'])]
'''

print('sorting by length of word'.center(65, '-'))

text = "I have taken a vow of poverty to annoy me send money"
mylist = text.split()
print("Original list:\n{}".format(mylist ))
mylist_sorted = sorted(mylist, key=len, reverse=True)
print("Sorted by length of word:\n{}".format(mylist_sorted))

"""
Original list:
['I', 'have', 'taken', 'a', 'vow', 'of', 'poverty', 'to', 'annoy',
 'me', 'send', 'money']
Sorted by length of word:
['poverty', 'taken', 'annoy', 'money', 'have', 'send', 'vow', 'of',
 'to', 'me', 'I', 'a']
"""

print("Find the longest word:")
print(max(mylist, key=len))   # poverty

print('sorting mixed ascending/descending'.center(65, '-'))

def sort_helper(tup):
    '''
    helper function for sorting of a list of (name, age, weight) tuples
    sort by looking at age tup[1] first then weight tup[2]
    the minus sign indicates reverse order (descending) sort for age
    '''
    return (-tup[1], tup[2])

# original list of (name, age, weight) tuples
q = [('Tom', 35, 244), ('Joe', 35, 150), ('Andi', 24, 175), ('Zoe', 35, 210)]
print('Original list of (name, age, weight) tuples:')
print(q)
print('-'*70)
print("List sorted without helper function:")
print(sorted(q))
print('-'*70)
print('List sorted with helper function')
print('age (descending), same age weight (ascending):')
print(sorted(q, key=sort_helper))
print('-'*70)
print("Same but using lambda as an anonymous helper function:")
print(sorted(q, key=lambda tup: (-tup[1], tup[2])))

''' result...
Original list of (name, age, weight) tuples:
[('Tom', 35, 244), ('Joe', 35, 150), ('Andi', 24, 175), ('Zoe', 35, 210)]
----------------------------------------------------------------------
List sorted without helper function:
[('Andi', 24, 175), ('Joe', 35, 150), ('Tom', 35, 244), ('Zoe', 35, 210)]
----------------------------------------------------------------------
List sorted with helper function
age (descending), same age weight (ascending):
[('Joe', 35, 150), ('Zoe', 35, 210), ('Tom', 35, 244), ('Andi', 24, 175)]
----------------------------------------------------------------------
Same but using lambda as an anonymous helper function:
[('Joe', 35, 150), ('Zoe', 35, 210), ('Tom', 35, 244), ('Andi', 24, 175)]
'''

print('sorting a dictionary by key'.center(65, '-'))


def sort_by_age(d):
    '''
    helper function for sorting a list of dictionaries
    by the value associated with the given key
    '''
    return d['age']

def sort_by_name(d):
    '''
    helper function for sorting a list of dictionaries
    by the value associated with the given key
    '''
    return d['name']


# a list of name/age dictionaries
d_list = [
{
'name' : 'frank',
'age' : 24,
},
{
'name' : 'joe',
'age' : 21,
},
{
'name' : 'tim',
'age' : 18,
},
{'name' : 'august',
'age' : 75,
}
]
print('original dictionary:')
pprint.pprint(d_list)

print('-'*30)

print("sorted by age:")
pprint.pprint(sorted(d_list, key=sort_by_age))

print('-'*30)

print("sorted by name:")
pprint.pprint(sorted(d_list, key=sort_by_name))

'''
original dictionary:
[{'age': 24, 'name': 'frank'},
 {'age': 21, 'name': 'joe'},
 {'age': 18, 'name': 'tim'},
 {'age': 75, 'name': 'august'}]
------------------------------
sorted by age:
[{'age': 18, 'name': 'tim'},
 {'age': 21, 'name': 'joe'},
 {'age': 24, 'name': 'frank'},
 {'age': 75, 'name': 'august'}]
------------------------------
sorted by name:
[{'age': 75, 'name': 'august'},
 {'age': 24, 'name': 'frank'},
 {'age': 21, 'name': 'joe'},
 {'age': 18, 'name': 'tim'}]
'''

print('-'*70)

# test dictionary with name:[age,weight] pairs
mydict = {
'Zack' : [35, 210],
'Adam' : [24, 175],
'John' : [35, 150],
'Tony' : [35, 244]
}

print('original name:[age,weight] dictionary:')
print(mydict)
# convert to list of (name, age, weight) tuples
mylist = []
for name, sublist in mydict.items():
    age, weight = sublist
    mylist.append((name, age, weight))

print('converted to a list of (name, age, weight) tuples:')
print(mylist)

# sort tuples by age at index 1, and weight at index 2
mylist_age_weight = sorted(mylist, key=operator.itemgetter(1, 2))

print('sorted by age (primary) and weight (secondary):')
print(mylist_age_weight)

''' 
original name:[age,weight] dictionary:
{'Zack': [35, 210], 'Adam': [24, 175], 'John': [35, 150], 'Tony': [35, 244]}
converted to a list of (name, age, weight) tuples:
[('Zack', 35, 210), ('Adam', 24, 175), ('John', 35, 150), ('Tony', 35, 244)]
sorted by age (primary) and weight (secondary):
[('Adam', 24, 175), ('John', 35, 150), ('Zack', 35, 210), ('Tony', 35, 244)]
'''

words = ["banana", "Apple", "cherry", "Dagmar"]

# sort the list in place independent of case
words.sort(key=str.lower)

print(words)
# ['Apple', 'banana', 'cherry', 'Dagmar']
