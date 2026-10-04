#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' slicing2.py

simple rule...
slicing uses [start:<end:step]
'start' defaults to 0, 'end' to len(sequence), 'step' to 1

VegasEat  03oct2026
'''

s4 = "hippopotamus"

print( "first 2 char = ", s4[0:2] )
print( "next 2 char  = ", s4[2:4] )
print( "last 2 char  = ", s4[-2:] )
print( "exclude first 3 char  = ", s4[3: ] )
print( "exclude last 4 char   = ", s4[:-4] )
print( "reverse the string    = ", s4[::-1] ) # step is -1
print( "the whole word again  = ", s4 )       # no change to original
print( "spell skipping 2 char = ", s4[::2] )  # step is 2

""" result...
first 2 char =  hi
next 2 char  =  pp
last 2 char  =  us
exclude first 3 char  =  popotamus
exclude last 4 char   =  hippopot
reverse the string    =  sumatopoppih
the whole word again  =  hippopotamus
spell skipping 2 char =  hpooau
"""

# insert 'ter' 4 places from the end
s5 = s4[:-4] + 'ter' + s4[-4:]
print(s5)  # hippopotteramus, a new animal species?
