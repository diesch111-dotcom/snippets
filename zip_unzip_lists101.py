#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' zip_unzip_lists101.py

Exploring Python's zip() function
zip() is a generator

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']

# zip the two lists
numlet = zip(numbers, letters)

print(numlet)
# show a list of tuples
print(list(numlet))
'''
<zip object at 0x0000022B30F6F800>
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
'''

print('-'*50)

# refresh the generator
numlet = zip(numbers, letters)
# show a dictionary number:letter
print(dict(numlet))
# zip() in different order
letnum = zip(letters, numbers)
# show a dictionary letter:number
print(dict(letnum))
'''
{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
'''

print('-'*50)

# refresh the generator
numlet = zip(numbers, letters)
print('unzip:')
# this will actually unzip the zipped numlet
print(list(zip(*numlet)))
'''
unzip:
[(1, 2, 3, 4, 5), ('a', 'b', 'c', 'd', 'e')]
'''

print('-'*50)

# extra goofy stuff (makes you think a little) ...
print("convert a list of 4 lists into a list of 3 tuples:")
list_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
print(list_list)
list_tuple = list(zip(*list_list))
print(list_tuple)
'''
convert a list of 4 lists into a list of 3 tuples:
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
[(0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11)]
'''
