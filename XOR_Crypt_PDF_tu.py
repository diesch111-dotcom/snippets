#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' XOR_Crypt_PDF_tu.py

I usually end up with quite a number of PDF files that contain financial
data that some privacy invaders could abuse.  So I have been using this
relatively short Python program that I put into a sub_folder created for
just those .pdf files I want to protect with encryption.  Run the program
once to encrypt, later run it again to decrypt, short and sweet!

xor encrypt/decrypt all pdf/pdfz data files in a given directory.

creates proper extension .pdf or .pdfz
listed .pdf files will be encrypted to .pdfz files
listed .pdfz files will be decrypted to .pdf files
the original files will be deleted

Uses turtle textinput() for the password input that the Sublime Text IDE 
can handle.

For initial testing create a subfolder with a number of test .pdf data files
(make sure you have backups of these files until you got the hang of it)

I recommend a password consisting of your First Friend's name followed by
his or her Birth Year; the hint given would be FFBY.
So let's say your friend's name is Carl May born in 1987 then the password
is CarlMay1987.

I hope your first best friend was not the famous Bonefacius Kiesewetter. 

tested using the Spyder IDE on Linux  dns aka vegaseat  9jul2026
'''

import operator
import glob
import os
import pprint


def create_outfile(filename):
    if filename.endswith('.pdf') or filename.endswith('.PDF'):
        return filename[:-4] + '.pdfz'
    elif filename.endswith('.pdfz'):
        return filename[:-5] + '.pdf'

def pdf_to_pdfz(list_pdf, password):
    sf = "Encrypting all {} .pdf files to .pdfz files"
    print(sf.format(len(list_pdf)))    
    for fname in list_pdf:
        with open(fname, "rb") as fin:
            text = fin.read()
        # Python2 uses str and Python3 uses bytes
        if isinstance(text, bytes):
            # Python3 stuff
            text = text.decode('latin')
        x_text = xor_crypt2(text, password)
        fname_out = create_outfile(fname)
        #print(fname, fname_out)  # test
        with open(fname_out, "wb") as fout:
            try:
                fout.write(x_text)
            except TypeError:
                # Python3 stuff
                fout.write(x_text.encode('latin'))
        # .pdfz has been written, remove .pdf file
        os.remove(fname)
    print("\nAll .pdf files in directory deleted")
    print('='*40)
    for path in glob.glob("*.pdfz"):
        dirname, filename = os.path.split(path)
        print(filename)
    print('='*40)

def pdfz_to_pdf(list_pdfz, password):
    sf = "Encrypting all {} .pdfz files to .pdf files"
    print(sf.format(len(list_pdfz)))
    for fname in list_pdfz:
        with open(fname, "rb") as fin:
            x_text = fin.read()
        # Python2 uses str and Python3 uses bytes
        if isinstance(x_text, bytes):
            # Python3 stuff
            x_text = x_text.decode('latin')
        text = xor_crypt2(x_text, password)
        fname_out = create_outfile(fname)
        #print(fname, fname_out)  # test
        with open(fname_out, "wb") as fout:
            try:
                fout.write(text)
            except TypeError:
                # Python3 stuff
                fout.write(text.encode('latin'))
        # .pdf has been written, remove .pdfz file
        os.remove(fname)
    print("\nAll .pdfz files in directory deleted")
    print('='*40)
    for path in glob.glob("*.pdf"):
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
    offset = 0  # ignore jpg header (usually ca. 180 bytes)
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


# pick a directory with a number of .pdf data files for testing
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

# create a list of all .pdf files in a given directory
list_pdf = []
for path in glob.glob("*.pdf"):
    dirname, filename = os.path.split(path)
    list_pdf.append(filename)

if list_pdf:
    print('='*40)
    pprint.pprint(list_pdf)  # test
    print('='*40)

# create a list of all .pdfz files in a given directory
list_pdfz = []
for path in glob.glob("*.pdfz"):
    dirname, filename = os.path.split(path)
    list_pdfz.append(filename)

if list_pdfz:
    print('='*40)
    pprint.pprint(list_pdfz)  # test
    print('='*40)

if list_pdf:
    pdf_to_pdfz(list_pdf, password)

if list_pdfz:
    pdfz_to_pdf(list_pdfz, password)
