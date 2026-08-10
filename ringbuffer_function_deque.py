#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''' ringbuffer_function_deque.py

Using the Python deque module as a ringbuffer,
as the buffer fills up, first entries are dropped

One way to prevent lists from overflowing your memory!

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import collections

def ringbuffer_append(item, dq=collections.deque(maxlen=3)):
    '''
    mimics a ringbuffer of length 3
    you can change maxlen to your needs    
    '''
    dq.append(item)
    return list(dq)

# testing
mylist = ringbuffer_append('red')
print(mylist)

mylist = ringbuffer_append('green')
print(mylist)

mylist = ringbuffer_append('blue')
print(mylist)

# first item will pop to make room for new item 3
mylist = ringbuffer_append('orange')
print(mylist)

mylist = ringbuffer_append('yellow')
print(mylist)

''' result...
['red']
['red', 'green']
['red', 'green', 'blue']
['green', 'blue', 'orange']
['blue', 'orange', 'yellow']
'''

print('='*40)

def ringbuffer_10(mylist, dq=collections.deque(maxlen=10)):
    '''
    mimics a ringbuffer of length 10
    you can change maxlen to your needs
    '''
    for n in mylist:
        dq.append(n)
    return list(dq)

# testing ...
mylist = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
ringbuffer = ringbuffer_10(mylist)
print(ringbuffer)
print('-'*40)

# send more data
mylist = [22, 23, 24, 25]
ringbuffer = ringbuffer_10(mylist)
print(ringbuffer)

''' result...
[12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
----------------------------------------
[16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
'''
