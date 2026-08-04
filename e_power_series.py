#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' e_power_series.py

// C code for...
// power series dev using a loop
// value of e = 2.71828182846 
 
#include <stdio.h>
 
int main()
{
    int n, f;
    float x;
    float e;
 
    x = 1.0;
    f = 1;
    e = 0.0;
    //e = 1+x/1!+x2/2!+x3/3!+x4/4! ...
    //e = 1 + x * x*2.0/2 + x*3.0/(2*3) + x*4.0/(2*3*4) ...
    for ( n = 1; n < 11; n++ ) {
        f *= n;  // factorial, don't exceed 12!
        e += x*n/f;
        printf( "%f  %d  %d\n", e, n, f);
    }

    getchar(); // wait
    return 0;
}

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

# power series for Euler's number (base of natural logs)
# e = 1 + x * x*2.0/2 + x*3.0/(2*3) + x*4.0/(2*3*4) ...

x = 1.0
f = 1
qe = 0.0
for n in range(1, 17):
    f *= n
    qe += x*n/f
    #print(qe, n, f)  # test

print("power series e = %0.12f" % qe)
# compare ...
import math
print("Python  math.e = %0.12f" % math.e)

''' result...
power series e = 2.718281828459
Python  math.e = 2.718281828459
'''