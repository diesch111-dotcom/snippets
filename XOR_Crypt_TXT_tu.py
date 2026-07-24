#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' XOR_Crypt_TXT_tu.py

I usually end up with quite a number of TXT files that contain financial
data that some privacy invaders could abuse.  So I have been using this
relatively short Python program that I put into a sub_folder created for
just those .txt files I want to protect with encryption.  Run the program
once to encrypt, later run it again to decrypt, short and sweet!

xor encrypt/decrypt all txt/txtz data files in a given directory.

creates proper extension .txt or .txtz
listed .txt files will be encrypted to .txtz files
listed .txtz files will be decrypted to .txt files

Now send off the encrypted .txtz file or files and this little program
Keep the originals in a safe place!!

Uses turtle textinput() for the password input that the Sublime Text IDE 
can handle.

For initial testing create a subfolder with a number of test .txt data files
(make sure you have backups of these files until you got the hang of it)

I recommend a password consisting of your First Friend's name followed by
his or her Birth Year; the hint given would be FFBY.
So let's say your friend's name is Carl May born in 1987 then the password
is CarlMay1987.

I hope your first best friend was not the famous Bonefacius Kiesewetter.
(a lot of typimg here)

tested using the Spyder or Sublime Text IDE   dns aka vegaseat  13jul2026
'''

import operator
import glob
import os
#import pprint


def file_exists(filename):
    '''check if a file exists'''
    try:
        with open(filename): return True
    except:
        return False

def create_outfile(filename):
    if filename.endswith('.txt'):
        return filename[:-4] + '.txtz'
    elif filename.endswith('.txtz'):
        return filename[:-5] + '.txt'

def txt_to_txtz(list_txt, password):
    sf = "Encrypting all {} .txt files to .txtz files"
    print(sf.format(len(list_txt)))    
    for fname in list_txt:
        with open(fname, "rb") as fin:
            text = fin.read()
        # Python2 uses str and Python3 uses bytes
        if isinstance(text, bytes):
            # Python3 stuff
            text = text.decode('latin')
        x_text = xor_crypt2(text, password)
        fname_out = create_outfile(fname)
        # .txtz has been written, remove .txt file
        os.remove(fname)
        
        #print(fname, fname_out)  # test
        with open(fname_out, "wb") as fout:
            try:
                fout.write(x_text)
            except TypeError:
                # Python3 stuff
                fout.write(x_text.encode('latin'))
    #print('='*40)
    print("\nAll .txt files in directory deleted")
    print('='*40)
    for path in glob.glob("*.txtz"):
        dirname, filename = os.path.split(path)
        print(filename)
    print('='*40)

def txtz_to_txt(list_txtz, password):
    sf = "Encrypting all {} .txtz files to .txt files"
    print(sf.format(len(list_txtz)))
    for fname in list_txtz:
        with open(fname, "rb") as fin:
            x_text = fin.read()
        # Python2 uses str and Python3 uses bytes
        if isinstance(x_text, bytes):
            # Python3 stuff
            x_text = x_text.decode('latin')
        text = xor_crypt2(x_text, password)
        fname_out = create_outfile(fname)
        # .txt has been written, remove .txtz file
        os.remove(fname)

        #print(fname, fname_out)  # test
        with open(fname_out, "wb") as fout:
            try:
                fout.write(text)
            except TypeError:
                # Python3 stuff
                fout.write(text.encode('latin'))
    #print('='*40)
    print("\nAll .txtz files in directory deleted")
    print('='*40)
    for path in glob.glob("*.txt"):
        dirname, filename = os.path.split(path)
        print(filename)
    print('='*40)

def xor_crypt2(text, password):
    '''
    xor crypt using list container 
    '''
    xlist = []
    n = 0
    k = 0
    offset = 0
    for c in text:
        # loop through password start to end and repeat
        if n >= len(password) - 1:
            n = 0
        pw = ord(password[n])
        n += 1
        bt = ord(c)
        # xor byte with password byte
        xbt = operator.xor(bt, pw)
        if k < offset:
            # do not xor header
            xlist.append(chr(bt))
        else:
            # convert to character and append to xlist
            xlist.append(chr(xbt))
        k += 1
    # convert xlist to string and return
    text_out = ''.join(xlist)
    return text_out


# pick a directory with a number of .txt data files for testing
# make sure you have backups of these files just in case
directory = os.getcwd()
# make it the working directory
os.chdir(directory)
print("Working in directory {}".format(directory))
print("This might take a  moment ...")

# pick a password you like (don't forget it!)
import turtle as tu
# keeps the turtle canvas/screen small, popup covers it
tu.Screen().setup(15, 15)
# string input
password = tu.textinput("Password", "Password (hint: FFBY): ")

# create a list of all .txt files in a given directory
list_txt = []
for path in glob.glob("*.txt"):
    dirname, filename = os.path.split(path)
    list_txt.append(filename)

# create a list of all .txtz files in a given directory
list_txtz = []
for path in glob.glob("*.txtz"):
    dirname, filename = os.path.split(path)
    list_txtz.append(filename)

if list_txt:
    txt_to_txtz(list_txt, password)

if list_txtz:
    txtz_to_txt(list_txtz, password)
