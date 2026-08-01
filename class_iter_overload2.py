#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' class_iter_overload2.py

operator overloading with instance method __iter__()

works with Mac OSX and Spyder IDE    vegaseat  15jun2026
'''

class Reverse:
    """
    custom iterator for looping over a sequence backwards
    hijacks the iterator used by the for loop and uses 
    __iter__(self) and __next__(self) to do the trick
    """
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# Reverse('iterator overload') is a class instance
data = 'iterator overload'
print(data)
rev = ""
for c in Reverse(data):
    rev += c

print(rev)  # little Italy?

''' result...
iterator overload
daolrevo rotareti
'''
