''' count_vowels1.py
using class Counter to count vowels in a text


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

import collections as coll

text = '''
Python? That is for children. A Klingon Warrior
uses only machine code, keyed in on the front
panel switches in raw binary.
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
[('i', 9), ('e', 9), ('o', 8), ('a', 7), ('u', 1)]
most common:
('i', 9)
'''
