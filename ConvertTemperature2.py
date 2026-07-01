''' ConvertTemperature2.py
convert temperatures Celsius/Fahrenheit


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

# ----------------------------------------------
# add these few lines near the start of your code
import sys
# make string input work with Python2 or Python3
if sys.version_info[0] < 3:
    input = raw_input
# ----------------------------------------------


def f2c( fahrenheit ):
    """convert Fahrenheit to Celsius"""
    return ( fahrenheit - 32 ) * 5.0 / 9.0

def c2f( celsius ):
    """convert Celsius to Fahrenheit"""
    return 9.0 / 5.0 * celsius + 32

def main(info):
    print( info )
    while True:
        t = str(input( "Enter the temperature (eg. 50C, q to exit): " )).lower()
        if 'q' in t:
            break
        if 'f' in t:
            # remove last char, convert to number
            num = float(t[:-1])
            celsius = f2c(num)
            print( "%0.1f F = %0.1f C" % (num, celsius) )
        elif 'c' in t:
            # remove last char, convert to number
            num = float(t[:-1])
            fahrenheit = c2f(num)
            print( "%0.1f C = %0.1f F" % (num, fahrenheit) )


info = """\
Enter the temperature with the unit of measurement,
for instance ...
100F will give the temperature in Celsius
100C will give the temperature in Fahrenheit
(enter just q to quit the program)
"""

main(info)
