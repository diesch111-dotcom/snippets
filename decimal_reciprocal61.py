#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' decimal_reciprocal61.py

For the folks who like to play with numbers!
The number 61 has a reciprocal of 1/61
with a period of 60 (repeats every 60 characters)
Every digit appears 6 times in each period

tested with SublimeText IDE on LinuxMint    vegaseat  15jun2026
'''

from decimal import *

getcontext().prec = 120

reciprocal61 = Decimal('1.0')/Decimal('61.0')
print("I put in the underline character to show the break:")
# take the '0.'into account to show the period of 60
print('-'*62)
print(reciprocal61)
print('-'*60)

print("the first repeating period of 60:")
# slice off the first 2 characters = '0.'
print(str(reciprocal61)[2:62])
print("the second repeating period of 60:")
# the next period
print(str(reciprocal61)[62:122])


'''
I put in the underline character to show the break:
--------------------------------------------------------------
0.016393442622950819672131147540983606557377049180327868852459_
0163934426229508196721311475409836065573770491803278688524590
------------------------------------------------------------
the first repeating period of 60:
016393442622950819672131147540983606557377049180327868852459
the second repeating period of 60:
016393442622950819672131147540983606557377049180327868852459
'''