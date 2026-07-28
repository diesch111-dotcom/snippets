#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Billionairs2026raw.py

source
http://en.wikipedia.org/wiki/The_World%27s_Billionaires

tested with LinuxMint and SublimeText IDE   vegaseat  19jul2026
"""

# adjusted to  form csv file data since tab separation does not work properly
# No.,Name,Net worth (USD),Age,Nationality,Primary source(s) of wealth
raw_data = '''\
1,Elon Musk,$839 billion,54,United States,Tesla and SpaceX
2,Larry Page,$257 billion,52,United States,Google
3,Sergey Brin,$237 billion,52,United States,Google
4,Jeff Bezos,$224 billion,62,United States,Amazon
5,Mark Zuckerberg,$222 billion,41,United States,Meta Platforms
6,Larry Ellison,$190 billion,81,United States,Oracle Corporation
7,Bernard Arnault & family,$171 billion,77,France,LVMH
8,Jensen Huang,$154 billion,63,Taiwan United States,Nvidia
9,Warren Buffett,$149 billion,95,United States,Berkshire Hathaway
10,Amancio Ortega,$148 billion,89,Spain,Indite'''


# a list of [name, wealth, age, source] lists; skip nationality
data_list = []
for line in raw_data.split('\n'):
    #print(line.split(','))
    rank, name, worth, age, country, source = line.split(',')
    #print(worth.split()[0][1:])
    wealth = "{:,.0f}".format(float(worth.split()[0][1:]) * 1e9)
    #print(wealth, type(wealth))
    data_list.append([name, wealth, age, source])

print('data_list = [')
for ix, data in enumerate(data_list):
    if ix < len(data_list) - 1:
        print(data, end=',\n')
    else:
        print(data)
print(']')    
print('-'*60)

# create a modified csv file text
print("# csv text with name,wealth,age,source per line")
csv_str = ""
for line in data_list:
    name, wealth, age, source = line
    # replace the comma in wealth with empty string
    wealth = wealth.replace(',', '')
    # reformat wealth
    wealth = "${:.1f} billion".format(float(wealth)/1e9)
    # replace the comma in source with 'and'
    source = source.replace(",", " and")
    csv_str += name+','+wealth+','+age+','+source+'\n'
    #print(name, wealth, age, source)
    temp = ",".join(line)
    #print(temp)

print(csv_str)
print('-'*60)

'''
data_list = [
['Elon Musk', '839,000,000,000', '54', 'Tesla and SpaceX'],
['Larry Page', '257,000,000,000', '52', 'Google'],
['Sergey Brin', '237,000,000,000', '52', 'Google'],
['Jeff Bezos', '224,000,000,000', '62', 'Amazon'],
['Mark Zuckerberg', '222,000,000,000', '41', 'Meta Platforms'],
['Larry Ellison', '190,000,000,000', '81', 'Oracle Corporation'],
['Bernard Arnault & family', '171,000,000,000', '77', 'LVMH'],
['Jensen Huang', '154,000,000,000', '63', 'Nvidia'],
['Warren Buffett', '149,000,000,000', '95', 'Berkshire Hathaway'],
['Amancio Ortega', '148,000,000,000', '89', 'Indite']
]
------------------------------------------------------------
# csv text with name,wealth,age,source per line
Elon Musk,$839.0 billion,54,Tesla and SpaceX
Larry Page,$257.0 billion,52,Google
Sergey Brin,$237.0 billion,52,Google
Jeff Bezos,$224.0 billion,62,Amazon
Mark Zuckerberg,$222.0 billion,41,Meta Platforms
Larry Ellison,$190.0 billion,81,Oracle Corporation
Bernard Arnault & family,$171.0 billion,77,LVMH
Jensen Huang,$154.0 billion,63,Nvidia
Warren Buffett,$149.0 billion,95,Berkshire Hathaway
Amancio Ortega,$148.0 billion,89,Indite
'''
