#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" set101.py

In Python, a set is an unordered collection of unique elements. 
They are highly efficient and are the perfect tool when you need to 
eliminate duplicates or perform mathematical set operations like 
unions and intersections.

Think of a set like a dictionary that only contains keys and no values.

Don't use keyword 'set' for a variable name, use eg. 'set2' instead

Unique: Duplicate elements are automatically ignored.
Unordered: Items do not have a fixed position. You cannot access items 
    using an index (like my_set[0]).
Mutable: You can add and remove items, but the items inside the set must 
    be hashable/immutable (e.g., numbers, strings, tuples). You cannot 
    put a list inside a set.

set2.add(item): Adds a single element.
set2,update([items]): Adds multiple elements (takes a list, tuple, or another set).
set2.remove(item): Removes an element. Throws a KeyError if it doesn't exist.
set2.discard(item): Removes an element safely. Does nothing if the item isn't there.
set2,pop(): Removes and returns an arbitrary element (since they are unordered, 
       (you don't know which one it will pick).

set2 = set(list2) creates a set from a list (removes any dublicate elemnts)

 Python uses a hash table, meaning it takes the exact same fraction of a 
 second.to check if an item exists whether your set has 5 items or 
 5,000,000 items. A list would be much slower!     

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""


# Creating a set with elements
fruits = {"apple", "banana", "cherry"}

# Automatically removing duplicates
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}

emails = ["a@test.com", "b@test.com", "a@test.com"]
# convert set to list
unique_emails = list(set(emails))
print(unique_emails) # ['a@test.com', 'b@test.com']


not_a_set =  {}  # This is a dict
is_a_set = set() # This is the correct way to create an empty set
print(is_a_set)  # set()

tags = {"python", "coding"}

tags.add("ai")               # {'python', 'coding', 'ai'}
tags.update(["web", "data"]) # {'python', 'coding', 'ai', 'web', 'data'}

tags.remove("coding")        # Removes 'coding'
tags.discard("javascript")   # No 'javascript' but no  crasht

# line of 40 '='
print("="*40)

# This is where sets truly shine. Python provides built-in operators and 
# methods to mimic standard mathematical Venn diagram operations.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"{set_a = }")
print(f"{set_b = }")

print("union()")
# 1. Union (Everything combined)
print(set_a | set_b)          # {1, 2, 3, 4, 5, 6}
print(set_a.union(set_b))     # Same as above

print("intersection()")
# 2. Intersection (Only items in BOTH sets)
print(set_a & set_b)          # {3, 4}
print(set_a.intersection(set_b)) 

print("difference()")
# 3. Difference (Items in set_a that are NOT in set_b)
print(set_a - set_b)          # {1, 2}
print(set_a.difference(set_b))

print("symmetric_difference()")
# 4. Symmetric Difference (Items in set_a or set_b but NOT both)
print(set_a ^ set_b)          # {1, 2, 5, 6}
print(set_a.symmetric_difference(set_b))

print("="*40)

small_set = {1, 2}
large_set = {1, 2, 3, 4}

# Is small_set entirely contained inside large_set?
print(small_set.issubset(large_set))    # True

# Does large_set completely contain small_set?
print(large_set.issuperset(small_set))  # True

# Do they share NO elements at all?
print(small_set.isdisjoint({5, 6}))     # True (They share nothing)

print("="*40)



