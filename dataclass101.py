#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" dataclass101.py

a class combines methods/functions that belong together
class names by convention are capitalized

Introduced in Python 3.7, dataclass decorators are designed to save you from 
writing tedious boilerplate code required by regular class constructs

If you've ever written a custom class just to hold data, you know the drill: 
    you have to write a custom __init__, a __repr__ so printing it looks nice, 
    and comparison methods like __eq__ so you can compare two objects. 
    dataclasses generate all of that for you automatically behind the scenes.

(double underline also known as "dunter")
vars() function returns the __dict__ attribute of an object/instance

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""

# needs Python 3.7+
from dataclasses import dataclass
import inspect

# hormal class construct
class Animal:
    """
    class names by convention are capitalized
    """
    def __init__(self, animal, sound):
        """
        __init__() is the 'constructor' of the class instance
        when you create an instance of Animal you have to supply
        it with the name and the sound of the animal
        'self' refers to the instance
        if the instance is dog, then
        name and sound will be that of the dog
        'self.' also makes name and sound and methods available
        to all the methods within the class
        """
        self.name = animal
        self.sound = sound
        self.age = age
        print(self)  # testing only

    def speak(self):
        """
        the first argument of a class method is always self
        this method needs to be called with self.speak() within
        the class, or the instance_name.speak() outside the class
        """
        print(f"{self.sound} I am {self.age} years old already")

    def __repr__(self):
        """
        overrides print()
        if you print the instance of the class, this format will display
        """
        # the first argument of a class method is always self
        return f"I am a {self.name} and go {self.sound}"
        

# the @dataclass decorator simplifies the class construct
@dataclass
class Animal2:
    name: str
    sound: str
    age: int
    #print(self)  # testing only
 
    def speak(self):
        print(f'{self = }')  # testing only, an odd result
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

print(dog)  # I am a dog and go woof
print(vars(dog))  # {'sound': 'woof', 'name': 'dog'}

# you can also access variables associated with the instance
# since cow is the instance
# self.sound becomes cow.sound
cow.speak()

'''
self = I am a cow and go mooh
mooh! I am 3 years old already
'''

print(cow.sound)  # mooh
# also ...
print(vars(cat)) # {'name': 'cat', 'sound': 'meeouw', 'age': 9}

# get the variables that a class instance needs
print(inspect.signature(Animal2))
'''
(name: str, sound: str, age: int) -> None
'''

print("="*40)

@dataclass
class PatientDC:
    # the @dataclass decorator simplifies the class construct
    ID: int
    name: str
    sex: chr
    age: int
    address: str
    phone: str
    bdate: str
    height: float
    weight: int

    def ask_address(self):
        print(f"{name} do you still live at: {address}")
        
    def ask_birthday(self):
        print(f"I was born on {bdate}")


# Patients(ID, name, sex, age, address, phone, bdate, height, weight)
# gether data
ID = 12345
name = "Payne N.Diaz"
sex = 'm'
age = 23
address = "105 Blue St  Monroe  KS"
phone = "123-456-9876"
bdate = "11nov1983"
height = 1.7
weight = 173
# create an instance of this patient
frank = PatientDC(ID, name, sex, age, address, phone, bdate, height, weight)
# do something with this instance
frank.ask_address()
'''
Payne N.Diaz do you still live at: 105 Blue St  Monroe  KS
'''
frank.ask_birthday()
'''
I was born on 11nov1983
'''

