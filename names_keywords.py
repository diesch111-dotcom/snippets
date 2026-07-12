#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" names_keywords.py

Show all builtin Python keywords;
avoid using any of those names for your variables, or
you will get conflicts, usually get an error flag!

sounds poetic:
    When in doubt,
    print it out!

tested using the Spyder IDE on Linux  dns(vegaseat)  4jul2026
"""

from keyword import kwlist

print("A list of Python's keywords:")
print('\n'.join(kwlist))

print('='*60)

'''
A list of Python's keywords:
False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
'''

# testing...
#raise = 'Yes!'  # SyntaxError: invalid syntax
#print(raise)    # SyntaxError: invalid syntax
