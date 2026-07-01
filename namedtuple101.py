#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" namedtuple101.py

Python's 'namedtuple' (found in the built-in collections module) is a great 
tool for a quick, lightweight way to group data together without writing a 
full, formal class.

Think of it as a regular tuple, that can access the fields by name 
(like an object) instead of just by index numbers. This makes code much 
easier to read and maintain.

Readability: user.email is much clearer than user[2].
Memory Efficient: They use no more memory than a standard tuple because 
    they don't have a per-instance __dict__ attribute.
Immutable: Just like regular tuples, once you create them, they cannot be 
    changed. Great for data integrity.

using Python 3.7 or newer, you might also want to look into dataclasses

Use namedtuple if...	
You want the data to be strictly immutable.
You want to unpack it like a normal tuple (x, y = point).
You need maximum performance and lowest memory overhead.

Use dataclasses if...
You need the data to be mutable (changeable).
You need advanced features like default values or type hints.
You want it to look and act like a standard Python class.

cannot pickle namedtuples or classes

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""

#from collections import namedtuple
import collections as coll


# create the named tuple
# (Name of the type, and a list of field names)
EmpRec = coll.namedtuple('record', 'name, department, salary')

# load the named tuple and create instances = named indexes
bob = EmpRec('Bob Zimmer', 'finance', 77123)
tim = EmpRec('Tim Bauer', 'shipping', 34231)

# another approach
fred_list = ['Fred Flint', 'purchasing', 42350]
# create a named index from a list
fred = EmpRec._make(fred_list)

# create a named index from an existing named index
john = fred._replace(name='John Ward', salary=49200)

# create a default named index for hourly manufacturing workers
# and apply it to new named indexes
default = EmpRec('addname', 'manufacturing', 26000)
mike = default._replace(name='Mike Holz')
gary = default._replace(name='Gary Wood')
carl = default._replace(name='Carl Boor')

# access by named index
print(bob.name, bob.salary)  # Bob Zimmer 77123
# or access by numeric index like a regular tuple
print(tim[0], tim[2])        # Tim Bauer 34231

print('-'*40)

# access from a list of named indexes
emp_list = [bob, fred, tim, john, mike, gary, carl]
for emp in emp_list:
    print( "%-15s works in %s" % (emp.name, emp.department) )

""" result...
Bob Zimmer      works in finance
Fred Flint      works in purchasing
Tim Bauer       works in shipping
John Ward       works in purchasing
Mike Holz       works in manufacturing
Gary Wood       works in manufacturing
Carl Boor       works in manufacturing
"""

print('-'*40)

# convert a named index to a dictionary via OrderedDict
# (or standard dict in Python 3.7+)
print( dict(bob._asdict()) )
"""
{'department': 'finance', 'salary': 77123, 'name': 'Bob Zimmer'}
"""

# list the fieldnames of a named index
print(bob._fields)  # ('name', 'department', 'salary')

# get the variables that a namedtuple instance needs
import inspect
print(inspect.signature(EmpRec))  # (name, department, salary)
