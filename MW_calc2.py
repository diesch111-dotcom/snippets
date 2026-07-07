#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" MW_calc2.py

The organic chemist synhesizes a compound that will have some use
in healthcare, as a color, a fragrance, a taste, or in agriculture etc.
The compound has to be tested by analytical chemists to have proof
of its makeup.  To do so, the compound is burned, radiated, magnetized
fragmented using analytical procedures like UV, IR, NMR, massSpec, HPLC
and so on ...
Some basic information needed is the structure, molecular formula, 
molecular weight and the percent of each element in the compound.

Given the molecular formula this program calculates
molecular weight (g/mol) 
element percentages

The 'mf' or 'molecular formula' of a chemical compound
should contain all the elements and their count in the molecule.
From a chemist's view a molecule like 'dichlorobenzoic acid''
has a benzene ring with two of its 'H' replaced by 'Cl' and
one of its 'H' replaced by a carboxylic acid group 'COOH',
so a chemist could write it like this:
mf = "C6H3Cl2COOH"
or simply add all the individual elements like this:
mf = "C7H4Cl2O2"

This program should take either approach.


using the Spyder IDE on Linux  dns(vegaseat) 4jul2026
"""

from collections import defaultdict
import pprint

# elements typically found in organic molecules
# might have to add some special ones
dict_org2 = \
{'C': ('Carbon', 6, 12.011),
 'Ca': ('Calcium', 20, 40.078),
 'Cl': ('Chlorine', 17, 35.45),
 'Co': ('Cobalt', 27, 58.933194),
 'Cu': ('Copper', 29, 63.546),
 'F': ('Fluorine', 9, 18.998403163),
 'Fe': ('Iron', 26, 55.845),
 'H': ('Hydrogen', 1, 1.008),
 'Hg': ('Mercury', 80, 200.592),
 'I': ('Iodine', 53, 126.90447),
 'K': ('Potassium', 19, 39.0983),
 'Li': ('Lithium', 3, 6.94),
 'Mg': ('Magnesium', 12, 24.305),
 'Mn': ('Manganese', 25, 54.938044),
 'Mo': ('Molybdenum', 42, 95.95),
 'N': ('Nitrogen', 7, 14.007),
 'Na': ('Sodium', 11, 22.98976928),
 'O': ('Oxygen', 8, 15.999),
 'P': ('Phosphorus', 15, 30.973761998),
 'Pb': ('Lead', 82, 207.2),
 'S': ('Sulfur', 16, 32.06),
 'Sb': ('Antimony', 51, 121.76),
 'Se': ('Selenium', 34, 78.971),
 'Si': ('Silicon', 14, 28.085),
 'Sn': ('Tin', 50, 118.71),
 'Ti': ('Titanium', 22, 47.867),
 'V': ('Vanadium', 23, 50.9415),
 'Zn': ('Zinc', 30, 65.38), 
 'Zr': ('Zirconium', 40, 91.224)}


def create_tuple_list(mf):
    """"
    create an (element, count) tuple list from a
    molecular formula string 'mf' then return the tuple list
    coded this in the late nineties
    """
    char_list = list(mf)
    temp_list = []
    temp_str = ""
    temp_num = ""
    for x, c in enumerate(char_list):
        #print x, c
        if c.isupper():
            temp_str = ""
            temp_num = ""
        if c.isalpha():
            temp_str += c
        if c.isdigit():
            temp_num += c
        # do your look ahead
        if x+1 < len(char_list):
            if char_list[x+1].isupper() and temp_num == "":
                temp_num = "1"
            if char_list[x+1].isupper():
                temp_list.append((temp_str, int(temp_num)))
        # except for the last element
        else:
            if temp_num == "":
                temp_num = "1"
            temp_list.append((temp_str, int(temp_num)))
    return temp_list


# eg. dichlorobenzoic acid
# is a benzene ring with two of its H replaced by Cl and
# one of its H replaced by a carboxylic acid group COOH
# a chemist could write it like this
mf = "C6H3Cl2COOH"
#mf = "C7H4Cl2O2"

tuple_list = create_tuple_list(mf)

# testing...
#print(tuple_list)
'''
[('C', 6), ('H', 3), ('Cl', 2), ('C', 1), ('O', 1), ('O', 1), ('H', 1)]
'''

# initialize a defaultdict with a 'list' factory
e_dict_grouped = defaultdict(list)
for key, value in tuple_list:
    # handles collisons
    e_dict_grouped[key].append(value)
    
# testing...
#print(e_dict_grouped)
'''
defaultdict(<class 'list'>, {'C': [6, 1], 'H': [3, 1], 'Cl': [2], 'O': [1, 1]})
'''

mweight = 0
for element, lst in e_dict_grouped.items():
    # multiply element atomic weight by element count
    e_weight = dict_org2[element][2]  * sum(lst)
    mweight += e_weight
    

# create an element:percent dictionary using a fancy dictionary comprehension
# here is a good case against long variable names
e_percent_dict = {dict_org2[elmnt][0]:100 * dict_org2[elmnt][2]*sum(lst)/mweight
                 for elmnt, lst in e_dict_grouped.items()}  

# testing...  
#pprint.pprint(e_percent_dict, width=72, compact=True)  
"""
{'Carbon': 44.01775851146816,
 'Chlorine': 37.11905846382594,
 'Hydrogen': 2.11091740093295,
 'Oxygen': 16.752265623772953}
"""

print("="*75)

# we are done, show the result
print(f"Compound {mf} has a molecular weight of {mweight} g/mol and contains:")
for element, percent in e_percent_dict.items(): 
    print(f"{percent:>6.2f}% {element}")

""" final result...
===========================================================================
Compound C6H3Cl2COOH has a molecular weight of 191.007 g/mol and contains:
 44.02% Carbon
  2.11% Hydrogen
 37.12% Chlorine
 16.75% Oxygen
===========================================================================
"""

print("="*75)
