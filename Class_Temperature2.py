#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' class_Temperature2.py

A class to convert F to C or C to F using property(),
property() combines get and set methods into one call.


tested using Linux and Spyder IDE  vegaseat  17jul2026
'''

class Temperature:
    """
    allows you to convert F to C  or  C to F
    double underline (dunter) prefix makes method private to class
    """
    def __init__(self):
        self.celsius = 0.0
    def __getFahrenheit(self):
        return 32 + (1.8 * self.celsius)
    def __setFahrenheit(self, f):
        self.celsius = (f - 32) / 1.8
    # property() combines get and set methods into one call
    # celsius and fahrenheit define each other
    # only one is needed to be given
    fahrenheit = property(__getFahrenheit, __setFahrenheit)


# create the class instance
tci = Temperature()

# convert Celcius to Fahrenheit
tci.celsius = 0
print("%0.1f C = %0.1f F" % (tci.celsius, tci.fahrenheit))

# convert Fahrenheit to Celsius
tci.fahrenheit = 98
print("%0.1f F = %0.1f C" % (tci.fahrenheit, tci.celsius))

''' result ...
0.0 C = 32.0 F
98.0 F = 36.7 C
'''

# more testing ...
print('='*30)
# convert Celcius to Fahrenheit
tci.celsius = 10
print("%0.1f C = %0.1f F" % (tci.celsius, tci.fahrenheit))
print("{:0.1f} C = {:0.1f} F".format(tci.celsius, tci.fahrenheit))

# convert Fahrenheit to Celsius
tci.fahrenheit = 10
print("{:0.1f} F = {:0.1f} C".format(tci.fahrenheit, tci.celsius))

# convert Celcius to Fahrenheit
tci.celsius = -12.2
print("{:0.1f} C = {:0.1f} F".format(tci.celsius, tci.fahrenheit))

''' result ...
10.0 C = 50.0 F
10.0 F = -12.2 C
-12.2 C = 10.0 F
'''
