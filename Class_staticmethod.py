#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' class_staticmethod.py

DBecorator @staticmethod can add another constructor to a class
it works on a function within a class (no self)
you can use @classmethod for methods within a class (has self)

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

class Person:
    def __init__(self, name, age):
        """
        the initial constructor of this class
        """        
        self.name = name
        self.age = age

    def __str__(self):
        """
        overloads print of class instance
        """
        sf = "Person(%s, %s)" % (self.name, self.age)
        return sf

    @staticmethod
    def from_sequence(seq):
        """
        this function adds another constructor to this class
        """        
        name, age = list(seq)
        return Person(name, age)

    @staticmethod
    def from_dict(dic):
        return Person(dic["name"], dic["age"])


my_tuple = ("John", 32)
my_dict = {"name": "Fred", "age": 35}

anna = Person("Anna", 25)
john = Person.from_sequence(my_tuple)
fred = Person.from_dict(my_dict)

# test it ...
for instance in (anna, john, fred):
    # notice that print(instance) uses __str__() overload
    print(instance)

'''result...
Person(Anna, 25)
Person(John, 32)
Person(Fred, 35)
'''
