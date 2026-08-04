#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' combinations_permutations-(via-factorials).py

find the number of unordered combinations (like lottery numbers)
type "n choose r"
also number of permutations (allows repeats)

there are 2 types of combinations:
repetition is allowed: such as coins in your pocket (5,5,5,10,10)
no repetition: such as lottery numbers (2,14,15,27,30,33)

see also:
http://www.mathwords.com/c/combination_formula.htm
http://www.mathwords.com/p/permutation_formula.htm
http://www.mathwords.com/a_to_z.htm
https://www.mathsisfun.com/combinatorics/combinations-permutations.html
https://math.stackexchange.com/questions/2125827/probability-of-guessing-a-password

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

from math import factorial


def number_combinations(n, r):
    '''
    return the number of unordered combinations of
    r items taken from a population of size n
    uses algorithm n!/(r!*(n-r)!)
    '''
    return factorial(n)/factorial(r)/factorial(n-r)


print("""\
How many different committees of 4 students
each can be chosen from a group of 15 students?""")
print("{:,}".format(int(number_combinations(15, 4))))
'''
How many different committees of 4 students
each can be chosen from a group of 15 students?
1365
'''

print("""\
There are 100 printable characters on a computer keyboard.
How many different 10 character passwords can you make?""")
print("{:,}".format(int(number_combinations(100, 10))))
'''
There are 100 printable characters on a computer keyboard.
How many different 10 character passwords can you make?
17,310,309,456,440
'''

def number_permutations(n, k):
    '''
    number of possible permutations of 
    k objects from a set of n
    '''
    return factorial(n)/factorial(n-k)


# a permutation problem
# number of possible permutations of k objects from a set of n
# p = n! / (n-k)!
print("""\
How many ways can 4 students from a group of 15 be lined up 
for a photograph?""")
print("{:,}".format(int(number_permutations(15, 4))))
'''
How many ways can 4 students from a group of 15 be lined up 
for a photograph?
32,760
'''

print("""\
How many ways can one enter a 6 digit numeric pass-code on a 
0 to 9 keypad?""")
print("if digits can be repeated = {:,}".format(10**6))
print("if digits can not be repeated = {:,}".format(10*9*8*7*6*5))
'''
How many ways can one enter a 6 digit numeric pass-code on a 
0 to 9 keypad?
if digits can be repeated = 1,000,000
if digits can not be repeated = 151,200
'''

print("""\
What is the probability of winning a 6/49 lottery?
That is 49 numbers, pick 6 (unordered))""")
probability = int(number_combinations(49, 6))
print("the probability of winning a 6/49 lottery is {:,} to 1".format(probability))
'''
What is the probability of winning a 6/49 lottery?
That is 49 numbers, pick 6 (unordered))
the probability of winning a 6/49 lottery is 13,983,816 to 1
'''
