#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' RomanNumeral.py

Convert a decimal (denary number) to roman numeral function

tested with Spyder IDE on LinuxMint  vegaseat (vegas-eat) 29jul2026
'''

def int2roman(number):
    '''convert a denary number to roman numerals'''
    numerals = {
    1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
    90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
    }
    result=""
    for value, numeral in sorted(numerals.items(), reverse=True):
        #print(value, numeral)  # for testing
        while number >= value:
            result += numeral
            number -= value
            #print(result, value)  # for testing only
    return result

# test ...
num = 14
print("{} --> {}".format(num, int2roman(num)))
num = 140
print("{} --> {}".format(num, int2roman(num)))
num = 1941
print("{} --> {}".format(num, int2roman(num)))
num = 2026
print("{} --> {}".format(num, int2roman(num)))

''' result...
14 --> XIV
140 --> CXL
1941 --> MCMXLI
2026 --> MMXXVI
'''
