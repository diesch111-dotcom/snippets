#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" names_funtions_methods.py

Show all names of Python builtin functions, methods and modules;
avoid using any of those names for your methods/functios/variables or
you will get potential conflicts sometimes later. 

tested using the Spyder IDE on Linux  dns(vegaseat)  4jul2026
"""

print("Show all Python builtin functions, class methods and alike:")
# do an alphabetical sort first...
print('\n'.join(sorted(dir(__builtins__))))

print('='*40)

'''
Show all Python builtin functions, class methods and alike:
__class__
__class_getitem__
__contains__
__delattr__
__delitem__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getstate__
__gt__
__hash__
__init__
__init_subclass__
__ior__
__iter__
__le__
__len__
__lt__
__ne__
__new__
__or__
__reduce__
__reduce_ex__
__repr__
__reversed__
__ror__
__setattr__
__setitem__
__sizeof__
__str__
__subclasshook__
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

# optional ...
#print("Show all the modules Python currently knows about:")

#help("modules")
