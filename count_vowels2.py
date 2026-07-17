''' count_vowels2.py

Using class Counter to count vowels in a text.

btw: I love to eat out in LV, hence the name vegas eat

works with LinuxMint and Spyder IDE  vegaseat  15jun2026
'''

import collections as coll

text = '''
Python? That is for children. A Klingon Warrior
uses only machine code, keyed in on the front
panel switches in raw binary.  No caps lock key here!
'''
vowels = 'aeiou'

# optional all lower case
text = text.lower()

# method most_common() sorts by most common vowel(s) first
vowels_count = coll.Counter(c for c in text if c in vowels).most_common()


print(text)
print('-'*50)
print('list of (vowel, frequency) tuples in the text:')
print(vowels_count)
print('most common:')
print(vowels_count[0])

'''
list of (vowel, frequency) tuples in the text:
[('e', 12), ('o', 10), ('i', 9), ('a', 8), ('u', 1)]
most common:
('e', 12)
'''
