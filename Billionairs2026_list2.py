#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Billionairs2026_list2.py

convert the Billionairs2026.csv to a list of lists
keep the name,wealth,age,source,nation header
wealth is in US billion  e9 or 1,000,000,000

source
http://en.wikipedia.org/wiki/The_World%27s_Billionaires

vegaseat  31oct2026
'''

# mid 2026 values...
# csv text with name,wealth,age,source,nation per line
Billionairs2026_csv = '''\
Elon Musk,$839.0 billion,54,Tesla and SpaceX,USA
Larry Page,$257.0 billion,52,Google,USA
Sergey Brin,$237.0 billion,52,Google,USA
Jeff Bezos,$224.0 billion,62,Amazon,USA
Mark Zuckerberg,$222.0 billion,41,Meta Platforms,USA
Larry Ellison,$190.0 billion,81,Oracle Corporation,USA
Bernard Arnault,$171.0 billion,77,LVMH,FRANCE
Jensen Huang,$154.0 billion,63,Nvidia,USA
Warren Buffett,$149.0 billion,95,Berkshire Hathaway,USA
Amancio Ortega,$148.0 billion,89,Indite,SPAIN'''

header = "name,wealth,age,source,nation"
bill_list = []
for line in Billionairs2026_csv.split('\n'):
    #print(line.split(','))
    name, wealth, age, source, nation = line.split(',')
    bill_list.append([name, wealth, age, source, nation])

print(f"{header = }")
print('bill_list = [')
for ix, data in enumerate(bill_list):
    if ix < len(bill_list) - 1:
        print(data, end=',\n')
    else:
        print(data)
print(']') 

'''
header = 'name,wealth,age,source,nation'
bill_list = [
['Elon Musk', '$839.0 billion', '54', 'Tesla and SpaceX', 'USA'],
['Larry Page', '$257.0 billion', '52', 'Google', 'USA'],
['Sergey Brin', '$237.0 billion', '52', 'Google', 'USA'],
['Jeff Bezos', '$224.0 billion', '62', 'Amazon', 'USA'],
['Mark Zuckerberg', '$222.0 billion', '41', 'Meta Platforms', 'USA'],
['Larry Ellison', '$190.0 billion', '81', 'Oracle Corporation', 'USA'],
['Bernard Arnault', '$171.0 billion', '77', 'LVMH', 'FRANCE'],
['Jensen Huang', '$154.0 billion', '63', 'Nvidia', 'USA'],
['Warren Buffett', '$149.0 billion', '95', 'Berkshire Hathaway', 'USA'],
['Amancio Ortega', '$148.0 billion', '89', 'Indite', 'SPAIN']
]
'''

