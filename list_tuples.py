#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' list_tuples.py

List methods that are not in tuple methods
tip from raymondh

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

import pprint

print('list methods that are not in tuple methods:')
pprint.pprint(sorted(set(dir(list)) - set(dir(tuple))))

'''
list methods that are not in tuple methods:
['__delitem__',
 '__iadd__',
 '__imul__',
 '__reversed__',
 '__setitem__',
 'append',
 'clear',
 'copy',
 'extend',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']
'''
