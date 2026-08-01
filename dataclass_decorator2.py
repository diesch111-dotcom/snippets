#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" dataclass_decorator2.py

A class combines methods/functions that belong together
(class names by convention are capitalized)

Introduced in Python 3.7, dataclass decorators are designed to save you from 
writing tedious boilerplate code required by regular class constructs

(double underline also known as "dunter")
vars() function returns the __dict__ attribute of an object/instance

works with Mac OSX and Spyder IDE    vegaseat  15jun2026
"""

# needs Python 3.7+
from dataclasses import dataclass
import inspect


# the @dataclass decorator simplifies the class construct
@dataclass
class Animal2:
    name: str
    sound: str
    age: int
    #print(self)  # testing only
 
    def speak(self):
        # print(self) for testing only, gives an odd result
        # shows result of __repr__(self)
        print(f'{self = }')  
        print(f"{self.sound}! I am {self.age} years old already")
     
    # subs for print(instance)
    def __repr__(self):
        # the first argument of a class method is always self
        return f"I am a {self.name} and go {self.sound}"
        

# create a few class instances
# remember to supply the name and the sound for each animal
dog = Animal2("dog", "woof", 4)
cat = Animal2("cat", "meeouw", 9)
cow = Animal2("cow", "mooh", 3)

print(dog)
print(vars(dog))

'''
I am a dog and go woof
{'name': 'dog', 'sound': 'woof', 'age': 4}
'''

print("="*40)

# you can also access variables associated with the instance
# since cow is the instance
# self.sound becomes cow.sound
cow.speak()

print(cow.sound)

'''
self = I am a cow and go mooh
mooh! I am 3 years old already
mooh
'''

print("="*40)

# also ...
print(vars(cat))

# get the variables that a class instance needs
print(inspect.signature(Animal2))

'''
{'name': 'cat', 'sound': 'meeouw', 'age': 9}
(name: str, sound: str, age: int) -> None
'''

print("="*40)
