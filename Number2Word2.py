#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Number2Word2.py

Integer number to english word conversion
Can be used for numbers as large as 999 vigintillion 
(a vigintillion is 10 to the power 60)

# SI prefixes (sometimes useful)
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deka = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

def int2word(n):
    """
    takes an integer number n and converts it into 
    a string of english words, returns the string
    """
    if n == 0:
        return "zero "
    # make sure n is a positive integer
    n = int(abs(n))

    # break the number into groups of 3 digits using slicing
    # each group representing hundred, thousand, million, billion, ...
    n3_list = []
    # create numeric string
    ns = str(n)
    for k in range(3, 66, 3):
        r = ns[-k:]
        q = len(ns) - k
        # break if end of ns has been reached
        if q < -2:
            break
        else:
            if  q >= 0:
                n3_list.append(int(r[:3]))
            elif q >= -1:
                n3_list.append(int(r[:2]))
            elif q >= -2:
                n3_list.append(int(r[:1]))

    # the lists of number words ...
    ones_list = ["", "one ","two ","three ","four ", "five ",
        "six ","seven ","eight ","nine "]

    tens_list = ["ten ","eleven ","twelve ","thirteen ", "fourteen ",
        "fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]

    twenties_list = ["","","twenty ","thirty ","forty ",
        "fifty ","sixty ","seventy ","eighty ","ninety "]

    thousands_list = ["","thousand ","million ", "billion ", 
        "trillion ", "quadrillion ", "quintillion ", "sextillion ", 
        "septillion ", "octillion ", "nonillion ", "decillion ", 
        "undecillion ", "duodecillion ", "tredecillion ", 
        "quattuordecillion ", "sexdecillion ", "septendecillion ", 
        "octodecillion ", "novemdecillion ", "vigintillion "]
        
    # form a string of words
    n2w = ""
    for i, x in enumerate(n3_list):
        # break each group of 3 digits into
        # ones_list, tens_list/twenties_list, hundreds
        hun = x % 10
        ten = (x % 100)//10
        one = (x % 1000)//100
        if x == 0:
            continue  # skip
        else:
            t = thousands_list[i]
        if ten == 0:
            n2w = ones_list[hun] + t + n2w
        elif ten == 1:
            n2w = tens_list[hun] + t + n2w
        elif ten > 1:
            n2w = twenties_list[ten] + ones_list[hun] + t + n2w
        if one > 0:
            n2w = ones_list[one] + "hundred " + n2w
    return n2w


# testing ...
if __name__ == '__main__':
    n = 1
    print(n)
    print( int2word(n) )
    print("-"*50)
    n = 1999
    print(n)
    print( int2word(n) )
    print("-"*50)
    n = 12345678
    print(n)
    print( int2word(n) )
    print("-"*50)
    n = 4321234567890
    print(n)
    print( int2word(n) )
    print("-"*50)
    # grains of rice on the chessboard problem
    n = 5270498306774157
    print(n)
    print( int2word(n) )    

""" result...
1
one 
--------------------------------------------------
1999
one thousand nine hundred ninety nine 
--------------------------------------------------
12345678
twelve million three hundred forty five thousand six hundred seventy eight 
--------------------------------------------------
4321234567890
four trillion three hundred twenty one billion two hundred thirty four 
million five hundred sixty seven thousand eight hundred ninety
--------------------------------------------------
5270498306774157
five quadrillion two hundred seventy trillion four hundred ninety eight 
billion three hundred six million seven hundred seventy four thousand one 
hundred fifty seven 
"""
