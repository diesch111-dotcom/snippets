#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" dict_print_table2.py

Print the contents of a dictionary as a table.
Adjust the table to maximum length of any key.

vegaseat  15jun2026
"""

# create a dictionary of food:cost pairs
food_dict = {
'almond milk' : 3.49,
'butter' : 2.99,
'bread' : 5.29,
'blue cheese' : 4,
'peanut butter' : 2.48,
'grape jelly' : 3.77
}

# find the maximum length of food keys
max_len = max(len(food) for food in food_dict)

# use food keys in sorted order
for food, price in sorted(food_dict.items()):
    print(f"{food.capitalize():{max_len}} = ${price:4.2f}")
    
''' result...
Almond milk   = $3.49
Blue cheese   = $4.00
Bread         = $5.29
Butter        = $2.99
Grape jelly   = $3.77
Peanut butter = $2.48
'''

print('='*22)

# use the dictionary key directly to print one item
sf = "Bread costs ${bread:4.2f}"
print(sf.format(**food_dict))

''' result ...
Bread costs $5.29
'''
