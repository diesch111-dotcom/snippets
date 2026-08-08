#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Nato_alphabet_dict.py

Create a dictionary for the
standard NATO phonetic alphabet for English

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

# copied from a nato war manual
nato_alphabet_str = '''\
A = Alpha
B = Bravo
C = Charlie
D = Delta
E = Echo
F = Foxtrot
G = Golf
H = Hotel
I = India
J = Juliet
K = Kilo
L = Lima
M = Mike
N = November
O = Oscar
P = Papa
Q = Quebec
R = Romeo
S = Sierra
T = Tango
U = Uniform
V = Victor
W = Whiskey
X = Xray
Y = Yankee
Z = Zulu'''

# convert to a dictionary
nato_alphabet_dict = {}
for line in nato_alphabet_str.split('\n'):
    k, v = line.split('=')
    # build the dictionary
    nato_alphabet_dict[k.strip()] = v.strip()

# testing
import pprint
pprint.pprint(nato_alphabet_dict)

'''
{'A': 'Alpha',
 'B': 'Bravo',
 'C': 'Charlie',
 'D': 'Delta',
 'E': 'Echo',
 'F': 'Foxtrot',
 'G': 'Golf',
 'H': 'Hotel',
 'I': 'India',
 'J': 'Juliet',
 'K': 'Kilo',
 'L': 'Lima',
 'M': 'Mike',
 'N': 'November',
 'O': 'Oscar',
 'P': 'Papa',
 'Q': 'Quebec',
 'R': 'Romeo',
 'S': 'Sierra',
 'T': 'Tango',
 'U': 'Uniform',
 'V': 'Victor',
 'W': 'Whiskey',
 'X': 'Xray',
 'Y': 'Yankee',
 'Z': 'Zulu'}
'''
