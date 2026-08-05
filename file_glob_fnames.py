#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' file_glob_fnames.py

Use module glob to list filenames and pathnames
glob takes care of upper/lower case variations

Python's glob module is a built-in library used to search for files and 
directories using pattern matching. It uses Unix shell-style wildcards 
rather than complex regular expressions, making it incredibly handy for 
quick file-management tasks.

* :     Matches zero or more characters
? :     Matches exactly one character
[] :    Matches any character inside the brackets 
[0-9] : Matches any single digit

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

import glob
import os

# raw string r"" takes care of Windoze's screwy \ character
# all files (full path names) in a given directory
# typical windows directory
# (change to other OS formats as needed)
#directory = r"C:\Temp\*.*"
directory = "/home/admin123/Pictures/image/Dice/*.*"
print('directory = {}'.format(directory))
for path in glob.glob(directory):
    print( path )

print( '='*40 )

'''
# all files (split off file names) in a given directory
directory = "/home/admin123/Pictures/image/Dice/*.*"
print('directory = {}'.format(directory))
for path in glob.glob(directory):
    dirname, filename = os.path.split(path)
    print( filename )

print( '-'*40 )
'''

# all files (full path names) in the next level subdirectories
#subdirectories = r"C:\Temp\*\*.*"
subdirectories = "/home/admin123/Pictures/image/Dice/*/*.*"
print('subdirectories = {}'.format(directory))
for path in glob.glob(subdirectories):
    print( path )

print( '='*40 )

# only .txt files in a given directory
# split full path into dirname, filename, basename, ext
#directory_txt = r"C:\Temp\*.txt"
directory_txt = "/home/admin123/Pictures/image/Dice/*.*txt"
print('directory = {}'.format(directory))
for path in glob.glob(directory_txt):
    print( path )
    dirname, filename = os.path.split(path)
    basename, ext = os.path.splitext(filename)
    # test ...
    print( dirname, filename, basename, ext )

print( '='*40 )

# only .py file names starting with 'by' in the working directory
print('directory = {}'.format(os.getcwd()))
print('all the python files starting with by -->')
for fname in glob.glob("by*.py"):
    print( fname )

print( '='*40 )

# only .txt file names in the working directory
print('directory = {}'.format(os.getcwd()))
print('all the text files sorted -->')
# sorted, case insensitive
for fname in sorted(glob.glob("*.txt"), key=str.lower):
    print( fname )

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
