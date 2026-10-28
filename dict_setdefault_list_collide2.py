#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' dict_setdefault_list_collide2.py

Put values in a list when keys collide

vegaseat  27oct2026
'''

import pprint

data = '''\
John 21st
Mary 3rd
John 27th
Tom 9th
Drew 11th'''

data_list = [line for line in data.split('\n')]

print(data_list)

print('-'*62)

data_dict = {}
for item in data_list:
    k, v = item.split()
    # default is [], a list
    data_dict.setdefault(k, []).append(v)

pprint.pprint(data_dict, width=40)

''' result ...
['John 21st', 'Mary 2rd', 'John 27th', 'Tom 9th', 'Drew 11th']
------------------------------------------------------------
{'Drew': ['11th'],
 'John': ['21st', '27th'],
 'Mary': ['3rd'],
 'Tom': ['9th']}
'''
