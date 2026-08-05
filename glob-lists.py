#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" glob-lists.py

Python's glob module is a built-in library used to search for files and 
directories using pattern matching. It uses Unix shell-style wildcards 
rather than complex regular expressions, making it incredibly handy for 
quick file-management tasks.

* :     Matches zero or more characters
? :     Matches exactly one character
[] :    Matches any character inside the brackets 
[0-9] : Matches any single digit

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
"""

import glob
import pprint
import os
# change to working diredory
# this will find eg. '../image/textfile.txt'
os.getcwd()

print("list of all .txt files in the current directory")
txt_files_list = glob.glob('*.txt')
print("use slicing to show first 3 files")
print(txt_files_list[:3])

''' possible result...
list of all .txt files in the current directory
use slicing to show first 3 files
['Install_python_modules.txt', 'datetime_format_specifiers.txt', 
'Dropbox_remove.txt']
'''

print("="*50)

# use slicing to show last 3 files
print("show last 3 files:")
for item in txt_files_list[-3:]:
    print(item)

'''  possible result...
show last 3 items:
Dropbox_remove.txt
hexfile.txt
new_usb_drive_on_iMac.txt
'''

print("="*50)

# list all .jsn jason files in sorted order
jsn_files_list = sorted(glob.glob('*.jsn'))
print(jsn_files_list)

''' possible result...
['mylist.jsn', 'mylist4.jsn', 'portfolio.jsn']
'''

print("="*50)

# list all .jsn jason files in subdirectory 'data'
jsn_files_list2 = sorted(glob.glob('../data/*.jsn'))
for item in jsn_files_list2:
    print(item)

''' possible result...
../data/FNames2.jsn
../data/all_portfolio-2026-07-29.jsn
../data/all_portfolio-2026-07-30.jsn
../data/all_portfolio-2026-07-31.jsn
../data/all_portfolio-2026-08-03.jsn
../data/all_portfolio-2026-08-04.jsn
../data/all_portfolio_mean_var_std_dict-2026-07-29.jsn
../data/all_portfolio_wed2026.jsn
...

'''

print("="*50)

print("all .txt files starting with char 'd' in subdirectory 'data'")
dir_files = "../data/d*.txt"
txt_files_list2 = sorted(glob.glob(dir_files))
for file_path in txt_files_list2:
    print(file_path)

''' possible result...
all .txt files starting with char 'd' in subdirectory 'data'
../data/data123.txt
../data/div_summary_portfolio-2023-11-17.txt
../data/div_summary_portfolio-2024-01-10.txt
../data/div_summary_portfolio-2024-05-09.txt
../data/dividend_dictionary2023.txt
../data/dividend_dictionary2024.txt
../data/dividend_dictionary2025.txt
../data/dividend_dictionary2026.txt
'''

print("="*50)

print("find all .htm files in this folder and all subfolders")
all_htm_files = glob.glob('../**/*.htm')
for filename in all_htm_files:
    print(filename)

'''possible result...
find all .htm files in this folder and all subfolders
../PIL/TwoJpegs.htm
../MatPlot/matplotlib  python plotting — Matplotlib v0.99.1.1 documentation.htm
../docs/Pygame Documentation.htm
../docs/numpy_functions.htm
../docs/Numpy_Example_List_With_Doc.htm
../docs/PyQt Class Reference.htm
../docs/PySide.QtGui — PySide v1.0.7 documentation.htm
../docs/mpmath 0.19 documentation.htm
../docs/PySide.QtCore — PySide v1.0.7 documentation.htm
../aatest_gz/html_table.htm
../aatest_gz/html_calendar0641.htm
../mpmath/mpmath 0.19 documentation.htm
../aatest_af/html_calendar0641.htm
'''

print( '='*40 )

print("only .txt and .htm files (full path names) in given directories")
directory_txt = "/home/admin123/AAtest_py/docs/*.txt"
directory_htm = "/home/admin123/AAtest_py/docs/*.htm"
# a simple '+' will do
for path in glob.glob(directory_txt) + glob.glob(directory_htm):
    print( path )

""" possible result...
only .txt and .htm files (full path names) in given directories
/home/admin123/AAtest_py/docs/Colour_Dict_X11.txt
/home/admin123/AAtest_py/docs/Python3.12.2_StandardLibrary.txt
/home/admin123/AAtest_py/docs/namedcolors.txt
/home/admin123/AAtest_py/docs/steganography_made_easy.txt
/home/admin123/AAtest_py/docs/SublimeText-change-Python-version.txt
/home/admin123/AAtest_py/docs/Help_turtle.txt
/home/admin123/AAtest_py/docs/Windchill1.txt
/home/admin123/AAtest_py/docs/Pygame Documentation.htm
/home/admin123/AAtest_py/docs/numpy_functions.htm
/home/admin123/AAtest_py/docs/Numpy_Example_List_With_Doc.htm
/home/admin123/AAtest_py/docs/PyQt Class Reference.htm
/home/admin123/AAtest_py/docs/mpmath 0.19 documentation.htm
"""
