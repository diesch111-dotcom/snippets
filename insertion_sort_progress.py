#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' insertion_sort_progress.py

Follow the progress of an insertion sort
Simple code, about twice as fast as bubble sort

http://en.wikipedia.org/wiki/Insertion_sort

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        save = mylist[i]
        j = i
        while j > 0 and mylist[j - 1] > save:
            mylist[j] = mylist[j - 1]
            j -= 1
        mylist[j] = save
        # optionally show sort progress
        print(mylist)

mylist = [8, 10, 6, 7, 4, 5, 9, 1, 3, 2]
#mylist = list(range(1, 11))  # test an already sorted list
insertion_sort(mylist)
print('-'*32)
print(mylist)

''' result...
[8, 10, 6, 7, 4, 5, 9, 1, 3, 2]
[6, 8, 10, 7, 4, 5, 9, 1, 3, 2]
[6, 7, 8, 10, 4, 5, 9, 1, 3, 2]
[4, 6, 7, 8, 10, 5, 9, 1, 3, 2]
[4, 5, 6, 7, 8, 10, 9, 1, 3, 2]
[4, 5, 6, 7, 8, 9, 10, 1, 3, 2]
[1, 4, 5, 6, 7, 8, 9, 10, 3, 2]
[1, 3, 4, 5, 6, 7, 8, 9, 10, 2]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
--------------------------------
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

# extra

def insertion_sort2(items):
    ''' simplified code '''
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            # swap
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
            