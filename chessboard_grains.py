#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' chessboard_grains.py

A classical Indian story:
Putting one grain of rice on the first square of a chess board
and doubling it every square, this is what the inventor of the chess 
game asked his 'leader', who wanted to give him a reward.
A simple request, until you do the math!

tested with VSCodium IDE on LinuxMint  VegasEat 29aug2026
'''

grains_sum = 0
grains = 1
for square in range(1, 64+1):
    grains = 2**(square-1)
    grains_sum = (2**square) - 1
    # test print to show we are are on the right track
    #print(f"square {square}  grains = {grains}  total = {grains_sum:_}")

print(f"{grains_sum:_} grains of rice")

# assume 7000 grains per pound of the rice
rice_pounds = grains_sum//7000
print(f"{rice_pounds:_} pounds of required rice")

''' result...
18_446_744_073_709_551_615 grains of rice
2_635_249_153_387_078 pounds of required rice
'''

# more...
print('-'*60)
ww_tonnes = 678_688_289
print(f"Worldwide Rice Production in 2009: {ww_tonnes:_} tonnes")
ww_pounds = ww_tonnes * 2000
print(f"or {ww_pounds:_} pounds")
print(f"The required {rice_pounds:_} pounds would consume")
ww_productions = int(rice_pounds / ww_pounds)
print(f"{ww_productions:,d} world productions.")

''' result...
Worldwide Rice Production in 2009: 678_688_289 tonnes
or 1_357_376_578_000 pounds
The required 2_635_249_153_387_078 pounds would consume
1,941 world productions.
'''
