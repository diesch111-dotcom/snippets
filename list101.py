#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" list101.py

Lists are Python’s most versatile and widely used data structure. 
They are ordered, mutable (changeable), and can hold a mix of different 
data types—including other lists.

Positive Indexing: Counts from the left (0, 1, 2...)
Negative Indexing: Counts from the right (-1, -2...)

Slicing allows you to extract a sub-portion of a list: 
[starting-at-index : but-less-than-index [ : step]]
'start' defaults to 0, 'end' to len(sequence), 'step' to 1

Don't use keyword 'list' for a variable name, use eg. 'list2' instead

Modify an item: Assign a new value directly to an index.
list2.append(item): Adds an item to the end of the list.
list2.insert(index, item): Inserts an item at a specific position.
list2.extend(list3): Appends another list to the end.

list2.pop(index): Removes and returns the item at the given index 
    (defaults to the last item if no index is provided).
list2.remove(value): Removes the first occurrence of a specific value. 
    Throws a ValueError if the item isn't there.
list2.clear(): Empties the entire list.
del list2(index): Deletes an item or a slice by index.

len(list2)  length (number of items) of list2
sum(list2)  sum all numeric values in list2
min(list2)  smallest item of list2
max(list2)  largest item of list2

'in' keyword: Check if an item exists in the list (returns True or False).
list2.count(value): Count how many times a value appears.
list2.index(value): Get the index of the first occurrence of a value.

list2.sort(): Sorts the list in-place (permanently changes the original list).
list2.reverse()  reverse the items of a list in place
sorted(list2): Returns a new sorted list, leaving the original list untouched.
Pass reverse=True to either function to sort in descending order.

List comprehensions provide a concise way to create lists, replace messy for loops.
Syntax: list2 = [expression for item in iterable]
or condional:  list2 = [expression for item in iterable if condition]

Assigning a list to a new variable (like list2 = list1) does not copy 
the list; it just creates a new reference to the same exact list in memory. 
If you change one, both change.

list3 = list2.copy() makes a true copy

import collections as coll
# find the difference between 2 lists
# Subtracts the counts of elements
diff = list((coll.Counter(list1) - coll.Counter(list2)).elements())

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""

# creating a list
fruits = ["apple", "banana", "cherry", "date"]
# use indexing to get items
print(fruits[0])   # "apple"  (First item)
print(fruits[-1])  # "date"   (Last item)
print(fruits[-2])  # "cherry" (Second to last item)

# line of 40 '='
print("="*40)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slicing
print(numbers[2:6])   # [2, 3, 4, 5] (From index 2 up to, but not including, 6)
print(numbers[:4])    # [0, 1, 2, 3] (From the beginning up to index 4)
print(numbers[7:])    # [7, 8, 9]    (From index 7 to the end)
print(numbers[::2])   # [0, 2, 4, 6, 8] (Every 2nd item - step size 2)
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (Reverses the list!)

print("="*40)

print(f"numbers = {numbers}")
print(f"sum(numbers) = {sum(numbers)}")
print(f"max(numbers) = {max(numbers)}")
print(f"min(numbers) = {min(numbers)}")

colors = ["red", "green"]

colors[1] = "blue"         # ['red', 'blue'] (Modifies index 1)
colors.append("yellow")    # ['red', 'blue', 'yellow']  added 'yellow'
# insert item "orange" at position 1 and shifts the rest up
colors.insert(1, "orange") # ['red', 'orange', 'blue', 'yellow']
# add another list ["purple", "pink"] to the end
colors.extend(["purple", "pink"]) 
# ['red', 'orange', 'blue', 'yellow', 'purple', 'pink']

print("="*40)

items = ["laptop", "mouse", "keyboard", "mouse"]

# Removes 'mouse' and returns it. items is now ['laptop', 'mouse', 'keyboard']
last_item = items.pop() 
print(f"item popped = '{last_item}' items left = {items}")
 # Removes the remaing item 'mouse'. items is now ['laptop', 'keyboard']
items.remove("mouse") 
print(items)
# Removes 'laptop'. items is now ['keyboard'] 
del items[0]             

print("="*40)

names = ["Alice", "Bob", "Charlie", "Alice"]

print(len(names))           # 4
print("Bob" in names)       # True
print(names.count("Alice")) # 2
print(names.index("Bob"))   # 1

print("="*40)

nums = [4, 1, 3, 2]

# 'in-place' sorting
nums.sort() 
print(nums)  # [1, 2, 3, 4]

# 'out-of-place' (original list intact) sorting (descending)
letters = ['b', 'd', 'a', 'c']
print(sorted(letters, reverse=True))  # ['d', 'c', 'b', 'a']

print([c for c in "love"][::-1])  # ['e', 'v', 'o', 'l']

# The Old Way:
squares1 = []
for x in range(5):
    squares1.append(x**2)
# squares1 is [0, 1, 4, 9, 16]

# The List Comprehension Way:
squares2 = [x**2 for x in range(5)]
# squares2 is [0, 1, 4, 9, 16]

# With an 'if' condition (get only even squares):
even_squares = [x**2 for x in range(5) if x % 2 == 0]
# even_squares is [0, 4, 16]

print("="*40)

original = [1, 2, 3]

# Wrong copy via aliasing
fake_copy = original
fake_copy.append(4)  # This updates 'original' too!

# correct way to copy:
true_copy = original.copy()  # or use original[:]
true_copy.append(5)  # 'original' remains untouched

# remove duplicates in a list by converting to a set
my_list2 = list("abcdefdghbf")
print(my_list2)
my_set2 = set(my_list2)  
# ['a', 'b', 'c', 'd', 'e', 'f', 'd', 'g', 'h', 'b', 'f']
# set items are unique, but in hash-order just like keys in a dictionary
print(my_set2)   # {'d', 'e', 'h', 'g', 'b', 'c', 'f', 'a'}
# sorted() produces automaticaly a list from the set
print(sorted(my_set2))  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
my_str2 = "".join(sorted(my_set2))
print(my_str2)  # abcdefgh


# If you don't know how many items are in the list, or you only care 
# about a few of them, you can use the asterisk (*) operator to grab 
# "the rest" of the items.
print("unpack a list:")
first, second, *rest = my_list2
print(first, second, rest )
# a b ['c', 'd', 'e', 'f', 'd', 'g', 'h', 'b', 'f']
first, *middle, rest = my_list2
print(first, middle, rest )  
# a ['b', 'c', 'd', 'e', 'f', 'd', 'g', 'h', 'b'] f
_, *middle, _ = my_list2
print(middle)

fruits = ["apple", "banana", "cherry"]

# unpacking without a '*', number of items have to match number of elements
item1, item2, item3 = fruits

print(item1)  # apple
print(item2)  # banana
print(item3)  # cherry

print("="*40)

import collections as coll
#help(collections)

list_a = ['apple', 'apricot', 'banana', 'cherry']
list_b = ['apple', 'banana']

print(list_a)
print(list_b)
print("difference between two lists")
# find the difference between 2 lists
# Subtracts the counts of elements
diff = list((coll.Counter(list_a) - coll.Counter(list_b)).elements())
print(diff)

'''
['apple', 'apricot', 'banana', 'cherry']
['apple', 'banana']
difference between two lists
['apricot', 'cherry']
'''

