#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' dict_print_table101.py

Use format() to print the contents of a dictionary as a table
Adjust the table to maximum length of any key

works with Mac OSX and Spyder IDE    vegaseat 15jun2026
'''

# create a dictionary of food:cost pairs
food_dict = {
'almond milk' : 3.29,
'butter' : 2.90,
'bread' : 1.67,
'blue cheese' : 4,
'peanut butter' : 2.48,
'grape jelly' : 1.77
}

# find max length of food keys
max_len = max(len(food) for food in food_dict)

# food keys print in dictionary hash order
# unless you sort them
for food, price in sorted(food_dict.items()):
    print("{fd:{mx}} = ${pr:4.2f}".format(
        fd=food, pr=price, mx=max_len))

''' result ...
almond milk   = $3.29
blue cheese   = $4.00
bread         = $1.67
butter        = $2.90
grape jelly   = $1.77
peanut butter = $2.48
'''

print('-'*26)

# use the dictionary key directly to print one item
sf = "Bread costs ${bread:4.2f}"
print(sf.format(**food_dict))

''' result ...
Bread costs $1.67
'''
