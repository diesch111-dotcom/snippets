#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' re_methods102.py

Explore the Python regular expression 're' module methods

https://docs.python.org/3/library/re.html

Methods:
match() Determine if the RE matches at the beginning of the string. 
search() Scan through a string, looking for any location where this RE matches. 
findall() Find all substrings where the RE matches, and returns them as a list. 
finditer() Find all substrings where the RE matches, and returns them as an 
    iterator. 
split() Split the string into a list, splitting it wherever the RE matches 
sub() Find all substrings where the RE matches, and replace them with a 
    different string 
subn() Does the same thing as sub(), but returns the new string and the 
    number of replacements 

group() Return the string matched by the RE 
start() Return the starting position of the match 
end() Return the ending position of the match 
span() Return a tuple containing the (start, end) positions of the match 
purge() Clear the regular expression cache

text  Match literal text
.     Match any character except newline
^     Match the start of a string, in MULTILINE mode each line
$     Match the end of a string, in MULTILINE mode each line
*     Match 0 or more repetitions
+     Match 1 or more repetitions
?     Match 0 or 1 repetitions
*?    Match 0 or more, few as possible
+?    Match 1 or more, few as possible
{n}   Match n repetitions, eg. a{3}b match 'aaab' only
{m,n} Match m to n repetitions, eg. a{3,5}b match 3 to 5 a before b
{m,n}? Match m to n repetitions, few as possible
[...] Match a set of characters, eg. [a-z] match all lower case char
[^...] Match characters not in set
A | B Match A or B
(...) Match regex in parenthesis as a group

\number Matches text matched by previous group
\A Matches start of string
\b Matches empty string at beginning or end of word
\B Matches empty string not at begin or end of word
\d Matches any decimal digit [0-9]
\D Matches any non-digit [^0-9]
\s Matches any whitespace [\t\n\r\f\v]
\S Matches any non-whitespace
\w Matches any alphanumeric character [a-zA-Z0-9_] 
\W Matches characters not in \w
\Z Match at end of string.
\\ Literal backslash

Flags for compile():
re.MULTILINE (or re.M) string and each line
re.DOTALL (or re.S) match any character, including a newline
re.IGNORECASE (or re.I) case-insensitive matching
re.VERBOSE or re.X allows for whitespace and comments
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)

IDLE usually comes with Python install, to gain access...
...might have to install the IDLE IDE, in the Linux terminal use:
sudo apt update
sudo apt install idle3
...once installed this way, it shows up under 'Programming' as IDLE

the Spyder IDE chokes on re.split(r"[,;\-\s]", text) backslashes, so use IDLE
tested with IDLE IDE on LinuxMint  vegaseat 19jul2026
'''

import re

# get a list of the math methods
# excluding the "dunder" (__) ones
myre = re
print("re object methods:")
for item in dir(myre):
    if not item.startswith('_'):
        print(item)

'''
re object methods:
A
ASCII
DEBUG
DOTALL
I
IGNORECASE
L
LOCALE
M
MULTILINE
Match
NOFLAG
Pattern
RegexFlag
S
Scanner
T
TEMPLATE
U
UNICODE
VERBOSE
X
compile
copyreg
enum
error
escape
findall
finditer
fullmatch
functools
match
purge
search
split
sub
subn
template
'''

# more info on individual re methods ...
print('-'*15)

help(re.compile)
help(re.findall)
help(re.sub)
help(re.subn)


'''
Help on function compile in module re:

compile(pattern, flags=0)
    Compile a regular expression pattern, returning a Pattern object.

Help on function findall in module re:

findall(pattern, string, flags=0)
    Return a list of all non-overlapping matches in the string.
    
    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.
    
    Empty matches are included in the result.

Help on function sub in module re:

sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used.

Help on function subn in module re:

subn(pattern, repl, string, count=0, flags=0)
    Return a 2-tuple containing (new_string, number).
    new_string is the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in the source
    string by the replacement repl.  number is the number of
    substitutions that were made. repl can be either a string or a
    callable; if a string, backslash escapes in it are processed.
    If it is a callable, it's passed the Match object and must
    return a replacement string to be used.
'''

print('re.findall() finditer() span()'.center(60, '-'))

print('find integer or float numbers in a string:')
data_raw = "5kg cost $45.99"
print(data_raw)
# '\d+\.\d+' finds floating point values, can use '[0-9]*\.[0-9]*' 
# '|\d+' or integer values 
data_list = re.findall(r'\d+\.\d+|\d+', data_raw)
print(data_list)

'''
find integer or float numbers in a string:
5kg cost $45.99
['5', '45.99']
'''

print("="*40)

# show all the (start, end) indexes of all occurances of a search string:
# re.IGNORECASE (or re.I) case-insensitive matching
rc = re.compile("what", re.IGNORECASE)
print("find (start, end) indexes of 'what' in text:")
text2 = "What is this, you are asking me, what you are doing"
print(text2)
for ix in rc.finditer(text2):
    print(ix.span())
    
'''
find (start, end) indexes of 'what' in text:
What is this, you are asking me, what you are doing
(0, 4)
(33, 37)
'''

print("="*40)

str2 = 'set width=20 and height=10'
print(str2)
print(re.findall(r'(\w+)=(\d+)', str2))
'''
set width=20 and height=10
[('width', '20'), ('height', '10')]
'''

print('re.sub() and re.subn()'.center(60, '-'))

print( 'sub() vowels in a string with *:')
vowels = 'aeiouAEIOU'
# a precompiled pattern will speed up re.sub()
p = re.compile(r'[aeiouAEIOU]')
str2 = 'statecontrol'
print('{} -> {}'.format(str2, p.sub('*', 'statecontrol')))

'''
sub() vowels in a string with *:
statecontrol -> st*t*c*ntr*l
'''

print("="*40)

print('remove punctuation marks:')
word1 = "hello! to my home?"
print(word1)
# a precompiled pattern will speed up sub()
punctuation = re.compile(r'[.?!,":;]')
word2 = punctuation.sub("", word1)
print(word2)

'''
remove punctuation marks:
hello! to my home?
hello to my home
'''

print("="*40)

print('multiple substitution:')
print("sub 'blue' or 'white' or 'red' with word 'color':")
# re.IGNORECASE (or re.I) case-insensitive matching
p = re.compile('(blue|white|red)', re.IGNORECASE)
text1 = 'Blue socks and red shoes'
print(text1)
s = p.sub('color', text1)
print(s)

'''
multiple substitution:
sub 'blue' or 'white' or 'red' with word 'color':
Blue socks and red shoes
color socks and color shoes
'''

print("="*40)

# subn() makes n substitutions from left to right
# similar to sub(), but returns a tuple 
# first element is the new string, 
# second element is the number of substitions made
# subn(replacement, targetstring [,count] )
#p = re.compile( '(blue|white|red)')
s = p.subn('color', text1, 1)
print(s)
# default is all ...
s = p.subn( 'color', text1)
print(s)

'''
('color socks and red shoes', 1)
('color socks and color shoes', 2)
'''

print('re.match()'.center(60, '-'))

# search() is simpler than match()
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))

'''
Isaac Newton
'''

print(m.group(1))

'''
Isaac
'''

print(m.group(2))

'''
Newton
'''

print(m.group(1, 2))
'''
('Isaac', 'Newton')
'''

print('re.search()'.center(60, '-'))

# with parentheses you can pull out individual parts of a match:
str1 = str(type(1))
print(str1)
# compile a regex pattern:
# a precompiled pattern will speed up searches!
p = re.compile(r"'(.*)'")
print(p.search(str1).group())   # 'int'
print(p.search(str1).group(1))  # int

'''
<class 'int'>
'int'
int
'''
print("="*40)

print('The search() function returns a Match object:')
txt = "The rain in Spain"
x = re.search("pain", txt)
# show row of index numbers
print('012345678901234567890')
# show the txt
print(x.string)
# show the onject
print(x)
# show the (start, end) index end is exclusive
print(f"string 'pain' is at index (start, end) = {x.span()}")

'''
The search() function returns a Match object:
012345678901234567890    
The rain in Spain
<re.Match object; span=(13, 17), match='pain'>
string 'pain' is at index (start, end) = (13, 17)
'''

print('re.split()'.center(60, '-'))

text = "apple,banana;orange-grape pineapple"
# Split by comma, semicolon, hyphen, or space
result = re.split(r"[,;\-\s]", text)
print(result)

'''
['apple', 'banana', 'orange', 'grape', 'pineapple']
'''


