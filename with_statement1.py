#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' with_statement1.py

Writing and reading files using the 'with' context manager

# UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 10908
# to fix this use "utf-8" encoding (is the default in Linux and MacOs)
with open(filename, encoding="utf-8") as fin:
    dt_text = fin.read()

you can also try (hint from MS Copilot), add this anyway!
file = open(filename, errors="ignore") as fin:

another way is to use rb --> read binary
file = open(filename, rb) as fin:

converted_file = binary_file.decode('utf-8') 

import os
# stop this file from being appened, 'wa' is now 'a'
fname = "/home/dietrich/Pictures/crop_coordinates.txt"
if os.path.exists(fname):
    os.remove(fname)

Corey Schafer video
https://youtu.be/Uh2ebFW8OYM?si=u5tM3Q_g2SUV7yJF

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import locale
# get current encoding if you have decode errors
print(locale.getpreferredencoding(False))  # eg. cp1252

fname = "CanadaSong.txt"

data = """\
First come the black flies,
Then the Horse flies,
Then the Deer flies,
Then the snow flies!
"""

# 'with' will close the file handle properly
# "w" will create a new file if it does not exist
# otherwise it will overwrite the existing file
# "a" will append to an existing file
with open(fname, "w") as fout:
    fout.write(data)

print("{} has been written".format(fname))

print('-'*40)

# "r" and read() gives a string of the existing file data
with open(fname, "r") as fin:
    text = fin.read()

print(text)
'''
First come the black flies,
Then the Horse flies,
Then the Deer flies,
Then the snow flies!
'''

print('-'*40)

# read only a specified chunk
# if read(chunk) exceeds the file, an empty string will result
chunk = 13
with open(fname, "r") as fin:
    text1 = fin.read(chunk)
    #read the next chunk
    text2 = fin.read(chunk)
    file_position = fin.tell()

print(text1)
print(text2)
print("you are now at file position {}".format(file_position))
'''
First come th
e black flies
you are now at file position 26
'''

print('-'*40)

# read from a specified position within the file
with open(fname, "r") as fin:
    fin.seek(29)
    text3 = fin.read(20)

print(text3)
'''
Then the Horse flies
'''

print('-'*40)


# note that readlines() gives a list of the file data lines with the newliine
# characteer still attached
with open(fname, "r") as fin:
    print(fin.readlines())

'''
['First come the black flies,\n', 'Then the Horse flies,\n',
'Then the Deer flies,\n', 'Then the snow flies!\n']
'''

print('-'*40)

# to limit the memory requirements read only one line at a time
# also allows you to process each line
with open(fname, "r") as fin:
    for line in fin:
        print(line, end='')

print()
print('-'*40)

# reading and writing a file, making a copy
# to copy a picture file use "rb" and "wb" binary modes
fname_in = "CanadaSong.txt"
fname_copy = "CanadaSong_copy.txt"

with open(fname_in, "r") as fin:
    # will create a new file if it does not exist
    # otherwise it will overwrite the existing file
    with open(fname_copy, "w") as fout:
        content = fin.read()
        fout.write(content)

print("{} has been written".format(fname_copy))

# for large files read and write in chunks (eg. 1k chunks)
chunk = 1024
filename_in = "/home/admin123/Pictures/image/jpg/Beach07.jpg"
filename_copy = "/home/admin123/Pictures/image/jpg/Beach07_copy.jpg" 
with open(filename_in, "rb") as fin:
    # will create a new file if it does not exist
    # otherwise it will overwrite the existing file
    with open(filename_copy, "wb") as fout:
        fin_chunk = fin.read(chunk)
        while len(fin_chunk) > 0:
            fout.write(fin_chunk)
            # next chunk until len = 0
            fin_chunk = fin.read(chunk)

print("{} has been written".format(filename_copy))
