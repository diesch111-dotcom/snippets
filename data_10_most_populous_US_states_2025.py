#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''  data_10_most_populous_US_states_2025.py

Copied the raw data string from:
http://www.census.gov/popclock/
convert to a list of lists for processing

The United States population on July 30, 2026 was: 342,709,581

works with LinuxMint and Spyder IDE  vegaseat 15jun2026
'''

print("10 most populous US states (2025):")
# raw data is tab separated tsv
data = '''\
State	Population, 2025	Pop. per sq. mi., 2025
California	39,355,309	252.5
Texas	31,709,821	121.4
Florida	23,462,518	437.3
New York	20,002,427	424.5
Pennsylvania	13,059,432	291.9
Illinois	12,719,141	229.1
Ohio	11,900,510	291.3
Georgia	11,302,748	195.8
North Carolina	11,197,968	230.3
Michigan	10,127,844	178.9'''

# create a list of [state, population, population/sqmile] lists
data_list = []
for line in data.split('\n'):
    data_list.append(line.split('\t'))

# test
import pprint
pprint.pprint(data_list)

'''
10 most populous US states (2025):
[['State', 'Population, 2025', 'Pop. per sq. mi., 2025'],
 ['California', '39,355,309', '252.5'],
 ['Texas', '31,709,821', '121.4'],
 ['Florida', '23,462,518', '437.3'],
 ['New York', '20,002,427', '424.5'],
 ['Pennsylvania', '13,059,432', '291.9'],
 ['Illinois', '12,719,141', '229.1'],
 ['Ohio', '11,900,510', '291.3'],
 ['Georgia', '11,302,748', '195.8'],
 ['North Carolina', '11,197,968', '230.3'],
 ['Michigan', '10,127,844', '178.9']]

'''
