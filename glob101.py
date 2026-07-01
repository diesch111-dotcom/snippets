#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" glob101.py

Python's glob module is a built-in library used to search for files and 
directories using pattern matching. It uses Unix shell-style wildcards 
rather than complex regular expressions, making it incredibly handy for 
quick file-management tasks.

* :     Matches zero or more characters
? :     Matches exactly one character
[] :    Matches any character inside the brackets 
[0-9] : Matches any single digit

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""

import glob

# list of all .txt files in the current dirrectory
txt_files_list = glob.glob('*.txt')
print(txt_files_list)

''' possible result...
['Text1.txt', 'Text2.txt', 'Names.txt', 'hexfile.txt', 'mystring.txt', ...]
'''

print("="*50)

# via slicing
print("show last 3 items:")
for item in txt_files_list[-3:]:
    print(item)

'''  possible result...
show last 3 items:
os_operations101.py.txt
math_operations101.py.txt
list_operations101.py.txt
'''

print("="*50)

# list all .jsn jason files 
jsn_files_list = glob.glob('*.jsn')
print(jsn_files_list)

''' possible result...
['mylist.jsn', 'mylist4.jsn', 'portfolio.jsn']
'''

print("="*50)

# list all .jsn jason files in subdirectory 'data'
jsn_files_list2 = glob.glob('../data/*.jsn')
for item in jsn_files_list2:
    print(item)

''' possible result...
../data/all_portfolio_wed2026.jsn
../data/div_portfolio-2023-11-17.jsn
../data/div_portfolio-2024-01-10.jsn
../data/div_portfolio-2024-05-09.jsn
../data/div_portfolio-2024-05-13.jsn
../data/div_portfolio-2024-07-19.jsn
../data/all_portfolio-2026-06-25.jsn
../data/all_portfolio_mean_var_std_dict-2026-06-25.jsn
'''

print("="*50)

# all .txt files starting with char 'd' in subdirectory 'data'
dir_files = "../data/d*.txt"
txt_files_list2 = glob.glob(dir_files)
print(txt_files_list2)

''' possible result...
['../data/data123.txt', '../data/dividend_dictionary2023.txt', ...]
'''

print("="*50)

# find all ,htm files in this folder and all subfolders
all_htm_files = glob.glob('../**/*.htm')
for filename in all_htm_files:
    print(filename)

'''possible result...
../aatest_gz/html_table.htm
../aatest_gz/html_calendar0641.htm
../MatPlot/matplotlib  python plotting — Matplotlib v0.99.1.1 documentation.htm
../mpmath/mpmath 0.19 documentation.htm
../docs/numpy_functions.htm
../docs/Pygame Documentation.htm
../docs/mpmath 0.19 documentation.htm
../docs/PySide.QtCore — PySide v1.0.7 documentation.htm
../docs/PyQt Class Reference.htm
../docs/PySide.QtGui — PySide v1.0.7 documentation.htm
../docs/Numpy_Example_List_With_Doc.htm
../PIL/TwoJpegs.htm
../aatest_af/html_calendar0641.htm
'''





