#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' f_formatted_string_print.py

use f-string instead of format()
new in Python 3.6 and higher

example:
pi = 355/133.0
the value is {:0.3f}".format(pi)
is now a simple f-string, is also faster than using format()
f"the value is {pi:0.3f}"  # use f (or F) to preced string

default is right-align
you can combine raw = r string with f string

# center (^) a string within dashes (-) (total length = 70)
print(f'{"create_line()":-^70}')
or use string method center()
print('create_line()'.center(70, '-'))

see more about f-strings:
https://pythoninoffice.com/python-f-string-formatting/

see "Formatted string literals" in the Python documentation

tested with SublimeText IDE on LinuxMint    vegaseat  15jun2026

'''

# center (^) a string within dashes (-) (total length = 60)
print(f'{"f string formatting":-^60}')

# simple examples
print("Precede the string with f or F to create an f-string")
print("and put the value directly into {}")
# approximation of pi
pi = 355/113.0
# using format()
print("pi = {:0.3f}".format(pi))
# is now
print(f"pi = {pi:0.3f}")

a = 0.1
b = 0.2
print(f"{a + b = }")       # a + b = 0.30000000000000004
# be nice
print(f"{a + b = :0.2f}")  # a + b = 0.30


num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}")
print(f"num1 = {num1} num2 = {num2}")
# even simpler
print(f"{num1 = } {num2 = }")
'''
Precede the string with f or F to create an f-string
and put the value directly into {}
pi = 3.142
pi = 3.142
The product of 83 and 9 is 747
num1 = 83 num2 = 9
num1 = 83 num2 = 9
'''

name = 'Bonefacius'
print(f"{name = }")    # name = 'Bonefacius'
# avoid default repr version
print(f"{name = !s}")  # name = Bonefacius


print(f'{"Alligment  left <  right >  center ^":-^60}')
# great for tables

print('integers:')
number = 1234567890
print(f"n = {number}")
# use 12 spaces right-align (default)
print(f"n = {number:12}")
# same, assumes decimal d
print(f"n = {number:12d}")
# fill with 0 right-align (is default)
print(f"n = {number:0>12}")
# precede with fill character _ (now left/right/center align shows)
print(f"n = {number:_>12}")
print(f"n = {number:_<12}")
print(f"n = {number:_^12}")
'''
integers:
n = 1234567890
n =   1234567890
n =   1234567890
n = 001234567890
n = __1234567890
n = 1234567890__
n = _1234567890_
'''

print('strings:')
s = "Fred Ferkel"
print(f"s = {s}")    # s = Fred Ferkel
# by default uses repr version
print(f"{s = }")     # s = 'Fred Ferkel'
# avoid repr version
print(f"{s = !s}")   # s = Fred Ferkel
# force repr() version
print(f"s = {s!r}")   # s = 'Fred Ferkel'

# use 15 spaces left-align is default (different then numbers)
print(f"s = {s:15}|")
# now right_align
print(f"s = {s:>15}")
# precede with fill character _ (now left/right/center align shows)
print(f"s = {s:_>15}")
print(f"s = {s:_<15}")
print(f"s = {s:_^15}")
# or use other fill charcters
print(f"s = {s:-^15}")
'''
strings:
s = Fred Ferkel
s = 'Fred Ferkel'
s = Fred Ferkel
s = 'Fred Ferkel'
s = Fred Ferkel    |  
s =     Fred Ferkel
s = ____Fred Ferkel
s = Fred Ferkel____
s = __Fred Ferkel__
s = --Fred Ferkel--
'''

print('floats:')
# approximation of pi
pi = 355/113.0
print(f"pi = {pi:12.3f}")
# same, right-align is default
print(f"pi = {pi:>12.3f}")
# with the fill character a left/right/center align differences show
print(f"pi = {pi:_>12.3f}")
print(f"pi = {pi:_<12.3f}")
print(f"pi = {pi:_^12.3f}")
# ten decimals and a total of 12 characters
print(f"pi = {pi:0.10f}")
'''
floats:
pi =        3.142
pi =        3.142
pi = _______3.142
pi = 3.142_______
pi = ___3.142____
pi = 3.1415929204
'''

print('percent:')
val = 0.12
print(f"percent of {val} = {val:.2%}")
'''
percent:
percent of 0.12 = 12.00%
'''

print('emoji:')
# press   windows_key + ;   to get emoji table on Windows OS
# type eg. dog = '' and put cursor between '' or ""
# select and click the dog emoji and it will appear at the cursor position
dog = '🐶'
print(f'{dog}')
# or
print(f'{dog!s}')
print(f'{dog!r}')
print(f'{dog!a}')
'''
emoji:
🐶
🐶
'🐶'
'\U0001f436'
'''
# use unicode of dog
print('\U0001f436')  # 🐶

# several emoji characters
# set cursor between quote characters, press windows button + semicolon
# search for beer and click the emoji three times
three_beer = "🍺🍺🍺"

print(f'{three_beer}')    # 🍺🍺🍺
print(f'{three_beer!a}')  # '\U0001f37a\U0001f37a\U0001f37a'
# print just one beer
print('\U0001f37a')       # 🍺

print('integer bin hex:')
n = 127825
# binary
print(f'{n:b}')
print(f'{n:#b}')
print(f'{n:#_b}')
# hexadecimal
print(f'{n:x}')
print(f'{n:#x}')
print(f'{n:#X}')
# emoji with unicode value n
print(f'{n:c}')

'''
integer bin hex:
11111001101010001
0b11111001101010001
0b1_1111_0011_0101_0001
1f351
0x1f351
0X1F351
🍑
'''

print(f'{"Number separators":-^60}')

large_number1 = 1000000000
# easier to read (but for Python the same as above)
large_number2 = 1_000_000_000
print(large_number1)
print(large_number2)
# format with thousand specifier comma
print('large_number = {:,}'.format(large_number1))
print('large_number = {:_}'.format(large_number1))

# comma
print(f"${44000000000:,}")    # $44,000,000,000
print(f"${44000000000:,.2f}") # $44,000,000,000.00
# underline allowed in Python
print(f"${44000000000:_.2f}") # $44_000_000_000.00 
print(f"{1e9:_}")             # 1_000_000_000.0   1e9 is a float!

'''
1000000000
1000000000
large_number = 1,000,000,000
large_number = 1_000_000_000
$44,000,000,000
$44,000,000,000.00
$44_000_000_000.00
'''
small_number1 = 0.0000001
# easier to read (but for Python the same as above)
small_number2 = 0.000_000_1
# scientific notation 1e+6 = 1 million (a 1 with 6 zeroes)
print(small_number2)         # 1e-07
print(f"{small_number2}")    # 1e-07
print(f"{large_number1:e}")  # 1.000000e+09
print(f"{large_number1:E}")  # 1.000000E+09
print(f"{small_number1:e}")  # 1.000000e-07


print(f'{"datetime formats for now()":-^60}')

import datetime as dt

dt_info = '''\
using eg. f'{now:%m/%d/%y}'
where:
%m  Month as a decimal number [01,12]
%d  Day of the month as a decimal number [01,31]
%y  Year without century as a decimal number [00,99]
%Y  Year with century as a decimal number
%a  Locale's abbreviated weekday name
%b  Locale's abbreviated month name
%H  Hour (24-hour clock) as a decimal number [00,23]
%M  Minute as a decimal number [00,59]
%S  Second as a decimal number [00,61]. Yes, 61 !
'''

now = dt.datetime.now()
print(now)  # eg. 2023-12-17 23:12:47.981966

#using f formatted strings (new in Python3.6)
print(f'{now:%m/%d/%y}')     # 12/17/23
print(f'{now:%a %d%b%Y}')    # Sun 17Dec2023
print(f"{now:%d%b%Y}")       # 17Dec2023
print(f'{now:%H:%M:%S}')     # 23:12:47
# include milliseconds
print(f'{now:%H:%M:%S.%f}')  # 23:12:47.160290
''' for instance
2023-12-17 23:12:47.981966
12/17/23
Sun 17Dec2023
17Dec2023
23:12:47
23:12:47.160290
'''

print('-'*22)
# shortcuts
print(f'{now:%D}') # 12/18/23
print(f'{now:%T}') # 18:48:33
print(f'{now:%A}') # Monday
print(f'{now:%B}') # December

# putting the date specifier into a string
date_spec = '%a %d%b%Y'
print(f'{now:{date_spec}}')  # Sun 17Dec2023
