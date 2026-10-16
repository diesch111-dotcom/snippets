#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' data_in_bins2.py

Put data into bins/buckets (integer numbered),
via collections.defaultdict(list)
then retrieve them by bin/bucket number

vegaseat  15joct2026
'''

import collections
import pprint

# (value, suggested/floor bin number)
data = ((5.639792, 1.36),
        (4.844813, 1.89),
        (4.809105, 2.33),
        (3.954150, 2.69),
        (2.924234, 3.42),
        (1.532669, 4.50),
        (0.007777, 5.63))

bucket = collections.defaultdict(list)
for each in data:
    bucket[int((each[1]))].append(each[0])

dict_bucket = dict(bucket)
pprint.pprint(dict_bucket)

'''
{1: [5.639792, 4.844813],
 2: [4.809105, 3.95415],
 3: [2.924234],
 4: [1.532669],
 5: [0.007777]}
'''

print('-'*25)

value = dict_bucket[1][0]
print(f"bucket #1 {value = }")  # bucket #1 value = 5.639792
