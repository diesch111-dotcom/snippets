#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" variable_names101.py

How private are variable names in Python code?
Some simple print() tests should give a clue.

a convenience template...

# testing...
print()
print("="*40)

The Spyder IDE 'New File...' command gives the 2 leading Shebang/Hashbang
lines that tell a Unix based system about Python3 location and which codex 
to use, it also adds a triple quote comment area ---  nice!

tested using the Spyder IDE on Linux  dns(vegaseat)  4jul2026
"""

# every body likes to use short names like x
x = 77

# testing...
print(x)  # 77

# is x safe to use in a typical for loop?
for x in "ABCD":
    print(x)
'''
A
B
C
D
'''

# testing...
print(x)  # D  oops we spoiled x, so watch out!

# how about a comprehension?
x = 77
char_list = [x for x in "XYZ"]

# testing...
print(x)  # 77  no leaks here!
print("="*40)

# does it leak out from a function?
def triple(x):
    x =  x * 3
    return x 

y = triple(x)
print(y)  # 231
# testing...
print(x)  # 77 no leak from the function!
print("="*40)

# Class anybody?
class Employee:
    # number of employees to start out
	x = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		# each time an instance is created a new emplyee is added 
		Employee.x += 1

	def fullname(self):
		return f'{self.first} {self.last}'
		self.pay *= self.raise_amount


# create instances of Employee(first, last, pay)
ben = Employee('Ben', 'Dover', 53_000)
stew = Employee('Stew', 'Pitt', 45_000)
bud = Employee('Bud', 'Ugly', 35_000)

print(ben.fullname()) # Ben Dover
print(ben.pay)        # 53000
print(Employee.x)     # 3

# testing...
print(x)  # 77  no leaks from the class!
  




