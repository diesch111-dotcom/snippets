#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' textwrap.py

Use module tetxwrap so text does not exceed
a set number of characters per line

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import textwrap

# mimics as 2 very long lines separated by a blank line
text = """Arthur:  "The Lady of the Lake, her arm clad in the purest
shimmering samite, held aloft Excalibur from the bosom of the water,
signifying by Divine Providence that I, Arthur, was to carry
Excalibur. That is why I am your king!"

Smarty:  "Listen. Strange women lying in ponds distributing swords is
no basis for a system of government. Supreme executive power derives
from a mandate from the masses, not from some farcical aquatic
ceremony!\""""

# make a text string fit in 40 columns using textwrap
# the generator expression keeps the paragraphs separated to preserve
# any blank lines, one \n from end of line and one \n from empty line
p = "\n\n"
print(p.join(textwrap.fill(elem, 40) for elem in text.split(p)))

print('-'*40)
print('-'*40)

# this simpler option would ignore any blank lines
print(textwrap.fill(text, 40))

""" result...
Arthur:  "The Lady of the Lake, her arm
clad in the purest shimmering samite,
held aloft Excalibur from the bosom of
the water, signifying by Divine
Providence that I, Arthur, was to carry
Excalibur. That is why I am your king!"

Smarty:  "Listen. Strange women lying in
ponds distributing swords is no basis
for a system of government. Supreme
executive power derives from a mandate
from the masses, not from some farcical
aquatic ceremony!"
----------------------------------------
----------------------------------------
Arthur:  "The Lady of the Lake, her arm
clad in the purest shimmering samite,
held aloft Excalibur from the bosom of
the water, signifying by Divine
Providence that I, Arthur, was to carry
Excalibur. That is why I am your king!"
Smarty:  "Listen. Strange women lying in
ponds distributing swords is no basis
for a system of government. Supreme
executive power derives from a mandate
from the masses, not from some farcical
aquatic ceremony!"

"""