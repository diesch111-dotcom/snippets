#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' difflib2.py

Use Python module difflib to find the line by
line differences between two texts

line markers ...
'- ' line unique to sequence 1
'+ ' line unique to sequence 2
' '  line common to both sequences
'? ' line not present in either input sequence
     used to point out character differences in lines
     + word has extra char,
     ^ spelling,
     - word has missing char
     
vegaseat  27oct2026
'''

import difflib

text1 = """The World's Shortest Books:
Humen Rights Advances in Burma
"My Plan to Find the Real Killers" by OJ Simpson
"Strom Thurmond:  Intelligent Quotes"
America's Most Popular Lawyers
Career Opportunities for History Majors
Different Ways to Spell "Tom"
Dr. Kevorkian's Collection of Motivational Speeches
Spotted Owl Recipes by the EPA
The Engineer's Guide to Fashion
Ralph Nader's List of Pleasures
Lindsey Graham Peace Deals
"""

text2 = """The World's Shortest Books:
Human Rights Advance in Burma
"My Plan to Find the Real Killer" by OJ Simpson
"Strom Thurmond:  Intlegigent Quotes"
America's Most Poppular Lawyers
Career Opportunities for History Majors
Different Ways to Sell "Tom"
Dr. Kevorkian's Collection of Motivational Speeches
Spotted Owl Recipes by the EPA
The Engineer's Guide to Passion
Ralph Nader's Lust of Pleasures
Lindsey Graham Deace Peals
"""

# create a list of lines in text1
text1_lines = text1.splitlines(True)

# dito for text2
text2_lines = text2.splitlines(True)

diff_instance = difflib.Differ()
diff_list = list(diff_instance.compare(text1_lines, text2_lines))

print("Lines in diff_list showing the markers:")
for line in diff_list:
    line = line.rstrip()
    print(line)
print('')

# lines common to text1 and text2
common = ""
for line in diff_list:
  if line[0] == ' ':
    common += line[2:]

# lines unique to text1
unique1 = ""
for line in diff_list:
  if line[0] == '-':
    unique1 += line[2:]

# lines unique to text2
unique2 = ""
for line in diff_list:
  if line[0] == '+':
    unique2 += line[2:]

print('-'*50)

print("Lines common to text1 and text2:")
print(common)
print('-'*50)
print("Lines unique to text1:")
print(unique1)
print('-'*50)
print("Lines unique to text2:")
print(unique2)

""" result...
Lines in diff_list showing the markers:
  The World's Shortest Books:
- Humen Rights Advances in Burma
?    ^                -
+ Human Rights Advance in Burma
?    ^
- "My Plan to Find the Real Killers" by OJ Simpson
?                                 -
+ "My Plan to Find the Real Killer" by OJ Simpson
- "Strom Thurmond:  Intelligent Quotes"
?                       ^^
+ "Strom Thurmond:  Intlegigent Quotes"
?                      + ^
- America's Most Popular Lawyers
+ America's Most Poppular Lawyers
?                   +
  Career Opportunities for History Majors
- Different Ways to Spell "Tom"
?                    -
+ Different Ways to Sell "Tom"
  Dr. Kevorkian's Collection of Motivational Speeches
  Spotted Owl Recipes by the EPA
- The Engineer's Guide to Fashion
?                         ^  ^
+ The Engineer's Guide to Passion
?                         ^  ^
- Ralph Nader's List of Pleasures
?                ^
+ Ralph Nader's Lust of Pleasures
?                ^
- Lindsey Graham Peace Deals
?                ^     ^
+ Lindsey Graham Deace Peals
?                ^     ^

--------------------------------------------------
Lines common to text1 and text2:
The World's Shortest Books:
Career Opportunities for History Majors
Dr. Kevorkian's Collection of Motivational Speeches
Spotted Owl Recipes by the EPA

--------------------------------------------------
Lines unique to text1:
Humen Rights Advances in Burma
"My Plan to Find the Real Killers" by OJ Simpson
"Strom Thurmond:  Intelligent Quotes"
America's Most Popular Lawyers
Different Ways to Spell "Tom"
The Engineer's Guide to Fashion
Ralph Nader's List of Pleasures
Lindsey Graham Peace Deals

--------------------------------------------------
Lines unique to text2:
Human Rights Advance in Burma
"My Plan to Find the Real Killer" by OJ Simpson
"Strom Thurmond:  Intlegigent Quotes"
America's Most Poppular Lawyers
Different Ways to Sell "Tom"
The Engineer's Guide to Passion
Ralph Nader's Lust of Pleasures
Lindsey Graham Deace Peals

"""

