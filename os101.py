#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" os101.py
Managing folders is one of the most common uses for the os module.
(folder is the same as directory)

Don't use keyword 'os' for a variable name!

Get current working directory: os.getcwd() (terminel pwd)
Change directory: os.chdir('path/to/dir') (terminel cd)
List contents: os.listdir('.') (terminel ls or dir)
Create a directory: os.mkdir('new_folder')
Remove a directory: os.rmdir('folder_name') (only works if empty)
Rename a file/folder: os.rename('old.txt', 'new.txt')
Delete a file: os.remove('file.txt') (terminal os.unlink())
Check if it exists: os.path.exists('file.txt')

Join paths safely: os.path.join('folder', 'subfolder', 'file.txt')
Get absolute path: os.path.abspath('relative/path')
Extract file name: os.path.basename('/path/to/file.txt') # Returns 'file.txt'
Extract directory: os.path.dirname('/path/to/file.txt')  # Returns '/path/to'
Split extension: os.path.splitext('image.png')  # Returns ('image', '.png')
Check type: os.path.isfile('path') or os.path.isdir('path')

Get an environment variable: os.environ.get('API_KEY')
Set an environment variable: os.environ['DEBUG'] = 'True'
Get logged-in user: os.getlogin()
Get OS name: os.name (returns 'posix' for Mac/Linux, 'nt' for Windows)

If you need to find every file inside a folder and all of its subfolders, 
os.walk() yields a 3-tuple (dirpath, dirnames, filenames) for every 
directory it visits.

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""

import os

# get the current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

''' possible result...

'''

# line 0f 40 '=' char
print("="*40)

# create a list of everything in the current directory
# sort in alphabetical order
file_list = sorted(os.listdir('.'))
print("first 5 files:")
for item in file_list[0:5]:
    print(item)

''' possible result...
first 5 files:
Cal_1220.html
GradeLetter1.py
Grades_bisect1.py
HTMLcalendar1.py
HelloWorld_fun101.py
'''

print("="*40)

# Cross-platform path joining (safe for Win, Linux, OS X)
# os.path.join('folder', 'subfolder', 'file.txt')
safe_path = os.path.join("assets", "images", "logo.png")
print(safe_path) 
# only the filenam
print(os.path.basename(safe_path))
# only the directory (or folder) name
print(os.path.dirname(safe_path))

'''
assets/images/logo.png
logo.png
assets/images
'''

print("="*40)

# 'posix' for Mac/Linux, 'nt' for Windows
print("operating system =", os.name)

print("="*40)
            
# display bytes used in each directory
# '..' is the top directory           
from os.path import join, getsize
for root, dirs, files in os.walk('..'):
    print(root, "consumes ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories

'''
.. consumes 
21724 bytes in 13 non-directory files
../aatest_gz consumes 
1012611 bytes in 445 non-directory files
../sound consumes 
13523424 bytes in 98 non-directory files
../sound/tk consumes 
839804 bytes in 100 non-directory files
../sound/tk/aaTurtle consumes 
189733 bytes in 60 non-directory files
../99 consumes 
1691 bytes in 4 non-directory files
../data consumes 
1667461 bytes in 93 non-directory files
../data/quotes consumes 
219504 bytes in 114 non-directory files
../data/TestDirectory2 consumes 
26 bytes in 1 non-directory files
../data/USPostalCodes consumes 
2664099 bytes in 1 non-directory files
../data/TestDirectory1 consumes 
26 bytes in 1 non-directory files
../data/quotes2023 consumes 
720912 bytes in 250 non-directory files
../data/quotes2025 consumes 
474538 bytes in 248 non-directory files
../data/quotes2024 consumes 
476701 bytes in 251 non-directory files
../data/quotes2022 consumes 
367099 bytes in 214 non-directory files
../MatPlot consumes 
2285986 bytes in 115 non-directory files
...

'''


#help(os.walk)




